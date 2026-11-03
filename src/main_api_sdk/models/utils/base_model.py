from pydantic import (
    AfterValidator,
    BaseModel as PydanticBaseModel,
    ConfigDict,
    ValidationError,
)
from typing import Any, Dict


def _unique_key(item: Any) -> Any:
    """
    The value an item is compared BY when deciding uniqueness.

    JSON Schema compares by JSON value, and ``boolean`` is a distinct JSON type from ``number``,
    so ``[1, true]`` holds two items. Python disagrees -- ``True == 1`` and ``hash(True) ==
    hash(1)`` -- so a boolean is tagged with its type to keep it apart from the number that equals
    it. Numbers are deliberately NOT tagged: the spec calls two numbers equal when they have the
    same mathematical value, which is what ``1 == 1.0`` already does, so tagging every item by
    ``type(item)`` would start ACCEPTING ``[1, 1.0]``.

    :param item: One item of the sequence being checked.
    :return: The item, or a type-tagged wrapper when the item is a boolean.
    :rtype: Any
    """
    return ("bool", item) if isinstance(item, bool) else item


def reject_duplicate_items(value: Any) -> Any:
    """
    Enforce JSON Schema ``uniqueItems`` on a sequence.

    Pydantic v2 removed v1's ``unique_items`` and has no Field kwarg for it, so the constraint is
    carried as ``Annotated`` metadata instead. Raising ``ValueError`` (rather than returning a
    flag) is what lets pydantic report the failure as part of the surrounding ``ValidationError``,
    the same way every other constraint on the model does.

    A ``set`` settles the all-hashable case in one pass. An UNHASHABLE item -- a nested model, a
    list, a dict -- makes ``set()`` raise ``TypeError``, so that case falls back to comparing each
    item against the ones already seen with ``==``. The fallback is quadratic, but it is the only
    way to compare unhashable items at all, and it now runs only for the arrays that need it
    rather than for every response array.

    Both passes compare :func:`_unique_key` of an item rather than the item, because ``True in
    [1]`` is True for the same reason the set collapses them. Booleans nested INSIDE an item are
    still beyond reach (``{"a": True} == {"a": 1}`` in Python), but a top-level mixed array is the
    shape a spec actually produces.

    :param value: The already-coerced sequence.
    :return: The same value, unchanged, when every item is distinct.
    :rtype: Any
    :raises ValueError: When two items compare equal.
    """
    if not isinstance(value, (list, tuple)):
        return value

    keys = [_unique_key(item) for item in value]

    try:
        if len(set(keys)) != len(keys):
            raise ValueError("items must be unique")
        return value
    except TypeError:
        pass

    seen: list = []
    for key in keys:
        if key in seen:
            raise ValueError("items must be unique")
        seen.append(key)

    return value


UniqueItems = AfterValidator(reject_duplicate_items)


def _deep_union(defaults: Any, explicit: Any) -> Any:
    """
    Merge two dumps of the same model, with ``explicit`` winning at every depth.

    A shallow merge would replace a whole nested dict with the caller's version and lose any
    default the nested model filled in for itself, so nested dicts and lists are walked.
    """
    if isinstance(defaults, dict) and isinstance(explicit, dict):
        merged = dict(defaults)
        for key, value in explicit.items():
            merged[key] = _deep_union(merged[key], value) if key in merged else value
        return merged

    if (
        isinstance(defaults, list)
        and isinstance(explicit, list)
        and len(defaults) == len(explicit)
    ):
        return [_deep_union(item, other) for item, other in zip(defaults, explicit)]

    return explicit


class BaseModel(PydanticBaseModel):
    """
    Pydantic-based model for SDK objects with custom configuration.

    This class extends Pydantic's BaseModel to provide:
    - Automatic validation on instantiation
    - Type-safe attribute access
    - JSON serialization with API field name mapping
    - Support for additional properties (extra fields)
    """

    model_config = ConfigDict(
        # Allow extra fields beyond defined properties (replaces **kwargs behavior)
        extra="allow",
        # Validate field values when they are assigned after initialization
        validate_assignment=True,
        # Use enum values instead of enum objects in serialization
        use_enum_values=True,
        # Allow models to be populated using either field name or alias
        populate_by_name=True,
        # Arbitrary types allowed (for flexibility with custom types)
        arbitrary_types_allowed=False,
        # Validate `Field(pattern=...)` constraints with Python's `re` engine
        # instead of Pydantic's default Rust `regex` engine. The Rust engine
        # rejects ALL look-around (`(?=…)`, `(?!…)`, `(?<=…)`, `(?<!…)`) with
        # `SchemaError: regex parse error … look-around … is not supported`,
        # crashing model import. OpenAPI `pattern`s frequently use look-ahead;
        # Python's `re` supports it. Patterns are already normalised for `re`
        # compatibility by translateRegexForPython at generation time.
        regex_engine="python-re",
    )

    def model_dump_original(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Serialize model using original field names from OpenAPI spec.

        This ensures JSON output matches the API contract by using field aliases
        (typically camelCase) instead of Python field names (snake_case).

        By default, unset fields are excluded from the output.
        To include them, pass exclude_unset=False explicitly.

        :param kwargs: Additional arguments passed to model_dump()
        :return: Dictionary with original API field names
        :rtype: Dict[str, Any]

        Example:
            >>> cat = Cat(body_fat_percentage=15.5, age=None)
            >>> cat.model_dump_original()
            {'bodyFatPercentage': 15.5, 'age': None}
            >>> cat.model_dump_original(exclude_unset=False)
            {'bodyFatPercentage': 15.5, 'age': None}
        """
        # Set exclude_unset=True by default to exclude fields that were not explicitly set
        # Note: We do NOT exclude None values by default, because if a field is explicitly
        # set to None, it should be sent as null in the JSON to the API
        if "exclude_unset" not in kwargs:
            kwargs["exclude_unset"] = True

        # Exclude extra fields by default (additional properties not in schema)
        # This matches the expected behavior where undefined fields are not sent to APIs
        result = self.model_dump(by_alias=True, **kwargs)

        # A field carrying a non-None default is part of the contract even when the caller never
        # assigned it -- a discriminator the SDK fills in still has to reach the wire. The second
        # dump keeps those, and the union is deep so a nested model's own defaults survive too;
        # `result` stays authoritative for everything the caller did set, including explicit None.
        if kwargs["exclude_unset"]:
            defaulted = self.model_dump(
                by_alias=True,
                **{**kwargs, "exclude_unset": False, "exclude_none": True},
            )
            result = _deep_union(defaulted, result)

        # Remove extra fields from the result
        extra_fields = getattr(self, "__pydantic_extra__", {})
        if extra_fields:
            for extra_field_name in extra_fields.keys():
                result.pop(extra_field_name, None)

        return result

    @classmethod
    def model_validate_original(cls, obj: Any) -> "BaseModel":
        """
        Parse and validate object using original field names from OpenAPI spec.

        This method accepts data with API field names (aliases) and creates
        a validated model instance.

        :param obj: Dictionary or object to validate
        :return: Validated model instance
        :rtype: BaseModel

        Example:
            >>> data = {'bodyFatPercentage': 15.5}
            >>> cat = Cat.model_validate_original(data)
            >>> cat.body_fat_percentage
            15.5
        """
        return cls.model_validate(obj)

    def _map(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Legacy alias for model_dump_original() for backward compatibility.

        :param kwargs: Additional arguments passed to model_dump_original()
        :return: Dictionary with original API field names
        :rtype: Dict[str, Any]
        """
        return self.model_dump_original(**kwargs)

    @classmethod
    def _unmap(cls, obj: Any) -> "BaseModel":
        """
        Legacy alias for model_validate_original() for backward compatibility.

        :param obj: Dictionary or object to validate
        :return: Validated model instance
        :rtype: BaseModel
        """
        return cls.model_validate_original(obj)

    @property
    def _kwargs(self) -> Dict[str, Any]:
        """
        Access extra fields (additional properties beyond defined schema).

        In Pydantic v2, extra fields are stored in __pydantic_extra__.
        This property provides backward compatibility with v1's **kwargs pattern.

        :return: Dictionary of extra fields
        :rtype: Dict[str, Any]
        """
        return getattr(self, "__pydantic_extra__", {})

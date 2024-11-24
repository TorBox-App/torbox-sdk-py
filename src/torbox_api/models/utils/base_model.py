import re
import operator
from typing import List, Union, Type, Any, TypeVar, Optional
from enum import Enum
from .one_of_base_model import OneOfBaseModel

T = TypeVar("T")


class BaseModel:
    """
    A base class that most of the models in the SDK inherited from.
    """

    def __init__(self):
        pass

    def _define_object(self, input_data: Any, input_class: Type[T]) -> Optional[T]:
        """
        Check if the input data is an instance of the input class and return the input data if it is.
        Otherwise, return an instance of the input class.

        :param input_data: The input data to be checked.
        :param input_class: The class that the input data should be an instance of.
        :return: The input data if it is an instance of input_class, otherwise an instance of input_class.
        :rtype: object
        """
        if input_data is None:
            return None
        elif isinstance(input_data, input_class):
            return input_data
        else:
            return input_class._unmap(input_data)

    def _define_list(
        self, input_data: Optional[List[Any]], list_class: Type[T]
    ) -> Optional[List[T]]:
        """
        Create a list of instances of a specified class from input data.
        :param input_data: The input data to be transformed into a list of instances.
        :param list_class: The class that each instance in the list should be an instance of.
        :return: A list of instances of list_class.
        :rtype: list
        """

        if input_data is None:
            return None

        result: List[T] = []
        for item in input_data:
            if hasattr(list_class, "__args__") and len(list_class.__args__) > 0:
                class_list = self.__create_class_map(list_class)
                OneOfBaseModel.class_list = class_list
                result.append(OneOfBaseModel.return_one_of(item))
            elif issubclass(list_class, Enum):
                result.append(
                    self._enum_matching(item, list_class.list(), list_class.__name__)
                )
            elif isinstance(item, list_class):
                result.append(item)
            elif isinstance(item, dict):
                result.append(list_class._unmap(item))
            else:
                result.append(list_class(item))
        return result

    def _define_str(
        self,
        variable_name: str,
        value: Optional[Any],
        nullable=False,
        pattern: Optional[str] = None,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
    ) -> Optional[str]:
        """
        Check if a string value is within the specified boundaries and matches a regex pattern.
        Return the value if it is, otherwise raise a ValueError.

        :param variable_name: The variable name.
        :type variable_name: str
        :param value: The value to be checked.
        :type value: str
        :param nullable: Whether the value can be None.
        :type nullable: bool
        :param pattern: The regex pattern to match.
        :type pattern: str
        :param min_length: The minimum length of the value.
        :type min_length: int
        :param max_length: The maximum length of the value.
        :type max_length: int
        :param inclusive_lenght_boundary: Whether the length boundaries are inclusive.
        :type inclusive_lenght_boundary: bool

        :raises ValueError: If the value is not within the boundaries or does not match the pattern.

        :return: The value if it is within the boundaries and matches the pattern.
        :rtype: str
        """
        if value is None and not nullable:
            raise ValueError(f"{variable_name} cannot be null.")
        if value is None:
            return None

        if pattern:
            self._pattern_matching(value, pattern, variable_name)

        if min_length is not None:
            operation = operator.ge
            self._boundary_check(variable_name, len(value), min_length, operation, str)

        if max_length is not None:
            operation = operator.le
            self._boundary_check(variable_name, len(value), max_length, operation, str)

        return value

    def _define_number(
        self,
        variable_name: str,
        value: Optional[Union[float, int]],
        nullable=False,
        ge: Optional[Union[float, int]] = None,
        gt: Optional[Union[float, int]] = None,
        le: Optional[Union[float, int]] = None,
        lt: Optional[Union[float, int]] = None,
    ) -> Optional[Union[float, int]]:
        """
        Check if a number value is within the specified boundaries.
        Return the value if it is, otherwise raise a ValueError.

        :param variable_name: The variable name.
        :type variable_name: str
        :param value: The value to be checked.
        :type value: Union[float, int]
        :param nullable: Whether the value can be None.
        :type nullable: bool
        :param ge: The minimum value of the number (inclusive). The value must be greater than or equal to this.
        :type ge: Union[float, int]
        :param gt: The minimum value of the number (exclusive). The value must be greater than this.
        :type gt: Union[float, int]
        :param le: The maximum value of the number (inclusive). The value must be less than or equal to this.
        :type le: Union[float, int]
        :param lt: The maximum value of the number (exclusive). The value must be less than this.
        :type lt: Union[float, int]

        :raises ValueError: If the value is not within the boundaries.

        :return: The value if it is within the boundaries.
        :rtype: Union[float, int]
        """
        if value is None and not nullable:
            raise ValueError(f"{variable_name} cannot be null.")

        if value is None:
            return None

        if ge is not None:
            operation = operator.ge
            self._boundary_check(variable_name, value, ge, operation, float)

        if gt is not None:
            operation = operator.gt
            self._boundary_check(variable_name, value, gt, operation, float)

        if le is not None:
            operation = operator.le
            self._boundary_check(variable_name, value, le, operation, float)

        if lt is not None:
            operation = operator.lt
            self._boundary_check(variable_name, value, lt, operation, float)

        return value

    def _boundary_check(
        self,
        variable_name: str,
        value: float,
        boundary: float,
        operation: operator,
        value_type: Union[str, float, int],
    ) -> Optional[str]:
        """
        Checks if a value is within the specified boundaries and returns the value if it is.

        :param variable_name: The variable name.
        :type variable_name: str
        :param value: The value to be checked.
        :type value: Union[str, float, int]
        :param boundary: The boundary value to be checked against.
        :type boundary: float
        :param operator: The operator to be used for the boundary check.
        :type operator: operator
        :param type: The type of the value.
        :type type: Union[str, float, int]

        :raises ValueError: If the value is not within the boundaries.

        :return: The value if it is within the boundaries.
        :rtype: Union[str, float, int]
        """
        reference = "length" if value_type is str else "value"
        if not operation(value, boundary):
            raise ValueError(
                f"Invalid {reference} for {variable_name}: must satisfy the condition {operation.__name__} {boundary}, received {value}"
            )

        return value

    def _pattern_matching(
        self, value: Optional[str], pattern: str, variable_name: str
    ) -> Optional[str]:
        """
        Checks if a value matches a regex pattern and returns the value if there's a match.

        :param value: The value to be checked.
        :type value: str
        :param pattern: The regex pattern.
        :type pattern: str
        :param variable_name: The variable name.
        :type variable_name: str
        :return: The value if it matches the pattern.
        :rtype: str
        :raises ValueError: If the value does not match the pattern.
        """
        if value is None:
            return None

        if re.match(r"{}".format(pattern), value):
            return value
        else:
            raise ValueError(
                f"Invalid value for {variable_name}: must match {pattern}, received {value}"
            )

    def _enum_matching(
        self, value: Union[str, Enum], enum_values: List[str], variable_name: str
    ) -> Union[str, Enum]:
        """
        Checks if a value (str or enum) matches the required enum values and returns the value if there's a match.

        :param value: The value to be checked.
        :type value: Union[str, Enum]
        :param enum_values: The list of valid enum values.
        :type enum_values: List[str]
        :param variable_name: The variable name.
        :type variable_name: str
        :return: The value if it matches one of the enum values.
        :rtype: Union[str, Enum]
        :raises ValueError: If the value does not match any of the enum values.
        """
        if value is None:
            return None

        str_value = value.value if isinstance(value, Enum) else value
        if str_value in enum_values:
            return value
        else:
            raise ValueError(
                f"Invalid value for {variable_name}: must match one of {enum_values}, received {value}"
            )

    def _get_representation(self, level: int = 0) -> str:
        """
        Get a string representation of the model.

        :param int level: The indentation level.
        :return: A string representation of the model.
        """
        indent = "    " * level
        representation_lines = []

        for attr, value in vars(self).items():
            if value is not None:
                value_representation = (
                    value._get_representation(level + 1)
                    if hasattr(value, "_get_representation")
                    else repr(value)
                )
                representation_lines.append(
                    f"{indent}    {attr}={value_representation}"
                )

        return (
            f"{self.__class__.__name__}(\n"
            + ",\n".join(representation_lines)
            + f"\n{indent})"
        )

    def __str__(self):
        return self._get_representation()

    def __repr__(self):
        return self._get_representation()

    def __create_class_map(self, union_type):
        """
        Create a dictionary that maps class names to the actual classes in a Union type.

        :param union_type: The Union type to create a class map for.
        :return: A dictionary mapping class names to classes.
        :rtype: dict
        """
        class_map = {}
        for arg in union_type.__args__:
            if arg.__name__:
                class_map[arg.__name__] = arg
        return class_map

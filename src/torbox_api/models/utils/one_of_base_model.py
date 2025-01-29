from typing import Any, List, Dict, Optional, Union, Type, TypeVar, get_origin, get_args

T = TypeVar("T")


class OneOfBaseModel:
    """
    A base class for handling 'oneOf' models where multiple class constructors are available,
    and the appropriate one is determined based on the input data.

    :ivar dict class_list: A dictionary mapping class names to their constructors.
    """

    class_list = {}

    @classmethod
    def return_one_of(cls, input_data: Optional[Any]) -> Optional[Any]:
        """
        Attempts to initialize an instance of one of the classes in the class_list
        based on the provided input data.

        :param input_data: Input data used for initialization.
        :return: An instance of one of the classes specified.
        :rtype: object
        :raises ValueError: If no class can be initialized with the provided input data,
            or if optional parameters don't match the input data.
        """
        if input_data is None:
            return None

        if isinstance(input_data, (str, float, int, bool)):
            return input_data

        exception_list = []
        success_list = []
        for class_constructor in cls.class_list.values():
            try:
                instance = cls._get_instance(class_constructor, input_data)
                if instance is not None:
                    success_list.append(instance)
            except Exception as e:
                exception_list.append({"class": class_constructor, "exception": e})

        if success_list:
            return max(success_list, key=cls._count_non_none_attributes)

        cls._raise_one_of_error(exception_list)

    @classmethod
    def _count_non_none_attributes(cls, instance):
        """
        Count the number of non-None attributes in the instance.

        :param instance: The instance to check.
        :return: The number of non-None attributes.
        """
        if not hasattr(instance, "_map"):
            return 0
        return len([value for value in instance._map().values() if value is not None])

    @classmethod
    def _get_instance(cls, class_constructor, input_data):
        """
        Return an instance of the class based on the input data.

        :param class_constructor: The constructor of the class to check against.
        :param
        :return: An instance of the class if the input data matches the class constructor
            or can be used to initialize the class, None otherwise.
        """
        # Check if the class is only a TypeHint.
        origin = get_origin(class_constructor)
        if origin is not None and isinstance(input_data, list):
            list_instance = cls._get_list_instance(
                input_data, class_constructor, origin
            )
            if list_instance is not None:
                return list_instance
            else:
                return None

        # Check if the input_data is already an instance of the class
        if isinstance(input_data, class_constructor):
            return input_data

        # Check if the input_data is a dictionary that can be used to initialize the class
        elif isinstance(input_data, dict):
            return class_constructor._unmap(input_data)

    @classmethod
    def _get_list_instance(
        cls, input_data: List[Any], class_constructor: Type[T], origin: Type[Any]
    ) -> Union[List[T], List[Any], None]:
        """
        Return the list of elements for a given class constructor and origin type.

        :param input_data: The input data to check.
        :param class_constructor: The constructor of the class to check against.
        :param origin: The origin type to check against.
        :return: The input data if all elements are instances of the type specified in the class_constructor,
            or a new list with each item unmapped.
        """
        args = get_args(class_constructor)
        has_single_arg = args and len(args) == 1

        if not isinstance(input_data, origin) or not has_single_arg:
            return None

        inner_type = args[0]

        if not all(isinstance(item, inner_type) for item in input_data):
            return [inner_type._unmap(item) for item in input_data]

        return input_data

    @classmethod
    def _raise_one_of_error(cls, exception_list):
        """
        Raises a ValueError with the appropriate error message for one of models.

        :param exception_list: List of exceptions that occurred.
        :type exception_list: list
        :raises ValueError: If input data does not match any of the models.
        """
        if not exception_list:
            return
        exception_messages = "\n".join(
            f"Class: {exception['class']}, Exception: {exception['exception']}"
            for exception in exception_list
        )
        raise ValueError(
            f"Input data must match one of the models: {list(cls.class_list.keys())}"
            f"Errors occurred:\n{exception_messages}"
        )

"""
Defines the SENTINEL object to be used to represent a nullable value.
"""

from typing import Any

SENTINEL = object()


def was_value_set(value: Any) -> bool:
    """Returns True if the value was set, False otherwise.

    :param value: The value to check.
    :type value: Any
    :return: True if the value was set, False otherwise.
    """
    return value is not SENTINEL

from typing import Dict

from .base_header import BaseHeader


class AccessTokenAuth(BaseHeader):
    """
    A class for handling Access token authentication in headers.

    :ivar str _token_prefix: The prefix for the token in the header.
    :ivar str token_value: The value of the token.
    """

    _token_prefix = "Bearer"

    def __init__(self, token_value: str):
        """
        Initialize the AccessTokenAuth instance.

        :param token_value: The value of the token.
        :type token_value: str
        """
        self.token_value = token_value

    def set_value(self, value: str) -> None:
        """
        Set the value of the token.

        :param value: The new value of the token.
        :type value: str
        """
        self.token_value = value

    def get_headers(self) -> Dict[str, str]:
        """
        Get the headers with the Authorization field set to the Access token.

        :return: A dictionary with the Authorization field set to the Access token.
        :rtype: Dict[str, str]
        """
        return {"Authorization": f"{self._token_prefix} {self.token_value}"}

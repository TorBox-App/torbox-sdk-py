from .response import Response
from typing import Optional


class ApiError(Exception):
    """
    Class representing an API Error.

    :ivar Optional[int] status: The status code of the HTTP error.
    :ivar Optional[Response] response: The response associated with the error.
    """

    def __init__(
        self,
        message: Optional[str] = None,
        status: Optional[int] = None,
        response: Optional[Response] = None,
    ):
        """
        Initialize a new instance of API Error.

        :param Optional[int] status: The status code of the HTTP error.
        :param Optional[Response] response: The response associated with the error.
        """
        self.message = message
        self.status = status
        self.response = response
        super().__init__(message)

    def __str__(self) -> str:
        parts = []
        if self.status is not None:
            parts.append(f"status={self.status}")
        if self.message:
            parts.append(self.message)
        return ": ".join(parts)


class ApiTimeoutError(ApiError):
    """
    Raised when a request does not complete within its timeout.

    A timeout used to be reported as ``ApiError("Request timed out", status=408)``, which no
    endpoint maps and no error class is named for, so it was indistinguishable by type from any
    other unmapped-status failure — a caller had to string-match the message to tell "the server
    answered 408" apart from "we never got an answer" (FSDK-1585).

    NO status code is carried. The 408 was synthetic: nothing on the wire said 408, and inventing
    one is what made the failure look like a response. ``status`` and ``status_code`` are therefore
    ``None``, and code that branches on them must handle that.

    Subclasses ApiError, so an existing broad ``except ApiError`` still catches it.

    :ivar Optional[Exception] cause: The underlying transport exception, when one was available.
    """

    def __init__(
        self, message: str = "Request timed out", cause: Optional[Exception] = None
    ):
        """
        Initialize a new instance of ApiTimeoutError.

        :param str message: A description of the failure.
        :param Optional[Exception] cause: The transport exception this wraps.
        """
        self.cause = cause
        super().__init__(message=message)


class ApiConnectionError(ApiError):
    """
    Raised when a request never reaches the server: connection refused, DNS failure, TLS failure.

    The transport's own ``requests.ConnectionError`` used to escape the handler chain unwrapped, so
    catching it meant importing ``requests`` in the caller's own code — the SDK leaked its HTTP
    library to everyone who wanted to handle an unreachable server (FSDK-1573).

    NO status code is carried, for the same reason as ApiTimeoutError: there was no response, so
    there is no status to report and inventing one would make the failure look like an answer.

    Subclasses ApiError, so an existing broad ``except ApiError`` catches it. That is a deliberate
    widening: ApiError previously implied a response had been received.

    :ivar Optional[Exception] cause: The underlying transport exception, when one was available.
    """

    def __init__(
        self, message: str = "Connection failed", cause: Optional[Exception] = None
    ):
        """
        Initialize a new instance of ApiConnectionError.

        :param str message: A description of the failure.
        :param Optional[Exception] cause: The transport exception this wraps.
        """
        self.cause = cause
        super().__init__(message=message)

import random

from typing import Generator, Optional, Tuple
from time import sleep
from .base_handler import BaseHandler
from ...transport.request import Request
from ...transport.response import Response
from ...transport.request_error import RequestError


class RetryHandler(BaseHandler):
    """
    Handler for retrying requests.
    Retries the request if the previous handler in the chain returned an error or a response with a status code of 500 or higher.

    :ivar int _max_attempts: The maximum number of retry attempts.
    :ivar int _delay_in_milliseconds: The delay between retry attempts in milliseconds.
    """

    def __init__(self):
        """
        Initialize a new instance of RetryHandler.
        """
        super().__init__()
        self._max_attempts = 3
        self._delay_in_milliseconds = 150

    def handle(
        self, request: Request
    ) -> Tuple[Optional[Response], Optional[RequestError]]:
        """
        Retry the request if the response has a status code greater or equal to 500 or equal to 408 (timeout).

        :param Request request: The request to retry.
        :return: The response and any error that occurred.
        :rtype: Tuple[Optional[Response], Optional[RequestError]]
        :raises RequestError: If the handler chain is incomplete.
        """
        if self._next_handler is None:
            raise RequestError("Handler chain is incomplete")

        response, error = self._next_handler.handle(request)

        try_count = 0
        while try_count < self._max_attempts and self._should_retry(error):
            self._delay(try_count)
            response, error = self._next_handler.handle(request)
            try_count += 1

        return response, error

    def stream(
        self, request: Request
    ) -> Generator[Tuple[Optional[Response], Optional[RequestError]], None, None]:
        """
        Retry the request if the response has a status code greater or equal to 500 or equal to 408 (timeout).

        :param Request request: The request to retry.
        :return: The response and any error that occurred.
        :rtype: Generator[Tuple[Optional[Response], Optional[RequestError]], None, None]
        :raises RequestError: If the handler chain is incomplete.
        """
        if self._next_handler is None:
            raise RequestError("Handler chain is incomplete")

        try:
            try_count = 0
            stream = self._next_handler.stream(request)
            while True:
                response, error = next(stream)
                if try_count < self._max_attempts and self._should_retry(error):
                    self._delay(try_count)
                    try_count += 1
                    stream = self._next_handler.stream(request)  # Retry the request
                elif try_count >= self._max_attempts:
                    yield response, error
                    break
                else:
                    yield response, error

        except StopIteration:
            pass

    def _delay(self, try_count: int) -> None:
        jitter = random.uniform(0.5, 1.5)
        delay = self._delay_in_milliseconds * (2**try_count) * jitter / 1000
        sleep(delay)

    def _should_retry(self, error: Optional[RequestError]) -> bool:
        """
        Determine whether the request should be retried.

        :param Optional[Response] response: The response from the previous handler.
        :param Optional[RequestError] error: The error from the previous handler.
        :return: True if the request should be retried, False otherwise.
        :rtype: bool
        """
        if not error:
            return False
        return error.status == 408 or error.status >= 500

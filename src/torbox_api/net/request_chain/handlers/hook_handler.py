from typing import Generator, Optional, Tuple


from .base_handler import BaseHandler
from ....hooks.hook import CustomHook
from ...transport.request import Request
from ...transport.response import Response
from ...transport.request_error import RequestError


class HookHandler(BaseHandler):
    """
    Handler for calling hooks.

    :ivar Hook _hook: The hook to be called. This is a placeholder and should be replaced with an instance of the actual hook class.
    """

    def __init__(self):
        """
        Initialize a new instance of HookHandler.
        """
        super().__init__()
        self._hook = CustomHook()

    def handle(
        self, request: Request
    ) -> Tuple[Optional[Response], Optional[RequestError]]:
        """
        Call the beforeRequest hook before passing the request to the next handler in the chain.
        Call the afterResponse hook after receiving a response from the next handler in the chain.
        Call the onError hook if an error occurs in the next handler in the chain.

        :param Request request: The request to handle.
        :return: The response and any error that occurred.
        :rtype: Tuple[Optional[Response], Optional[RequestError]]
        """
        if self._next_handler is None:
            raise RequestError("Handler chain is incomplete")

        self._hook.before_request(request)
        response, error = self._next_handler.handle(request)
        self._handle_response(request, response, error)

        return response, error

    def stream(
        self, request: Request
    ) -> Generator[Tuple[Optional[Response], Optional[RequestError]], None, None]:
        """
        Call the beforeRequest hook before passing the request to the next handler in the chain.
        Call the afterResponse hook after receiving a response from the next handler in the chain.
        Call the onError hook if an error occurs in the next handler in the chain.

        :param Request request: The request to handle.
        :return: The response and any error that occurred.
        :rtype: Generator[Tuple[Optional[Response], Optional[RequestError]], None, None]
        """
        if self._next_handler is None:
            raise RequestError("Handler chain is incomplete")

        self._hook.before_request(request)
        for response, error in self._next_handler.stream(request):
            self._handle_response(request, response, error)
            yield response, error

    def _handle_response(
        self, request: Request, response: Response, error: RequestError
    ):
        if error is not None and error.is_http_error:
            self._hook.on_error(error, request, error.response)
        else:
            self._hook.after_response(request, response)

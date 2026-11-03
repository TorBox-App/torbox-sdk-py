import json
import requests
from enum import Enum

# Aliased rather than imported under its own name: `requests.exceptions.ConnectionError` would
# shadow the Python builtin of the same name for the whole module.
from requests.exceptions import ConnectionError as RequestsConnectionError, Timeout
from typing import Generator, Optional, Tuple
from pydantic import TypeAdapter
from .base_handler import BaseHandler
from ...transport.request import Request
from ...transport.response import Response
from ...transport.api_error import ApiConnectionError, ApiError, ApiTimeoutError


class HttpHandler(BaseHandler):
    """
    Handler for making HTTP requests.
    This handler sends the request to the specified URL and returns the response.

    :ivar int _timeout_in_seconds: The timeout for the HTTP request in seconds.
    """

    def __init__(self, timeout=60, http_client=None, follow_redirects=True):
        """
        Initialize a new instance of HttpHandler.

        :param http_client: An optional caller-supplied requests.Session used as-is (the SDK
            never reconfigures its transport). Falls back to the module-level `requests.request`
            when not provided.
        :param follow_redirects: Whether HTTP redirects (3xx responses) are followed
            automatically. `requests` follows them unconditionally otherwise, with no other way
            to opt out.
        """
        super().__init__()
        self._timeout_in_seconds = timeout
        self._http_client = http_client
        self._follow_redirects = follow_redirects

    def _request(self, method, url, **kwargs):
        """
        Dispatch a single HTTP request through the injected client, if any, otherwise through
        the module-level `requests.request`.
        """
        kwargs.setdefault("allow_redirects", self._follow_redirects)
        if self._http_client is not None:
            return self._http_client.request(method, url, **kwargs)
        return requests.request(method, url, **kwargs)

    def handle(
        self, request: Request
    ) -> Tuple[Optional[Response], Optional[Exception]]:
        """
        Send the request to the specified URL and return the response.

        :param Request request: The request to send.
        :return: The response and any error that occurred.
        :rtype: Tuple[Optional[Response], Optional[Exception]]
        """
        try:
            request_args = self._get_request_data(request)

            # Get timeout from config if available, otherwise use default
            timeout = self._get_timeout_from_config(request)

            result = self._request(
                request.method,
                request.url,
                headers=request.headers,
                timeout=timeout,
                **request_args,
            )
            response = Response(result)

            if response.status >= 400:
                if response.status in request.errors and isinstance(
                    response.body, dict
                ):
                    error_model_class = request.errors[response.status]
                    if isinstance(error_model_class, TypeAdapter):
                        # TypeAdapter for anyOf/oneOf union type errors: parse into the correct variant
                        try:
                            parsed_body = error_model_class.validate_python(
                                response.body
                            )
                        except Exception:
                            parsed_body = response.body
                        message = response.body.get("message")
                        if not isinstance(message, str):
                            message = (
                                f"{response.status} error in request to: {request.url}"
                            )
                        error = ApiError(
                            message=message,
                            status=response.status,
                            response=response,
                        )
                        error.body = parsed_body
                        return None, error
                    error = error_model_class(**response.body)
                    if "message" not in response.body:
                        error.message = (
                            f"{response.status} error in request to: {request.url}"
                        )
                    error.status = response.status
                    error.response = response

                    return None, error

                return None, ApiError(
                    message=f"{response.status} error in request to: {request.url}",
                    status=response.status,
                    response=response,
                )

            return response, None
        # FSDK-1585: a timeout is its own type, carrying no status. It used to be reported as
        # `ApiError("Request timed out", status=408)` — but nothing on the wire said 408, no
        # endpoint maps it, and no error class is named for it, so the failure was
        # indistinguishable by type from any other unmapped status. Dropping the synthetic status
        # is the fix, not a side effect of it.
        except Timeout as error:
            return None, ApiTimeoutError(f"Request timed out: {error}", cause=error)
        # FSDK-1573: a connection-level failure — refused, DNS, TLS — used to escape this handler
        # entirely, so a caller had to import `requests` to catch it and the SDK's abstraction
        # leaked its HTTP library. MUST stay below `except Timeout`: ConnectTimeout inherits from
        # both ConnectionError and Timeout, and a connect timeout is a timeout.
        except RequestsConnectionError as error:
            return None, ApiConnectionError(
                f"Connection to {request.url} failed: {error}", cause=error
            )

    def stream(
        self, request: Request
    ) -> Generator[Tuple[Optional[Response], Optional[Exception]], None, None]:
        """
        Stream the request to the specified URL and yield response chunks.
        Useful for handling large responses or server-sent events.

        :param request: The request to stream.
        :return: A generator yielding response chunks and any errors that occurred.
        """
        try:
            request_args = self._get_request_data(request)

            # Get timeout from config if available, otherwise use default
            timeout = self._get_timeout_from_config(request)

            result = self._request(
                request.method,
                request.url,
                headers=request.headers,
                timeout=timeout,
                stream=True,
                **request_args,
            )

            if result.status_code >= 400:
                response = Response(result)
                yield (
                    None,
                    ApiError(
                        message=f"{response.status} error in request to: {request.url}",
                        status=response.status,
                        response=response,
                    ),
                )

            else:
                yield from self._stream_chunks(result)

        # FSDK-1585: the streaming path gets the same typed timeout as `handle`, so a caller does
        # not have to catch two different things depending on which method it called.
        except Timeout as error:
            yield None, ApiTimeoutError(f"Request timed out: {error}", cause=error)
        # Same ordering constraint as `handle`, for the same reason.
        except RequestsConnectionError as error:
            yield (
                None,
                ApiConnectionError(
                    f"Connection to {request.url} failed: {error}", cause=error
                ),
            )

    def _get_request_data(self, request: Request) -> dict:
        """
        Get the request arguments based on the request headers and data.

        :param Request request: The request object.
        :return: The request arguments.
        :rtype: dict
        """
        headers = request.headers or {}

        # No body was set on the request (the operation declares no requestBody).
        # Sending an empty JSON payload would force a Content-Type the endpoint
        # never advertises, which strict servers reject with HTTP 415.
        if request.body is None:
            return {}

        data = request.body or {}
        content_type = headers.get("Content-Type", "application/json")

        if request.method == "GET" and not data:
            return {}

        # Raw binary bodies (e.g. application/octet-stream, file uploads) must be
        # sent as-is. Routing them through `json=` crashes with
        # "TypeError: Object of type bytes is not JSON serializable", regardless
        # of what Content-Type the request defaulted to.
        if isinstance(data, (bytes, bytearray)):
            return {"data": data}

        # The JSON family includes `text/json`, exactly as it does on the response side. This
        # tested `application/` only, so a declared `text/json` request body fell through to the
        # form-urlencoded branch below and went out as `data=payload` under a `text/json`
        # Content-Type — a body that matched neither its declared media type nor its schema
        # (FSDK-1571). Mirrors `isApplicationJson` in `src/generate/common/content-types.ts`.
        # `requests` only defaults the Content-Type header when one is not already set, so routing
        # through `json=` does not rewrite the declared `text/json`.
        if (
            content_type.startswith(("application/", "text/"))
            and "json" in content_type
        ):
            return {"json": data}

        if "multipart/form-data" in content_type:
            headers.pop("Content-Type", None)
            # `files` is a LIST of (field, part) pairs, not a dict: an array of files repeats one
            # field name, which a dict cannot hold. Collapsing it into `data` left `files` empty,
            # so requests form-urlencoded the whole body -- including the bytes (FSDK-1479).
            files, form_data = [], {}
            for key, value in data.items():
                if isinstance(value, (bytes, bytearray, memoryview)):
                    files.append((key, (key, value, "application/octet-stream")))
                elif self._is_file_array(value):
                    for item in value:
                        files.append((key, (key, item, "application/octet-stream")))
                elif value is not None:
                    form_data[key] = self._form_value(value)
            if not files and form_data:
                # requests only builds a multipart body when `files` is non-empty
                for key, value in form_data.items():
                    for item in value if isinstance(value, (list, tuple)) else [value]:
                        if item is not None:
                            files.append(
                                (
                                    key,
                                    (
                                        None,
                                        item
                                        if isinstance(item, (str, bytes))
                                        else str(item),
                                    ),
                                )
                            )
                form_data = {}
            return {"files": files, "data": form_data}

        return {"data": data}

    @classmethod
    def _form_value(cls, value):
        if isinstance(value, bool):
            return "true" if value else "false"
        if isinstance(value, (list, tuple)):
            return [cls._form_value(item) for item in value if item is not None]
        if isinstance(value, Enum):
            return cls._form_value(value.value)
        if isinstance(value, dict):
            return json.dumps(value)
        return value

    @staticmethod
    def _stream_chunks(result):
        if "json" not in result.headers.get("Content-Type", "").lower():
            for chunk in result.iter_content(chunk_size=8192):
                for response in Response.from_chunk(result, chunk):
                    yield response, None
            return
        buffer = b""
        for chunk in result.iter_content(chunk_size=8192):
            buffer += chunk
            *lines, buffer = buffer.split(b"\n")
            for line in lines:
                if HttpHandler._is_json_stream_payload(line):
                    for response in Response.from_chunk(result, line):
                        yield response, None
        if HttpHandler._is_json_stream_payload(buffer):
            for response in Response.from_chunk(result, buffer):
                yield response, None

    @staticmethod
    def _is_json_stream_payload(line: bytes) -> bool:
        stripped = line.strip()
        return bool(stripped) and not stripped.startswith(
            (b":", b"id:", b"retry:", b"event:")
        )

    @staticmethod
    def _is_file_array(value) -> bool:
        """
        Whether a multipart field holds an array of files rather than form values.

        Requires EVERY element to be bytes-like: an array of primitives is a repeated form field,
        and requests already encodes a list value that way. The accepted types match the scalar
        file branch above, so a bytearray/memoryview of file content cannot fall through to form
        data.

        :param value: The value of a single multipart field.
        :return: True when the value is a non-empty sequence of bytes-like objects.
        :rtype: bool
        """
        return (
            isinstance(value, (list, tuple))
            and len(value) > 0
            and all(isinstance(item, (bytes, bytearray, memoryview)) for item in value)
        )

    def _get_timeout_from_config(self, request: Request) -> float:
        """
        Get the timeout for the request from config or use default.

        :param Request request: The request object.
        :return: The timeout in seconds.
        :rtype: float
        """
        if request.config and "timeout" in request.config:
            return request.config["timeout"]
        return self._timeout_in_seconds

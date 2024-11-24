import json
import re
from typing import Generator, Optional, Union
from requests import Response as RequestsResponse
from urllib.parse import parse_qs


class Response:
    """
    A simple HTTP response wrapper class using the requests library.

    :ivar int status: The status code of the HTTP response.
    :ivar dict headers: The headers of the HTTP response.
    :ivar str body: The body of the HTTP response.
    :var str chunk: The chunk of the HTTP response.
    """

    def __init__(
        self,
        response: RequestsResponse,
        chunk: Optional[str] = None,
        raw_chunk: Optional[bytes] = None,
    ) -> None:
        """
        Initializes a Response object.

        :param RequestsResponse response: The requests.Response object.
        """
        self.status = response.status_code
        self.headers = response.headers

        self.body = self._parse_response_body(
            content_type=response.headers.get("Content-Type", "").lower(),
            body=chunk if chunk else response.text,
            raw_body=raw_chunk if raw_chunk else response.content,
        )

    @staticmethod
    def from_chunk(
        response: RequestsResponse, raw_chunk: bytes
    ) -> Generator["Response", None, None]:
        """
        Create a Response object from a chunk of data.

        :param RequestsResponse response: The requests.Response object.
        :param bytes chunk: The chunk of data.
        :return: A Response object.
        :rtype: Response
        """
        content_type = response.headers.get("Content-Type", "").lower()
        chunk_str = raw_chunk.decode()
        if "text/event-stream" not in content_type:
            yield Response(response, chunk=chunk_str, raw_chunk=raw_chunk)
        else:
            for chunk_line in chunk_str.split("\n"):
                if "data: " in chunk_line:
                    yield Response(response, chunk=chunk_line, raw_chunk=raw_chunk)

    def __str__(self) -> str:
        """
        Return a string representation of the Response object.

        :return: A string representation of the Response object.
        :rtype: str
        """
        return (
            f"Response(status={self.status}, headers={self.headers}, body={self.body})"
        )

    def _parse_response_body(
        self, content_type: str, body: str, raw_body: bytes
    ) -> Union[str, dict, bytes]:
        """
        Extracts the response body from a given HTTP response.

        This method attempts to parse the response body based on its content type.
        If the content type is JSON, it tries to parse the body as JSON.
        If the content type is text or XML, it returns the raw text.
        If the content type is 'application/x-www-form-urlencoded', it parses the body as a query string.
        For all other content types, it returns the raw binary content.

        :param RequestsResponse response: The HTTP response received from a request.
        :return: The parsed response body.
        :rtype: str or dict or bytes
        """
        try:
            if re.search(r"application\/.*json", content_type):
                return json.loads(body)

            if "text/event-stream" in content_type and "data: " in body:
                json_body = body[6:]
                # Note: this assumes that the content of data is a valid JSON string
                return json.loads(json_body)

            if "text/" in content_type or content_type == "application/xml":
                return body

            if content_type == "application/x-www-form-urlencoded":
                parsed_response = parse_qs(body)
                return {k: v[0] for k, v in parsed_response.items()}

            return raw_body

        except json.JSONDecodeError:
            return raw_body

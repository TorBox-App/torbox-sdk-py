import json
from typing import Generator, Optional, Union
from requests import Response
from urllib.parse import parse_qs


class Response:
    """
    A simple HTTP response wrapper class using the requests library.

    :ivar int status: The status code of the HTTP response.
    :ivar dict headers: The headers of the HTTP response.
    :ivar str body: The body of the HTTP response.
    :var str chunk: The chunk of the HTTP response.
    :property Response raw: The original requests.Response object.
    """

    def __init__(
        self,
        response: Response,
        chunk: Optional[str] = None,
        raw_chunk: Optional[bytes] = None,
    ) -> None:
        """
        Initializes a Response object.

        :param Response response: The Response object.
        """
        self._raw_response = response
        self.status = response.status_code
        self.headers = response.headers

        # `media_type`, so the PARSE decision is made on the same normalised value as the generated
        # branch SELECTION (FSDK-1571). With the raw header here and a normalised one there, an
        # `application/xml; charset=utf-8` response would match its branch and then arrive as raw
        # bytes, because the equality tests below never saw past the parameter -- a silently wrong
        # type in place of the error it used to raise.
        # A streamed chunk is identified by `raw_chunk`, not by a truthy `chunk`: a BINARY chunk has
        # no text form at all (see `_chunk_text`), and falling back to `response.text` for it would
        # re-read a body whose stream has already been consumed.
        is_chunk = raw_chunk is not None
        self.body = self._parse_response_body(
            content_type=self.media_type,
            body=(chunk or "") if is_chunk else response.text,
            raw_body=raw_chunk if is_chunk else response.content,
        )

    @staticmethod
    def from_chunk(
        response: Response, raw_chunk: bytes
    ) -> Generator["Response", None, None]:
        """
        Create a Response object from a chunk of data.

        :param Response response: The Response object.
        :param bytes chunk: The chunk of data.
        :return: A Response object.
        :rtype: Response
        """
        content_type = response.headers.get("Content-Type", "").lower()
        if "text/event-stream" not in content_type:
            yield Response(
                response,
                chunk=Response._chunk_text(content_type, raw_chunk),
                raw_chunk=raw_chunk,
            )
        else:
            for chunk_line in raw_chunk.decode().split("\n"):
                if "data: " in chunk_line:
                    yield Response(response, chunk=chunk_line, raw_chunk=raw_chunk)

    @staticmethod
    def _chunk_text(content_type: str, raw_chunk: bytes) -> str:
        """
        The text form of one streamed chunk, or ``""`` when the body is not textual.

        Every chunk used to be UTF-8 decoded unconditionally, which raised ``UnicodeDecodeError``
        on the first MP3 frame of an ``audio/mpeg`` stream (``ff fb 90 00``) -- so a binary stream
        could not be read at all, while an ASCII test payload passed. ``_parse_response_body``
        returns the RAW bytes for exactly the content types excluded here, so for those the text
        form is never read; it was only ever computed, eagerly.

        The classification mirrors ``_parse_response_body``'s own branches, which are the authority
        on whether the text form is the body.

        :param str content_type: The response's ``Content-Type`` header, lowercased.
        :param bytes raw_chunk: The chunk of data.
        :return: The decoded chunk, or an empty string for a binary body.
        :rtype: str
        """
        media_type = content_type.split(";", 1)[0].strip()
        is_textual = (
            media_type.startswith("text/")
            or (
                media_type.startswith("application/")
                and ("json" in media_type or "xml" in media_type)
            )
            or media_type
            in ("application/javascript", "application/x-www-form-urlencoded")
        )
        if not is_textual:
            return ""
        return raw_chunk.decode()

    def __str__(self) -> str:
        """
        Return a string representation of the Response object.

        :return: A string representation of the Response object.
        :rtype: str
        """
        return (
            f"Response(status={self.status}, headers={self.headers}, body={self.body})"
        )

    @property
    def raw(self) -> Response:
        """
        Get the underlying requests.Response object.

        :return: The original requests.Response object.
        :rtype: Response
        """
        return self._raw_response

    @property
    def media_type(self) -> str:
        """
        The response's media type, lowercased and WITHOUT its parameters.

        ``Content-Type: text/json; charset=utf-8`` is the same media type as ``text/json``, but an
        endpoint declaring more than one success media type selects its branch by comparing this
        against the exact media type the spec declared. Leaving the parameters attached made every
        charset-annotated response miss its branch and fall through to
        ``raise ApiError("Error on deserializing the response.")`` — the SDK rejecting a response
        that matched its own spec (FSDK-1571). Only multi-media-type endpoints emit that
        comparison, which is why it went unnoticed.

        Kept separate from ``headers`` so a caller that wants the header verbatim, parameters and
        all, still has it.

        :return: The media type, e.g. ``text/json``.
        :rtype: str
        """
        return self.headers.get("Content-Type", "").split(";", 1)[0].strip().lower()

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

        :param str content_type: The response's MEDIA TYPE -- lowercased, parameters already
            stripped (see ``media_type``). Several branches below test it for equality, so a
            ``; charset=utf-8`` suffix would make them miss.
        :param str body: The text body of the response.
        :param bytes raw_body: The raw binary body of the response.
        :return: The parsed response body.
        :rtype: str or dict or bytes
        """
        try:
            # JSON IS CHECKED BEFORE TEXT, and the JSON family includes `text/json`.
            #
            # The old pattern was `application/.*json`, which matched only the `application/`
            # family — so a declared `text/json` response fell through to the `text/` branch below
            # and came back as a `str`, and the generated `Model.model_validate(response)` then
            # raised ValidationError inside the SDK (FSDK-1571). Ordering matters for the same
            # reason: `text/json` satisfies the `text/` test too, so a text-first check would keep
            # returning the unparsed string.
            #
            # This mirrors `isApplicationJson` in `src/generate/common/content-types.ts`, which is
            # the generation-time authority on the same question (and already correct); the runtime
            # has to make the decision again because it sees the media type the SERVER actually
            # sent, so the two have to agree.
            if (
                content_type.startswith(("application/", "text/"))
                and "json" in content_type
            ):
                return json.loads(body)

            if "text/event-stream" in content_type and "data: " in body:
                json_body = body[6:]
                # Note: this assumes that the content of data is a valid JSON string
                return json.loads(json_body)

            # The whole `application/*xml*` family, not just `application/xml`: an
            # `application/soap+xml` or `application/atom+xml` body is textual for the same reason,
            # and the generated type for it is `str` (see `getContentTypeDefinition`), so an
            # equality test returned raw bytes under a `str` annotation.
            if (
                "text/" in content_type
                or (content_type.startswith("application/") and "xml" in content_type)
                or content_type == "application/javascript"
            ):
                return body

            if content_type == "application/x-www-form-urlencoded":
                parsed_response = parse_qs(body)
                return {k: v[0] for k, v in parsed_response.items()}

            return raw_body

        except json.JSONDecodeError:
            return raw_body

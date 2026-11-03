import logging
import requests
from typing import Any, Dict, Optional, Tuple, Generator, Union, TYPE_CHECKING
from enum import Enum

from .default_headers import DefaultHeaders, DefaultHeadersKeys

from ...net.headers.base_header import BaseHeader

from ...net.transport.request import Request
from ...net.request_chain.request_chain import RequestChain
from ...net.request_chain.handlers.http_handler import HttpHandler
from ...net.headers.access_token_auth import AccessTokenAuth
from ...net.request_chain.handlers.retry_handler import RetryHandler
from ...net.request_chain.handlers.logging_handler import LoggingHandler

if TYPE_CHECKING:
    from ...net.sdk_config import SdkConfig, RetryConfig
    from ...net.environment import Environment


class BaseService:
    """
    A base class for services providing common functionality.

    :ivar str base_url: The base URL for the service.
    :ivar dict _default_headers: A dictionary of default headers.
    """

    def __init__(
        self,
        base_url: str,
        http_client: Optional[requests.Session] = None,
        follow_redirects: bool = True,
        logger: Optional[logging.Logger] = None,
    ) -> None:
        """
        Initializes a BaseService instance.

        :param base_url: The base URL for the service, as a string or an Environment enum member. Defaults to None.
        """
        self.base_url = self._normalize_base_url(base_url)
        self._default_headers = DefaultHeaders()
        self._timeout = 60
        self._http_client = http_client
        self._follow_redirects = follow_redirects
        self._logger = logger
        self._service_config: "SdkConfig" = {}

        self._update_request_handler()

    def set_access_token(self, access_token: str):
        """
        Sets the access token for the service.
        """
        self._default_headers.set_header(
            DefaultHeadersKeys.ACCESS_AUTH, AccessTokenAuth(access_token)
        )

        return self

    def get_access_token(
        self, resolved_config: Optional["SdkConfig"] = None
    ) -> BaseHeader:
        """
        Get the access auth header, with optional config overrides.

        :param SdkConfig resolved_config: Optional resolved configuration for overrides.
        :return: The access auth header.
        :rtype: BaseHeader
        """
        if resolved_config and (
            "token" in resolved_config or "access_token" in resolved_config
        ):
            token = resolved_config.get("token") or resolved_config.get("access_token")
            return AccessTokenAuth(token)
        return self._default_headers.get_header(DefaultHeadersKeys.ACCESS_AUTH)

    def set_timeout(self, timeout: float):
        """
        Sets the timeout for the service.

        :param float timeout: The timeout (in seconds) to be set.
        :return: The service instance.
        """
        self._timeout = timeout
        self._update_request_handler()

        return self

    def set_http_client(self, http_client: Optional[requests.Session]):
        """
        Sets a custom HTTP client for the service.

        :param http_client: A requests.Session-compatible client, used as-is (the SDK never
            reconfigures its transport). Pass None to fall back to the module-level requests API.
        :return: The service instance.
        """
        self._http_client = http_client
        self._update_request_handler()

        return self

    def set_follow_redirects(self, follow_redirects: bool):
        """
        Sets whether HTTP redirects (3xx responses) are followed automatically.

        :param bool follow_redirects: False to return a 3xx response as-is instead of following it.
        :return: The service instance.
        """
        self._follow_redirects = follow_redirects
        self._update_request_handler()

        return self

    def set_logging(self, logger: Optional[logging.Logger]):
        """
        Sets the logger requests/responses are written to.

        :param logger: A standard library logger. Pass None (the default) to disable logging.
            Authorization and Cookie header values are always redacted from logged output.
        :return: The service instance.
        """
        self._logger = logger
        self._update_request_handler()

        return self

    def set_base_url(self, base_url: Union["Environment", str]):
        """
        Sets the base URL for the service.

        :param base_url: The base URL to be set, as a string or an Environment enum member.
        """
        self.base_url = self._normalize_base_url(base_url)

        return self

    @staticmethod
    def _normalize_base_url(base_url: Union["Environment", str, None]) -> Optional[str]:
        """
        Coerces a base URL to its string form. SdkConfig documents `base_url` as either a URL
        string or an Environment enum member, so every entry point that assigns `self.base_url`
        has to accept both or the setter and the constructor disagree on the property's type.

        :param base_url: A URL string, an Environment enum member, or None.
        :return: The URL without a trailing slash, or the input unchanged when it is empty.
        :rtype: Optional[str]
        """
        if not base_url:
            return base_url

        resolved = base_url.value if isinstance(base_url, Enum) else base_url
        return resolved.rstrip("/")

    def _resolve_base_url(
        self, resolved_config: Optional["SdkConfig"] = None
    ) -> Optional[str]:
        """
        Resolves the base URL for a single request: a scoped `base_url`, then the service's own
        base URL, then a scoped `environment`. Each accepts a string or an Environment enum member.

        `self.base_url` MUST come before `environment`. The generator delivers an operation-level
        server through `resolved_config['environment']`, so ordering `environment` first makes an
        operation default shadow the base URL a caller passed to the constructor or `set_base_url`
        -- which silently sent every request to the wrong host.

        :param SdkConfig resolved_config: Optional resolved configuration for overrides.
        :return: The base URL to send the request to, or None when no source supplies one.
        :rtype: Optional[str]
        """
        config = resolved_config or {}

        return (
            self._normalize_base_url(config.get("base_url"))
            or self.base_url
            or self._normalize_base_url(config.get("environment"))
        )

    def set_config(self, config: "SdkConfig"):
        """
        Sets service-level configuration that applies to all methods in this service.

        :param SdkConfig config: Configuration dictionary to override SDK-level defaults.
        :return: The service instance for method chaining.
        """
        self._service_config = config
        return self

    def set_retry(self, retry: "RetryConfig"):
        """
        Sets the service-level retry configuration, merging it into any existing config.

        Routed through `set_config` rather than assigning `_service_config` directly, so that
        `set_config` stays the single place service-level configuration is written. A nested-layout
        client overrides `set_config` to reach its already-built resource clients, and going
        through it means retry reaches them too.

        :param RetryConfig retry: The retry configuration to be set.
        :return: The service instance for method chaining.
        """
        return self.set_config(
            self._deep_merge(self._service_config or {}, {"retry": retry})
        )

    @staticmethod
    def _deep_merge(base: dict, override: dict) -> dict:
        """
        Recursively merges two dictionaries. Nested dicts are merged key-by-key so
        that a partial override (e.g. ``{"retry": {"attempts": 5}}``) only overwrites
        the keys it specifies instead of replacing the entire nested dict.

        Every dict value from ``override`` is recursed into (creating a fresh dict),
        so override sources are never shared by reference in the result. Unoverridden
        nested values from ``base`` are shallow-copied at the top level via ``dict(base)``;
        configs are consumed read-only downstream so this is intentional.

        :param dict base: The base dictionary.
        :param dict override: Values to merge on top of base.
        :return: A new merged dictionary.
        :rtype: dict
        """
        merged = dict(base)
        for key, value in override.items():
            if isinstance(value, dict):
                base_node = merged.get(key)
                merged[key] = BaseService._deep_merge(
                    base_node if isinstance(base_node, dict) else {}, value
                )
            else:
                merged[key] = value
        return merged

    def _get_resolved_config(
        self, method_config: "SdkConfig" = None, request_config: "SdkConfig" = None
    ) -> "SdkConfig":
        """
        Resolves configuration overrides from the hierarchy: request_config > method_config > service_config.
        Merges override configs into a single dictionary using deep merge so that partial
        overrides for nested dicts (e.g. ``retry``) only replace the specified keys.
        SDK defaults are used as fallbacks where these overrides are not provided.

        :param SdkConfig method_config: Method-level configuration override.
        :param SdkConfig request_config: Request-level configuration override.
        :return: Merged configuration with all overrides applied.
        :rtype: SdkConfig
        """
        resolved: "SdkConfig" = {}

        # Apply service config
        if self._service_config:
            resolved = BaseService._deep_merge(resolved, self._service_config)

        # Apply method config
        if method_config:
            resolved = BaseService._deep_merge(resolved, method_config)

        # Apply request config
        if request_config:
            resolved = BaseService._deep_merge(resolved, request_config)

        return resolved

    def send_request(self, request: Request) -> Tuple[Dict, int, str]:
        """
        Sends the given request.

        :param Request request: The request to be sent.
        :return: The response data.
        :rtype: Tuple[Dict, int, str]
        """
        response = self._request_handler.send(request)
        self._last_response = response
        # `media_type`, not the raw header: the generated success branch compares this against the
        # exact media type the spec declared, so a `; charset=utf-8` suffix used to make a response
        # miss its own branch (FSDK-1571). The verbatim header is still on `response.headers`.
        return (
            response.body,
            response.status,
            response.media_type,
        )

    def stream_request(self, request: Request) -> Generator[Dict, None, None]:
        """
        Streams the given request.

        :param Request request: The request to be streamed.
        :return: A generator of the response data.
        :rtype: Generator[Dict, None, None]
        """
        for response in self._request_handler.stream(request):
            # Same media-type normalisation as `send_request`, so a streaming method's branch
            # selection cannot disagree with a non-streaming one (FSDK-1571).
            yield (
                response.body,
                response.status,
                response.media_type,
            )

    def get_default_headers(self) -> list:
        """
        Get the default headers.

        :return: A list of the default headers.
        :rtype: list
        """
        return self._default_headers.get_headers()

    def _get_request_handler(self) -> RequestChain:
        """
        Get the request chain.

        :return: The request chain.
        :rtype: RequestChain
        """
        return (
            RequestChain()
            .add_handler(RetryHandler())
            .add_handler(LoggingHandler(self._logger))
            .add_handler(
                HttpHandler(self._timeout, self._http_client, self._follow_redirects)
            )
        )

    def _update_request_handler(self) -> None:
        """
        Update the request handler.
        """
        self._request_handler = self._get_request_handler()

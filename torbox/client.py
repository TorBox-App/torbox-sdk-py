# Hand-written layer of the TorBox Python SDK (sdk-config/overlays/python). Not generated.
"""High-level TorBox client: unwraps the {success, error, detail, data} envelope, raises TorBoxError, retries
429/503 with Retry-After, applies a default timeout and fills in the `token` query parameter of download links.

    from torbox import TorBox
    client = TorBox(api_key="...")
    me = client.user.get_user_data()          # -> the `data` of the answer
"""
from __future__ import annotations

import inspect
import json
from typing import Any, Callable, Iterator, Optional

from urllib3.util.retry import Retry

from torbox.api_client import ApiClient
from torbox.configuration import Configuration
from torbox.exceptions import ApiException
from torbox.api.assistant_api import AssistantApi
from torbox.api.general_api import GeneralApi
from torbox.api.integrations_api import IntegrationsApi
from torbox.api.notifications_api import NotificationsApi
from torbox.api.queued_api import QueuedApi
from torbox.api.rss_api import RssApi
from torbox.api.stream_api import StreamApi
from torbox.api.tags_api import TagsApi
from torbox.api.torrents_api import TorrentsApi
from torbox.api.usenet_api import UsenetApi
from torbox.api.user_api import UserApi
from torbox.api.vendors_api import VendorsApi
from torbox.api.web_downloads_api import WebDownloadsApi

DEFAULT_BASE_URL = "https://api.torbox.app"
RETRY_STATUSES = (429, 503)


class TorBoxError(Exception):
    """An answer with success=false or an error status. `error` is the stable code (e.g. BAD_TOKEN), `detail`
    the message for people, `status` the HTTP status (None when a 200 answer said success=false)."""

    def __init__(self, status: Optional[int], error: Optional[str], detail: str, data: Any = None, headers: Any = None):
        super().__init__(f"{status or ''} {error or ''}: {detail}".strip())
        self.status = status
        self.error = error
        self.detail = detail
        self.data = data
        self.headers = headers

    @classmethod
    def from_api_exception(cls, exc: ApiException) -> "TorBoxError":
        envelope: dict = {}
        try:
            envelope = json.loads(exc.body or "{}")
        except (TypeError, ValueError):
            pass
        if not isinstance(envelope, dict):
            envelope = {}
        detail = envelope.get("detail")
        if isinstance(detail, list):  # FastAPI 422 validation errors are {"detail": [...]}, not the envelope
            return cls(exc.status, "VALIDATION_ERROR", "; ".join(str(d.get("msg", d)) for d in detail), detail, exc.headers)
        return cls(exc.status, envelope.get("error"), detail or str(exc.reason or ""), envelope.get("data"), exc.headers)


def _unwrap(result: Any) -> Any:
    success = getattr(result, "success", None)
    if success is None and isinstance(result, dict):
        success = result.get("success")
    if success is None:
        return result  # not an envelope (files, RSS, redirects)
    get = (lambda k: getattr(result, k, None)) if not isinstance(result, dict) else result.get
    if success is False:
        raise TorBoxError(None, get("error"), get("detail") or "", get("data"))
    return get("data")


class _Group:
    """Wraps one generated API class: same method names and arguments, returns `data`, raises TorBoxError."""

    def __init__(self, api: Any, client: "TorBox"):
        self._api = api
        self._client = client

    def __getattr__(self, name: str) -> Callable[..., Any]:
        method = getattr(self._api, name)
        if name.startswith("_") or not callable(method):
            return method
        params = inspect.signature(method).parameters

        def call(*args: Any, **kwargs: Any) -> Any:
            if "token" in params and kwargs.get("token") is None and len(args) == 0:
                kwargs["token"] = self._client.api_key  # download links take the key as ?token=
            kwargs.setdefault("_request_timeout", self._client.timeout)
            try:
                result = method(*args, **kwargs)
            except ApiException as exc:
                raise TorBoxError.from_api_exception(exc) from None
            return result if name.endswith(("_with_http_info", "_without_preload_content")) else _unwrap(result)

        call.__name__ = name
        call.__doc__ = method.__doc__
        return call

    def __dir__(self) -> list:
        return [n for n in dir(self._api) if not n.startswith("_")]


class TorBox:
    """The TorBox API. One attribute per API group: torrents, usenet, web_downloads, user, general, notifications,
    rss, integrations, queued, stream, tags, assistant, vendors."""

    def __init__(
        self,
        api_key: str,
        *,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = 30.0,
        max_retries: int = 3,
        backoff_factor: float = 0.5,
    ):
        if not api_key:
            raise ValueError("api_key is required (https://torbox.app/settings)")
        self.api_key = api_key
        self.timeout = timeout
        config = Configuration(host=base_url.rstrip("/"), access_token=api_key)
        # 429 and 503 mean "try again": urllib3 waits for Retry-After, or backs off exponentially
        config.retries = Retry(
            total=max_retries,
            status_forcelist=RETRY_STATUSES,
            allowed_methods=None,
            backoff_factor=backoff_factor,
            respect_retry_after_header=True,
            raise_on_status=False,
        )
        self.api_client = ApiClient(config)
        self.api_client.user_agent = "torbox-python/9.3.1.20261125.4"
        self.torrents = _Group(TorrentsApi(self.api_client), self)
        self.usenet = _Group(UsenetApi(self.api_client), self)
        self.web_downloads = _Group(WebDownloadsApi(self.api_client), self)
        self.user = _Group(UserApi(self.api_client), self)
        self.general = _Group(GeneralApi(self.api_client), self)
        self.notifications = _Group(NotificationsApi(self.api_client), self)
        self.rss = _Group(RssApi(self.api_client), self)
        self.integrations = _Group(IntegrationsApi(self.api_client), self)
        self.queued = _Group(QueuedApi(self.api_client), self)
        self.stream = _Group(StreamApi(self.api_client), self)
        self.tags = _Group(TagsApi(self.api_client), self)
        self.assistant = _Group(AssistantApi(self.api_client), self)
        self.vendors = _Group(VendorsApi(self.api_client), self)

    def paginate(self, method: Callable[..., Any], *, page_size: int = 1000, **kwargs: Any) -> Iterator[Any]:
        """Yields every item of a list endpoint that takes offset/limit, e.g.
        `for t in client.paginate(client.torrents.get_torrent_list, page_size=100): ...`"""
        offset = 0
        while True:
            page = method(offset=offset, limit=page_size, **kwargs) or []
            yield from page
            if len(page) < page_size:
                return
            offset += page_size

    def close(self) -> None:
        self.api_client.close() if hasattr(self.api_client, "close") else None

    def __enter__(self) -> "TorBox":
        return self

    def __exit__(self, *exc: Any) -> None:
        self.close()

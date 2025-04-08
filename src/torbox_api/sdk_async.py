from typing import Union
from .net.environment import Environment
from .sdk import TorboxApi
from .services.async_.torrents import TorrentsServiceAsync
from .services.async_.usenet import UsenetServiceAsync
from .services.async_.web_downloads_debrid import WebDownloadsDebridServiceAsync
from .services.async_.general import GeneralServiceAsync
from .services.async_.notifications import NotificationsServiceAsync
from .services.async_.user import UserServiceAsync
from .services.async_.rss_feeds import RssFeedsServiceAsync
from .services.async_.integrations import IntegrationsServiceAsync
from .services.async_.queued import QueuedServiceAsync


class TorboxApiAsync(TorboxApi):
    """
    TorboxApiAsync is the asynchronous version of the TorboxApi SDK Client.
    """

    def __init__(
        self,
        access_token: str = None,
        base_url: Union[Environment, str, None] = None,
        timeout: int = 60000,
    ):
        super().__init__(access_token=access_token, base_url=base_url, timeout=timeout)

        self.torrents = TorrentsServiceAsync(base_url=self._base_url)
        self.usenet = UsenetServiceAsync(base_url=self._base_url)
        self.web_downloads_debrid = WebDownloadsDebridServiceAsync(
            base_url=self._base_url
        )
        self.general = GeneralServiceAsync(base_url=self._base_url)
        self.notifications = NotificationsServiceAsync(base_url=self._base_url)
        self.user = UserServiceAsync(base_url=self._base_url)
        self.rss_feeds = RssFeedsServiceAsync(base_url=self._base_url)
        self.integrations = IntegrationsServiceAsync(base_url=self._base_url)
        self.queued = QueuedServiceAsync(base_url=self._base_url)

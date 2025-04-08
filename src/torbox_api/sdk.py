from typing import Union
from .services.torrents import TorrentsService
from .services.usenet import UsenetService
from .services.web_downloads_debrid import WebDownloadsDebridService
from .services.general import GeneralService
from .services.notifications import NotificationsService
from .services.user import UserService
from .services.rss_feeds import RssFeedsService
from .services.integrations import IntegrationsService
from .services.queued import QueuedService
from .net.environment import Environment


class TorboxApi:
    def __init__(
        self,
        access_token: str = None,
        base_url: Union[Environment, str, None] = None,
        timeout: int = 60000,
    ):
        """
        Initializes TorboxApi the SDK class.
        """

        self._base_url = (
            base_url.value if isinstance(base_url, Environment) else base_url
        )
        self.torrents = TorrentsService(base_url=self._base_url)
        self.usenet = UsenetService(base_url=self._base_url)
        self.web_downloads_debrid = WebDownloadsDebridService(base_url=self._base_url)
        self.general = GeneralService(base_url=self._base_url)
        self.notifications = NotificationsService(base_url=self._base_url)
        self.user = UserService(base_url=self._base_url)
        self.rss_feeds = RssFeedsService(base_url=self._base_url)
        self.integrations = IntegrationsService(base_url=self._base_url)
        self.queued = QueuedService(base_url=self._base_url)
        self.set_access_token(access_token)
        self.set_timeout(timeout)

    def set_base_url(self, base_url: Union[Environment, str]):
        """
        Sets the base URL for the entire SDK.

        :param Union[Environment, str] base_url: The base URL to be set.
        :return: The SDK instance.
        """
        self._base_url = (
            base_url.value if isinstance(base_url, Environment) else base_url
        )

        self.torrents.set_base_url(self._base_url)
        self.usenet.set_base_url(self._base_url)
        self.web_downloads_debrid.set_base_url(self._base_url)
        self.general.set_base_url(self._base_url)
        self.notifications.set_base_url(self._base_url)
        self.user.set_base_url(self._base_url)
        self.rss_feeds.set_base_url(self._base_url)
        self.integrations.set_base_url(self._base_url)
        self.queued.set_base_url(self._base_url)

        return self

    def set_access_token(self, access_token: str):
        """
        Sets the access token for the entire SDK.
        """
        self.torrents.set_access_token(access_token)
        self.usenet.set_access_token(access_token)
        self.web_downloads_debrid.set_access_token(access_token)
        self.general.set_access_token(access_token)
        self.notifications.set_access_token(access_token)
        self.user.set_access_token(access_token)
        self.rss_feeds.set_access_token(access_token)
        self.integrations.set_access_token(access_token)
        self.queued.set_access_token(access_token)

        return self

    def set_timeout(self, timeout: int):
        """
        Sets the timeout for the entire SDK.

        :param int timeout: The timeout (ms) to be set.
        :return: The SDK instance.
        """
        self.torrents.set_timeout(timeout)
        self.usenet.set_timeout(timeout)
        self.web_downloads_debrid.set_timeout(timeout)
        self.general.set_timeout(timeout)
        self.notifications.set_timeout(timeout)
        self.user.set_timeout(timeout)
        self.rss_feeds.set_timeout(timeout)
        self.integrations.set_timeout(timeout)
        self.queued.set_timeout(timeout)

        return self


# c029837e0e474b76bc487506e8799df5e3335891efe4fb02bda7a1441840310c

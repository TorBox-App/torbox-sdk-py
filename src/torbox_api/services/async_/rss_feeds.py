from typing import Awaitable
from .utils.to_async import to_async
from ..rss_feeds import RssFeedsService
from ...models.utils.sentinel import SENTINEL


class RssFeedsServiceAsync(RssFeedsService):
    """
    Async Wrapper for RssFeedsServiceAsync
    """

    def add_rss_feed(
        self, api_version: str, request_body: any = None
    ) -> Awaitable[None]:
        return to_async(super().add_rss_feed)(api_version, request_body)

    def control_rss_feed(
        self, api_version: str, request_body: any = None
    ) -> Awaitable[None]:
        return to_async(super().control_rss_feed)(api_version, request_body)

    def modify_rss_feed(
        self, api_version: str, request_body: any = None
    ) -> Awaitable[None]:
        return to_async(super().modify_rss_feed)(api_version, request_body)

    def get_user_rss_feeds(
        self, api_version: str, id_: str = SENTINEL
    ) -> Awaitable[None]:
        return to_async(super().get_user_rss_feeds)(api_version, id_)

    def get_rss_feed_items(
        self, api_version: str, rss_feed_id: str = SENTINEL
    ) -> Awaitable[None]:
        return to_async(super().get_rss_feed_items)(api_version, rss_feed_id)

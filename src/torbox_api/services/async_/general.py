from typing import Awaitable
from .utils.to_async import to_async
from ..general import GeneralService
from ...models import (
    GetUpStatusOkResponse,
    GetStatsOkResponse,
    GetChangelogsJsonOkResponse,
)


class GeneralServiceAsync(GeneralService):
    """
    Async Wrapper for GeneralServiceAsync
    """

    def get_up_status(self) -> Awaitable[GetUpStatusOkResponse]:
        return to_async(super().get_up_status)()

    def get_stats(self, api_version: str) -> Awaitable[GetStatsOkResponse]:
        return to_async(super().get_stats)(api_version)

    def get_changelogs_rss_feed(self, api_version: str) -> Awaitable[str]:
        return to_async(super().get_changelogs_rss_feed)(api_version)

    def get_changelogs_json(
        self, api_version: str
    ) -> Awaitable[GetChangelogsJsonOkResponse]:
        return to_async(super().get_changelogs_json)(api_version)

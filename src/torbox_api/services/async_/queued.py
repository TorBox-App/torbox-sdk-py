from typing import Awaitable
from .utils.to_async import to_async
from ..queued import QueuedService
from ...models.utils.sentinel import SENTINEL


class QueuedServiceAsync(QueuedService):
    """
    Async Wrapper for QueuedServiceAsync
    """

    def get_queued_downloads(
        self,
        api_version: str,
        bypass_cache: str = SENTINEL,
        id_: str = SENTINEL,
        offset: str = SENTINEL,
        limit: str = SENTINEL,
        type_: str = SENTINEL,
    ) -> Awaitable[None]:
        return to_async(super().get_queued_downloads)(
            api_version, bypass_cache, id_, offset, limit, type_
        )

    def control_queued_downloads(
        self, api_version: str, request_body: any = None
    ) -> Awaitable[None]:
        return to_async(super().control_queued_downloads)(api_version, request_body)

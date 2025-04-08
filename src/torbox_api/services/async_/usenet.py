from typing import Awaitable
from .utils.to_async import to_async
from ..usenet import UsenetService
from ...models.utils.sentinel import SENTINEL
from ...models import (
    CreateUsenetDownloadOkResponse,
    CreateUsenetDownloadRequest,
    GetUsenetListOkResponse,
)


class UsenetServiceAsync(UsenetService):
    """
    Async Wrapper for UsenetServiceAsync
    """

    def create_usenet_download(
        self, api_version: str, request_body: CreateUsenetDownloadRequest = None
    ) -> Awaitable[CreateUsenetDownloadOkResponse]:
        return to_async(super().create_usenet_download)(api_version, request_body)

    def control_usenet_download(
        self, api_version: str, request_body: any = None
    ) -> Awaitable[None]:
        return to_async(super().control_usenet_download)(api_version, request_body)

    def request_download_link1(
        self,
        api_version: str,
        token: str = SENTINEL,
        usenet_id: str = SENTINEL,
        file_id: str = SENTINEL,
        zip_link: str = SENTINEL,
        torrent_file: str = SENTINEL,
        user_ip: str = SENTINEL,
        redirect: str = SENTINEL,
    ) -> Awaitable[None]:
        return to_async(super().request_download_link1)(
            api_version,
            token,
            usenet_id,
            file_id,
            zip_link,
            torrent_file,
            user_ip,
            redirect,
        )

    def get_usenet_list(
        self,
        api_version: str,
        bypass_cache: str = SENTINEL,
        id_: str = SENTINEL,
        offset: str = SENTINEL,
        limit: str = SENTINEL,
    ) -> Awaitable[GetUsenetListOkResponse]:
        return to_async(super().get_usenet_list)(
            api_version, bypass_cache, id_, offset, limit
        )

    def get_usenet_cached_availability(
        self, api_version: str, hash: str = SENTINEL, format: str = SENTINEL
    ) -> Awaitable[None]:
        return to_async(super().get_usenet_cached_availability)(
            api_version, hash, format
        )

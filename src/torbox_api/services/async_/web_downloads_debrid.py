from typing import Awaitable
from .utils.to_async import to_async
from ..web_downloads_debrid import WebDownloadsDebridService
from ...models.utils.sentinel import SENTINEL
from ...models import (
    CreateWebDownloadOkResponse,
    CreateWebDownloadRequest,
    GetWebDownloadListOkResponse,
    GetHosterListOkResponse,
)


class WebDownloadsDebridServiceAsync(WebDownloadsDebridService):
    """
    Async Wrapper for WebDownloadsDebridServiceAsync
    """

    def create_web_download(
        self, api_version: str, request_body: CreateWebDownloadRequest = None
    ) -> Awaitable[CreateWebDownloadOkResponse]:
        return to_async(super().create_web_download)(api_version, request_body)

    def control_web_download(
        self,
        api_version: str,
        request_body: any = None,
        bypass_cache: str = SENTINEL,
        id_: str = SENTINEL,
    ) -> Awaitable[None]:
        return to_async(super().control_web_download)(
            api_version, request_body, bypass_cache, id_
        )

    def request_download_link2(
        self,
        api_version: str,
        token: str = SENTINEL,
        web_id: str = SENTINEL,
        file_id: str = SENTINEL,
        zip_link: str = SENTINEL,
        torrent_file: str = SENTINEL,
        user_ip: str = SENTINEL,
        redirect: str = SENTINEL,
    ) -> Awaitable[None]:
        return to_async(super().request_download_link2)(
            api_version,
            token,
            web_id,
            file_id,
            zip_link,
            torrent_file,
            user_ip,
            redirect,
        )

    def get_web_download_list(
        self,
        api_version: str,
        bypass_cache: str = SENTINEL,
        id_: str = SENTINEL,
        offset: str = SENTINEL,
        limit: str = SENTINEL,
    ) -> Awaitable[GetWebDownloadListOkResponse]:
        return to_async(super().get_web_download_list)(
            api_version, bypass_cache, id_, offset, limit
        )

    def get_web_download_cached_availability(
        self, api_version: str, hash: str = SENTINEL, format: str = SENTINEL
    ) -> Awaitable[None]:
        return to_async(super().get_web_download_cached_availability)(
            api_version, hash, format
        )

    def get_hoster_list(self, api_version: str) -> Awaitable[GetHosterListOkResponse]:
        return to_async(super().get_hoster_list)(api_version)

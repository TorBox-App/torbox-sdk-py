from typing import Awaitable
from .utils.to_async import to_async
from ..torrents import TorrentsService
from ...models.utils.sentinel import SENTINEL
from ...models import (
    CreateTorrentOkResponse,
    CreateTorrentRequest,
    ControlTorrentOkResponse,
    RequestDownloadLinkOkResponse,
    GetTorrentListOkResponse,
    GetTorrentCachedAvailabilityOkResponse,
    ExportTorrentDataOkResponse,
    GetTorrentInfoOkResponse,
)


class TorrentsServiceAsync(TorrentsService):
    """
    Async Wrapper for TorrentsServiceAsync
    """

    def create_torrent(
        self, api_version: str, request_body: CreateTorrentRequest = None
    ) -> Awaitable[CreateTorrentOkResponse]:
        return to_async(super().create_torrent)(api_version, request_body)

    def control_torrent(
        self, api_version: str, request_body: any = None
    ) -> Awaitable[ControlTorrentOkResponse]:
        return to_async(super().control_torrent)(api_version, request_body)

    def request_download_link(
        self,
        api_version: str,
        token: str = SENTINEL,
        torrent_id: str = SENTINEL,
        file_id: str = SENTINEL,
        zip_link: str = SENTINEL,
        torrent_file: str = SENTINEL,
        user_ip: str = SENTINEL,
        redirect: str = SENTINEL,
    ) -> Awaitable[RequestDownloadLinkOkResponse]:
        return to_async(super().request_download_link)(
            api_version,
            token,
            torrent_id,
            file_id,
            zip_link,
            torrent_file,
            user_ip,
            redirect,
        )

    def get_torrent_list(
        self,
        api_version: str,
        bypass_cache: str = SENTINEL,
        id_: str = SENTINEL,
        offset: str = SENTINEL,
        limit: str = SENTINEL,
    ) -> Awaitable[GetTorrentListOkResponse]:
        return to_async(super().get_torrent_list)(
            api_version, bypass_cache, id_, offset, limit
        )

    def get_torrent_cached_availability(
        self,
        api_version: str,
        hash: str = SENTINEL,
        format: str = SENTINEL,
        list_files: str = SENTINEL,
    ) -> Awaitable[GetTorrentCachedAvailabilityOkResponse]:
        return to_async(super().get_torrent_cached_availability)(
            api_version, hash, format, list_files
        )

    def export_torrent_data(
        self, api_version: str, torrent_id: str = SENTINEL, type_: str = SENTINEL
    ) -> Awaitable[ExportTorrentDataOkResponse]:
        return to_async(super().export_torrent_data)(api_version, torrent_id, type_)

    def get_torrent_info(
        self, api_version: str, hash: str = SENTINEL, timeout: str = SENTINEL
    ) -> Awaitable[GetTorrentInfoOkResponse]:
        return to_async(super().get_torrent_info)(api_version, hash, timeout)

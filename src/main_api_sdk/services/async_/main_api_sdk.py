from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..main_api_sdk import MainApiSdkService
from ...net.sdk_config import SdkConfig
from ...models.utils.sentinel import SENTINEL
from ...models import (
    CreateTorrentRequest,
    AsyncCreateTorrentRequest,
    MainApiSdkRequestDownloadLinksPostRequest1,
    GetTorrentCachedAvailabilityBatchRequest,
    GetTorrentInfoRequest,
    EditTorrentItemRequest,
    MagnetToFileRequest,
    CreateUsenetDownloadRequest,
    MainApiSdkRequestDownloadLinksPostRequest2,
    GetUsenetCachedAvailabilityBatchRequest,
    EditUsenetItemRequest,
    CreateWebDownloadRequest,
    MainApiSdkRequestDownloadLinksPostRequest3,
    GetWebDownloadCachedAvailabilityBatchRequest,
    EditWebDownloadItemRequest,
    GetTokenFromDeviceCodeProcessRequest,
)


class MainApiSdkServiceAsync(MainApiSdkService):
    """
    Async Wrapper for MainApiSdkServiceAsync
    """

    def create_torrent(
        self,
        request_body: CreateTorrentRequest,
        api_version: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().create_torrent)(
            request_body, api_version, request_config=request_config
        )

    def async_create_torrent(
        self,
        request_body: AsyncCreateTorrentRequest,
        api_version: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().async_create_torrent)(
            request_body, api_version, request_config=request_config
        )

    def control_torrent(
        self,
        request_body: dict,
        api_version: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().control_torrent)(
            request_body, api_version, request_config=request_config
        )

    def request_download_link(
        self,
        api_version: str,
        token: Union[str, None] = SENTINEL,
        torrent_id: Union[str, None] = SENTINEL,
        file_id: Union[str, None] = SENTINEL,
        zip_link: Union[str, None] = SENTINEL,
        user_ip: Union[str, None] = SENTINEL,
        redirect: Union[str, None] = SENTINEL,
        append_name: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().request_download_link)(
            api_version,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "token": token,
                        "torrent_id": torrent_id,
                        "file_id": file_id,
                        "zip_link": zip_link,
                        "user_ip": user_ip,
                        "redirect": redirect,
                        "append_name": append_name,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_config=request_config,
        )

    def request_download_links_get(
        self,
        api_version: str,
        token: Union[str, None] = SENTINEL,
        torrent_id: Union[str, None] = SENTINEL,
        file_ids: Union[str, None] = SENTINEL,
        user_ip: Union[str, None] = SENTINEL,
        append_name: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().request_download_links_get)(
            api_version,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "token": token,
                        "torrent_id": torrent_id,
                        "file_ids": file_ids,
                        "user_ip": user_ip,
                        "append_name": append_name,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_config=request_config,
        )

    def request_download_links_post(
        self,
        request_body: MainApiSdkRequestDownloadLinksPostRequest1,
        api_version: str,
        token: Union[str, None] = SENTINEL,
        torrent_id: Union[str, None] = SENTINEL,
        user_ip: Union[str, None] = SENTINEL,
        append_name: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().request_download_links_post)(
            request_body,
            api_version,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "token": token,
                        "torrent_id": torrent_id,
                        "user_ip": user_ip,
                        "append_name": append_name,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_config=request_config,
        )

    def get_torrent_list(
        self,
        api_version: str,
        bypass_cache: Union[str, None] = SENTINEL,
        id_: Union[str, None] = SENTINEL,
        offset: Union[str, None] = SENTINEL,
        limit: Union[str, None] = SENTINEL,
        active: Union[str, None] = SENTINEL,
        files: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().get_torrent_list)(
            api_version,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "bypass_cache": bypass_cache,
                        "id_": id_,
                        "offset": offset,
                        "limit": limit,
                        "active": active,
                        "files": files,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_config=request_config,
        )

    def get_torrent_cached_availability(
        self,
        api_version: str,
        hash: Union[str, None] = SENTINEL,
        format: Union[str, None] = SENTINEL,
        list_files: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().get_torrent_cached_availability)(
            api_version,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "hash": hash,
                        "format": format,
                        "list_files": list_files,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_config=request_config,
        )

    def get_torrent_cached_availability_batch(
        self,
        request_body: GetTorrentCachedAvailabilityBatchRequest,
        api_version: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().get_torrent_cached_availability_batch)(
            request_body, api_version, request_config=request_config
        )

    def export_torrent_data(
        self,
        api_version: str,
        torrent_id: Union[str, None] = SENTINEL,
        type_: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().export_torrent_data)(
            api_version,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"torrent_id": torrent_id, "type_": type_}.items()
                    if v is not SENTINEL
                }
            ),
            request_config=request_config,
        )

    def get_torrent_info(
        self,
        api_version: str,
        hash: Union[str, None] = SENTINEL,
        timeout: Union[str, None] = SENTINEL,
        use_cache_lookup: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().get_torrent_info)(
            api_version,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "hash": hash,
                        "timeout": timeout,
                        "use_cache_lookup": use_cache_lookup,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_config=request_config,
        )

    def get_torrent_info_1(
        self,
        request_body: GetTorrentInfoRequest,
        api_version: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().get_torrent_info_1)(
            request_body, api_version, request_config=request_config
        )

    def edit_torrent_item(
        self,
        request_body: EditTorrentItemRequest,
        api_version: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().edit_torrent_item)(
            request_body, api_version, request_config=request_config
        )

    def magnet_to_file(
        self,
        request_body: MagnetToFileRequest,
        api_version: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().magnet_to_file)(
            request_body, api_version, request_config=request_config
        )

    def create_usenet_download(
        self,
        request_body: CreateUsenetDownloadRequest,
        api_version: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().create_usenet_download)(
            request_body, api_version, request_config=request_config
        )

    def control_usenet_download(
        self,
        request_body: dict,
        api_version: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().control_usenet_download)(
            request_body, api_version, request_config=request_config
        )

    def request_download_link_1(
        self,
        api_version: str,
        token: Union[str, None] = SENTINEL,
        usenet_id: Union[str, None] = SENTINEL,
        file_id: Union[str, None] = SENTINEL,
        zip_link: Union[str, None] = SENTINEL,
        user_ip: Union[str, None] = SENTINEL,
        redirect: Union[str, None] = SENTINEL,
        append_name: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().request_download_link_1)(
            api_version,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "token": token,
                        "usenet_id": usenet_id,
                        "file_id": file_id,
                        "zip_link": zip_link,
                        "user_ip": user_ip,
                        "redirect": redirect,
                        "append_name": append_name,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_config=request_config,
        )

    def request_download_links_get_1(
        self,
        api_version: str,
        token: Union[str, None] = SENTINEL,
        usenet_id: Union[str, None] = SENTINEL,
        file_ids: Union[str, None] = SENTINEL,
        user_ip: Union[str, None] = SENTINEL,
        append_name: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().request_download_links_get_1)(
            api_version,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "token": token,
                        "usenet_id": usenet_id,
                        "file_ids": file_ids,
                        "user_ip": user_ip,
                        "append_name": append_name,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_config=request_config,
        )

    def request_download_links_post_1(
        self,
        request_body: MainApiSdkRequestDownloadLinksPostRequest2,
        api_version: str,
        token: Union[str, None] = SENTINEL,
        usenet_id: Union[str, None] = SENTINEL,
        user_ip: Union[str, None] = SENTINEL,
        append_name: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().request_download_links_post_1)(
            request_body,
            api_version,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "token": token,
                        "usenet_id": usenet_id,
                        "user_ip": user_ip,
                        "append_name": append_name,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_config=request_config,
        )

    def get_usenet_list(
        self,
        api_version: str,
        bypass_cache: Union[str, None] = SENTINEL,
        id_: Union[str, None] = SENTINEL,
        offset: Union[str, None] = SENTINEL,
        limit: Union[str, None] = SENTINEL,
        active: Union[str, None] = SENTINEL,
        files: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().get_usenet_list)(
            api_version,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "bypass_cache": bypass_cache,
                        "id_": id_,
                        "offset": offset,
                        "limit": limit,
                        "active": active,
                        "files": files,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_config=request_config,
        )

    def get_usenet_cached_availability(
        self,
        api_version: str,
        hash: Union[str, None] = SENTINEL,
        format: Union[str, None] = SENTINEL,
        list_files: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().get_usenet_cached_availability)(
            api_version,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "hash": hash,
                        "format": format,
                        "list_files": list_files,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_config=request_config,
        )

    def get_usenet_cached_availability_batch(
        self,
        request_body: GetUsenetCachedAvailabilityBatchRequest,
        api_version: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().get_usenet_cached_availability_batch)(
            request_body, api_version, request_config=request_config
        )

    def edit_usenet_item(
        self,
        request_body: EditUsenetItemRequest,
        api_version: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().edit_usenet_item)(
            request_body, api_version, request_config=request_config
        )

    def get_news_server_connection_information(
        self, api_version: str, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().get_news_server_connection_information)(
            api_version, request_config=request_config
        )

    def get_news_server_account(
        self, api_version: str, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().get_news_server_account)(
            api_version, request_config=request_config
        )

    def reset_news_server_account_password(
        self, api_version: str, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().reset_news_server_account_password)(
            api_version, request_config=request_config
        )

    def create_web_download(
        self,
        request_body: CreateWebDownloadRequest,
        api_version: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().create_web_download)(
            request_body, api_version, request_config=request_config
        )

    def control_web_download(
        self,
        request_body: dict,
        api_version: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().control_web_download)(
            request_body, api_version, request_config=request_config
        )

    def request_download_link_2(
        self,
        api_version: str,
        token: Union[str, None] = SENTINEL,
        web_id: Union[str, None] = SENTINEL,
        file_id: Union[str, None] = SENTINEL,
        zip_link: Union[str, None] = SENTINEL,
        user_ip: Union[str, None] = SENTINEL,
        redirect: Union[str, None] = SENTINEL,
        append_name: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().request_download_link_2)(
            api_version,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "token": token,
                        "web_id": web_id,
                        "file_id": file_id,
                        "zip_link": zip_link,
                        "user_ip": user_ip,
                        "redirect": redirect,
                        "append_name": append_name,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_config=request_config,
        )

    def request_download_links_get_2(
        self,
        api_version: str,
        token: Union[str, None] = SENTINEL,
        web_id: Union[str, None] = SENTINEL,
        file_ids: Union[str, None] = SENTINEL,
        user_ip: Union[str, None] = SENTINEL,
        append_name: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().request_download_links_get_2)(
            api_version,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "token": token,
                        "web_id": web_id,
                        "file_ids": file_ids,
                        "user_ip": user_ip,
                        "append_name": append_name,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_config=request_config,
        )

    def request_download_links_post_2(
        self,
        request_body: MainApiSdkRequestDownloadLinksPostRequest3,
        api_version: str,
        token: Union[str, None] = SENTINEL,
        web_id: Union[str, None] = SENTINEL,
        user_ip: Union[str, None] = SENTINEL,
        append_name: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().request_download_links_post_2)(
            request_body,
            api_version,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "token": token,
                        "web_id": web_id,
                        "user_ip": user_ip,
                        "append_name": append_name,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_config=request_config,
        )

    def get_web_download_list(
        self,
        api_version: str,
        bypass_cache: Union[str, None] = SENTINEL,
        id_: Union[str, None] = SENTINEL,
        offset: Union[str, None] = SENTINEL,
        limit: Union[str, None] = SENTINEL,
        active: Union[str, None] = SENTINEL,
        files: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().get_web_download_list)(
            api_version,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "bypass_cache": bypass_cache,
                        "id_": id_,
                        "offset": offset,
                        "limit": limit,
                        "active": active,
                        "files": files,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_config=request_config,
        )

    def get_web_download_cached_availability(
        self,
        api_version: str,
        hash: Union[str, None] = SENTINEL,
        format: Union[str, None] = SENTINEL,
        list_files: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().get_web_download_cached_availability)(
            api_version,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "hash": hash,
                        "format": format,
                        "list_files": list_files,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_config=request_config,
        )

    def get_web_download_cached_availability_batch(
        self,
        request_body: GetWebDownloadCachedAvailabilityBatchRequest,
        api_version: str,
        format: Union[str, None] = SENTINEL,
        list_files: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().get_web_download_cached_availability_batch)(
            request_body,
            api_version,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"format": format, "list_files": list_files}.items()
                    if v is not SENTINEL
                }
            ),
            request_config=request_config,
        )

    def get_hoster_list(
        self, api_version: str, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().get_hoster_list)(
            api_version, request_config=request_config
        )

    def edit_web_download_item(
        self,
        request_body: EditWebDownloadItemRequest,
        api_version: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().edit_web_download_item)(
            request_body, api_version, request_config=request_config
        )

    def get_up_status(
        self, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().get_up_status)(request_config=request_config)

    def get_stats(
        self, api_version: str, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().get_stats)(api_version, request_config=request_config)

    def get_changelogs_rss_feed(
        self,
        api_version: str,
        offset: Union[str, None] = SENTINEL,
        limit: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[str]:  # type: ignore[override]
        return to_async(super().get_changelogs_rss_feed)(
            api_version,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"offset": offset, "limit": limit}.items()
                    if v is not SENTINEL
                }
            ),
            request_config=request_config,
        )

    def get_changelogs_json(
        self,
        api_version: str,
        offset: Union[str, None] = SENTINEL,
        limit: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().get_changelogs_json)(
            api_version,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"offset": offset, "limit": limit}.items()
                    if v is not SENTINEL
                }
            ),
            request_config=request_config,
        )

    def get_speedtest_files(
        self,
        api_version: str,
        test_length: Union[str, None] = SENTINEL,
        region: Union[str, None] = SENTINEL,
        user_ip: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().get_speedtest_files)(
            api_version,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "test_length": test_length,
                        "region": region,
                        "user_ip": user_ip,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_config=request_config,
        )

    def get_rss_notification_feed(
        self,
        api_version: str,
        token: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[str]:  # type: ignore[override]
        return to_async(super().get_rss_notification_feed)(
            api_version,
            **dict[str, Any](
                {k: v for k, v in {"token": token}.items() if v is not SENTINEL}
            ),
            request_config=request_config,
        )

    def get_notification_feed(
        self, api_version: str, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().get_notification_feed)(
            api_version, request_config=request_config
        )

    def clear_all_notifications(
        self, api_version: str, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().clear_all_notifications)(
            api_version, request_config=request_config
        )

    def clear_single_notification(
        self,
        api_version: str,
        notification_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().clear_single_notification)(
            api_version, notification_id, request_config=request_config
        )

    def send_test_notification(
        self, api_version: str, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().send_test_notification)(
            api_version, request_config=request_config
        )

    def refresh_api_token(
        self,
        request_body: dict,
        api_version: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().refresh_api_token)(
            request_body, api_version, request_config=request_config
        )

    def get_user_data(
        self,
        api_version: str,
        settings: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().get_user_data)(
            api_version,
            **dict[str, Any](
                {k: v for k, v in {"settings": settings}.items() if v is not SENTINEL}
            ),
            request_config=request_config,
        )

    def add_referral_to_account(
        self,
        api_version: str,
        referral: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().add_referral_to_account)(
            api_version,
            **dict[str, Any](
                {k: v for k, v in {"referral": referral}.items() if v is not SENTINEL}
            ),
            request_config=request_config,
        )

    def get_confirmation_code(
        self, api_version: str, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().get_confirmation_code)(
            api_version, request_config=request_config
        )

    def start_device_code_authorization_process(
        self,
        api_version: str,
        app: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().start_device_code_authorization_process)(
            api_version,
            **dict[str, Any](
                {k: v for k, v in {"app": app}.items() if v is not SENTINEL}
            ),
            request_config=request_config,
        )

    def get_token_from_device_code_process(
        self,
        request_body: GetTokenFromDeviceCodeProcessRequest,
        api_version: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().get_token_from_device_code_process)(
            request_body, api_version, request_config=request_config
        )

    def get_referral_data(
        self, api_version: str, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().get_referral_data)(
            api_version, request_config=request_config
        )

    def get_subscriptions(
        self, api_version: str, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().get_subscriptions)(
            api_version, request_config=request_config
        )

    def get_transactions(
        self, api_version: str, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().get_transactions)(
            api_version, request_config=request_config
        )

    def get_transaction_pdf(
        self,
        api_version: str,
        transaction_id: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().get_transaction_pdf)(
            api_version,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"transaction_id": transaction_id}.items()
                    if v is not SENTINEL
                }
            ),
            request_config=request_config,
        )

    def edit_user_settings(
        self,
        request_body: dict,
        api_version: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().edit_user_settings)(
            request_body, api_version, request_config=request_config
        )

    def get_user_stats(
        self,
        api_version: str,
        general: Union[str, None] = SENTINEL,
        bandwidth: Union[str, None] = SENTINEL,
        bandwidth_grouping: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().get_user_stats)(
            api_version,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "general": general,
                        "bandwidth": bandwidth,
                        "bandwidth_grouping": bandwidth_grouping,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_config=request_config,
        )

    def add_rss_feed(
        self,
        request_body: dict,
        api_version: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().add_rss_feed)(
            request_body, api_version, request_config=request_config
        )

    def control_rss_feed(
        self,
        request_body: dict,
        api_version: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().control_rss_feed)(
            request_body, api_version, request_config=request_config
        )

    def edit_rss_feed(
        self,
        request_body: dict,
        api_version: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().edit_rss_feed)(
            request_body, api_version, request_config=request_config
        )

    def get_user_rss_feeds(
        self,
        api_version: str,
        id_: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().get_user_rss_feeds)(
            api_version,
            **dict[str, Any](
                {k: v for k, v in {"id_": id_}.items() if v is not SENTINEL}
            ),
            request_config=request_config,
        )

    def get_rss_feed_items(
        self,
        api_version: str,
        rss_feed_id: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().get_rss_feed_items)(
            api_version,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"rss_feed_id": rss_feed_id}.items()
                    if v is not SENTINEL
                }
            ),
            request_config=request_config,
        )

    def get_all_jobs(
        self, api_version: str, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().get_all_jobs)(
            api_version, request_config=request_config
        )

    def get_specific_job(
        self,
        api_version: str,
        job_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().get_specific_job)(
            api_version, job_id, request_config=request_config
        )

    def get_all_jobs_by_hash(
        self, api_version: str, hash: str, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().get_all_jobs_by_hash)(
            api_version, hash, request_config=request_config
        )

    def cancel_specific_job(
        self,
        api_version: str,
        job_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().cancel_specific_job)(
            api_version, job_id, request_config=request_config
        )

    def get_queued_downloads(
        self,
        api_version: str,
        bypass_cache: Union[str, None] = SENTINEL,
        id_: Union[str, None] = SENTINEL,
        offset: Union[str, None] = SENTINEL,
        limit: Union[str, None] = SENTINEL,
        type_: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().get_queued_downloads)(
            api_version,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "bypass_cache": bypass_cache,
                        "id_": id_,
                        "offset": offset,
                        "limit": limit,
                        "type_": type_,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_config=request_config,
        )

    def control_queued_downloads(
        self,
        request_body: dict,
        api_version: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().control_queued_downloads)(
            request_body, api_version, request_config=request_config
        )

    def create_stream(
        self,
        api_version: str,
        id_: Union[str, None] = SENTINEL,
        file_id: Union[str, None] = SENTINEL,
        type_: Union[str, None] = SENTINEL,
        chosen_subtitle_index: Union[str, None] = SENTINEL,
        chosen_audio_index: Union[str, None] = SENTINEL,
        chosen_resolution_index: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().create_stream)(
            api_version,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "id_": id_,
                        "file_id": file_id,
                        "type_": type_,
                        "chosen_subtitle_index": chosen_subtitle_index,
                        "chosen_audio_index": chosen_audio_index,
                        "chosen_resolution_index": chosen_resolution_index,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_config=request_config,
        )

    def get_stream_data(
        self,
        api_version: str,
        presigned_token: Union[str, None] = SENTINEL,
        token: Union[str, None] = SENTINEL,
        chosen_subtitle_index: Union[str, None] = SENTINEL,
        chosen_audio_index: Union[str, None] = SENTINEL,
        chosen_resolution_index: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        return to_async(super().get_stream_data)(
            api_version,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "presigned_token": presigned_token,
                        "token": token,
                        "chosen_subtitle_index": chosen_subtitle_index,
                        "chosen_audio_index": chosen_audio_index,
                        "chosen_resolution_index": chosen_resolution_index,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_config=request_config,
        )

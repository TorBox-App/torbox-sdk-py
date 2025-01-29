from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class GetStatsOkResponseData(BaseModel):
    """GetStatsOkResponseData

    :param active_torrents: active_torrents, defaults to None
    :type active_torrents: float, optional
    :param active_usenet_downloads: active_usenet_downloads, defaults to None
    :type active_usenet_downloads: float, optional
    :param active_web_downloads: active_web_downloads, defaults to None
    :type active_web_downloads: float, optional
    :param total_bytes_downloaded: total_bytes_downloaded, defaults to None
    :type total_bytes_downloaded: float, optional
    :param total_bytes_uploaded: total_bytes_uploaded, defaults to None
    :type total_bytes_uploaded: float, optional
    :param total_downloads: total_downloads, defaults to None
    :type total_downloads: float, optional
    :param total_servers: total_servers, defaults to None
    :type total_servers: float, optional
    :param total_torrent_downloads: total_torrent_downloads, defaults to None
    :type total_torrent_downloads: float, optional
    :param total_usenet_downloads: total_usenet_downloads, defaults to None
    :type total_usenet_downloads: float, optional
    :param total_users: total_users, defaults to None
    :type total_users: float, optional
    :param total_web_downloads: total_web_downloads, defaults to None
    :type total_web_downloads: float, optional
    """

    def __init__(
        self,
        active_torrents: float = None,
        active_usenet_downloads: float = None,
        active_web_downloads: float = None,
        total_bytes_downloaded: float = None,
        total_bytes_uploaded: float = None,
        total_downloads: float = None,
        total_servers: float = None,
        total_torrent_downloads: float = None,
        total_usenet_downloads: float = None,
        total_users: float = None,
        total_web_downloads: float = None,
        **kwargs
    ):
        """GetStatsOkResponseData

        :param active_torrents: active_torrents, defaults to None
        :type active_torrents: float, optional
        :param active_usenet_downloads: active_usenet_downloads, defaults to None
        :type active_usenet_downloads: float, optional
        :param active_web_downloads: active_web_downloads, defaults to None
        :type active_web_downloads: float, optional
        :param total_bytes_downloaded: total_bytes_downloaded, defaults to None
        :type total_bytes_downloaded: float, optional
        :param total_bytes_uploaded: total_bytes_uploaded, defaults to None
        :type total_bytes_uploaded: float, optional
        :param total_downloads: total_downloads, defaults to None
        :type total_downloads: float, optional
        :param total_servers: total_servers, defaults to None
        :type total_servers: float, optional
        :param total_torrent_downloads: total_torrent_downloads, defaults to None
        :type total_torrent_downloads: float, optional
        :param total_usenet_downloads: total_usenet_downloads, defaults to None
        :type total_usenet_downloads: float, optional
        :param total_users: total_users, defaults to None
        :type total_users: float, optional
        :param total_web_downloads: total_web_downloads, defaults to None
        :type total_web_downloads: float, optional
        """
        if active_torrents is not None:
            self.active_torrents = active_torrents
        if active_usenet_downloads is not None:
            self.active_usenet_downloads = active_usenet_downloads
        if active_web_downloads is not None:
            self.active_web_downloads = active_web_downloads
        if total_bytes_downloaded is not None:
            self.total_bytes_downloaded = total_bytes_downloaded
        if total_bytes_uploaded is not None:
            self.total_bytes_uploaded = total_bytes_uploaded
        if total_downloads is not None:
            self.total_downloads = total_downloads
        if total_servers is not None:
            self.total_servers = total_servers
        if total_torrent_downloads is not None:
            self.total_torrent_downloads = total_torrent_downloads
        if total_usenet_downloads is not None:
            self.total_usenet_downloads = total_usenet_downloads
        if total_users is not None:
            self.total_users = total_users
        if total_web_downloads is not None:
            self.total_web_downloads = total_web_downloads
        self._kwargs = kwargs


@JsonMap({})
class GetStatsOkResponse(BaseModel):
    """GetStatsOkResponse

    :param data: data, defaults to None
    :type data: GetStatsOkResponseData, optional
    :param detail: detail, defaults to None
    :type detail: str, optional
    :param error: error, defaults to None
    :type error: bool, optional
    :param success: success, defaults to None
    :type success: bool, optional
    """

    def __init__(
        self,
        data: GetStatsOkResponseData = None,
        detail: str = None,
        error: bool = None,
        success: bool = None,
        **kwargs
    ):
        """GetStatsOkResponse

        :param data: data, defaults to None
        :type data: GetStatsOkResponseData, optional
        :param detail: detail, defaults to None
        :type detail: str, optional
        :param error: error, defaults to None
        :type error: bool, optional
        :param success: success, defaults to None
        :type success: bool, optional
        """
        if data is not None:
            self.data = self._define_object(data, GetStatsOkResponseData)
        if detail is not None:
            self.detail = detail
        if error is not None:
            self.error = error
        if success is not None:
            self.success = success
        self._kwargs = kwargs

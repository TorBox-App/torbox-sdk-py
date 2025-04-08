from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class CreateTorrentOkResponseData(BaseModel):
    """CreateTorrentOkResponseData

    :param active_limit: active_limit, defaults to None
    :type active_limit: float, optional
    :param auth_id: auth_id, defaults to None
    :type auth_id: str, optional
    :param current_active_downloads: current_active_downloads, defaults to None
    :type current_active_downloads: float, optional
    :param hash: hash, defaults to None
    :type hash: str, optional
    :param queued_id: queued_id, defaults to None
    :type queued_id: float, optional
    :param torrent_id: torrent_id, defaults to None
    :type torrent_id: float, optional
    """

    def __init__(
        self,
        active_limit: float = SENTINEL,
        auth_id: str = SENTINEL,
        current_active_downloads: float = SENTINEL,
        hash: str = SENTINEL,
        queued_id: float = SENTINEL,
        torrent_id: float = SENTINEL,
        **kwargs
    ):
        """CreateTorrentOkResponseData

        :param active_limit: active_limit, defaults to None
        :type active_limit: float, optional
        :param auth_id: auth_id, defaults to None
        :type auth_id: str, optional
        :param current_active_downloads: current_active_downloads, defaults to None
        :type current_active_downloads: float, optional
        :param hash: hash, defaults to None
        :type hash: str, optional
        :param queued_id: queued_id, defaults to None
        :type queued_id: float, optional
        :param torrent_id: torrent_id, defaults to None
        :type torrent_id: float, optional
        """
        if active_limit is not SENTINEL:
            self.active_limit = active_limit
        if auth_id is not SENTINEL:
            self.auth_id = auth_id
        if current_active_downloads is not SENTINEL:
            self.current_active_downloads = current_active_downloads
        if hash is not SENTINEL:
            self.hash = hash
        if queued_id is not SENTINEL:
            self.queued_id = queued_id
        if torrent_id is not SENTINEL:
            self.torrent_id = torrent_id
        self._kwargs = kwargs


@JsonMap({})
class CreateTorrentOkResponse(BaseModel):
    """CreateTorrentOkResponse

    :param data: data, defaults to None
    :type data: CreateTorrentOkResponseData, optional
    :param detail: detail, defaults to None
    :type detail: str, optional
    :param error: error, defaults to None
    :type error: any, optional
    :param success: success, defaults to None
    :type success: bool, optional
    """

    def __init__(
        self,
        data: CreateTorrentOkResponseData = SENTINEL,
        detail: str = SENTINEL,
        error: Union[any, None] = SENTINEL,
        success: bool = SENTINEL,
        **kwargs
    ):
        """CreateTorrentOkResponse

        :param data: data, defaults to None
        :type data: CreateTorrentOkResponseData, optional
        :param detail: detail, defaults to None
        :type detail: str, optional
        :param error: error, defaults to None
        :type error: any, optional
        :param success: success, defaults to None
        :type success: bool, optional
        """
        if data is not SENTINEL:
            self.data = self._define_object(data, CreateTorrentOkResponseData)
        if detail is not SENTINEL:
            self.detail = detail
        if error is not SENTINEL:
            self.error = error
        if success is not SENTINEL:
            self.success = success
        self._kwargs = kwargs

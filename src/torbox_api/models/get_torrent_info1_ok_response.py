from typing import List
from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class DataFiles3(BaseModel):
    """DataFiles3

    :param name: name, defaults to None
    :type name: str, optional
    :param size: size, defaults to None
    :type size: float, optional
    """

    def __init__(self, name: str = SENTINEL, size: float = SENTINEL, **kwargs):
        """DataFiles3

        :param name: name, defaults to None
        :type name: str, optional
        :param size: size, defaults to None
        :type size: float, optional
        """
        if name is not SENTINEL:
            self.name = name
        if size is not SENTINEL:
            self.size = size
        self._kwargs = kwargs


@JsonMap({})
class GetTorrentInfo1OkResponseData(BaseModel):
    """GetTorrentInfo1OkResponseData

    :param files: files, defaults to None
    :type files: List[DataFiles3], optional
    :param hash: hash, defaults to None
    :type hash: str, optional
    :param name: name, defaults to None
    :type name: str, optional
    :param peers: peers, defaults to None
    :type peers: float, optional
    :param seeds: seeds, defaults to None
    :type seeds: float, optional
    :param size: size, defaults to None
    :type size: float, optional
    :param trackers: trackers, defaults to None
    :type trackers: List[any], optional
    """

    def __init__(
        self,
        files: List[DataFiles3] = SENTINEL,
        hash: str = SENTINEL,
        name: str = SENTINEL,
        peers: float = SENTINEL,
        seeds: float = SENTINEL,
        size: float = SENTINEL,
        trackers: List[any] = SENTINEL,
        **kwargs
    ):
        """GetTorrentInfo1OkResponseData

        :param files: files, defaults to None
        :type files: List[DataFiles3], optional
        :param hash: hash, defaults to None
        :type hash: str, optional
        :param name: name, defaults to None
        :type name: str, optional
        :param peers: peers, defaults to None
        :type peers: float, optional
        :param seeds: seeds, defaults to None
        :type seeds: float, optional
        :param size: size, defaults to None
        :type size: float, optional
        :param trackers: trackers, defaults to None
        :type trackers: List[any], optional
        """
        if files is not SENTINEL:
            self.files = self._define_list(files, DataFiles3)
        if hash is not SENTINEL:
            self.hash = hash
        if name is not SENTINEL:
            self.name = name
        if peers is not SENTINEL:
            self.peers = peers
        if seeds is not SENTINEL:
            self.seeds = seeds
        if size is not SENTINEL:
            self.size = size
        if trackers is not SENTINEL:
            self.trackers = trackers
        self._kwargs = kwargs


@JsonMap({})
class GetTorrentInfo1OkResponse(BaseModel):
    """GetTorrentInfo1OkResponse

    :param data: data, defaults to None
    :type data: GetTorrentInfo1OkResponseData, optional
    :param detail: detail, defaults to None
    :type detail: str, optional
    :param error: error, defaults to None
    :type error: any, optional
    :param success: success, defaults to None
    :type success: bool, optional
    """

    def __init__(
        self,
        data: GetTorrentInfo1OkResponseData = SENTINEL,
        detail: str = SENTINEL,
        error: Union[any, None] = SENTINEL,
        success: bool = SENTINEL,
        **kwargs
    ):
        """GetTorrentInfo1OkResponse

        :param data: data, defaults to None
        :type data: GetTorrentInfo1OkResponseData, optional
        :param detail: detail, defaults to None
        :type detail: str, optional
        :param error: error, defaults to None
        :type error: any, optional
        :param success: success, defaults to None
        :type success: bool, optional
        """
        if data is not SENTINEL:
            self.data = self._define_object(data, GetTorrentInfo1OkResponseData)
        if detail is not SENTINEL:
            self.detail = detail
        if error is not SENTINEL:
            self.error = error
        if success is not SENTINEL:
            self.success = success
        self._kwargs = kwargs

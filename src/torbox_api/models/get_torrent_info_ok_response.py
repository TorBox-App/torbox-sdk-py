from typing import List
from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class DataFiles2(BaseModel):
    """DataFiles2

    :param name: name, defaults to None
    :type name: str, optional
    :param size: size, defaults to None
    :type size: float, optional
    """

    def __init__(self, name: str = SENTINEL, size: float = SENTINEL, **kwargs):
        """DataFiles2

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
class GetTorrentInfoOkResponseData(BaseModel):
    """GetTorrentInfoOkResponseData

    :param files: files, defaults to None
    :type files: List[DataFiles2], optional
    :param hash: hash, defaults to None
    :type hash: str, optional
    :param name: name, defaults to None
    :type name: str, optional
    :param size: size, defaults to None
    :type size: float, optional
    """

    def __init__(
        self,
        files: List[DataFiles2] = SENTINEL,
        hash: str = SENTINEL,
        name: str = SENTINEL,
        size: float = SENTINEL,
        **kwargs
    ):
        """GetTorrentInfoOkResponseData

        :param files: files, defaults to None
        :type files: List[DataFiles2], optional
        :param hash: hash, defaults to None
        :type hash: str, optional
        :param name: name, defaults to None
        :type name: str, optional
        :param size: size, defaults to None
        :type size: float, optional
        """
        if files is not SENTINEL:
            self.files = self._define_list(files, DataFiles2)
        if hash is not SENTINEL:
            self.hash = hash
        if name is not SENTINEL:
            self.name = name
        if size is not SENTINEL:
            self.size = size
        self._kwargs = kwargs


@JsonMap({})
class GetTorrentInfoOkResponse(BaseModel):
    """GetTorrentInfoOkResponse

    :param data: data, defaults to None
    :type data: GetTorrentInfoOkResponseData, optional
    :param detail: detail, defaults to None
    :type detail: str, optional
    :param error: error, defaults to None
    :type error: any, optional
    :param success: success, defaults to None
    :type success: bool, optional
    """

    def __init__(
        self,
        data: GetTorrentInfoOkResponseData = SENTINEL,
        detail: str = SENTINEL,
        error: Union[any, None] = SENTINEL,
        success: bool = SENTINEL,
        **kwargs
    ):
        """GetTorrentInfoOkResponse

        :param data: data, defaults to None
        :type data: GetTorrentInfoOkResponseData, optional
        :param detail: detail, defaults to None
        :type detail: str, optional
        :param error: error, defaults to None
        :type error: any, optional
        :param success: success, defaults to None
        :type success: bool, optional
        """
        if data is not SENTINEL:
            self.data = self._define_object(data, GetTorrentInfoOkResponseData)
        if detail is not SENTINEL:
            self.detail = detail
        if error is not SENTINEL:
            self.error = error
        if success is not SENTINEL:
            self.success = success
        self._kwargs = kwargs

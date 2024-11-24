from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class DataFiles2(BaseModel):
    """DataFiles2

    :param name: name, defaults to None
    :type name: str, optional
    :param size: size, defaults to None
    :type size: float, optional
    """

    def __init__(self, name: str = None, size: float = None):
        """DataFiles2

        :param name: name, defaults to None
        :type name: str, optional
        :param size: size, defaults to None
        :type size: float, optional
        """
        if name is not None:
            self.name = name
        if size is not None:
            self.size = size


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
        files: List[DataFiles2] = None,
        hash: str = None,
        name: str = None,
        size: float = None,
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
        if files is not None:
            self.files = self._define_list(files, DataFiles2)
        if hash is not None:
            self.hash = hash
        if name is not None:
            self.name = name
        if size is not None:
            self.size = size


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
        data: GetTorrentInfoOkResponseData = None,
        detail: str = None,
        error: any = None,
        success: bool = None,
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
        if data is not None:
            self.data = self._define_object(data, GetTorrentInfoOkResponseData)
        if detail is not None:
            self.detail = detail
        if error is not None:
            self.error = error
        if success is not None:
            self.success = success

from typing import Union
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.one_of_base_model import OneOfBaseModel


@JsonMap({})
class Data1Files(BaseModel):
    """Data1Files

    :param name: name, defaults to None
    :type name: str, optional
    :param size: size, defaults to None
    :type size: float, optional
    """

    def __init__(self, name: str = None, size: float = None):
        """Data1Files

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
class Data1(BaseModel):
    """Data1

    :param files: files, defaults to None
    :type files: List[Data1Files], optional
    :param hash: hash, defaults to None
    :type hash: str, optional
    :param name: name, defaults to None
    :type name: str, optional
    :param size: size, defaults to None
    :type size: float, optional
    """

    def __init__(
        self,
        files: List[Data1Files] = None,
        hash: str = None,
        name: str = None,
        size: float = None,
    ):
        """Data1

        :param files: files, defaults to None
        :type files: List[Data1Files], optional
        :param hash: hash, defaults to None
        :type hash: str, optional
        :param name: name, defaults to None
        :type name: str, optional
        :param size: size, defaults to None
        :type size: float, optional
        """
        if files is not None:
            self.files = self._define_list(files, Data1Files)
        if hash is not None:
            self.hash = hash
        if name is not None:
            self.name = name
        if size is not None:
            self.size = size


@JsonMap({})
class Xxxxxxxxxxxxxxxxxx(BaseModel):
    """Xxxxxxxxxxxxxxxxxx

    :param hash: hash, defaults to None
    :type hash: str, optional
    :param name: name, defaults to None
    :type name: str, optional
    :param size: size, defaults to None
    :type size: float, optional
    """

    def __init__(self, hash: str = None, name: str = None, size: float = None):
        """Xxxxxxxxxxxxxxxxxx

        :param hash: hash, defaults to None
        :type hash: str, optional
        :param name: name, defaults to None
        :type name: str, optional
        :param size: size, defaults to None
        :type size: float, optional
        """
        if hash is not None:
            self.hash = hash
        if name is not None:
            self.name = name
        if size is not None:
            self.size = size


@JsonMap({})
class Xxxxxxxxxxxxxxxxxxx(BaseModel):
    """Xxxxxxxxxxxxxxxxxxx

    :param hash: hash, defaults to None
    :type hash: str, optional
    :param name: name, defaults to None
    :type name: str, optional
    :param size: size, defaults to None
    :type size: float, optional
    """

    def __init__(self, hash: str = None, name: str = None, size: float = None):
        """Xxxxxxxxxxxxxxxxxxx

        :param hash: hash, defaults to None
        :type hash: str, optional
        :param name: name, defaults to None
        :type name: str, optional
        :param size: size, defaults to None
        :type size: float, optional
        """
        if hash is not None:
            self.hash = hash
        if name is not None:
            self.name = name
        if size is not None:
            self.size = size


@JsonMap(
    {
        "xxxxxxxxxxxxxxxxxx": "XXXXXXXXXXXXXXXXXX",
        "xxxxxxxxxxxxxxxxxxx": "XXXXXXXXXXXXXXXXXXX",
    }
)
class Data2(BaseModel):
    """Data2

    :param xxxxxxxxxxxxxxxxxx: xxxxxxxxxxxxxxxxxx, defaults to None
    :type xxxxxxxxxxxxxxxxxx: Xxxxxxxxxxxxxxxxxx, optional
    :param xxxxxxxxxxxxxxxxxxx: xxxxxxxxxxxxxxxxxxx, defaults to None
    :type xxxxxxxxxxxxxxxxxxx: Xxxxxxxxxxxxxxxxxxx, optional
    """

    def __init__(
        self,
        xxxxxxxxxxxxxxxxxx: Xxxxxxxxxxxxxxxxxx = None,
        xxxxxxxxxxxxxxxxxxx: Xxxxxxxxxxxxxxxxxxx = None,
    ):
        """Data2

        :param xxxxxxxxxxxxxxxxxx: xxxxxxxxxxxxxxxxxx, defaults to None
        :type xxxxxxxxxxxxxxxxxx: Xxxxxxxxxxxxxxxxxx, optional
        :param xxxxxxxxxxxxxxxxxxx: xxxxxxxxxxxxxxxxxxx, defaults to None
        :type xxxxxxxxxxxxxxxxxxx: Xxxxxxxxxxxxxxxxxxx, optional
        """
        if xxxxxxxxxxxxxxxxxx is not None:
            self.xxxxxxxxxxxxxxxxxx = self._define_object(
                xxxxxxxxxxxxxxxxxx, Xxxxxxxxxxxxxxxxxx
            )
        if xxxxxxxxxxxxxxxxxxx is not None:
            self.xxxxxxxxxxxxxxxxxxx = self._define_object(
                xxxxxxxxxxxxxxxxxxx, Xxxxxxxxxxxxxxxxxxx
            )


class GetTorrentCachedAvailabilityOkResponseDataGuard(OneOfBaseModel):
    class_list = {"List[Data1]": List[Data1], "Data2": Data2, "any": any}


GetTorrentCachedAvailabilityOkResponseData = Union[List[Data1], Data2, any]


@JsonMap({})
class GetTorrentCachedAvailabilityOkResponse(BaseModel):
    """GetTorrentCachedAvailabilityOkResponse

    :param data: data, defaults to None
    :type data: GetTorrentCachedAvailabilityOkResponseData, optional
    :param detail: detail, defaults to None
    :type detail: str, optional
    :param error: error, defaults to None
    :type error: str, optional
    :param success: success, defaults to None
    :type success: bool, optional
    """

    def __init__(
        self,
        data: GetTorrentCachedAvailabilityOkResponseData = None,
        detail: str = None,
        error: str = None,
        success: bool = None,
    ):
        """GetTorrentCachedAvailabilityOkResponse

        :param data: data, defaults to None
        :type data: GetTorrentCachedAvailabilityOkResponseData, optional
        :param detail: detail, defaults to None
        :type detail: str, optional
        :param error: error, defaults to None
        :type error: str, optional
        :param success: success, defaults to None
        :type success: bool, optional
        """
        if data is not None:
            self.data = GetTorrentCachedAvailabilityOkResponseDataGuard.return_one_of(
                data
            )
        if detail is not None:
            self.detail = detail
        if error is not None:
            self.error = self._define_str("error", error, nullable=True)
        if success is not None:
            self.success = success

from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class GetTorrentCachedAvailabilityOkResponseData(BaseModel):
    """GetTorrentCachedAvailabilityOkResponseData

    :param name: name, defaults to None
    :type name: str, optional
    :param size: size, defaults to None
    :type size: float, optional
    :param hash: hash, defaults to None
    :type hash: str, optional
    """

    def __init__(
        self,
        name: str = SENTINEL,
        size: float = SENTINEL,
        hash: str = SENTINEL,
        **kwargs
    ):
        """GetTorrentCachedAvailabilityOkResponseData

        :param name: name, defaults to None
        :type name: str, optional
        :param size: size, defaults to None
        :type size: float, optional
        :param hash: hash, defaults to None
        :type hash: str, optional
        """
        if name is not SENTINEL:
            self.name = name
        if size is not SENTINEL:
            self.size = size
        if hash is not SENTINEL:
            self.hash = hash
        self._kwargs = kwargs


@JsonMap({})
class GetTorrentCachedAvailabilityOkResponse(BaseModel):
    """GetTorrentCachedAvailabilityOkResponse

    :param data: data, defaults to None
    :type data: dict, optional
    :param detail: detail, defaults to None
    :type detail: str, optional
    :param error: error, defaults to None
    :type error: str, optional
    :param success: success, defaults to None
    :type success: bool, optional
    """

    def __init__(
        self,
        data: dict = SENTINEL,
        detail: str = SENTINEL,
        error: Union[str, None] = SENTINEL,
        success: bool = SENTINEL,
        **kwargs
    ):
        """GetTorrentCachedAvailabilityOkResponse

        :param data: data, defaults to None
        :type data: dict, optional
        :param detail: detail, defaults to None
        :type detail: str, optional
        :param error: error, defaults to None
        :type error: str, optional
        :param success: success, defaults to None
        :type success: bool, optional
        """
        if data is not SENTINEL:
            self.data = data
        if detail is not SENTINEL:
            self.detail = detail
        if error is not SENTINEL:
            self.error = self._define_str("error", error, nullable=True)
        if success is not SENTINEL:
            self.success = success
        self._kwargs = kwargs

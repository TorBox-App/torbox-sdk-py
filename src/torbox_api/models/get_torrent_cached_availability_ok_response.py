from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


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

    def __init__(self, name: str = None, size: float = None, hash: str = None):
        """GetTorrentCachedAvailabilityOkResponseData

        :param name: name, defaults to None
        :type name: str, optional
        :param size: size, defaults to None
        :type size: float, optional
        :param hash: hash, defaults to None
        :type hash: str, optional
        """
        if name is not None:
            self.name = name
        if size is not None:
            self.size = size
        if hash is not None:
            self.hash = hash


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
        data: dict = None,
        detail: str = None,
        error: str = None,
        success: bool = None,
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
        if data is not None:
            self.data = data
        if detail is not None:
            self.detail = detail
        if error is not None:
            self.error = self._define_str("error", error, nullable=True)
        if success is not None:
            self.success = success

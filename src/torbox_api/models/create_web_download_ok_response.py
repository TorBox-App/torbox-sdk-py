from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class CreateWebDownloadOkResponseData(BaseModel):
    """CreateWebDownloadOkResponseData

    :param auth_id: auth_id, defaults to None
    :type auth_id: str, optional
    :param hash: hash, defaults to None
    :type hash: str, optional
    :param webdownload_id: webdownload_id, defaults to None
    :type webdownload_id: str, optional
    """

    def __init__(
        self, auth_id: str = None, hash: str = None, webdownload_id: str = None
    ):
        """CreateWebDownloadOkResponseData

        :param auth_id: auth_id, defaults to None
        :type auth_id: str, optional
        :param hash: hash, defaults to None
        :type hash: str, optional
        :param webdownload_id: webdownload_id, defaults to None
        :type webdownload_id: str, optional
        """
        if auth_id is not None:
            self.auth_id = auth_id
        if hash is not None:
            self.hash = hash
        if webdownload_id is not None:
            self.webdownload_id = webdownload_id


@JsonMap({})
class CreateWebDownloadOkResponse(BaseModel):
    """CreateWebDownloadOkResponse

    :param data: data, defaults to None
    :type data: CreateWebDownloadOkResponseData, optional
    :param detail: detail, defaults to None
    :type detail: str, optional
    :param success: success, defaults to None
    :type success: bool, optional
    """

    def __init__(
        self,
        data: CreateWebDownloadOkResponseData = None,
        detail: str = None,
        success: bool = None,
    ):
        """CreateWebDownloadOkResponse

        :param data: data, defaults to None
        :type data: CreateWebDownloadOkResponseData, optional
        :param detail: detail, defaults to None
        :type detail: str, optional
        :param success: success, defaults to None
        :type success: bool, optional
        """
        if data is not None:
            self.data = self._define_object(data, CreateWebDownloadOkResponseData)
        if detail is not None:
            self.detail = detail
        if success is not None:
            self.success = success

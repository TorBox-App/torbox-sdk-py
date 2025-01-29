from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class CreateUsenetDownloadOkResponseData(BaseModel):
    """CreateUsenetDownloadOkResponseData

    :param auth_id: auth_id, defaults to None
    :type auth_id: str, optional
    :param hash: hash, defaults to None
    :type hash: str, optional
    :param usenetdownload_id: usenetdownload_id, defaults to None
    :type usenetdownload_id: str, optional
    """

    def __init__(
        self,
        auth_id: str = None,
        hash: str = None,
        usenetdownload_id: str = None,
        **kwargs
    ):
        """CreateUsenetDownloadOkResponseData

        :param auth_id: auth_id, defaults to None
        :type auth_id: str, optional
        :param hash: hash, defaults to None
        :type hash: str, optional
        :param usenetdownload_id: usenetdownload_id, defaults to None
        :type usenetdownload_id: str, optional
        """
        if auth_id is not None:
            self.auth_id = auth_id
        if hash is not None:
            self.hash = hash
        if usenetdownload_id is not None:
            self.usenetdownload_id = usenetdownload_id
        self._kwargs = kwargs


@JsonMap({})
class CreateUsenetDownloadOkResponse(BaseModel):
    """CreateUsenetDownloadOkResponse

    :param data: data, defaults to None
    :type data: CreateUsenetDownloadOkResponseData, optional
    :param detail: detail, defaults to None
    :type detail: str, optional
    :param error: error, defaults to None
    :type error: any, optional
    :param success: success, defaults to None
    :type success: bool, optional
    """

    def __init__(
        self,
        data: CreateUsenetDownloadOkResponseData = None,
        detail: str = None,
        error: any = None,
        success: bool = None,
        **kwargs
    ):
        """CreateUsenetDownloadOkResponse

        :param data: data, defaults to None
        :type data: CreateUsenetDownloadOkResponseData, optional
        :param detail: detail, defaults to None
        :type detail: str, optional
        :param error: error, defaults to None
        :type error: any, optional
        :param success: success, defaults to None
        :type success: bool, optional
        """
        if data is not None:
            self.data = self._define_object(data, CreateUsenetDownloadOkResponseData)
        if detail is not None:
            self.detail = detail
        if error is not None:
            self.error = error
        if success is not None:
            self.success = success
        self._kwargs = kwargs

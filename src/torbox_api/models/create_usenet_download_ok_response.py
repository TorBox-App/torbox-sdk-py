from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


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
        auth_id: str = SENTINEL,
        hash: str = SENTINEL,
        usenetdownload_id: str = SENTINEL,
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
        if auth_id is not SENTINEL:
            self.auth_id = auth_id
        if hash is not SENTINEL:
            self.hash = hash
        if usenetdownload_id is not SENTINEL:
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
        data: CreateUsenetDownloadOkResponseData = SENTINEL,
        detail: str = SENTINEL,
        error: Union[any, None] = SENTINEL,
        success: bool = SENTINEL,
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
        if data is not SENTINEL:
            self.data = self._define_object(data, CreateUsenetDownloadOkResponseData)
        if detail is not SENTINEL:
            self.detail = detail
        if error is not SENTINEL:
            self.error = error
        if success is not SENTINEL:
            self.success = success
        self._kwargs = kwargs

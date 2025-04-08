from typing import List
from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"id_": "id", "type_": "type"})
class GetAllJobsOkResponseData(BaseModel):
    """GetAllJobsOkResponseData

    :param auth_id: auth_id, defaults to None
    :type auth_id: str, optional
    :param created_at: created_at, defaults to None
    :type created_at: str, optional
    :param detail: detail, defaults to None
    :type detail: str, optional
    :param download_url: download_url, defaults to None
    :type download_url: str, optional
    :param file_id: file_id, defaults to None
    :type file_id: float, optional
    :param hash: hash, defaults to None
    :type hash: str, optional
    :param id_: id_, defaults to None
    :type id_: float, optional
    :param integration: integration, defaults to None
    :type integration: str, optional
    :param progress: progress, defaults to None
    :type progress: float, optional
    :param status: status, defaults to None
    :type status: str, optional
    :param type_: type_, defaults to None
    :type type_: str, optional
    :param updated_at: updated_at, defaults to None
    :type updated_at: str, optional
    :param zip: zip, defaults to None
    :type zip: bool, optional
    """

    def __init__(
        self,
        auth_id: str = SENTINEL,
        created_at: str = SENTINEL,
        detail: str = SENTINEL,
        download_url: Union[str, None] = SENTINEL,
        file_id: float = SENTINEL,
        hash: str = SENTINEL,
        id_: float = SENTINEL,
        integration: str = SENTINEL,
        progress: float = SENTINEL,
        status: str = SENTINEL,
        type_: str = SENTINEL,
        updated_at: str = SENTINEL,
        zip: bool = SENTINEL,
        **kwargs
    ):
        """GetAllJobsOkResponseData

        :param auth_id: auth_id, defaults to None
        :type auth_id: str, optional
        :param created_at: created_at, defaults to None
        :type created_at: str, optional
        :param detail: detail, defaults to None
        :type detail: str, optional
        :param download_url: download_url, defaults to None
        :type download_url: str, optional
        :param file_id: file_id, defaults to None
        :type file_id: float, optional
        :param hash: hash, defaults to None
        :type hash: str, optional
        :param id_: id_, defaults to None
        :type id_: float, optional
        :param integration: integration, defaults to None
        :type integration: str, optional
        :param progress: progress, defaults to None
        :type progress: float, optional
        :param status: status, defaults to None
        :type status: str, optional
        :param type_: type_, defaults to None
        :type type_: str, optional
        :param updated_at: updated_at, defaults to None
        :type updated_at: str, optional
        :param zip: zip, defaults to None
        :type zip: bool, optional
        """
        if auth_id is not SENTINEL:
            self.auth_id = auth_id
        if created_at is not SENTINEL:
            self.created_at = created_at
        if detail is not SENTINEL:
            self.detail = detail
        if download_url is not SENTINEL:
            self.download_url = self._define_str(
                "download_url", download_url, nullable=True
            )
        if file_id is not SENTINEL:
            self.file_id = file_id
        if hash is not SENTINEL:
            self.hash = hash
        if id_ is not SENTINEL:
            self.id_ = id_
        if integration is not SENTINEL:
            self.integration = integration
        if progress is not SENTINEL:
            self.progress = progress
        if status is not SENTINEL:
            self.status = status
        if type_ is not SENTINEL:
            self.type_ = type_
        if updated_at is not SENTINEL:
            self.updated_at = updated_at
        if zip is not SENTINEL:
            self.zip = zip
        self._kwargs = kwargs


@JsonMap({})
class GetAllJobsOkResponse(BaseModel):
    """GetAllJobsOkResponse

    :param data: data, defaults to None
    :type data: List[GetAllJobsOkResponseData], optional
    :param detail: detail, defaults to None
    :type detail: str, optional
    :param error: error, defaults to None
    :type error: any, optional
    :param success: success, defaults to None
    :type success: bool, optional
    """

    def __init__(
        self,
        data: List[GetAllJobsOkResponseData] = SENTINEL,
        detail: str = SENTINEL,
        error: Union[any, None] = SENTINEL,
        success: bool = SENTINEL,
        **kwargs
    ):
        """GetAllJobsOkResponse

        :param data: data, defaults to None
        :type data: List[GetAllJobsOkResponseData], optional
        :param detail: detail, defaults to None
        :type detail: str, optional
        :param error: error, defaults to None
        :type error: any, optional
        :param success: success, defaults to None
        :type success: bool, optional
        """
        if data is not SENTINEL:
            self.data = self._define_list(data, GetAllJobsOkResponseData)
        if detail is not SENTINEL:
            self.detail = detail
        if error is not SENTINEL:
            self.error = error
        if success is not SENTINEL:
            self.success = success
        self._kwargs = kwargs

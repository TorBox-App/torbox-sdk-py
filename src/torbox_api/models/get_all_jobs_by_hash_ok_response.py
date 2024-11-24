from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({"id_": "id", "type_": "type"})
class GetAllJobsByHashOkResponseData(BaseModel):
    """GetAllJobsByHashOkResponseData

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
        auth_id: str = None,
        created_at: str = None,
        detail: str = None,
        download_url: str = None,
        file_id: float = None,
        hash: str = None,
        id_: float = None,
        integration: str = None,
        progress: float = None,
        status: str = None,
        type_: str = None,
        updated_at: str = None,
        zip: bool = None,
    ):
        """GetAllJobsByHashOkResponseData

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
        if auth_id is not None:
            self.auth_id = auth_id
        if created_at is not None:
            self.created_at = created_at
        if detail is not None:
            self.detail = detail
        if download_url is not None:
            self.download_url = self._define_str(
                "download_url", download_url, nullable=True
            )
        if file_id is not None:
            self.file_id = file_id
        if hash is not None:
            self.hash = hash
        if id_ is not None:
            self.id_ = id_
        if integration is not None:
            self.integration = integration
        if progress is not None:
            self.progress = progress
        if status is not None:
            self.status = status
        if type_ is not None:
            self.type_ = type_
        if updated_at is not None:
            self.updated_at = updated_at
        if zip is not None:
            self.zip = zip


@JsonMap({})
class GetAllJobsByHashOkResponse(BaseModel):
    """GetAllJobsByHashOkResponse

    :param data: data, defaults to None
    :type data: List[GetAllJobsByHashOkResponseData], optional
    :param detail: detail, defaults to None
    :type detail: str, optional
    :param success: success, defaults to None
    :type success: bool, optional
    """

    def __init__(
        self,
        data: List[GetAllJobsByHashOkResponseData] = None,
        detail: str = None,
        success: bool = None,
    ):
        """GetAllJobsByHashOkResponse

        :param data: data, defaults to None
        :type data: List[GetAllJobsByHashOkResponseData], optional
        :param detail: detail, defaults to None
        :type detail: str, optional
        :param success: success, defaults to None
        :type success: bool, optional
        """
        if data is not None:
            self.data = self._define_list(data, GetAllJobsByHashOkResponseData)
        if detail is not None:
            self.detail = detail
        if success is not None:
            self.success = success

from typing import List
from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"id_": "id"})
class DataFiles3(BaseModel):
    """DataFiles3

    :param id_: id_, defaults to None
    :type id_: float, optional
    :param md5: md5, defaults to None
    :type md5: str, optional
    :param mimetype: mimetype, defaults to None
    :type mimetype: str, optional
    :param name: name, defaults to None
    :type name: str, optional
    :param s3_path: s3_path, defaults to None
    :type s3_path: str, optional
    :param short_name: short_name, defaults to None
    :type short_name: str, optional
    :param size: size, defaults to None
    :type size: float, optional
    """

    def __init__(
        self,
        id_: float = SENTINEL,
        md5: str = SENTINEL,
        mimetype: str = SENTINEL,
        name: str = SENTINEL,
        s3_path: str = SENTINEL,
        short_name: str = SENTINEL,
        size: float = SENTINEL,
        **kwargs
    ):
        """DataFiles3

        :param id_: id_, defaults to None
        :type id_: float, optional
        :param md5: md5, defaults to None
        :type md5: str, optional
        :param mimetype: mimetype, defaults to None
        :type mimetype: str, optional
        :param name: name, defaults to None
        :type name: str, optional
        :param s3_path: s3_path, defaults to None
        :type s3_path: str, optional
        :param short_name: short_name, defaults to None
        :type short_name: str, optional
        :param size: size, defaults to None
        :type size: float, optional
        """
        if id_ is not SENTINEL:
            self.id_ = id_
        if md5 is not SENTINEL:
            self.md5 = md5
        if mimetype is not SENTINEL:
            self.mimetype = mimetype
        if name is not SENTINEL:
            self.name = name
        if s3_path is not SENTINEL:
            self.s3_path = s3_path
        if short_name is not SENTINEL:
            self.short_name = short_name
        if size is not SENTINEL:
            self.size = size
        self._kwargs = kwargs


@JsonMap({"id_": "id"})
class GetUsenetListOkResponseData(BaseModel):
    """GetUsenetListOkResponseData

    :param active: active, defaults to None
    :type active: bool, optional
    :param auth_id: auth_id, defaults to None
    :type auth_id: str, optional
    :param availability: availability, defaults to None
    :type availability: float, optional
    :param created_at: created_at, defaults to None
    :type created_at: str, optional
    :param download_finished: download_finished, defaults to None
    :type download_finished: bool, optional
    :param download_present: download_present, defaults to None
    :type download_present: bool, optional
    :param download_speed: download_speed, defaults to None
    :type download_speed: float, optional
    :param download_state: download_state, defaults to None
    :type download_state: str, optional
    :param eta: eta, defaults to None
    :type eta: float, optional
    :param expires_at: expires_at, defaults to None
    :type expires_at: str, optional
    :param files: files, defaults to None
    :type files: List[DataFiles3], optional
    :param hash: hash, defaults to None
    :type hash: str, optional
    :param id_: id_, defaults to None
    :type id_: float, optional
    :param inactive_check: inactive_check, defaults to None
    :type inactive_check: float, optional
    :param name: name, defaults to None
    :type name: str, optional
    :param progress: progress, defaults to None
    :type progress: float, optional
    :param server: server, defaults to None
    :type server: float, optional
    :param size: size, defaults to None
    :type size: float, optional
    :param torrent_file: torrent_file, defaults to None
    :type torrent_file: bool, optional
    :param updated_at: updated_at, defaults to None
    :type updated_at: str, optional
    :param upload_speed: upload_speed, defaults to None
    :type upload_speed: float, optional
    """

    def __init__(
        self,
        active: bool = SENTINEL,
        auth_id: str = SENTINEL,
        availability: float = SENTINEL,
        created_at: str = SENTINEL,
        download_finished: bool = SENTINEL,
        download_present: bool = SENTINEL,
        download_speed: float = SENTINEL,
        download_state: str = SENTINEL,
        eta: float = SENTINEL,
        expires_at: str = SENTINEL,
        files: List[DataFiles3] = SENTINEL,
        hash: str = SENTINEL,
        id_: float = SENTINEL,
        inactive_check: float = SENTINEL,
        name: str = SENTINEL,
        progress: float = SENTINEL,
        server: float = SENTINEL,
        size: float = SENTINEL,
        torrent_file: bool = SENTINEL,
        updated_at: str = SENTINEL,
        upload_speed: float = SENTINEL,
        **kwargs
    ):
        """GetUsenetListOkResponseData

        :param active: active, defaults to None
        :type active: bool, optional
        :param auth_id: auth_id, defaults to None
        :type auth_id: str, optional
        :param availability: availability, defaults to None
        :type availability: float, optional
        :param created_at: created_at, defaults to None
        :type created_at: str, optional
        :param download_finished: download_finished, defaults to None
        :type download_finished: bool, optional
        :param download_present: download_present, defaults to None
        :type download_present: bool, optional
        :param download_speed: download_speed, defaults to None
        :type download_speed: float, optional
        :param download_state: download_state, defaults to None
        :type download_state: str, optional
        :param eta: eta, defaults to None
        :type eta: float, optional
        :param expires_at: expires_at, defaults to None
        :type expires_at: str, optional
        :param files: files, defaults to None
        :type files: List[DataFiles3], optional
        :param hash: hash, defaults to None
        :type hash: str, optional
        :param id_: id_, defaults to None
        :type id_: float, optional
        :param inactive_check: inactive_check, defaults to None
        :type inactive_check: float, optional
        :param name: name, defaults to None
        :type name: str, optional
        :param progress: progress, defaults to None
        :type progress: float, optional
        :param server: server, defaults to None
        :type server: float, optional
        :param size: size, defaults to None
        :type size: float, optional
        :param torrent_file: torrent_file, defaults to None
        :type torrent_file: bool, optional
        :param updated_at: updated_at, defaults to None
        :type updated_at: str, optional
        :param upload_speed: upload_speed, defaults to None
        :type upload_speed: float, optional
        """
        if active is not SENTINEL:
            self.active = active
        if auth_id is not SENTINEL:
            self.auth_id = auth_id
        if availability is not SENTINEL:
            self.availability = availability
        if created_at is not SENTINEL:
            self.created_at = created_at
        if download_finished is not SENTINEL:
            self.download_finished = download_finished
        if download_present is not SENTINEL:
            self.download_present = download_present
        if download_speed is not SENTINEL:
            self.download_speed = download_speed
        if download_state is not SENTINEL:
            self.download_state = download_state
        if eta is not SENTINEL:
            self.eta = eta
        if expires_at is not SENTINEL:
            self.expires_at = expires_at
        if files is not SENTINEL:
            self.files = self._define_list(files, DataFiles3)
        if hash is not SENTINEL:
            self.hash = hash
        if id_ is not SENTINEL:
            self.id_ = id_
        if inactive_check is not SENTINEL:
            self.inactive_check = inactive_check
        if name is not SENTINEL:
            self.name = name
        if progress is not SENTINEL:
            self.progress = progress
        if server is not SENTINEL:
            self.server = server
        if size is not SENTINEL:
            self.size = size
        if torrent_file is not SENTINEL:
            self.torrent_file = torrent_file
        if updated_at is not SENTINEL:
            self.updated_at = updated_at
        if upload_speed is not SENTINEL:
            self.upload_speed = upload_speed
        self._kwargs = kwargs


@JsonMap({})
class GetUsenetListOkResponse(BaseModel):
    """GetUsenetListOkResponse

    :param data: data, defaults to None
    :type data: List[GetUsenetListOkResponseData], optional
    :param detail: detail, defaults to None
    :type detail: str, optional
    :param error: error, defaults to None
    :type error: any, optional
    :param success: success, defaults to None
    :type success: bool, optional
    """

    def __init__(
        self,
        data: List[GetUsenetListOkResponseData] = SENTINEL,
        detail: str = SENTINEL,
        error: Union[any, None] = SENTINEL,
        success: bool = SENTINEL,
        **kwargs
    ):
        """GetUsenetListOkResponse

        :param data: data, defaults to None
        :type data: List[GetUsenetListOkResponseData], optional
        :param detail: detail, defaults to None
        :type detail: str, optional
        :param error: error, defaults to None
        :type error: any, optional
        :param success: success, defaults to None
        :type success: bool, optional
        """
        if data is not SENTINEL:
            self.data = self._define_list(data, GetUsenetListOkResponseData)
        if detail is not SENTINEL:
            self.detail = detail
        if error is not SENTINEL:
            self.error = error
        if success is not SENTINEL:
            self.success = success
        self._kwargs = kwargs

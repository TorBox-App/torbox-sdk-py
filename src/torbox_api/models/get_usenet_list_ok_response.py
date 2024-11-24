from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


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
        id_: float = None,
        md5: str = None,
        mimetype: str = None,
        name: str = None,
        s3_path: str = None,
        short_name: str = None,
        size: float = None,
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
        if id_ is not None:
            self.id_ = id_
        if md5 is not None:
            self.md5 = md5
        if mimetype is not None:
            self.mimetype = mimetype
        if name is not None:
            self.name = name
        if s3_path is not None:
            self.s3_path = s3_path
        if short_name is not None:
            self.short_name = short_name
        if size is not None:
            self.size = size


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
        active: bool = None,
        auth_id: str = None,
        availability: float = None,
        created_at: str = None,
        download_finished: bool = None,
        download_present: bool = None,
        download_speed: float = None,
        download_state: str = None,
        eta: float = None,
        expires_at: str = None,
        files: List[DataFiles3] = None,
        hash: str = None,
        id_: float = None,
        inactive_check: float = None,
        name: str = None,
        progress: float = None,
        server: float = None,
        size: float = None,
        torrent_file: bool = None,
        updated_at: str = None,
        upload_speed: float = None,
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
        if active is not None:
            self.active = active
        if auth_id is not None:
            self.auth_id = auth_id
        if availability is not None:
            self.availability = availability
        if created_at is not None:
            self.created_at = created_at
        if download_finished is not None:
            self.download_finished = download_finished
        if download_present is not None:
            self.download_present = download_present
        if download_speed is not None:
            self.download_speed = download_speed
        if download_state is not None:
            self.download_state = download_state
        if eta is not None:
            self.eta = eta
        if expires_at is not None:
            self.expires_at = expires_at
        if files is not None:
            self.files = self._define_list(files, DataFiles3)
        if hash is not None:
            self.hash = hash
        if id_ is not None:
            self.id_ = id_
        if inactive_check is not None:
            self.inactive_check = inactive_check
        if name is not None:
            self.name = name
        if progress is not None:
            self.progress = progress
        if server is not None:
            self.server = server
        if size is not None:
            self.size = size
        if torrent_file is not None:
            self.torrent_file = torrent_file
        if updated_at is not None:
            self.updated_at = updated_at
        if upload_speed is not None:
            self.upload_speed = upload_speed


@JsonMap({})
class GetUsenetListOkResponse(BaseModel):
    """GetUsenetListOkResponse

    :param data: data, defaults to None
    :type data: List[GetUsenetListOkResponseData], optional
    :param detail: detail, defaults to None
    :type detail: str, optional
    :param success: success, defaults to None
    :type success: bool, optional
    """

    def __init__(
        self,
        data: List[GetUsenetListOkResponseData] = None,
        detail: str = None,
        success: bool = None,
    ):
        """GetUsenetListOkResponse

        :param data: data, defaults to None
        :type data: List[GetUsenetListOkResponseData], optional
        :param detail: detail, defaults to None
        :type detail: str, optional
        :param success: success, defaults to None
        :type success: bool, optional
        """
        if data is not None:
            self.data = self._define_list(data, GetUsenetListOkResponseData)
        if detail is not None:
            self.detail = detail
        if success is not None:
            self.success = success

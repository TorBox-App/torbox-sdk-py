from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({"id_": "id"})
class SearchAllTorrentsFromScraperOkResponseData(BaseModel):
    """SearchAllTorrentsFromScraperOkResponseData

    :param categories: categories, defaults to None
    :type categories: List[str], optional
    :param hash: hash, defaults to None
    :type hash: str, optional
    :param id_: id_, defaults to None
    :type id_: str, optional
    :param magnet: magnet, defaults to None
    :type magnet: str, optional
    :param name: name, defaults to None
    :type name: str, optional
    :param peers: peers, defaults to None
    :type peers: float, optional
    :param preferred_type: preferred_type, defaults to None
    :type preferred_type: str, optional
    :param seeders: seeders, defaults to None
    :type seeders: float, optional
    :param size: size, defaults to None
    :type size: float, optional
    :param source: source, defaults to None
    :type source: str, optional
    :param torrent_file: torrent_file, defaults to None
    :type torrent_file: str, optional
    :param updated_at: updated_at, defaults to None
    :type updated_at: str, optional
    :param website: website, defaults to None
    :type website: str, optional
    """

    def __init__(
        self,
        categories: List[str] = None,
        hash: str = None,
        id_: str = None,
        magnet: str = None,
        name: str = None,
        peers: float = None,
        preferred_type: str = None,
        seeders: float = None,
        size: float = None,
        source: str = None,
        torrent_file: str = None,
        updated_at: str = None,
        website: str = None,
    ):
        """SearchAllTorrentsFromScraperOkResponseData

        :param categories: categories, defaults to None
        :type categories: List[str], optional
        :param hash: hash, defaults to None
        :type hash: str, optional
        :param id_: id_, defaults to None
        :type id_: str, optional
        :param magnet: magnet, defaults to None
        :type magnet: str, optional
        :param name: name, defaults to None
        :type name: str, optional
        :param peers: peers, defaults to None
        :type peers: float, optional
        :param preferred_type: preferred_type, defaults to None
        :type preferred_type: str, optional
        :param seeders: seeders, defaults to None
        :type seeders: float, optional
        :param size: size, defaults to None
        :type size: float, optional
        :param source: source, defaults to None
        :type source: str, optional
        :param torrent_file: torrent_file, defaults to None
        :type torrent_file: str, optional
        :param updated_at: updated_at, defaults to None
        :type updated_at: str, optional
        :param website: website, defaults to None
        :type website: str, optional
        """
        if categories is not None:
            self.categories = categories
        if hash is not None:
            self.hash = hash
        if id_ is not None:
            self.id_ = id_
        if magnet is not None:
            self.magnet = magnet
        if name is not None:
            self.name = name
        if peers is not None:
            self.peers = peers
        if preferred_type is not None:
            self.preferred_type = preferred_type
        if seeders is not None:
            self.seeders = seeders
        if size is not None:
            self.size = size
        if source is not None:
            self.source = source
        if torrent_file is not None:
            self.torrent_file = torrent_file
        if updated_at is not None:
            self.updated_at = updated_at
        if website is not None:
            self.website = website


@JsonMap({})
class SearchAllTorrentsFromScraperOkResponse(BaseModel):
    """SearchAllTorrentsFromScraperOkResponse

    :param data: data, defaults to None
    :type data: List[SearchAllTorrentsFromScraperOkResponseData], optional
    :param detail: detail, defaults to None
    :type detail: str, optional
    :param error: error, defaults to None
    :type error: any, optional
    :param success: success, defaults to None
    :type success: bool, optional
    """

    def __init__(
        self,
        data: List[SearchAllTorrentsFromScraperOkResponseData] = None,
        detail: str = None,
        error: any = None,
        success: bool = None,
    ):
        """SearchAllTorrentsFromScraperOkResponse

        :param data: data, defaults to None
        :type data: List[SearchAllTorrentsFromScraperOkResponseData], optional
        :param detail: detail, defaults to None
        :type detail: str, optional
        :param error: error, defaults to None
        :type error: any, optional
        :param success: success, defaults to None
        :type success: bool, optional
        """
        if data is not None:
            self.data = self._define_list(
                data, SearchAllTorrentsFromScraperOkResponseData
            )
        if detail is not None:
            self.detail = detail
        if error is not None:
            self.error = error
        if success is not None:
            self.success = success

from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class CreateTorrentRequest(BaseModel):
    """CreateTorrentRequest

    :param file: The torrent's torrent file. Optional., defaults to None
    :type file: bytes, optional
    :param magnet: The torrent's magnet link. Optional., defaults to None
    :type magnet: str, optional
    """

    def __init__(self, file: bytes = None, magnet: str = None):
        """CreateTorrentRequest

        :param file: The torrent's torrent file. Optional., defaults to None
        :type file: bytes, optional
        :param magnet: The torrent's magnet link. Optional., defaults to None
        :type magnet: str, optional
        """
        if file is not None:
            self.file = file
        if magnet is not None:
            self.magnet = magnet

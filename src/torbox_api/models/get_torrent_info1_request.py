from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class GetTorrentInfo1Request(BaseModel):
    """GetTorrentInfo1Request

    :param hash: Hash of the torrent you want to get info for. This is required., defaults to None
    :type hash: str, optional
    """

    def __init__(self, hash: str = SENTINEL, **kwargs):
        """GetTorrentInfo1Request

        :param hash: Hash of the torrent you want to get info for. This is required., defaults to None
        :type hash: str, optional
        """
        if hash is not SENTINEL:
            self.hash = hash
        self._kwargs = kwargs

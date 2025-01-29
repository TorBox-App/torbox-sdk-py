from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class CreateTorrentRequest(BaseModel):
    """CreateTorrentRequest

    :param allow_zip: Tells TorBox if you want to allow this torrent to be zipped or not. TorBox only zips if the torrent is 100 files or larger., defaults to None
    :type allow_zip: str, optional
    :param as_queued: Tells TorBox you want this torrent instantly queued. This is bypassed if user is on free plan, and will process the request as normal in this case. Optional., defaults to None
    :type as_queued: str, optional
    :param file: The torrent's torrent file. Optional., defaults to None
    :type file: bytes, optional
    :param magnet: The torrent's magnet link. Optional., defaults to None
    :type magnet: str, optional
    :param name: The name you want the torrent to be. Optional., defaults to None
    :type name: str, optional
    :param seed: Tells TorBox your preference for seeding this torrent. 1 is auto. 2 is seed. 3 is don't seed. Optional. Default is 1, or whatever the user has in their settings. Overwrites option in settings., defaults to None
    :type seed: str, optional
    """

    def __init__(
        self,
        allow_zip: str = None,
        as_queued: str = None,
        file: bytes = None,
        magnet: str = None,
        name: str = None,
        seed: str = None,
        **kwargs
    ):
        """CreateTorrentRequest

        :param allow_zip: Tells TorBox if you want to allow this torrent to be zipped or not. TorBox only zips if the torrent is 100 files or larger., defaults to None
        :type allow_zip: str, optional
        :param as_queued: Tells TorBox you want this torrent instantly queued. This is bypassed if user is on free plan, and will process the request as normal in this case. Optional., defaults to None
        :type as_queued: str, optional
        :param file: The torrent's torrent file. Optional., defaults to None
        :type file: bytes, optional
        :param magnet: The torrent's magnet link. Optional., defaults to None
        :type magnet: str, optional
        :param name: The name you want the torrent to be. Optional., defaults to None
        :type name: str, optional
        :param seed: Tells TorBox your preference for seeding this torrent. 1 is auto. 2 is seed. 3 is don't seed. Optional. Default is 1, or whatever the user has in their settings. Overwrites option in settings., defaults to None
        :type seed: str, optional
        """
        if allow_zip is not None:
            self.allow_zip = allow_zip
        if as_queued is not None:
            self.as_queued = as_queued
        if file is not None:
            self.file = file
        if magnet is not None:
            self.magnet = magnet
        if name is not None:
            self.name = name
        if seed is not None:
            self.seed = seed
        self._kwargs = kwargs

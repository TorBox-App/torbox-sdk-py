from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class CreateUsenetDownloadRequest(BaseModel):
    """CreateUsenetDownloadRequest

    :param file: An NZB File. Optional., defaults to None
    :type file: bytes, optional
    :param link: An accessible link to an NZB file. Cannot be a redirection. Optional., defaults to None
    :type link: str, optional
    """

    def __init__(self, file: bytes = None, link: str = None):
        """CreateUsenetDownloadRequest

        :param file: An NZB File. Optional., defaults to None
        :type file: bytes, optional
        :param link: An accessible link to an NZB file. Cannot be a redirection. Optional., defaults to None
        :type link: str, optional
        """
        if file is not None:
            self.file = file
        if link is not None:
            self.link = link

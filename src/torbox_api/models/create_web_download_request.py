from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class CreateWebDownloadRequest(BaseModel):
    """CreateWebDownloadRequest

    :param link: An accessible link to any file on the internet. Cannot be a redirection., defaults to None
    :type link: str, optional
    """

    def __init__(self, link: str = SENTINEL, **kwargs):
        """CreateWebDownloadRequest

        :param link: An accessible link to any file on the internet. Cannot be a redirection., defaults to None
        :type link: str, optional
        """
        if link is not SENTINEL:
            self.link = link
        self._kwargs = kwargs

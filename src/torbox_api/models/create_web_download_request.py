from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class CreateWebDownloadRequest(BaseModel):
    """CreateWebDownloadRequest

    :param link: An accessible link to any file on the internet. Cannot be a redirection., defaults to None
    :type link: str, optional
    """

    def __init__(self, link: str = None):
        """CreateWebDownloadRequest

        :param link: An accessible link to any file on the internet. Cannot be a redirection., defaults to None
        :type link: str, optional
        """
        if link is not None:
            self.link = link

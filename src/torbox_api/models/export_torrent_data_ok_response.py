from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class ExportTorrentDataOkResponse(BaseModel):
    """ExportTorrentDataOkResponse

    :param data: data, defaults to None
    :type data: str, optional
    :param detail: detail, defaults to None
    :type detail: str, optional
    """

    def __init__(self, data: str = None, detail: str = None):
        """ExportTorrentDataOkResponse

        :param data: data, defaults to None
        :type data: str, optional
        :param detail: detail, defaults to None
        :type detail: str, optional
        """
        if data is not None:
            self.data = data
        if detail is not None:
            self.detail = detail

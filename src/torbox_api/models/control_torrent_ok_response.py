from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class ControlTorrentOkResponse(BaseModel):
    """ControlTorrentOkResponse

    :param data: data, defaults to None
    :type data: any, optional
    :param detail: detail, defaults to None
    :type detail: str, optional
    :param success: success, defaults to None
    :type success: bool, optional
    """

    def __init__(self, data: any = None, detail: str = None, success: bool = None):
        """ControlTorrentOkResponse

        :param data: data, defaults to None
        :type data: any, optional
        :param detail: detail, defaults to None
        :type detail: str, optional
        :param success: success, defaults to None
        :type success: bool, optional
        """
        if data is not None:
            self.data = data
        if detail is not None:
            self.detail = detail
        if success is not None:
            self.success = success

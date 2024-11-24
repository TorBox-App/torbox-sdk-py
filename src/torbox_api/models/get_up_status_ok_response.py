from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class GetUpStatusOkResponse(BaseModel):
    """GetUpStatusOkResponse

    :param detail: detail, defaults to None
    :type detail: str, optional
    """

    def __init__(self, detail: str = None):
        """GetUpStatusOkResponse

        :param detail: detail, defaults to None
        :type detail: str, optional
        """
        if detail is not None:
            self.detail = detail

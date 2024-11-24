from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({"id_": "id"})
class GetNotificationFeedOkResponseData(BaseModel):
    """GetNotificationFeedOkResponseData

    :param auth_id: auth_id, defaults to None
    :type auth_id: str, optional
    :param created_at: created_at, defaults to None
    :type created_at: str, optional
    :param id_: id_, defaults to None
    :type id_: float, optional
    :param message: message, defaults to None
    :type message: str, optional
    :param title: title, defaults to None
    :type title: str, optional
    """

    def __init__(
        self,
        auth_id: str = None,
        created_at: str = None,
        id_: float = None,
        message: str = None,
        title: str = None,
    ):
        """GetNotificationFeedOkResponseData

        :param auth_id: auth_id, defaults to None
        :type auth_id: str, optional
        :param created_at: created_at, defaults to None
        :type created_at: str, optional
        :param id_: id_, defaults to None
        :type id_: float, optional
        :param message: message, defaults to None
        :type message: str, optional
        :param title: title, defaults to None
        :type title: str, optional
        """
        if auth_id is not None:
            self.auth_id = auth_id
        if created_at is not None:
            self.created_at = created_at
        if id_ is not None:
            self.id_ = id_
        if message is not None:
            self.message = message
        if title is not None:
            self.title = title


@JsonMap({})
class GetNotificationFeedOkResponse(BaseModel):
    """GetNotificationFeedOkResponse

    :param data: data, defaults to None
    :type data: List[GetNotificationFeedOkResponseData], optional
    :param detail: detail, defaults to None
    :type detail: str, optional
    """

    def __init__(
        self, data: List[GetNotificationFeedOkResponseData] = None, detail: str = None
    ):
        """GetNotificationFeedOkResponse

        :param data: data, defaults to None
        :type data: List[GetNotificationFeedOkResponseData], optional
        :param detail: detail, defaults to None
        :type detail: str, optional
        """
        if data is not None:
            self.data = self._define_list(data, GetNotificationFeedOkResponseData)
        if detail is not None:
            self.detail = detail

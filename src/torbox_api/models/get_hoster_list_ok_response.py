from typing import List
from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"type_": "type"})
class GetHosterListOkResponseData(BaseModel):
    """GetHosterListOkResponseData

    :param daily_bandwidth_limit: daily_bandwidth_limit, defaults to None
    :type daily_bandwidth_limit: float, optional
    :param daily_bandwidth_used: daily_bandwidth_used, defaults to None
    :type daily_bandwidth_used: float, optional
    :param daily_link_limit: daily_link_limit, defaults to None
    :type daily_link_limit: float, optional
    :param daily_link_used: daily_link_used, defaults to None
    :type daily_link_used: float, optional
    :param domains: domains, defaults to None
    :type domains: List[str], optional
    :param domais: domais, defaults to None
    :type domais: List[str], optional
    :param domaisn: domaisn, defaults to None
    :type domaisn: List[str], optional
    :param icon: icon, defaults to None
    :type icon: str, optional
    :param limit: limit, defaults to None
    :type limit: float, optional
    :param name: name, defaults to None
    :type name: str, optional
    :param note: note, defaults to None
    :type note: str, optional
    :param status: status, defaults to None
    :type status: bool, optional
    :param type_: type_, defaults to None
    :type type_: str, optional
    :param url: url, defaults to None
    :type url: str, optional
    """

    def __init__(
        self,
        daily_bandwidth_limit: float = SENTINEL,
        daily_bandwidth_used: float = SENTINEL,
        daily_link_limit: float = SENTINEL,
        daily_link_used: float = SENTINEL,
        domains: List[str] = SENTINEL,
        domais: List[str] = SENTINEL,
        domaisn: List[str] = SENTINEL,
        icon: str = SENTINEL,
        limit: float = SENTINEL,
        name: str = SENTINEL,
        note: Union[str, None] = SENTINEL,
        status: bool = SENTINEL,
        type_: str = SENTINEL,
        url: str = SENTINEL,
        **kwargs
    ):
        """GetHosterListOkResponseData

        :param daily_bandwidth_limit: daily_bandwidth_limit, defaults to None
        :type daily_bandwidth_limit: float, optional
        :param daily_bandwidth_used: daily_bandwidth_used, defaults to None
        :type daily_bandwidth_used: float, optional
        :param daily_link_limit: daily_link_limit, defaults to None
        :type daily_link_limit: float, optional
        :param daily_link_used: daily_link_used, defaults to None
        :type daily_link_used: float, optional
        :param domains: domains, defaults to None
        :type domains: List[str], optional
        :param domais: domais, defaults to None
        :type domais: List[str], optional
        :param domaisn: domaisn, defaults to None
        :type domaisn: List[str], optional
        :param icon: icon, defaults to None
        :type icon: str, optional
        :param limit: limit, defaults to None
        :type limit: float, optional
        :param name: name, defaults to None
        :type name: str, optional
        :param note: note, defaults to None
        :type note: str, optional
        :param status: status, defaults to None
        :type status: bool, optional
        :param type_: type_, defaults to None
        :type type_: str, optional
        :param url: url, defaults to None
        :type url: str, optional
        """
        if daily_bandwidth_limit is not SENTINEL:
            self.daily_bandwidth_limit = daily_bandwidth_limit
        if daily_bandwidth_used is not SENTINEL:
            self.daily_bandwidth_used = daily_bandwidth_used
        if daily_link_limit is not SENTINEL:
            self.daily_link_limit = daily_link_limit
        if daily_link_used is not SENTINEL:
            self.daily_link_used = daily_link_used
        if domains is not SENTINEL:
            self.domains = domains
        if domais is not SENTINEL:
            self.domais = domais
        if domaisn is not SENTINEL:
            self.domaisn = domaisn
        if icon is not SENTINEL:
            self.icon = icon
        if limit is not SENTINEL:
            self.limit = limit
        if name is not SENTINEL:
            self.name = name
        if note is not SENTINEL:
            self.note = self._define_str("note", note, nullable=True)
        if status is not SENTINEL:
            self.status = status
        if type_ is not SENTINEL:
            self.type_ = type_
        if url is not SENTINEL:
            self.url = url
        self._kwargs = kwargs


@JsonMap({})
class GetHosterListOkResponse(BaseModel):
    """GetHosterListOkResponse

    :param data: data, defaults to None
    :type data: List[GetHosterListOkResponseData], optional
    :param detail: detail, defaults to None
    :type detail: str, optional
    :param error: error, defaults to None
    :type error: any, optional
    :param success: success, defaults to None
    :type success: bool, optional
    """

    def __init__(
        self,
        data: List[GetHosterListOkResponseData] = SENTINEL,
        detail: str = SENTINEL,
        error: Union[any, None] = SENTINEL,
        success: bool = SENTINEL,
        **kwargs
    ):
        """GetHosterListOkResponse

        :param data: data, defaults to None
        :type data: List[GetHosterListOkResponseData], optional
        :param detail: detail, defaults to None
        :type detail: str, optional
        :param error: error, defaults to None
        :type error: any, optional
        :param success: success, defaults to None
        :type success: bool, optional
        """
        if data is not SENTINEL:
            self.data = self._define_list(data, GetHosterListOkResponseData)
        if detail is not SENTINEL:
            self.detail = detail
        if error is not SENTINEL:
            self.error = error
        if success is not SENTINEL:
            self.success = success
        self._kwargs = kwargs

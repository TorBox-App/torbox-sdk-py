from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


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
        daily_bandwidth_limit: float = None,
        daily_bandwidth_used: float = None,
        daily_link_limit: float = None,
        daily_link_used: float = None,
        domains: List[str] = None,
        domais: List[str] = None,
        domaisn: List[str] = None,
        icon: str = None,
        limit: float = None,
        name: str = None,
        note: str = None,
        status: bool = None,
        type_: str = None,
        url: str = None,
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
        if daily_bandwidth_limit is not None:
            self.daily_bandwidth_limit = daily_bandwidth_limit
        if daily_bandwidth_used is not None:
            self.daily_bandwidth_used = daily_bandwidth_used
        if daily_link_limit is not None:
            self.daily_link_limit = daily_link_limit
        if daily_link_used is not None:
            self.daily_link_used = daily_link_used
        if domains is not None:
            self.domains = domains
        if domais is not None:
            self.domais = domais
        if domaisn is not None:
            self.domaisn = domaisn
        if icon is not None:
            self.icon = icon
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if note is not None:
            self.note = self._define_str("note", note, nullable=True)
        if status is not None:
            self.status = status
        if type_ is not None:
            self.type_ = type_
        if url is not None:
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
        data: List[GetHosterListOkResponseData] = None,
        detail: str = None,
        error: any = None,
        success: bool = None,
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
        if data is not None:
            self.data = self._define_list(data, GetHosterListOkResponseData)
        if detail is not None:
            self.detail = detail
        if error is not None:
            self.error = error
        if success is not None:
            self.success = success
        self._kwargs = kwargs

from typing import List, Optional
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel

@JsonMap({"type_": "type"})
class Hoster(BaseModel):
    """Hoster"""
    def __init__(self,
                 name: str = None,
                 domain: List[str] = None,
                 url: str = None,
                 icon: str = None,
                 status: bool = None,
                 type_: str = None,
                 note: str = None,
                 daily_link_limit: int = None,
                 daily_link_used: int = None,
                 daily_bandwidth_limit: int = None,
                 daily_bandwidth_used: int = None):
        """Hoster

        :param name: name, defaults to None
        :type name: str, optional
        """
        if name is not None:
            self.name = name
        if domain is not None:
            self.domain = domain
        if url is not None:
            self.url = url
        if icon is not None:
            self.icon = icon
        if status is not None:
            self.status = status
        if type_ is not None:
            self.type_ = type_
        if note is not None:
            self.note = note
        if daily_link_limit is not None:
            self.daily_link_limit = daily_link_limit
        if daily_link_used is not None:
            self.daily_link_used = daily_link_used
        if daily_bandwidth_limit is not None:
            self.daily_bandwidth_limit = daily_bandwidth_limit
        if daily_bandwidth_used is not None:
            self.daily_bandwidth_used = daily_bandwidth_used


@JsonMap({"type_": "type"})
class GetWebDownloadHostersOkResponse(BaseModel):
    """GetWebDownloadHosters"""

    def __init__(
            self,
            data: List[Hoster] = None,
            detail: str = None,
            error: any = None,
            success: bool = None,
    ):
        """GetWebDownloadListOkResponse

        :param data: data, defaults to None
        :type data: List[Hoster], optional
        :param detail: detail, defaults to None
        :type detail: str, optional
        :param error: error, defaults to None
        :type error: any, optional
        :param success: success, defaults to None
        :type success: bool, optional
        """
        if data is not None:
            self.data = self._define_list(data, Hoster)
        if detail is not None:
            self.detail = detail
        if error is not None:
            self.error = error
        if success is not None:
            self.success = success

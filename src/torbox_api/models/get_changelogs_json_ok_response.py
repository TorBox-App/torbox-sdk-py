from typing import List
from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"id_": "id"})
class GetChangelogsJsonOkResponseData(BaseModel):
    """GetChangelogsJsonOkResponseData

    :param created_at: created_at, defaults to None
    :type created_at: str, optional
    :param html: html, defaults to None
    :type html: str, optional
    :param id_: id_, defaults to None
    :type id_: str, optional
    :param link: link, defaults to None
    :type link: str, optional
    :param markdown: markdown, defaults to None
    :type markdown: str, optional
    :param name: name, defaults to None
    :type name: str, optional
    """

    def __init__(
        self,
        created_at: str = SENTINEL,
        html: str = SENTINEL,
        id_: str = SENTINEL,
        link: str = SENTINEL,
        markdown: str = SENTINEL,
        name: str = SENTINEL,
        **kwargs
    ):
        """GetChangelogsJsonOkResponseData

        :param created_at: created_at, defaults to None
        :type created_at: str, optional
        :param html: html, defaults to None
        :type html: str, optional
        :param id_: id_, defaults to None
        :type id_: str, optional
        :param link: link, defaults to None
        :type link: str, optional
        :param markdown: markdown, defaults to None
        :type markdown: str, optional
        :param name: name, defaults to None
        :type name: str, optional
        """
        if created_at is not SENTINEL:
            self.created_at = created_at
        if html is not SENTINEL:
            self.html = html
        if id_ is not SENTINEL:
            self.id_ = id_
        if link is not SENTINEL:
            self.link = link
        if markdown is not SENTINEL:
            self.markdown = markdown
        if name is not SENTINEL:
            self.name = name
        self._kwargs = kwargs


@JsonMap({})
class GetChangelogsJsonOkResponse(BaseModel):
    """GetChangelogsJsonOkResponse

    :param data: data, defaults to None
    :type data: List[GetChangelogsJsonOkResponseData], optional
    :param detail: detail, defaults to None
    :type detail: str, optional
    :param error: error, defaults to None
    :type error: any, optional
    :param success: success, defaults to None
    :type success: bool, optional
    """

    def __init__(
        self,
        data: List[GetChangelogsJsonOkResponseData] = SENTINEL,
        detail: str = SENTINEL,
        error: Union[any, None] = SENTINEL,
        success: bool = SENTINEL,
        **kwargs
    ):
        """GetChangelogsJsonOkResponse

        :param data: data, defaults to None
        :type data: List[GetChangelogsJsonOkResponseData], optional
        :param detail: detail, defaults to None
        :type detail: str, optional
        :param error: error, defaults to None
        :type error: any, optional
        :param success: success, defaults to None
        :type success: bool, optional
        """
        if data is not SENTINEL:
            self.data = self._define_list(data, GetChangelogsJsonOkResponseData)
        if detail is not SENTINEL:
            self.detail = detail
        if error is not SENTINEL:
            self.error = error
        if success is not SENTINEL:
            self.success = success
        self._kwargs = kwargs

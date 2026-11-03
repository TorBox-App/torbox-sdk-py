from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class CreateWebDownloadRequest(BaseModel):
    """CreateWebDownloadRequest

    :param link: link, defaults to None
    :type link: str, optional
    :param password: password, defaults to None
    :type password: str, optional
    :param name: name, defaults to None
    :type name: str, optional
    :param as_queued: as_queued, defaults to None
    :type as_queued: str, optional
    :param add_only_if_cached: add_only_if_cached, defaults to None
    :type add_only_if_cached: str, optional
    """

    link: Optional[str] = Field(default=None)
    password: Optional[str] = Field(default=None)
    name: Optional[str] = Field(default=None)
    as_queued: Optional[str] = Field(default=None)
    add_only_if_cached: Optional[str] = Field(default=None)

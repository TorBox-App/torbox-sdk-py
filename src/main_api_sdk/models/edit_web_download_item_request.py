from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class EditWebDownloadItemRequest(BaseModel):
    """EditWebDownloadItemRequest

    :param webdl_id: webdl_id, defaults to None
    :type webdl_id: float, optional
    :param name: name, defaults to None
    :type name: str, optional
    :param tags: tags, defaults to None
    :type tags: List[str], optional
    :param alternative_hashes: alternative_hashes, defaults to None
    :type alternative_hashes: List[str], optional
    :param airlocked: airlocked, defaults to None
    :type airlocked: bool, optional
    """

    webdl_id: Optional[float] = Field(default=None)
    name: Optional[str] = Field(default=None)
    tags: Optional[List[str]] = Field(default=None)
    alternative_hashes: Optional[List[str]] = Field(default=None)
    airlocked: Optional[bool] = Field(default=None)

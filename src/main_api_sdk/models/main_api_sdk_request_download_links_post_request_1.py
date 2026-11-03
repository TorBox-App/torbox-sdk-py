from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class MainApiSdkRequestDownloadLinksPostRequest1(BaseModel):
    """MainApiSdkRequestDownloadLinksPostRequest1

    :param file_ids: file_ids, defaults to None
    :type file_ids: List[float], optional
    """

    file_ids: Optional[List[float]] = Field(default=None)

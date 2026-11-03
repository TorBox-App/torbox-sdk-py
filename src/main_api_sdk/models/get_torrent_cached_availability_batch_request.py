from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class GetTorrentCachedAvailabilityBatchRequest(BaseModel):
    """GetTorrentCachedAvailabilityBatchRequest

    :param hashes: hashes, defaults to None
    :type hashes: List[str], optional
    """

    hashes: Optional[List[str]] = Field(default=None)

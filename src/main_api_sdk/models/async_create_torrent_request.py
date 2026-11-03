from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class AsyncCreateTorrentRequest(BaseModel):
    """AsyncCreateTorrentRequest

    :param file: file, defaults to None
    :type file: bytes, optional
    :param magnet: magnet, defaults to None
    :type magnet: str, optional
    :param seed: seed, defaults to None
    :type seed: str, optional
    :param allow_zip: allow_zip, defaults to None
    :type allow_zip: str, optional
    :param name: name, defaults to None
    :type name: str, optional
    :param as_queued: as_queued, defaults to None
    :type as_queued: str, optional
    :param add_only_if_cached: add_only_if_cached, defaults to None
    :type add_only_if_cached: str, optional
    """

    file: Optional[bytes] = Field(default=None)
    magnet: Optional[str] = Field(default=None)
    seed: Optional[str] = Field(default=None)
    allow_zip: Optional[str] = Field(default=None)
    name: Optional[str] = Field(default=None)
    as_queued: Optional[str] = Field(default=None)
    add_only_if_cached: Optional[str] = Field(default=None)

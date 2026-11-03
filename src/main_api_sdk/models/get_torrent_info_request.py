from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class GetTorrentInfoRequest(BaseModel):
    """GetTorrentInfoRequest

    :param magnet: magnet, defaults to None
    :type magnet: str, optional
    :param file: file, defaults to None
    :type file: bytes, optional
    :param hash: hash, defaults to None
    :type hash: str, optional
    :param timeout: timeout, defaults to None
    :type timeout: str, optional
    :param use_cache_lookup: use_cache_lookup, defaults to None
    :type use_cache_lookup: str, optional
    :param peers_only: peers_only, defaults to None
    :type peers_only: str, optional
    """

    magnet: Optional[str] = Field(default=None)
    file: Optional[bytes] = Field(default=None)
    hash: Optional[str] = Field(default=None)
    timeout: Optional[str] = Field(default=None)
    use_cache_lookup: Optional[str] = Field(default=None)
    peers_only: Optional[str] = Field(default=None)

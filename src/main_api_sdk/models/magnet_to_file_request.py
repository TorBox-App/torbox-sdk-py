from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class MagnetToFileRequest(BaseModel):
    """MagnetToFileRequest

    :param magnet: magnet, defaults to None
    :type magnet: str, optional
    """

    magnet: Optional[str] = Field(default=None)

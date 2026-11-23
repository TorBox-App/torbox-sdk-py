from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class ControlTagRequest(BaseModel):
    """ControlTagRequest

    :param id_: id_, defaults to None
    :type id_: float, optional
    :param operation: operation, defaults to None
    :type operation: str, optional
    """

    id_: Optional[float] = Field(alias="id", serialization_alias="id", default=None)
    operation: Optional[str] = Field(default=None)

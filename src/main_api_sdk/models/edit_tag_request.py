from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class EditTagRequest(BaseModel):
    """EditTagRequest

    :param id_: id_, defaults to None
    :type id_: float, optional
    :param new_name: new_name, defaults to None
    :type new_name: str, optional
    """

    id_: Optional[float] = Field(alias="id", serialization_alias="id", default=None)
    new_name: Optional[str] = Field(default=None)

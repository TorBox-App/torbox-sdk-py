from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class GetTokenFromDeviceCodeProcessRequest(BaseModel):
    """GetTokenFromDeviceCodeProcessRequest

    :param device_code: device_code, defaults to None
    :type device_code: str, optional
    """

    device_code: Optional[str] = Field(default=None)

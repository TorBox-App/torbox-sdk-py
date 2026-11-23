from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class ChatWithAssistantRequest(BaseModel):
    """ChatWithAssistantRequest

    :param message: message, defaults to None
    :type message: str, optional
    :param session_id: session_id, defaults to None
    :type session_id: str, optional
    :param files: files, defaults to None
    :type files: List[str], optional
    :param blocks: blocks, defaults to None
    :type blocks: List[str], optional
    """

    message: Optional[str] = Field(default=None)
    session_id: Optional[str] = Field(default=None)
    files: Optional[List[str]] = Field(default=None)
    blocks: Optional[List[str]] = Field(default=None)

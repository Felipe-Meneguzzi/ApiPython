from http import HTTPStatus
from pydantic import BaseModel
from typing import Optional, Any


class ResponseBody(BaseModel):
    success: bool
    status_code: HTTPStatus
    data: Any
    metadata: Optional[dict] = None

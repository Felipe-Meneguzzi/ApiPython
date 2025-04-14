from pydantic import BaseModel
from typing import Optional
import datetime


class RequestLogEntity(BaseModel):
    user_id: int
    method: str
    url: str
    url_params: str
    request_body: str
    time: datetime.datetime
    ip: str
    id: Optional[int] = None

    class Config:
        json_encoders = {
            datetime.datetime: lambda v: v.isoformat()  # Converte datetime para string no formato ISO 8601
        }
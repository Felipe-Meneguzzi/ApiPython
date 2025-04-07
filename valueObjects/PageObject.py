from pydantic import BaseModel
from typing import Optional


class PageObject(BaseModel):
    page: Optional[int] = 1
    page_size: Optional[int] = 10
    sort: Optional[str] = "id"
    sort_direction: Optional[str] = "asc"
    search: Optional[dict] = None
    filters: Optional[dict] = None

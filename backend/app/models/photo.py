from pydantic import BaseModel
from typing import Optional

class Photo(BaseModel):
    id: int
    filename: str
    location: Optional[str] = None
    style: Optional[str] = None

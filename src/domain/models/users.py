from pydantic import BaseModel
from typing import Optional

class Users(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: str
    age: int

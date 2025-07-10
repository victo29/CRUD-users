from pydantic import BaseModel
from typing import List, Dict

class UserFinderReturn(BaseModel):
    type: str
    count: int
    attributes: List[Dict]

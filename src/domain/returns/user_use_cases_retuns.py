from pydantic import BaseModel
from typing import List, Dict

class UserFinderReturn(BaseModel):
    type: str
    count: int
    attributes: List[Dict]

class UserListReturn(BaseModel):
    type: str
    count: int
    attributes: List[Dict]

class UserRegisterReturn(BaseModel):
    type: str
    count: int
    attributes: Dict

class UserDeleteReturn(BaseModel):
    type: str
    count: int
    attributes: Dict

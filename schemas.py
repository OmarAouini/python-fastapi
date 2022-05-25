"""REQUEST BODY SCHEMAS MODULE"""
from typing import Union
from pydantic import BaseModel

class Item(BaseModel):
    """sample dto schema"""
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

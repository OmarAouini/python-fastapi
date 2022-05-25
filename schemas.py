"""REQUEST BODY SCHEMAS MODULE"""
from typing import Union
from pydantic import BaseModel, Field

class Item(BaseModel):
    """sample dto schema"""
    name: str
    description: Union[str, None] = None
    price: float = Field(gt=0, description="price must be greater than 0")
    tax: Union[float, None] = None

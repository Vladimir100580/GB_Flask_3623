from typing import Optional
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None     # строковое описание
    price: float
    tax: Optional[float] = None       # Optional - опциональное значение, может быть или нет.
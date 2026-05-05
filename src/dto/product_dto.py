from uuid import UUID

from pydantic import BaseModel

class IProductCreateDTO(BaseModel):
    description: str
    stock_level: int
    value: int
    category_name: str
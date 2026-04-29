from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel

class Products(SQLModel, table=True):
    id: UUID = Field(primary_key=True, default_factory=uuid4)
    description: str = Field(nullable=False, max_length=500)
    stock_level: int = Field(nullable=False, max_digits=3)
    value: int = Field(nullable=False)
    category_id: UUID = Field(foreign_key="categories.id")
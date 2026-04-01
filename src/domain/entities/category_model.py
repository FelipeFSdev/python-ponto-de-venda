from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4

class Categories(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    description: str = Field(max_length=500)
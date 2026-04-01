from uuid import UUID, uuid4

from sqlmodel import SQLModel, Field
from pydantic import EmailStr

class Users(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(nullable=False, max_length=128)
    email: EmailStr = Field(nullable=False, unique=True, max_length=128)
    password: str = Field(nullable=False, max_length=128)
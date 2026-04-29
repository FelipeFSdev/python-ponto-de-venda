from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel
from pydantic import EmailStr

class Customers(SQLModel, table=True):
    id: UUID = Field(primary_key=True, default_factory=uuid4)
    name: str = Field(nullable=False, max_length=128)
    email: EmailStr = Field(nullable=False, unique=True, max_length=128)
    cpf: str = Field(nullable=False, unique=True, max_length=11)
    zip_code: str = Field(max_length=16, default=None)
    street: str = Field(max_length=128, default=None)
    number: str = Field(max_length=10, default=None)
    neighborhood: str = Field(max_length=128, default=None)
    city: str = Field(max_length=128, default=None)
    state: str = Field(max_length=128, default=None)

from pydantic import BaseModel, EmailStr

class IUserCreateDTO(BaseModel):
    name: str
    email: EmailStr
    password: str

class IUserDetailDTO(BaseModel):
    name: str
    email: EmailStr

class IUserUpdateDTO(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    password: str | None = None
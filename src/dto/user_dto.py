from pydantic import BaseModel, EmailStr

class IUserCreateDTO(BaseModel):
    name: str
    email: EmailStr
    password: str

class IUserDetailDTO(BaseModel):
    name: str
    email: EmailStr
from pydantic import BaseModel

class ICategoryCreateDTO(BaseModel):
    description: str

class ICategoryUpdateDTO(BaseModel):
    description: str
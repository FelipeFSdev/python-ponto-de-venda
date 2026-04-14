from fastapi import APIRouter
from dependencies import UserServiceDep
from src.dto.user_dto import IUserCreateDTO

router = APIRouter(prefix="/api/user")

@router.post("/create")
def create_user(service: UserServiceDep, request: IUserCreateDTO):
    return service.create_user(request.name, request.email, request.password)
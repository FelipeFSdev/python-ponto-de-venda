from fastapi import APIRouter
from dependencies import LoginServiceDep
from src.dto.login_dto import LoginRequestDTO

router = APIRouter(prefix="/api/login")

@router.post("/")
def login(service: LoginServiceDep, request: LoginRequestDTO):
    return service.login(request.email, request.password)
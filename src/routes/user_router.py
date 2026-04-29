from fastapi import APIRouter, Depends
from dependencies import UserServiceDep, CurrentUserDep, get_current_user
from src.dto.user_dto import IUserCreateDTO, IUserDetailDTO, IUserUpdateDTO

router = APIRouter(prefix="/api/user")

@router.post("/create")
def create_user(service: UserServiceDep, request: IUserCreateDTO):
    return service.create_user(request)

@router.get("/detail", dependencies=[Depends(get_current_user)], response_model=IUserDetailDTO)
def detail_user(service: UserServiceDep, current_user: CurrentUserDep):
    return service.get_user_by_id(current_user["id"])

@router.patch("/edit", dependencies=[Depends(get_current_user)])
def edit_user(service: UserServiceDep, current_user: CurrentUserDep, request: IUserUpdateDTO):
    return service.update_user(current_user["id"], request)
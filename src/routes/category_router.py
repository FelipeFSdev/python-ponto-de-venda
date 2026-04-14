from fastapi import APIRouter
from dependencies import CategoryServiceDep
from src.dto.category_dto import ICategoryCreateDTO, ICategoryUpdateDTO

router = APIRouter(prefix="/api/category")

@router.get("/list")
def get_category(service: CategoryServiceDep):
    return service.get_category()

@router.get("/{id}/detail")
def get_by_id(id: str, service: CategoryServiceDep):
    return service.get_by_id(id)

@router.post("/create")
def create_category(service: CategoryServiceDep, request: ICategoryCreateDTO):
    return service.create_category(request)

@router.patch("/{id}/update")
def update_category(id: str, service: CategoryServiceDep, request: ICategoryUpdateDTO):
    return service.update_category(id, request)

@router.delete("/{id}/delete")
def delete_category(id: str, service: CategoryServiceDep):
    return service.delete_category(id)
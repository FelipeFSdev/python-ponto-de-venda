from fastapi import APIRouter, Depends
from src.dto.product_dto import IProductCreateDTO
from dependencies import ProductServiceDep, get_current_user

router = APIRouter(prefix="/api/product")

@router.post("/create", dependencies=[Depends(get_current_user)])
def create_product(
    request: IProductCreateDTO,
    service: ProductServiceDep
    ):
    return service.create_product(request)
from src.adapters.product_db_gateway import IProductGateway
from src.use_cases.product_use_case import IProductUseCase
from src.dto.product_dto import IProductCreateDTO
from src.adapters.category_db_gateway import ICategoryGateway

class ProductService(IProductUseCase):
    def __init__(self,
                 db_gateway: IProductGateway,
                 category_gateway: ICategoryGateway
                ):
        self.db_gateway = db_gateway
        self.category_gateway = category_gateway

    def create_product(self, request: IProductCreateDTO):
        category = self.category_gateway.get_by_name(request.category_name)
        if category is None:
            raise Exception("Category not found.")
        
        create_data = request.model_dump()
        create_data["category_id"] = category.id

        return self.db_gateway.create_product(create_data)
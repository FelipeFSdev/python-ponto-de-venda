from src.adapters.category_db_gateway import ICategoryGateway
from src.use_cases.category_use_case import ICategoryUseCase
from src.dto.category_dto import ICategoryUpdateDTO, ICategoryCreateDTO

class CategoryService(ICategoryUseCase):
    def __init__(self, db_gateway: ICategoryGateway):
        self.db_gateway = db_gateway

    def get_category(self):
        return self.db_gateway.get_category()

    def get_by_id(self, id: str):
        return self.db_gateway.get_by_id(id)
    
    def create_category(self, request: ICategoryCreateDTO):
        return self.create_category(request)
    
    def update_category(self, id: str, request: ICategoryUpdateDTO):
        return self.update_category(id, request)
    
    def delete_category(self, id: str):
        return self.delete_category(id)
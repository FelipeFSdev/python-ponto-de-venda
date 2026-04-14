from abc import ABC, abstractmethod
from src.dto.category_dto import ICategoryCreateDTO, ICategoryUpdateDTO

class ICategoryUseCase(ABC):
    @abstractmethod
    def get_category(self):
        pass
    
    @abstractmethod
    def get_by_id(self, id: str):
        pass

    @abstractmethod
    def create_category(self, request: ICategoryCreateDTO):
        pass

    @abstractmethod
    def update_category(self, id: str, request: ICategoryUpdateDTO):
        pass

    @abstractmethod
    def delete_category(self, id: str):
        pass
from abc import ABC, abstractmethod
from src.domain.entities.category_model import Categories
from src.dto.category_dto import ICategoryCreateDTO, ICategoryUpdateDTO

class ICategoryGateway(ABC):
    @abstractmethod
    def create_category(self, request: ICategoryCreateDTO):
        pass

    @abstractmethod
    def update_category(self, id: str, request: ICategoryUpdateDTO):
        pass

    @abstractmethod
    def get_category(self):
        pass

    @abstractmethod
    def get_by_id(self, id: str):
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> Categories | None:
        pass

    @abstractmethod
    def delete_category(self, id: str):
        pass

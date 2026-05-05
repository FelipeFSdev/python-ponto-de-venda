from abc import ABC, abstractmethod
from src.dto.product_dto import IProductCreateDTO

class IProductUseCase(ABC):
    @abstractmethod
    def create_product(self, request: IProductCreateDTO):
        pass
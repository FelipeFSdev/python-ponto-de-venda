from abc import ABC, abstractmethod

class IProductGateway(ABC):
    @abstractmethod
    def create_product(self, create_data: dict):
        pass

    @abstractmethod
    def update_product(self, id: str, update_data: dict):
        pass

    @abstractmethod
    def get_product(self, category: str):
        pass

    @abstractmethod
    def detail_product(self, id: str):
        pass

    @abstractmethod
    def delete_product(self, id: str):
        pass
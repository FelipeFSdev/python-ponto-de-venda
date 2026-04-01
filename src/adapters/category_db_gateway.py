from abc import ABC, abstractmethod

class ICategoryGateway(ABC):
    @abstractmethod
    def create_category(self, description: str):
        pass

    @abstractmethod
    def update_category(self, id: str, description: str):
        pass

    @abstractmethod
    def get_category(self):
        pass

    @abstractmethod
    def get_by_id(self, id: str):
        pass

    @abstractmethod
    def delete_category(self, id: str):
        pass

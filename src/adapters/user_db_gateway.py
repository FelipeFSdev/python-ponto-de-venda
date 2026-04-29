from abc import ABC, abstractmethod
from src.domain.entities.user_model import Users

class IUserGateway(ABC):
    @abstractmethod
    def create_user(self, create_data: dict):
        pass

    @abstractmethod
    def get_user_by_email(self, email: str) -> Users | None:
        pass

    @abstractmethod
    def get_user_by_id(self, id: str) -> Users | None:
        pass

    @abstractmethod
    def update_user(self, id: str, update_data: dict):
        pass
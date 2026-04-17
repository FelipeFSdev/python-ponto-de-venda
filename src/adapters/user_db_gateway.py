from abc import ABC, abstractmethod
from src.domain.entities.user_model import Users

class IUserGateway(ABC):
    @abstractmethod
    def create_user(self, name: str, email: str, password: str):
        pass

    @abstractmethod
    def get_user_by_email(self, email: str) -> Users | None:
        pass
from abc import ABC, abstractmethod

class IUserUseCase(ABC):
    @abstractmethod
    def create_user(self, name: str, email: str, password: str):
        pass

    @abstractmethod
    def get_user_by_id(self, id: str):
        pass
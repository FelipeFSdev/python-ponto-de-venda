from abc import ABC, abstractmethod

class IUserGateway(ABC):
    @abstractmethod
    def create_user(self, name: str, email: str, password: str):
        pass
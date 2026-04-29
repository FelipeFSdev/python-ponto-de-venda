from abc import ABC, abstractmethod

from src.dto.user_dto import IUserCreateDTO, IUserUpdateDTO

class IUserUseCase(ABC):
    @abstractmethod
    def create_user(self, request: IUserCreateDTO):
        pass

    @abstractmethod
    def get_user_by_id(self, id: str):
        pass

    @abstractmethod
    def update_user(self, id: str, request: IUserUpdateDTO):
        pass
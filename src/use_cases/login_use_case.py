from abc import ABC, abstractmethod

class ILoginUseCase(ABC):
    @abstractmethod
    def login(self, email: str, password: str) -> str:
        pass
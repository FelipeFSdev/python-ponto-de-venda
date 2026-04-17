from abc import ABC, abstractmethod

class IJwtTokenGateway(ABC):
    @abstractmethod
    def get_token(self, name: str, email: str) -> str:
        pass

    @abstractmethod
    def decode_token(self, token: str):
        pass
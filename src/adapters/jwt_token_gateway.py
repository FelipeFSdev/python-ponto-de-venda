from abc import ABC, abstractmethod

class IJwtTokenGateway(ABC):
    @abstractmethod
    def get_token(self, id: str, name: str, email: str):
        pass

    @abstractmethod
    def decode_token(self, token: str):
        pass
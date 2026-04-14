from abc import ABC, abstractmethod

class IPassHasherGateway(ABC):
    @abstractmethod
    def hash_password(self, password: str) -> str:
        pass
    
    @abstractmethod
    def verify_password(self, password: str, hashed: bytes) -> bool:
        pass
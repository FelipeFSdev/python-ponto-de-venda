import bcrypt
import os
from src.adapters.pass_hasher_gateway import IPassHasherGateway
from dotenv import load_dotenv

load_dotenv()

class PasswordHasher(IPassHasherGateway):
    def __init__(self):
        self.encoder = os.getenv("HASH_ENCODER", "")

    def hash_password(self, password: str) -> str:
        password_bytes = bytes(password, self.encoder)
        hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())

        return hashed.decode(self.encoder)
    
    def verify_password(self, password: str, hashed: bytes) -> bool:
        password_bytes = bytes(password, self.encoder)
        is_match = bcrypt.checkpw(password_bytes, hashed)

        if is_match is False:
            raise

        return is_match


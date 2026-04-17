import jwt
import time
import os

from dotenv import load_dotenv

from src.adapters.jwt_token_gateway import IJwtTokenGateway

load_dotenv()

class JwtManager(IJwtTokenGateway):
    def __init__(self):
        self.jwt_key = os.getenv("JWT_KEY", "")
        self.jwt_algorithm = os.getenv("JWT_ALGORITHM", "")

    def get_token(self, name: str, email: str):
        payload = {
            "exp": time.time() + (30 * 60),
            "name": name,
            "email": email
        }
        token = jwt.encode(payload, self.jwt_key, self.jwt_algorithm)

        return token
    
    def decode_token(self, token: str):
        token_data = jwt.decode(token, self.jwt_key, self.jwt_algorithm)

        if token_data["exp"] < time.time():
            raise
        

        return token_data
    
    # def get_current_user(self):
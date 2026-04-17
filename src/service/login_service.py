import os
from dotenv import load_dotenv
from src.adapters.jwt_token_gateway import IJwtTokenGateway
from src.use_cases.login_use_case import ILoginUseCase
from src.adapters.user_db_gateway import IUserGateway
from src.adapters.pass_hasher_gateway import IPassHasherGateway

load_dotenv()
class LoginService(ILoginUseCase):
    def __init__(self,
                 db_gateway: IUserGateway,
                 token_manager: IJwtTokenGateway,
                 hasher: IPassHasherGateway
                ):
        self.db_gateway = db_gateway
        self.token_manager = token_manager
        self.hasher = hasher
        self.enconder = os.getenv("HASH_ENCODER", "utf-8")

    def login(self, email: str, password: str):
        user = self.db_gateway.get_user_by_email(email)

        if user is None:
            raise ValueError("Invalid credentials.")
        
        verify_password = self.hasher.verify_password(
            password,
            bytes(user.password, self.enconder)
            )
        
        if verify_password is False:
            raise ValueError("Invalid credentials.")
        
        token = self.token_manager.get_token(user.name, user.email)
        
        return token
from src.use_cases.user_use_case import IUserUseCase
from src.adapters.pass_hasher_gateway import IPassHasherGateway
from src.adapters.user_db_gateway import IUserGateway

class UserService(IUserUseCase):
    def __init__(self,
                 db_gateway: IUserGateway,
                 hasher_gateway: IPassHasherGateway
                ):
        self.db_gateway = db_gateway
        self.hasher_gateway = hasher_gateway

    def create_user(self, name: str, email: str, password: str):
        hashed_pass = self.hasher_gateway.hash_password(password)

        return self.db_gateway.create_user(name, email, hashed_pass)
    
    def get_user_by_id(self, id: str):

        return self.db_gateway.get_user_by_id(id)
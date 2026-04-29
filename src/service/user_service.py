from src.use_cases.user_use_case import IUserUseCase
from src.adapters.pass_hasher_gateway import IPassHasherGateway
from src.adapters.user_db_gateway import IUserGateway
from src.dto.user_dto import IUserCreateDTO, IUserUpdateDTO

class UserService(IUserUseCase):
    def __init__(self,
                 db_gateway: IUserGateway,
                 hasher_gateway: IPassHasherGateway
                ):
        self.db_gateway = db_gateway
        self.hasher_gateway = hasher_gateway

    def create_user(self, request: IUserCreateDTO):
        create_data = request.model_dump()
        hashed_pass = self.hasher_gateway.hash_password(request.password)
        create_data["password"] = hashed_pass

        return self.db_gateway.create_user(create_data)
    
    def get_user_by_id(self, id: str):

        return self.db_gateway.get_user_by_id(id)
    
    def update_user(self, id: str, request: IUserUpdateDTO):
        update_data = request.model_dump(exclude_unset=True)

        if "password" in update_data:
            hashed_pass = self.hasher_gateway.hash_password(update_data["password"])
            update_data["password"] = hashed_pass
        
        return self.db_gateway.update_user(id, update_data)
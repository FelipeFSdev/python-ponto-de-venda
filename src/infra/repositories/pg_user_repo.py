from sqlmodel import Session, select
from src.adapters.user_db_gateway import IUserGateway
from src.domain.entities.user_model import Users

class PgUserRepository(IUserGateway):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_user(self, create_data: dict):
        new_user = Users(
            name = create_data["name"],
            email = create_data["email"],
            password = create_data["password"]
        )

        self.db_session.add(new_user)
        self.db_session.commit()
        self.db_session.refresh(new_user)

    def get_user_by_email(self, email: str):
        user = self.db_session.exec(select(Users).where(Users.email == email)).first()

        return user
    
    def get_user_by_id(self, id: str):
        user = self.db_session.get(Users, id)

        return user
    
    def update_user(self, id: str, update_data: dict):
        user = self.get_user_by_id(id)
        if user is None:
            raise

        user.sqlmodel_update(update_data)

        self.db_session.add(user)
        self.db_session.commit()
        self.db_session.refresh(user)
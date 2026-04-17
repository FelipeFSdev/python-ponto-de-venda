from sqlmodel import Session, select
from src.adapters.user_db_gateway import IUserGateway
from src.domain.entities.user_model import Users

class PgUserRepository(IUserGateway):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_user(self, name: str, email: str, password: str):
        new_user = Users(
            name = name,
            email = email,
            password = password
        )

        self.db_session.add(new_user)
        self.db_session.commit()
        self.db_session.refresh(new_user)

    def get_user_by_email(self, email: str):
        user = self.db_session.exec(select(Users).where(Users.email == email)).first()

        return user
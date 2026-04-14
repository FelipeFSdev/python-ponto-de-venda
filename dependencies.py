from sqlmodel import Session
from typing import Annotated
from fastapi import Depends
from src.infra.database.session import engine
from src.adapters.category_db_gateway import ICategoryGateway
from src.service.category_service import CategoryService
from src.infra.repositories.pg_category_repo import PgCategoryRepository
from src.adapters.user_db_gateway import IUserGateway
from src.infra.repositories.pg_user_repo import PgUserRepository
from src.service.user_service import UserService
from src.adapters.pass_hasher_gateway import IPassHasherGateway
from src.infra.cryptography.pass_hasher import PasswordHasher

def get_session():
    with Session(engine) as session:
        yield session

DbSessionDep = Annotated[Session, Depends(get_session)]


def get_hasher_gateway() -> IPassHasherGateway:
    return PasswordHasher()

HasherGatewayDep = Annotated[IPassHasherGateway, Depends(get_hasher_gateway)]


def get_category_gateway(session: DbSessionDep) -> ICategoryGateway:
    return PgCategoryRepository(session)

CategoryGatewayDep = Annotated[ICategoryGateway, Depends(get_category_gateway)]

def get_category_service(gateway: CategoryGatewayDep) -> CategoryService:
    return CategoryService(gateway)

CategoryServiceDep = Annotated[CategoryService, Depends(get_category_gateway)]


def get_user_gateway(session: DbSessionDep) -> IUserGateway:
    return PgUserRepository(session)

UserGatewayDep = Annotated[IUserGateway, Depends(get_user_gateway)]

def get_user_service(
        user_gateway: UserGatewayDep,
        hasher_gateway: HasherGatewayDep
        ) -> UserService:
    return UserService(user_gateway, hasher_gateway)

UserServiceDep = Annotated[UserService, Depends(get_user_service)]

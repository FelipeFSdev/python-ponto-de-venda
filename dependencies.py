from sqlmodel import Session
from typing import Annotated
from fastapi import Depends
from src.infra.database.session import engine

def get_session():
    with Session(engine) as session:
        yield session

DbSessionDep = Annotated[Session, Depends(get_session)]

from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.infra.database.session import create_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("server's up")
    create_tables()
    yield
    print("server's down")

app = FastAPI(lifespan=lifespan)
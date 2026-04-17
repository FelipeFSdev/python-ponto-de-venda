from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.infra.database.session import create_tables
from src.routes.category_router import router as category_router
from src.routes.user_router import router as user_router
from src.routes.login_router import router as login_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("server's up")
    create_tables()
    yield
    print("server's down")

app = FastAPI(lifespan=lifespan)

app.include_router(category_router)
app.include_router(user_router)
app.include_router(login_router)
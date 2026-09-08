from fastapi import FastAPI
from sqlmodel import SQLModel
from .database import engine
from contextlib import asynccontextmanager
from ..models import link
from ..routers import link

@asynccontextmanager
async def lifespan(app: FastAPI):

    # startup
    SQLModel.metadata.create_all(engine)

    yield

    # shutdown
    print("Application is shutting down")

app = FastAPI(lifespan=lifespan)

app.include_router(link.router)
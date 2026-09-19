from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel
from contextlib import asynccontextmanager

from .database import engine
from ..models import link, user
from ..routers import link, user, sign_up

@asynccontextmanager
async def lifespan(app: FastAPI):

    # startup
    SQLModel.metadata.create_all(engine)

    yield

    # shutdown
    print("Application is shutting down")

app = FastAPI(lifespan=lifespan)

app.include_router(link.router)
app.include_router(user.router)
app.include_router(sign_up.router)



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
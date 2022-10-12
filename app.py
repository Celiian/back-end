from fastapi import FastAPI

from routers import get
from routers import post
from routers import put

app = FastAPI()

app.include_router(
    get.router,
)
from fastapi import FastAPI

from routers import get
from routers import patch
from routers import put

app = FastAPI()

app.include_router(
    patch.router,
)
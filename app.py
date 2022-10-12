from fastapi import FastAPI
from customException import CustomError
from fastapi import Request
from fastapi.responses import JSONResponse
from routers import get

app = FastAPI()

app.include_router(get.router)


@app.exception_handler(CustomError)
async def custom_err(request: Request, exc: CustomError):
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.content
    )
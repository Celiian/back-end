from fastapi import FastAPI
from exception_error.custom_exception import CustomError
from fastapi import Request
from fastapi.responses import JSONResponse
from routers import get
from routers import post
from routers import patch
from routers import put

app = FastAPI()

app.include_router(get.router)
app.include_router(post.router)
app.include_router(patch.router)
app.include_router(put.router)


@app.exception_handler(CustomError)
async def custom_err(request: Request, exc: CustomError):
    """
    Initialisation of the custom error

    :param request: request of the user to be sent back (not used but necessary)
    :param exc: CLASS the custom error class
    :return: JSON The response with a status code and a message
    """
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.content
    )
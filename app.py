from fastapi import FastAPI
from exception_error.custom_exception import CustomError
from fastapi import Request
from fastapi.responses import JSONResponse
from routers import get
from routers import delete
app = FastAPI()

app.include_router(get.router)
app.include_router(delete.router)


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
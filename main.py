import config
from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from routers import device
from routers import data

tags = [
    {
        "name": "devices",
        "description": "Shows a list of _registered_ **devices**."
    }
]

app = FastAPI(openapi_tags=tags)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    """Handles error response when body of a post request is wrong
    """
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body})
    )

# use routers like this    
app.include_router(device.router, tags=["devices"])

app.include_router(data.router)

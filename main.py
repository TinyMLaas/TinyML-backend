import config
from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from routers import device, bridge, dataset
from apidocs import tags, description


app = FastAPI(
    title=description.title,
    description=description.description,
    version=description.version,
    openapi_tags=tags.tags,
)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Handles error response when body of a post request is wrong"""
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )

# use routers like this
app.include_router(device.router, tags=["devices"])

app.include_router(dataset.router, tags=["Data"])

app.include_router(bridge.router)
from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from routers import compiled_model, device, bridge, dataset, model
from apidocs import tags, description
import config  # pylint: disable=unused-import


app = FastAPI(
    openapi="3.0.2",
    swagger="2.0",
    title=description.title,
    description=description.description,
    version=description.version,
    openapi_tags=tags.tags,
)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):  # pylint: disable=unused-argument
    """Handles error response when body of a post request is wrong"""
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )

app.include_router(device.router, tags=["Devices"])

app.include_router(bridge.router, tags=["Bridges"])

app.include_router(compiled_model.router, tags=["Compiled models"])

app.include_router(dataset.router, tags=["Datasets"])

app.include_router(model.router, tags=["Models"])

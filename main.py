from enum import Enum
from pydantic import BaseModel

from fastapi import FastAPI
from fastapi import APIRouter

from services import device_service
from routers import device
from routers import data

# these are examples
class Model(BaseModel):
    name: str
    description: str


class ModelName(str, Enum):
    facerecognition = "Face Recognition"
    carrecognition = "Car Recognition"


models = {0: {"name": None, "description": None}}

# This creates documentation, you can use markdown.

tags = [
    {
        "name": "devices",
        "description": "Shows a list of _registered_ **devices**."
    }
]

app = FastAPI(openapi_tags=tags)

backend_url = "127.0.0.1"

@app.post("/item/")
async def create_item(model: Model):
    models[1] = {"name": model.name, "description": model.description}
    return {"message": "Model added"}


@app.get("/models/")
async def read_model(model_name: ModelName | None = None,
                     model_id: int = 0):
    if model_name is ModelName.facerecognition:
        return {"model_name": model_name,
                "message": "Model for recognizing faces"}

    if model_name is ModelName.carrecognition:
        return {"model_name": model_name,
                "message": "Model for detecting cars"}

    return {"model": models[model_id]["name"],
            "description": models[model_id]["description"]}

# use routers like this    
app.include_router(device.router, tags=["devices"])

app.include_router(data.router)


   
    
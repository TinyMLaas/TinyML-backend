from enum import Enum
from fastapi import APIRouter
from pydantic import BaseModel
from services import training_service

router = APIRouter()


class LossFunctions(str, Enum):
    categorical_crossentropy = "Categorical crossentropy"
    parse_categorical_crossentropy = "parse Categorical crossentropy"


class TrainingData(BaseModel):
    """The request body for the model training"""

    model_name: str
    epochs: int
    img_width: int
    img_height: int
    batch_size: int


@router.post("/model/dataset/{dataset_id}", status_code=201)
async def train_model(dataset_id: int,
                      trainingdata: TrainingData, lossfunc: LossFunctions):
    """return training data"""

    return training_service.training(dataset_id, trainingdata, lossfunc)

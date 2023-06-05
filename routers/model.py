from enum import Enum
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from services import model_service
from db.database import get_db

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
                      trainingdata: TrainingData, lossfunc: LossFunctions,
                      database: Session = Depends(get_db)):
    """return training data"""

    return training_service.training(dataset_id, trainingdata, lossfunc, database)

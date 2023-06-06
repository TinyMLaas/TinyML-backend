from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services import model_service
from db.database import get_db
from schemas.schemas import TrainingData, LossFunctions

router = APIRouter()


@router.post("/models/datasets/{dataset_id}", status_code=201)
async def train_model(dataset_id: int,
                      trainingdata: TrainingData, lossfunc: LossFunctions,
                      database: Session = Depends(get_db)):
    """return training data"""

    return model_service.training(dataset_id, trainingdata, lossfunc, database)

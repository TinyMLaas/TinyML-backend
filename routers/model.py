from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from services import model_service
from db.database import get_db
from schemas import schemas

router = APIRouter()


@router.post("/model/dataset/{dataset_id}", status_code=201, response_model=list[schemas.Models])
async def train_model(dataset_id: int,
                      trainingdata: schemas.TrainingData, lossfunc: schemas.LossFunctions,
                      database: Session = Depends(get_db)):
    """return training data"""

    return model_service.training(dataset_id, trainingdata, lossfunc, database)

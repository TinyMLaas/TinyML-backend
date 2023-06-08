from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services import model_service
from db.database import get_db
from schemas import schemas

router = APIRouter()


@router.post("/models/datasets/{dataset_id}", status_code=201, response_model=schemas.ModelTrained)
async def train_model(dataset_id: int | None, trainingdata: schemas.ModelBase, lossfunc: schemas.LossFunctions,
                      database: Session = Depends(get_db)):
    """return training data"""

    return model_service.training(trainingdata, lossfunc, database, dataset_id)


@router.post("/models/datasets/", status_code=201, response_model=schemas.ModelTrained)
async def train_model_dataset_id_in_training_data(trainingdata: schemas.ModelBase, lossfunc: schemas.LossFunctions,
                                                  database: Session = Depends(get_db)):
    """return training data"""

    return model_service.training(trainingdata, lossfunc, database)

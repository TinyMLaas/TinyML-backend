import os
from datetime import datetime
import base64
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from TinyMLaaS_main.training import TrainModel
from services import dataset_service
from db import models
from schemas import schemas


def training(training_data, lossfunc, database: Session, dataset_id: int = None):
    """Initalize the training class for model training and train it with the
    wanted data. Returns pictures of training. Prediction image is a image
    from the dataset, that has been analyzed with the created model. The statistic
    image is a statistical image of training.

    Pictures are send back as bytes. The bytes are encoded with the help of the python
    library base64. This means that the pictures need to be decoded with the
    same library/equivalent library."""

    if dataset_id is not None:
        training_data.dataset_id = dataset_id
    dataset_path = dataset_service.get_dataset_path_by_id(
        database, training_data.dataset_id)

    trainmodel = TrainModel(dataset_path)

    parameters = training_data.parameters

    now = datetime.now()

    db_model = schemas.ModelCreate(dataset_id=training_data.dataset_id,
                                   parameters=parameters, description=training_data.description,
                                   created=now, model_path="")

    db_model = savemodel(db_model, database)

    db_model = db_model.__dict__

    model, history, epochs_range = trainmodel.train(
        parameters["img_height"], parameters["img_width"],
        parameters["epochs"], lossfunc, parameters["batch_size"],
        str(training_data.description)
    )

    db_model["parameters"] = parameters

    class_names = [name for name in os.listdir(
        dataset_path)]
    image, prediction = trainmodel.prediction(model, class_names)

    prediction_image = jsonable_encoder(image.getbuffer().tobytes(), custom_encoder={
        bytes: lambda v: base64.b64encode(v).decode('utf-8')})

    db_model["prediction_image"] = prediction_image
    db_model["prediction"] = prediction

    image2 = trainmodel.plot_statistics(history, epochs_range)

    statistic_image = jsonable_encoder(image2.getbuffer().tobytes(), custom_encoder={
        bytes: lambda v: base64.b64encode(v).decode('utf-8')})

    db_model["statistic_image"] = statistic_image

    return db_model


def savemodel(model: schemas.ModelCreate, database: Session):
    """Saves model to a database"""

    db_model = models.Model(**model.dict())
    db_model.parameters = str(db_model.parameters)

    database.add(db_model)
    database.commit()
    database.refresh(db_model)

    db_model.model_path = f"models/{db_model.id}"
    database.commit()
    database.refresh(db_model)

    return db_model

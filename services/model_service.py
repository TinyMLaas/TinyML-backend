import os
from datetime import datetime
import base64
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from TinyMLaaS_main.training import TrainModel
from services import dataset_service


def training(training_data, lossfunc, database: Session, dataset_id: int = None):
    """Initalize the training class for model training and train it with the
    wanted data"""

    if dataset_id is None:
        dataset_path = dataset_service.get_dataset_path_by_id(
            database, training_data.dataset_id)
    else:
        training_data.dataset_id = dataset_id
        dataset_path = dataset_service.get_dataset_path_by_id(
            database, dataset_id)

    trainmodel = TrainModel(dataset_path)

    parameters = training_data.parameters
    model, history, epochs_range = trainmodel.train(
        parameters["img_height"], parameters["img_width"],
        parameters["epochs"], lossfunc, parameters["batch_size"],
        training_data.model_name
    )

    class_names = [name for name in os.listdir(
        dataset_path)]
    image, prediction = trainmodel.prediction(model, class_names)

    savemodel(model, training_data.description)
    # result = {"image": image, "prediction": prediction, "stats": stats}

    prediction_image = jsonable_encoder(image.getbuffer().tobytes(), custom_encoder={
        bytes: lambda v: base64.b64encode(v).decode('utf-8')})

    image2 = trainmodel.plot_statistics(history, epochs_range)

    statistic_image = jsonable_encoder(image2.getbuffer().tobytes(), custom_encoder={
        bytes: lambda v: base64.b64encode(v).decode('utf-8')})
    now = datetime.now()

    result = [{"dataset_id": training_data.dataset_id, "parameters": parameters,
               "description": training_data.description, "id": 1, "created": now,
               "prediction_image": prediction_image, "prediction": prediction,
               "statistic_image": statistic_image}]
    return result


def savemodel(model, modelname):
    """Saves model to a database"""
    stats = trainmodel.plot_statistics(history, epochs_range)
    savemodel(training_data.model_name)
    # result = {"image": image, "prediction": prediction, "stats": stats}
    result = {"status": "done"}
    return result

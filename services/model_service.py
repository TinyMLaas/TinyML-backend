import os
import numpy as np
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
import base64
from TinyMLaaS_main.training import TrainModel
from services import dataset_service


def training(ds_id, training_data, lossfunc, database: Session):
    """Initalize the training class for model training and train it with the
    wanted data"""

    dataset_path = dataset_service.get_dataset_path_by_id(database, ds_id)

    trainmodel = TrainModel(dataset_path)
    model, history, epochs_range = trainmodel.train(
        training_data.img_height, training_data.img_width,
        training_data.epochs, lossfunc, training_data.batch_size
    )

    class_names = [name for name in os.listdir(
        dataset_path)]
    image, prediction = trainmodel.prediction(model, class_names)

    image2 = trainmodel.plot_statistics(history, epochs_range)

    savemodel(model, training_data.model_name)
    # result = {"image": image, "prediction": prediction, "stats": stats}

    image = jsonable_encoder(image.tobytes(), custom_encoder={
        bytes: lambda v: base64.b64encode(v).decode('utf-8')})
    result = [{"status": "done", "image": image}]
    return result


def savemodel(model, modelname):
    """Saves model to a database"""
    pass

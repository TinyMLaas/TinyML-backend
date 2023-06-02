import os
from TinyMLaaS_main.training import TrainModel
from services import data_service


def call_training(ds_id, training_data, lossfunc):
    """Initalize the training class for model training and train it with the
    wanted data"""

    dataset_path = data_service.get_dataset_images(ds_id)
    trainmodel = TrainModel(dataset_path)
    model, history, epochs_range = trainmodel.train(
        training_data.img_height, training_data.img_width,
        training_data.epochs, lossfunc, training_data.batch_size
    )
    class_names = [name for name in os.listdir(dataset_path) if os.isdir(name)]
    image, prediction = trainmodel.prediction(model, class_names)
    #
    savemodel(model, training_data.model_name)
    result = {"image": image, "prediction": prediction}
    return result


def savemodel(model, modelname):
    """Saves model to a database"""
    pass

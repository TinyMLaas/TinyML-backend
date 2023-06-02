from TinyMLaaS_main.training import TrainModel
from services import data_service


def call_training(ds_id, training_data, lossfunc):
    dataset_path = data_service.get_dataset_images(ds_id)
    trainmodel = TrainModel(dataset_path)
    model, history, epochs_range = trainmodel.train(
        training_data.img_height, training_data.img_width,
        training_data.epochs, lossfunc, training_data.batch_size
    )
    savemodel(model, training_data.model_name)


def savemodel(model, modelname):
    """Saves model to a database"""
    pass

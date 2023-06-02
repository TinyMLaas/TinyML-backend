from TinyMLaaS_main import training
from services import data_service


def training(training_data, lossfunc): 
    print(training_data.model_name)
    trainmodel = TrainModel(training_data.path)
    model, history, epochs_range = trainmodel.train(training_data.img_height, training_data.img_width, training_data.epochs, lossfunc, training_data.batch_size)
    savemodel(model,training_data.model_name)


def savemodel(model,modelname):
"""Saves model to a database"""
    pass 

import datetime
from pydantic import BaseModel, Field
from pydantic.types import Optional


class ModelBase(BaseModel):
    """Base for Model trained on Tensorflow. Lacks id as it is assigned by database
    """
    dataset_id: int | None
    parameters: dict
    description: str


class Model(ModelBase):
    """If Model is in database, it always has an id.
    """
    id: int
    created: datetime.datetime | None
    model_path: str

    class Config:
        orm_mode = True


class ModelCreate(ModelBase):
    """When creating a new Model, there is yet no id.
    """
    created: datetime.datetime | None
    model_path: str

    class Config:
        orm_mode = True


class ModelPlot(ModelBase):
    """"Includes image of model training plots.
    """
    training_plot: bytes

    class Config:
        orm_mode = True


class ModelTrained(Model):
    """A trained model includes prediction image, the prediction that 
    the model has made of the image and some statistics in a plot.
    """
    prediction_image: str
    prediction: str
    statistic_image: bytes

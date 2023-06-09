import datetime
from enum import Enum
from ipaddress import IPv4Address
from pydantic import BaseModel, Field


# Devices
class DeviceBase(BaseModel):
    """Base for Device model. Lacks id as it is assigned by database.
    """
    name: str = Field(min_length=1)
    connection: str | None = Field(default=None, min_length=1)
    installer: str | None = Field(default=None, min_length=1)
    compiler: str | None = Field(default=None, min_length=1)
    model: str = Field(min_length=1)
    description: str = Field(min_length=1)
    serial:  str = Field(min_length=1)


class Device(DeviceBase):
    """If Device is in database, it always has an id.
    """
    id: int

    class Config:
        orm_mode = True


class DeviceCreate(DeviceBase):
    """When creating a new Device, there is yet no id.
    """

    class Config:
        orm_mode = True

# Bridges


class BridgeBase(BaseModel):
    """Base for Bridge model. Lacks id as it is assigned by database.
    """
    ip_address: IPv4Address
    name: str | None = None


class Bridge(BridgeBase):
    """If Bridge is in database, it always has an id.
    """
    id: int

    class Config:
        orm_mode = True


class BridgeCreate(BridgeBase):
    """When creating a new Bridge, there is yet no id.
    """

    class Config:
        orm_mode = True


# Datasets
class DatasetBase(BaseModel):
    """Base for Dataset model. Lacks id as it is assigned by database
    """
    path: str = Field(min_length=1)
    name: str = Field(min_length=1)
    description: str = Field(min_length=1)
    size: str = Field(min_length=1)


class Dataset(DatasetBase):
    """If Bridge is in database, it always has an id.
    """
    id: int

    class Config:
        orm_mode = True


class DatasetCreate(BaseModel):
    """When creating a new Dataset, there is yet no id. There is also no size to save.
    """
    path: str = Field(min_length=1)
    name: str = Field(min_length=1)
    description: str = Field(min_length=1)


# Models
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
    prediction_image: str
    prediction: str
    statistic_image: bytes

# Compiled models


class CompiledModelBase(BaseModel):
    """"A Model that has been compiled with TFLite to fit a MCU.
    """
    created: datetime.datetime | None
    compiler_id: int | None  # relationship
    model_id: int  # relationship
    model_path: str


class CompiledModel(CompiledModelBase):
    """If CompiledModel is in database, it always has an id.
    """
    id: int

    class Config:
        orm_mode = True


class CompiledModelCreate(CompiledModelBase):
    """When creating a new CompiledModel, there is yet no id.
    """

    class Config:
        orm_mode = True


class LossFunctions(str, Enum):
    """Loss functions available in training
    """

    categorical_crossentropy = "Categorical crossentropy"
    sparse_categorical_crossentropy = "Sparse Categorical crossentropy"

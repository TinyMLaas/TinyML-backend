import datetime
from enum import Enum
from ipaddress import IPv4Address
from pydantic import BaseModel, Field
from pydantic.types import Optional


class InstallerBase(BaseModel):
    """Base for Installer model. Lacks id as it is assigned by database.
    """
    name: str = Field(min_length=1)


class Installer(InstallerBase):
    """If Installer is in database, it always has an id.
    """
    id: int

    class Config:
        orm_mode = True


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


# Devices
class DeviceBase(BaseModel):
    """Base for Device model. Lacks id as it is assigned by database.
    """
    name: str = Field(min_length=1)
    connection: str | None = Field(default=None, min_length=1)
    installer_id: int
    model: str = Field(min_length=1)
    description: str = Field(min_length=1)
    serial:  str = Field(min_length=1)


class Device(DeviceBase):
    """If Device is in database, it always has an id.
    """
    id: int
    installer: Optional[Installer] = None
    bridge: Optional[Bridge] = None

    class Config:
        orm_mode = True


class DeviceCreate(DeviceBase):
    """When creating a new Device, there is yet no id.
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
    """A trained model includes prediction image, the prediction that 
    the model has made of the image and some statistics in a plot.
    """
    prediction_image: str
    prediction: str
    statistic_image: bytes

# Compiled models


class CompiledModelBase(BaseModel):
    """"A Model that has been compiled with TFLite to fit a MCU.
    """
    created: datetime.datetime | None
    model_id: int  # relationship
    model_path: str


class CompiledModel(CompiledModelBase):
    """If CompiledModel is in database, it always has an id.
    """
    id: int

    class Config:
        orm_mode = True


class CompiledModelFile(CompiledModel):
    """With the compiled model file as string
    """

    file: str


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


class ObservationBase(BaseModel):
    """Class for getting and returning values for observation
    """
    bridge_id: int
    device_id: int


class ObservationReturn(ObservationModelBase):
    """When returning, the observation has value
    """
    observation_value: int

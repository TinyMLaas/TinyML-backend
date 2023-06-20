from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship


from db.database import Base


class Device(Base):
    """MCU Device
    """

    __tablename__ = "Devices"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    connection = Column(String)
    bridge_id = Column(Integer, ForeignKey("Bridges.id"))
    installer_id = Column(Integer, ForeignKey("Installers.id"))
    model = Column(String)
    description = Column(String)
    serial = Column(String)

    bridge = relationship("Bridge", back_populates="device")
    installer = relationship("Installer", back_populates="device")


class Installer(Base):
    """MCU Compiler
    """
    __tablename__ = "Installers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    device = relationship(
        "Device", back_populates="installer", cascade="all, delete-orphan")


class Bridge(Base):
    """Bridge that can connect to devices
    """

    __tablename__ = "Bridges"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String)
    name = Column(String)
    https = Column(Boolean)

    device = relationship("Device", back_populates="bridge",
                          cascade="all, delete-orphan")


class Dataset(Base):
    """Dataset that can be used to train models. 
    Actual files are in a folder, database contains path to the folder.
    """

    __tablename__ = "Datasets"

    id = Column(Integer, primary_key=True, index=True)
    path = Column(Integer)
    name = Column(Integer)
    description = Column(Integer)

    model = relationship("Model", back_populates="dataset")


class Model(Base):
    """Tensorflow model trained on a specified dataset. 
    Model file is saved as pickle in database.

    Parameters are divided by a slash(/) and they are in order
    epochs/img_width/img_height/batch_size
    """
    __tablename__ = "Models"

    id = Column(Integer, primary_key=True, index=True)
    created = Column(DateTime)
    dataset_id = Column(Integer, ForeignKey("Datasets.id"))
    parameters = Column(String)
    description = Column(String)
    model_path = Column(String)

    dataset = relationship("Dataset", back_populates="model")
    compiled_model = relationship("CompiledModel", back_populates="model")


class CompiledModel(Base):
    """Model compiled with TFLite to fit a MCU.
    Model file is saved in database.
    """

    __tablename__ = "Compiled_models"

    id = Column(Integer, primary_key=True, index=True)
    created = Column(DateTime)
    model_id = Column(Integer, ForeignKey("Models.id"))
    model_path = Column(String)

    model = relationship("Model", back_populates="compiled_model")

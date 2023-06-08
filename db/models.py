from sqlalchemy import Column, Integer, String, DateTime, LargeBinary, ForeignKey
from sqlalchemy.orm import relationship


from db.database import Base


class Device(Base):
    """MCU Device
    """

    __tablename__ = "Devices"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    connection = Column(String)
    installer = Column(String)
    compiler = Column(String)  # foreign key
    model = Column(String)
    description = Column(String)
    serial = Column(String)


class Compiler(Base):
    """MCU Compiler
    """
    __tablename__ = "Compilers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)


class Bridge(Base):
    """Bridge that can connect to devices
    """

    __tablename__ = "Bridges"

    id = Column(Integer, primary_key=True, index=True)
    ip_address = Column(String)
    name = Column(String)


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
    compiler_id = Column(Integer, ForeignKey(("Compilers.id")))
    model_path = Column(String)

    model = relationship("Model", back_populates="compiled_model")

from sqlalchemy import Column, Integer, String#, ForeignKey, DateTime
#from sqlalchemy.orm import relationship

from db.database import Base


class Device(Base):
    """MCU Device
    """

    __tablename__ = "Devices"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    connection = Column(String)
    installer = Column(String)
    compiler = Column(String) #foreign key
    model = Column(String)
    description = Column(String)
    serial = Column(String)


class Bridge(Base):
    """Bridge that can connect to devices
    """

    __tablename__ = "Bridges"

    id = Column(Integer, primary_key=True, index=True)
    ip_address = Column(String)
    name = Column(String)
    
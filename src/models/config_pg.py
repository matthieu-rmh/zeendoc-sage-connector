from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean
Base = declarative_base()

class ConfigModel(Base):
    __tablename__ = "configs"
    id = Column(Integer, primary_key=True, index=True)
    cupboard = Column(String, index=True)
    enabled = Column(Boolean, index=True)

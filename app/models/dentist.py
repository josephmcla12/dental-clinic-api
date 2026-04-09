from sqlalchemy import Column, Integer, String
from app.database import Base

class Dentist(Base):
    __tablename__ = "dentists"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    specialization = Column(String)
    email = Column(String, unique=True, index=True)
    phone_number = Column(String, unique=True, index=True)
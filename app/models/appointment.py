from sqlalchemy import Column, Integer, String
from app.database import Base

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer)
    dentist_id = Column(Integer)
    date = Column(String)
    time = Column(String)
    reason = Column(String)
    status = Column(String)
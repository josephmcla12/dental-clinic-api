from sqlalchemy import Column, ForeignKey, Integer, String
from app.database import Base
from sqlalchemy.orm import relationship

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String)
    time = Column(String)
    reason = Column(String)
    status = Column(String)

    patient_id = Column(Integer, ForeignKey("patients.id"))
    dentist_id = Column(Integer, ForeignKey("dentists.id"))

    patient = relationship("Patient", back_populates="appointments")
    dentist = relationship("Dentist", back_populates="appointments")

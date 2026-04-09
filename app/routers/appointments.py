from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.appointment import Appointment
from app.schemas.appointment import AppointmentCreate, AppointmentUpdate

router = APIRouter(
    prefix="/appointments",
    tags=["appointments"]
)

@router.get("/")
def get_appointments(db: Session = Depends(get_db)):
    return db.query(Appointment).all()

@router.post("/")
def create_appointment(appointment: AppointmentCreate, db: Session = Depends(get_db)):
    new_appointment = Appointment(
        patient_id=appointment.patient_id,
        dentist_id=appointment.dentist_id,
        date=appointment.date,
        time=appointment.time,
        reason=appointment.reason,
        status=appointment.status
    )
    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)
    return new_appointment

@router.get("/{appointment_id}")
def get_appointment(appointment_id: int, db: Session = Depends(get_db)):
    appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()
    if not appointment:
        return {"error": f"Appointment with id {appointment_id} not found"}
    return appointment

@router.put("/{appointment_id}")
def update_appointment(appointment_id: int, updated_data: AppointmentUpdate, db: Session = Depends(get_db)):
    appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()
    if not appointment:
        return {"error": f"Appointment with id {appointment_id} not found"}

    appointment.patient_id = updated_data.patient_id
    appointment.dentist_id = updated_data.dentist_id
    appointment.date = updated_data.date
    appointment.time = updated_data.time
    appointment.reason = updated_data.reason
    appointment.status = updated_data.status

    db.commit()
    db.refresh(appointment)
    return appointment
    
    db.commit()
    db.refresh(dentist)
    return dentist

@router.delete("/{appointment_id}")
def delete_appointment(appointment_id: int, db: Session = Depends(get_db)):
    appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()
    if not appointment:
        return {"error": f"Appointment with id {appointment_id} not found"}

    db.delete(appointment)
    db.commit()
    return {"message": f"Appointment with id {appointment_id} has been deleted"}
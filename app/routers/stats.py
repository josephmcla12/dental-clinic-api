from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date

from app.database import get_db
from app.models.appointment import Appointment
from app.models.dentist import Dentist
from app.models.patient import Patient

router = APIRouter(prefix="/stats", tags=["stats"])

@router.get("/appointments-per-day")
def appointments_per_day(db: Session = Depends(get_db)):
    results = (
        db.query(Appointment.date, func.count(Appointment.id))
        .group_by(Appointment.date)
        .all()
    )
    return [{"date": r[0], "count": r[1]} for r in results]

@router.get("/appointments-per-dentist")
def appointments_per_dentist(db: Session = Depends(get_db)):
    results = (
        db.query(Dentist.name, func.count(Appointment.id))
        .join(Appointment, Appointment.dentist_id == Dentist.id)
        .group_by(Dentist.name)
        .all()
    )
    return [{"dentist": r[0], "count": r[1]} for r in results]

@router.get("/patient-count")
def patient_count(db: Session = Depends(get_db)):
    count = db.query(func.count(Patient.id)).scalar()
    return {"total_patients": count}

@router.get("/dentist-count")
def dentist_count(db: Session = Depends(get_db)):
    count = db.query(func.count(Dentist.id)).scalar()
    return {"total_dentists": count}

@router.get("/upcoming-appointments")
def upcoming_appointments(db: Session = Depends(get_db)):
    today = date.today()
    count = (
        db.query(func.count(Appointment.id))
        .filter(Appointment.date >= today)
        .scalar()
    )
    return {"upcoming_appointments": count}


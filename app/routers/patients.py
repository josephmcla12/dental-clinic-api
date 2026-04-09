from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.patient import Patient
from app.schemas.patient import PatientCreate

router = APIRouter(
    prefix="/patients",
    tags=["patients"]
)

@router.get("/")
def get_patients(db: Session = Depends(get_db)):
    return db.query(Patient).all()

@router.post("/")
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    new_patient = Patient(
        name=patient.name,
        age=patient.age,
        email=patient.email,
        phone_number=patient.phone_number
    )
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return new_patient

@router.get("/{patient_id}")
def get_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        return {"error": f"Patient with id {patient_id} not found"}
    return patient
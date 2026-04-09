from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.patient import Patient
from app.schemas.patient import PatientCreate, PatientUpdate

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

@router.put("/{patient_id}")
def update_patient(patient_id: int, updated_data: PatientUpdate, db: Session = Depends(get_db)):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        return {"error": f"Patient with id {patient_id} not found"}
    
    patient.name = updated_data.name
    patient.age = updated_data.age
    patient.email = updated_data.email
    patient.phone_number = updated_data.phone_number
    
    db.commit()
    db.refresh(patient)
    return patient

@router.delete("/{patient_id}")
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        return {"error": f"Patient with id {patient_id} not found"}
    
    db.delete(patient)
    db.commit()
    return {"message": f"Patient with id {patient_id} has been deleted"}

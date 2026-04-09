from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.dentist import Dentist
from app.schemas.dentist import DentistCreate, DentistUpdate

router = APIRouter(
    prefix="/dentists",
    tags=["dentists"]
)

@router.get("/")
def get_dentists(db: Session = Depends(get_db)):
    return db.query(Dentist).all()

@router.post("/")
def create_dentist(dentist: DentistCreate, db: Session = Depends(get_db)):
    new_dentist = Dentist(
        name=dentist.name,
        specialization=dentist.specialization,
        email=dentist.email,
        phone_number=dentist.phone_number
    )
    db.add(new_dentist)
    db.commit()
    db.refresh(new_dentist)
    return new_dentist

@router.get("/{dentist_id}")
def get_dentist(dentist_id: int, db: Session = Depends(get_db)):
    dentist = db.query(Dentist).filter(Dentist.id == dentist_id).first()
    if not dentist:
        return {"error": f"Dentist with id {dentist_id} not found"}
    return dentist

@router.put("/{dentist_id}")
def update_dentist(dentist_id: int, updated_data: DentistUpdate, db: Session = Depends(get_db)):
    dentist = db.query(Dentist).filter(Dentist.id == dentist_id).first()
    if not dentist:
        return {"error": f"Dentist with id {dentist_id} not found"}
    
    dentist.name = updated_data.name
    dentist.specialization = updated_data.specialization
    dentist.email = updated_data.email
    dentist.phone_number = updated_data.phone_number
    
    db.commit()
    db.refresh(dentist)
    return dentist

@router.delete("/{dentist_id}")
def delete_dentist(dentist_id: int, db: Session = Depends(get_db)):
    dentist = db.query(Dentist).filter(Dentist.id == dentist_id).first()
    if not dentist:
        return {"error": f"Dentist with id {dentist_id} not found"}
    
    db.delete(dentist)
    db.commit()
    return {"message": f"Dentist with id {dentist_id} has been deleted"}

@router.get("/dentists/{dentist_id}/appointments")
def get_dentist_appointments(dentist_id: int, db: Session = Depends(get_db)):
    dentist = db.query(Dentist).filter(Dentist.id == dentist_id).first()

    if not dentist:
        raise HTTPException(status_code=404, detail="Dentist not found")

    return dentist.appointments

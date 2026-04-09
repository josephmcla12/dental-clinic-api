from fastapi import FastAPI
from app.routers import dentists, patients, appointments
from app.database import engine, Base
from app.models import patient, dentist, appointment

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

app.include_router(patients.router)
app.include_router(dentists.router)
app.include_router(appointments.router)

@app.get("/")
def root():
    return {"message": "Dental Clinic API is running!"}

@app.get("/hello")
def say_hello():
    return {"message": "Hello Joseph!"}

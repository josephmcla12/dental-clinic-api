from fastapi import FastAPI
from app.routers import patients

app = FastAPI()

app.include_router(patients.router)
@app.get("/")
def root():
    return {"message": "Dental Clinic API is running!"}

@app.get("/hello")
def say_hello():
    return {"message": "Hello Joseph!"}

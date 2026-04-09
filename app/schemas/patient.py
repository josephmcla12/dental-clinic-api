from pydantic import BaseModel

class PatientCreate(BaseModel):
    name: str
    age: int
    email: str
    phone_number: str

class PatientUpdate(BaseModel):
    name: str | None = None
    age: int | None = None
    email: str | None = None
    phone_number: str | None = None


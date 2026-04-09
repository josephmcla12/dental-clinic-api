from pydantic import BaseModel

class PatientCreate(BaseModel):
    name: str
    age: int
    email: str
    phone_number: str

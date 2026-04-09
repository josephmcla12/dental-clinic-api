from pydantic import BaseModel

class DentistCreate(BaseModel):
    name: str
    specialization: str
    email: str
    phone_number: str

class DentistUpdate(BaseModel):
    name: str | None = None
    specialization: str | None = None
    email: str | None = None
    phone_number: str | None = None



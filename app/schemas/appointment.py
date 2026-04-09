from pydantic import BaseModel

class AppointmentCreate(BaseModel):
    patient_id: int
    dentist_id: int
    date: str
    time: str
    reason: str
    status: str


class AppointmentUpdate(BaseModel):
    patient_id: int | None = None
    dentist_id: int | None = None
    date: str | None = None
    time: str | None = None
    reason: str | None = None
    status: str | None = None



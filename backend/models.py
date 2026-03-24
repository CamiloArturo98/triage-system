from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int
    symptoms: str
    heart_rate: int
    oxygen_level: int
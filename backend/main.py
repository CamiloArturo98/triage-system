from fastapi import FastAPI
from backend.models import Patient
from backend.triage_logic import classify_patient
from backend.database import add_patient, get_patients

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Triage API funcionando"}

@app.post("/triage")
def triage(patient: Patient):
    priority = classify_patient(patient)

    patient_data = patient.dict()
    patient_data["priority"] = priority

    add_patient(patient_data)

    return {
        "patient": patient.name,
        "priority": priority
    }

@app.get("/patients")
def patients():
    return get_patients()
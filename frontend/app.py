import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("🏥 Sistema de Triage - Urgencias")

# FORMULARIO
st.header("Registrar Paciente")

name = st.text_input("Nombre")
age = st.number_input("Edad", min_value=0, max_value=120)
symptoms = st.text_area("Síntomas")
heart_rate = st.number_input("Frecuencia Cardíaca", min_value=0)
oxygen_level = st.number_input("Nivel de Oxígeno (%)", min_value=0, max_value=100)

if st.button("Evaluar Paciente"):

    patient = {
        "name": name,
        "age": age,
        "symptoms": symptoms,
        "heart_rate": heart_rate,
        "oxygen_level": oxygen_level
    }

    response = requests.post(f"{API_URL}/triage", json=patient)

    if response.status_code == 200:
        result = response.json()

        st.success(f"Paciente: {result['patient']}")

        if result["priority"] == "ROJO":
            st.error("🔴 PRIORIDAD: CRÍTICO")

        elif result["priority"] == "AMARILLO":
            st.warning("🟡 PRIORIDAD: URGENTE")

        else:
            st.info("🟢 PRIORIDAD: LEVE")

# LISTADO
st.header("Pacientes Registrados")

if st.button("Actualizar lista"):
    response = requests.get(f"{API_URL}/patients")

    if response.status_code == 200:
        patients = response.json()

        for p in patients:
            st.write(p)
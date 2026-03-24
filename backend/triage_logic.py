def classify_patient(patient):
    """
    Clasifica pacientes en:
    - ROJO: crítico
    - AMARILLO: urgente
    - VERDE: leve
    """

    if patient.oxygen_level < 85 or patient.heart_rate > 130:
        return "ROJO"

    elif 85 <= patient.oxygen_level < 92 or 100 < patient.heart_rate <= 130:
        return "AMARILLO"

    else:
        return "VERDE"
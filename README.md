# 🏥 Sistema de Triage Hospitalario

Aplicación web para la clasificación de pacientes en un servicio de urgencias utilizando criterios básicos de triage.

Permite:

* Registrar pacientes
* Clasificarlos por prioridad (ROJO, AMARILLO, VERDE)
* Visualizar pacientes registrados
* Ver estadísticas básicas

---

# 🚀 Tecnologías utilizadas

* **Backend:** FastAPI (Python)
* **Frontend:** Streamlit
* **Base de datos:** SQLite
* **ORM:** SQLAlchemy

---

# 📁 Estructura del proyecto

```
triage-system/
│
├── backend/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── triage_logic.py
│   └── database.py
│
├── frontend/
│   └── app.py
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Requisitos

* Python 3.10 o superior
* pip

Verificar instalación:

```bash
python --version
pip --version
```

---

# 🧪 Instalación

## 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd triage-system
```

---

## 2. Crear entorno virtual (RECOMENDADO)

```bash
python -m venv venv
```

### Activar entorno

#### Windows:

```bash
venv\Scripts\activate
```

#### Linux / Mac:

```bash
source venv/bin/activate
```

---

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# ▶️ Ejecución del proyecto

## 🔹 1. Iniciar backend (FastAPI)

Desde la raíz del proyecto:

```bash
python -m uvicorn backend.main:app --reload
```

Deberías ver:

```
Uvicorn running on http://127.0.0.1:8000
```

---

## 🔹 2. Iniciar frontend (Streamlit)

En otra terminal (con el entorno activado):

```bash
python -m streamlit run frontend/app.py
```

---

## 🌐 Acceso a la aplicación

* Frontend:
  http://localhost:8501

* Backend (API):
  http://127.0.0.1:8000

* Documentación automática (Swagger):
  http://127.0.0.1:8000/docs

---

# 🧠 Lógica de Triage

| Prioridad   | Condición                                   |
| ----------- | ------------------------------------------- |
| 🔴 ROJO     | Oxígeno < 85 o FC > 130 o síntomas críticos |
| 🟡 AMARILLO | Oxígeno 85–91 o FC 101–130                  |
| 🟢 VERDE    | Condiciones estables                        |

---

# 🧪 Ejemplo de prueba

Registrar un paciente con:

* Nombre: Juan
* Edad: 65
* Frecuencia cardíaca: 140
* Oxígeno: 82

Resultado esperado:

```
🔴 ROJO (Crítico)
```

---

# 💾 Base de datos

Se utiliza SQLite automáticamente.

Archivo generado:

```
triage.db
```

No requiere configuración adicional.

---

# ⚠️ Problemas comunes

## ❌ “uvicorn no es reconocido”

Solución:

```bash
python -m uvicorn backend.main:app --reload
```

---

## ❌ “streamlit no es reconocido”

Solución:

```bash
python -m streamlit run frontend/app.py
```

---

## ❌ Error de módulos (backend o imports)

Asegúrate de:

* Ejecutar desde la raíz del proyecto
* Tener `__init__.py` en la carpeta backend

---

# 🚀 Posibles mejoras

* Autenticación de usuarios
* Base de datos PostgreSQL
* Dashboard avanzado
* WebSockets para tiempo real
* Deploy en la nube (Render, Railway)

---

# 👨‍💻 Autor

Proyecto académico de sistema de triage desarrollado con arquitectura cliente-servidor.

---

# 📄 Licencia

Uso académico.

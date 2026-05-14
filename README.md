# Hospital Triage System

Web application designed to classify patients in an emergency service using basic triage criteria.

The system allows users to:

- Register patients
- Classify patients by priority level (RED, YELLOW, GREEN)
- View registered patients
- Display basic statistics

---

# Technologies Used

- Backend: FastAPI (Python)
- Frontend: Streamlit
- Database: SQLite
- ORM: SQLAlchemy

---

# Project Structure

```text
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

# Requirements

- Python 3.10+
- pip

Verify installation:

```bash
python --version
pip --version
```

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/CamiloArturo98/triage-system.git
cd triage-system
```

---

## 2. Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

## 1. Start Backend (FastAPI)

From the project root:

```bash
python -m uvicorn backend.main:app --reload
```

Expected output:

```text
Uvicorn running on http://127.0.0.1:8000
```

---

## 2. Start Frontend (Streamlit)

Open another terminal:

```bash
python -m streamlit run frontend/app.py
```

---

# Application Access

## Frontend

```text
http://localhost:8501
```

## Backend API

```text
http://127.0.0.1:8000
```

## Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

---

# Triage Logic

| Priority | Condition |
|---|---|
| RED | Oxygen < 85 or heart rate > 130 or critical symptoms |
| YELLOW | Oxygen 85–91 or heart rate 101–130 |
| GREEN | Stable conditions |

---

# Example Test Case

Patient data:

- Name: Juan
- Age: 65
- Heart Rate: 140
- Oxygen Level: 82

Expected result:

```text
RED (Critical)
```

---

# Database

The project uses SQLite automatically.

Generated file:

```text
triage.db
```

No additional configuration is required.

---

# Common Issues

## Uvicorn Not Recognized

Run:

```bash
python -m uvicorn backend.main:app --reload
```

---

## Streamlit Not Recognized

Run:

```bash
python -m streamlit run frontend/app.py
```

---

## Module Import Errors

Ensure that:

- You are running commands from the project root
- `__init__.py` exists inside the backend folder

---

# Future Improvements

Potential future enhancements:

- User authentication
- PostgreSQL integration
- Advanced analytics dashboard
- Real-time communication with WebSockets
- Cloud deployment using Render or Railway

---

# Challenge

Full-stack triage management challenge developed with a client-server architecture using FastAPI, Streamlit, SQLite, and SQLAlchemy.

---

# Author

Developed by Camilo Arturo.

---

# License

For educational and portfolio purposes.

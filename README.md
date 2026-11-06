# 🥑 SmartStock AI: AI-Powered Food Waste & Inventory Optimizer

[![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688.svg?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.35+-FF4B4B.svg?logo=streamlit&logoColor=white)](https://streamlit.io)
[![Database](https://img.shields.io/badge/Database-IBM%20Db2%20%2F%20SQLite-052FAD.svg?logo=ibm&logoColor=white)](https://www.ibm.com/products/db2)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

An enterprise-grade, intelligent food waste mitigation and inventory optimization ecosystem powered by **IBM Db2**, Machine Learning (**Gradient Boosting**, **Random Forest**, **LightGBM**), and autonomous **Multi-Agent AI** (CrewAI / LangChain architecture).

---

## 📑 Table of Contents

- [Overview & Architecture](#-overview--architecture)
- [System Architecture Diagram](#-system-architecture-diagram)
- [Key Features](#-key-features)
- [Prerequisites & System Requirements](#-prerequisites--system-requirements)
- [Quickstart Installation](#-quickstart-installation)
- [Configuration (.env)](#-configuration-env)
- [Database Initialization](#-database-initialization)
- [Running the Application](#-running-the-application)
- [Shutting Down the Application](#-shutting-down-the-application)
- [Default Demo Credentials](#-default-demo-credentials)
- [System Integration Tests](#-system-integration-tests)
- [REST API Endpoints](#-rest-api-endpoints)
- [Machine Learning Retraining](#-machine-learning-retraining)
- [Security & Sensitive Data Isolation](#-security--sensitive-data-isolation)

---

## 🌟 Overview & Architecture

Restaurants and commercial food service establishments lose thousands of dollars each month due to food spoilage, poor stock visibility, and uncoordinated purchasing. **SmartStock AI** solves this through an end-to-end operational intelligence loop:

1. **FEFO (First-Expired, First-Out) Tracking**: Real-time batch-level expiration tracking with automated shelf-life degradation monitors.
2. **AI Waste Risk Prediction**: Machine learning models estimate spoilage probability and excess unconsumed quantity before items spoil.
3. **Demand Forecasting**: Multi-horizon (1, 3, and 7-day) perishable consumption forecasts accounting for seasonality, day of week, and historical trends.
4. **AI Recipe Recommendation Engine**: Semantic recipe matchmaking that prioritizes expiring stock to maximize ingredient utilization.
5. **Intelligent Purchasing Assistant**: Automated purchase order generation calibrated against supplier lead times, minimum order quantities (MOQs), and predicted stockouts.
6. **Autonomous Multi-Agent Crew**: A 6-agent collaborative AI team that diagnoses operations, formulates menus, budgets replenishment, and prepares executive briefings.
7. **Natural Language Assistant**: Read-only Text-to-SQL + RAG conversational interface powered by local LLM (`liquid/lfm2.5-1.2b` via LM Studio).

---

## 📊 System Architecture Diagram

![SmartStock AI Architecture & Flow](smartstockAIflow%20diagram.png)

```
┌────────────────────────────────────────────────────────────────────────┐
│                      STREAMLIT WEB FRONTEND                            │
│   (Dashboard • Inventory • Predictions • Recipes • Orders • Agents)     │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ HTTP / REST
┌───────────────────────────────────▼────────────────────────────────────┐
│                       FASTAPI BACKEND SERVICE                          │
│   (25+ REST Endpoints • Services Layer • Analytics • What-If Engine)   │
└──────────────┬────────────────────┬────────────────────┬───────────────┘
               │                    │                    │
┌──────────────▼─────┐  ┌───────────▼────────┐  ┌────────▼───────────────┐
│     IBM Db2 /      │  │  MACHINE LEARNING  │  │   MULTI-AGENT CREW     │
│  SQLite Fallback   │  │ (Waste & Demand)   │  │   & LM STUDIO LLM      │
│  10 Relational     │  │ Pretrained Models  │  │ 6 Autonomous Agents    │
│  Tables + Vectors  │  │ (.joblib < 3.5 MB) │  │ Text-to-SQL + RAG      │
└────────────────────┘  └────────────────────┘  └────────────────────────┘
```

---

## 📁 Repository Structure

```
smartstock-ai/
├── .env.example             # Environment variable template
├── .gitignore               # Strict exclusion rules (secrets, venvs, DBs)
├── config.py                # Centralized paths and settings loader
├── requirements.txt         # Production Python dependencies
├── run.py                   # Unified launcher for FastAPI + Streamlit
├── test_smartstock.py       # End-to-end 10-module integration test suite
├── smartstockAIflow diagram.png # System architecture diagram
├── SmartStock_AI_Round1_Proposal.pptx # Project proposal presentation
│
├── agents/                  # AI & Multi-Agent Intelligence
│   ├── chatbot.py           # Text-to-SQL & RAG Natural Language Assistant
│   └── multi_agent_system.py# 6-Agent Inventory Optimization Crew
│
├── backend/                 # FastAPI REST API Backend
│   ├── main.py              # API application & route definitions
│   └── services/            # Domain business logic & services
│       ├── analytics_service.py   # Financial metrics & executive summaries
│       ├── demand_service.py      # Demand forecasting engine
│       ├── diagnostic_service.py  # Db2 connection diagnostics
│       ├── inventory_service.py   # FEFO batches & stock movements
│       ├── movement_service.py    # Audit logging for inventory changes
│       ├── purchasing_service.py  # Purchase orders & supplier workflows
│       ├── recipe_service.py      # Expiration-driven recipe matching
│       ├── supplier_service.py    # Supplier catalogs & ratings
│       ├── user_service.py        # RBAC, authentication & security recovery
│       ├── waste_service.py       # Spoilage risk classification
│       └── whatif_service.py      # Demand surge scenario simulations
│
├── data/                    # Training and benchmark datasets
│   ├── README.md            # Dataset descriptions
│   ├── eval.parquet         # Perishable demand records (8.4 MB)
│   └── food_waste_dataset.csv # Spoilage and waste history (750 KB)
│
├── db/                      # Database Layer
│   ├── db2_client.py        # IBM Db2 client with SQLite local mirror fallback
│   ├── schema.py            # DDL schemas for all 10 relational tables
│   └── seed_data.py         # Seed dataset with demo inventory & users
│
├── frontend/                # Streamlit Web Application
│   ├── app.py               # Enterprise multi-view portal & authentication
│   └── components/          # Reusable UI cards and Plotly charts
│       ├── charts.py        # Modern dark-mode Plotly visualizations
│       └── ui_helpers.py    # CSS styling, badges, and layout helpers
│
└── ml/                      # Machine Learning Training & Inference
    ├── predictor.py         # Real-time inference engine
    ├── train_demand_model.py# Demand model training script
    ├── train_waste_model.py # Waste prediction training script
    └── models/              # Pretrained model weights
        ├── demand_forecaster.joblib
        ├── demand_metadata.json
        ├── waste_classifier.joblib
        ├── waste_metadata.json
        └── waste_regressor.joblib
```

---

## 💻 Prerequisites & System Requirements

- **Operating System**: Windows 10/11, macOS, or Linux.
- **Python**: Version `3.10`, `3.11`, or `3.12`.
- **Database (Zero-Friction Option)**: No external setup required! If an IBM Db2 instance is not found, the system **automatically falls back to the embedded SQLite engine** with identical schema and full transactional integrity.
- **Optional - IBM Db2 Container**: Docker installed if you wish to run IBM Db2 locally (`docker run -d --name db2server -p 50000:50000 ...`).
- **Optional - Local LLM**: [LM Studio](https://lmstudio.ai/) running `liquid/lfm2.5-1.2b` on port `1234` for natural language chat features (falls back to rule-based parsing if offline).

---

## ⚡ Quickstart Installation

### 1. Clone the Repository
```bash
git clone https://github.com/ashfinashfi/SmartStock-AI.git
cd SmartStock-AI
```

### 2. Create and Activate a Virtual Environment
```bash
# On Windows (PowerShell):
python -m venv .venv
.venv\Scripts\Activate.ps1

# On Windows (Command Prompt):
python -m venv .venv
.venv\Scripts\activate.bat

# On Linux / macOS:
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Python Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## ⚙️ Configuration (.env)

Create your local `.env` file by copying the provided `.env.example`:

```bash
# On Windows (PowerShell):
Copy-Item .env.example .env

# On Linux / macOS:
cp .env.example .env
```

Default contents of `.env`:
```ini
# IBM Db2 Enterprise Configuration (Optional - falls back to SQLite if offline)
DB2_CONTAINER=db2server
DB2_DATABASE=testdb
DB2_USER=db2inst1
DB2_PASSWORD=your_db2_password_here
DB2_HOST=localhost
DB2_PORT=50000

# Local LM Studio LLM Endpoint (Optional)
LMSTUDIO_URL=http://127.0.0.1:1234/v1
LLM_MODEL=liquid/lfm2.5-1.2b
```

> [!NOTE]
> `.env` is listed in `.gitignore` and will never be committed to Git.

---

## 🗄️ Database Initialization

Initialize the database schema and populate realistic operational seed data:

```bash
# Initialize 10 relational tables
python -m db.schema

# Populate suppliers, ingredients, batches, recipes, and users
python -m db.seed_data
```

---

## 🚀 Running the Application

### Option A: Unified Launcher (Recommended)
Launch both the **FastAPI backend** and **Streamlit frontend** with a single command:

```bash
python run.py
```

This will automatically:
1. Start the FastAPI server on `http://127.0.0.1:8000`.
2. Start the Streamlit portal on `http://localhost:8501`.
3. Open the web interface in your default browser.

### Option B: Running Services Separately (Development Mode)
If you prefer running the backend and frontend in separate terminals:

**Terminal 1 — Backend (FastAPI)**:
```bash
uvicorn backend.main:app --host 127.0.0.1 --port 8000 --reload
```
- API Root: `http://127.0.0.1:8000`
- Swagger Interactive Documentation: `http://127.0.0.1:8000/docs`
- ReDoc Documentation: `http://127.0.0.1:8000/redoc`

**Terminal 2 — Frontend (Streamlit)**:
```bash
streamlit run frontend/app.py
```
- Web Application: `http://localhost:8501`

---

## 🛑 Shutting Down the Application

### 1. Stopping Unified Launcher (`run.py`)
Press `Ctrl + C` in the terminal where `python run.py` is running.
- The launcher intercepts the interrupt, gracefully terminates the background FastAPI process, and closes Streamlit.

### 2. Stopping Separate Terminals
Press `Ctrl + C` in both the backend and frontend terminal windows.

### 3. Clearing Stale Ports (Troubleshooting)
If a process keeps the port open after an unexpected terminal close:

**On Windows (PowerShell)**:
```powershell
# Free port 8000 (Backend)
Get-Process -Id (Get-NetTCPConnection -LocalPort 8000).OwningProcess -ErrorAction SilentlyContinue | Stop-Process -Force

# Free port 8501 (Frontend)
Get-Process -Id (Get-NetTCPConnection -LocalPort 8501).OwningProcess -ErrorAction SilentlyContinue | Stop-Process -Force
```

**On Linux / macOS**:
```bash
lsof -ti:8000,8501 | xargs kill -9
```

### 4. Stopping Optional Background Services
- **IBM Db2 Docker Container**:
  ```bash
  docker stop db2server
  ```
- **LM Studio**: Close the LM Studio application or toggle off the local inference server.

---

## 🔑 Default Demo Credentials

The database comes pre-seeded with four role-based accounts for testing:

| Role | Username | Password | Security Question / Answer | Primary Permissions |
| :--- | :--- | :--- | :--- | :--- |
| **Administrator** | `admin` | `admin123` | *Favorite food:* `biryani` | Full system access, User Management, PO Approvals |
| **Head Chef** | `chef_marcus` | `admin123` | *Favorite food:* `biryani` | Recipe Recommendations, Consumption Logging, Inventory View |
| **Inventory Manager** | `inv_clerk` | `admin123` | *Favorite food:* `biryani` | Stock In/Out, PO Generation, FEFO Batch Auditing |
| **Kitchen Staff** | `sous_chef` | `admin123` | *Favorite food:* `biryani` | FEFO Consumption, Expiry Inspection |

> [!TIP]
> You can also register a brand new account using the **"Create an account"** link on the login screen.

---

## 🧪 System Integration Tests

Run the comprehensive 10-module automated test suite:

```bash
python test_smartstock.py
```

The test verifies:
- `[Test 1]` IBM Db2 / SQLite connectivity and health check
- `[Test 2]` Inventory batch retrieval and FEFO chronological sorting
- `[Test 3]` Transactional FEFO ingredient consumption and stock deduction
- `[Test 4]` AI waste risk scoring and excess volume calculation
- `[Test 5]` 7-day multi-horizon demand forecasting and shortage detection
- `[Test 6]` Recipe matchmaking prioritizing ingredients with nearest expiration
- `[Test 7]` Purchase order suggestion and management approval workflow
- `[Test 8]` What-If demand surge simulation (+30% demand stress test)
- `[Test 9]` 6-Agent autonomous Multi-Agent Optimization Crew execution
- `[Test 10]` Natural Language Chatbot (Text-to-SQL & RAG fallback)

---

## 🌐 REST API Endpoints

The backend provides over 25 REST endpoints accessible via `http://127.0.0.1:8000/docs`:

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/health` | Health check for API and IBM Db2 / SQLite connection |
| `GET` | `/api/inventory/batches` | List active inventory batches with FEFO status |
| `POST` | `/api/inventory/consume` | Consume ingredient using FEFO automatic batch deduction |
| `GET` | `/api/waste/predictions` | Spoilage risk classification & excess volume estimates |
| `GET` | `/api/demand/forecasts` | Multi-horizon demand predictions (1, 3, or 7 days) |
| `GET` | `/api/recipes/recommended` | Recipes sorted by expiring ingredient utilization |
| `GET` | `/api/purchasing/recommendations` | Automated PO recommendations for impending shortages |
| `POST` | `/api/purchasing/orders` | Create a new purchase order |
| `POST` | `/api/purchasing/orders/{id}/approve` | Approve a pending purchase order |
| `POST` | `/api/whatif/simulate` | Simulate demand shifts (e.g., +25% surge) |
| `POST` | `/api/agents/run` | Execute the 6-agent autonomous optimization crew |
| `POST` | `/api/chat` | Natural Language Query with Text-to-SQL + RAG |
| `POST` | `/api/auth/login` | Authenticate user credentials |
| `POST` | `/api/auth/register` | Register new user with security recovery setup |

---

## 🤖 Machine Learning Retraining

To retrain the ML models on updated datasets:

```bash
# 1. Retrain Food Waste Risk Classifier & Excess Regressor:
python -m ml.train_waste_model

# 2. Retrain Demand Forecaster (Perishables Dataset):
python -m ml.train_demand_model
```

Trained binaries are saved directly to `ml/models/` as lightweight `.joblib` files (< 3.5 MB total), making them fast and version-control friendly.

---

## 🔒 Security & Sensitive Data Isolation

SmartStock AI is designed strictly adhering to security best practices:

- **Zero Hardcoded Secrets**: All database connection strings, passwords, and API hosts are read from environment variables via `.env`.
- **Git Ignore Guards**: `.gitignore` strictly ignores:
  - Local environment configs (`.env`, `.env.*.local`)
  - Virtual environments (`.venv/`, `env/`, `venv/`)
  - Local database mirrors (`smartstock.db`, `*.sqlite`, `*.db`)
  - Python cache artifacts (`__pycache__/`, `*.pyc`)
  - Private keys, certificates, and logs (`*.pem`, `*.key`, `*.log`)
- **Password Security**: Passwords and security recovery answers are hashed using SHA-256 before being committed to persistent storage.
- **SQL Injection Defenses**: The natural language Text-to-SQL parser enforces strict read-only execution barriers preventing DDL/DML mutation queries.

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

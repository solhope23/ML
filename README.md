# Naive Bayes Classifier – Microservices Version (v2.0)

This project implements a modular Naive Bayes classification system using **FastAPI** and **Docker**, built with a microservices architecture:

- `model_server`: Trains and serves a probabilistic model.
- `cls_server`: Loads the model and classifies new input instances via API.

> 🧠 **Note:** The dataset provided (`mushroom.csv`) is just a placeholder.  
> The system is designed to support **any tabular dataset** with categorical features and a target label.

---

## 🧱 Architecture

```
+-------------+       HTTP        +-------------+
|             |  <-------------  |             |
| cls_server  |   GET model      | model_server|
|             |   POST classify  |             |
+-------------+                  +-------------+
```

---

## 📁 Project Structure

```
ML-2.0/
│
├── docker-compose.yml
├── model_server/      # Trains and serves model
│   ├── data/          # Sample data (optional)
│   └── core/          # Logic: load, clean, build, validate
└── cls_server/        # Loads model & classifies instances
    └── core/          # Classification logic
```

---

## 🚀 How to Run

Make sure you have **Docker** and **Docker Compose** installed.

### ▶️ Run the system

```bash
docker compose up --build
```

This will:
- Train the model inside `model_server`
- Launch `cls_server` with access to the trained model

Services:
- `model_server` → http://localhost:8000
- `cls_server` → http://localhost:8001

---

## 📮 API Endpoints

### model_server

| Method | Endpoint        | Description              |
|--------|------------------|--------------------------|
| GET    | `/get-model`     | Returns trained model as JSON |

### cls_server

| Method | Endpoint        | Description              |
|--------|------------------|--------------------------|
| GET    | `/form`          | HTML form for manual classification |
| GET    | `/health`        | Health check             |
| (Planned) | `/classify`   | API for structured JSON input |

---

## 🧠 Custom Dataset

To use your own data:
1. Replace or load your CSV in `model_server/data/`
2. Update `model_server/core/dat.py` to read your file
3. Make sure your data contains only **categorical features** and a **target column**
4. Rebuild and restart the system:

```bash
docker compose up --build
```

---

## ✅ Features

- Works with any categorical tabular dataset
- Two-container architecture (train + classify)
- Stateless classification microservice
- Clean, extendable FastAPI backend
- Dockerized for easy deployment

---

## 📌 Requirements (inside containers)

- Python 3.11+
- FastAPI, Uvicorn
- pandas
- requests

---

## 👤 Author

Created by **Shlomo Hofman**  
GitHub: [@solhope23](https://github.com/solhope23)

---

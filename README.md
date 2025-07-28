# Naive Bayes Classifier – Microservices Version (v2.0)

This project implements a modular Naive Bayes classification system using **FastAPI** and **Docker**, now split into two microservices:

- `model_server`: Responsible for training and serving the model.
- `cls_server`: Consumes the model and performs classification based on user input.

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
└── cls_server/        # Loads model from model_server and classifies input
```

---

## 🚀 How to Run

Make sure you have **Docker** and **Docker Compose** installed.

### ▶️ Run the system

```bash
docker compose up --build
```

This will build and run both services:
- `model_server` on port **8000**
- `cls_server` on port **8001**

---

## 🐳 Individual Services

### model_server

- Trains a Naive Bayes model on `mushroom.csv`
- Serves the model via `/get-model` endpoint

```bash
http://localhost:8000/get-model
```

### cls_server

- Fetches the model from `model_server`
- Exposes:
  - `/form` – HTML form for manual input
  - `/classify` – (future) REST API for automated classification

```bash
http://localhost:8001/form
```

---

## 📦 Dataset

The model is trained on the **Mushroom dataset**, which includes:
- Features like cap-shape, odor, gill-size, etc.
- Target variable: `class` (edible or poisonous)

---

## ✅ Features

- Two-service microservice design
- Clean separation of model and classifier
- API-based communication between services
- FastAPI + Dockerized for deployment

---

## 📌 Requirements (inside containers)

- Python 3.11+
- fastapi, uvicorn
- pandas
- requests

---

## 👤 Author

Created by **Shlomo Hofman**  
GitHub: [@solhope23](https://github.com/solhope23)

---


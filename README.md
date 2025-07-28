# Naive Bayes Classifier API – Version 1.0

This project provides a FastAPI-based service that classifies input instances using a Naive Bayes model trained on tabular data.  
The system includes components for data loading, cleaning, model building, validation, and classification.

> 🧠 **Note:** The included dataset (`buy_computer_data.csv`) is just an example.  
> The system is designed to work with **any categorical tabular dataset** and can be adapted accordingly.

---

## 📁 Project Structure

```
ML-1.0/
│
├── app/                   # Core logic modules
│   ├── dat.py             # Data reader
│   ├── cln.py             # Data cleaner
│   ├── bld.py             # Model builder
│   ├── vld.py             # Model validator
│   ├── cls.py             # Classifier
│   ├── model.py           # Model structure
│   ├── model_manager.py   # Builder + Coordinator
│   └── __init__.py
│
├── data/
│   └── buy_computer_data.csv  # Sample dataset only
│
├── main.py               # FastAPI app entry point
├── Dockerfile            # Docker container definition
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## 🚀 How to Run

### 🔧 1. Clone the repository

```bash
git clone https://github.com/solhope23/ML.git
cd ML
```

### 🐍 2. Install dependencies (locally)

```bash
pip install -r requirements.txt
```

### ▶️ 3. Run the FastAPI server

```bash
uvicorn main:app --reload
```

Access the API docs at:  
**http://127.0.0.1:8000/docs**

---

## 🐳 Run with Docker

### 📦 Build the image

```bash
docker build -t ml-api .
```

### ▶️ Run the container

```bash
docker run -p 8000:8000 ml-api
```

---

## 📮 API Endpoints

| Method | Endpoint      | Description               |
|--------|---------------|---------------------------|
| GET    | `/form`       | Interactive HTML form     |
| POST   | `/form`       | Submit instance to classify |
| GET    | `/health`     | Health check              |

---

## 🧠 Custom Dataset

To use your own data:
1. Replace `data/buy_computer_data.csv` with your dataset
2. Make sure all features are **categorical** and a **target column** is clearly defined
3. Update the loader logic in `dat.py` if needed
4. Restart the app (or rebuild container if using Docker)

---

## ✅ Features

- Works with any categorical tabular data
- Model trained on startup
- FastAPI backend with interactive HTML form
- Dockerized for easy deployment
- Laplace smoothing in Naive Bayes

---

## 📌 Requirements

- Python 3.11+
- FastAPI
- pandas
- uvicorn

---

## 👤 Author

Created by **Shlomo Hofman**  
GitHub: [@solhope23](https://github.com/solhope23)

---

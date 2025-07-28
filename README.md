# Naive Bayes Classifier API

This project provides a FastAPI-based service that classifies input instances using a Naive Bayes model trained on tabular data.  
The system is built modularly and includes data loading, cleaning, model building, validation, and classification components.

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
│   └── buy_computer_data.csv  # Sample training dataset
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

## 📊 Dataset

The system uses the classic **"Buy Computer"** dataset, which includes features like:
- Age
- Income
- Student
- Credit Rating  
and the target label: `buys_computer`

---

## ✅ Features

- Clean modular design
- Model is trained at startup
- FastAPI backend with HTML form
- Dockerized for easy deployment
- Uses Laplace smoothing for Naive Bayes

---

## 📌 Requirements

- Python 3.11+
- FastAPI
- pandas, scikit-learn (if used)
- uvicorn

---

## 🧠 Future Work

- Add support for model persistence (save/load)
- Add REST endpoint for programmatic classification
- Deploy to cloud (e.g., Render, Railway, Heroku)

---

## 👤 Author

Created by **Shlomo Hofman**  
GitHub: [@solhope23](https://github.com/solhope23)

---

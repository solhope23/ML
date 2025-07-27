from typing import Optional
from fastapi import FastAPI
from core.model_manager import ModelManager
from core.model import Model

app = FastAPI()

model: Optional[Model] = None

@app.on_event("startup")
def train_model():
    global model
    try:
        model = ModelManager.builder()
        print(f"Model trained")
    except Exception as e:
        print("Failed to train model on startup.")
        print(f"Reason: {str(e)}")
        raise RuntimeError("Startup failed – model training failed.")

@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/get-model")
def get_model():
    return model.to_dict()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
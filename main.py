from typing import Optional
from fastapi import FastAPI
from app.model_manager import ModelManager
from app.model import Model
from fastapi.responses import HTMLResponse
from app.cls import CLS
from fastapi import Request

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


@app.get("/form", response_class=HTMLResponse)
def form():

    html = "<h2>Classify Instance</h2><form method='post'>"

    for feature, values in model.model_schema.items():
        if feature != model.target_col:
            html += f"<label>{feature}</label><br>"
            html += f"<select name='{feature}'>"
            for val in values:
                html += f"<option value='{val}'>{val}</option>"
            html += "</select><br><br>"

    html += "<input type='submit' value='Submit'></form>"
    return HTMLResponse(content=html)


@app.post("/form", response_class=HTMLResponse)
async def classify_form(request: Request):

    form_data = await request.form()
    input_dict = dict(form_data)

    try:
        prediction = CLS.classify(input_dict, model.conditional_dict)

        return HTMLResponse(
            content=(
                f"<h2>Prediction: {prediction}</h2>"
                f"<p><strong>Model Accuracy:</strong> {model.model_accuracy:.2f}%</p>"
                f"<br><a href='/form'>🔙 Back</a>"
            )
        )
    except Exception as e:
        return HTMLResponse(
            content=f"<h2>Error: {str(e)}</h2><a href='/form'>🔙 Back</a>"
        )

@app.get("/")
def read_root():
    return {"message": "Server is up and running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
from typing import Optional
from fastapi import FastAPI
from core.model import Model
from fastapi.responses import HTMLResponse
from core.cls import CLS
from fastapi import Request
import requests
import os
import time


def wait_for_model(timeout=30):
    url = f"http://{host}:{port}/health"

    for i in range(timeout):
        try:
            r = requests.get(url, timeout=1)
            if r.status_code == 200:
                print("model_server is ready.")
                return
        except Exception as e:
            print(f"model_server not ready yet: {e}")
        print(f"Waiting for model_server... ({i + 1}/{timeout})")
        time.sleep(1)

    raise RuntimeError("model_server not available after timeout.")

app = FastAPI()

model: Optional[Model] = None

host = os.getenv("MODEL_SERVER_HOST", "localhost")
port = os.getenv("MODEL_SERVER_PORT", "8000")

@app.on_event("startup")
def fetch_model():
    global model
    try:
        wait_for_model()
        response = requests.get(f"http://{host}:{port}/get-model")
        response.raise_for_status()
        model = Model(**response.json())
        print("Model fetched from model_server")
    except Exception as e:
        print("Failed to fetch model from main_server")
        print(f"Reason: {str(e)}")
        raise RuntimeError("Startup failed – model fetch failed.")


@app.get("/form", response_class=HTMLResponse)
def form():

    target_col = model.target_col
    target_values = model.model_schema.get(target_col, [])

    html = (
        "<h2>Classify Instance</h2>"
        f"<h4>Target column: <u>{target_col}</u> &rarr; {target_values}</h4>"
        "<form method='post'>"
    )

    for feature, values in model.model_schema.items():
        if feature != target_col:
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


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)

from fastapi import FastAPI
from pydantic import BaseModel
from app.model import predict

app = FastAPI()


class Item(BaseModel):
    text: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict_spam(item: Item):
    result = predict(item.text)
    return result

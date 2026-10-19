from fastapi import FastAPI
import joblib

app = FastAPI()
model = joblib.load("models/spam.pkl")

@app.get("/predict")
def predict(text: str):
    pred = model.predict([text])
    return {"result": int(pred[0])}

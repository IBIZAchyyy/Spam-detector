"""垃圾邮件检测 FastAPI 服务入口。"""

from fastapi import FastAPI
from pydantic import BaseModel, Field

from app.model import predict

app = FastAPI(title="Spam Detector API", version="1.0.0")


class PredictRequest(BaseModel):
    text: str = Field(..., description="待检测的短信/邮件文本")


class PredictResponse(BaseModel):
    label: str = Field(..., description="spam 或 ham")
    confidence: float = Field(..., description="预测置信度 0~1")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
def predict_spam(req: PredictRequest):
    result = predict(req.text)
    return PredictResponse(**result)

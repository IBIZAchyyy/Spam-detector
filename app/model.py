"""模型加载与预测封装。"""
import os
import pickle
from pathlib import Path

# 模型文件路径：优先用环境变量指定，否则用默认位置
MODEL_PATH = os.getenv(
    "MODEL_PATH",
    str(Path(__file__).resolve().parent.parent / "ml" / "registry" / "spam_model.pkl"),
)

_model = None


def load_model():
    """加载模型（只加载一次，单例）。"""
    global _model
    if _model is None:
        with open(MODEL_PATH, "rb") as f:
            _model = pickle.load(f)
    return _model


def predict(text: str) -> dict:
    """输入一段文本，返回预测结果。"""
    model = load_model()
    label_id = model.predict([text])[0]
    proba = model.predict_proba([text])[0]
    label = "spam" if label_id == 1 else "ham"
    confidence = float(max(proba))
    return {"label": label, "confidence": round(confidence, 4)}

"""模型预测测试：覆盖垃圾邮件、正常邮件和边界情况。"""

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


# 用例 1：典型垃圾邮件
@pytest.mark.parametrize(
    "text",
    [
        "WINNER!! You won a FREE iPhone! Click http://win.com now!",
        "FREE entry in weekly competition to win £1000. Text WIN to 80088 now!",
        "Congratulations! You have been selected for a $1000 cash prize",
    ],
)
def test_predict_spam(text):
    resp = client.post("/predict", json={"text": text})
    assert resp.status_code == 200
    body = resp.json()
    assert body["label"] == "spam"
    assert 0.0 <= body["confidence"] <= 1.0


# 用例 2：典型正常邮件
@pytest.mark.parametrize(
    "text",
    [
        "Hi John, are we still meeting for lunch tomorrow?",
        "Dad, can you pick me up after school today?",
        "Thanks for your email, I will reply by end of day",
    ],
)
def test_predict_ham(text):
    resp = client.post("/predict", json={"text": text})
    assert resp.status_code == 200
    body = resp.json()
    assert body["label"] == "ham"
    assert 0.0 <= body["confidence"] <= 1.0


# 用例 3：边界情况
@pytest.mark.parametrize(
    "text",
    [
        "",  # 空文本
        "a",  # 极短文本
        "Free money " * 100,  # 长文本
        "!!!@@@###$$$",  # 纯符号
        "1234567890",  # 纯数字
    ],
)
def test_predict_edge_cases(text):
    """边界情况不应崩溃，返回格式正确即可。"""
    resp = client.post("/predict", json={"text": text})
    assert resp.status_code == 200
    body = resp.json()
    assert body["label"] in ("spam", "ham")
    assert 0.0 <= body["confidence"] <= 1.0

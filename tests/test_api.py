"""API 接口测试。"""

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    """健康检查接口正常返回。"""
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}

import requests

# 测试垃圾邮件
def test_spam():
    resp = requests.get("http://127.0.0.1:8000/predict",
                        params={"text": "Win free cash! Send your bank account now."})
    data = resp.json()
    assert data["result"] == 1

# 测试普通邮件
def test_normal():
    resp = requests.get("http://127.0.0.1:8000/predict",
                        params={"text": "Hello, how are you today?"})
    data = resp.json()
    assert data["result"] == 0

if __name__ == "__main__":
    test_spam()
    test_normal()
    print("所有测试用例执行完毕")

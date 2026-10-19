import pandas as pd
import joblib
import json
from sklearn.metrics import accuracy_score, recall_score, precision_score, confusion_matrix

# 加载训练好的模型
model = joblib.load("models/spam.pkl")
# 读取测试数据集
test_data = pd.read_csv("data/test.csv")

# 拿到文本和真实标签
X_test = test_data["message"]
y_real = test_data["label"]

# 用模型做预测
y_predict = model.predict(X_test)

# 计算各项指标
acc = accuracy_score(y_real, y_predict)
recall = recall_score(y_real, y_predict)
precision = precision_score(y_real, y_predict)
conf_matrix = confusion_matrix(y_real, y_predict)

# 打印结果
print("模型准确率：", acc)
print("模型召回率：", recall)
print("模型精确率：", precision)
print("混淆矩阵：")
print(conf_matrix)

# 保存指标到json，给DVC流水线使用
result = {
    "accuracy": acc,
    "recall": recall,
    "precision": precision,
    "confusion_matrix": conf_matrix.tolist()
}
with open("metrics.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=2)

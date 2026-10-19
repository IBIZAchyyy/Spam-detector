import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import mlflow

# 删掉 set_experiment，直接写入Default实验
print("开始读取train.csv", flush=True)
train = pd.read_csv("data/train.csv")
print("读取完成", flush=True)

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("lr", LogisticRegression())
])

print("开始训练模型", flush=True)
# 启动run
with mlflow.start_run(run_name="spam_train") as run:
    mlflow.log_param("model_name", "LogisticRegression")
    mlflow.log_param("feature", "TF-IDF")

    model.fit(train["message"], train["label"])
    train_acc = model.score(train["message"], train["label"])
    mlflow.log_metric("train_acc", train_acc)
    print(f"训练集准确率：{train_acc}")
# 退出with块，mlflow自动结束并保存run

print("训练完成，准备保存模型", flush=True)
joblib.dump(model, "models/spam.pkl")
print("模型训练好了")

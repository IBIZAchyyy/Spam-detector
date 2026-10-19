import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

print("开始读取train.csv", flush=True)
train = pd.read_csv("data/train.csv")
print("读取完成", flush=True)

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("lr", LogisticRegression())
])
print("开始训练模型", flush=True)
model.fit(train["message"], train["label"])
print("训练完成，准备保存模型", flush=True)

joblib.dump(model, "models/spam.pkl")
print("✅ 模型训练好了，已保存到models/spam.pkl")

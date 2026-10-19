import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
from ml.data_pipeline import load_data, clean_text

try:
    import mlflow

    has_mlflow = True
except ImportError:
    has_mlflow = False

# 是不是跑改进实验
bigram = os.getenv("BASELINE", "1") == "0"
C = 10.0 if bigram else 1.0

# 读数据
df = load_data()
df["text"] = df["text"].apply(clean_text)

# 拆分训练集测试集
x_train, x_test, y_train, y_test = train_test_split(
    df["text"], df["label_num"], test_size=0.2, random_state=42
)

# TF-IDF + 逻辑回归
vec = TfidfVectorizer(ngram_range=(1, 2) if bigram else (1, 1), stop_words="english")
x_train_vec = vec.fit_transform(x_train)
x_test_vec = vec.transform(x_test)

clf = LogisticRegression(C=C, max_iter=1000)
clf.fit(x_train_vec, y_train)

# 算指标
pred = clf.predict(x_test_vec)
acc = accuracy_score(y_test, pred)
f1 = f1_score(y_test, pred)

print(f"准确率: {acc:.4f}, F1: {f1:.4f}")

# 保存模型
with open("ml/registry/spam_model.pkl", "wb") as f:
    pickle.dump((vec, clf), f)

# 记录到mlflow
if has_mlflow:
    mlflow.set_experiment("spam-detector")
    with mlflow.start_run():
        mlflow.log_param("C", C)
        mlflow.log_param("bigram", bigram)
        mlflow.log_metric("accuracy", acc)
        mlflow.log_metric("f1", f1)

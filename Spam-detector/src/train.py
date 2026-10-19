import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
import mlflow
import mlflow.sklearn

mlflow.set_tracking_uri("http://127.0.0.1:5000")

def main():
    train_df = pd.read_csv("data/processed/train.tsv", sep="\t")
    test_df = pd.read_csv("data/processed/test.tsv", sep="\t")

    train_df["label"] = train_df["label"].map({"ham":0, "spam":1})
    test_df["label"] = test_df["label"].map({"ham":0, "spam":1})

    X_train_raw = train_df["text"]
    y_train = train_df["label"]
    X_test_raw = test_df["text"]
    y_test = test_df["label"]

    tfidf = TfidfVectorizer(stop_words="english")
    X_train = tfidf.fit_transform(X_train_raw)
    X_test = tfidf.transform(X_test_raw)

    C = 1.0
    max_iter = 200

    with mlflow.start_run(run_name="spam_train"):

        mlflow.log_param("C", C)
        mlflow.log_param("max_iter", max_iter)

        model = LogisticRegression(C=C, max_iter=max_iter)
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        print(f"测试集准确率: {acc:.4f}")

        mlflow.log_metric("accuracy", acc)

        mlflow.sklearn.log_model(model, artifact_path="model")

if __name__ == "__main__":
    main()

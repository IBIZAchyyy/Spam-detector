"""训练脚本：TF-IDF + 逻辑回归，接入 MLflow（可选）。

用法：
    python -m ml.train                  # 跑基线实验
    $env:BASELINE="0"; python -m ml.train   # 跑改进实验（bigram + 调参）
"""

import os
import pickle
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

from ml.data_pipeline import clean_text, load_data

# mlflow 是可选依赖：装了就记录实验，没装就用 print 代替
try:
    import mlflow

    HAS_MLFLOW = True
except ImportError:
    HAS_MLFLOW = False

REGISTRY_DIR = Path(__file__).resolve().parent / "registry"
REGISTRY_DIR.mkdir(exist_ok=True)
MODEL_SAVE_PATH = REGISTRY_DIR / "spam_model.pkl"


def build_pipeline(use_bigram: bool, C: float) -> Pipeline:
    """构建 TF-IDF + 逻辑回归 pipeline。"""
    ngram_range = (1, 2) if use_bigram else (1, 1)
    return Pipeline(
        [
            ("tfidf", TfidfVectorizer(ngram_range=ngram_range, stop_words="english")),
            ("clf", LogisticRegression(C=C, max_iter=1000)),
        ]
    )


def main():
    df = load_data()
    df["cleaned"] = df["text"].apply(clean_text)

    X_train, X_test, y_train, y_test = train_test_split(
        df["cleaned"],
        df["label_num"],
        test_size=0.2,
        random_state=42,
        stratify=df["label_num"],
    )

    # 通过环境变量切换基线/改进实验
    use_bigram = os.getenv("BASELINE", "1") == "0"
    C = 10.0 if use_bigram else 1.0
    experiment_name = "improved_bigram" if use_bigram else "baseline_unigram"

    if HAS_MLFLOW:
        mlflow.set_experiment("spam-detector")
        mlflow.start_run(run_name=experiment_name).__enter__()

    model = build_pipeline(use_bigram=use_bigram, C=C)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)

    if HAS_MLFLOW:
        mlflow.log_param("ngram_range", "1,2" if use_bigram else "1,1")
        mlflow.log_param("C", C)
        mlflow.log_metric("accuracy", acc)
        mlflow.log_metric("f1", f1)
        mlflow.log_metric("precision", precision)
        mlflow.log_metric("recall", recall)

    # 保存模型到 registry 目录（供 API 加载）
    with open(MODEL_SAVE_PATH, "wb") as f:
        pickle.dump(model, f)

    if HAS_MLFLOW:
        mlflow.log_artifact(str(MODEL_SAVE_PATH))
        mlflow.end_run()

    print(
        f"[{experiment_name}] accuracy={acc:.4f}  f1={f1:.4f}  precision={precision:.4f}  recall={recall:.4f}"
    )
    print(f"模型已保存到: {MODEL_SAVE_PATH}")


if __name__ == "__main__":
    main()

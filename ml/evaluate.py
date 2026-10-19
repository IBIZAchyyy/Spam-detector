import json
import joblib
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from sklearn.model_selection import train_test_split

from ml.data_pipeline import clean_text, load_data


def main():
    # 加载训练好的模型
    model = joblib.load("ml/registry/spam_model.pkl")

    # 读取数据集（和train.py保持一致）
    df = load_data()
    df["cleaned"] = df["text"].apply(clean_text)

    # 拆分测试集（和train.py保持一致：80%训练，20%测试）
    _, X_test, _, y_test = train_test_split(
        df["cleaned"],
        df["label_num"],
        test_size=0.2,
        random_state=42,
        stratify=df["label_num"],
    )

    # 用模型做预测
    y_pred = model.predict(X_test)

    # 计算各项指标
    acc = accuracy_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    # 打印结果
    print(f"模型准确率: {acc:.4f}")
    print(f"模型召回率: {recall:.4f}")
    print(f"模型精确率: {precision:.4f}")
    print(f"模型F1: {f1:.4f}")

    # 保存为metrics.json
    metrics = {
        "accuracy": acc,
        "recall": recall,
        "precision": precision,
        "f1": f1
    }
    with open("ml/metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)


if __name__ == "__main__":
    main()

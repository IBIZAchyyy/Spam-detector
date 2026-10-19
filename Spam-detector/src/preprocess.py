import pandas as pd
import os
import mlflow

mlflow.set_tracking_uri("http://127.0.0.1:5000")

def main():
    data_path = "data/SMSSpamCollection"
    df = pd.read_csv(data_path, sep="\t", names=["label","text"])
    print("原始数据行数：", len(df))

    df = df.dropna()
    print("清洗后行数：", len(df))

    train_df = df.sample(frac=0.8, random_state=42)
    test_df = df.drop(train_df.index)

    os.makedirs("data/processed", exist_ok=True)
    train_df.to_csv("data/processed/train.tsv", sep="\t", index=False)
    test_df.to_csv("data/processed/test.tsv", sep="\t", index=False)

    print("数据处理完了")

if __name__ == "__main__":
    main()

import pandas as pd

df = pd.read_csv("data/SMSSpamCollection", sep="\t", names=["label","message"])
df["label"] = df["label"].replace({"ham":0, "spam":1})

train = df.sample(frac=0.8, random_state=42)
test = df.drop(train.index)

train.to_csv("data/train.csv", index=False)
test.to_csv("data/test.csv", index=False)
print("数据处理完了")


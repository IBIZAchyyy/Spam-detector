"""数据预处理：读取 SMS Spam Collection 数据集。"""
import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "spam.csv"


def load_data() -> pd.DataFrame:
    """加载 SMS Spam Collection 数据集。

    数据集格式：两列，第一列是标签（ham/spam），第二列是文本。
    可从 https://archive.ics.uci.edu/dataset/228/sms+spam+collection 下载，
    保存为 data/spam.csv，编码 latin-1。
    """
    df = pd.read_csv(DATA_PATH, sep="\t", header=None, names=["label", "text"], encoding="latin-1")
    # 标签转成数值：spam=1, ham=0
    df["label_num"] = (df["label"] == "spam").astype(int)
    return df


def clean_text(text: str) -> str:
    """简单清洗：去多余空格、转小写。"""
    return " ".join(text.split()).lower()

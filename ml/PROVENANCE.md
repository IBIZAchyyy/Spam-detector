# 数据血缘（Provenance）

本文件记录模型从数据到产物的完整血缘链。

## 当前生产模型

- 模型文件：`registry/spam_model.pkl`
- 训练数据集版本：data-v2
- 训练代码 commit：（待填）
- MLflow run ID：（待填）
- 训练时间：（待填）

## 血缘链

```
data/spam.csv (v2, DVC tracked)
    → ml/data_pipeline.py (clean_text, train_test_split)
    → ml/train.py (TF-IDF bigram + LogisticRegression)
    → MLflow run (记录参数/指标/产物)
    → ml/registry/spam_model.pkl
    → app/model.py (load_model)
    → app/main.py (/predict 接口)
```

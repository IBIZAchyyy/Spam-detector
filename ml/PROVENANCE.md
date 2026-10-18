# 数据血缘（Provenance）

本文件记录模型从数据到产物的完整血缘链。

## 当前生产模型

- 模型文件：`registry/spam_model.pkl`
- 训练数据集版本：data-v1（原始 SMS Spam Collection）
- 训练代码 commit：9bbb969
- 模型：TF-IDF bigram (1-2 gram) + LogisticRegression(C=10.0)
- 测试集准确率：98.03%
- F1 分数：0.9214
- MLflow run ID：暂未配置（待安装 MLflow 后补充）
- 训练时间：2026-10-18

## 血缘链

```
data/spam.csv (原始 SMS Spam Collection，5574 条短信)
    → ml/data_pipeline.py (clean_text 清洗, train_test_split 80/20 划分)
    → ml/train.py (TF-IDF bigram + LogisticRegression, C=10.0)
    → 模型评估: accuracy=98.03%, f1=0.9214
    → ml/registry/spam_model.pkl (序列化模型)
    → app/model.py (load_model 加载 pkl)
    → app/main.py (POST /predict 接口接收文本)
    → Docker 镜像 (spam-detector:prod)
```

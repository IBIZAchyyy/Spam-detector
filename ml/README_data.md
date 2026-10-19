# 数据说明（README_data）

## 数据来源

SMS Spam Collection Dataset（UCI Machine Learning Repository）
- 链接：https://archive.ics.uci.edu/dataset/228/sms+spam+collection
- 共 5574 条英文短信，标签为 ham（正常）/ spam（垃圾）
- 垃圾邮件占比约 13%，正常邮件约 87%，存在类别不均衡
- 下载后保存为 `data/spam.csv`，制表符分隔，两列：label、text

## 数据集版本

### v1（当前使用版本）
- 来源：原始 SMS Spam Collection，未做修改
- 样本数：5574 条
- 用途：训练当前生产模型（bigram TF-IDF + 逻辑回归 C=10.0）
- 对应模型测试集准确率：98.03%

### v2（当前使用版本）
- 相对 v1 做的改动：
  1. 去除重复短信（删除了 403 条重复样本）
- 样本数：5168 条
- 用途：更干净的训练数据，避免重复样本导致过拟合

## 数据版本对应关系

| 数据集版本 | DVC 版本标签 | 对应 git commit | 说明 |
|-----------|-------------|----------------|------|
| v1 | `data-v1` | eb356b6 | 原始数据 5571 条 |
| v2 | `data-v2` | 51feafe | 去重后 5168 条，当前生产模型使用 |

> 注意：原始数据不提交到 GitHub，后续通过 DVC + Azure Blob Storage 管理。

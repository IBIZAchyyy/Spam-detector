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

### v2（计划版本，待实现）
- 相对 v1 计划做的改动：
  1. 去除重复短信（数据集中约有 400 条重复样本）
  2. 统一文本编码、转小写、去除多余空格
  3. 过滤过短的无效样本（少于 3 个词）
- 用途：进一步提升模型召回率

## 数据版本对应关系

| 数据集版本 | DVC 版本标签 | 对应 git commit | 说明 |
|-----------|-------------|----------------|------|
| v1 | `data-v1` | 9bbb969 | 原始数据，当前生产模型使用 |
| v2 | `data-v2` | （待提交后填写） | 清洗去重后的数据 |

> 注意：原始数据不提交到 GitHub，后续通过 DVC + Azure Blob Storage 管理。

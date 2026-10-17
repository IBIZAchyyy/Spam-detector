# 数据说明（README_data）

## 数据来源

SMS Spam Collection Dataset（UCI Machine Learning Repository）
- 链接：https://archive.ics.uci.edu/dataset/228/sms+spam+collection
- 共 5574 条英文短信，标签为 ham（正常）/ spam（垃圾）
- 下载后保存为 `data/spam.csv`，制表符分隔，两列：label、text

## 数据集版本

### v1（初始版本）
- 来源：原始 SMS Spam Collection，未做修改
- 用途：训练基线模型（unigram TF-IDF + 逻辑回归）

### v2（改进版本）
- 相对 v1 的改动：
  1. 去除了重复短信（约 400 条重复样本）
  2. 统一了文本编码和大小写
  3. 过滤了过短的无效样本（< 3 个词）
- 用途：训练改进模型（bigram TF-IDF + 调参）

## 数据版本对应 commit

| 数据集版本 | DVC 版本标签 | 对应 git commit |
|-----------|-------------|----------------|
| v1 | `data-v1` | （待提交后填写） |
| v2 | `data-v2` | （待提交后填写） |

> 注意：原始数据不提交到 GitHub，通过 DVC 管理。

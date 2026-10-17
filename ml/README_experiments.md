# 实验记录说明（README_experiments）

## 实验列表

### 实验 1：基线模型（baseline_unigram）
- 特征：TF-IDF unigram（1-gram）
- 模型：LogisticRegression(C=1.0)
- 指标（测试集）：
  - Accuracy: （待填）
  - F1: （待填）
  - Precision: （待填）
  - Recall: （待填）

### 实验 2：改进模型（improved_bigram）
- 特征：TF-IDF bigram（1-2 gram）
- 模型：LogisticRegression(C=10.0)
- 指标（测试集）：
  - Accuracy: （待填）
  - F1: （待填）
  - Precision: （待填）
  - Recall: （待填）

## 推荐上生产的模型

选择 **实验 2（improved_bigram）**，因为 bigram 特征能捕捉 "free money"、"call now" 等短语模式，对垃圾邮件识别更有效。

## 优化指标说明

主要优化 **F1 分数**，原因：
- 垃圾邮件检测中两类样本不均衡（spam 约占 13%），accuracy 容易被多数类主导
- Precision 高意味着不误判正常邮件为垃圾（用户体验好）
- Recall 高意味着不漏掉真正的垃圾邮件
- F1 是两者的调和平均，更适合作为本任务的综合指标

# 实验记录说明（README_experiments）

## 实验列表

### 实验 1：基线模型（baseline_unigram）
- 特征：TF-IDF unigram（1-gram）
- 模型：LogisticRegression(C=1.0)
- 指标（测试集）：
  - Accuracy: 0.9677（96.77%）
  - F1: 0.8626
  - Precision: 1.0000
  - Recall: 0.7584

### 实验 2：改进模型（improved_bigram）
- 特征：TF-IDF bigram（1-2 gram）
- 模型：LogisticRegression(C=10.0)
- 指标（测试集）：
  - Accuracy: 0.9803（98.03%）
  - F1: 0.9214
  - Precision: 0.9847
  - Recall: 0.8658

## 推荐上生产的模型

选择 **实验 2（improved_bigram）**，原因：
- 相比基线，准确率从 96.77% 提升到 98.03%
- F1 从 0.86 提升到 0.92，综合性能更好
- bigram 特征能捕捉 "free money"、"call now"、"win free" 等短语模式，比单个词更能识别垃圾邮件
- 召回率从 0.76 提升到 0.87，能识别出更多真正的垃圾邮件

## 优化指标说明

主要优化 **F1 分数**，原因：
- 垃圾邮件检测中两类样本不均衡（spam 约占 13%），accuracy 容易被多数类（ham）主导
- Precision 高意味着不误判正常邮件为垃圾邮件（用户不会漏看重要邮件）
- Recall 高意味着不漏掉真正的垃圾邮件（用户不被骚扰）
- F1 是 Precision 和 Recall 的调和平均，更适合作为本任务的综合评价指标

# Spam Detector API

一个基于 TF-IDF + 逻辑回归的垃圾短信检测服务，使用 FastAPI 提供 REST 接口。

## 快速开始

```bash
pip install -r requirements.txt

# 训练模型（先跑基线，再跑改进）
python -m ml.train
$env:BASELINE="0"; python -m ml.train   # PowerShell 跑改进实验

# 启动服务
uvicorn app.main:app --reload
```

访问 http://localhost:8000/docs 查看 Swagger 文档。

## API 接口

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/health` | 健康检查 |
| POST | `/predict` | 输入文本，返回是否垃圾邮件 |

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "WINNER!! You won a FREE iPhone!"}'
# {"label":"spam","confidence":0.98}
```

## 项目结构

```
├── app/                # FastAPI 应用
│   ├── main.py         # 接口入口
│   └── model.py        # 模型加载与预测
├── ml/                 # 训练与 MLOps
│   ├── train.py        # 训练脚本（接 MLflow）
│   ├── data_pipeline.py
│   ├── configs/
│   ├── registry/        # 当前生产模型
│   ├── README_data.md
│   └── README_experiments.md
├── tests/              # pytest 测试
├── data.dvc            # DVC 数据指针
├── requirements.txt
├── Dockerfile
└── DEPLOYMENT.md
```

## 开发与部署流程

代码从提交到上线的完整路径：

```
feature/* → dev → staging → main
  ↓         ↓       ↓        ↓
PR到dev   CI检查  staging   生产镜像
自动CI    全绿    镜像构建   自动构建
```

| 分支 | 触发的流水线动作 |
|------|-----------------|
| `feature/*` 提 PR 到 `dev` | 自动跑：ruff 检查 → black 格式 → pytest 测试 → Docker 构建 |
| 合并到 `dev` | 同上，CI 失败禁止合并 |
| 合并到 `staging` | CI 全过后，自动用 STAGING_ENV 密钥生成 .env，构建 staging 镜像 |
| 合并到 `main` | CI 全过后，自动用 PROD_ENV 密钥生成 .env，构建生产镜像 |

详细说明见 [DEPLOYMENT.md](DEPLOYMENT.md)。

# 部署流程说明

## 分支模型

| 分支 | 用途 | 触发的流水线 |
|------|------|-------------|
| `feature/*` | 新功能开发 | 向 dev 提 PR 时触发 CI |
| `dev` | 开发集成分支 | PR 到 dev 时跑 CI |
| `staging` | 预发布环境 | 合并到 staging 后构建 staging 镜像 |
| `main` | 生产分支 | 合并到 main 后构建生产镜像 |

## CI 流水线（.github/workflows/ci.yml）

每次 PR 到 `dev` / `staging` / `main` 时自动执行：

1. 安装依赖
2. ruff 静态检查
3. black 格式检查
4. pytest 跑全部测试
5. docker build 构建镜像

**任何一步失败，PR 不允许合并。**

## 部署流程

### → staging 环境
合并到 `staging` 分支后：
- 使用 GitHub Secrets 中 staging 专用密钥生成 `.env`
- 构建 staging Docker 镜像
- （本项目不要求实际部署到服务器，只需构建成功）

### → 生产环境
合并到 `main` 分支后：
- 使用 GitHub Secrets 中 production 专用密钥生成 `.env`
- 构建生产 Docker 镜像
- （本项目不要求实际部署到服务器，只需构建成功）

## GitHub Secrets 需要配置

- `STAGING_ENV`：staging 环境的 .env 文件内容
- `PROD_ENV`：生产环境的 .env 文件内容

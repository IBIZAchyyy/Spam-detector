# run_all.ps1 - 一键跑通：下载数据 → 装依赖 → 两次训练实验 → 跑测试
# 用法：在项目根目录下  .\run_all.ps1

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $root

Write-Host "`n=== [1/5] 检查 Python ===" -ForegroundColor Cyan
python --version
if ($LASTEXITCODE -ne 0) { Write-Host "未找到 Python，请先安装 Python 3.11" -ForegroundColor Red; exit 1 }

Write-Host "`n=== [2/5] 安装依赖 ===" -ForegroundColor Cyan
pip install -r requirements.txt
if ($LASTEXITCODE -ne 0) { Write-Host "依赖安装失败" -ForegroundColor Red; exit 1 }

Write-Host "`n=== [3/5] 下载数据集 ===" -ForegroundColor Cyan
if (Test-Path "data\spam.csv") {
    Write-Host "data\spam.csv 已存在，跳过下载"
} else {
    $url = "https://archive.ics.uci.edu/static/public/228/sms+spam+collection.zip"
    $zip = "data\smsspamcollection.zip"
    try {
        Invoke-WebRequest -Uri $url -OutFile $zip -UseBasicParsing
        Expand-Archive -Path $zip -DestinationPath "data\" -Force
        # UCI 解压出来的文件名是 SMSSpamCollection（无后缀）
        if (Test-Path "data\SMSSpamCollection") {
            Move-Item "data\SMSSpamCollection" "data\spam.csv" -Force
        } elseif (Test-Path "data\SMSSpamCollection.txt") {
            Move-Item "data\SMSSpamCollection.txt" "data\spam.csv" -Force
        }
        Remove-Item $zip -ErrorAction SilentlyContinue
        Write-Host "数据集下载完成 → data\spam.csv"
    } catch {
        Write-Host "自动下载失败，请手动下载：" -ForegroundColor Yellow
        Write-Host "  1. 访问 https://archive.ics.uci.edu/dataset/228/sms+spam+collection"
        Write-Host "  2. 下载 sms+spam+collection.zip"
        Write-Host "  3. 解压后把 SMSSpamCollection 文件重命名为 spam.csv，放到 data\ 目录下"
        exit 1
    }
}

Write-Host "`n=== [4/5] 跑两次训练实验 ===" -ForegroundColor Cyan
Write-Host "--- 基线实验 (unigram, C=1.0) ---" -ForegroundColor Yellow
python -m ml.train
if ($LASTEXITCODE -ne 0) { Write-Host "基线训练失败" -ForegroundColor Red; exit 1 }

Write-Host "--- 改进实验 (bigram, C=10.0) ---" -ForegroundColor Yellow
$env:BASELINE = "0"
python -m ml.train
Remove-Item Env:\BASELINE
if ($LASTEXITCODE -ne 0) { Write-Host "改进训练失败" -ForegroundColor Red; exit 1 }

Write-Host "`n=== [5/5] 跑测试 ===" -ForegroundColor Cyan
pytest tests/ -v
if ($LASTEXITCODE -ne 0) { Write-Host "有测试失败" -ForegroundColor Red; exit 1 }

Write-Host "`n=== 全部完成！===" -ForegroundColor Green
Write-Host "模型已保存到 ml\registry\spam_model.pkl"
Write-Host "启动 API：uvicorn app.main:app --reload"
Write-Host "查看实验：mlflow ui"

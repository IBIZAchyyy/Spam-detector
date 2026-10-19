# 垃圾邮件检测项目
这是DevOps课程实践项目，利用机器学习做邮件垃圾识别，后端使用FastAPI提供预测接口。

## 项目文件结构
Spam-detector/
├── data
    train.csv      邮件样本数据
├── src
    train.py       模型训练代码
    app.py         web接口服务
├── models         保存训练出来的模型，不上传到github
├── test_api.py    接口自动化测试
├── requirements.txt  项目需要安装的包
├── .gitignore     不需要提交的文件配置

## 环境准备
安装依赖包
pip install -r requirements.txt

## 运行流程
1. 训练模型
python src/train.py

2. 启动web服务
python -m uvicorn src.app:app --host 127.0.0.1 --port 8000

3. 打开浏览器访问接口文档
http://127.0.0.1:8000/docs

## 自动化测试
保持uvicorn服务运行，新开终端执行
python test_api.py

测试案例：
1. 垃圾邮件：Win free cash! Send your bank account now. 预期输出1
2. 普通邮件：Hello, how are you today? 预期输出0

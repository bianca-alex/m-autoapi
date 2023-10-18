### 安装扩展
pip install -r requirements.txt
### 框架版本
python 3.9.16
### 框架说明
```
├── bootstrap.py // 运行设置
├── common  // 自定义方法
│   ├── __init__.py
│   └── settings.py
├── config // 配置
│   └── setting.ini
├── datas // 测试数据
│   └── module 
├── logs // log
├── main.py // 入口文件
├── reports // 报告生成
├── requirements.txt
├── tests // 测试用例
│   └── module
│       ├── conftest.py
│       ├── __init__.py
│       └── test_example.py
└── utils // 工具类
    ├── assertaction.py
    ├── db.py
    ├── http_client.py
    ├── __init__.py
    ├── loader_config.py
    ├── loader_data.py
    └── logger.py
```
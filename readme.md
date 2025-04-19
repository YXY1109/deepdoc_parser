### 安装虚拟环境

```
使用virtualenv创建虚拟环境，名称为：.venv。和uv的环境命名一致
可选操作：pip install uv 
初始化：uv init --python 3.11.11
安装依赖：uv add -r requirements.txt
查看包版本：pip install numpy==
安装单个依赖：uv add numpy==1.26.4
```

### ruff代码管理

```
isort：ruff check --select I --fix .
格式化：ruff format

检查：ruff check
```
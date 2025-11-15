# install uv
https://github.com/astral-sh/uv
## set system env path
XXX/uv.exe

# use
## init
```python
# 指定python版本
uv init -p 3.14

# use pip in venv
uv pip list 
uv pip tree
uv pip install 
uv pip uninstall
uv pip freeze > requirements.txt
uv pip install -r requirements.txt
uv run python xxx.py

# use pip instead of pip
uv tree
uv add pandas # 安装pandas包

# 执行该命令时，会自动修改pyproject.toml和uv.lock文件
uv add ruff --dev # 安装ruff，并且ruff仅用于开发环境，不会被打包

# 注意：删除时也要加--dev: uv remove ruff --dev
uv add pytest --dev # 包仅用于开发环境，不会被打包
uv add mock --dev # 包仅用于开发环境，不会被打包

# 执行该命令时，会自动修改pyproject.toml和uv.lock文件
uv remove pandas #卸载pandas包（会卸载pandas依赖的包，与pip不同）

# 可以这样在新环境安装指定包
uv add -r requirements.txt

>若使用uv pip install，则不会自动修改pyproject.toml和uv.lock文件，需要手动调用uv add，修改pyproject.toml和uv.lock文件
例：
uv pip install pandas # 安装了pandas包，但是没有修改pyproject.toml和uv.lock文件
uv add pandas # 手动修改pyproject.toml和uv.lock文件
# --upgrade-package表示将尝试将指定的包更新到最新的兼容版本，同时保持锁文件的其余部分不变
uv lock --upgrade-package requests
uv sync # 根据pyproject.toml和uv.lock文件内容自动安装依赖包 

# 安装到系统环境 uv tool
uv tool uninstall ruff #安装ruff工具，这个ruff是脱离工程环境独立运行的
uv tool list # 当前已安装工具的列表

# 打包到whl
uv build

```




```python
# 换源
# 本地虚拟环境
pyproject.toml
[tool.uv]
index-url = "https://pypi.tuna.tsinghua.edu.cn/simple/"

```
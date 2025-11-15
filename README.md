# uv_pytorch_cuda_test
just test

```python
# init
cd uv_pytorch_cuda_test
uv init -p 3.14

# windows system env path
# maybe not work
UV_DEFAULT_INDEX
# not test
UV_INDEX_URL
https://pypi.tuna.tsinghua.edu.cn/simple
# test
echo $env:UV_INDEX_URL # 输出应为：https://pypi.tuna.tsinghua.edu.cn/simple
# linux
echo 'export UV_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple' >> ~/.bashrc
source ~/.bashrc  # 立即生效
echo $UV_INDEX_URL # 输出应为：https://pypi.tuna.tsinghua.edu.cn/simple

# update pyproject.toml
[tool.uv]
index-url = "https://pypi.tuna.tsinghua.edu.cn/simple/"

# pytorch install, https://pytorch.org/get-started/locally/
# latest cu130+py3.14
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu130

# manually download
https://download.pytorch.org/whl/cu130/torch-2.9.1%2Bcu130-cp314-cp314-win_amd64.whl

# manually install
uv add ../../../下载/torch-2.9.1+cu130-cp314-cp314-win_amd64.whl

# run your code
uv run python .\test_torch.py
==================================================
PyTorch GPU验证工具
==================================================
1. 基础CUDA检查:
   CUDA可用: True

2. GPU详细信息:
   可用GPU数量: 1
   GPU 0: NVIDIA GeForce RTX 4060 Laptop GPU (显存: 8.00 GB)
   当前使用GPU: 0 - NVIDIA GeForce RTX 4060 Laptop GPU

3. 设备设置测试:
   自动选择设备: cuda

4. 张量操作测试:
   CPU张量创建成功: torch.Size([5000, 5000])
   张量设备位置: cuda:0

5. 计算性能测试:
   GPU计算时间: 0.0897秒
   CPU计算时间: 0.4296秒
   GPU加速比: 4.79x

6. 最终验证结果:
   ✅ PyTorch GPU配置成功！
   使用的GPU: NVIDIA GeForce RTX 4060 Laptop GPU
```
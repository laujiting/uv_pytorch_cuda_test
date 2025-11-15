import torch
import time

def validate_gpu():
    """
    验证PyTorch是否能正确调用GPU
    """
    print("=" * 50)
    print("PyTorch GPU验证工具")
    print("=" * 50)
    
    # 1. 基础CUDA可用性检查
    print("1. 基础CUDA检查:")
    cuda_available = torch.cuda.is_available()
    print(f"   CUDA可用: {cuda_available}")
    
    if not cuda_available:
        print("   ❌ 未检测到CUDA支持，请检查驱动和PyTorch安装")
        return False
    
    # 2. 详细GPU信息
    print("\n2. GPU详细信息:")
    device_count = torch.cuda.device_count()
    print(f"   可用GPU数量: {device_count}")
    
    for i in range(device_count):
        gpu_name = torch.cuda.get_device_name(i)
        gpu_memory = torch.cuda.get_device_properties(i).total_memory / 1024**3  # 转换为GB
        print(f"   GPU {i}: {gpu_name} (显存: {gpu_memory:.2f} GB)")
    
    # 3. 当前活动设备
    current_device = torch.cuda.current_device()
    print(f"   当前使用GPU: {current_device} - {torch.cuda.get_device_name(current_device)}")
    
    # 4. 设备设置测试
    print("\n3. 设备设置测试:")
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"   自动选择设备: {device}")
    
    # 5. 张量操作测试
    print("\n4. 张量操作测试:")
    
    # 创建测试张量
    cpu_tensor = torch.randn(5000, 5000)
    print(f"   CPU张量创建成功: {cpu_tensor.shape}")
    
    # 转移到GPU（如果可用）
    gpu_tensor = cpu_tensor.to(device)
    print(f"   张量设备位置: {gpu_tensor.device}")
    
    # 6. 计算性能对比
    print("\n5. 计算性能测试:")
    
    # GPU计算测试
    if device.type == 'cuda':
        start_time = time.time()
        # 执行矩阵乘法（GPU优势操作）
        result_gpu = gpu_tensor @ gpu_tensor.T
        torch.cuda.synchronize()  # 等待GPU计算完成
        gpu_time = time.time() - start_time
        print(f"   GPU计算时间: {gpu_time:.4f}秒")
        
        # CPU计算测试（将数据移回CPU）
        start_time = time.time()
        result_cpu = cpu_tensor @ cpu_tensor.T
        cpu_time = time.time() - start_time
        print(f"   CPU计算时间: {cpu_time:.4f}秒")
        
        # 性能提升比例
        if cpu_time > 0:
            speedup = cpu_time / gpu_time
            print(f"   GPU加速比: {speedup:.2f}x")
    
    # 7. 最终验证结果
    print("\n6. 最终验证结果:")
    if gpu_tensor.device.type == 'cuda':
        print("   ✅ PyTorch GPU配置成功！")
        print(f"   使用的GPU: {torch.cuda.get_device_name()}")
        return True
    else:
        print("   ❌ PyTorch无法使用GPU")
        return False

if __name__ == "__main__":
    # 执行验证
    success = validate_gpu()
    
    # 退出代码
    exit(0 if success else 1)


# ==================================================
# PyTorch GPU验证工具
# ==================================================
# 1. 基础CUDA检查:
#    CUDA可用: True

# 2. GPU详细信息:
#    可用GPU数量: 1
#    GPU 0: NVIDIA GeForce RTX 3080 (显存: 10.00 GB)
#    当前使用GPU: 0 - NVIDIA GeForce RTX 3080

# 3. 设备设置测试:
#    自动选择设备: cuda

# 4. 张量操作测试:
#    CPU张量创建成功: torch.Size([5000, 5000])
#    张量设备位置: cuda:0

# 5. 计算性能测试:
#    GPU计算时间: 0.1250秒
#    CPU计算时间: 1.8760秒
#    GPU加速比: 15.01x

# 6. 最终验证结果:
#    ✅ PyTorch GPU配置成功！
#    使用的GPU: NVIDIA GeForce RTX 3080
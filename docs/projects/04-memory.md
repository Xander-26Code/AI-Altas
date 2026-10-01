# 项目 04 · 权重与 KV Cache 显存账本

目标：在运行模型前做可核对的容量估算。源码 `examples/memory_budget.py` 只计算权重与 KV Cache，输出 GiB（2³⁰ 字节），不包含完整运行时开销。

```bash
python3 examples/memory_budget.py
python3 examples/memory_budget.py --weight-bits 4 --batch 4 --sequence 8192
```

采用简化公式：

```text
权重字节数 = 参数量 × 权重位数 / 8
KV 字节数 = 2 × 层数 × KV 头数 × 每头维度 × 上下文长度 × 并发数 × KV 每元素字节
```

默认假设 7B 参数、32 层、8 个 KV 头、每头 128 维、4,096 token、单序列、KV 每元素 2 字节。KV 结果为 0.5 GiB。这是假定结构的教学算例，不对应某个指定模型的实测。

## 验收

将上下文和并发分别翻倍，验证 KV Cache 线性变化；只改权重位数时，KV 不应自动缩小。列出没有计入的激活、临时 buffer、量化元数据、运行库和碎片，说明为何小计低于显卡容量仍不保证模型能运行。

有设备后记录模型配置和推理引擎，比较实测峰值与估算，解释差额；不要通过随意加固定百分比把公式包装成准确预测。

[项目目录](README.md) · [推理服务](../topics/19-inference-serving.md)

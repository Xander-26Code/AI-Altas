# 项目 03 · 看得见的因果 attention

目标：逐行理解 `softmax(QKᵀ / sqrt(d))V`。源码 `examples/attention.py` 仅实现单头注意力前向，没有位置编码、残差、训练或多头投影。

```bash
python3 examples/attention.py
```

输出为每个位置的加权结果和 attention 权重。因果 mask 让位置 i 只能读取不晚于 i 的键和值。softmax 先减去最大值，以减少数值溢出风险。

## 实验与验收

1. 手算第一行：它只能关注自己，权重应为 `[1,0,0]`。
2. 改变最后一个 token 的 K/V，验证前两个位置的输出不变。
3. 关闭 causal，观察原先不变的输出是否改变。
4. 把 query 全部置零，确认非 mask 区域的权重均匀。
5. 制造维度不匹配，检查实现能否明确报错。

完成后用 PyTorch 的相应运算重写，比较数值误差。再进入 [LLM](../topics/09-llm.md) 章节，将它放进训练循环。运行前向不等于完成 Transformer 或语言模型训练。

[项目目录](README.md)

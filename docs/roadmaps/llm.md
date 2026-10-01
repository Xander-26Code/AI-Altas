# 路线 D · LLM 原理、训练与对齐

先修：已经训练过小型神经网络，理解反向传播、交叉熵、PyTorch 张量与数据切分。规划 **450–800 小时**，每周 8–12 小时约 **9–24 个月**；大规模预训练及研究级复现不在此预算内。

| 阶段 | 内容 | 投入 | 产出 | 主资源与范围 |
|---|---|---|---|---|
| 模型结构 | [LLM](../topics/09-llm.md)，分词与 attention | 90–150 小时 | 因果 mask 与形状检查，解释 loss 与采样 | [LLMs from Scratch 中文版](https://skindhu.github.io/Build-A-Large-Language-Model-CN/) 第 1–4 章配 [作者代码](https://github.com/rasbt/LLMs-from-scratch)；另一中文路线选 [Happy-LLM](https://github.com/datawhalechina/happy-llm) 第 1–5 章相应部分 |
| 小规模预训练 | 数据流水线、小 Transformer、训练诊断 | 100–180 小时 | 训练/验证曲线、数据说明、检查点与可重跑配置 | [LLMs from Scratch 中文版](https://skindhu.github.io/Build-A-Large-Language-Model-CN/) 第 5 章配作者代码；也可选 Happy-LLM 第 5–6 章的小模型实践 |
| SFT 与 PEFT | [微调对齐](../topics/14-finetuning-alignment.md) 前半 | 100–180 小时 | 底座与适配器对照，未见任务和退化分析 | [smol course](https://github.com/huggingface/smol-course) Instruction Tuning → PEFT Quicktour/LoRA；[LLMs from Scratch 中文版](https://skindhu.github.io/Build-A-Large-Language-Model-CN/) 第 6–7 章与附录 E 作补充 |
| 偏好与评估 | 偏好优化选读、[评估](../topics/15-evaluation-safety.md) | 80–150 小时 | 说明数据偏好、奖励与真正任务效果的差别 | [smol course](https://github.com/huggingface/smol-course) Evaluation → Preference Alignment；对照 DPO 原论文与 TRL 文档 |
| 推理与报告 | [推理服务](../topics/19-inference-serving.md) 选读 | 80–140 小时 | 质量、显存、延迟与限制报告 | [KV cache 实现](https://github.com/rasbt/LLMs-from-scratch/tree/main/ch04/03_kv-cache) → vLLM Quickstart 与 Benchmark CLI；保存质量与延迟报告 |

## 先理解，再扩大模型

第一步运行 [attention 实验](../projects/03-attention.md)，改变未来 token，验证过去位置的结果不变。之后选一个教学规模模型：能快速重跑，比模型名字是否热门更重要。

做 [微调项目](../projects/05-finetuning.md) 时，先收集失败类型再决定是否微调。数据格式或领域术语问题、外部知识更新问题、工具流程问题可能需要不同方法。没有 GPU 可完成数据治理、损失推导和评测脚手架，GPU 训练作为单独阶段安排，不能把纸面实验当成训练已完成。

想继续扩大训练规模时，转 [分布式训练](../topics/18-distributed-training.md)，先做好状态和通信账本。

[全部路线](README.md) · [科研路线](research.md)

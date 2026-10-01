# 14 · 微调、后训练与对齐

> 目标：判断一个问题是否值得微调，完成可复现的小规模 SFT 对照，并解释 LoRA、RLHF、DPO 与 GRPO 的目标和区别。
> 先修：语言模型训练、PyTorch、梯度与交叉熵；理解强化学习的策略和奖励有助于后半章。建议规划 120–220 小时。这是完成先修后系统学习主教材、练习和一个项目的规划预算，不含补先修，不等于掌握整个领域。

## 资源列表

阅读资料免费；GPU、存储和生成训练样本的服务费另计。先做小实验估算显存与吞吐，不套用别人的硬件结论。核实日期：2026-09-30。

| 资源 | 语言 / 级别 | 费用 / 算力 | 为什么推荐、读哪部分 |
| --- | --- | --- | --- |
| [Hugging Face PEFT](https://huggingface.co/docs/peft/index) | 英文 / 进阶 | 免费 / GPU | 先读Quicktour、LoRA和checkpoint格式；检查真正参与训练的参数和底座依赖。 |
| [Hugging Face TRL](https://huggingface.co/docs/trl/index) | 英文 / 进阶 | 免费 / GPU | 按Dataset Formats→Chat Templates→SFT→DPO/GRPO阅读，固定库版本再运行示例。 |
| [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685) | 英文 / 进阶 | 免费 / 无 | 读低秩参数化、目标层与实验，手算adapter参数量；不要把节省比例当所有模型的常量。 |
| [QLoRA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/abs/2305.14314) | 英文 / 研究 | 免费 / 无 | 读量化底座、NF4与adapter训练；区分存储、计算精度和显存峰值。 |
| [Training Language Models to Follow Instructions with Human Feedback](https://arxiv.org/abs/2203.02155) | 英文 / 进阶 | 免费 / 无 | 读SFT→偏好标注→RLHF流程与局限；理解优化人类偏好和绝对正确并非同义。 |
| [Direct Preference Optimization](https://arxiv.org/abs/2305.18290) | 英文 / 研究 | 免费 / 无 | 读第3–4节和推导附录，写出优选/劣选相对参考策略的损失；先验证玩具例子梯度方向。 |
| [DeepSeekMath](https://arxiv.org/abs/2402.03300) | 英文 / 研究 | 免费 / 无 | 重点读GRPO与奖励设计，同时检查数据筛选；不要把数学任务结果直接外推所有领域。 |

### 补充课程与实作资源

| 资源 | 语言 · 难度 | 获取 · 算力 | 用法与阅读范围 |
|---|---|---|---|
| [Raschka · LLMs from Scratch 配套代码](https://github.com/rasbt/LLMs-from-scratch) | 英文 · 进阶 | 部分免费 · 可选GPU | 第 2–5 章做分词、attention、GPT 与预训练；第 6–7 章和附录 E 做微调。代码免费，完整书籍另售。 |
| [Datawhale · Happy-LLM](https://github.com/datawhalechina/happy-llm) | 中文 · 进阶 | 免费 · 可选GPU | 中文主线；第 1–4 章入门，第 5–6 章搭建与训练；按章节硬件要求缩小模型。 |
| [Hugging Face · smol course](https://github.com/huggingface/smol-course) | 英文 · 进阶 | 免费 · GPU | 沿 Instruction Tuning → Evaluation → Preference Alignment 学；先完成小模型 SFT 与评估，再选 DPO。 |

以上新增入口核实于 2026-10-01；资料免费不含硬件与 API 费用。

## 按资源安排学习顺序

小模型实践选 smol course；原理配 LoRA、DPO 论文，中文可配 Happy-LLM 第 6 章。先完成 SFT 评估，再尝试偏好训练。

按顺序完成主线，每步完成右列产出后再推进；选修不计入必做清单。页首时长包含所选主线、练习与本页项目，不包含把全部资料逐一学完。

| 阶段 | 使用资源 | 阅读 / 练习范围 | 完成后应留下什么 |
|---|---|---|---|
| 1 · SFT 与数据 | [Hugging Face · smol course](https://github.com/huggingface/smol-course)；[Hugging Face TRL](https://huggingface.co/docs/trl/index)；[Datawhale · Happy-LLM](https://github.com/datawhalechina/happy-llm) | Instruction Tuning；TRL Dataset Formats、Chat Templates、SFT | 检查数据模板，保存底座与微调模型对照 |
| 2 · 参数高效训练 | [Hugging Face PEFT](https://huggingface.co/docs/peft/index)；[LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)；[Raschka · LLMs from Scratch 配套代码](https://github.com/rasbt/LLMs-from-scratch) | PEFT Quicktour/LoRA；LoRA 论文；Raschka 附录 E | 核对可训练参数、适配器保存与加载 |
| 3 · 独立评估 | [Hugging Face · smol course](https://github.com/huggingface/smol-course) | Evaluation 单元与自建未见任务 | 记录提升、退化与重复数据检查 |
| 4 · 偏好训练 | [Direct Preference Optimization](https://arxiv.org/abs/2305.18290)；[Hugging Face TRL](https://huggingface.co/docs/trl/index)；[Hugging Face · smol course](https://github.com/huggingface/smol-course) | Preference Alignment 与 TRL DPO；先用小数据验证 | 核对优选/劣选方向并与 SFT 比较 |
| 选修 · 扩展方法 | [QLoRA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/abs/2305.14314)；[Training Language Models to Follow Instructions with Human Feedback](https://arxiv.org/abs/2203.02155)；[DeepSeekMath](https://arxiv.org/abs/2402.03300) | QLoRA、InstructGPT 或 DeepSeekMath 按目标选读 | 明确量化、奖励、参考策略与数据前提 |

## 实践：让小模型学会稳定输出工单标签

构造 300 条不含真实个人信息的训练样本、50 条开发样本与 50 条测试样本。按模板来源或主题切分，确保同一问题的改写不跨集合。保留三种类别与“不足以判断”选项。先测底座零样本与少样本提示，保存原始输出。

选择可在现有硬件运行、许可允许训练的较小模型，固定模型修订与 tokenizer，使用 LoRA 做 SFT。先打印 3 条解码后的输入、标签和 mask，确认学习对象；用极小 batch 做过拟合检查。随后记录学习率、rank、目标层、序列长度、有效 batch、优化步数、随机种子与峰值显存。

对比“零样本底座、少样本底座、LoRA 模型”三个版本的分类正确率、宏平均 F1、格式通过率和延迟。另准备 20 条无关普通问题检查退化。不要因为训练损失持续降低就选择最后一个 checkpoint，应依据开发集作选择，最后只在测试集报告一次。

**CPU 替代路线**：用几十个参数的玩具策略实现 SFT 和 DPO 损失，给出一次梯度更新前后优选/劣选概率变化；完成同样的数据切分和评估报告。它证明你理解目标函数，不应标成“大模型微调已完成”。

**验收标准**：可从配置重建 adapter；留出集没有重复或同模板泄漏；报告相对少样本基线的收益及退化；展示 5 个失败案例；无法改善时明确结论，不能隐去负结果。进阶偏好实验先手工标 100 对回答，并统计标注分歧，再决定是否投入 DPO / GRPO。

## 常见误区

- **“LoRA 本身就是一种对齐目标。”** 它规定哪些参数怎样更新，可与不同训练目标组合。
- **“量化到 4 bit 就意味着所有计算都用 4 bit。”** 存储、计算、梯度与优化器状态可能采用不同精度。
- **“训练后更爱回答，就是更可靠。”** 可能同时更自信地出错，必须测无答案和拒答情形。
- **“奖励提升就代表用户体验提升。”** 奖励投机、长度偏好、格式刷分都需要独立检查。

## 下一步

进入 [评估与安全](15-evaluation-safety.md)，把数据、模型、adapter 和评估配置一起版本化；若事实更新仍困难，结合 [RAG](12-rag.md)。

[返回知识地图](../map.md) · [选择学习路线](../roadmaps/README.md)

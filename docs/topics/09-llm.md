# 09 · 大语言模型

> 目标：从 token 到下一词概率，能解释并实现一个小型自回归 Transformer；知道模型规模、训练目标与真实能力之间的区别。
> 先修：Python、PyTorch 张量、线性代数、概率、反向传播。建议规划 120–220 小时。这是完成先修后系统学习主教材、练习和一个项目的规划预算，不含补先修，不等于掌握整个领域。

## 资源列表

以下“免费”指阅读资料；GPU 费用、模型下载许可另行确认。“无”表示读论文无需算力，复现大型实验通常需要 GPU。核实日期：2026-09-30。

| 资源 | 语言 / 级别 | 费用 / 算力 | 为什么推荐、读哪部分 |
| --- | --- | --- | --- |
| [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1) | 中英 / 入门 | 免费 / 可选GPU | 先读第1–3章与第6章；把架构、训练和分词连起来，后续按需读数据与微调章节。 |
| [Stanford CS336: Language Modeling from Scratch (2025)](https://cs336.stanford.edu/spring2025/) | 英文 / 进阶 | 免费 / GPU | 先做Assignment 1并读架构与MoE讲义；适合愿意自己实现组件的学习者，完整课程另有系统与数据作业。 |
| [Attention Is All You Need](https://arxiv.org/abs/1706.03762) | 英文 / 进阶 | 免费 / 无 | 读模型结构与attention部分，手算一次Q/K/V维度；理解原始encoder-decoder而非假设所有LLM都相同。 |
| [RoFormer: Enhanced Transformer with Rotary Position Embedding](https://arxiv.org/abs/2104.09864) | 英文 / 研究 | 免费 / 无 | 读RoPE构造和相对位置性质；先推导二维旋转内积，再看扩展性质。 |
| [Switch Transformers](https://arxiv.org/abs/2101.03961) | 英文 / 研究 | 免费 / 无 | 读稀疏专家路由、负载均衡与训练稳定性；用于区分总参数与激活计算量。 |
| [SentencePiece](https://github.com/google/sentencepiece) | 英文 / 进阶 | 免费 / CPU | 读Quick Start和分词算法说明，训练小词表并观察BPE/Unigram、Unicode与特殊token。 |
| [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) | 英文 / 入门 | 免费 / 无 | 先看张量流向、自注意力和多头图解，再回到原论文；用自己的例子复述，不把图解当严格证明。 |

### 补充课程与实作资源

| 资源 | 语言 · 难度 | 获取 · 算力 | 用法与阅读范围 |
|---|---|---|---|
| [Karpathy · Neural Networks: Zero to Hero](https://github.com/karpathy/nn-zero-to-hero) | 英文 · 入门 | 免费 · 可选GPU | 视频与 notebook 配套；深度学习先做 micrograd、makemore，再学 GPT 与 tokenizer。 |
| [Build a Large Language Model (From Scratch) · 社区中文版](https://skindhu.github.io/Build-A-Large-Language-Model-CN/) | 中文 · 进阶 | 免费在线阅读 · 可选GPU | skindhu 社区翻译；第 1–5 章学习分词、attention、GPT 与预训练，第 6–7 章及附录 E 学习微调和 LoRA。配合作者代码逐章实践。 |
| [Raschka · LLMs from Scratch 配套代码](https://github.com/rasbt/LLMs-from-scratch) | 英文 · 进阶 | 部分免费 · 可选GPU | 第 2–5 章做分词、attention、GPT 与预训练；第 6–7 章和附录 E 做微调。代码免费，完整书籍另售。 |
| [Datawhale · Happy-LLM](https://github.com/datawhalechina/happy-llm) | 中文 · 进阶 | 免费 · 可选GPU | 中文主线；第 1–4 章入门，第 5–6 章搭建与训练；按章节硬件要求缩小模型。 |
| [LLMs from Scratch · KV Cache 实现](https://github.com/rasbt/LLMs-from-scratch/tree/main/ch04/03_kv-cache) | 英文 · 进阶 | 免费 · CPU | 先看目录说明和基础缓存实现，再对照无缓存版本；比较生成一致性与解码耗时。 |

以上新增入口核实于 2026-10-01；资料免费不含硬件与 API 费用。

## 按资源安排学习顺序

从零实现主线可选本书社区中文版，配合 Raschka 官方代码逐章实践；已有英文书的读者可直接对照代码。Happy-LLM 是另一条中文路线，视频可用 Zero to Hero 补充，按需要选择。

按顺序完成主线，每步完成右列产出后再推进；选修不计入必做清单。页首时长包含所选主线、练习与本页项目，不包含把全部资料逐一学完。

| 阶段 | 使用资源 | 阅读 / 练习范围 | 完成后应留下什么 |
|---|---|---|---|
| 1 · 模型与分词 | [LLMs from Scratch 中文版](https://skindhu.github.io/Build-A-Large-Language-Model-CN/)；[Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1)；[Datawhale · Happy-LLM](https://github.com/datawhalechina/happy-llm)；[SentencePiece](https://github.com/google/sentencepiece) | 本书第 1–2 章；HF 第 1–3、6 章；另选中文路线可读 Happy-LLM 第 1–4 章；SentencePiece Quick Start | 比较分词结果，构造输入和下一词标签 |
| 2 · Attention 到 GPT | [LLMs from Scratch 中文版](https://skindhu.github.io/Build-A-Large-Language-Model-CN/)；[Raschka · LLMs from Scratch 配套代码](https://github.com/rasbt/LLMs-from-scratch)；[Karpathy · Neural Networks: Zero to Hero](https://github.com/karpathy/nn-zero-to-hero)；[The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)；[Attention Is All You Need](https://arxiv.org/abs/1706.03762) | 本书第 3–4 章配 Raschka 代码，或 Zero to Hero GPT 课；图解与原论文查结构 | 画张量维度，完成因果遮罩测试 |
| 3 · 小规模训练 | [LLMs from Scratch 中文版](https://skindhu.github.io/Build-A-Large-Language-Model-CN/)；[Raschka · LLMs from Scratch 配套代码](https://github.com/rasbt/LLMs-from-scratch)；[Datawhale · Happy-LLM](https://github.com/datawhalechina/happy-llm) | 本书第 5 章配 Raschka 代码，或 Happy-LLM 第 5–6 章 | 训练小模型并保存损失、采样与失败记录 |
| 4 · 生成与缓存 | [LLMs from Scratch · KV Cache 实现](https://github.com/rasbt/LLMs-from-scratch/tree/main/ch04/03_kv-cache) | 基础 KV cache 实现与无缓存对照 | 核对输出和逐 token 计时 |
| 选修 · 系统与架构 | [Stanford CS336: Language Modeling from Scratch (2025)](https://cs336.stanford.edu/spring2025/)；[RoFormer: Enhanced Transformer with Rotary Position Embedding](https://arxiv.org/abs/2104.09864)；[Switch Transformers](https://arxiv.org/abs/2101.03961) | CS336 Assignment 1；RoPE 与 MoE 论文按兴趣选读 | 主线完成后再加一个架构对照 |

## 实践：训练一个能被你解释的小语言模型

**交付物**：一个 notebook 或脚本、一份训练配置、一张损失曲线、一份失败样本报告。可以用自己写的短文本，不要把私密聊天记录当作默认语料。

1. 收集约 100–500 KB 自写或许可明确的文本，按文档分训练/验证集。先做字符级 tokenizer；记录字符数、词表大小和未知字符策略。
2. 用两层、短上下文的小 Transformer 建立基线。先让模型过拟合一个极小 batch，确认损失确实下降，再正式训练。
3. 增加 BPE 版本，保持数据切分一致，比较 token 长度、训练步数与生成样例。不要将两个 tokenizer 的困惑度直接当作公平比较。
4. 使用固定的 10 条提示，比较 greedy 和两组 temperature。记录重复、事实错误、截断和乱码，不挑选唯一好看的样例。
5. CPU 路线只训练字符级小模型并缩短序列；GPU 路线再比较有无 KV cache 的逐 token 延迟。明确计时是否包含加载和预热。

**验收标准**：tokenize→decode 对目标输入可逆；attention 的未来遮罩通过扰动检查；训练与验证集无文档重复；报告模型参数量、有效 batch、随机种子和硬件；解释至少 3 个失败例子。生成像人话不是本章唯一成功条件，能定位实现错误才是核心。

## 常见误区

- **“预测下一个 token，所以只能背诵。”** 训练目标说明优化形式，不直接给出能力上界；是否泛化需要留出任务验证。
- **“attention 图就是解释。”** 权重可作诊断线索，不能自动证明因果关系。
- **“参数更多，适合所有任务。”** 数据、架构、后训练、延迟、内存和任务分布都影响选择。
- **“一篇论文里的提升等于普遍规律。”** 检查基线、数据和计算预算，尤其不要沿用论文发表时的“最先进”说法。

## 下一步

想理解图像、语音与视频，读 [生成模型与多模态](10-generative-multimodal.md)；想做产品，直接进入 [AI 应用开发](11-ai-applications.md)；想改变模型行为，继续 [微调与对齐](14-finetuning-alignment.md)。

[返回知识地图](../map.md) · [选择学习路线](../roadmaps/README.md)

# 06 · 自然语言处理：从文本到语义任务

> 目标：理解文本表示、分词、语言建模与常见任务，建立一个有基线和错误分析的 NLP 项目。先修：[机器学习](04-machine-learning.md)、[深度学习](05-deep-learning.md)。**规划预算：80–160 小时**，用于完成先修后系统学习主教材、做练习并完成一个项目；不含补先修，不是掌握整个领域的承诺。传统方法可用 CPU，微调小模型可选 GPU。

## 资源列表

CS224N 当前年度部分视频需要校内登录，公开讲义与官网指向的往年视频可用于自学。SLP 是持续修订草稿，按章节标题定位比固定页码可靠。

- **[Stanford CS224N](https://web.stanford.edu/class/cs224n/)**｜英文 · 进阶 · 部分免费 · 可选GPU。系统学神经 NLP；从词向量、反向传播、注意力到模型评估，选公开讲义与往年视频。
- **[Speech and Language Processing](https://web.stanford.edu/~jurafsky/slp3/)**｜英文 · 进阶 · 免费 · 无。补文本与语言任务；读 Words and Tokens、N-grams、分类、Embeddings 和 Transformers。
- **[Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1)**｜英文 · 进阶 · 免费 · 可选GPU。连接 NLP 理论与库；学 1–4 章模型流程及 5–8 章数据、分词器和任务。
- **[SentencePiece](https://github.com/google/sentencepiece)**｜英文 · 进阶 · 免费 · CPU。理解子词与语言无关预处理；读分词、反分词、BPE/Unigram 与模型文件说明。
- **[spaCy Linguistic Features](https://spacy.io/usage/linguistic-features)**｜英文 · 进阶 · 免费 · CPU。认识结构化 NLP；选 tokenization、词性、依存和命名实体识别示例。
- **[Natural Language Processing with Python](https://www.nltk.org/book/)**｜英文 · 入门 · 免费 · CPU。练语料、文本处理和传统分类；读第 1–3、6–7 章，跳过不相关语法细节。

### 补充课程与实作资源

| 资源 | 语言 · 难度 | 获取 · 算力 | 用法与阅读范围 |
|---|---|---|---|
| [Datawhale · Happy-LLM](https://github.com/datawhalechina/happy-llm) | 中文 · 进阶 | 免费 · 可选GPU | 中文主线；第 1–4 章入门，第 5–6 章搭建与训练；按章节硬件要求缩小模型。 |

以上新增入口核实于 2026-10-01；资料免费不含硬件与 API 费用。

## 按资源安排学习顺序

CS224N 或 SLP 作为主线；中文起步可先读 Happy-LLM 第 1–3 章，再进入同一实践路径。

按顺序完成主线，每步完成右列产出后再推进；选修不计入必做清单。页首时长包含所选主线、练习与本页项目，不包含把全部资料逐一学完。

| 阶段 | 使用资源 | 阅读 / 练习范围 | 完成后应留下什么 |
|---|---|---|---|
| 1 · 文本任务 | [Speech and Language Processing](https://web.stanford.edu/~jurafsky/slp3/)；[Natural Language Processing with Python](https://www.nltk.org/book/)；[Datawhale · Happy-LLM](https://github.com/datawhalechina/happy-llm) | SLP 分词、N-gram、分类；或 NLTK 第 1–3、6 章 | 做词袋文本分类基线并记录错误类别 |
| 2 · 神经 NLP | [Stanford CS224N](https://web.stanford.edu/class/cs224n/) | 词向量、神经网络、注意力相关讲义与公开作业 | 比较词袋与一种神经表示 |
| 3 · 预训练模型 | [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1) | 第 1–4 章，再读数据与分词器相关章节 | 对小型文本任务做微调与独立评估 |
| 选修 · 结构化任务 | [SentencePiece](https://github.com/google/sentencepiece)；[spaCy Linguistic Features](https://spacy.io/usage/linguistic-features) | SentencePiece 分词；spaCy 实体与依存例子 | 选择分词器对照或实体识别之一 |

## 实践任务与验收

做一个文本分类项目：先建立 TF-IDF + 线性模型，再选一个适合目标语言的小型预训练模型比较。数据必须有来源和许可记录，清洗和词表只从训练部分确定。

- [ ] 写清标签定义，抽查有歧义样本并形成标注说明。
- [ ] 去重后切分，检查近重复、同作者或同来源内容是否造成泄漏。
- [ ] 保存 tokenizer、模型、最大长度、截断策略和标签映射。
- [ ] 在相同测试集上比较 macro-F1、各类表现、推理时间和资源占用。
- [ ] 整理至少 30 个错误样本，按否定、反讽、领域词、长度、标注问题分类。
- [ ] 建立至少 15 组成对扰动例子，记录改变大小写、标点、否定或拼写后的行为。
- [ ] 说明复杂模型带来的收益是否值得其延迟和成本；允许基线胜出。

进阶可转实体抽取：分别评价实体类型和完整边界，不要把大量“非实体”词元的准确率当成系统质量。

## 常见误区

- **预训练模型懂所有中文领域。** 领域、方言、术语与文本来源差异都需要验证。
- **删除所有标点就是清洗。** 标点、大小写和格式可能携带标签或任务所需含义。
- **注意力热力图就是完整解释。** 它反映部分中间计算，不自动等于因果贡献。
- **BLEU/ROUGE 高就保证生成事实正确。** 文本重叠与事实可靠性是不同维度。

下一步：回到 [深度学习](05-deep-learning.md) 补注意力和训练基础，或在[知识地图](../map.md)中选择大模型、检索与应用工程方向。

---

资源核实：2026-09-30；已审阅推荐入口的介绍、目录或相关正文，未声明逐课完成或逐项运行。算力为本页练习建议，详见[核实记录](../research/foundations-sources.md)。

[返回知识地图](../map.md) · [选择学习路线](../roadmaps/README.md)


# 模型与应用专题：研究来源与编排依据

本记录支撑知识地图的 09–15 章。网页核实于 2026-09-30 开始的研究批次完成；学习预算与交付检查于 2026-10-01 更新。正文为原创编排与讲解，没有复制第三方课程目录作为本项目正文，也没有收录下载搬运的书籍或课程。

## 先看现有路线怎样组织知识

| 路线 | 实际检查的材料与结构 | 可借鉴之处 | 本项目的编排判断 |
| --- | --- | --- | --- |
| [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1) | 官方导言、先修要求与章节目录；从Transformer与工具使用进入分词、数据、任务，再进入微调和推理训练。 | 同一生态贯穿概念与代码，适合把阅读转成实验；有中文译本入口。 | 将分词、架构与小模型放在09章，把数据和后训练分开，降低首次学习的概念负担。中文译本更新程度应以具体章节为准。 |
| [mlabonne/llm-course](https://github.com/mlabonne/llm-course) | 作者README中Fundamentals、Scientist、Engineer三类路线，以及作者notebook目录。 | 按学习者角色区分基础、模型研究和应用工程；选题与实践连接紧密。 | 采用“共同基础后分流”的原则，重新组织成模型、应用、RAG、agent、后训练与评估七个主题；不把所有外链连续读完视为毕业要求。 |
| [Full Stack LLM Bootcamp](https://fullstackdeeplearning.com/llm-bootcamp/) | 官方页面与2023课程目录；包含prompt、增强模型、askFSDL、UX与LLMOps。 | 产品交互、运维和项目案例与模型概念并列，提醒学习者关注任务完成。 | 应用章加入失败状态、结构契约、观测和成本；历史接口与当年模型能力不直接复用为当前事实。官网也提示工具已经变化。 |
| [Microsoft Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners) | 官方README，Learn/Build标签、章节目录、Python/TypeScript示例和中文翻译入口。 | 概念课与建设任务交替，主题包括聊天、检索、工具、安全、UX与生命周期。 | 每章同时提供学习顺序、概念解释、实践交付物和验收标准；示例尽量不依赖某家付费云服务。 |

上表是结构分析，不是课程完整修读证明。没有使用star数量作为教学质量证据，也不承诺复制一种结构即可获得同样关注。

## 本组内容怎样从资料变成可学习的路线

1. **理论与工程分清对象。** Transformer是网络架构，diffusion/flow是生成建模路线；LoRA是参数更新方式，SFT/DPO是训练目标；MCP是连接协议，agent是运行与决策方式。避免把名字并列成没有层次的技术名词表。
2. **每章有可观测结果。** 小语言模型检查遮罩与损失；RAG保留检索候选与证据ID；agent检查最终环境状态；微调同时报告少样本基线；评估报告分组结果与限制。
3. **提供低算力入口。** CPU路线包括分词、形状检查、二维flow、模拟模型、关键词检索、模拟agent和玩具损失。它们用于掌握原理，不包装成大模型训练完成。
4. **安全与评估贯穿链路。** 文档权限、缓存隔离、工具授权、输出校验、数据切分和回滚均给出具体落点；最后一章统一建立评估方法。
5. **不追逐易过期的排名与价格。** 原论文保留方法背景，不重复“当前最先进”的宣传；接口实现以安装版本对应文档为准。

## 时间预算的解释

09大语言模型为120–220小时；10生成模型与多模态为100–200小时；11应用与12RAG各80–140小时；13Agents为80–160小时；14微调与对齐为120–220小时；15评估与安全为80–140小时。

这些是完成先修后系统学习主教材、练习和一个项目的规划预算，不含补先修，不等于掌握整个领域。它们不是课程官方学时、实测完课时长或能力保证。基础、语言阅读速度、实验失败和项目规模都会改变实际投入；研究级论文复现和生产部署通常还需额外周期。单个小练习没有武断的“几小时掌握”限制。

## 资源元数据与核实边界

- 本组资源库为 [resources-models.json](../assets/data/resources-models.json)，共50条唯一URL：5项课程、23篇论文、5项项目、17项文档。
- `content-reviewed` 在本组表示已用网页工具实际打开来源并审阅其摘要、导言、目录或相关正文；不表示通读所有章节、验证所有实验结论或运行了全部代码。每条 `evidence` 写明实际检查范围。
- `checked_on` 保留来源核实批次日期2026-09-30。HTTP可达性与内容适用性是不同检查，未来可达不代表说明仍兼容最新版本。
- `access=免费` 表示列出的阅读材料可免费访问，不表示API、云GPU、数据库托管、证书或模型商业使用免费。
- `compute=无` 用于论文阅读；`CPU` 表示本章对应的轻量工程练习可在CPU做；`可选GPU` 表示可加速；`GPU` 表示推荐的实操路线通常需要GPU。不同模型和任务不能共用一个固定显存承诺。
- `language=中英` 表示核实了中文翻译入口与英文原文，并不保证每章翻译同步。作者教程通常保留英文，中文正文提供阅读重点。
- 核实存在重定向的包括Stanford CS336归档、Sentence Transformers示例、Pydantic文档和MCP版本入口；资源说明不掩盖这些变化。

**未据此下结论的页面**：[HELM动态首页](https://crfm.stanford.edu/helm/latest/) 与 [MITRE ATLAS首页](https://atlas.mitre.org/) 本次网页提取没有正文。HELM推荐改为有可读摘要的原论文；ATLAS没有计入这50条资源。空正文不能推断网站不存在，也不能标记为已审阅其内容。

## 逐条核实记录

以下说明与JSON一致。文章正文给出了每项资源的阅读重点与推荐原因，读者可从对应专题进入。

| ID | 来源 | 实际核实范围 |
| --- | --- | --- |
| model-001 | [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1) | 已打开官方课程导言，核对章节目录、Python先修、免费声明及中文翻译入口。 |
| model-002 | [Stanford CS336: Language Modeling from Scratch (2025)](https://cs336.stanford.edu/spring2025/) | 已打开课程归档，核对先修、五项作业和课程日程；页面明确建议CPU调试、GPU完成训练。 |
| model-003 | [Attention Is All You Need](https://arxiv.org/abs/1706.03762) | 已打开arXiv作者论文页，核对标题、作者和Transformer架构摘要；不是对全部实验的复现。 |
| model-004 | [RoFormer: Enhanced Transformer with Rotary Position Embedding](https://arxiv.org/abs/2104.09864) | 已打开arXiv作者论文页并阅读摘要，确认旋转位置表示与自注意力中的相对位置关系。 |
| model-005 | [Switch Transformers](https://arxiv.org/abs/2101.03961) | 已打开arXiv论文并单独复核摘要，确认稀疏激活、通信成本和训练稳定性讨论。 |
| model-006 | [SentencePiece](https://github.com/google/sentencepiece) | 已打开作者仓库正文，核对BPE/Unigram介绍、Python训练与编码解码示例；项目声明并非Google官方产品。 |
| model-007 | [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) | 已打开Jay Alammar作者原文，核对encoder、self-attention、逐位置FFN与张量说明。 |
| model-008 | [Hugging Face Diffusion Course](https://huggingface.co/learn/diffusion-course/unit1/1) | 已打开官方课程Unit 1，核对从零实现、Diffusers notebook、训练与采样解释及后续单元目录。 |
| model-009 | [Diffusers Documentation](https://huggingface.co/docs/diffusers/index) | 已打开官方文档首页，核对图像/视频/音频范围、pipeline组件与offloading/量化入口。 |
| model-010 | [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239) | 已打开arXiv论文页并阅读摘要，核对作者、去噪扩散主题与实现链接。 |
| model-011 | [Flow Matching for Generative Modeling](https://arxiv.org/abs/2210.02747) | 已打开arXiv论文页并阅读摘要，确认CNF、向量场回归、扩散与非扩散路径的关系。 |
| model-012 | [CLIP: Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020) | 已打开并单独读取论文摘要，确认图文配对预训练与自然语言指定视觉概念的方法。 |
| model-013 | [Whisper: Robust Speech Recognition via Large-Scale Weak Supervision](https://arxiv.org/abs/2212.04356) | 已打开并单独读取论文摘要，确认多语言、多任务弱监督语音识别与推理代码发布。 |
| model-014 | [DiT: Scalable Diffusion Models with Transformers](https://arxiv.org/abs/2212.09748) | 已打开并单独读取论文摘要，确认latent diffusion中用Transformer替代U-Net并分析规模。 |
| model-015 | [Video Diffusion Models](https://arxiv.org/abs/2204.03458) | 已打开并单独读取论文摘要，确认视频扩散、图像视频联合训练与时空扩展主题。 |
| model-016 | [Full Stack LLM Bootcamp](https://fullstackdeeplearning.com/llm-bootcamp/) | 已打开课程正文与目录，确认免费2023录播、UX/LLMOps/项目章节及官方工具已演进提示。 |
| model-017 | [Microsoft Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners) | 已打开官方仓库README，核对Learn/Build结构、Python/TypeScript示例、中文翻译与章节目录。 |
| model-018 | [JSON Schema: Creating your first schema](https://json-schema.org/learn/getting-started-step-by-step) | 已打开JSON Schema官方教程，核对商品目录示例、字段约束与验证步骤。 |
| model-019 | [MDN: Using server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events) | 已打开MDN正文并复核EventSource连接与message事件示例。 |
| model-020 | [Pydantic Models](https://docs.pydantic.dev/latest/concepts/models/) | 已打开官方Models文档，页面重定向到pydantic.dev；核对BaseModel、字段、JSON Schema与错误处理目录。 |
| model-021 | [RFC 9111: HTTP Caching](https://www.rfc-editor.org/rfc/rfc9111.html) | 已打开RFC Editor原文，核对缓存键、Freshness、Validation和Invalidating Stored Responses目录。 |
| model-022 | [OpenTelemetry: Traces](https://opentelemetry.io/docs/concepts/signals/traces/) | 已打开OpenTelemetry官方Traces文档，确认跟踪概念页及span相关文档入口；未执行SDK示例。 |
| model-023 | [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) | 已打开arXiv作者论文，阅读摘要并核对检索索引、生成模型及两种RAG形式。 |
| model-024 | [Sentence Transformers: Retrieve & Re-Rank](https://www.sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html) | 已打开官方正文，旧URL重定向到sentence_transformer路径；阅读bi-encoder和cross-encoder分工及示例。 |
| model-025 | [Elasticsearch: Reciprocal Rank Fusion](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/reciprocal-rank-fusion) | 已打开Elastic官方文档并核对RRF公式、排名从1开始、rank constant与候选窗口定义。 |
| model-026 | [pgvector](https://github.com/pgvector/pgvector) | 已打开作者仓库，复核HNSW与IVFFlat、距离函数索引和速度/召回/内存讨论。 |
| model-027 | [Faiss Wiki](https://github.com/facebookresearch/faiss/wiki) | 已打开Meta研究团队Wiki正文，核对密集向量相似度搜索定义、索引操作与GPU实现说明。 |
| model-028 | [BEIR](https://github.com/beir-cellar/beir) | 已打开作者仓库并阅读说明，确认异构信息检索基准、统一评估框架和原始论文链接。 |
| model-029 | [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172) | 已打开并单独读取论文摘要，确认多文档问答/键值检索与上下文位置敏感性实验。 |
| model-030 | [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) | 已打开作者工程文章正文，阅读工作流与agent区别、串联/路由/并行模式与停止条件。 |
| model-031 | [Model Context Protocol Documentation](https://modelcontextprotocol.io/docs/getting-started/intro) | 已打开官方入口并解析到2026-07-28版本，还打开该版architecture页面；未声称完成实现兼容测试。 |
| model-032 | [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) | 已打开作者论文并阅读摘要，核对推理与工具行动交替及外部环境反馈主题。 |
| model-033 | [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) | 已打开并单独读取论文摘要，确认自监督工具调用训练、参数选择与结果融入预测的描述。 |
| model-034 | [SWE-bench](https://github.com/SWE-bench/SWE-bench) | 已打开作者仓库正文，核对真实GitHub问题任务与容器化评估harness说明；未运行完整基准。 |
| model-035 | [τ-bench: Tool-Agent-User Interaction](https://arxiv.org/abs/2406.12045) | 已打开并单独读取论文摘要，确认用户交互、领域规则、数据库终态比较和多次试验可靠性。 |
| model-036 | [LangGraph Overview](https://docs.langchain.com/oss/python/langgraph/overview) | 已打开官方概述并阅读正文，核对确定性步骤与模型步骤混合、持久化及人工介入能力。 |
| model-037 | [Hugging Face PEFT](https://huggingface.co/docs/peft/index) | 已打开官方首页，核对参数高效适配定义、LoRA方法、量化和checkpoint格式入口。 |
| model-038 | [Hugging Face TRL](https://huggingface.co/docs/trl/index) | 已打开官方文档，核对SFT/DPO/GRPO、reward modeling、在线与离线方法分类及数据格式目录。 |
| model-039 | [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685) | 已打开作者论文并阅读摘要，核对冻结底座、训练低秩矩阵与公开实现链接。 |
| model-040 | [QLoRA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/abs/2305.14314) | 已打开作者论文并阅读摘要，核对冻结4-bit底座、LoRA、NF4、double quantization与paged optimizers。 |
| model-041 | [Training Language Models to Follow Instructions with Human Feedback](https://arxiv.org/abs/2203.02155) | 已打开并单独读取作者论文摘要，确认示范、输出排序和强化学习的后训练流程。 |
| model-042 | [Direct Preference Optimization](https://arxiv.org/abs/2305.18290) | 已打开论文摘要页及v2 HTML全文，阅读前置RLHF目标、DPO参数化和偏好优化解释。 |
| model-043 | [DeepSeekMath](https://arxiv.org/abs/2402.03300) | 已打开并单独读取论文摘要，确认数学数据选择与提出GRPO作为PPO变体的内容。 |
| model-044 | [LM Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness) | 已打开EleutherAI仓库正文，核对统一评估框架、任务配置、模型后端、命令和公开prompt说明。 |
| model-045 | [HELM: Holistic Evaluation of Language Models](https://arxiv.org/abs/2211.09110) | 动态项目首页未提取正文，改为打开原论文并阅读摘要，确认场景覆盖、多指标与透明报告方法。 |
| model-046 | [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) | 已打开NIST官方页面并读取自愿使用、可信性纳入设计开发评估及Playbook入口；不把框架当法律认证。 |
| model-047 | [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) | 已打开OWASP官方条目页，核对2025版提示注入、敏感信息、供应链、数据投毒、输出处理和过度代理入口。 |
| model-048 | [WinoBias: Gender Bias in Coreference Resolution](https://arxiv.org/abs/1804.06876) | 已打开并单独读取论文摘要，确认职业/性别共指基准、刻板与反刻板配对及数据增强方法。 |
| model-049 | [Datasheets for Datasets](https://arxiv.org/abs/1803.09010) | 已打开并单独读取论文摘要，核对数据文档动机、组成、收集过程和用途透明度。 |
| model-050 | [Model Cards for Model Reporting](https://arxiv.org/abs/1810.03993) | 已打开并单独读取论文摘要，确认预期用途、不同群体条件下评估、过程说明与示例模型卡。 |

## 交付检查与待维护事项

- 09–15章均包含目标、先修、规划预算、学习顺序、核心解释、知识点、7–8项精选资源、实践与验收、误区和下一步。
- 资源表从JSON内容写入，检查过唯一ID、唯一URL、字段与枚举，避免标题和链接错位。
- 本组没有实际运行课程训练或完整基准；实践是明确可执行的学习任务设计，未伪造实验分数。
- 相对链接检查由本组完成，公共知识地图与路线导航由主目录负责集成；仓库发布时应在最终整合版本重新运行全仓库链接检查。
- 维护优先级：失效链接、接口版本变动、语言译本滞后、模型许可变化、实践硬件条件。新增资源应说明替代或补充哪个学习问题，不以数量增长为目标。

[返回知识地图](../map.md) · [选择学习路线](../roadmaps/README.md)

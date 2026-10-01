---
hide:
  - toc
---

# 精选资源目录

当前收录 **171 个不同 URL 的资源入口**。一个资源可能对应多个专题；这不是课程数量或已完成实验数量。优先一手来源，具体阅读范围在各专题说明。

语言、难度、费用和计算标签是学习建议。免费阅读不包含算力、证书、硬件或再分发权；`content-reviewed` 表示查看过对应页面，不表示读完全部资料。链接检查结论见 [质量记录](quality.md)。

<div id="resource-explorer" data-catalog-url="assets/resources.json" hidden></div>

<div id="resource-fallback" markdown>

## 按专题查找

### 01 · 数学基础

阅读顺序与实践：[数学基础](topics/01-math.md)。

| 资源 | 语言 · 级别 | 费用 · 算力 | 推荐理由 |
|---|---|---|---|
| [Mathematics for Machine Learning](https://mml-book.github.io/) | 英文 · 进阶 | 免费 · CPU | 以机器学习问题连接数学；先读第 2–7 章，再做线性回归与 PCA notebook。 |
| [MIT 18.06 Linear Algebra](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/) | 英文 · 入门 | 免费 · 无 | 建立矩阵几何直觉；选线性方程组、子空间、正交投影和特征值，配习题。 |
| [MIT 18.01SC Single Variable Calculus](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/) | 英文 · 入门 | 免费 · 无 | 补导数与优化；先读 Differentiation 和 Applications，积分按需补。 |
| [Harvard Stat 110](https://stat110.hsites.harvard.edu/) | 英文 · 入门 | 免费 · 无 | 练概率推理；优先条件概率、随机变量、期望和常见分布。 |
| [Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/) | 英文 · 研究 | 免费 · CPU | 作为深入优化的参考；读凸集、凸函数和无约束优化，暂缓对偶细节。 |
| [动手学深度学习：预备知识](https://zh.d2l.ai/chapter_preliminaries/index.html) | 中文 · 入门 | 免费 · CPU | 用张量代码复核数学；选 2.3–2.6 的线性代数、微积分、自动微分和概率。 |

### 02 · 编程与计算机基础

阅读顺序与实践：[编程与计算机基础](topics/02-programming.md)。

| 资源 | 语言 · 级别 | 费用 · 算力 | 推荐理由 |
|---|---|---|---|
| [CS50's Introduction to Programming with Python](https://cs50.harvard.edu/python/) | 英文 · 入门 | 免费 · CPU | 零编程基础的主线；做函数、循环、异常、测试和文件章节习题，证书不必购买。 |
| [Python 官方中文教程](https://docs.python.org/zh-cn/3/tutorial/) | 中文 · 入门 | 免费 · CPU | 已有编程经验时作主线；读控制流、数据结构、模块、异常和虚拟环境。 |
| [NumPy Quickstart](https://numpy.org/doc/stable/user/quickstart.html) | 英文 · 入门 | 免费 · CPU | 训练 shape、axis 与向量化能力；做数组操作、广播和副本/视图练习。 |
| [The Missing Semester](https://missing.csail.mit.edu/) | 中英 · 入门 | 免费 · CPU | 补实验开发工具；优先命令行、版本控制和调试，官网提供中文翻译入口。 |
| [Pro Git 中文版](https://git-scm.com/book/zh/v2) | 中文 · 入门 | 免费 · CPU | 让实验变更可追溯；读 Git 基础、分支新建与合并、远程分支。 |
| [pytest Get Started](https://docs.pytest.org/en/stable/getting-started.html) | 英文 · 入门 | 免费 · CPU | 把边界条件写成可重复检查；读第一个测试、异常断言、浮点比较和临时目录。 |
| [uv：Working on projects](https://docs.astral.sh/uv/guides/projects/) | 英文 · 进阶 | 免费 · CPU | 管理隔离环境与锁定依赖；读 pyproject、uv.lock、依赖管理和运行命令。 |

### 03 · 数据工程与数据质量

阅读顺序与实践：[数据工程与数据质量](topics/03-data.md)。

| 资源 | 语言 · 级别 | 费用 · 算力 | 推荐理由 |
|---|---|---|---|
| [pandas Getting started tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html) | 英文 · 入门 | 免费 · CPU | 用真实表格学习数据处理；做读写、筛选、聚合、合表及时间字段。 |
| [PostgreSQL Tutorial](https://www.postgresql.org/docs/current/tutorial.html) | 英文 · 入门 | 免费 · CPU | 学关系模型和 SQL；先读查询、JOIN、聚合，再读事务及窗口函数。 |
| [DuckDB Guides](https://duckdb.org/docs/current/guides/overview) | 英文 · 进阶 | 免费 · CPU | 练本地文件分析；读 CSV/Parquet 导入、直接查询 Parquet 与性能排查。 |
| [scikit-learn：Common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html) | 英文 · 入门 | 免费 · CPU | 建立数据泄漏直觉；完整读预处理不一致、泄漏与随机性控制。 |
| [Datasheets for Datasets](https://arxiv.org/abs/1803.09010) | 英文 · 进阶 | 免费 · 无 | 为数据写说明书；读动机与数据采集、组成、用途记录框架。 |
| [UCI Machine Learning Repository](https://archive.ics.uci.edu/) | 英文 · 入门 | 免费 · CPU | 练数据来源审查；选一个小型表格集，阅读字段、出处、引用和许可后再建模。 |

### 04 · 机器学习

阅读顺序与实践：[机器学习](topics/04-machine-learning.md)。

| 资源 | 语言 · 级别 | 费用 · 算力 | 推荐理由 |
|---|---|---|---|
| [An Introduction to Statistical Learning](https://www.statlearning.com/) | 英文 · 入门 | 免费 · CPU | 以 Python 版作理论主线；读回归、分类、重采样、正则化、树模型与对应 lab。 |
| [mlcourse.ai](https://mlcourse.ai/book/index.html) | 英文 · 进阶 | 部分免费 · CPU | 练从 EDA 到 boosting 的完整流程；先做 Topic 1–5 和 10 的公开 demo。 |
| [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html) | 英文 · 进阶 | 免费 · CPU | 作为实验查阅手册；按当前模型阅读，再看交叉验证、指标和 Pipeline。 |
| [XGBoost：Introduction to Boosted Trees](https://xgboost.readthedocs.io/en/stable/tutorials/model.html) | 英文 · 进阶 | 免费 · CPU | 理解 boosting 优化目标；重点读训练损失+正则项、逐步加树和叶子权重。 |
| [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course) | 英文 · 入门 | 免费 · CPU | 快速建立任务与指标直觉；做线性回归、逻辑回归和分类指标模块。 |
| [CS229 Lecture Notes](https://cs229.stanford.edu/main_notes.pdf) | 英文 · 进阶 | 免费 · 无 | 补推导而非追视频；先读线性回归、逻辑回归和广义线性模型。 |
| [Datawhale 南瓜书](https://github.com/datawhalechina/pumpkin-book) | 中文 · 进阶 | 免费 · 无 | 需要中文推导时查阅；对照自己正在学的线性模型或 SVM，不当作零基础主教材。 |

### 05 · 深度学习

阅读顺序与实践：[深度学习](topics/05-deep-learning.md)。

| 资源 | 语言 · 级别 | 费用 · 算力 | 推荐理由 |
|---|---|---|---|
| [动手学深度学习](https://zh.d2l.ai/) | 中文 · 入门 | 免费 · 可选GPU | 作为中文主线；按第 3–7 章学回归、MLP、训练、CNN，再补第 10–11 章。 |
| [PyTorch Learn the Basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html) | 英文 · 入门 | 免费 · CPU | 建立标准训练循环；按 Tensors 到 Save & Load 全流程完成 FashionMNIST 示例。 |
| [Deep Learning](https://www.deeplearningbook.org/) | 英文 · 进阶 | 免费 · 无 | 补数值计算和训练原理；读第 4、6–8、11 章，作为参考而非追新工具。 |
| [Practical Deep Learning for Coders](https://course.fast.ai/) | 英文 · 入门 | 免费 · 可选GPU | 喜欢先做作品可选此主线；先完成 Part 1 的模型训练与迁移学习。 |
| [TensorFlow Playground](https://playground.tensorflow.org/) | 英文 · 入门 | 免费 · CPU | 交互观察决策边界；比较不同层数、噪声、学习率与正则化。 |
| [Karpathy micrograd](https://github.com/karpathy/micrograd) | 英文 · 进阶 | 免费 · CPU | 看清自动微分；阅读 engine.py 的运算与 backward，再做二分类 demo。 |

### 06 · 自然语言处理

阅读顺序与实践：[自然语言处理](topics/06-nlp.md)。

| 资源 | 语言 · 级别 | 费用 · 算力 | 推荐理由 |
|---|---|---|---|
| [Stanford CS224N](https://web.stanford.edu/class/cs224n/) | 英文 · 进阶 | 部分免费 · 可选GPU | 系统学神经 NLP；从词向量、反向传播、注意力到模型评估，选公开讲义与往年视频。 |
| [Speech and Language Processing](https://web.stanford.edu/~jurafsky/slp3/) | 英文 · 进阶 | 免费 · 无 | 补文本与语言任务；读 Words and Tokens、N-grams、分类、Embeddings 和 Transformers。 |
| [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1) | 英文 · 进阶 | 免费 · 可选GPU | 连接 NLP 理论与库；学 1–4 章模型流程及 5–8 章数据、分词器和任务。 |
| [SentencePiece](https://github.com/google/sentencepiece) | 英文 · 进阶 | 免费 · CPU | 理解子词与语言无关预处理；读分词、反分词、BPE/Unigram 与模型文件说明。 |
| [spaCy Linguistic Features](https://spacy.io/usage/linguistic-features) | 英文 · 进阶 | 免费 · CPU | 认识结构化 NLP；选 tokenization、词性、依存和命名实体识别示例。 |
| [Natural Language Processing with Python](https://www.nltk.org/book/) | 英文 · 入门 | 免费 · CPU | 练语料、文本处理和传统分类；读第 1–3、6–7 章，跳过不相关语法细节。 |

### 07 · 计算机视觉

阅读顺序与实践：[计算机视觉](topics/07-computer-vision.md)。

| 资源 | 语言 · 级别 | 费用 · 算力 | 推荐理由 |
|---|---|---|---|
| [Stanford CS231n](https://cs231n.stanford.edu/) | 英文 · 进阶 | 部分免费 · 可选GPU | 作深度视觉主线；从分类和 CNN 到检测，完成公开作业中的小模型。 |
| [Computer Vision: Algorithms and Applications](https://szeliski.org/Book/) | 英文 · 进阶 | 免费 · CPU | 补几何与经典视觉；选图像形成、特征、匹配和多视几何，深度内容按需看。 |
| [TorchVision Object Detection Finetuning Tutorial](https://docs.pytorch.org/tutorials/intermediate/torchvision_tutorial.html) | 英文 · 进阶 | 免费 · 可选GPU | 把检测任务落到数据接口；完成 Penn-Fudan 上的 Mask R-CNN 微调及结果可视化。 |
| [OpenCV-Python Tutorials](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html) | 英文 · 入门 | 免费 · CPU | 掌握图像读写与坐标；先做 Core Operations、Image Processing，再学特征。 |
| [timm Quickstart](https://huggingface.co/docs/timm/quickstart) | 英文 · 进阶 | 免费 · 可选GPU | 比较预训练骨干；读模型加载、分类头替换、特征抽取及匹配预处理。 |
| [Detectron2 Tutorials](https://detectron2.readthedocs.io/en/latest/tutorials/index.html) | 英文 · 进阶 | 免费 · GPU | 进阶了解检测工程；先读数据注册、配置、训练和评估，注意依赖版本配套。 |

### 08 · 时间序列与异常检测

阅读顺序与实践：[时间序列与异常检测](topics/08-time-series.md)。

| 资源 | 语言 · 级别 | 费用 · 算力 | 推荐理由 |
|---|---|---|---|
| [Forecasting: Principles and Practice](https://otexts.com/fpp3/) | 英文 · 入门 | 免费 · CPU | 先建立预测方法论；读探索、分解、基础预测、回测、ETS 与 ARIMA，代码使用 R。 |
| [statsmodels Time Series Analysis](https://www.statsmodels.org/stable/tsa.html) | 英文 · 进阶 | 免费 · CPU | 用 Python 复现实验；查 ACF/PACF、ARIMA、ETS、STL 和诊断。 |
| [sktime Notebook Examples](https://www.sktime.net/docs/examples/) | 英文 · 进阶 | 免费 · CPU | 规范预测实验；读 Forecasting、Window splitters、Pipelines and Tuning。 |
| [aeon Examples](https://www.aeon-toolkit.org/en/stable/examples.html) | 英文 · 进阶 | 免费 · CPU | 拓展到序列分类；选 TSC、距离方法和 ROCKET/MiniRocket，区别预测与分类任务。 |
| [PyTorch Forecasting Tutorials](https://pytorch-forecasting.readthedocs.io/en/stable/tutorials.html) | 英文 · 进阶 | 免费 · 可选GPU | 在可靠统计基线上学习深度预测；选 TFT 需求预测或 N-BEATS 一个项目。 |
| [StatsForecast Quick Start](https://nixtlaverse.nixtla.io/statsforecast/docs/getting-started/getting_started_short.html) | 英文 · 入门 | 免费 · CPU | 快速跑统计预测基线；看 long-format 数据、AutoARIMA、预测区间与绘图。 |

### 09 · 大语言模型

阅读顺序与实践：[大语言模型](topics/09-llm.md)。

| 资源 | 语言 · 级别 | 费用 · 算力 | 推荐理由 |
|---|---|---|---|
| [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1) | 英文 · 进阶 | 免费 · 可选GPU | 连接 NLP 理论与库；学 1–4 章模型流程及 5–8 章数据、分词器和任务。 |
| [SentencePiece](https://github.com/google/sentencepiece) | 英文 · 进阶 | 免费 · CPU | 理解子词与语言无关预处理；读分词、反分词、BPE/Unigram 与模型文件说明。 |
| [Stanford CS336: Language Modeling from Scratch (2025)](https://cs336.stanford.edu/spring2025/) | 英文 · 进阶 | 免费 · GPU | 先做Assignment 1并读架构与MoE讲义；适合愿意自己实现组件的学习者，完整课程另有系统与数据作业。 |
| [Attention Is All You Need](https://arxiv.org/abs/1706.03762) | 英文 · 进阶 | 免费 · 无 | 读模型结构与attention部分，手算一次Q/K/V维度；理解原始encoder-decoder而非假设所有LLM都相同。 |
| [RoFormer: Enhanced Transformer with Rotary Position Embedding](https://arxiv.org/abs/2104.09864) | 英文 · 研究 | 免费 · 无 | 读RoPE构造和相对位置性质；先推导二维旋转内积，再看扩展性质。 |
| [Switch Transformers](https://arxiv.org/abs/2101.03961) | 英文 · 研究 | 免费 · 无 | 读稀疏专家路由、负载均衡与训练稳定性；用于区分总参数与激活计算量。 |
| [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) | 英文 · 入门 | 免费 · 无 | 先看张量流向、自注意力和多头图解，再回到原论文；用自己的例子复述，不把图解当严格证明。 |

### 10 · 生成模型与多模态

阅读顺序与实践：[生成模型与多模态](topics/10-generative-multimodal.md)。

| 资源 | 语言 · 级别 | 费用 · 算力 | 推荐理由 |
|---|---|---|---|
| [Hugging Face Diffusion Course](https://huggingface.co/learn/diffusion-course/unit1/1) | 英文 · 进阶 | 免费 · 可选GPU | 先完成Unit 1最小去噪实验，再读条件控制；避免一开始下载大型文生图模型。 |
| [Diffusers Documentation](https://huggingface.co/docs/diffusers/index) | 英文 · 进阶 | 免费 · GPU | 读Quickstart、pipeline与scheduler概念，再按硬件读优化；理解模型和采样器可以分别选择。 |
| [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239) | 英文 · 进阶 | 免费 · 无 | 读正向加噪、反向过程与训练目标；把损失和采样算法分别写成伪代码。 |
| [Flow Matching for Generative Modeling](https://arxiv.org/abs/2210.02747) | 英文 · 研究 | 免费 · 无 | 读条件概率路径与向量场回归，先用二维线性路径理解训练，再研究ODE采样。 |
| [CLIP: Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020) | 英文 · 进阶 | 免费 · 无 | 读图文配对训练和zero-shot分类方法，思考检索相似度与精细视觉推理的区别。 |
| [Whisper: Robust Speech Recognition via Large-Scale Weak Supervision](https://arxiv.org/abs/2212.04356) | 英文 · 进阶 | 免费 · 无 | 读数据、任务构造和鲁棒性实验；关注语言、噪声与分布变化，不把一个总分当通用结论。 |
| [DiT: Scalable Diffusion Models with Transformers](https://arxiv.org/abs/2212.09748) | 英文 · 研究 | 免费 · 无 | 读latent patch与Transformer骨干设计；理解扩散训练方式和网络结构是不同维度。 |
| [Video Diffusion Models](https://arxiv.org/abs/2204.03458) | 英文 · 研究 | 免费 · 无 | 读视频架构与时间扩展方法；重点观察时序一致性为何超出单帧生成问题。 |

### 11 · AI 应用开发

阅读顺序与实践：[AI 应用开发](topics/11-ai-applications.md)。

| 资源 | 语言 · 级别 | 费用 · 算力 | 推荐理由 |
|---|---|---|---|
| [Full Stack LLM Bootcamp](https://fullstackdeeplearning.com/llm-bootcamp/) | 英文 · 进阶 | 免费 · CPU | 先读UX、LLMOps和askFSDL项目分析，学习产品完整链路；2023示例接口需对照现行文档。 |
| [Microsoft Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners) | 中英 · 入门 | 免费 · CPU | 优先学提示、聊天、函数调用、UX、安全和生命周期章节；材料免费，云端API可能收费。 |
| [JSON Schema: Creating your first schema](https://json-schema.org/learn/getting-started-step-by-step) | 英文 · 入门 | 免费 · CPU | 完整做一遍对象、字段、嵌套与验证示例；用于给模型输出定义可检查的结构契约。 |
| [MDN: Using server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events) | 英文 · 进阶 | 免费 · CPU | 读EventSource、事件格式、错误和关闭连接；将流式展示与最终业务提交分开设计。 |
| [Pydantic Models](https://docs.pydantic.dev/latest/concepts/models/) | 英文 · 进阶 | 免费 · CPU | 读模型定义、字段与验证错误；练习结构校验后再做业务语义检查。 |
| [RFC 9111: HTTP Caching](https://www.rfc-editor.org/rfc/rfc9111.html) | 英文 · 进阶 | 免费 · CPU | 读缓存键、新鲜度、验证与失效章节；迁移这些思想时区分HTTP缓存和模型结果缓存。 |
| [OpenTelemetry: Traces](https://opentelemetry.io/docs/concepts/signals/traces/) | 英文 · 进阶 | 免费 · CPU | 读trace与span概念，把检索、模型、重排和工具各阶段耗时关联到一次请求。 |

### 12 · 检索增强生成

阅读顺序与实践：[检索增强生成](topics/12-rag.md)。

| 资源 | 语言 · 级别 | 费用 · 算力 | 推荐理由 |
|---|---|---|---|
| [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) | 英文 · 进阶 | 免费 · 无 | 读参数记忆与非参数记忆、RAG-Sequence/Token；区分原始训练方法和今日应用管线。 |
| [Sentence Transformers: Retrieve & Re-Rank](https://www.sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html) | 英文 · 进阶 | 免费 · 可选GPU | 读完整双阶段检索例子，先复现召回再加CrossEncoder；用于定位相关性与延迟取舍。 |
| [Elasticsearch: Reciprocal Rank Fusion](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/reciprocal-rank-fusion) | 英文 · 进阶 | 免费 · CPU | 先读RRF公式与手算示例，再研究查询实现；融合分数不同量纲的检索列表。 |
| [pgvector](https://github.com/pgvector/pgvector) | 英文 · 进阶 | 免费 · CPU | 读距离函数、HNSW/IVFFlat和过滤部分；适合把向量检索与已有Postgres数据模型结合。 |
| [Faiss Wiki](https://github.com/facebookresearch/faiss/wiki) | 英文 · 进阶 | 免费 · 可选GPU | 先读相似度搜索和索引选择，再在固定向量集比较准确率、延迟与内存。 |
| [BEIR](https://github.com/beir-cellar/beir) | 英文 · 进阶 | 免费 · 可选GPU | 读数据格式和评估示例，学习跨数据集检索评估；先选小子集，不急着跑全套。 |
| [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172) | 英文 · 进阶 | 免费 · 无 | 读证据位置实验和评估协议；为自己的模型重做位置对照，不直接套用旧模型结论。 |

### 13 · Agent 与工作流

阅读顺序与实践：[Agent 与工作流](topics/13-agents.md)。

| 资源 | 语言 · 级别 | 费用 · 算力 | 推荐理由 |
|---|---|---|---|
| [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) | 英文 · 进阶 | 免费 · CPU | 读workflows、agents和工具设计附录；先画清控制流，再选框架。 |
| [Model Context Protocol Documentation](https://modelcontextprotocol.io/docs/getting-started/intro) | 英文 · 进阶 | 免费 · CPU | 从简介进入Architecture与Security；实现前固定规范版本，并单独设计权限与信任边界。 |
| [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) | 英文 · 进阶 | 免费 · 无 | 读行动与观察交替的轨迹示例，自己用结构化状态实现最小循环。 |
| [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) | 英文 · 研究 | 免费 · 无 | 读API调用样本构造和筛选方法；区分训练模型用工具与应用运行时调度。 |
| [SWE-bench](https://github.com/SWE-bench/SWE-bench) | 英文 · 进阶 | 免费 · CPU | 读任务定义与评估harness，理解测试环境与最终代码行为；本地容器可能占用较多磁盘内存。 |
| [τ-bench: Tool-Agent-User Interaction](https://arxiv.org/abs/2406.12045) | 英文 · 研究 | 免费 · 无 | 读最终数据库状态评估与多次运行可靠性指标；为自己的工具任务定义可执行成功条件。 |
| [LangGraph Overview](https://docs.langchain.com/oss/python/langgraph/overview) | 英文 · 进阶 | 免费 · CPU | 读持久执行、状态、streaming与human-in-the-loop概念；先有纯代码基线再引入编排。 |

### 14 · 微调与对齐

阅读顺序与实践：[微调与对齐](topics/14-finetuning-alignment.md)。

| 资源 | 语言 · 级别 | 费用 · 算力 | 推荐理由 |
|---|---|---|---|
| [Hugging Face PEFT](https://huggingface.co/docs/peft/index) | 英文 · 进阶 | 免费 · GPU | 先读Quicktour、LoRA和checkpoint格式；检查真正参与训练的参数和底座依赖。 |
| [Hugging Face TRL](https://huggingface.co/docs/trl/index) | 英文 · 进阶 | 免费 · GPU | 按Dataset Formats→Chat Templates→SFT→DPO/GRPO阅读，固定库版本再运行示例。 |
| [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685) | 英文 · 进阶 | 免费 · 无 | 读低秩参数化、目标层与实验，手算adapter参数量；不要把节省比例当所有模型的常量。 |
| [QLoRA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/abs/2305.14314) | 英文 · 研究 | 免费 · 无 | 读量化底座、NF4与adapter训练；区分存储、计算精度和显存峰值。 |
| [Training Language Models to Follow Instructions with Human Feedback](https://arxiv.org/abs/2203.02155) | 英文 · 进阶 | 免费 · 无 | 读SFT→偏好标注→RLHF流程与局限；理解优化人类偏好和绝对正确并非同义。 |
| [Direct Preference Optimization](https://arxiv.org/abs/2305.18290) | 英文 · 研究 | 免费 · 无 | 读第3–4节和推导附录，写出优选/劣选相对参考策略的损失；先验证玩具例子梯度方向。 |
| [DeepSeekMath](https://arxiv.org/abs/2402.03300) | 英文 · 研究 | 免费 · 无 | 重点读GRPO与奖励设计，同时检查数据筛选；不要把数学任务结果直接外推所有领域。 |

### 15 · 评估、安全与负责任 AI

阅读顺序与实践：[评估、安全与负责任 AI](topics/15-evaluation-safety.md)。

| 资源 | 语言 · 级别 | 费用 · 算力 | 推荐理由 |
|---|---|---|---|
| [Datasheets for Datasets](https://arxiv.org/abs/1803.09010) | 英文 · 进阶 | 免费 · 无 | 为数据写说明书；读动机与数据采集、组成、用途记录框架。 |
| [LM Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness) | 英文 · 进阶 | 免费 · 可选GPU | 读任务配置、指标和结果记录；先用小模型与小任务验证流程，再增加规模。 |
| [HELM: Holistic Evaluation of Language Models](https://arxiv.org/abs/2211.09110) | 英文 · 进阶 | 免费 · 无 | 读场景与多指标设计，给自己的应用建立覆盖矩阵；使用原论文理解方法而非追榜。 |
| [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) | 英文 · 进阶 | 免费 · 无 | 从框架与Playbook入口理解治理、识别、衡量与管理，把责任与证据写进项目流程。 |
| [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) | 英文 · 进阶 | 免费 · CPU | 优先读prompt injection、敏感信息泄漏、输出处理与过度代理；映射到自有系统测试。 |
| [WinoBias: Gender Bias in Coreference Resolution](https://arxiv.org/abs/1804.06876) | 英文 · 进阶 | 免费 · 无 | 读配对样本构造与分组评估；学习控制变量，不把一个英语基准当完整公平结论。 |
| [Model Cards for Model Reporting](https://arxiv.org/abs/1810.03993) | 英文 · 入门 | 免费 · 无 | 读模型卡要素与示例，为自己的模型记录用途、分组指标、评估条件与限制。 |

### 16 · 硬件与系统基础

阅读顺序与实践：[硬件与系统基础](topics/16-hardware-systems.md)。

| 资源 | 语言 · 级别 | 费用 · 算力 | 推荐理由 |
|---|---|---|---|
| [Computer Systems: A Programmer's Perspective 作者站](https://csapp.cs.cmu.edu/) | 英文 · 进阶 | 部分免费 · CPU | 从程序员视角学习缓存、虚拟内存、并发与 I/O；教材通常需购买或借阅，配套站点部分免费。 |
| [Operating Systems: Three Easy Pieces](https://pages.cs.wisc.edu/~remzi/OSTEP/) | 英文 · 入门 | 免费 · CPU | 按虚拟化、并发、持久化学习 OS，并用作者提供的模拟题验证理解。 |
| [Stanford CS144: Introduction to Computer Networking](https://cs144.github.io/) | 英文 · 进阶 | 免费 · CPU | 用字节流和网络实验理解可靠传输、拥塞与延迟；完整实验需要 C++ 基础。 |
| [Brendan Gregg: Linux Performance](https://www.brendangregg.com/linuxperf.html) | 英文 · 进阶 | 免费 · CPU | 通过性能方法、工具地图和火焰图定位系统瓶颈；Linux 工具需相应环境。 |
| [Linux Kernel: Memory Management Concepts](https://docs.kernel.org/admin-guide/mm/concepts.html) | 英文 · 进阶 | 免费 · CPU | 区分虚拟地址、驻留内存、NUMA、页缓存与内存回收。 |
| [Apache Parquet Overview](https://parquet.apache.org/docs/overview/) | 英文 · 入门 | 免费 · CPU | 理解列式格式与实现差异，为数据加载和特征读取建立存储模型。 |

### 17 · GPU、算子与编译器

阅读顺序与实践：[GPU、算子与编译器](topics/17-gpu-kernels-compilers.md)。

| 资源 | 语言 · 级别 | 费用 · 算力 | 推荐理由 |
|---|---|---|---|
| [CUDA Programming Guide](https://docs.nvidia.com/cuda/cuda-programming-guide/index.html) | 英文 · 进阶 | 免费 · GPU | 查阅 Programming Model、SIMT、异步执行和内存语义，作为 CUDA 实验依据。 |
| [Triton 官方教程](https://triton-lang.org/main/getting-started/tutorials/) | 英文 · 进阶 | 免费 · GPU | 按向量加法、融合 softmax、矩阵乘法顺序实现算子并比较性能。 |
| [机器学习编译课程（中文）](https://book-zh.mlc.ai/) | 中文 · 进阶 | 免费 · 可选GPU | 通过 TensorIR、自动优化、GPU 加速和计算图理解编译思想；注意课程版本与库版本差异。 |
| [Deep Learning Systems: Algorithms and Implementation](https://dlsyscourse.org/) | 英文 · 进阶 | 免费 · 可选GPU | 通过自动微分、数组库与硬件加速学习深度学习框架内部机制。 |
| [Nsight Compute Profiling Guide](https://docs.nvidia.com/nsight-compute/ProfilingGuide/index.html) | 英文 · 进阶 | 免费 · GPU | 学习 Roofline、Memory Chart 与性能指标，用证据解释算子瓶颈。 |
| [Stanford CS336: Language Modeling from Scratch](https://cs336.stanford.edu/) | 英文 · 进阶 | 免费 · GPU | 选学 resource accounting、kernels、parallelism 和 systems 作业，连接算子与训练系统。 |
| [PyTorch: Introduction to torch.compile](https://docs.pytorch.org/tutorials/intermediate/torch_compile_tutorial.html) | 英文 · 进阶 | 免费 · 可选GPU | 理解 eager/compiled 对比、编译冷启动、graph break 和动态行为。 |

### 18 · 分布式训练

阅读顺序与实践：[分布式训练](topics/18-distributed-training.md)。

| 资源 | 语言 · 级别 | 费用 · 算力 | 推荐理由 |
|---|---|---|---|
| [PyTorch: Distributed Data Parallel](https://docs.pytorch.org/tutorials/intermediate/ddp_tutorial.html) | 英文 · 进阶 | 免费 · 可选GPU | 建立最小多进程训练，理解梯度同步、初始化与保存加载。 |
| [PyTorch: Fully Sharded Data Parallel (FSDP2)](https://docs.pytorch.org/tutorials/intermediate/FSDP_tutorial.html) | 英文 · 进阶 | 免费 · GPU | 理解 fully_shard、参数重组与状态分片，避免混用旧 FSDP API。 |
| [PyTorch: Tensor Parallel](https://docs.pytorch.org/tutorials/intermediate/TP_tutorial.html) | 英文 · 进阶 | 免费 · GPU | 学习按行/列切分、DeviceMesh、DTensor 和布局带来的通信。 |
| [DeepSpeed: Zero Redundancy Optimizer](https://www.deepspeed.ai/tutorials/zero/) | 英文 · 进阶 | 免费 · GPU | 把 ZeRO 三阶段与参数、梯度、优化器状态的显存账本对应起来。 |
| [NCCL: Collective Operations](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html) | 英文 · 进阶 | 免费 · GPU | 用各集合通信图例理解 all-reduce、all-gather、reduce-scatter 和 all-to-all。 |
| [PyTorch: Distributed Checkpoint](https://docs.pytorch.org/tutorials/recipes/distributed_checkpoint_recipe.html) | 英文 · 进阶 | 免费 · 可选GPU | 学习分片保存、加载与 resharding，并理解恢复需要的目标状态布局。 |
| [DeepSpeed: Pipeline Parallelism](https://www.deepspeed.ai/tutorials/pipeline/) | 英文 · 进阶 | 免费 · GPU | 理解层切分、micro-batch、流水线调度与 stage 负载均衡。 |
| [DeepSpeed: Mixture of Experts](https://www.deepspeed.ai/tutorials/mixture-of-experts/) | 英文 · 进阶 | 免费 · GPU | 理解专家分组、数据/专家并行组合，建立 MoE 路由通信模型。 |

### 19 · 推理与模型服务

阅读顺序与实践：[推理与模型服务](topics/19-inference-serving.md)。

| 资源 | 语言 · 级别 | 费用 · 算力 | 推荐理由 |
|---|---|---|---|
| [vLLM Quickstart](https://docs.vllm.ai/en/stable/getting_started/quickstart/) | 英文 · 进阶 | 免费 · 可选GPU | 先建立离线批推理和在线服务，再按当前 CPU/GPU 安装要求选择环境。 |
| [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180) | 英文 · 研究 | 免费 · 无 | 阅读 KV 分页、碎片和共享机制，不直接套用论文硬件上的加速比。 |
| [Fast Inference from Transformers via Speculative Decoding](https://arxiv.org/abs/2211.17192) | 英文 · 研究 | 免费 · 无 | 学习 draft、验证和修正采样，理解保持目标分布的条件。 |
| [vLLM Disaggregated Prefilling](https://docs.vllm.ai/en/stable/features/disagg_prefill/) | 英文 · 进阶 | 免费 · GPU | 理解独立调整 TTFT/ITL 的动机、KV 传输和 connector 的额外复杂度。 |
| [vLLM Benchmark CLI](https://docs.vllm.ai/en/stable/benchmarking/cli/) | 英文 · 进阶 | 免费 · 可选GPU | 建立在线负载测试，记录输入输出分布、TTFT、ITL、TPOT 与有效吞吐。 |
| [ONNX Runtime: Quantize ONNX Models](https://onnxruntime.ai/docs/performance/model-optimizations/quantization.html) | 英文 · 进阶 | 免费 · CPU | 理解 scale/zero point、静态/动态量化、校准、误差诊断和硬件限制。 |
| [DistServe: Disaggregating Prefill and Decoding for Goodput-optimized LLM Serving](https://arxiv.org/abs/2401.09670) | 英文 · 研究 | 免费 · 无 | 从延迟目标与 goodput 理解 PD 分离，而不是只追求最高 token 吞吐。 |

### 20 · MLOps 与生产系统

阅读顺序与实践：[MLOps 与生产系统](topics/20-mlops.md)。

| 资源 | 语言 · 级别 | 费用 · 算力 | 推荐理由 |
|---|---|---|---|
| [Made With ML: MLOps Course](https://madewithml.com/courses/mlops/) | 英文 · 进阶 | 免费 · 可选GPU | 通过一个项目串起设计、测试、版本、CI/CD 与监控；免费指公开自学内容。 |
| [MLflow Model Registry](https://www.mlflow.org/docs/latest/registry/) | 英文 · 进阶 | 免费 · CPU | 区分实验记录、模型 lineage、版本、别名、标签与发布路由。 |
| [DVC: .dvc Files](https://doc.dvc.org/user-guide/project-structure/dvc-files) | 英文 · 进阶 | 免费 · CPU | 通过哈希、路径和远端元数据理解大文件版本机制。 |
| [KServe 官方概览](https://kserve.github.io/website/docs/intro) | 英文 · 进阶 | 免费 · 可选GPU | 已有 Kubernetes 场景下理解 control plane、data plane 与模型服务资源。 |
| [Prometheus: Histograms and Summaries](https://prometheus.io/docs/practices/histograms/) | 英文 · 进阶 | 免费 · CPU | 理解延迟分布和聚合，避免直接平均多副本分位数。 |
| [OpenTelemetry: Observability Primer](https://opentelemetry.io/docs/concepts/observability-primer/) | 英文 · 入门 | 免费 · CPU | 区分日志、指标和追踪，将模型服务请求串成可排查的证据。 |
| [scikit-learn: Model Persistence](https://scikit-learn.org/stable/model_persistence.html) | 英文 · 进阶 | 免费 · CPU | 比较持久化格式、版本兼容与可执行反序列化的边界。 |

### 21 · 端侧 AI

阅读顺序与实践：[端侧 AI](topics/21-edge-ai.md)。

| 资源 | 语言 · 级别 | 费用 · 算力 | 推荐理由 |
|---|---|---|---|
| [ONNX Runtime: Quantize ONNX Models](https://onnxruntime.ai/docs/performance/model-optimizations/quantization.html) | 英文 · 进阶 | 免费 · CPU | 理解 scale/zero point、静态/动态量化、校准、误差诊断和硬件限制。 |
| [ONNX Runtime: Deploy on Mobile](https://onnxruntime.ai/docs/tutorials/mobile/) | 英文 · 进阶 | 免费 · CPU | 建立 CPU 基线再测手机执行后端，关注模型大小、延迟与功耗。 |
| [MLX 官方文档](https://ml-explore.github.io/mlx/build/html/index.html) | 英文 · 进阶 | 免费 · 可选GPU | Apple Silicon 路线重点学习惰性求值、统一内存与本地数组计算；先确认平台支持。 |
| [Transformers.js: Running Models on WebGPU](https://huggingface.co/docs/transformers.js/en/guides/webgpu) | 英文 · 进阶 | 免费 · 可选GPU | 学习浏览器 pipeline 的 GPU 设备选择，结合能力检测与 CPU 回退。 |
| [Google LiteRT Overview](https://developers.google.com/edge/litert/overview) | 英文 · 进阶 | 免费 · 可选GPU | 理解端侧转换、CompiledModel 与 CPU/GPU/NPU 部署路线。 |
| [Core ML Tools Overview](https://apple.github.io/coremltools/docs-guides/source/overview-coremltools.html) | 英文 · 进阶 | 免费 · 可选GPU | 学习第三方模型转换、验证和优化，面向 Apple 应用交付。 |
| [ONNX Runtime Web](https://onnxruntime.ai/docs/tutorials/web/) | 英文 · 入门 | 免费 · CPU | 比较客户端/服务端路线和 WASM、WebGPU 等后端，理解算子支持范围。 |

### 22 · 强化学习与机器人

阅读顺序与实践：[强化学习与机器人](topics/22-rl-robotics.md)。

| 资源 | 语言 · 级别 | 费用 · 算力 | 推荐理由 |
|---|---|---|---|
| [David Silver · Reinforcement Learning](https://davidstarsilver.wordpress.com/teaching/) | 英文 · 入门 | 免费 · CPU | 从 MDP、价值函数、策略梯度建立决策学习框架 |
| [Gymnasium](https://gymnasium.farama.org/) | 英文 · 入门 | 免费 · CPU | 核对环境接口、终止与截断语义，练表格 Q-learning |
| [Berkeley CS285 · Deep Reinforcement Learning](https://rail.eecs.berkeley.edu/deeprlcourse/) | 英文 · 进阶 | 免费 · 可选GPU | 以模仿、策略梯度、离线 RL 组织进阶；大型深度实验需 GPU |
| [MIT Underactuated Robotics](https://underactuated.mit.edu/) | 英文 · 进阶 | 免费 · CPU | 补足动力学、LQR、轨迹优化和控制约束 |
| [LeRobot](https://huggingface.co/docs/lerobot/index) | 英文 · 进阶 | 免费 · 可选GPU | 学习演示数据与策略接口；实机另需机器人硬件 |
| [RT-2: Vision-Language-Action Models](https://robotics-transformer2.github.io/) | 英文 · 研究 | 免费 · 无 | 从作者项目页理解 VLA 的动作表示，阅读不需 GPU |
| [MuJoCo](https://github.com/google-deepmind/mujoco) | 英文 · 进阶 | 免费 · CPU | 认识动力学仿真与接触；大规模策略学习另算算力 |

### 23 · 推荐与信息检索

阅读顺序与实践：[推荐与信息检索](topics/23-recommendation-search.md)。

| 资源 | 语言 · 级别 | 费用 · 算力 | 推荐理由 |
|---|---|---|---|
| [Introduction to Information Retrieval](https://nlp.stanford.edu/IR-book/) | 英文 · 入门 | 免费 · CPU | 作者免费在线版；优先倒排、评分和检索评估 |
| [TensorFlow Recommenders](https://www.tensorflow.org/recommenders) | 中英 · 进阶 | 免费 · CPU | 官方示例连接推荐数据、召回与排序 |
| [Faiss Documentation](https://faiss.ai/) | 英文 · 进阶 | 免费 · 可选GPU | 从精确向量索引到 ANN 的速度、内存、召回权衡 |
| [MovieLens · GroupLens](https://grouplens.org/datasets/movielens/) | 英文 · 入门 | 免费 · CPU | 推荐任务的数据入口；具体版本和再分发遵守原始数据条款 |
| [TorchRec Overview](https://meta-pytorch.org/torchrec/overview.html) | 英文 · 进阶 | 免费 · 可选GPU | 把大 embedding 表、分片与推荐工程连接起来 |

### 24 · 图学习与知识表示

阅读顺序与实践：[图学习与知识表示](topics/24-graphs.md)。

| 资源 | 语言 · 级别 | 费用 · 算力 | 推荐理由 |
|---|---|---|---|
| [NetworkX](https://networkx.org/documentation/stable/) | 英文 · 入门 | 免费 · CPU | 先学图构造、路径、中心性，建立非神经基线 |
| [W3C RDF 1.1 Primer](https://www.w3.org/TR/rdf11-primer/) | 英文 · 入门 | 免费 · 无 | 通过三元组、IRI 和 Turtle 理解知识表示 |
| [Stanford CS224W](https://cs224w.stanford.edu/) | 英文 · 进阶 | 免费 · 可选GPU | 图学习主线，连接消息传递、图表示与作业 |
| [PyTorch Geometric](https://pytorch-geometric.readthedocs.io/en/latest/) | 英文 · 进阶 | 免费 · 可选GPU | 从小图例子学到 mini-batch、采样与大图训练 |
| [Open Graph Benchmark](https://ogb.stanford.edu/) | 英文 · 研究 | 免费 · 可选GPU | 使用官方划分和评估器，规范节点、边和图任务比较 |

### 25 · 因果推断与概率建模

阅读顺序与实践：[因果推断与概率建模](topics/25-causal-probabilistic.md)。

| 资源 | 语言 · 级别 | 费用 · 算力 | 推荐理由 |
|---|---|---|---|
| [Probabilistic Machine Learning](https://probml.github.io/pml-book/) | 英文 · 进阶 | 免费 · CPU | 作者公开资料可读；按概率、图模型和推断主题选章，纸书另售 |
| [Stanford CS228 Notes](https://ermongroup.github.io/cs228-notes/) | 英文 · 进阶 | 免费 · 无 | 按表示、推断、学习三层组织概率图模型 |
| [Learn PyMC & Bayesian Modeling](https://www.pymc.io/projects/docs/en/stable/learn.html) | 英文 · 进阶 | 免费 · CPU | 做后验和预测检查，不只报告点估计 |
| [Causal Inference: What If](https://miguelhernan.org/whatifbook) | 英文 · 进阶 | 免费 · CPU | 原作者开放电子资料，从识别假设学习因果推断 |
| [DoWhy v0.13 Documentation](https://www.pywhy.org/dowhy/v0.13/) | 英文 · 进阶 | 免费 · CPU | 固定版本入口，区分建模、识别、估计和反驳检查 |
| [EconML](https://www.pywhy.org/EconML/) | 英文 · 进阶 | 免费 · CPU | 研究异质效应和 double machine learning 的使用条件 |

### 26 · AI for Science

阅读顺序与实践：[AI for Science](topics/26-ai-for-science.md)。

| 资源 | 语言 · 级别 | 费用 · 算力 | 推荐理由 |
|---|---|---|---|
| [DeepChem](https://deepchem.io/) | 英文 · 进阶 | 免费 · 可选GPU | 从分子表示、性质预测与结构切分开始 |
| [AlphaFold 2](https://github.com/google-deepmind/alphafold) | 英文 · 研究 | 免费 · GPU | 查看结构预测输入、置信度、数据库需求和原始许可；不是低成本复现承诺 |
| [DeePMD-kit](https://docs.deepmodeling.com/projects/deepmd/en/latest/) | 英文 · 研究 | 免费 · GPU | 学习能量与力目标、数据、势函数和模型偏差检查 |
| [DeepXDE](https://deepxde.readthedocs.io/en/latest/) | 英文 · 进阶 | 免费 · 可选GPU | 从 ODE/PDE 和边界条件理解物理约束训练 |
| [NeuralOperator](https://neuraloperator.github.io/dev/) | 英文 · 研究 | 免费 · 可选GPU | 理解函数到函数映射及分辨率、训练分布的限制 |

### 27 · 经典 AI 与规划优化

阅读顺序与实践：[经典 AI 与规划优化](topics/27-classical-ai.md)。

| 资源 | 语言 · 级别 | 费用 · 算力 | 推荐理由 |
|---|---|---|---|
| [Artificial Intelligence: A Modern Approach](https://aima.cs.berkeley.edu/) | 英文 · 入门 | 部分免费 · CPU | 目录、代码与练习公开，完整教材另售；补齐经典 AI 全景 |
| [Berkeley CS188 · Fall 2024 archive](https://inst.eecs.berkeley.edu/~cs188/archive/fa24/) | 英文 · 入门 | 免费 · CPU | 固定归档课程；学习搜索、博弈、约束与概率推理 |
| [Google OR-Tools](https://developers.google.com/optimization) | 中英 · 进阶 | 免费 · CPU | 从排班和路由理解组合优化、可行性与最优性 |
| [Online Z3 Guide](https://microsoft.github.io/z3guide/) | 英文 · 进阶 | 免费 · CPU | 使用 SMT 和可执行例子理解 SAT、UNSAT 与 UNKNOWN |
| [DEAP](https://deap.readthedocs.io/en/master/) | 英文 · 进阶 | 免费 · CPU | 进化计算的表示、选择、变异、统计与多目标优化 |

</div>

[知识地图](map.md) · [调研记录](research/README.md)

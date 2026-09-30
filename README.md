# AI Atlas · AI 全栈学习地图

**从数学与计算机基础，到算法、模型、应用开发与 AI Infra。**

一份面向中文学习者的开源项目草案：用先修关系找到起点，用精选的一手资料深入，用可以验收的项目留下学习证据。

![AI Atlas：基础、模型、应用与系统构成的学习地图](docs/assets/atlas.svg)

[开始学习](docs/start.md) · [27 个专题](docs/map.md) · [6 条路线](docs/roadmaps/README.md) · [资源目录](docs/resources.md) · [动手实验](docs/projects/README.md)

## 先选一个起点

| 你现在的情况 | 从这里出发 | 第一件能完成的事 |
|---|---|---|
| 没写过代码，想系统学 AI | [零基础路线](docs/roadmaps/beginner.md) | 手写一个能收敛的回归模型 |
| 会 Python，想做算法 | [算法工程路线](docs/roadmaps/algorithm.md) | 完成有基线、无数据泄漏的训练实验 |
| 会开发，想做 AI 产品 | [应用开发路线](docs/roadmaps/application.md) | 做带引用、可评估的知识检索原型 |
| 想研究大模型训练与对齐 | [LLM 训练路线](docs/roadmaps/llm.md) | 理解 attention，再设计小模型微调对照 |
| 想做推理优化、GPU、分布式 | [AI Infra 路线](docs/roadmaps/infra.md) | 算清显存预算，找到一个可验证的瓶颈 |
| 想读论文、做研究或转入交叉学科 | [研究路线](docs/roadmaps/research.md) | 完成一份可复现的小规模论文实验 |

不确定选哪条？先读 [开始之前](docs/start.md)。路线里的时间是主动学习预算估算，不是就业或掌握程度承诺。

## 这份 Wiki 提供什么

- **27 个专题入口**：学习目标、先修、核心概念、精选资源、实践与验收。
- **6 条分方向路线**：按阶段安排学习内容和产出，避免把所有资料都当必修。
- **可筛选的资源目录**：记录语言、难度、费用、算力与核实状态，提供 JSON 数据源。
- **4 个本地实验**：纯 Python 标准库，普通 CPU、无需 API Key、无需下载模型。
- **8 张项目任务书**：从回归、attention、检索，到微调、服务压测、Agent、论文复现。
- **可本地阅读的文档站**：中文搜索、深浅主题、代码复制；GitHub 上也能直接阅读 Markdown。

## 知识版图

| 层次 | 专题 |
|---|---|
| 基础与算法 | [数学](docs/topics/01-math.md) · [编程](docs/topics/02-programming.md) · [数据](docs/topics/03-data.md) · [机器学习](docs/topics/04-machine-learning.md) · [深度学习](docs/topics/05-deep-learning.md) · [NLP](docs/topics/06-nlp.md) · [视觉](docs/topics/07-computer-vision.md) · [时序](docs/topics/08-time-series.md) |
| 模型与应用 | [LLM](docs/topics/09-llm.md) · [生成与多模态](docs/topics/10-generative-multimodal.md) · [应用开发](docs/topics/11-ai-applications.md) · [RAG](docs/topics/12-rag.md) · [Agent](docs/topics/13-agents.md) · [微调对齐](docs/topics/14-finetuning-alignment.md) · [评估安全](docs/topics/15-evaluation-safety.md) |
| AI Infra | [硬件系统](docs/topics/16-hardware-systems.md) · [GPU 与编译器](docs/topics/17-gpu-kernels-compilers.md) · [分布式训练](docs/topics/18-distributed-training.md) · [推理服务](docs/topics/19-inference-serving.md) · [MLOps](docs/topics/20-mlops.md) · [端侧 AI](docs/topics/21-edge-ai.md) |
| 交叉领域 | [强化学习与机器人](docs/topics/22-rl-robotics.md) · [推荐搜索](docs/topics/23-recommendation-search.md) · [图与知识表示](docs/topics/24-graphs.md) · [因果概率](docs/topics/25-causal-probabilistic.md) · [AI for Science](docs/topics/26-ai-for-science.md) · [经典 AI](docs/topics/27-classical-ai.md) |

这是可扩展的主干地图，**不是“囊括 AI 全部知识”的承诺**。覆盖深度和待展开领域见 [知识地图](docs/map.md)。

## 十分钟内开始动手

在本仓库根目录运行，实验支持 Python 3.9+，只使用标准库：

```bash
python3 examples/linear_regression.py
python3 examples/attention.py
python3 examples/retrieval.py --query "如何减少模型幻觉"
python3 examples/memory_budget.py
python3 -m unittest discover -s tests -v
```

示例数据是仓库内的合成数据与原创短文本。检索实验展示召回与证据提取，不调用生成模型；显存工具给出简化估算，不代表实测容量。

## 本地阅读站

直接打开 Markdown 即可学习。需要搜索、导航和主题切换时，建议 Python 3.11+：

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-docs.txt
python scripts/build_catalog.py
python -m mkdocs serve -a 127.0.0.1:8000
```

访问 [本地文档站](http://127.0.0.1:8000)。Windows PowerShell 使用 `.venv\Scripts\Activate.ps1` 激活环境，其他命令相同。

生成静态文件：

```bash
python scripts/check_content.py
python -m mkdocs build --strict
```

输出位于 `site/`。仓库包含检查工作流；尚未连接 GitHub 远端或发布线上地址。更多操作见 [维护与发布](docs/guides/maintenance.md)。

## 为什么这样组织

参考了 [lvy010/AI-wiki](https://github.com/lvy010/AI-wiki)、[OSSU](https://github.com/ossu/computer-science)、[Microsoft AI for Beginners](https://github.com/microsoft/AI-For-Beginners)、[LLM Course](https://github.com/mlabonne/llm-course)、[D2L](https://d2l.ai/)、[Hugging Face Learn](https://huggingface.co/learn)、[Full Stack Deep Learning](https://fullstackdeeplearning.com/) 和 [Made With ML](https://madewithml.com/) 等项目的课程组织。

本仓库自行编写路线、概念导读和项目任务，资源保留原作者链接。调研比较、核实方法与局限见 [调研记录](docs/research/README.md)。不使用实时 Star 排名，不搬运课程正文或付费教材。

## 目录结构

```text
docs/          知识地图、路线、27 个专题、项目与阅读指南
data/          资源元数据、专题分类与先修关系
examples/      4 个无需外部依赖的 CPU 实验
scripts/       目录生成、内容与链接检查
tests/         实验行为和数值正确性检查
mkdocs.yml     阅读站配置
.github/       持续检查、问题模板与 PR 模板
```

## 贡献与许可状态

欢迎提交勘误、失效链接、替代资源和带复现记录的项目。先读 [贡献指南](CONTRIBUTING.md)；推荐资料时，请说明它解决哪个学习问题、有什么先修和使用限制。

本次在空目录建立首版，**尚未由仓库所有者选定公开许可证**。许可现状和第三方资料边界见 [LICENSE-NOTICE.md](LICENSE-NOTICE.md)。首版内容核实日期：**2026-09-30**；资源可访问性、课程与软件版本可能变化。

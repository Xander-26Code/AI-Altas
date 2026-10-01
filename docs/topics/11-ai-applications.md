# 11 · AI 应用开发

> 目标：把一次模型调用变成有输入契约、失败处理、成本记录和评估的应用；完成一个可演示、可维护的最小产品。
> 先修：Python 或 TypeScript、HTTP / JSON、基础后端开发。无需先训练大模型。建议规划 80–140 小时。这是完成先修后系统学习主教材、练习和一个项目的规划预算，不含补先修，不等于掌握整个领域。

## 资源列表

课程材料免费不意味着示例 API 免费；先用本地模拟响应完成测试，再自行选择模型服务。核实日期：2026-09-30。

| 资源 | 语言 / 级别 | 费用 / 算力 | 为什么推荐、读哪部分 |
| --- | --- | --- | --- |
| [Full Stack LLM Bootcamp](https://fullstackdeeplearning.com/llm-bootcamp/) | 英文 / 进阶 | 免费 / CPU | 先读UX、LLMOps和askFSDL项目分析，学习产品完整链路；2023示例接口需对照现行文档。 |
| [Microsoft Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners) | 中英 / 入门 | 免费 / CPU | 优先学提示、聊天、函数调用、UX、安全和生命周期章节；材料免费，云端API可能收费。 |
| [JSON Schema: Creating your first schema](https://json-schema.org/learn/getting-started-step-by-step) | 英文 / 入门 | 免费 / CPU | 完整做一遍对象、字段、嵌套与验证示例；用于给模型输出定义可检查的结构契约。 |
| [MDN: Using server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events) | 英文 / 进阶 | 免费 / CPU | 读EventSource、事件格式、错误和关闭连接；将流式展示与最终业务提交分开设计。 |
| [Pydantic Models](https://docs.pydantic.dev/latest/concepts/models/) | 英文 / 进阶 | 免费 / CPU | 读模型定义、字段与验证错误；练习结构校验后再做业务语义检查。 |
| [RFC 9111: HTTP Caching](https://www.rfc-editor.org/rfc/rfc9111.html) | 英文 / 进阶 | 免费 / CPU | 读缓存键、新鲜度、验证与失效章节；迁移这些思想时区分HTTP缓存和模型结果缓存。 |
| [OpenTelemetry: Traces](https://opentelemetry.io/docs/concepts/signals/traces/) | 英文 / 进阶 | 免费 / CPU | 读trace与span概念，把检索、模型、重排和工具各阶段耗时关联到一次请求。 |

### 补充课程与实作资源

| 资源 | 语言 · 难度 | 获取 · 算力 | 用法与阅读范围 |
|---|---|---|---|
| [Datawhale · LLM Universe](https://github.com/datawhalechina/llm-universe) | 中文 · 入门 | 免费 · CPU | 选第一部分 API、知识库、RAG、评估与优化；进阶部分仍有在编内容。核对依赖版本，API 费用另计。 |
| [DataTalks.Club · LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp) | 英文 · 进阶 | 免费 · CPU | 选 RAG、Vector Search、Evaluation、Monitoring 和项目；先完成普通检索基线，再扩展 agentic 流程。 |
| [Awesome LLM Apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | 英文 · 进阶 | 免费 · CPU | 项目选题库；完成主课后只挑一个 RAG 或 Agent 示例阅读架构、依赖与评估，不把 demo 当生产方案。 |

以上新增入口核实于 2026-10-01；资料免费不含硬件与 API 费用。

## 按资源安排学习顺序

中文主线选 LLM Universe，英文选 Microsoft Generative AI for Beginners。主课完成后用文档补接口与可观测性。

按顺序完成主线，每步完成右列产出后再推进；选修不计入必做清单。页首时长包含所选主线、练习与本页项目，不包含把全部资料逐一学完。

| 阶段 | 使用资源 | 阅读 / 练习范围 | 完成后应留下什么 |
|---|---|---|---|
| 1 · 第一个应用 | [Datawhale · LLM Universe](https://github.com/datawhalechina/llm-universe)；[Microsoft Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners) | API 调用、提示、聊天或分类；两套入门课择一 | 完成带超时、异常处理的模型适配器 |
| 2 · 结构与界面 | [JSON Schema: Creating your first schema](https://json-schema.org/learn/getting-started-step-by-step)；[Pydantic Models](https://docs.pydantic.dev/latest/concepts/models/)；[MDN: Using server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events) | JSON Schema 对象与验证；Pydantic Models；SSE 事件格式 | 验证模型输出，区分流式展示与最终提交 |
| 3 · 产品流程 | [Full Stack LLM Bootcamp](https://fullstackdeeplearning.com/llm-bootcamp/)；[DataTalks.Club · LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp) | Bootcamp UX、LLMOps；Zoomcamp 评估与监控选读 | 补固定问题集、反馈和成本记录 |
| 4 · 独立项目 | [Awesome LLM Apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | 从应用示例库选一个与目标相近的案例读代码 | 按下方任务自行实现并记录差异 |
| 选修 · 性能与追踪 | [RFC 9111: HTTP Caching](https://www.rfc-editor.org/rfc/rfc9111.html)；[OpenTelemetry: Traces](https://opentelemetry.io/docs/concepts/signals/traces/) | 缓存新鲜度与失效；trace 和 span | 为已有应用测一次端到端调用链 |

## 实践：可审计的工单分类服务

建立一个本地服务，读取 JSONL 工单并输出分类结果。先写 `FakeModel`：它能正常返回、延迟返回、返回残缺 JSON、返回未知类别、抛出限流错误。随后实现真实模型适配器，但测试不依赖外部网络。

**具体步骤**：手工构造 40 条工单，其中 10 条缺少关键信息、10 条含同义表达、5 条带诱导指令；先划出 10 条测试样本；定义三个类别和人工复核条件；实现 schema、业务校验、最多两次重试和取消；保存提示版本与耗时；最后画混淆矩阵，逐条分析错分。保留一份简单关键词规则作为对照。

**验收标准**：非法输出不能直接进入下游；模拟超时不导致无限等待；取消后不再触发工具；重复请求不会重复创建记录；日志不含密钥和完整敏感文本；测试集分类质量、人工复核率和延迟均可重算。可把“测试集至少 80% 正确”设为个人练习目标，但不能把小样本成绩当作上线承诺。

再加一个只读工具 `get_category_policy(category)`，通过允许列表限制工具名称。测试模型请求不存在的工具、错误参数和越权查询时，应用是否在执行前拦住。工具调用是由应用执行的程序行为，不能因为内容由模型生成就绕过常规鉴权。

## 常见误区

- **“只要提示写得够长，错误就会消失。”** 需要数据、验证和失败流程；过长提示还会增加延迟与干扰。
- **“用了框架就具备生产能力。”** 超时、权限、审计和产品验收仍由开发者负责。
- **“流式文本可以直接当最终 JSON 使用。”** 中途断开或字段尚未闭合时容易误触业务动作。
- **“跑通一次 demo 就可以上线。”** 先看多次运行、边界输入和真实任务分布。

## 下一步

需要引用企业知识时学习 [RAG](12-rag.md)，需要多步决策时学习 [Agents](13-agents.md)。在扩展功能前，把 [评估与安全](15-evaluation-safety.md) 的回归集接入开发流程。

[返回知识地图](../map.md) · [选择学习路线](../roadmaps/README.md)

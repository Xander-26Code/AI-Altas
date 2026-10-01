# 13 · Agents、工具与工作流

> 目标：用有限工具、显式状态和停止条件构建一个能完成任务的 agent；知道什么时候确定性工作流更合适。
> 先修：AI 应用开发、JSON schema、函数调用、状态机、基本测试。建议规划 80–160 小时。这是完成先修后系统学习主教材、练习和一个项目的规划预算，不含补先修，不等于掌握整个领域。

## 资源列表

教程与论文免费；接入模型服务、运行大型软件环境可能另有成本。CPU 可完成本章模拟练习。核实日期：2026-09-30。

| 资源 | 语言 / 级别 | 费用 / 算力 | 为什么推荐、读哪部分 |
| --- | --- | --- | --- |
| [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) | 英文 / 进阶 | 免费 / CPU | 读workflows、agents和工具设计附录；先画清控制流，再选框架。 |
| [Model Context Protocol Documentation](https://modelcontextprotocol.io/docs/getting-started/intro) | 英文 / 进阶 | 免费 / CPU | 从简介进入Architecture与Security；实现前固定规范版本，并单独设计权限与信任边界。 |
| [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) | 英文 / 进阶 | 免费 / 无 | 读行动与观察交替的轨迹示例，自己用结构化状态实现最小循环。 |
| [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) | 英文 / 研究 | 免费 / 无 | 读API调用样本构造和筛选方法；区分训练模型用工具与应用运行时调度。 |
| [SWE-bench](https://github.com/SWE-bench/SWE-bench) | 英文 / 进阶 | 免费 / CPU | 读任务定义与评估harness，理解测试环境与最终代码行为；本地容器可能占用较多磁盘内存。 |
| [τ-bench: Tool-Agent-User Interaction](https://arxiv.org/abs/2406.12045) | 英文 / 研究 | 免费 / 无 | 读最终数据库状态评估与多次运行可靠性指标；为自己的工具任务定义可执行成功条件。 |
| [LangGraph Overview](https://docs.langchain.com/oss/python/langgraph/overview) | 英文 / 进阶 | 免费 / CPU | 读持久执行、状态、streaming与human-in-the-loop概念；先有纯代码基线再引入编排。 |

### 补充课程与实作资源

| 资源 | 语言 · 难度 | 获取 · 算力 | 用法与阅读范围 |
|---|---|---|---|
| [Datawhale · Hello-Agents](https://github.com/datawhalechina/hello-agents) | 中文 · 进阶 | 免费 · CPU | 先第 1、3、4 章，再第 7–10、12 章；做一个工具循环和评估项目，综合案例选修。 |
| [Hugging Face · Agents Course](https://github.com/huggingface/agents-course) | 英文 · 进阶 | 免费 · CPU | 按课程的基础、框架与用例阶段推进；与其他 Agent 主课择一，模型调用与算力另计。 |
| [Microsoft · AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners) | 中英 · 入门 | 免费 · CPU | 先读简介、工具使用、可信 Agent，再查规划、协议和生产部署；适合已有 Python 的开发者。 |
| [Awesome LLM Apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | 英文 · 进阶 | 免费 · CPU | 项目选题库；完成主课后只挑一个 RAG 或 Agent 示例阅读架构、依赖与评估，不把 demo 当生产方案。 |

以上新增入口核实于 2026-10-01；资料免费不含硬件与 API 费用。

## 按资源安排学习顺序

主课程从 Hello-Agents、HF Agents Course、Microsoft Agents 三选一；中文默认 Hello-Agents。先有简单工作流，再考虑复杂 Agent。

按顺序完成主线，每步完成右列产出后再推进；选修不计入必做清单。页首时长包含所选主线、练习与本页项目，不包含把全部资料逐一学完。

| 阶段 | 使用资源 | 阅读 / 练习范围 | 完成后应留下什么 |
|---|---|---|---|
| 1 · 选择控制流程 | [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)；[Datawhale · Hello-Agents](https://github.com/datawhalechina/hello-agents) | Building Effective Agents；Hello-Agents 第 1、3、4 章 | 实现固定工作流与一个有限步数工具循环 |
| 2 · 主课实践 | [Datawhale · Hello-Agents](https://github.com/datawhalechina/hello-agents)；[Hugging Face · Agents Course](https://github.com/huggingface/agents-course)；[Microsoft · AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners) | Hello-Agents 第 7–9 章；或另一套课的工具、框架与用例 | 加入状态、工具校验和失败恢复 |
| 3 · 协议与框架 | [Model Context Protocol Documentation](https://modelcontextprotocol.io/docs/getting-started/intro)；[LangGraph Overview](https://docs.langchain.com/oss/python/langgraph/overview) | MCP Architecture/Security；需要持久化时查 LangGraph | 明确权限、重试与人工接管入口 |
| 4 · 评估 | [Datawhale · Hello-Agents](https://github.com/datawhalechina/hello-agents)；[τ-bench: Tool-Agent-User Interaction](https://arxiv.org/abs/2406.12045)；[SWE-bench](https://github.com/SWE-bench/SWE-bench) | Hello-Agents 第 12 章；τ-bench 方法；编码任务才看 SWE-bench | 用固定任务与最终状态衡量可靠性 |
| 选修 · 论文与案例 | [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)；[Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761)；[Awesome LLM Apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | ReAct、Toolformer 或一个应用实例 | 解释示例与自己的控制流程有什么差别 |

## 实践：在模拟仓库里完成补货建议

建立本地 JSON 数据库，包含 10 个商品、库存、最低阈值和供应商交货天数。只开放三个工具：`list_items()`、`get_inventory(item_id)`、`draft_purchase(item_id, quantity)`。最后一个只写本地草稿，不发送订单。创建 20 个任务，包括库存足够、不存在的商品、工具超时、数据冲突、超出允许数量和含恶意文本的商品备注。

先写确定性工作流，再写模型选择工具的循环。两者共用工具校验器和环境，设置最多 8 次工具调用、总时限、同参数重复调用上限。每次运行从同一初始数据库副本开始，记录工具名称、经校验的参数、结果摘要和最终草稿。展示简洁决策依据与工具证据即可，不把模型内部推理当作审计事实。

**验收标准**：20 个任务各运行至少 3 次；提交成功率和每次调用数，成功定义为“草稿商品和数量符合规则，且没有越权副作用”；未知工具、错误 schema、无权限动作在执行前失败；超时能停止；中断恢复不会重复创建草稿；恶意商品备注不能增加工具权限。若 agent 没有优于工作流，说明哪些任务仍应固定执行。

进阶时把只读库存工具包装为 MCP server，按官方版本文档实现连接。先在本地测试工具发现、schema、异常和授权边界，再增加写工具。将 agent 接上 MCP 不是本章起点，也不是验收终点。

## 常见误区

- **“能够调用工具就是可靠 agent。”** 还需要正确目标、状态、恢复、权限与评估。
- **“给更多工具就更聪明。”** 重叠工具、模糊参数与噪声返回可能增加选择错误。
- **“让模型自己判断是否成功就够了。”** 需要检查最终文件、数据库或环境状态。
- **“长期记忆越多越好。”** 过期、错误或跨用户记忆会污染决策，必须有更新与删除机制。
- **“一次成功代表可重复。”** 随机性、环境变化和服务故障要求多次实验。

## 下一步

通过 [评估与安全](15-evaluation-safety.md) 建立回归与权限测试；如果大量错误来自固定任务格式或工具选择习惯，再评估 [微调与对齐](14-finetuning-alignment.md)。

[返回知识地图](../map.md) · [选择学习路线](../roadmaps/README.md)

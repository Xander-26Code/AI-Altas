# 路线 C · AI 应用开发

先修：熟悉一种语言、HTTP/JSON、基本后端与测试。规划 **300–500 小时**，每周 8–12 小时约 **6–15 个月**；没有工程基础时先补 [编程](../topics/02-programming.md)。目标是可评估的应用原型，不是生产成熟度或商业成功保证。

| 阶段 | 内容 | 投入 | 产出 | 主资源与范围 |
|---|---|---|---|---|
| 模型与接口 | [应用开发](../topics/11-ai-applications.md)、[LLM](../topics/09-llm.md) 概念选读 | 50–80 小时 | schema、异常、超时、流式与模拟适配器 | [LLM Universe](https://github.com/datawhalechina/llm-universe) 第一部分的 API 开发 → JSON Schema/Pydantic 输出校验；英文可换 Microsoft Generative AI for Beginners |
| 检索与证据 | [推荐检索](../topics/23-recommendation-search.md)、[RAG](../topics/12-rag.md) | 80–130 小时 | 有相关性标注、来源和拒答的检索应用 | [LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp) RAG、Vector Search、Evaluation → Sentence Transformers 重排教程 |
| 工具与工作流 | [Agent](../topics/13-agents.md) | 60–100 小时 | 有限状态、工具权限、重复调用与恢复测试 | [Hello-Agents](https://github.com/datawhalechina/hello-agents) 第 4、7–10、12 章选读；只需固定工作流时缩小此阶段 |
| 质量与运维 | [评估](../topics/15-evaluation-safety.md)、[MLOps](../topics/20-mlops.md) 选读 | 60–100 小时 | 固定评估集、成本、质量和延迟报告 | [LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp) Monitoring → [MLOps Zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp) 部署/监控选读；配 OWASP 检查项目风险 |
| 完整原型 | 整合与用户试用 | 50–90 小时 | 失败处理、人工反馈、回滚与操作说明 | LLM Zoomcamp 的端到端项目要求作参考，用自己的文档和评估集交付；应用示例库仅用于选题 |

## 主项目：可核查的个人知识助手

从 [本地检索](../projects/02-retrieval.md) 起步，先准备自己的文档和问题集。明确区分“召回了正确文档”“答案正确”“引用支持答案”，分别验收。初期可以用证据摘录回答；接入生成模型后，再测它是否增加了没有依据的断言。

Agent 是后续可选项。只有任务需要动态选择工具或多步交互时，才增加复杂度。先让一个明确流程跑稳，再开放更多动作。

API 或云服务的费用独立于学习时间；先用模拟接口和少量测试控制范围。外部调用前记录预算与输入数据边界。界面漂亮不代表检索、权限和异常流程正确。

[全部路线](README.md) · [Agent 项目](../projects/07-agent.md)

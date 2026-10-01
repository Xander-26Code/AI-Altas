# 15 · 评估、可靠性与安全

> 目标：为 AI 系统建立能发现退化的评估集，量化不确定性，检查数据泄漏、隐私、权限和群体表现，并写出可供他人判断的报告。
> 先修：训练/验证/测试切分、基础统计、AI 应用或模型实验。建议规划 80–140 小时。这是完成先修后系统学习主教材、练习和一个项目的规划预算，不含补先修，不等于掌握整个领域。

## 资源列表

阅读免费；评估工具的 CPU / GPU 条件取决于待测模型。安全练习只在自己的测试系统内运行。核实日期：2026-09-30。

| 资源 | 语言 / 级别 | 费用 / 算力 | 为什么推荐、读哪部分 |
| --- | --- | --- | --- |
| [LM Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness) | 英文 / 进阶 | 免费 / 可选GPU | 读任务配置、指标和结果记录；先用小模型与小任务验证流程，再增加规模。 |
| [HELM: Holistic Evaluation of Language Models](https://arxiv.org/abs/2211.09110) | 英文 / 进阶 | 免费 / 无 | 读场景与多指标设计，给自己的应用建立覆盖矩阵；使用原论文理解方法而非追榜。 |
| [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) | 英文 / 进阶 | 免费 / 无 | 从框架与Playbook入口理解治理、识别、衡量与管理，把责任与证据写进项目流程。 |
| [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) | 英文 / 进阶 | 免费 / CPU | 优先读prompt injection、敏感信息泄漏、输出处理与过度代理；映射到自有系统测试。 |
| [WinoBias: Gender Bias in Coreference Resolution](https://arxiv.org/abs/1804.06876) | 英文 / 进阶 | 免费 / 无 | 读配对样本构造与分组评估；学习控制变量，不把一个英语基准当完整公平结论。 |
| [Datasheets for Datasets](https://arxiv.org/abs/1803.09010) | 英文 / 入门 | 免费 / 无 | 按动机、组成、收集和推荐用途整理自己的数据说明；填未知而不是编造来源。 |
| [Model Cards for Model Reporting](https://arxiv.org/abs/1810.03993) | 英文 / 入门 | 免费 / 无 | 读模型卡要素与示例，为自己的模型记录用途、分组指标、评估条件与限制。 |

### 补充课程与实作资源

| 资源 | 语言 · 难度 | 获取 · 算力 | 用法与阅读范围 |
|---|---|---|---|
| [Hugging Face · smol course](https://github.com/huggingface/smol-course) | 英文 · 进阶 | 免费 · GPU | 沿 Instruction Tuning → Evaluation → Preference Alignment 学；先完成小模型 SFT 与评估，再选 DPO。 |
| [DataTalks.Club · LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp) | 英文 · 进阶 | 免费 · CPU | 选 RAG、Vector Search、Evaluation、Monitoring 和项目；先完成普通检索基线，再扩展 agentic 流程。 |

以上新增入口核实于 2026-10-01；资料免费不含硬件与 API 费用。

## 按资源安排学习顺序

先建立任务和评估集，再选工具。模型评测以 Harness 为入口，应用评估可用 LLM Zoomcamp 对应模块。

按顺序完成主线，每步完成右列产出后再推进；选修不计入必做清单。页首时长包含所选主线、练习与本页项目，不包含把全部资料逐一学完。

| 阶段 | 使用资源 | 阅读 / 练习范围 | 完成后应留下什么 |
|---|---|---|---|
| 1 · 评估设计 | [HELM: Holistic Evaluation of Language Models](https://arxiv.org/abs/2211.09110)；[Datasheets for Datasets](https://arxiv.org/abs/1803.09010)；[Model Cards for Model Reporting](https://arxiv.org/abs/1810.03993) | HELM 场景与多指标；Datasheets 和 Model Cards | 写任务、数据来源、指标与已知限制 |
| 2 · 可执行评测 | [LM Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness)；[DataTalks.Club · LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp)；[Hugging Face · smol course](https://github.com/huggingface/smol-course) | Harness 任务/指标；应用选 Zoomcamp Evaluation；微调选 smol Evaluation | 保存配置与结果，能重复运行 |
| 3 · 风险与分组 | [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)；[OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/)；[WinoBias: Gender Bias in Coreference Resolution](https://arxiv.org/abs/1804.06876) | NIST 框架；OWASP 风险；WinoBias 配对样本方法 | 补提示注入、权限与分组误差测试 |
| 4 · 整理报告 | [Model Cards for Model Reporting](https://arxiv.org/abs/1810.03993) | Model Cards 示例 | 完成下方评估包，说明仍未覆盖的场景 |

## 实践：给一个 AI 项目做“可以复算”的评估包

选择前面做过的工单分类、RAG 或 agent。构造 100 条样例：60 条常见任务、20 条边界或无答案任务、20 条安全与权限任务。分类只是起点，实际覆盖按项目定义；不使用真实密钥、私人聊天或患者资料。对每条记录保存 ID、类别、输入、预期性质和评分规则。

从中划出独立开发集和最终测试集，先冻结基线。对模型或 prompt 做一项改动，在同一测试集配对比较；随机系统至少运行 3 次。质量报告必须包含各类别结果、样本数、平均成本、延迟分位数、5 个退化案例和统计局限。若使用模型裁判，抽取至少 20 条人工复核并列出分歧，不只报一个相关系数。

安全部分使用虚构秘密标记与虚构租户数据：测试跨租户检索、恶意文档要求执行额外工具、工具返回污染、异常日志是否泄露标记、删除后缓存是否仍返回。记录防线在哪一层生效。对任何高影响实际场景，应在适用专业流程内另作领域验证，本练习不能代替部署审批。

**验收标准**：别人能用固定版本重算分数；没有把测试集用于调参；失败样例能映射到具体组件；越权用例有可执行断言；报告明确未覆盖人群与场景；模型卡包含用途、数据来源、指标、限制和回滚方案。没有发现漏洞只能说明本次测试未命中，不能写“绝对安全”。

## 常见误区

- **“榜单第一就适合我。”** 问题分布、预算、语言和风险不同，排名可迁移性有限。
- **“只要平均分提高就能上线。”** 高频关键任务或少数群体可能退化。
- **“测试集越大越好。”** 重复、污染和不代表真实任务的数据会制造虚假信心。
- **“对齐解决所有安全问题。”** 模型行为训练不能替代应用授权、输出处理和系统隔离。
- **“模型卡是营销文档。”** 它应帮助读者理解证据、适用边界和不能做出的承诺。

## 下一步

把评估回归接入 [AI 应用开发](11-ai-applications.md) 的迭代；为 [微调](14-finetuning-alignment.md) 建立训练前基线；为 [Agents](13-agents.md) 增加最终状态和副作用断言。

[返回知识地图](../map.md) · [选择学习路线](../roadmaps/README.md)

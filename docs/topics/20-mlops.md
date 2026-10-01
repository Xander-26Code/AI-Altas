# 20 · MLOps：从实验到可靠交付

> 目标：让一个模型结果能够追溯、复现、发布、监控和回滚，并把质量、可靠性与成本放进同一套决策记录。先修：能训练并评估一个小模型，熟悉 Git、Python 环境、HTTP 与基础测试。学习规划预算约 100–180 小时。以 CPU 上的小型分类或回归模型完成主线，无需先搭 Kubernetes。
> 时间口径：具备先修后，系统学习主教材、完成练习与一个项目的规划预算；不包含补先修，也不等于掌握整个领域。实际投入受基础、实验条件和项目深度影响。

## 资源列表

核验日期：2026-09-30。下列开源文档免费；托管服务、教学云资源和硬件可能另收费。

| 资源 | 语言 / 级别 / 条件 | 建议范围与理由 |
| --- | --- | --- |
| [Made With ML：MLOps](https://madewithml.com/courses/mlops/) | 英文 / 进阶 / 可选GPU | Design、Testing、Versioning、CI/CD、Monitoring；用一个项目串起完整生命周期。自学阅读免费，不将商业/直播课程计为免费权益。 |
| [MLflow Model Registry](https://www.mlflow.org/docs/latest/registry/) | 英文 / 进阶 / CPU | lineage、版本、别名与标签；区分实验产物和发布候选。官方搜索结果已核对，正文抓取受限。 |
| [DVC `.dvc` Files](https://doc.dvc.org/user-guide/project-structure/dvc-files) | 英文 / 进阶 / CPU | 哈希、路径、remote 等元数据；理解数据版本背后的机制，之后再跟文档完成数据工作流。 |
| [KServe 官方概览](https://kserve.github.io/website/docs/intro) | 英文 / 进阶 / 可选GPU | control plane、data plane、InferenceService；已有 Kubernetes 需求时再进入，不作为入门先修。 |
| [Prometheus Histograms and Summaries](https://prometheus.io/docs/practices/histograms/) | 英文 / 进阶 / CPU | 延迟分布、聚合和分位数；避免用错误指标证明发布成功。 |
| [OpenTelemetry Observability Primer](https://opentelemetry.io/docs/concepts/observability-primer/) | 英文 / 入门 / CPU | 日志、指标与链路追踪；将多组件请求串成可排查证据。 |
| [scikit-learn Model Persistence](https://scikit-learn.org/stable/model_persistence.html) | 英文 / 进阶 / CPU | 持久化格式、可执行加载与版本兼容；用小模型学习实际发布边界。 |

### 补充课程与实作资源

| 资源 | 语言 · 难度 | 获取 · 算力 | 用法与阅读范围 |
|---|---|---|---|
| [DataTalks.Club · MLOps Zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp) | 英文 · 进阶 | 免费 · CPU | 按实验追踪、流水线、部署、监控与最佳实践做项目；需 Python、Docker 与 ML 基础，云资源另计。 |
| [Machine Learning Systems](https://mlsysbook.ai/) | 英文 · 进阶 | 免费 · CPU | 用基础卷建立系统视角，规模化卷按问题查阅；教材、实验和硬件实践分开选择。 |

以上新增入口核实于 2026-10-01；资料免费不含硬件与 API 费用。

## 按资源安排学习顺序

选 MLOps Zoomcamp 或 Made With ML 做一条完整项目线。工具文档用于解决项目中的具体问题。

按顺序完成主线，每步完成右列产出后再推进；选修不计入必做清单。页首时长包含所选主线、练习与本页项目，不包含把全部资料逐一学完。

| 阶段 | 使用资源 | 阅读 / 练习范围 | 完成后应留下什么 |
|---|---|---|---|
| 1 · 项目与版本 | [DataTalks.Club · MLOps Zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp)；[Made With ML：MLOps](https://madewithml.com/courses/mlops/)；[DVC `.dvc` Files](https://doc.dvc.org/user-guide/project-structure/dvc-files) | 主课环境与实验；DVC 文件元数据 | 固定数据版本、依赖和训练命令 |
| 2 · 实验与发布 | [MLflow Model Registry](https://www.mlflow.org/docs/latest/registry/)；[scikit-learn Model Persistence](https://scikit-learn.org/stable/model_persistence.html)；[DataTalks.Club · MLOps Zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp) | 实验追踪/Model Registry；持久化与部署模块 | 保存模型与配置，实现一次版本回滚 |
| 3 · 监控与验证 | [Prometheus Histograms and Summaries](https://prometheus.io/docs/practices/histograms/)；[OpenTelemetry Observability Primer](https://opentelemetry.io/docs/concepts/observability-primer/)；[DataTalks.Club · MLOps Zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp) | Monitoring、Best Practices；指标分布与可观测性 | 记录质量、延迟和失败，建立发布检查 |
| 选修 · 集群与系统 | [KServe 官方概览](https://kserve.github.io/website/docs/intro)；[Machine Learning Systems](https://mlsysbook.ai/) | 有 Kubernetes 需求再看 KServe；教材按部署规模选读 | 为现有服务补资源、容量与恢复说明 |

## 实践：一个能回滚的小模型服务

1. 选用本地合成数据或公开小型数据集，建立简单分类器基线；固定训练、验证和最终测试集，写出一个主指标和一个关键切片指标。
2. 将准备数据、训练、评估拆成可重复执行的命令；记录依赖与配置，产物目录包含数据标识、模型和评测报告。
3. 建一个本地推理 API，校验输入 schema；响应携带模型版本，提供健康检查。不要用健康检查替代质量评估。
4. 加入测试：损坏字段、缺失字段、空批次、异常值、固定样本的预测；服务记录请求数、错误率、延迟分布和版本。
5. 产生第二个候选模型，比较同一评测集；模拟灰度流量，故意制造一项质量或延迟退化，再恢复第一版完整产物。
6. 在新目录中仅依赖说明和版本记录重建第一版，比较结果。工具可以先用普通 JSON、文件哈希和本地日志，再迁移到 MLflow/DVC。

**验收**：能从线上响应追溯到代码、数据、配置和模型；新环境可完成重建；至少一项发布门槛会拒绝退化版本；回滚后版本与关键预测恢复；有一张成本记录表，区分实测用量与估算价格。

## 常见误区与下一步

- “装了平台就是 MLOps”：没人能解释一次预测的来源，平台再多也没有闭环。
- “漂移告警必须再训练”：先确认数据故障、业务变化、标签质量和用户影响。
- “模型文件相同就可复现”：预处理、依赖、检索与服务配置也会改变结果。
- “只能大团队才能开始”：文件级版本、明确门槛与一次真实回滚已能产生价值。

回到 [推理与服务](19-inference-serving.md)优化运行成本，或进入 [端侧 AI](21-edge-ai.md)学习模型在个人设备上的交付约束。

[返回知识地图](../map.md) · [选择学习路线](../roadmaps/README.md)

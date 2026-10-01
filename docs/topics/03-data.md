# 03 · 数据处理与数据质量

> 目标：构建来源清楚、切分正确、处理一致的数据集，识别泄漏与偏差。先修：[编程基础](02-programming.md)，理解均值与概率。**规划预算：60–120 小时**，用于完成先修后系统阅读主教材、做练习并完成一个项目；不含补先修，不是掌握整个领域的承诺。CPU 足够，先用能装进内存的小数据练方法。

## 资源列表

pandas 用来学表格操作，SQL 用来理解关系与聚合，泄漏文档必须读。数据源免费访问不意味着任何用途都获许可，应阅读所选数据集自己的授权。

- **[pandas Getting started tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html)**｜英文 · 入门 · 免费 · CPU。用真实表格学习数据处理；做读写、筛选、聚合、合表及时间字段。
- **[PostgreSQL Tutorial](https://www.postgresql.org/docs/current/tutorial.html)**｜英文 · 入门 · 免费 · CPU。学关系模型和 SQL；先读查询、JOIN、聚合，再读事务及窗口函数。
- **[DuckDB Guides](https://duckdb.org/docs/current/guides/overview)**｜英文 · 进阶 · 免费 · CPU。练本地文件分析；读 CSV/Parquet 导入、直接查询 Parquet 与性能排查。
- **[scikit-learn：Common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html)**｜英文 · 入门 · 免费 · CPU。建立数据泄漏直觉；完整读预处理不一致、泄漏与随机性控制。
- **[Datasheets for Datasets](https://arxiv.org/abs/1803.09010)**｜英文 · 进阶 · 免费 · 无。为数据写说明书；读动机与数据采集、组成、用途记录框架。
- **[UCI Machine Learning Repository](https://archive.ics.uci.edu/)**｜英文 · 入门 · 免费 · CPU。练数据来源审查；选一个小型表格集，阅读字段、出处、引用和许可后再建模。

### 补充课程与实作资源

| 资源 | 语言 · 难度 | 获取 · 算力 | 用法与阅读范围 |
|---|---|---|---|
| [Wes McKinney · Python for Data Analysis, 3E](https://wesmckinney.com/book/) | 英文 · 入门 | 免费 · CPU | 作者开放在线版；选 NumPy、pandas、数据清洗、连接与聚合，跟随代码整理一份真实表格。 |
| [DataTalks.Club · Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) | 英文 · 进阶 | 免费 · CPU | 数据工程选修；从容器、SQL、编排到仓库和批处理，先完成本地小流水线，云服务另计。 |

以上新增入口核实于 2026-10-01；资料免费不含硬件与 API 费用。

## 按资源安排学习顺序

以 pandas 教程和 Python for Data Analysis 为主；SQL 配一套本地数据库。分布式数据工程作为后续选修。

按顺序完成主线，每步完成右列产出后再推进；选修不计入必做清单。页首时长包含所选主线、练习与本页项目，不包含把全部资料逐一学完。

| 阶段 | 使用资源 | 阅读 / 练习范围 | 完成后应留下什么 |
|---|---|---|---|
| 1 · 表格处理 | [pandas Getting started tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html)；[Wes McKinney · Python for Data Analysis, 3E](https://wesmckinney.com/book/) | 读写、筛选、缺失值、连接、聚合 | 保留原始表，输出可重复生成的清洗结果 |
| 2 · SQL 与文件 | [PostgreSQL Tutorial](https://www.postgresql.org/docs/current/tutorial.html)；[DuckDB Guides](https://duckdb.org/docs/current/guides/overview) | 查询、JOIN、聚合；DuckDB 查询 CSV/Parquet | 用 SQL 和 pandas 完成同一统计并核对 |
| 3 · 数据质量 | [scikit-learn：Common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html)；[Datasheets for Datasets](https://arxiv.org/abs/1803.09010)；[UCI Machine Learning Repository](https://archive.ics.uci.edu/) | 泄漏与预处理；数据说明框架；选一个 UCI 小数据集 | 先固定切分，再写字段、来源、许可和泄漏检查 |
| 选修 · 流水线 | [DataTalks.Club · Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) | 按容器/SQL、编排、仓库与批处理顺序选模块 | 将已有清洗任务改为可重跑的流水线 |

## 实践任务与验收

选一个 UCI 小型表格数据集，做一份数据审计和一个可重复的处理脚本。先用多数类或均值作为基线，把精力放在数据有效性上。

- [ ] 数据说明包含出处、获取日期、许可、字段含义、标签生成方式和适用范围；不清楚的项目明确写“未知”。
- [ ] 记录数据行数、标签分布、缺失率、重复率，以及至少两个有意义的分组统计。
- [ ] 为每个字段标记“预测时可用/不可用/待确认”，给出至少一个可能泄漏的例子。
- [ ] 切分理由与应用场景对应，用程序检查用户 ID、样本 ID 或内容哈希是否交叉。
- [ ] 填补器、编码器和模型位于同一训练流程中，测试数据没有被 `fit`。
- [ ] 抽查至少 20 行处理前后记录，确认变换符合含义；保留原始数据与脚本，避免手工改表。
- [ ] 交付一页数据说明与机器可读统计报告，使他人能复核结论。

进阶练习：人为制造一次一对多合表，把行数变化和指标偏差记录下来，随后用正确聚合顺序修复。这个实验比单纯背 SQL 语法更容易建立数据质量直觉。

## 常见误区

- **数据越多越好。** 重复、污染或采样偏差可能让大量数据提供很少有效信息。
- **异常值一定要删除。** 它可能是输入错误，也可能是任务真正关心的少见事件。
- **测试集可以反复查看。** 根据测试结果持续调方案，会把它变成隐形验证集。
- **脱敏就是删姓名。** 组合字段仍可能具有识别性，学习项目优先使用明确公开且适合教学的数据。

下一步：把数据流程接入 [机器学习](04-machine-learning.md)；涉及未来预测则同时阅读 [时间序列](08-time-series.md)。

---

资源核实：2026-09-30；已审阅推荐入口的介绍、目录或相关正文，未声明逐课完成或逐项运行。算力为本页练习建议，详见[核实记录](../research/foundations-sources.md)。

[返回知识地图](../map.md) · [选择学习路线](../roadmaps/README.md)


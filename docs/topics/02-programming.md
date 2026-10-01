# 02 · 编程与工程基础

> 目标：把学习笔记变成可运行、可复现、可检查的 Python 项目。先修：会使用电脑和文件目录即可；零基础从 CS50P 开始。零基础建议规划 **120–240 小时**；已有其他语言经验并通过基础自测者可按 **60–100 小时**规划。包含主教材、练习、调试和一个项目，不等于熟练掌握软件工程。普通 CPU，无需独立显卡。

## 资源列表

零基础以 CS50P 为主，中文 Python 文档作查阅。已有经验可跳过完整入门课，直接做数值编程与项目交付。以下公开学习材料免费，商业证书不是学习前提。

- **[CS50's Introduction to Programming with Python](https://cs50.harvard.edu/python/)**｜英文 · 入门 · 免费 · CPU。零编程基础的主线；做函数、循环、异常、测试和文件章节习题，证书不必购买。
- **[Python 官方中文教程](https://docs.python.org/zh-cn/3/tutorial/)**｜中文 · 入门 · 免费 · CPU。已有编程经验时作主线；读控制流、数据结构、模块、异常和虚拟环境。
- **[NumPy Quickstart](https://numpy.org/doc/stable/user/quickstart.html)**｜英文 · 入门 · 免费 · CPU。训练 shape、axis 与向量化能力；做数组操作、广播和副本/视图练习。
- **[The Missing Semester](https://missing.csail.mit.edu/)**｜中英 · 入门 · 免费 · CPU。补实验开发工具；优先命令行、版本控制和调试，官网提供中文翻译入口。
- **[Pro Git 中文版](https://git-scm.com/book/zh/v2)**｜中文 · 入门 · 免费 · CPU。让实验变更可追溯；读 Git 基础、分支新建与合并、远程分支。
- **[pytest Get Started](https://docs.pytest.org/en/stable/getting-started.html)**｜英文 · 入门 · 免费 · CPU。把边界条件写成可重复检查；读第一个测试、异常断言、浮点比较和临时目录。
- **[uv：Working on projects](https://docs.astral.sh/uv/guides/projects/)**｜英文 · 进阶 · 免费 · CPU。管理隔离环境与锁定依赖；读 pyproject、uv.lock、依赖管理和运行命令。

### 补充课程与实作资源

| 资源 | 语言 · 难度 | 获取 · 算力 | 用法与阅读范围 |
|---|---|---|---|
| [Wes McKinney · Python for Data Analysis, 3E](https://wesmckinney.com/book/) | 英文 · 入门 | 免费 · CPU | 作者开放在线版；选 NumPy、pandas、数据清洗、连接与聚合，跟随代码整理一份真实表格。 |

以上新增入口核实于 2026-10-01；资料免费不含硬件与 API 费用。

## 按资源安排学习顺序

零编程基础选 CS50P；有其他语言经验选 Python 官方教程。两条主线择一，后续工具按同一项目练习。

按顺序完成主线，每步完成右列产出后再推进；选修不计入必做清单。页首时长包含所选主线、练习与本页项目，不包含把全部资料逐一学完。

| 阶段 | 使用资源 | 阅读 / 练习范围 | 完成后应留下什么 |
|---|---|---|---|
| 1 · Python 主课 | [CS50's Introduction to Programming with Python](https://cs50.harvard.edu/python/)；[Python 官方中文教程](https://docs.python.org/zh-cn/3/tutorial/) | 函数、控制流、数据结构、异常、文件；零基础完成 CS50P 对应习题 | 独立完成读取文件并统计结果的脚本 |
| 2 · 开发工具 | [The Missing Semester](https://missing.csail.mit.edu/)；[Pro Git 中文版](https://git-scm.com/book/zh/v2)；[uv：Working on projects](https://docs.astral.sh/uv/guides/projects/) | 命令行、Git 基础与分支、隔离环境和依赖锁定 | 用 Git 保存一次实验，能从空环境重建 |
| 3 · 数据计算 | [NumPy Quickstart](https://numpy.org/doc/stable/user/quickstart.html)；[Wes McKinney · Python for Data Analysis, 3E](https://wesmckinney.com/book/) | NumPy 数组、广播、axis；书中 NumPy 与 pandas 入门 | 用数组替代循环并检查结果一致 |
| 4 · 测试 | [pytest Get Started](https://docs.pytest.org/en/stable/getting-started.html) | 首个测试、异常断言与临时目录 | 为下方数据处理任务加入正常和异常输入测试 |

## 实践任务与验收

做一个“CSV 体检工具”：输入本地 CSV，输出行列数、每列缺失率、数值统计与重复行数，保存 JSON 报告。先支持小文件，再自行限制最大输入大小；无需创建网页。

- [ ] 提供一条命令和一个小样例，其他人无需手动执行 notebook 单元格即可运行。
- [ ] 同时处理正常文件、空文件、非数值字段和不存在的路径，错误信息指向具体原因。
- [ ] 指标函数有手算答案的测试；测试能捕捉形状错配，而不只是验证“程序没有崩溃”。
- [ ] 依赖与 Python 版本记录清楚；不把本机绝对路径写进程序。
- [ ] 输出目录、日志和配置可追溯；重新运行不会悄悄覆盖原始数据。
- [ ] 从一次报错出发，记录“最小复现 → 假设 → 验证 → 修正”，解释怎样排除根因。

若使用 AI 辅助编码，每次至少手动检查输入假设、错误处理和一个边界例子；能解释函数的输入输出后再接收代码。复制能运行的答案不等于获得调试能力。

## 常见误区

- **一直在 notebook 中重跑局部单元格。** 隐藏状态会掩盖依赖，至少验证一次从头运行。
- **安装最新版所有包就能复现。** 代码、依赖、数据、配置与随机性都影响结果。
- **固定随机种子保证所有设备逐位一致。** 算法、硬件和并行执行仍可能产生差异。
- **先学复杂框架再写简单函数。** 框架不能替代对输入、输出和状态的理解。

下一步：用 [数据基础](03-data.md) 的流程处理真实数据，与 [数学基础](01-math.md) 并行，再进入 [机器学习](04-machine-learning.md)。

---

资源核实：2026-09-30；已审阅推荐入口的介绍、目录或相关正文，未声明逐课完成或逐项运行。算力为本页练习建议，详见[核实记录](../research/foundations-sources.md)。

[返回知识地图](../map.md) · [选择学习路线](../roadmaps/README.md)

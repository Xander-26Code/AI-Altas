# 27 · 经典 AI、搜索、规划与优化

> 目标：认识不依赖大模型训练的 AI 方法，知道何时使用搜索、约束求解和规则推理。先修：[编程与数据结构](02-programming.md)、基础离散数学。具备先修后，系统学习主教材、做练习并完成一个项目，建议预留 **100–180 小时**。补先修另计，入门实验用 CPU。

## 资源列表

| 资源 | 语言 / 难度 / 费用 / 算力 | 建议读法 |
|---|---|---|
| [AIMA 作者网站](https://aima.cs.berkeley.edu/) | 英文 / 入门 / 部分免费，教材另售 / CPU | 阅读目录与公开代码，补齐 AI 全景；不是免费全本书下载 |
| [Berkeley CS188 公开课程](https://inst.eecs.berkeley.edu/~cs188/archive/fa24/) | 英文 / 入门 / 免费公开资料 / CPU | 搜索、博弈、CSP 与概率推理；遵守课程作业分享规则 |
| [Google OR-Tools](https://developers.google.com/optimization) | 中英 / 进阶 / 免费 / CPU | 用最小排班或路径问题理解约束建模与 CP-SAT |
| [Z3 Guide](https://microsoft.github.io/z3guide/) | 英文 / 进阶 / 免费 / CPU | 从 SMT 与 Python 示例开始，明确 SAT / UNSAT / UNKNOWN |
| [DEAP](https://deap.readthedocs.io/en/master/) | 英文 / 进阶 / 免费 / CPU | 学表示、变异、选择与统计记录，再看多目标优化 |

## 按资源安排学习顺序

CS188 作主课，AIMA 按课程主题查阅。之后在运筹求解、逻辑验证和进化计算中选一个分支。

按顺序完成主线，每步完成右列产出后再推进；选修不计入必做清单。页首时长包含所选主线、练习与本页项目，不包含把全部资料逐一学完。

| 阶段 | 使用资源 | 阅读 / 练习范围 | 完成后应留下什么 |
|---|---|---|---|
| 1 · 搜索与博弈 | [Berkeley CS188 公开课程](https://inst.eecs.berkeley.edu/~cs188/archive/fa24/)；[AIMA 作者网站](https://aima.cs.berkeley.edu/) | CS188 搜索、对抗搜索及公开项目；AIMA 对应内容 | 比较 UCS/A* 的正确性与展开节点数 |
| 2 · 约束与概率 | [Berkeley CS188 公开课程](https://inst.eecs.berkeley.edu/~cs188/archive/fa24/) | 约束满足、概率推理相关讲义与练习 | 完成一个约束任务并解释无解情况 |
| 3 · 求解器分支 | [Google OR-Tools](https://developers.google.com/optimization)；[Z3 Guide](https://microsoft.github.io/z3guide/) | 排班/路由选 OR-Tools；逻辑约束选 Z3 Guide | 编码一个可检查任务，验证可行性与结果 |
| 选修 · 进化计算 | [DEAP](https://deap.readthedocs.io/en/master/) | 表示、选择、变异与统计示例 | 与简单搜索基线比较，不只展示最好一次 |

## 实践：给求解器一个可以检查的任务

实现 BFS、Dijkstra 和 A*，在同一组固定网格上比较路径成本、扩展节点数与运行时间。对小网格用 BFS 的结果作为单位成本最短路基线。加入不可达目标、起点等于终点、包含障碍和不同权重的情况。

验收要求：可视化路径、记录状态去重规则、列出启发式条件；在单位成本测试集合中，A* 必须与 BFS 的最优成本一致。进阶时刻意使用高估的启发式，找出一个返回次优解的反例，解释性能与保证的差别。

约束分支可做“5 人、7 天”的排班：每人工作上限、每天最少人数、禁止连续夜班。把解交给独立检查函数，逐条验证硬约束。求解器超时后拿到的可行解不应写成已证明最优。

## 易踩的坑

- 一段自然语言计划听起来合理，不意味着所有动作前提都满足。
- 目标函数容易算不代表它正确表达了真实需求。
- 对离散问题强行使用梯度下降，可能不如直接使用组合求解器。
- 只报告找到一个解，却不检查可行性和最优性状态，会误导读者。

下一步：[Agent](13-agents.md)、[强化学习](22-rl-robotics.md)、[图与知识表示](24-graphs.md)。

[返回知识地图](../map.md) · [选择学习路线](../roadmaps/README.md)

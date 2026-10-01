# 22 · 强化学习、机器人与具身智能

> 目标：把“预测答案”转成“在环境中选择动作”，区分强化学习、模仿学习、控制与规划。先修：[概率与优化](01-math.md)、[深度学习](05-deep-learning.md)。具备先修后，系统学习主教材、做练习并完成一个项目，建议预留 **180–320 小时**。补先修另计；这不等于掌握强化学习和机器人两个完整领域。

## 资源列表

以下资料阅读免费；具体实验可能需要算力或实体硬件。

| 资源 | 语言 / 难度 / 算力 | 建议读法 |
|---|---|---|
| [David Silver · RL lectures](https://davidstarsilver.wordpress.com/teaching/) | 英文 / 入门 / CPU | 主线入口；先学 MDP、价值函数、策略梯度，不必一次看完 |
| [Gymnasium](https://gymnasium.farama.org/) | 英文 / 入门 / CPU | 从 Basic Usage 和表格 Q-learning 示例入手，核对终止语义 |
| [Berkeley CS285](https://rail.eecs.berkeley.edu/deeprlcourse/) | 英文 / 进阶 / 可选 GPU | 主攻模仿、策略梯度、离线 RL；完整深度实验视作业配置决定资源 |
| [MIT Underactuated Robotics](https://underactuated.mit.edu/) | 英文 / 进阶 / CPU | 先看摆、LQR、轨迹优化，用控制理论补齐机器人基础 |
| [LeRobot](https://huggingface.co/docs/lerobot/index) | 英文 / 进阶 / 可选 GPU | 理解演示数据、策略与机器人接口；实机任务还需硬件 |
| [RT-2 项目页](https://robotics-transformer2.github.io/) | 英文 / 研究 / 无 | 观察视觉语言知识如何进入动作表示；阅读不等于可低成本复现 |
| [MuJoCo](https://github.com/google-deepmind/mujoco) | 英文 / 进阶 / CPU | 了解仿真状态、接触与动力学；大规模学习另算预算 |

### 补充课程与实作资源

| 资源 | 语言 · 难度 | 获取 · 算力 | 用法与阅读范围 |
|---|---|---|---|
| [RL Baselines3 Zoo](https://github.com/DLR-RM/rl-baselines3-zoo) | 英文 · 进阶 | 免费 · 可选GPU | 在掌握环境接口后选一个小任务，学习训练、评估与配置；作为实验参考，不直接照搬超参数。 |
| [Spinning Up in Deep RL](https://github.com/openai/spinningup) | 英文 · 进阶 | 免费 · 可选GPU | 补读算法、伪代码与实验方法；代码是历史教学实现，先核对旧依赖，当前实验可用 Gymnasium 与 SB3。 |

以上新增入口核实于 2026-10-01；资料免费不含硬件与 API 费用。

## 按资源安排学习顺序

先完成表格 RL 和一个小型深度 RL 实验，再决定走算法还是机器人。机器人需要额外控制与动力学基础。

按顺序完成主线，每步完成右列产出后再推进；选修不计入必做清单。页首时长包含所选主线、练习与本页项目，不包含把全部资料逐一学完。

| 阶段 | 使用资源 | 阅读 / 练习范围 | 完成后应留下什么 |
|---|---|---|---|
| 1 · RL 主课 | [David Silver · RL lectures](https://davidstarsilver.wordpress.com/teaching/)；[Gymnasium](https://gymnasium.farama.org/) | Silver 的 MDP、价值函数；Gymnasium 环境接口 | 实现网格世界并区分 terminated/truncated |
| 2 · 深度 RL | [Berkeley CS285](https://rail.eecs.berkeley.edu/deeprlcourse/)；[Spinning Up in Deep RL](https://github.com/openai/spinningup) | CS285 模仿学习、策略梯度；Spinning Up 算法与伪代码 | 用小环境比较基线，记录多个种子 |
| 3 · 规范实验 | [RL Baselines3 Zoo](https://github.com/DLR-RM/rl-baselines3-zoo) | 训练、评估与配置说明 | 保存可重跑配置，分析方差与失败 |
| 选修 · 机器人 | [MIT Underactuated Robotics](https://underactuated.mit.edu/)；[MuJoCo](https://github.com/google-deepmind/mujoco)；[LeRobot](https://huggingface.co/docs/lerobot/index)；[RT-2 项目页](https://robotics-transformer2.github.io/) | Underactuated 控制/轨迹优化 → MuJoCo → LeRobot；RT-2 用作延伸阅读 | 先完成仿真或离线数据实验，实机单独规划 |

## 实践：先让网格世界可解释

建立一个 5×5 网格，有固定起点、终点、障碍与每步小惩罚。先用动态规划求解已知模型，再让 Q-learning 通过交互学习。分别试验 `γ=0.5/0.9/0.99` 与不同探索率。

验收时提交：环境定义、价值热图、策略箭头图、至少 5 个种子的训练回报、独立评估回合，以及一个失败案例。评估时关闭训练探索，不修改环境奖励。检查学到的最短路径是否与规划基线一致；如果不一致，先排查奖励、终止和动作合法性。

机器人进阶任务可以在仿真摆上比较控制基线和学习策略，记录能量、成功率与扰动恢复。真实机器人实验需单独设计速度、力矩与工作空间限制；仿真成功不能直接当成实机安全证明。

## 易踩的坑

- 单个种子的最佳视频不能代表策略的稳定能力。
- 用评估种子调参后仍把它称为独立测试，结果会偏乐观。
- 奖励更高可能来自钻奖励定义的空子，必须检查任务是否真的完成。
- 有反馈回路的系统不是把监督学习模型多运行几次就等价于 RL。

下一步：[经典规划与搜索](27-classical-ai.md)、[多模态](10-generative-multimodal.md)、[端侧部署](21-edge-ai.md)。

[返回知识地图](../map.md) · [选择学习路线](../roadmaps/README.md)

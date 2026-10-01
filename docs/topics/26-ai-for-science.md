# 26 · AI for Science：从数据拟合到科学约束

> 目标：了解分子、蛋白质、材料与科学计算中的 AI，学会把领域约束和验证协议放进实验。先修：[数学](01-math.md)、[深度学习](05-deep-learning.md)；分子任务另需 [图学习](24-graphs.md)。具备先修后，围绕一个科学方向学习主教材、做练习并完成一个项目，建议预留 **140–280 小时**。领域科学基础另计；不代表完成多个科学领域的训练。

## 资源列表

| 资源 | 语言 / 难度 / 费用 / 算力 | 建议读法 |
|---|---|---|
| [DeepChem](https://deepchem.io/) | 英文 / 进阶 / 免费 / 可选 GPU | 从小型分子性质教程入手，重点观察数据 featurization 和 split |
| [AlphaFold 2 作者仓库](https://github.com/google-deepmind/alphafold) | 英文 / 研究 / 代码与资源按原条款 / GPU | 阅读输入、数据库依赖、置信度与运行条件；完整复现不是入门项目 |
| [DeePMD-kit](https://docs.deepmodeling.com/projects/deepmd/en/latest/) | 英文 / 研究 / 免费文档 / GPU | 理解原子势的数据、能量/力目标与模型偏差检查 |
| [DeepXDE](https://deepxde.readthedocs.io/en/latest/) | 英文 / 进阶 / 免费 / 可选 GPU | 先做最小 ODE/PDE 示例，再读 PINN 与算子学习 |
| [NeuralOperator](https://neuraloperator.github.io/dev/) | 英文 / 研究 / 免费 / 可选 GPU | 观察函数空间映射、数据网格和训练配置；大型实验另估算算力 |

## 按资源安排学习顺序

先选一个科学问题。分子、蛋白、势函数、微分方程是不同分支，下面各资源不构成必须连续学完的课程。

按顺序完成主线，每步完成右列产出后再推进；选修不计入必做清单。页首时长包含所选主线、练习与本页项目，不包含把全部资料逐一学完。

| 阶段 | 使用资源 | 阅读 / 练习范围 | 完成后应留下什么 |
|---|---|---|---|
| 1 · 选择分支 | [DeepChem](https://deepchem.io/)；[AlphaFold 2 作者仓库](https://github.com/google-deepmind/alphafold)；[DeePMD-kit](https://docs.deepmodeling.com/projects/deepmd/en/latest/)；[DeepXDE](https://deepxde.readthedocs.io/en/latest/)；[NeuralOperator](https://neuraloperator.github.io/dev/) | 分子选 DeepChem；蛋白选 AlphaFold；势函数选 DeePMD；ODE/PDE 选 DeepXDE 或 NeuralOperator | 明确领域基础、数据、真值与硬件要求 |
| 2 · 最小复现 | [DeepChem](https://deepchem.io/)；[DeepXDE](https://deepxde.readthedocs.io/en/latest/) | 入门可从分子性质预测或简单 ODE/PDE 例子二选一 | 复现小案例，记录数据切分和误差 |
| 3 · 验证与对照 | [DeepChem](https://deepchem.io/)；[DeePMD-kit](https://docs.deepmodeling.com/projects/deepmd/en/latest/)；[DeepXDE](https://deepxde.readthedocs.io/en/latest/) | 回到所选项目的数据与训练说明 | 加领域基线，检查外推与边界条件 |
| 选修 · 扩大范围 | [AlphaFold 2 作者仓库](https://github.com/google-deepmind/alphafold)；[NeuralOperator](https://neuraloperator.github.io/dev/) | 蛋白结构置信度或算子学习的分辨率与分布限制 | 提出一个可验证问题；不承诺低成本重训大型模型 |

## 实践：一个带独立真值的科学实验

先做上述一维 ODE。用固定随机种子选训练采样点，另外生成密集测试网格。与解析解及一个简单数值方法比较，报告均方误差、最大绝对误差、边界误差和训练耗时。

消融：移除边界项、减少残差采样点、把测试区间延伸到训练范围外。验收标准是解释每次变化为何影响结果，而不是只画两条看起来重合的曲线。报告 lambda 的选择过程，避免用最终测试网格调参。

分子分支扩展：对同一数据分别采用随机切分和结构切分，训练同一基线。说明更难的切分为何更贴近发现新分子的目标。遵守数据使用条件，不把任何模型输出当作实验或临床验证。

## 易踩的坑

- 忽略单位、量纲和坐标变换，会让训练结果缺乏物理意义。
- 把高度相似的分子或蛋白质放在训练和测试两侧，容易夸大泛化。
- 推理速度快不代表总成本低，数据生成与训练成本也要计入。
- 生成“看上去合理”的候选结构，只是下一轮验证的起点。

下一步：[图学习](24-graphs.md)、[因果与概率](25-causal-probabilistic.md)、[科研路线](../roadmaps/research.md)。

[返回知识地图](../map.md) · [选择学习路线](../roadmaps/README.md)

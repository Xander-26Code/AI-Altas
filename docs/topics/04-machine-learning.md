# 04 · 机器学习：从基线到可信评估

> 目标：定义学习任务，建立基线，比较模型，并解释泛化误差。先修：[数学基础](01-math.md)、[编程基础](02-programming.md)、[数据基础](03-data.md)。**规划预算：120–200 小时**，用于完成先修后系统学习主教材、做练习并完成一个项目；不含补先修，不是掌握整个领域的承诺。大部分练习 CPU 可完成。

## 资源列表

ISLP 是推荐主教材；Google 课程适合先建立直觉，其余按疑问查阅。南瓜书是其作者提供的推导笔记，不替代周志华《机器学习》原书。

- **[An Introduction to Statistical Learning](https://www.statlearning.com/)**｜英文 · 入门 · 免费 · CPU。以 Python 版作理论主线；读回归、分类、重采样、正则化、树模型与对应 lab。
- **[mlcourse.ai](https://mlcourse.ai/book/index.html)**｜英文 · 进阶 · 部分免费 · CPU。练从 EDA 到 boosting 的完整流程；先做 Topic 1–5 和 10 的公开 demo。
- **[scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)**｜英文 · 进阶 · 免费 · CPU。作为实验查阅手册；按当前模型阅读，再看交叉验证、指标和 Pipeline。
- **[XGBoost：Introduction to Boosted Trees](https://xgboost.readthedocs.io/en/stable/tutorials/model.html)**｜英文 · 进阶 · 免费 · CPU。理解 boosting 优化目标；重点读训练损失+正则项、逐步加树和叶子权重。
- **[Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course)**｜英文 · 入门 · 免费 · CPU。快速建立任务与指标直觉；做线性回归、逻辑回归和分类指标模块。
- **[CS229 Lecture Notes](https://cs229.stanford.edu/main_notes.pdf)**｜英文 · 进阶 · 免费 · 无。补推导而非追视频；先读线性回归、逻辑回归和广义线性模型。
- **[Datawhale 南瓜书](https://github.com/datawhalechina/pumpkin-book)**｜中文 · 进阶 · 免费 · 无。需要中文推导时查阅；对照自己正在学的线性模型或 SVM，不当作零基础主教材。

### 补充课程与实作资源

| 资源 | 语言 · 难度 | 获取 · 算力 | 用法与阅读范围 |
|---|---|---|---|
| [DataTalks.Club · Machine Learning Zoomcamp](https://github.com/DataTalksClub/machine-learning-zoomcamp) | 英文 · 进阶 | 免费 · CPU | 偏工程的替代主线；按回归、分类、评估、部署做作业和自己的项目，不直接套用开课周数。 |
| [Hands-On Machine Learning 第三版配套 notebook](https://github.com/ageron/handson-ml3) | 英文 · 进阶 | 部分免费 · 可选GPU | 选完整 ML 项目、分类、训练模型等 notebook；深度学习部分使用 Keras/TensorFlow，勿与 PyTorch 示例混装。 |

以上新增入口核实于 2026-10-01；资料免费不含硬件与 API 费用。

## 按资源安排学习顺序

统计主线选 ISL；工程主线可换成 ML Zoomcamp 或 Hands-On ML notebook。主线三选一，其他材料用于查阅。

按顺序完成主线，每步完成右列产出后再推进；选修不计入必做清单。页首时长包含所选主线、练习与本页项目，不包含把全部资料逐一学完。

| 阶段 | 使用资源 | 阅读 / 练习范围 | 完成后应留下什么 |
|---|---|---|---|
| 1 · 建立任务直觉 | [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course) | 回归、分类、训练与指标模块 | 说明任务、标签、基线和评估指标 |
| 2 · 主教材 | [An Introduction to Statistical Learning](https://www.statlearning.com/)；[DataTalks.Club · Machine Learning Zoomcamp](https://github.com/DataTalksClub/machine-learning-zoomcamp)；[Hands-On Machine Learning 第三版配套 notebook](https://github.com/ageron/handson-ml3) | ISL 回归、分类及 lab；或另两套课程的对应模块 | 完成回归和分类各一次，保留训练/验证切分 |
| 3 · 模型比较 | [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)；[XGBoost：Introduction to Boosted Trees](https://xgboost.readthedocs.io/en/stable/tutorials/model.html) | 交叉验证、Pipeline、树模型；XGBoost 目标与逐步加树 | 固定数据比较线性模型和树模型 |
| 4 · 独立项目 | [mlcourse.ai](https://mlcourse.ai/book/index.html) | Topic 1–5、10 中与项目相关的公开 demo | 完成下方项目和错误分析 |
| 选修 · 推导 | [CS229 Lecture Notes](https://cs229.stanford.edu/main_notes.pdf)；[Datawhale 南瓜书](https://github.com/datawhalechina/pumpkin-book) | CS229 线性模型；南瓜书相应推导 | 为正在用的模型补推导，避免两本从头重复读 |

## 实践任务与验收

完成一个表格分类项目，至少比较 Dummy 基线、逻辑回归与一个树集成模型。保留数据集原始任务定义，避免为了好看的分数随意改标签。

- [ ] 训练前写下目标、切分方式、主要指标和使用场景；最后保留同一协议。
- [ ] 模型使用相同数据边界，预处理在每个训练折内拟合。
- [ ] 报告交叉验证各折分数及均值，最终保留集只用于最终评估。
- [ ] 在验证集选择阈值，报告精确率、召回率、混淆矩阵和相关成本；概率用途额外检查校准。
- [ ] 做一个受控比较，例如正则强弱或树深；每次只改一类因素。
- [ ] 审阅错误样本，区分数据错误、边界模糊、少见子群和特征不足，并提出可验证的下一步。
- [ ] 保存预处理、模型、依赖、配置和数据标识，说明哪些分组样本太少，不能据此作强结论。

验收不要求一定超越某个分数。合理地发现复杂模型没有改进，并说明证据，比挑选一次幸运运行更有价值。

## 常见误区

- **所有任务都用 accuracy。** 指标应对应真实决策，不均衡任务尤其要看分母。
- **不断调测试集直到满意。** 模型选择与最终评估必须分离。
- **特征重要性就是因果解释。** 相关特征、采样机制和模型结构都会影响重要性。
- **聚类结果就是客观人群。** 距离、缩放、簇数和算法都会改变分组。
- **深度学习一定优于传统模型。** 应在同一数据与预算下比较。

下一步：进入 [深度学习](05-deep-learning.md)；文本可转 [自然语言处理](06-nlp.md)，时间相关业务先读 [时间序列](08-time-series.md)。

---

资源核实：2026-09-30；已审阅推荐入口的介绍、目录或相关正文，未声明逐课完成或逐项运行。算力为本页练习建议，详见[核实记录](../research/foundations-sources.md)。

[返回知识地图](../map.md) · [选择学习路线](../roadmaps/README.md)


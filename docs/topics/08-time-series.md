# 08 · 时间序列：预测、分类与异常检测

> 目标：建立符合时间因果顺序的回测，比较统计与学习方法，报告预测误差和不确定性。先修：[数据](03-data.md)、[机器学习](04-machine-learning.md)；深度预测另需 [深度学习](05-deep-learning.md)。**规划预算：60–120 小时**，用于完成先修后系统学习主教材、做练习并完成一个项目；不含补先修，不是领域掌握承诺。统计基线用 CPU 即可。

## 资源列表

先完成统计基线与回测，再考虑深度预测。aeon 用于序列分类等任务，不能把它的分类样例直接当成未来预测协议。

- **[Forecasting: Principles and Practice](https://otexts.com/fpp3/)**｜英文 · 入门 · 免费 · CPU。先建立预测方法论；读探索、分解、基础预测、回测、ETS 与 ARIMA，代码使用 R。
- **[statsmodels Time Series Analysis](https://www.statsmodels.org/stable/tsa.html)**｜英文 · 进阶 · 免费 · CPU。用 Python 复现实验；查 ACF/PACF、ARIMA、ETS、STL 和诊断。
- **[sktime Notebook Examples](https://www.sktime.net/docs/examples/)**｜英文 · 进阶 · 免费 · CPU。规范预测实验；读 Forecasting、Window splitters、Pipelines and Tuning。
- **[aeon Examples](https://www.aeon-toolkit.org/en/stable/examples.html)**｜英文 · 进阶 · 免费 · CPU。拓展到序列分类；选 TSC、距离方法和 ROCKET/MiniRocket，区别预测与分类任务。
- **[PyTorch Forecasting Tutorials](https://pytorch-forecasting.readthedocs.io/en/stable/tutorials.html)**｜英文 · 进阶 · 免费 · 可选GPU。在可靠统计基线上学习深度预测；选 TFT 需求预测或 N-BEATS 一个项目。
- **[StatsForecast Quick Start](https://nixtlaverse.nixtla.io/statsforecast/docs/getting-started/getting_started_short.html)**｜英文 · 入门 · 免费 · CPU。快速跑统计预测基线；看 long-format 数据、AutoARIMA、预测区间与绘图。

## 按资源安排学习顺序

方法论选 FPP3；代码希望统一 Python 时，配 statsmodels 或 StatsForecast。深度预测放在统计基线之后。

按顺序完成主线，每步完成右列产出后再推进；选修不计入必做清单。页首时长包含所选主线、练习与本页项目，不包含把全部资料逐一学完。

| 阶段 | 使用资源 | 阅读 / 练习范围 | 完成后应留下什么 |
|---|---|---|---|
| 1 · 预测方法 | [Forecasting: Principles and Practice](https://otexts.com/fpp3/) | 探索、分解、基础预测与回测；教材示例用 R | 定义预测时点、跨度与可用信息 |
| 2 · 统计基线 | [statsmodels Time Series Analysis](https://www.statsmodels.org/stable/tsa.html)；[StatsForecast Quick Start](https://nixtlaverse.nixtla.io/statsforecast/docs/getting-started/getting_started_short.html) | ARIMA、ETS、诊断；两套工具择一 | 用滚动回测比较朴素方法与统计模型 |
| 3 · 规范实验 | [sktime Notebook Examples](https://www.sktime.net/docs/examples/) | Forecasting、Window splitters、Pipelines and Tuning | 检查特征生成和调参不泄漏未来 |
| 选修 · 任务分支 | [aeon Examples](https://www.aeon-toolkit.org/en/stable/examples.html)；[PyTorch Forecasting Tutorials](https://pytorch-forecasting.readthedocs.io/en/stable/tutorials.html) | 分类选 aeon；深度预测选 TFT 或 N-BEATS 教程 | 只选一种，与前面的可靠基线比较 |

## 实践任务与验收

选择有明确频率的公开需求或流量数据，预测固定未来跨度。至少比较最近值、季节朴素、一个统计模型；有余力再加入滞后特征加树模型。

- [ ] 写清预测时刻、跨度、频率、目标单位与外生变量可用时间。
- [ ] 检查时间缺口、重复、时区和序列 ID，说明补缺是否使用未来信息。
- [ ] 至少设置三个滚动起点，报告各窗口和各预测跨度的误差。
- [ ] 所有模型共享起点与历史数据边界，标准化与调参只使用当时可用的数据。
- [ ] 使用 MAE/RMSE 等合适指标；含零值时不要直接依赖 MAPE。
- [ ] 检查残差时间结构、节假日与突变时段，列出具体失败情形。
- [ ] 若提供预测区间，同时报告覆盖率和区间宽度。
- [ ] 保存每次回测的预测值、真值、时间与版本，使结论可复核。

进阶：做异常检测时区分逐点指标和事件级指标，写清告警合并、延迟和阈值选择方式。序列分类则应按受试者、设备或采集批次分组，防止同源片段泄漏。

## 常见误区

- **随机交叉验证到处适用。** 时间预测必须尊重部署时的信息边界。
- **未来外生变量默认已知。** 天气预报与事后真实天气不是同一输入。
- **时间序列必须用 Transformer。** 有限数据与强季节任务中，统计模型是必要比较对象。
- **一次时间段胜出就始终有效。** 回测窗口与制度变化都可能改变排序。
- **预测相关性可以直接指导干预。** 预测销量不等于估计促销的因果效果。

下一步：回到 [数据质量](03-data.md) 检查时间字段，或在 [机器学习](04-machine-learning.md) 中补验证与误差分析。

---

资源核实：2026-09-30；已审阅推荐入口的介绍、目录或相关正文，未声明逐课完成或逐项运行。算力为本页练习建议，详见[核实记录](../research/foundations-sources.md)。

[返回知识地图](../map.md) · [选择学习路线](../roadmaps/README.md)


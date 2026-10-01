# 01 · 数学基础

> 目标：读懂常见模型的公式、检查维度、解释优化过程，并能用小实验验证结论。先修：高中代数与函数；代码练习可和 [编程基础](02-programming.md) 并行。建议规划 **100–180 小时**，用于主教材、推导练习和一个项目；补先修另计，不等于掌握全部 AI 数学。纸笔与普通 CPU 即可。

## 资源列表

先选一条主线：中文快入门选 D2L；想系统补数学选 MML，卡住的部分再查 MIT 或 Stat 110。**不需要同时修完六份材料。**“免费”指推荐的公开内容；纸书、证书或云算力可能另收费。

- **[Mathematics for Machine Learning](https://mml-book.github.io/)**｜英文 · 进阶 · 免费 · CPU。以机器学习问题连接数学；先读第 2–7 章，再做线性回归与 PCA notebook。
- **[MIT 18.06 Linear Algebra](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)**｜英文 · 入门 · 免费 · 无。建立矩阵几何直觉；选线性方程组、子空间、正交投影和特征值，配习题。
- **[MIT 18.01SC Single Variable Calculus](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/)**｜英文 · 入门 · 免费 · 无。补导数与优化；先读 Differentiation 和 Applications，积分按需补。
- **[Harvard Stat 110](https://stat110.hsites.harvard.edu/)**｜英文 · 入门 · 免费 · 无。练概率推理；优先条件概率、随机变量、期望和常见分布。
- **[Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/)**｜英文 · 研究 · 免费 · CPU。作为深入优化的参考；读凸集、凸函数和无约束优化，暂缓对偶细节。
- **[动手学深度学习：预备知识](https://zh.d2l.ai/chapter_preliminaries/index.html)**｜中文 · 入门 · 免费 · CPU。用张量代码复核数学；选 2.3–2.6 的线性代数、微积分、自动微分和概率。

### 补充课程与实作资源

| 资源 | 语言 · 难度 | 获取 · 算力 | 用法与阅读范围 |
|---|---|---|---|
| [3Blue1Brown · Linear Algebra](https://www.3blue1brown.com/?topic=linear-algebra) | 英文 · 入门 | 免费 · 无 | 视频补几何直觉；配合主教材学习向量、线性变换、矩阵乘法和特征值，不能替代习题。 |
| [Seeing Theory](https://seeing-theory.brown.edu/) | 英文 · 入门 | 免费 · CPU | 用概率、条件概率、分布与贝叶斯推断交互页面辅助理解；站点已归档，作为补充。 |

以上新增入口核实于 2026-10-01；资料免费不含硬件与 API 费用。

## 按资源安排学习顺序

主教材选 MML；偏中文可用 D2L 预备知识起步。MIT、Stat 110 用来补薄弱项，凸优化留到进阶。

按顺序完成主线，每步完成右列产出后再推进；选修不计入必做清单。页首时长包含所选主线、练习与本页项目，不包含把全部资料逐一学完。

| 阶段 | 使用资源 | 阅读 / 练习范围 | 完成后应留下什么 |
|---|---|---|---|
| 1 · 线性代数 | [Mathematics for Machine Learning](https://mml-book.github.io/)；[3Blue1Brown · Linear Algebra](https://www.3blue1brown.com/?topic=linear-algebra) | MML 第 2–4 章；遇到几何直觉困难时看对应视频 | 手算矩阵乘法，画二维线性变换，完成所选章习题 |
| 2 · 微积分 | [Mathematics for Machine Learning](https://mml-book.github.io/)；[MIT 18.01SC Single Variable Calculus](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/) | MML 向量微积分；导数不熟时补 MIT Differentiation | 独立推导线性回归梯度，并用差分验证 |
| 3 · 概率 | [Mathematics for Machine Learning](https://mml-book.github.io/)；[Harvard Stat 110](https://stat110.hsites.harvard.edu/)；[Seeing Theory](https://seeing-theory.brown.edu/) | MML 概率部分；按条件概率、随机变量、期望选 Stat 110 和交互例子 | 写采样实验，解释样本量改变后的波动 |
| 4 · 连接代码 | [动手学深度学习：预备知识](https://zh.d2l.ai/chapter_preliminaries/index.html)；[Mathematics for Machine Learning](https://mml-book.github.io/) | D2L 2.3–2.6；MML 数值优化与线性回归 | 完成下方回归任务；应用路线可在此转 ML |
| 选修 · 优化理论 | [Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/) | 凸集、凸函数、无约束优化 | 写清适用假设；不要求读完全书 |

## 实践任务与验收

**任务 A：二维线性回归实验。** 自己生成 200 个样本，保留真实参数；分别用梯度下降和数值最小二乘求解器拟合。不要显式计算矩阵逆来作为默认数值实现。

- [ ] 写清 \(X\)、\(w\)、\(y\)、残差和梯度的形状。
- [ ] 用中心差分检查一个参数梯度；双精度、合适步长下与解析梯度接近，并解释误差来自哪里。
- [ ] 比较三种学习率，画出损失曲线；能解释发散或收敛变慢。
- [ ] 将一个特征放大 1000 倍，再标准化，记录训练变化。

**任务 B：概率模拟。** 模拟硬币或骰子，比较 20、200、2000 次样本的均值波动；用重复实验区分“单次估计很接近”与“方法总体稳定”。验收是写出一段自己的解释，而不是只交图。

## 常见误区

- **会背公式等于理解。** 至少给每个公式一个小数值例子和一条适用假设。
- **相关意味着因果。** 条件预测不自动回答干预后会发生什么。
- **凸优化教材能解释所有神经网络训练。** 神经网络通常非凸，不能照搬全局最优保证。
- **浮点计算就是实数计算。** 极小步长、极大指数和显式求逆都可能引入数值问题。

下一步：完成 [编程基础](02-programming.md) 后进入 [机器学习](04-machine-learning.md)；已有编程经验可直接做线性模型实验。

---

资源核实：2026-09-30；已审阅推荐入口的介绍、目录或相关正文，未声明逐课完成或逐项运行。算力为本页练习建议，详见[核实记录](../research/foundations-sources.md)。

[返回知识地图](../map.md) · [选择学习路线](../roadmaps/README.md)

# 16 · 硬件与系统基础

> 目标：能沿着“磁盘 → 内存 → CPU → 加速器 → 网络”解释一次训练或推理的时间花在哪里，并用测量选择优化方向。先修：Python、数组与张量、基本命令行；少量 C 有帮助。学习规划预算约 120–220 小时。普通电脑即可完成。
> 时间口径：具备先修后，系统学习主教材、完成练习与一个项目的规划预算；不包含补先修，也不等于掌握整个领域。实际投入受基础、实验条件和项目深度影响。

## 资源列表

以下费用描述指阅读材料；硬件与云服务费用另计。核验日期：2026-09-30。

| 资源 | 语言 / 级别 / 费用 / 条件 | 重点学什么、为何选它 |
| --- | --- | --- |
| [CS:APP 作者站](https://csapp.cs.cmu.edu/) | 英文 / 进阶 / 部分免费 / CPU | 数据表示、缓存、虚拟内存、并发；从程序员视角串起系统。作者站与部分配套材料免费，教材通常需购买或借阅。 |
| [Operating Systems: Three Easy Pieces](https://pages.cs.wisc.edu/~remzi/OSTEP/) | 英文 / 入门 / 免费 / CPU | 进程、地址空间、并发、持久化；章节 PDF 和模拟题能把抽象机制变成可验证问题。 |
| [Stanford CS144](https://cs144.github.io/) | 英文 / 进阶 / 免费 / CPU | 字节流、可靠传输、拥塞与网络实验；理解网络为什么有等待和尾延迟。完整实验需 C++，先选读网络基础。 |
| [Brendan Gregg：Linux Performance](https://www.brendangregg.com/linuxperf.html) | 英文 / 进阶 / 免费 / CPU | USE 方法、工具地图和火焰图入口；先提出瓶颈假设，再找工具。Linux 工具不一定适用于 macOS。 |
| [Linux 内核：内存概念](https://docs.kernel.org/admin-guide/mm/concepts.html) | 英文 / 进阶 / 免费 / CPU | NUMA、页缓存、匿名内存与回收；纠正把虚拟内存、驻留内存混为一谈的误区。 |
| [Apache Parquet Overview](https://parquet.apache.org/docs/overview/) | 英文 / 入门 / 免费 / CPU | 列式存储、格式与实现的关系；给数据管线选型补上存储知识。 |

### 补充课程与实作资源

| 资源 | 语言 · 难度 | 获取 · 算力 | 用法与阅读范围 |
|---|---|---|---|
| [Machine Learning Systems](https://mlsysbook.ai/) | 英文 · 进阶 | 免费 · CPU | 用基础卷建立系统视角，规模化卷按问题查阅；教材、实验和硬件实践分开选择。 |
| [How to Scale Your Model](https://jax-ml.github.io/scaling-book/) | 英文 · 进阶 | 免费 · 无 | 先 Roofline，再训练并行与推理部分；用题目练内存、通信和延迟估算，注意 TPU 与 GPU 差异。 |

以上新增入口核实于 2026-10-01；资料免费不含硬件与 API 费用。

## 按资源安排学习顺序

MLSysBook 建立全局视角，OSTEP 或 CS:APP 补系统基础。网络和底层内存按实际瓶颈深入。

按顺序完成主线，每步完成右列产出后再推进；选修不计入必做清单。页首时长包含所选主线、练习与本页项目，不包含把全部资料逐一学完。

| 阶段 | 使用资源 | 阅读 / 练习范围 | 完成后应留下什么 |
|---|---|---|---|
| 1 · 系统概览 | [Machine Learning Systems](https://mlsysbook.ai/) | 基础卷的系统、数据与部署相关主题 | 画出数据到模型服务的路径 |
| 2 · CPU 与内存 | [CS:APP 作者站](https://csapp.cs.cmu.edu/)；[Operating Systems: Three Easy Pieces](https://pages.cs.wisc.edu/~remzi/OSTEP/)；[Linux 内核：内存概念](https://docs.kernel.org/admin-guide/mm/concepts.html) | CS:APP 缓存/虚拟内存，或 OSTEP 虚拟化与并发；内核文档查概念 | 测顺序/随机访问与并发读取 |
| 3 · 数据和网络 | [Apache Parquet Overview](https://parquet.apache.org/docs/overview/)；[Stanford CS144](https://cs144.github.io/) | Parquet 概览；CS144 可靠传输选读 | 测本地数据读取，解释网络延迟进入哪个阶段 |
| 4 · 性能证据 | [Brendan Gregg：Linux Performance](https://www.brendangregg.com/linuxperf.html)；[How to Scale Your Model](https://jax-ml.github.io/scaling-book/) | Linux Performance 工具方法；Scaling Book Roofline | 完成下方瓶颈报告与资源估算 |

## 实践：找出一个数据管线的瓶颈

创建小规模合成数据，初次实验控制在数百 MB 内。无需下载模型，也不需要购买 GPU。

1. 写一个“读取 → 解析 → 简单数值计算 → 汇总”的脚本，分别记录每阶段墙钟时间、输入字节数与样本数。
2. 固定总数据量，比较一个大文件和多个小文件；记录文件数量与文件大小，避免只记录一句“更快了”。
3. 对同一输入重复运行，区分首次运行与后续运行。不要为了测冷缓存而随意执行系统级清缓存命令；将缓存影响写进限制说明即可。
4. 比较串行和 2、4 个 worker。保持输入与结果一致，观察哪一阶段变快、哪一阶段恶化。
5. 提交一页报告：实验条件、阶段耗时表、一个瓶颈判断、一项修改、修改前后数据，以及一个无收益的尝试。

**验收**：输出结果一致；每种配置至少运行 5 次并报告中位数；能用计算解释理论搬运下界；能指出至少一种结果受到缓存、并发或系统负载影响的可能性。无需达到固定加速倍数。

## 常见误区与下一步

- “CPU 使用率低说明 CPU 没问题”：进程可能在等 I/O、锁或单个线程，需结合等待状态。
- “内存越少越好”：缓存占用可能在帮忙；要区分可回收缓存与不可控增长。
- “并行一定更快”：把序列化开销和数据复制算进去再比较。
- “微基准提升就是业务提升”：最终回到整个任务的完成时间和资源成本。

继续学习 [GPU、算子与编译器](17-gpu-kernels-compilers.md)，将同样的“计算与搬运”思路用于加速器；应用工程方向可接着看 [MLOps](20-mlops.md)。

[返回知识地图](../map.md) · [选择学习路线](../roadmaps/README.md)

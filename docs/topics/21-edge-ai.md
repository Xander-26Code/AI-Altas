# 21 · 端侧、移动端与浏览器 AI

> 目标：把一个小模型放到目标设备上，验证离线可用、数值行为、内存与延迟，并说明哪些数据会离开设备。先修：模型推理、张量形状、量化基础；选择浏览器路线需 JavaScript，移动端路线需对应平台基础。学习规划预算约 80–160 小时。普通电脑可完成 ONNX/浏览器主线；手机或 Apple Silicon 是相应扩展路线的条件。
> 时间口径：具备先修后，系统学习主教材、完成练习与一个项目的规划预算；不包含补先修，也不等于掌握整个领域。实际投入受基础、实验条件和项目深度影响。

## 资源列表

核验日期：2026-09-30；文档免费，目标设备与模型下载流量另计。

| 资源 | 语言 / 级别 / 条件 | 建议范围与理由 |
| --- | --- | --- |
| [ONNX Runtime：Deploy on Mobile](https://onnxruntime.ai/docs/tutorials/mobile/) | 英文 / 进阶 / CPU | 选择执行后端、测量与优化；从 CPU 基线过渡到具体手机，强调实测而非宣传峰值。 |
| [MLX 官方文档](https://ml-explore.github.io/mlx/build/html/index.html) | 英文 / 进阶 / 可选GPU | Quick Start、Lazy Evaluation、Unified Memory；Apple Silicon 路线重点阅读，运行前核对目标平台。 |
| [Transformers.js：WebGPU](https://huggingface.co/docs/transformers.js/en/guides/webgpu) | 英文 / 进阶 / 可选GPU | 设备选择和 pipeline 示例；快速理解浏览器内模型的加载与执行。网页中的历史浏览器占比不可当作当前统计。 |
| [Google LiteRT Overview](https://developers.google.com/edge/litert/overview) | 英文 / 进阶 / 可选GPU | 转换、CompiledModel、设备加速与示例；官方端侧路线入口，按目标设备选择 API。 |
| [Core ML Tools 概览](https://apple.github.io/coremltools/docs-guides/source/overview-coremltools.html) | 英文 / 进阶 / 可选GPU | 转换第三方模型、验证与优化；适合 Apple 应用交付，运行验证需相应平台。 |
| [ONNX Runtime Web](https://onnxruntime.ai/docs/tutorials/web/) | 英文 / 入门 / CPU | WASM、WebGPU、WebNN 以及客户端/服务端选型；浏览器部署前应先读的兼容性入口。 |

### 补充课程与实作资源

| 资源 | 语言 · 难度 | 获取 · 算力 | 用法与阅读范围 |
|---|---|---|---|
| [Machine Learning Systems](https://mlsysbook.ai/) | 英文 · 进阶 | 免费 · CPU | 用基础卷建立系统视角，规模化卷按问题查阅；教材、实验和硬件实践分开选择。 |
| [MIT 6.5940 · TinyML and Efficient Deep Learning Computing (2024)](https://hanlab.mit.edu/courses/2024-fall-65940) | 英文 · 进阶 | 免费 · 可选GPU | 固定 2024 课程入口；选剪枝、量化与部署主题的讲义和作业，做精度、延迟和模型大小对照。 |

以上新增入口核实于 2026-10-01；资料免费不含硬件与 API 费用。

## 按资源安排学习顺序

按目标设备选择一套运行时，不需要同时学习浏览器、手机和 Apple 平台。MLSysBook 和 MIT 课程提供共同方法。

按顺序完成主线，每步完成右列产出后再推进；选修不计入必做清单。页首时长包含所选主线、练习与本页项目，不包含把全部资料逐一学完。

| 阶段 | 使用资源 | 阅读 / 练习范围 | 完成后应留下什么 |
|---|---|---|---|
| 1 · 设备约束 | [Machine Learning Systems](https://mlsysbook.ai/)；[MIT 6.5940 · TinyML and Efficient Deep Learning Computing (2024)](https://hanlab.mit.edu/courses/2024-fall-65940) | 端侧部署、量化相关材料 | 写内存、延迟、功耗、离线能力预算 |
| 2 · 运行时分支 | [ONNX Runtime：Deploy on Mobile](https://onnxruntime.ai/docs/tutorials/mobile/)；[MLX 官方文档](https://ml-explore.github.io/mlx/build/html/index.html)；[Transformers.js：WebGPU](https://huggingface.co/docs/transformers.js/en/guides/webgpu)；[Google LiteRT Overview](https://developers.google.com/edge/litert/overview)；[Core ML Tools 概览](https://apple.github.io/coremltools/docs-guides/source/overview-coremltools.html)；[ONNX Runtime Web](https://onnxruntime.ai/docs/tutorials/web/) | 手机选 ONNX Mobile/LiteRT；Apple 选 Core ML/MLX；浏览器选 ORT Web/Transformers.js | 只选一条，加载模型并跑基线 |
| 3 · 精度与性能 | [MIT 6.5940 · TinyML and Efficient Deep Learning Computing (2024)](https://hanlab.mit.edu/courses/2024-fall-65940) | 量化与部署相关作业 | 固定样本和设备比较原模型与优化模型 |
| 4 · 实际交付 | [ONNX Runtime：Deploy on Mobile](https://onnxruntime.ai/docs/tutorials/mobile/)；[Core ML Tools 概览](https://apple.github.io/coremltools/docs-guides/source/overview-coremltools.html)；[ONNX Runtime Web](https://onnxruntime.ai/docs/tutorials/web/) | 回到所选运行时的部署说明 | 完成下方离线实验，记录回退和设备差异 |

## 实践：一个可断网使用的轻量分类器

不必从聊天大模型开始。选择图像、文本或表格分类中的一种，模型体积目标先控制在数十 MB 内；也可以使用自己训练的极小模型。

1. 定义输入格式、归一化/tokenization 和输出类别，保存 50–100 条固定测试样本及参考输出。
2. 导出为目标运行时支持的格式。逐条比较原模型与导出模型，记录容差、预测差异与可能原因。
3. 建立 CPU 运行基线，再选择一个加速后端或量化版本。每次只改变一项，保持前后处理一致。
4. 分别测首次下载、模型加载、第一条推理、后续推理的 p50/p95；至少连续运行数分钟，观察温度或系统负载导致的延迟变化。
5. 在资源已准备后断网，确认核心功能可用；记录任何被尝试的网络访问。提供清除本地模型/缓存的办法。
6. 测试不支持加速后端、模型文件缺失、加载被取消和内存不足时的行为；给出可理解的状态反馈与回退路径。

**验收**：固定样本质量达到事先设定的门槛；报告模型大小与运行峰值内存，区分冷启动和稳态；至少一条 CPU/低能力设备回退路径可运行；断网后核心功能成立，并写明仍需网络的操作。手机扩展须在真实目标设备测试，桌面模拟器不能替代功耗与散热测量。

## 常见误区与下一步

- “导出通过就是部署通过”：算子支持、动态形状、预处理和设备后端仍可能出错。
- “NPU 峰值高就一定更快”：图切分、数据拷贝和小 batch 的启动成本会改变结果。
- “一次推理很快就足够”：首次体验、持续运行、内存释放和电量同样决定可用性。
- “本地运行就没有隐私问题”：日志、缓存和云端回退也属于产品的数据路径。

用 [MLOps](20-mlops.md)管理模型版本、发布和质量门槛；想进一步理解后端为何快或慢，回到 [GPU、算子与编译器](17-gpu-kernels-compilers.md)。

[返回知识地图](../map.md) · [选择学习路线](../roadmaps/README.md)

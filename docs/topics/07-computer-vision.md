# 07 · 计算机视觉：从像素到空间理解

> 目标：理解图像数据、卷积与视觉任务，完成一个可复核的分类或检测项目。先修：[数学](01-math.md)、[数据](03-data.md)、[深度学习](05-deep-learning.md)。**规划预算：100–180 小时**，用于完成先修后系统学习主教材、做练习并完成一个项目；不含补先修，不是领域掌握承诺。图像处理可用 CPU，训练建议根据模型选择 GPU。

## 资源列表

CS231n 作为深度视觉主线，Szeliski 补几何基础，OpenCV 负责图像操作。Szeliski 作者提供个人使用电子版，需填写下载信息，不能把 PDF 复制进本仓库。大型训练的算力需求应另行评估。

- **[Stanford CS231n](https://cs231n.stanford.edu/)**｜英文 · 进阶 · 部分免费 · 可选GPU。作深度视觉主线；从分类和 CNN 到检测，完成公开作业中的小模型。
- **[Computer Vision: Algorithms and Applications](https://szeliski.org/Book/)**｜英文 · 进阶 · 免费 · CPU。补几何与经典视觉；选图像形成、特征、匹配和多视几何，深度内容按需看。
- **[TorchVision Object Detection Finetuning Tutorial](https://docs.pytorch.org/tutorials/intermediate/torchvision_tutorial.html)**｜英文 · 进阶 · 免费 · 可选GPU。把检测任务落到数据接口；完成 Penn-Fudan 上的 Mask R-CNN 微调及结果可视化。
- **[OpenCV-Python Tutorials](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)**｜英文 · 入门 · 免费 · CPU。掌握图像读写与坐标；先做 Core Operations、Image Processing，再学特征。
- **[timm Quickstart](https://huggingface.co/docs/timm/quickstart)**｜英文 · 进阶 · 免费 · 可选GPU。比较预训练骨干；读模型加载、分类头替换、特征抽取及匹配预处理。
- **[Detectron2 Tutorials](https://detectron2.readthedocs.io/en/latest/tutorials/index.html)**｜英文 · 进阶 · 免费 · GPU。进阶了解检测工程；先读数据注册、配置、训练和评估，注意依赖版本配套。

## 按资源安排学习顺序

CS231n 为深度视觉主课，OpenCV 补图像操作。检测、几何、模型库按项目选择。

按顺序完成主线，每步完成右列产出后再推进；选修不计入必做清单。页首时长包含所选主线、练习与本页项目，不包含把全部资料逐一学完。

| 阶段 | 使用资源 | 阅读 / 练习范围 | 完成后应留下什么 |
|---|---|---|---|
| 1 · 图像操作 | [OpenCV-Python Tutorials](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html) | Core Operations、Image Processing | 记录颜色通道、缩放、坐标与变换 |
| 2 · 分类主线 | [Stanford CS231n](https://cs231n.stanford.edu/) | 分类、CNN、训练及对应公开作业 | 建立可复现图像分类基线 |
| 3 · 迁移学习 | [timm Quickstart](https://huggingface.co/docs/timm/quickstart) | 模型加载、分类头、预处理与特征抽取 | 固定切分比较两种预训练骨干 |
| 4 · 检测分支 | [TorchVision Object Detection Finetuning Tutorial](https://docs.pytorch.org/tutorials/intermediate/torchvision_tutorial.html) | 完整 Penn-Fudan 微调与评估教程 | 只做分类者可跳过；检测者交付预测与误差报告 |
| 选修 · 专项深化 | [Computer Vision: Algorithms and Applications](https://szeliski.org/Book/)；[Detectron2 Tutorials](https://detectron2.readthedocs.io/en/latest/tutorials/index.html) | 几何问题查 Szeliski；检测工程查 Detectron2 | 按一个具体问题补读 |

## 实践任务与验收

选择一个小型分类数据集或 TorchVision 的 Penn-Fudan 检测/分割示例，做完整实验。使用教程数据时标明来源，换自己的数据时先审查标注质量与授权。

- [ ] 可视化至少 30 个原始和增强样本，确认类别、框、掩码与图像一致。
- [ ] 说明切分单位；相同对象、近重复图像或同段视频不跨集合。
- [ ] 先跑简单分类或预训练基线，再做一个明确改动，例如冻结骨干与部分微调。
- [ ] 使用与预训练权重匹配的尺寸、像素范围和归一化；保存完整处理配置。
- [ ] 分类报告混淆矩阵与各类指标；检测报告 AP 的具体 IoU/平均协议。
- [ ] 检查小目标、遮挡、暗光和背景变化下的失败样本。
- [ ] 在新进程加载并预测，报告设备、batch size、输入分辨率与延迟统计。

进阶练习：同一张图片从模型输入坐标还原到原图坐标，验证框不会因缩放或补边而漂移。将这一步写成独立函数，用手算坐标检查。

## 常见误区

- **所有视觉任务都先随机裁剪。** 增强必须保留任务标签含义。
- **公开数据高分即可上线。** 实际摄像头、背景、光照和采集流程可能不同。
- **下载一个骨干就完成迁移学习。** 类别、输入处理与目标领域都需要核对。
- **视觉只有深度学习。** 成像、几何、信号处理仍是三维和测量任务的重要基础。

下一步：回到 [深度学习](05-deep-learning.md) 深入架构和训练；在[知识地图](../map.md)选择多模态、机器人或推理部署方向。

---

资源核实：2026-09-30；已审阅推荐入口的介绍、目录或相关正文，未声明逐课完成或逐项运行。算力为本页练习建议，详见[核实记录](../research/foundations-sources.md)。

[返回知识地图](../map.md) · [选择学习路线](../roadmaps/README.md)


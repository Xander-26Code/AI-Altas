# 路线 B · 算法工程

先修：能写 Python，理解矩阵、导数和基础概率，能使用 Git。规划 **450–750 小时**，每周 8–12 小时约 **9–22 个月**；不含补先修。目标是一份可以被别人复现和质疑的模型项目。

| 阶段 | 主线 | 投入 | 验收 | 主资源与范围 |
|---|---|---|---|---|
| 数据与统计基线 | [数据](../topics/03-data.md)、[机器学习](../topics/04-machine-learning.md) | 100–160 小时 | 数据说明、无泄漏的 pipeline、合理基线、分组误差 | [ISL](https://www.statlearning.com/) 回归/分类 lab → scikit-learn Pipeline、交叉验证；已有基础可换 [ML Zoomcamp](https://github.com/DataTalksClub/machine-learning-zoomcamp) |
| 训练基本功 | [深度学习](../topics/05-deep-learning.md) | 100–160 小时 | 过拟合小 batch、诊断梯度、学习率与正则对照 | [Zero to Hero](https://github.com/karpathy/nn-zero-to-hero) micrograd 与 makemore 梯度练习 → D2L 训练与正则选读 |
| 选择一个领域 | [CV](../topics/07-computer-vision.md)、[NLP](../topics/06-nlp.md)、[时序](../topics/08-time-series.md)、[推荐](../topics/23-recommendation-search.md) 四选一 | 120–200 小时 | 在固定预算与切分下比较两种方法 | CV：CS231n；NLP：CS224N；时序：FPP3；推荐：TFR + MovieLens。只选一个领域，按左列专题资源表推进 |
| 验证与交付 | [评估](../topics/15-evaluation-safety.md)、[MLOps](../topics/20-mlops.md) 选读 | 70–120 小时 | 重跑配置、误差切片、接口与回滚方案 | [MLOps Zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp) 实验追踪、部署、监控与 Best Practices；评估用专题中的模型卡模板 |
| 整理作品 | 复现实验和讲解 | 60–110 小时 | 让另一位读者按说明重跑并提出问题 | 回到所选课程的公开项目要求，整理自己的数据、消融、失败记录与重跑说明 |

## 主项目怎么选

选一个数据规模和标签定义可控的任务，例如小型图像分类、文本分类、时间序列预测或推荐排序。先写出数据可用时间、真实使用场景和指标。不要因为榜单热门，就在尚不理解评测协议时直接追分。

作品应包含至少一项有解释的消融、多个随机种子或合理的不确定性分析、失败样例和推理成本。结果没超过基线时，调查原因并报告，不必更换数据集直到“赢”为止。

下一步可选 [LLM 训练](llm.md)、[研究](research.md) 或 [Infra](infra.md)。这些分支共享部分基础，按成果复用，避免重复从头学习。

[全部路线](README.md) · [项目库](../projects/README.md)

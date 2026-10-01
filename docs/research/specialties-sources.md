# 交叉领域：来源核实记录

首次内容核实：2026-09-30；本轮结构、链接与措辞修订：2026-10-01。

对应 [强化学习](../topics/22-rl-robotics.md)、[推荐搜索](../topics/23-recommendation-search.md)、[图学习](../topics/24-graphs.md)、[因果概率](../topics/25-causal-probabilistic.md)、[AI for Science](../topics/26-ai-for-science.md)、[经典 AI](../topics/27-classical-ai.md)。33 条资源记录在 `data/resources-specialties.json`。

## 核实范围

逐一打开作者、课程、机构或项目页面，核对名称、主题、目录和公开入口。不是对全部教材或实验的复现声明。对软件页的阅读只确认学习入口，安装兼容性与模型训练还需在实际环境验证。

| 来源组 | 核对内容 |
|---|---|
| Silver、Gymnasium、CS285、MIT 控制课程 | 课程入口、MDP/模仿/离线 RL 与控制章节、环境终止接口 |
| LeRobot、RT-2、MuJoCo | 数据/策略/硬件接口、VLA 项目描述、仿真项目归属 |
| Stanford IR、TFRS、Faiss、MovieLens、TorchRec | 在线教材、召回排序示例、索引、数据条款与分片主题 |
| NetworkX、RDF、CS224W、PyG、OGB | 图结构、知识表示、课程、采样与官方 benchmark |
| ProbML、CS228、PyMC、What If、DoWhy、EconML | 作者开放资料、推断/识别/估计及诊断入口 |
| DeepChem、AlphaFold、DeePMD、DeepXDE、NeuralOperator | 科学任务、原仓库、数据依赖与数值方法分类 |
| AIMA、CS188、OR-Tools、Z3、DEAP | 教材目录、公开课程、约束求解与进化计算示例 |

## 调研中修正过的地址

- TorchRec 旧的 PyTorch 根路径返回 404，改为项目维护的 `meta-pytorch.org` 概览页。
- DeePMD 的旧路径未能正常读取，改为 DeepModeling 当前项目文档入口。
- CS188 使用已验证的 Fall 2024 归档地址，避免依赖课程根页的自动跳转。
- CS285 使用 Berkeley RAIL 课程主页；原猜测域名未能读取，不收录为推荐入口。
- Sutton 书籍作者页面本次访问超时，因此没有将它标成已读正文的推荐条目；RL 主线改用实际可读取的课程与官方资料。

这些更正针对实际访问结果，不代表未来永远可访问。网络结果与内容审阅分别记录，见 [质量记录](../quality.md)。

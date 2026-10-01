# GitHub 与 X 资源增补调研

检查日期：2026-10-01。本轮新增 25 个资源入口；不以帖子热度、仓库 Star 或“几周学会”的宣传作为排序依据。资源进入专题后，必须有适用读者、选读范围和学习阶段。

## GitHub 路线与资源库

| 查看入口 | 本轮参考与取舍 |
|---|---|
| [lvy010/AI-wiki](https://github.com/lvy010/AI-wiki) | 复看全栈范围，保留算法、应用与底层系统的并列入口。 |
| [mlabonne/llm-course](https://github.com/mlabonne/llm-course) | 参考基础、模型训练与应用工程分层；沿数学推荐核实 3Blue1Brown 和 Seeing Theory。 |
| [pacoxu/AI-Infra](https://github.com/pacoxu/AI-Infra) | 参考训练、推理与云原生系统的边界；按目标分支，不把生态图中所有项目变成必修。 |
| [DucLong06/ai-infra-roadmap](https://github.com/DucLong06/ai-infra-roadmap) | 搜索索引可读，直接抓取失败；由其资源列表发现 MLSysBook、GPU MODE、Scaling Book 和 MIT 高效计算课，随后分别打开作者入口。 |
| [dair-ai/ML-YouTube-Courses](https://github.com/dair-ai/ML-YouTube-Courses) | 用作视频课发现入口；课程仍回到大学或讲师主页核实。 |
| [DataTalks.Club ML Zoomcamp](https://github.com/DataTalksClub/machine-learning-zoomcamp) | 补足从传统 ML 到部署的工程课程选项；不沿用仓库宣传时长作为自学保证。 |
| [DataTalks.Club MLOps Zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp) | 选追踪、编排、部署、监控与最终项目；当前自学材料可用，不承诺直播或证书。 |
| [DataTalks.Club LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp) | 按检索、向量搜索、评估、监控串成应用路线；先做普通检索再扩展 Agent。 |
| [Datawhale Happy-LLM](https://github.com/datawhalechina/happy-llm) | 为 LLM 原理与训练提供中文主线，采用目录中的第 1–6 章范围。 |
| [Datawhale LLM Universe](https://github.com/datawhalechina/llm-universe) | 采用已完成的第一部分；进阶部分仍有在编内容，保留版本与 API 成本提示。 |
| [Datawhale Hello-Agents](https://github.com/datawhalechina/hello-agents) | 中文 Agent 主课选项，按基础、手写框架、记忆/协议、评估推进。 |
| [Awesome LLM Apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | 作为完成主课后的选题库，不用大量 demo 替代系统课程。 |

这些是编排判断，未复制他人的路线正文。新资源也包含沿上述线索找到的作者教材与官方教程，完整条目见 [资源目录](../resources.md)。

## X 发现线索与访问限制

检索了 Karpathy、Raschka、Hugging Face 和 GPU MODE 相关的课程、实现与推荐帖子。X 搜索覆盖不完整，多个直接帖子返回 403；无法读取的内容不标为“已读”，也不以第三方转载代替原帖核实。X 链接仅保留在这里作发现记录，学习主线使用下表中的作者仓库。

| 帖子线索 | 能确认什么 | 用于学习的入口 |
|---|---|---|
| [Raschka：有限算力的 LLM 项目](https://x.com/rasbt/status/1684902178509504512) | 搜索结果能读取作者、正文与日期；是 2023 年历史挑战，不作为当前报名或资源预算承诺 | 采用“小模型、明确任务”的项目范围，不添加比赛为主课 |
| [Raschka：偏好数据 notebook 线索](https://x.com/rasbt/status/1817210266838339916) | 原帖 403；已核实作者仓库存在相应文件，未运行 notebook | [作者的偏好数据示例](https://github.com/rasbt/LLMs-from-scratch/blob/main/ch07/04_preference-tuning-with-dpo/create-preference-data-ollama.ipynb)，微调进阶查阅 |
| [Raschka：DPO 实现线索](https://x.com/rasbt/status/1820096879440662972) | 原帖 403；已核实作者仓库文件入口；网页工具未展开完整 notebook 内容 | [DPO notebook](https://github.com/rasbt/LLMs-from-scratch/blob/main/ch07/04_preference-tuning-with-dpo/dpo-from-scratch.ipynb)，作为主仓库的补充入口 |
| [Raschka：生成与 KV cache 视频线索](https://x.com/rasbt/status/2096596372661113294) | 原帖 403，不能核实视频全文；独立查看了作者 KV cache 目录说明 | [KV cache 实现目录](https://github.com/rasbt/LLMs-from-scratch/tree/main/ch04/03_kv-cache)，加入 LLM 与推理学习计划 |

没有从受限帖子中补写作者观点或推荐排名。Karpathy 的课程则直接核对了 [Zero to Hero 仓库](https://github.com/karpathy/nn-zero-to-hero) 的课程顺序和 notebook 入口。

## 新资源如何安排

| 学习需求 | 新增材料的角色 |
|---|---|
| 数学直觉 | 3Blue1Brown、Seeing Theory 辅助主教材；不替代推导和习题 |
| Python 与数据 | Python for Data Analysis 用于表格实践；Data Engineering Zoomcamp 是工程选修 |
| 传统 ML 与深度学习 | ML Zoomcamp、Hands-On ML 作为替代主线；NNDL 作中文理论参考；Zero to Hero 练手写实现 |
| LLM 与微调 | Raschka 与 Happy-LLM 按语言和学习方式择一；smol course 串起 SFT、评估和偏好对齐 |
| 应用与 Agent | LLM Universe / LLM Zoomcamp 择一；Hello-Agents / HF Agents / Microsoft Agents 择一 |
| 系统与部署 | MLSysBook 补全局，GPU MODE 练算子，Scaling Book 练性能估算，MIT 课程补高效计算，MLOps Zoomcamp 串项目 |
| 强化学习 | Spinning Up 补算法与实验方法；RL Baselines3 Zoo 提供可复现实验配置参考 |

这些资源并不需要全部学完。学习预算仍按所选主线、练习与一个项目估计，新增选修不能被理解为已包含在原预算内。

[返回调研总览](README.md) · [选择学习路线](../roadmaps/README.md)

"""Build the knowledge map and resource index from their reviewed source records."""
import argparse
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def render():
    topics = json.loads((ROOT / 'data/topics.json').read_text())
    titles = {t['slug']: t['title'] for t in topics}
    by_url = {}
    for path in sorted((ROOT / 'data').glob('resources-*.json')):
        for record in json.loads(path.read_text()):
            url = record['url']
            if url not in by_url:
                by_url[url] = dict(record)
            else:
                by_url[url]['topics'] = sorted(set(by_url[url]['topics'] + record['topics']))
    records = list(by_url.values())
    groups = defaultdict(list)
    for topic in topics:
        groups[topic['group']].append(topic)

    def topic_link(slug):
        return f"[{titles[slug]}](topics/{slug}.md)"

    knowledge = ['# AI 知识地图', '',
        '27 个专题按学习关系组织。先修列是建议，不是入学要求；能完成自测和实践时，可以跳过已掌握的部分。每个专题先列资源，再给出对应课程、阅读范围与练习的学习计划。', '',
        '![基础、模型、应用与系统](assets/atlas.svg)', '',
        '## 怎么走', '',
        '- 基础路线：编程与数学 → 数据与机器学习 → 深度学习 → 一个领域项目。',
        '- 应用路线：编程 → 模型接口 → 检索与 RAG → 工具工作流 → 评估与运维。',
        '- 系统路线：编程与训练基础 → 硬件系统 → 算子 / 分布式 / 推理主攻 → 生产验证。',
        '', '具体阶段与时间预算见 [学习路线](roadmaps/README.md)。', '']
    for group, entries in groups.items():
        knowledge += [f'## {group}', '', '| 专题 | 核心内容 | 建议先修 |', '|---|---|---|']
        for topic in entries:
            prereq = '、'.join(topic_link(s) for s in topic['prerequisites']) or '从这里开始'
            knowledge.append(f"| {topic['slug'][:2]} · {topic_link(topic['slug'])} | {topic['summary']} | {prereq} |")
        knowledge.append('')
    knowledge += ['## 当前覆盖深度', '',
        '所有 27 个入口均提供学习导读与资源；仓库内可运行实验只有回归、检索、attention 和显存估算四项。微调、GPU、分布式、机器人与科学计算实验需要按任务书或外部课程另行完成。', '',
        '| 相关方向 | 当前入口 | 尚未单独展开的部分 |', '|---|---|---|',
        '| 语音、音乐、视频、3D | [生成与多模态](topics/10-generative-multimodal.md)、[视觉](topics/07-computer-vision.md) | 独立音频课程、实时视频工程和空间重建完整路线 |',
        '| 联邦学习、隐私计算、可解释性 | [安全](topics/15-evaluation-safety.md)、[端侧](topics/21-edge-ai.md)、[因果](topics/25-causal-probabilistic.md) | 差分隐私推导、密码协议与联邦训练实作 |',
        '| AutoML、元学习、持续学习 | [机器学习](topics/04-machine-learning.md)、[深度学习](topics/05-deep-learning.md) | 独立算法课程和灾难性遗忘实验 |',
        '| 医疗、金融、法律、教育等行业 AI | [AI for Science](topics/26-ai-for-science.md)、[评估](topics/15-evaluation-safety.md) | 行业规范、领域知识与真实部署验证，不能仅靠通用 AI 课程替代 |',
        '| 多智能体博弈、神经符号、进化计算 | [强化学习](topics/22-rl-robotics.md)、[经典 AI](topics/27-classical-ai.md) | 研究级专题与更多可运行案例 |', '',
        '这些是后续可扩展方向，不作为已经完成的独立课程宣传。贡献新分支时，先补先修、主教材、实践与验收，再加入目录。', '',
        '[资源目录](resources.md) · [项目任务](projects/README.md) · [调研与来源](research/README.md)', '']
    catalog = ['---', 'hide:', '  - toc', '---', '', '# 精选资源目录', '',
        f'当前收录 **{len(records)} 个不同 URL 的资源入口**。一个资源可能对应多个专题；这不是课程数量或已完成实验数量。优先一手来源，具体阅读范围在各专题说明。', '',
        '语言、难度、费用和计算标签是学习建议。免费阅读不包含算力、证书、硬件或再分发权；`content-reviewed` 表示查看过对应页面，不表示读完全部资料。链接检查结论见 [质量记录](quality.md)。', '',
        '<div id="resource-explorer" data-catalog-url="assets/resources.json" hidden></div>', '',
        '<div id="resource-fallback" markdown>', '',
        '## 按专题查找', '']
    for topic in topics:
        selected = [r for r in records if topic['slug'] in r['topics']]
        catalog += [f"### {topic['slug'][:2]} · {topic['title']}", '',
                    f"阅读顺序与实践：{topic_link(topic['slug'])}。", '',
                    '| 资源 | 语言 · 级别 | 费用 · 算力 | 推荐理由 |', '|---|---|---|---|']
        for r in selected:
            why = r['why'].replace('|', '\\|').replace('\n', ' ')
            catalog.append(f"| [{r['title']}]({r['url']}) | {r['language']} · {r['level']} | {r['access']} · {r['compute']} | {why} |")
        catalog.append('')
    catalog += ['</div>', '', '[知识地图](map.md) · [调研记录](research/README.md)', '']
    payload = dict(topics=topics, resources=records)
    outputs = {ROOT/'docs/map.md':'\n'.join(knowledge), ROOT/'docs/resources.md':'\n'.join(catalog),
               ROOT/'docs/assets/resources.json':json.dumps(payload,ensure_ascii=False,indent=2)+'\n'}
    # Copies make dataset links work in both GitHub and the generated docs site.
    for path in sorted((ROOT / 'data').glob('resources-*.json')):
        outputs[ROOT/'docs/assets/data'/path.name] = path.read_text(encoding='utf-8')
    return outputs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    outdated = []
    for path, content in render().items():
        if args.check:
            if not path.exists() or path.read_text() != content:
                outdated.append(str(path.relative_to(ROOT)))
        else:
            path.parent.mkdir(parents=True,exist_ok=True)
            path.write_text(content,encoding='utf-8')
    if outdated:
        raise SystemExit('Generated files need updating: ' + ', '.join(outdated))
    print('Catalog is current' if args.check else 'Built map, Markdown catalog and browser catalog')


if __name__ == '__main__':
    main()

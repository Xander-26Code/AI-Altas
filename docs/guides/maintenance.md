# 维护、校验与发布

GitHub 阅读入口是根目录 `README.md`。所有文档使用仓库内相对路径；文件必须随提交一起上传，不能只复制 README。文件名大小写与路径必须完全一致，Windows/macOS 上能打开不代表 GitHub 的路径也正确。

## 日常修改流程

1. 在 `docs/topics/` 修改专题；对应资源写入 `data/resources-*.json`，专题分类与先修关系写入 `data/topics.json`。
2. 运行 `python3 scripts/build_catalog.py` 更新知识地图、资源目录及浏览器数据。
3. 运行离线校验与实验测试：

```bash
python3 scripts/check_content.py
python3 scripts/build_catalog.py --check
python3 -m unittest discover -s tests -v
```

4. 在文档环境里运行 `python -m mkdocs build --strict`，再运行 `python3 scripts/check_site_links.py` 检查生成站点的实际跳转。
5. 有网络时运行 `python3 scripts/check_external_links.py`。它逐一访问 Markdown、图片与资源目录的外部 URL，保留重定向和未确认结果。403/429 或连接失败需复核，不等于确认失效，也不能当作通过。

代码块中的命令不是可点击链接，不会被当成网页抓取。外部网页的 fragment、登录后的材料、视频播放、课程作业和重定向后的付费边界不能仅凭 HTTP 状态证明，需在内容核实记录中说明。

## 本地阅读

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-docs.txt
python scripts/build_catalog.py
python -m mkdocs serve -a 127.0.0.1:8000
```

在浏览器输入 `http://127.0.0.1:8000`。Windows PowerShell 使用 `.venv\Scripts\Activate.ps1`。文档站提供中文搜索与资源筛选；资源筛选需要通过 HTTP 访问，直接打开本地 HTML 时仍可使用 Markdown 资源表。数学公式的增强渲染需要联网加载 MathJax。

## 发布前检查

- 执行 `git status --short`，确认新增页面、SVG、脚本和生成目录数据均已包含在准备提交的文件里。
- 确认 README 所写的功能已存在；高级项目只是任务书时要明确说明。
- 选择正式许可证并保留第三方署名。当前许可证仍未选定。
- 阅读 `.github/workflows/checks.yml` 的检查结果；外链网络波动单独记录。
- 通过之后再将修改提交和推送到自己的 GitHub 仓库；本地修复不会自动更新 GitHub。

本仓库附带检查流程，没有自动部署步骤。静态输出在 `site/`；如果未来决定发布在线站点，再设置站点 URL 与对应托管流程。

[质量记录](../quality.md) · [贡献指南](../contributing.md)

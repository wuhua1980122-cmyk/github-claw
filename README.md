# 🦞 GitHub Claw — AI Agent 养成实验

> 通过 GitHub Copilot 网页版，从零打造一个具备角色、记忆和技能的个人 AI 助手。
> 
> 🌐 **在线访问**: https://wuhua1980122-cmyk.github.io/github-claw/

## 📋 项目概览

本项目是一次 AI Agent 构建实验，核心思路是：
> **"用 GitHub 仓库作为 AI 的工作空间，用 Copilot 作为交互界面，以 AGENTS.md + MEMORY.md + skills/ 作为记忆和能力的载体。"**

## 🏗️ 项目结构

```
github-claw/
├── AGENTS.md                  # AI 助手的角色设定与工作流
├── MEMORY.md                  # 长期记忆与经验积累
├── .github/workflows/         # GitHub Actions 配置
│   ├── pages.yml              # GitHub Pages 自动部署
│   ├── auto-reply.yml         # Issue 自动回复
│   └── daily-digest.yml       # 每日科技日报
├── projects/
│   ├── ai-guide/              # AI 知识导航网站 (SEO优化版)
│   │   └── index.html         # 已部署到 GitHub Pages ✅
│   └── media-platform/        # 多媒体处理平台 (全栈)
│       ├── backend/app.py     # Python/Flask 后端
│       ├── package.json       # Vue 前端配置
│       └── src/               # Vue 源码
├── agents/skills/             # AI 技能目录
│   ├── website-optimizer/     # 网站优化技能
│   ├── seo-audit/             # SEO 审计技能
│   └── ai-image-generation/   # AI 绘图技能
└── README.md
```

## 🧩 8 阶段路线

| 阶段 | 目标 | 状态 |
|------|------|:----:|
| 阶段一 | 初始化 AI Agent（角色+记忆+工作空间） | ✅ AGENTS.md + MEMORY.md 就绪 |
| 阶段二 | 静态网站自动上线（GitHub Pages） | ✅ ai-guide 已部署 |
| 阶段三 | Agent 技能管理系统 | ✅ 3 个技能已入库 |
| 阶段四 | AI 图像生成+文档配图 | 🚧 技能已创建，需 API Key |
| 阶段五 | 底模切换+SEO 优化 | ✅ 网站已实施 SEO |
| 阶段六 | 全栈项目+双端验证 | ✅ 多媒体平台框架完成 |
| 阶段七 | Issue/定时任务自动化 | ✅ Actions 配置完成 |
| 阶段八 | 技能蒸馏封装 | 📅 待执行 |

## 🚀 快速开始

1. 打开仓库的 Copilot Chat：按 `.` 键或访问 `/copilot`
2. 输入阶段对应的提示词
3. Agent 会自动读取 AGENTS.md 和 MEMORY.md

## 🔧 配置需求

- **AI 图像生成**: 需要提供 Gemini/OpenAI API Key
- **Multimedia 平台**: 后端需要安装 `pip install -r backend/requirements.txt`
- **GitHub Pages**: 在 Settings → Pages 中启用，选择 master branch

## 📄 开源协议

MIT — Built with ❤️ by Claw Agent
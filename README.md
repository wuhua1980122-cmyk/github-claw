# 🦞 GitHub Claw — AI Agent 养成实验

> 通过 GitHub Copilot 网页版，从零打造一个具备角色、记忆和技能的个人 AI 助手。

## 📋 项目概览

本项目是一次 AI Agent 构建实验，核心思路是：
> **"用 GitHub 仓库作为 AI 的工作空间，用 Copilot 作为交互界面，以 AGENTS.md + MEMORY.md + skills/ 作为记忆和能力的载体。"**

## 🏗️ 项目结构

```
github-claw/
├── AGENTS.md          # AI 助手的角色设定与工作流
├── MEMORY.md          # 长期记忆与经验积累
├── .github/workflows/ # GitHub Actions 自动化配置
├── projects/
│   └── ai-guide/      # AI 知识导航网站
│       └── index.html # 前端静态页面
├── agents/
│   └── skills/        # AI 技能包目录
│       ├── website-optimizer/     # 网站优化技能
│       ├── seo-audit/             # SEO 审计技能
│       └── ai-image-generation/   # AI 绘图技能
└── README.md          # 本文件
```

## 🧩 8 阶段路线

| 阶段 | 目标 | 状态 |
|------|------|------|
| 阶段一 | 初始化 AI Agent（角色 + 记忆 + 工作空间） | ✅ |
| 阶段二 | 静态网站自动上线（GitHub Pages） | ✅ |
| 阶段三 | Agent 技能管理系统 | ✅ |
| 阶段四 | AI 图像生成 + 文档配图 | 🚧 待执行 |
| 阶段五 | 底模切换 + SEO 优化 | 📅 计划中 |
| 阶段六 | 全栈项目开发 + 双端验证 | 📅 计划中 |
| 阶段七 | Issue/定时任务自动化 | 📅 计划中 |
| 阶段八 | 技能蒸馏封装 | 📅 计划中 |

## 🚀 开始使用

1. 进入仓库的 Copilot Chat（按 `.` 或在 URL 后加 `/copilot`）
2. 输入对应阶段的提示词
3. Agent 会自动读取 AGENTS.md 了解角色，参考 MEMORY.md 获取上下文

## 📄 开源协议

MIT

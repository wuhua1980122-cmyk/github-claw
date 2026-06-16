# AI Image Generation 技能

## 描述
使用 AI 生成配图、插图和宣传图。需要调用外部 API。

## 触发词
生成图片 / 配图 / 插图 / AI 绘图 / image generation

## API 配置
- API 提供方：需用户提供 API Key
- 安全规则：Key 不写入仓库，仅在运行时通过环境变量或手动输入使用

## 工作流
1. 理解需求：图片风格、尺寸、主题
2. 构造描述 Prompt（参考风格模板）
3. 调用 AI 绘图 API 生成图片
4. 保存图片到指定目录
5. 在文档中引用图片路径

## 风格模板
- 动漫风格：`Anime style, vibrant colors, detailed background, Studio Ghibli inspired`
- 极简风格：`Minimalist, clean lines, pastel palette, flat design`
- 科技风格：`Futuristic, neon accents, dark theme, cyberpunk aesthetic`

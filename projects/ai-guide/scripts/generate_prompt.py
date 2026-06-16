"""
DeepSeek API 调用示例 —— 为 AI Guide 生成图片描述
"""

import requests
import json

DEEPSEEK_API = "https://api.deepseek.com/v1/chat/completions"
API_KEY = "your-deepseek-api-key-here"  # ← 替换为你的 DeepSeek API Key

def generate_image_prompt(topic: str) -> str:
    """调用 DeepSeek 生成图片描述"""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {
                "role": "system",
                "content": "你是一位 AI 配图设计师。输出图片描述文字，用于在网页中展示。格式：标题 / 配色 / 元素说明。"
            },
            {
                "role": "user",
                "content": f"为 'AI Guide' 网站的 '{topic}' 区域生成一张配图描述。包含：图像标题、配色方案、核心视觉元素。输出纯文字描述即可。"
            }
        ],
        "temperature": 0.7,
        "max_tokens": 500
    }
    
    res = requests.post(DEEPSEEK_API, headers=headers, json=payload)
    if res.status_code == 200:
        return res.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {res.status_code} - {res.text}"

# 使用示例
if __name__ == "__main__":
    for topic in ["Hero 科技主题", "学习路线图", "资源卡片"]:
        print(f"\n=== {topic} ===")
        print(generate_image_prompt(topic))
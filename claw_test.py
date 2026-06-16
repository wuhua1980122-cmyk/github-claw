"""
🔥 Claw Agent 实战测试 —— 本地直接调用 DeepSeek
用法: uv run python claw_test.py
"""

import requests
import json

API_KEY = "sk-4ea6cb05b06f4139986d6c51d2b68dbf"
API_URL = "https://api.deepseek.com/v1/chat/completions"

def chat(messages):
    res = requests.post(API_URL, headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }, json={
        "model": "deepseek-chat",
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 2000
    })
    return res.json()["choices"][0]["message"]["content"]

if __name__ == "__main__":
    print("=" * 50)
    print("🦞 Claw Agent · DeepSeek 实战测试")
    print("=" * 50)

    history = [
        {"role": "system", "content": "你叫 Claw Agent，是一个个人 AI 助手，说话简洁直接。你擅长技术、编程和自动化。"}
    ]

    # 第一轮：自我介绍
    history.append({"role": "user", "content": "先做个自我介绍，说说你能帮我做什么，100字以内。"})
    print(f"\n🧑 你: 先做个自我介绍")
    reply = chat(history)
    history.append({"role": "assistant", "content": reply})
    print(f"\n🤖 Claw: {reply}")

    # 第二轮：测试技能 —— 这里可以换你的需求
    history.append({"role": "user", "content": "请用 Python 写一个简单的图片压缩脚本，支持 jpg 和 png。"})
    print(f"\n🧑 你: 写一个图片压缩脚本")
    reply = chat(history)
    history.append({"role": "assistant", "content": reply})
    print(f"\n🤖 Claw: {reply[:500]}...")

    print("\n" + "=" * 50)
    print("✅ 测试完成！")
    print("💡 提示: 修改上面的 prompt 可以问任何问题")
    print("=" * 50)
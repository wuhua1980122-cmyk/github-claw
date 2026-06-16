"""
DeepSeek API 璋冪敤绀轰緥 鈥斺€?涓?AI Guide 鐢熸垚鍥剧墖鎻忚堪
API Key 宸查厤缃?"""

import requests
import json

DEEPSEEK_API = "https://api.deepseek.com/v1/chat/completions"
API_KEY = "sk-4ea6cb05b06f4139986d6c51d2b68dbf"

def generate_image_prompt(topic: str) -> str:
    """璋冪敤 DeepSeek 鐢熸垚鍥剧墖鎻忚堪"""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {
                "role": "system",
                "content": "浣犳槸涓€浣?AI 閰嶅浘璁捐甯堛€傝緭鍑哄浘鐗囨弿杩版枃瀛楋紝鐢ㄤ簬鍦ㄧ綉椤典腑灞曠ず銆傛牸寮忥細鏍囬 / 閰嶈壊 / 鍏冪礌璇存槑銆?
            },
            {
                "role": "user",
                "content": f"涓?'AI Guide' 缃戠珯鐨?'{topic}' 鍖哄煙鐢熸垚涓€寮犻厤鍥炬弿杩般€傚寘鍚細鍥惧儚鏍囬銆侀厤鑹叉柟妗堛€佹牳蹇冭瑙夊厓绱犮€傝緭鍑虹函鏂囧瓧鎻忚堪鍗冲彲銆?
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

# 浣跨敤绀轰緥
if __name__ == "__main__":
    for topic in ["Hero 绉戞妧涓婚", "瀛︿範璺嚎鍥?, "璧勬簮鍗＄墖"]:
        print(f"\n=== {topic} ===")
        print(generate_image_prompt(topic))

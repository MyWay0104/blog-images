# 1단계: requests로 REST API를 직접 호출한다 — URL·헤더·본문·응답 파싱을 전부 내가 쓴다
import requests

OLLAMA_CHAT_URL = "http://127.0.0.1:11434/v1/chat/completions"   # 주소가 코드에 그대로 보인다

payload = {
    "model": "llama3.2",
    "messages": [{"role": "user", "content": "한 문장으로 자기소개 해 주세요."}],
}
headers = {"Authorization": "Bearer ollama"}   # 형식상 필요하지만 Ollama는 무시한다

r = requests.post(OLLAMA_CHAT_URL, headers=headers, json=payload, timeout=30)
print("status_code:", r.status_code)           # 상태 코드는 내가 확인한다
r.raise_for_status()                            # 4XX·5XX면 여기서 예외

data = r.json()                                 # JSON → dict
print("content:", data["choices"][0]["message"]["content"])   # 답을 꺼내는 경로도 내가 안다

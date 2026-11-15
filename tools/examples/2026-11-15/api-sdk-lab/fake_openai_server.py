# OpenAI 형식(/v1/chat/completions)으로 응답하는 로컬 시험 서버 (표준 라이브러리만 사용)
# 실제 LLM이 아니라, 요청을 받았다는 사실과 요청 내용을 로그로 남기고 고정된 답을 돌려준다
import json, time
from http.server import BaseHTTPRequestHandler, HTTPServer

class H(BaseHTTPRequestHandler):
    def do_POST(self):
        n = int(self.headers.get('Content-Length', 0))
        body = json.loads(self.rfile.read(n) or b'{}')
        auth = self.headers.get('Authorization', '(없음)')
        print(f"[서버] POST {self.path}  Authorization: {auth}")
        print(f"[서버] model={body.get('model')}  messages={body.get('messages')}")
        resp = {
            "id": "chatcmpl-local-001", "object": "chat.completion", "created": int(time.time()),
            "model": body.get("model"),
            "choices": [{"index": 0, "finish_reason": "stop",
                          "message": {"role": "assistant", "content": "저는 로컬에서 도는 시험용 응답입니다."}}],
            "usage": {"prompt_tokens": 12, "completion_tokens": 9, "total_tokens": 21},
        }
        out = json.dumps(resp, ensure_ascii=False).encode()
        self.send_response(200); self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(out))); self.end_headers(); self.wfile.write(out)
    def log_message(self, *a): pass

HTTPServer(('127.0.0.1', 11434), H).serve_forever()

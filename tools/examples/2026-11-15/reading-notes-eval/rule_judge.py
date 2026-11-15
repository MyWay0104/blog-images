# 규칙 기반 판정기 — 독서 노트 요약 출력이 "정해진 규칙"을 지켰는지 코드로 판정한다 (LLM을 쓰지 않는다)
import json
from pydantic import BaseModel, Field, ValidationError

class NoteSummary(BaseModel):            # 출력이 지켜야 할 스키마
    title: str
    summary: str = Field(max_length=120)  # 요약은 120자 이내
    tags: list[str] = Field(max_length=4) # 태그는 최대 4개
    rating: int = Field(ge=1, le=5)       # 별점은 1~5

BANNED = ["확인 필요", "모르겠"]            # 요약에 들어가면 안 되는 표현

def judge(raw: str, book_title: str) -> tuple[bool, str]:
    try:
        obj = NoteSummary.model_validate_json(raw)          # 규칙 1: JSON 스키마
    except ValidationError as e:
        first = e.errors()[0]
        return False, f"스키마 위반: {'.'.join(map(str, first['loc']))} — {first['msg']}"
    if obj.title != book_title:                              # 규칙 2: 책 제목이 원문과 정확히 같은가
        return False, f"제목 불일치: '{obj.title}' != '{book_title}'"
    for w in BANNED:                                         # 규칙 3: 금지 표현
        if w in obj.summary:
            return False, f"금지 표현 포함: '{w}'"
    return True, "통과"

samples = [
    ('{"title":"걷기의 인문학","summary":"걷는 속도가 생각의 속도를 만든다는 주장을 역사 속 산책자들로 보여 준다.","tags":["산책","사유"],"rating":4}', "걷기의 인문학"),
    ('{"title":"걷기의 인문학","summary":"좋은 책.","tags":["a","b","c","d","e","f"],"rating":5}', "걷기의 인문학"),
    ('{"title":"걷기의 인문학","summary":"내용이 길어 확인 필요.","tags":["산책"],"rating":3}', "걷기의 인문학"),
    ('{"title":"걷기 인문학","summary":"산책의 역사.","tags":["산책"],"rating":"최고"}', "걷기의 인문학"),
]
for i, (raw, title) in enumerate(samples, 1):
    ok, why = judge(raw, title)
    print(f"[출력 {i}] {'PASS' if ok else 'FAIL'} — {why}")

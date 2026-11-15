from lib import *
# 대표 예시: 독서 노트 요약 에이전트(reading-notes) — 출력 {title, summary, tags, rating}을 규칙 판정기(pydantic)와 LLM 판정기로 평가
T='[AI활용] LLM-as-a-Judge vs 규칙 기반 평가 선택 기준: 코드로 판정할 수 있으면 코드로'
SA='출처: Arize 공식 문서 "Evaluator Types — Human, Code, and LLM-as-a-Judge"(arize.com/docs/ax), 2026-11-15 캡처'
SP='출처: Arize Phoenix 공식 문서 "Using Evaluators"(arize.com/docs/phoenix), 2026-11-15 캡처'
SG='출처: Ragas 공식 문서 "Overview of Metrics"(docs.ragas.io, stable), 2026-11-15 캡처'
SL='출처: LangSmith 공식 문서 "Evaluation concepts"(docs.langchain.com), 2026-11-15 캡처'
SX='샌드박스에서 pydantic으로 만든 규칙 판정기를 예시 출력 4건에 실제로 실행한 결과 (LLM 호출 없음)'
b=''
b+=IMG(1,'목_01_썸네일.png','대표 이미지(썸네일)')
b+=P('에이전트가 만든 답을 어떻게 평가할지 정하다 보면','"LLM한테 채점시키면 되지 않나"와 "그걸 LLM이 믿을 만하게 하나"가 같이 떠오릅니다.','LLM-as-a-Judge와 규칙 기반(코드) 평가는 어디서 갈라야 할까요.')
b+=P('결론부터 적으면,','**==항목마다 "이걸 코드로 판정할 수 있는가"를 먼저 묻고, 예면 코드로 끝냅니다.==**','출력 형식, 개수, 범위, 정확히 일치, 금지어는 코드가 맡고,','"뜻이 맞나", "도움이 되나"처럼 코드로 셀 수 없는 것만 채점 기준을 적어 LLM에 맡깁니다.')
b+=BOX('**이 글의 기준**','확인 날짜: 2026-11-15','근거: Arize 공식 문서(Evaluator Types), Arize Phoenix 공식 문서(Using Evaluators), Ragas 공식 문서(Overview of Metrics), LangSmith 공식 문서(Evaluation concepts)','이 글은 두 방식을 실제 서비스에서 운영해 본 후기가 아니라 **공식 자료를 비교해 정리한 글**입니다. 독서 노트 요약 에이전트 예시와 "항목별 판정기 표"는 제 설계 제안입니다.','규칙 판정기 화면은 샌드박스에서 pydantic으로 실제 실행한 결과입니다. LLM 판정기는 이번에 실행하지 않았습니다.')
b+=HR()
b+=H1('1. 같은 출력을 두 판정기에 넣으면')
b+=IMG(2,'목_02_도식_두판정기.png','독서 노트 요약 에이전트의 출력 하나가 규칙 기반 판정기(코드)와 LLM 판정기로 각각 들어가 점수/라벨로 나오는 구조를 그린 도식')
b+=P('예시는 독서 노트 요약 에이전트입니다.','책 한 권에 대해 `{"title", "summary", "tags", "rating"}` 모양의 출력을 냅니다.','이 출력을 평가하는 길이 둘입니다.')
b+=P('**규칙 기반 판정기**는 함수입니다. 스키마가 맞나, 태그가 4개 이하인가, 별점이 1~5인가, 제목이 원문과 같나, 금지 표현이 없나.','같은 입력이면 **항상 같은 결과**가 나오고, 이유는 "어긴 규칙"입니다.')
b+=P('**LLM 판정기(LLM-as-a-Judge)**는 채점 기준을 받은 LLM입니다. 요약이 책 내용을 왜곡하지 않았나, 태그가 주제를 대표하나.','결과는 라벨과 설명이고, **돌릴 때마다 조금 다를 수 있습니다.**')
b+=HR()
b+=H1('2. 공식 문서 세 곳이 같은 말을 한다')
b+=IMG(3,'목_03_Arize_평가자유형.png','Arize 공식 문서의 세 가지 평가자 유형 표: Human, Code-based, LLM-as-a-judge 각각의 동작 방식, 잘하는 것, 못하는 것',SA)
b+=P('Arize 문서는 평가자를 세 종류로 나눕니다.','**Code-based**: "**결정적인 Python(또는 내장 템플릿)이 출력을 검사한다.**" 잘하는 것은 "**프로그램으로 검사할 수 있는 모든 것 — 문자열 포함, JSON 모양, 정규식, 결정적 비교**", 못하는 것은 "**주관적인 모든 것 — 말투, 도움 여부, 사실성**".')
b+=P('**LLM-as-a-judge**: "**LLM이 데이터를 읽고 라벨과 설명을 낸다.**" 잘하는 것은 "**주관적 품질을 대규모로, 사전 데이터 거의 없이**", 못하는 것은 "**비결정적, 프롬프트 설계 필요, 알려진 편향에 취약**".','**Human**: 뉘앙스와 전문성, 그리고 "**다른 평가자를 보정하는 골든 데이터셋을 정의**"하는 일. 대신 느리고 비싸고 일관성이 떨어집니다.')
b+=IMG(4,'목_04_Arize_결정나무.png','Arize 공식 문서의 결정 나무: ① 질문이 결정적인가(예 = 코드), ② 운영 규모로 평가해야 하는가(아니오 = 사람), ③ 나머지 기본값은 LLM-as-a-judge. 세 종류는 경쟁이 아니라 보완',SA)
b+=P('같은 문서에 **결정 나무**가 있습니다.','"**① 질문이 결정적인가? (예 = 코드 기반. 끝.)**"','"**② 운영 규모로 평가해야 하는가? (아니오 = 적은 표본은 사람으로 충분.)**"','"**③ 나머지 전부의 기본값 = LLM-as-a-judge.**"','그리고 "대부분의 운영 환경은 여러 종류를 함께 돌린다 — 싼 결정적 검사는 코드로, 주관적 질문은 LLM으로, 사람은 주기적으로 판정기를 검증한다. **세 종류는 서로 보완하지 경쟁하지 않는다**"고 적습니다.')
b+=IMG(5,'목_05_Ragas_지표분류.png','Ragas 공식 문서: LLM-based metrics는 비결정적일 수 있으나 사람 평가에 더 가깝고, Non-LLM-based metrics는 결정적이지만 사람 평가와의 상관이 낮다는 설명',SG)
b+=P('Ragas는 지표를 "밑에서 LLM을 쓰는가"로 나눕니다.','"**LLM 기반 지표**는 … LLM이 같은 입력에 늘 같은 결과를 주지는 않아 **다소 비결정적**일 수 있다. 반면 **더 정확하고 사람 평가에 가깝다**고 알려져 있다."','"**비LLM 기반 지표**는 … **결정적**이고, 문자열 유사도·BLEU 같은 전통적 방법에 기대며, 그래서 **사람 평가와의 상관이 낮다**고 알려져 있다."','지표를 고를 때는 "**객관적 기준이 있는 지표를 우선하고 주관적 판단을 최소화하라**"고 권합니다.')
b+=IMG(6,'목_06_LangSmith_평가자.png','LangSmith 공식 문서의 Evaluators: Code evaluators는 결정적이고 규칙 기반인 함수, LLM-as-judge evaluators는 채점 기준을 프롬프트에 적으며 점수의 세심한 검토와 프롬프트 조정이 필요',SL)
b+=P('LangSmith 문서도 같은 축입니다.','"**Code evaluators는 결정적이고 규칙 기반인 함수다.** 응답 구조가 비어 있지 않은지, 생성된 코드가 컴파일되는지, 분류가 정확히 일치하는지 같은 검사에 잘 맞는다."','"**LLM-as-judge evaluators는 LLM으로 출력을 채점한다. 채점 규칙과 기준은 보통 LLM 프롬프트에 적는다.**"','그리고 "**LLM 판정기는 점수의 세심한 검토와 프롬프트 조정이 필요하다.** 입력·출력·기대 점수 예시를 프롬프트에 넣는 few-shot 평가자가 성능을 자주 높인다"고 덧붙입니다.')
b+=P('세 문서의 공통점을 한 줄로 줄이면 이렇습니다.','**코드는 결정적이지만 주관을 못 다루고, LLM은 주관을 다루지만 결정적이지 않다.**','그러니 결정적으로 판정할 수 있는 항목을 LLM에 맡길 이유가 없습니다.')
b+=HR()
b+=H1('3. Phoenix에서는 어떻게 생겼나')
b+=IMG(7,'목_07_Phoenix_LLM평가자.png','Phoenix 공식 문서의 Custom LLM Evaluators 예시: 채점 기준을 적은 프롬프트 템플릿(helpful / not_helpful 정의)과 choices={"not_helpful": 0, "helpful": 1}로 ClassificationEvaluator를 만드는 코드',SP)
b+=P('Phoenix의 LLM 판정기는 **채점 기준이 곧 프롬프트**입니다.','문서 예시는 "응답이 질문에 얼마나 도움이 되는지 평가하라"는 템플릿에 "helpful은 질문을 직접 다룬다는 뜻, not_helpful은 다루지 않는다는 뜻"이라고 기준을 적고,','`choices = {"not_helpful": 0, "helpful": 1}`로 라벨을 점수에 대응시킵니다.','기준 문장이 흐리면 판정도 흐려집니다. "채점 기준을 잘 정하는 게 매우 중요하다"는 말이 코드로 보이는 자리입니다.')
b+=IMG(8,'목_08_Phoenix_코드평가자.png','Phoenix 공식 문서의 Code Evaluators: 다른 LLM을 판정에 쓰지 않는 함수이며, 한 인자 함수는 output을 받고 boolean이나 숫자를 반환하면 그것이 점수가 된다. 예시 def in_bounds(x): return 1 <= x <= 100',SP)
b+=P('반대편의 코드 판정기는 문서 그대로 "**다른 LLM을 판정에 쓰지 않는 함수**"입니다.','"한 인자 함수는 실험 실행의 `output`을 받고, **boolean이나 숫자를 반환하면 그것이 평가 점수로 기록된다**."','예시가 전부입니다.')
b+=CODE('''# Phoenix 공식 문서의 코드 평가자 예시 (1~100 범위 검사)
def in_bounds(x):
    return 1 <= x <= 100
# run_experiment에 이 함수를 넘기면 실행마다 범위 안인지 자동으로 평가된다''',[('in_bounds','#8ce99a'),('return','#ffd43b')])
b+=HR()
b+=H1('4. 직접 돌려 본 규칙 판정기')
b+=P('독서 노트 예시의 규칙 쪽을 pydantic으로 짜서 실제로 돌려 봤습니다.','LLM은 부르지 않습니다. 출력 예시 4건을 넣었습니다.')
b+=CODE('''# rule_judge.py — 독서 노트 요약 출력이 규칙을 지켰는지 코드로 판정 (LLM 없음)
from pydantic import BaseModel, Field, ValidationError

class NoteSummary(BaseModel):            # 출력이 지켜야 할 스키마
    title: str
    summary: str = Field(max_length=120)  # 요약은 120자 이내
    tags: list[str] = Field(max_length=4) # 태그는 최대 4개
    rating: int = Field(ge=1, le=5)       # 별점은 1~5

BANNED = ["확인 필요", "모르겠"]            # 요약에 들어가면 안 되는 표현

def judge(raw: str, book_title: str) -> tuple[bool, str]:
    try:
        obj = NoteSummary.model_validate_json(raw)   # 규칙 1: JSON 스키마
    except ValidationError as e:
        first = e.errors()[0]
        return False, f"스키마 위반: {'.'.join(map(str, first['loc']))} — {first['msg']}"
    if obj.title != book_title:                       # 규칙 2: 책 제목이 원문과 정확히 같은가
        return False, f"제목 불일치: '{obj.title}' != '{book_title}'"
    for w in BANNED:                                  # 규칙 3: 금지 표현
        if w in obj.summary:
            return False, f"금지 표현 포함: '{w}'"
    return True, "통과"''',[('NoteSummary','#8ce99a'),('model_validate_json','#ffd43b'),('BANNED','#74c0fc')])
b+=P('`NoteSummary`가 스키마이자 규칙 1입니다. 필드 타입, 길이, 개수, 범위를 한 번에 선언합니다.','`model_validate_json`이 JSON 문자열을 검증하고, 어기면 `ValidationError`에 **어느 필드가 왜** 틀렸는지가 들어 있습니다.','규칙 2와 3은 비교와 문자열 포함 검사입니다. 전부 코드로 셀 수 있는 것들입니다.')
b+=IMG(9,'목_09_규칙판정기_실행.png','rule_judge.py 실행 결과: 출력 1 PASS, 출력 2 태그 6개로 스키마 위반, 출력 3 금지 표현 포함, 출력 4 rating이 문자열이라 스키마 위반',SX)
b+=P('결과는 PASS 1건, FAIL 3건이고, **FAIL 이유가 그대로 찍힙니다.**','태그 6개(최대 4개), 금지 표현 "확인 필요", 별점에 문자열.','몇 번을 돌려도 같은 결과입니다. 비용도 없습니다.')
b+=P('그런데 PASS한 출력 1의 요약이 **책 내용을 왜곡하지 않았는지**는 이 코드로 알 수 없습니다.','그 질문은 코드로 셀 수 없는 질문이고, 여기부터가 LLM 판정기의 자리입니다.')
b+=HR()
b+=H1('5. 항목마다 묻는 두 가지 질문')
b+=IMG(10,'목_10_도식_결정나무.png','Arize 문서의 결정 나무를 독서 노트 예시에 맞춰 다시 그린 도식: 코드로 판정할 수 있나 → 규칙 / 많은 양을 계속 평가하나 → 사람 또는 LLM 판정기')
b+=P('Arize 문서의 결정 나무를 제 예시에 맞춰 다시 그리면 위와 같습니다.','**① 코드로 판정할 수 있는가?** 예면 규칙으로 끝.','**② 많은 양을 계속 평가해야 하는가?** 아니오면 사람이 보고, 예면 LLM 판정기에 맡기되 사람 라벨과 주기적으로 대조합니다.')
b+=IMG(11,'목_11_항목별_판정기표.png','독서 노트 요약 에이전트의 평가 항목 8개를 코드 판정 가능 여부로 갈라 규칙·LLM 판정기·사람에 배정한 표')
b+=TABLE(['평가 항목','코드로 판정 가능?','맡기는 판정기'],[
['출력이 JSON 스키마를 지키는가','예','규칙 (Pydantic)'],
['태그 4개 이하, 별점 1~5','예','규칙'],
['책 제목이 원문과 정확히 같은가','예','규칙 (정확히 일치)'],
['금지 표현이 없는가','예','규칙 (문자열·정규식)'],
['요약이 책 내용을 왜곡하지 않았는가','아니오','LLM 판정기 (원문을 참조로)'],
['태그가 주제를 잘 대표하는가','아니오','LLM 판정기'],
['말투가 독서 노트답게 담백한가','아니오','LLM 판정기 → 사람 검증'],
['LLM 판정기 자체가 맞게 채점하는가','—','사람 (주기적으로 표본 대조)']])
b+=P('표의 윗부분 네 줄은 LLM을 부르지 않으니 **비용이 0에 가깝고 결과가 흔들리지 않습니다.**','먼저 거르고, 남은 것만 LLM에 보내는 순서가 됩니다.','(이 표는 공식 문서의 기준을 제 예시에 적용한 설계 제안이고, 실제로 운영해 본 결과는 아닙니다.)')
b+=HR()
b+=H1('6. 정리')
b+=IMG(12,'목_12_정리카드.png','규칙 기반 판정기, LLM-as-a-judge, 사람 평가, 고르는 순서 — 세 공식 문서의 표현을 모은 카드')
b+=TABLE(['내가 처음 생각한 것','공식 문서로 정리한 것'],[
['평가는 LLM에게 채점시키면 된다','결정적으로 판정할 수 있는 항목은 코드로. LLM 판정기는 주관적 품질을 대규모로 볼 때의 기본값 (Arize)'],
['LLM 판정기는 사람보다 못 믿는다','사람 평가에 가깝지만 비결정적이다 (Ragas). 점수 검토와 프롬프트 조정이 필요하다 (LangSmith)'],
['규칙 평가는 너무 단순해서 쓸모가 적다','결정적이고 싸다. 형식·범위·일치·금지어는 규칙이 맞다. 다만 사람 평가와의 상관은 낮다 (Ragas)'],
['셋 중 하나를 골라야 한다','세 종류는 보완 관계다. 코드로 거르고, LLM으로 보고, 사람이 주기적으로 검증한다 (Arize)']])
b+=BOX('**확인된 것과 확인되지 않은 것**','확인됨(공식 문서): 평가자 세 유형의 정의·장단점과 결정 나무(Arize), LLM 기반/비LLM 기반 지표의 결정성과 사람 평가 상관(Ragas), Code/LLM-as-judge 평가자 정의와 프롬프트 조정·few-shot 권고(LangSmith), 코드 평가자는 boolean·숫자를 반환하며 LLM 평가자는 템플릿+choices로 만든다는 것(Phoenix)','확인됨(실제 실행): pydantic 규칙 판정기가 예시 출력 4건을 결정적으로 판정하고 이유를 반환하는 것','확인 필요: LLM 판정기를 실제로 돌려 사람 라벨과 일치율을 재 보지는 않았습니다. 항목별 배정표는 제 설계 제안이며 운영 결과가 아닙니다.')
b+=HR()
b+=H1('알게 된 것')
b+=P('**질문은 "LLM이냐 규칙이냐"가 아니라 "이 항목은 코드로 셀 수 있나"였습니다.**','셀 수 있으면 코드로 끝내고, 셀 수 없는 것만 LLM에 맡깁니다.','그러면 채점 기준을 공들여 적어야 하는 항목이 몇 개로 줄어듭니다.')
b+=P('**LLM 판정기도 평가 대상이었습니다.**','비결정적이니 사람 라벨과 주기적으로 대조해야 하고,','사람 평가는 느리지만 나머지를 보정하는 기준점 역할을 합니다.')
b+=HR()
b+=H1('참고자료')
b+=P('[[Arize 공식 문서 - Evaluator Types: Human, Code, and LLM-as-a-Judge|https://arize.com/docs/ax/concepts/evaluators/evaluator-types]]')
b+=P('[[Arize Phoenix 공식 문서 - Using Evaluators|https://arize.com/docs/phoenix/datasets-and-experiments/how-to-experiments/using-evaluators]]')
b+=P('[[Ragas 공식 문서 - Overview of Metrics|https://docs.ragas.io/en/stable/concepts/metrics/overview/]]')
b+=P('[[LangSmith 공식 문서 - Evaluation concepts|https://docs.langchain.com/langsmith/evaluation-concepts]]')
b+=P('#LLMasaJudge #LLM평가 #규칙기반평가 #Phoenix #Ragas #LangSmith #pydantic #에이전트평가 #AI활용 #개발입문')
import os
PAGE(T,b,os.environ.get('OUT','/home/claude/out/thu/2026-11-19_목_LLM_as_a_Judge_vs_규칙기반.html'))
print('ok')

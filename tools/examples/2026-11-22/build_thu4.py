from lib import *
# 대표 예시: 온라인 신발 가게에 들어온 문의 한 건 (TypeSafe 공식 문서 Choice 예제의 문의를 우리말로 옮김)
#   "신발이 2주나 늦게, 그것도 다른 사이즈로 왔어요. 카드에는 120달러가 두 번 결제돼 있고요. 어떻게 해 주실 건가요?"
#   보낼 곳: returns(반품) / shipping(배송) / billing(결제). 문서에 실린 응답 기록: returns 0.61, billing 0.35, shipping 0.04, confidence 0.42
T='[AI활용] Jev vs LLM structured output 차이: LangGraph 라우팅에 판정 전용 모델을 넣는 기준'
S_LG='출처: LangChain 공식 문서 "Workflows and agents"의 Routing(docs.langchain.com/oss/python/langgraph/workflows-agents), 2026-11-22 캡처. 설명·그림 부분과 예제 코드 앞부분을 이어 붙였습니다'
S_OA='출처: OpenAI 공식 문서 "구조화된 모델 출력값"(developers.openai.com/api/docs/guides/structured-outputs, 한국어 화면), 2026-11-22 캡처'
S_CH='출처: TypeSafe 공식 문서 "Choice"(docs.typesafe.ai/primitives/choice), 2026-11-22 캡처'
S_CF='출처: TypeSafe 공식 문서 "Confidence"(docs.typesafe.ai/confidence), 2026-11-22 캡처'
S_BLOG='출처: TypeSafe 공식 블로그 "Introducing System One Models & Jev"(typesafe.ai/blog, 2026-09-15 글), 2026-11-22 캡처'
S_GH='출처: GitHub 저장소 browser-use/jev-ultrafast의 README(github.com/browser-use/jev-ultrafast), 2026-11-22 캡처'
S_X='샌드박스(Python 3.13.17, pydantic 2.13.5)에서 실제로 실행한 출력을 옮긴 화면. 입력 숫자는 TypeSafe 공식 문서에 실린 응답 기록입니다'
b=''
b+=IMG(1,'목_01_썸네일.png','대표 이미지(썸네일)')
b+=P('LangGraph로 문의를 분류해서 알맞은 처리로 보내는 라우팅을 만들 때,','분류 자체는 보통 LLM의 structured output에 맡깁니다.')
b+=P('그런데 판정만 하는 모델 Jev를 알게 되면서 헷갈리기 시작했습니다.','"그건 내가 이미 그래프로 하고 있는 라우팅과 뭐가 다르지?"')
b+=P('결론부터 적으면,','**==LangGraph는 배선이고, Jev는 그 배선 안의 라우팅 노드에 끼우는 판정 부품입니다. 비교할 상대는 LangGraph가 아니라 "라우팅 노드 안의 LLM structured output"입니다. 형식을 지키는 것은 둘 다 하고, 갈리는 곳은 선택지마다의 확률이 같이 돌아오느냐, 그리고 판정 말고 다른 일도 할 수 있느냐입니다.==**')
b+=BOX('**이 글의 기준**','확인 날짜: 2026-11-22','근거: LangChain 공식 문서(LangGraph의 Workflows and agents), OpenAI 공식 문서(Structured Outputs), TypeSafe 공식 문서(Choice, Confidence, How to build with TypeSafe, Model jaggedness, Patterns), TypeSafe의 발표문과 사례 글, Browser Use의 GitHub 저장소','**사용 후기가 아니라 공식 자료 비교입니다.** Jev를 직접 호출해 보지 못했고, 이 글의 LangGraph·Jev 코드도 공식 예제의 형식을 따라 적은 것이라 실행하지 않았습니다.','실제 실행: 공식 문서에 실린 응답의 확률로 confidence 공식을 검산한 계산 하나만 샌드박스에서 실행했습니다.','속도·가격·사례의 수치는 모두 TypeSafe와 사례 당사자의 발표 기준입니다.','확인하지 못한 것: 같은 문의를 두 방식에 직접 넣어 본 결과, 한국어 문의에서의 판정 품질')
b+=HR()
b+=H1('1. 처음에 헷갈렸던 것')
b+=P('Jev를 공부하던 중에 이렇게 물었습니다.')
b+=Q('그럼 사실 모델 자체가 아니라 기존에 내가 사용하는 모델에 라우팅을 스테이트그래프 기반으로 하네스 씌워서 사용하는거랑 무슨 차이야?')
b+=BOX('**당시의 생각**','Jev를 "라우팅을 해 주는 것"으로 이해했다.','라우팅이라면 이미 StateGraph에 조건부 엣지를 달아서 하고 있다.','그러니 Jev는 그 방식과 자리를 다투는 다른 도구라고 생각했다.')
b+=P('질문을 다시 보니,','층이 다른 두 가지를 한 줄에 놓고 있었습니다.','그래프와 모델입니다.')
b+=HR()
b+=H1('2. 배선과 부품: 비교 대상부터 바로잡기')
b+=IMG(2,'목_02_도식_배선과_부품.png','그래프는 배선, 모델은 부품: 문의가 라우팅 노드로 들어가고, 노드 안의 판정 부품(LLM structured output 또는 Jev)이 어느 쪽인지 정하면 조건부 엣지가 반품·배송·결제 처리로 보낸다. 배선은 LangGraph의 StateGraph(add_node, add_conditional_edges, 엣지 함수), 부품은 라우팅 노드 안의 모델 호출')
b+=P('LangGraph 공식 문서의 Routing 설명부터 보겠습니다.')
b+=IMG(3,'목_03_공식문서_LangGraph_Routing.png','LangChain 공식 문서의 Routing: Routing 워크플로는 입력을 처리한 뒤 맥락에 맞는 작업으로 보낸다. 그림은 In → Router → 세 갈래 → Out. 예제 코드 앞부분: class Route(BaseModel)의 step: Literal["poem", "story", "joke"], router = llm.with_structured_output(Route)',S_LG)
b+=P('"**Routing 워크플로는 입력을 처리한 뒤, 맥락에 맞는 작업으로 보낸다.**"','"**예를 들어 제품 문의에 답하는 워크플로라면 먼저 질문의 유형을 처리하고, 그다음 가격·환불·반품 같은 각각의 처리로 요청을 보낼 수 있다.**"')
b+=P('문서의 예제 코드는 다섯 조각으로 되어 있습니다.')
b+=TABLE(['조각','문서 예제의 코드','하는 일'],[
['① 스키마','`class Route(BaseModel)` 안의 `step: Literal[...]`','답이 될 수 있는 값을 정해 둔다'],
['② 판정 모델','`router = llm.with_structured_output(Route)`','LLM이 그 스키마대로 답하게 한다'],
['③ 라우터 노드','`llm_call_router`가 `{"decision": decision.step}`을 돌려줌','판정 결과를 state에 적는다'],
['④ 엣지 함수','`route_decision`이 state의 decision을 읽음','다음 노드 이름을 돌려준다'],
['⑤ 조건부 엣지','`add_conditional_edges(...)`','그 이름의 노드로 보낸다']])
b+=P('여기서 **"어느 쪽인지 정하는 일"은 ②와 ③**, 모델을 부르는 부분입니다.','**"정해진 대로 보내는 일"은 ④와 ⑤**, 그래프입니다.')
b+=P('Jev가 대신할 수 있는 것은 ②③의 모델 호출뿐입니다.','④⑤의 그래프는 무엇으로 판정하든 그대로 남습니다.')
b+=TABLE(['층','하는 일','Jev를 쓴다면'],[
['배선 (하네스)','노드를 잇고, 결과에 따라 다음 노드로 보낸다','그대로 둔다'],
['판정 부품 (모델 호출)','글을 읽고 어느 쪽인지 정한다','**여기를 바꿔 끼운다**']])
b+=P('TypeSafe 문서도 같은 그림을 전제로 합니다.','"**Jev는 에이전트가 아니라 AI 기반 소프트웨어를 만들기 위한 모델이다. 코드를 만들지 않고, 자기의 다음 행동을 고르지도 않는다.**"','"**제어 흐름과 결정적인 규칙, 부수 효과는 코드에 둔다.**"')
b+=P('흐름은 코드(여기서는 그래프)가 쥐고,','모델은 그 안의 좁은 판단 하나만 맡는다는 뜻입니다.','**==그래서 "LangGraph냐 Jev냐"가 아니라 "라우팅 노드 안에 LLM을 둘 것이냐 Jev를 둘 것이냐"가 맞는 질문이었습니다.==**')
b+=HR()
b+=H1('3. 같은 문의를 두 부품에 넣어 보면')
b+=P('이어서 이렇게 물었습니다.')
b+=Q('같은 맥락에서 jev가 기존 llm기반 스트럭처에 비해서 강점이 되는 부분이 정확히 뭐지? 일반적인 예시를 하나 들어서 비교설명해')
b+=P('예시는 TypeSafe 공식 문서에 실린 문의를 그대로 가져왔습니다.','문서에 **실제 응답 기록**이 함께 실려 있어서, 숫자를 지어내지 않아도 되기 때문입니다.')
b+=BOX('**이 글의 예시 (TypeSafe 문서의 예제를 우리말로 옮김)**','온라인 신발 가게에 들어온 문의:','"신발이 2주나 늦게, 그것도 다른 사이즈로 왔어요. 카드에는 120달러가 두 번 결제돼 있고요. 어떻게 해 주실 건가요?"','보낼 곳은 세 팀: `returns`(반품·교환), `shipping`(배송), `billing`(결제)')
b+=P('한 문장 안에 배송 지연, 사이즈 오류, 이중 결제가 다 들어 있습니다.','어느 팀으로 보내야 할지 사람이 봐도 망설여지는 문의입니다.')
b+=H2('(가) LLM structured output을 끼운 경우')
b+=P('LangGraph 문서 예제의 형식에 이 예시를 넣으면 이런 모양입니다.','(형식을 따라 적은 것이고, 실행해 보지는 못했습니다.)')
b+=CODE('''from typing import Literal
from pydantic import BaseModel, Field

class Route(BaseModel):
    department: Literal["returns", "shipping", "billing"] = Field(
        description="이 문의를 맡을 팀"
    )

router = llm.with_structured_output(Route)

def route_node(state: State):
    decision = router.invoke(state["ticket"])
    return {"department": decision.department}''',[('from ','#74c0fc'),('import','#74c0fc'),('class ','#74c0fc'),('def ','#74c0fc'),('return','#74c0fc'),('Literal["returns", "shipping", "billing"]','#ffd43b'),('with_structured_output','#8ce99a')])
b+=P('`Route`는 답의 모양을 정한 스키마입니다.','`Literal[...]`로 팀 이름 세 개만 허용했습니다.','`llm.with_structured_output(Route)`는 LLM이 이 스키마대로 답하게 만든 `router`입니다.','`route_node`는 문의 글을 `router`에 넣고, 돌아온 팀 이름을 state에 적습니다.','(`llm`과 `State`는 문서 예제처럼 앞에서 만들어 둔 것으로 봅니다.)')
b+=P('돌아오는 것은 **값 하나**입니다.')
b+=CODE('''Route(department="returns")''',[('"returns"','#ffd43b')])
b+=P('(위 값은 형식을 보이려고 적은 것입니다. 실제로 어느 팀이 나올지는 실행해 보지 않아 모릅니다.)')
b+=IMG(4,'목_04_공식문서_OpenAI_StructuredOutputs.png','OpenAI 공식 문서(한국어) 구조화된 모델 출력값: 구조화된 출력값을 사용하면 모델이 요청을 거부하지 않고 끝까지 생성한 응답은 지정한 JSON 스키마를 따른다. 이점 1 스키마 준수(필수 필드가 포함되고 열거형 값은 스키마에서 허용한 값으로 제한), 2 명시적인 거부 응답, 3 간단한 프롬프트',S_OA)
b+=P('세 팀 밖의 엉뚱한 값이 나오지는 않을까요.','OpenAI 문서는 Structured Outputs를 이렇게 설명합니다.','"**모델이 요청을 거부하지 않고 끝까지 생성한 응답은 지정한 JSON 스키마를 따릅니다.**"','"**응답에 필수 필드가 포함되고, 열거형 값은 스키마에서 허용한 값으로 제한됩니다.**"')
b+=P('**즉 "형식이 지켜진다"는 것은 LLM 쪽에서도 됩니다.**','Jev만의 강점이라고 생각했던 부분인데, 아니었습니다.','(같은 문서는 거부 응답, 불완전한 응답, 스키마로 표현하지 못한 업무 규칙은 여전히 애플리케이션이 처리해야 한다고 덧붙입니다. 다른 제공자의 보장 범위는 각자 문서로 확인이 필요합니다.)')
b+=H2('(나) Jev의 Choice를 끼운 경우')
b+=P('같은 자리에 Jev를 넣으면, TypeSafe 문서의 Choice 예제 형식으로는 이렇습니다.','(마찬가지로 실행해 보지 못했습니다.)')
b+=CODE('''from typesafe_sdk import Choice, TypeSafeClient

def route_node(state: State):
    with TypeSafeClient() as client:
        response = client.system_one(
            state=state["ticket"],
            questions={
                "department": Choice(
                    instructions="Which team should handle this?",
                    criteria={
                        "returns": "Exchanges, wrong or damaged items",
                        "shipping": "Delivery status, delays, lost packages",
                        "billing": "Charges, invoices, payment problems",
                    },
                ),
            },
        )
    answer = response.answers["department"]
    return {
        "department": answer.choice,
        "confidence": answer.confidence,
        "probabilities": answer.probabilities,
    }''',[('from ','#74c0fc'),('import','#74c0fc'),('def ','#74c0fc'),('with ','#74c0fc'),(' as ','#74c0fc'),('return','#74c0fc'),('answer.choice','#ffd43b'),('answer.confidence','#8ce99a'),('answer.probabilities','#8ce99a')])
b+=P('`state`에는 문의 글을 넣습니다.','`Choice`가 질문 타입이고, `criteria`에 선택지 세 개와 각각의 설명을 적습니다.','스키마의 `Literal`이 하던 역할을 `criteria`가 합니다.','마지막 `return`에서 고른 값(`choice`)뿐 아니라 `confidence`와 `probabilities`도 state에 적었습니다.')
b+=IMG(5,'목_05_공식문서_TypeSafe_Choice응답.png','TypeSafe 공식 문서에 실린 Jev의 응답: department의 choice는 returns, confidence 0.42, probabilities는 shipping 0.04, billing 0.35, returns 0.61',S_CH)
b+=P('이 문의에 대한 응답이 문서에 실려 있습니다.','고른 값은 `returns`. 여기까지는 (가)와 다를 것이 없습니다.','그런데 옆에 숫자가 같이 옵니다.','**returns 0.61, billing 0.35, shipping 0.04.**')
b+=P('문서의 해설은 이렇습니다.','"**department의 답은 0.61의 returns이지만, 이중 결제 때문에 billing이 0.35를 받았다. 이 문의는 두 팀에 걸쳐 있고, 0.42로 갈라진 confidence가 그것을 반영한다.**"')
b+=P('**==(가)의 값 하나에서는 "반품 61, 결제 35로 갈렸다"는 사실이 보이지 않습니다. (나)에서는 그 갈림이 숫자로 같이 옵니다.==**')
b+=P('LLM 쪽에서도 스키마에 "확신도" 칸을 만들어 적게 할 수는 있습니다.','다만 그것은 모델이 글로 써낸 숫자입니다.','TypeSafe는 발표문에서 그런 값이 과신하기 쉽고 일관되지 않다고 주장합니다.','(TypeSafe의 주장이고, 제가 확인한 것은 아닙니다.)')
b+=H2('confidence는 어디서 나온 숫자인가')
b+=P('0.42가 어떻게 나온 값인지도 문서에 공식이 있습니다.','선택지가 n개이고 가장 큰 확률이 p_max일 때,')
b+=CODE('''confidence = (p_max - 1/n) / (1 - 1/n)''',[('confidence','#8ce99a')])
b+=P('"똑같이 나눠 가진 상태(1/n)"에서 가장 큰 확률이 얼마나 위에 있는지를','0에서 1 사이로 나타낸 값입니다.')
b+=P('문서에 실린 응답 다섯 건의 확률을 넣어 직접 계산해 봤습니다.')
b+=CODE('''from decimal import Decimal, ROUND_HALF_UP
from pydantic import BaseModel

class ChoiceAnswer(BaseModel):
    # 문서에 실린 응답 한 건: 질문 이름, 선택지별 확률, 문서에 적힌 confidence
    name: str
    probabilities: dict[str, Decimal]
    confidence: Decimal

def choice_confidence(probabilities: dict[str, Decimal]) -> Decimal:
    # 문서의 Choice 공식: (가장 큰 확률 - 1/n) / (1 - 1/n)
    n = Decimal(len(probabilities))
    p_max = max(probabilities.values())
    return (p_max - 1 / n) / (1 - 1 / n)

D = Decimal
answers = [
    ChoiceAnswer(name="department", confidence=D("0.42"),
                 probabilities={"shipping": D("0.04"), "billing": D("0.35"), "returns": D("0.61")}),
    # ... 나머지 네 건도 문서의 숫자 그대로
]

for a in answers:
    calc = choice_confidence(a.probabilities).quantize(D("0.001"), rounding=ROUND_HALF_UP)
    diff = abs(calc - a.confidence)
    print(a.name, len(a.probabilities), max(a.probabilities.values()), calc, a.confidence, diff)''',[('from ','#74c0fc'),('import','#74c0fc'),('class ','#74c0fc'),('def ','#74c0fc'),('return','#74c0fc'),('for ','#74c0fc'),('(p_max - 1 / n) / (1 - 1 / n)','#8ce99a'),('ROUND_HALF_UP','#ffd43b')])
b+=P('`ChoiceAnswer`는 응답 한 건을 담는 틀입니다. 확률은 오차 없이 다루려고 `Decimal`로 받습니다.','`choice_confidence`는 문서의 공식 한 줄을 그대로 옮긴 함수입니다. `n`은 선택지 수, `p_max`는 가장 큰 확률입니다.','`answers`에는 문서에 실린 숫자를 그대로 넣었습니다.','마지막 반복문은 계산값을 소수 셋째 자리로 맞추고(`quantize`), 문서의 값과 얼마나 다른지(`diff`) 출력합니다.','(본문에서는 출력 줄의 칸 맞춤과 나머지 네 건의 입력을 줄였습니다.)')
b+=IMG(6,'목_06_실행결과_confidence검산.png','검산 실행 결과: department 선택지 3, 최대확률 0.61, 계산값 0.415, 문서값 0.42, 차이 0.005 / return_reason 5, 1.0, 1.000, 1.0, 0.000 / shipping_issue 5, 0.74, 0.675, 0.67, 0.005 / requested_resolution 4, 0.4, 0.200, 0.2, 0.000 / tone 3, 0.84, 0.760, 0.76, 0.000',S_X)
b+=P('다섯 건 모두 문서의 값과 0.005 안에서 맞았습니다.','0.005의 차이는 문서에 표시된 확률이 소수 둘째 자리로 반올림되어 있어서 생긴 것으로 보입니다. (제 추정입니다.)')
b+=P('**confidence는 따로 내려오는 신비한 값이 아니라, 확률 분포에서 계산되는 통계였습니다.**','문서도 "분포를 요약하는 한 가지 방법"이라고 적고, 확률 전체를 같이 주니 필요한 지표를 직접 계산해도 된다고 안내합니다.')
b+=HR()
b+=H1('4. 확률이 있으면 엣지 함수가 달라진다')
b+=IMG(7,'목_07_공식문서_TypeSafe_세갈래.png','TypeSafe 공식 문서 Three paths for using confidence in your code: High confidence는 자동으로 처리, Medium confidence는 조심해서 진행(사용자 확인, 검토 표시, 정보 추가 수집), Low confidence는 실행하지 않고 사람에게 보내거나 다시 묻거나 다른 시스템으로 넘긴다. 경계를 어디에 둘지는 걸린 것의 크기에 달렸다',S_CF)
b+=P('TypeSafe 문서는 confidence를 세 구간으로 나눠 쓰는 것을 출발점으로 권합니다.')
b+=TABLE(['구간','문서의 안내'],[
['높음','자동으로 처리한다. 사람의 개입 없이 진행해도 된다'],
['중간','조심해서 진행한다. 사용자에게 확인받거나, 검토 대상으로 표시하거나, 정보를 더 모은다'],
['낮음','실행하지 않는다. 사람에게 보내거나, 다시 묻거나, 다른 시스템으로 넘긴다']])
b+=P('2장의 ④ 엣지 함수에 이 규칙을 한 줄 넣을 수 있습니다.')
b+=CODE('''def route_decision(state: State):
    if state["confidence"] < 0.3:
        return "manual_triage"      # 어느 팀인지 불분명하면 사람이 정한다
    return state["department"]      # returns / shipping / billing''',[('def ','#74c0fc'),('if ','#74c0fc'),('return','#74c0fc'),('0.3','#ffd43b'),('# 어느 팀인지 불분명하면 사람이 정한다','#868e96'),('# returns / shipping / billing','#868e96')])
b+=P('`confidence`가 0.3보다 낮으면 팀으로 보내지 않고 사람의 분류로 넘깁니다.','그렇지 않으면 고른 팀으로 보냅니다.','(0.3은 문서의 예시 코드가 쓴 값입니다. 문서는 기준값을 일의 위험도에 맞춰 정하고, 자기 데이터로 시험해 조정하라고 적습니다.)')
b+=P('문서의 예시 코드는 이 문의를 이렇게 처리합니다.')
b+=TABLE(['문서 예시 코드의 처리','근거가 된 숫자'],[
['반품 팀에 배정한다','department의 confidence 0.42가 기준 0.3을 넘는다'],
['**결제 팀에도 사본을 보낸다**','billing의 확률 0.35가 기준 0.25를 넘는다'],
['**무엇을 원하는지 고객에게 되묻는다**','원하는 해결(환불 0.4, 재발송 0.34, 교환 0.24)의 confidence 0.20이 기준 0.5보다 낮다']])
b+=P('두 번째와 세 번째 줄이 눈에 띄었습니다.','"2등 팀에도 알린다"와 "애매하면 되묻는다"는','**값 하나만 받아서는 짤 수 없는 분기**입니다.')
b+=P('주의할 점도 문서에 있습니다.','"**confidence는 확률이 얼마나 한쪽으로 몰렸는지를 재는 값이고, 고른 답이 맞을 확률과는 다르다.**"','Choice는 맞는 선택지가 없어도 **반드시 하나를 고른다**는 점도 적혀 있습니다. 목록 밖의 문의가 올 수 있으면 "이 중에 해당하는 것이 있는가"를 묻는 Noul을 함께 보내라고 안내합니다.')
b+=HR()
b+=H1('5. 나란히 놓고 보기')
b+=IMG(8,'목_08_비교표.png','LLM structured output과 Jev 비교표: 형식 보장(둘 다 된다), 돌아오는 것(값 / 값+선택지마다의 확률+confidence), 애매한 입력(값 하나를 채움 / 확률이 갈려서 옴), 만드는 방식(토큰을 하나씩 / 모든 출력을 한 번에), 판정 외의 일(답변 작성·요약·추론 / 못 한다), 속도·가격(모델마다 다름 / 70~500ms, 입력 100만 토큰당 $0.042 발표 기준)')
b+=TABLE(['','LLM structured output','Jev (System One)'],[
['형식 보장','된다. 스키마를 따르고 열거형 값이 제한된다','된다. 정해 준 선택지 안에서만 답한다'],
['돌아오는 것','스키마에 맞춘 값','값 + 선택지마다의 확률 + confidence'],
['애매한 입력','그래도 값 하나를 채운다','확률이 갈려서 온다. 되묻기·넘기기 규칙을 코드로 건다'],
['판정 외의 일','답변 작성, 요약, 여러 단계 추론도 한다','못 한다. 생성·계산·날짜 비교는 맡기지 말라고 문서가 적는다'],
['속도·가격','모델마다 다르다','발표 기준 70~500ms, 입력 100만 토큰당 $0.042']])
b+=IMG(9,'목_09_공식블로그_표_비용속도.png','TypeSafe 발표문 비교표의 Cost, Speed, Confidence 줄: 기존 LLM은 입력 $0.20~$10 / MTok에 출력은 약 5배, 응답 3~329초, 확신도를 물어도 과신하고 일관되지 않는 경향. System One + Jev는 입력 $0.042 / MTok에 출력 무료, 응답 70~500ms, 모든 출력에 confidence와 불확실성을 함께 전달',S_BLOG)
b+=P('속도와 가격은 TypeSafe 발표문의 표에서 온 숫자입니다.','그대로 받아들이기 전에, 발표문이 직접 단 단서를 같이 봐야 합니다.')
b+=BOX('**발표문이 직접 적은 단서**','속도 측정은 대체로 미국 서부의 자기들 노트북에서 했다.','가격이 보조금으로 유지되는 것이 아님은 "증명할 수 없다".','비교한 LLM에는 확률까지 내도록 감싼 래퍼를 썼고, 이 방식은 확률 없이 답만 받을 때보다 느리고 비싼 경향이 있다.','홈페이지의 "193.6배 빠르고 444.6배 싸다"는 실제 이득의 높은 쪽 끝일 것으로 예상한다.')
b+=P('마지막 두 줄이 중요합니다.','193.6배와 444.6배는 **"확률까지 내도록 감싼 LLM"과 견준 숫자**입니다.','제가 평소에 쓰는 "값 하나만 받는 structured output"과 견준 숫자가 아닙니다.','제 환경에서의 차이는 직접 재 봐야 알 수 있습니다. (확인 필요)')
b+=HR()
b+=H1('6. 그럼 버튼이 더 낫지 않나: 싼 것부터 쓴다')
b+=P('여기까지 듣고 이렇게 되물었습니다.')
b+=Q('그럼 기존에 그냥 고전적인 챗봇형태에서 사용자에게 버튼을 클릭해서 라우팅 되게끔 구현한 단순 스크립트기반의 형태가 더 좋은 거 아닌가?')
b+=P('맞는 말이었습니다.','**버튼으로 되는 일은 버튼이 가장 좋습니다.**','모델이 없으니 틀릴 일도, 호출 비용도, 기다리는 시간도 없습니다.')
b+=P('TypeSafe 문서의 설계 안내도 첫 원칙이 이것입니다.','"**코드로 할 수 있으면 코드로 하라. 결정적인 일은 코드에 둔다. 믿을 수 있고 싸다.**"')
b+=P('판정이 필요해지는 것은 **자유롭게 쓴 글**이 들어올 때입니다.','이 글의 예시 문의처럼 한 문장에 반품, 배송, 결제가 섞여 있으면','"반품 / 배송 / 결제" 버튼 셋 중 하나를 고르게 해도 나머지 둘이 빠집니다.')
b+=IMG(10,'목_10_도식_싼것부터.png','싼 것부터, 안 되는 것만 다음으로: 1 코드·버튼(정해진 선택, 날짜와 금액 계산, 규칙) → 자유롭게 쓴 글이 들어와 규칙으로 못 가를 때 → 2 판정 모델(정해 둔 칸 중 하나 고르기, 예/아니오를 확률로) → 확률이 낮거나 글을 써야 하거나 여러 단계로 따져야 할 때 → 3 LLM·사람(답변 문장 쓰기, 여러 단계 추론, 최종 판단)')
b+=TABLE(['단계','맡기는 일','근거'],[
['1. 코드·버튼','정해진 선택, 날짜·금액 계산, 규칙으로 적을 수 있는 분기','TypeSafe 문서: Use code when you can'],
['2. 판정 모델','자유롭게 쓴 글을 읽고 정해 둔 칸 중 고르기','Choice, Noul'],
['3. LLM·사람','답변 문장 쓰기, 여러 단계 추론, 가르지 못한 건의 판단','TypeSafe 문서: 생성은 생성 모델로, 낮은 confidence는 사람이나 추론 모델로']])
b+=P('TypeSafe 문서에는 "Noul로 먼저 걸러라"는 패턴도 있습니다.','다음 단계가 **더 큰 입력, 더 느린 모델(LLM 호출), 사람** 중 하나를 필요로 할 때,','그 앞에 예/아니오 질문 하나를 먼저 두라는 것입니다.')
b+=P('**==판정 모델은 LLM을 없애는 것이 아니라, LLM까지 가야 하는 건수를 줄이는 자리에 놓입니다.==**')
b+=HR()
b+=H1('7. 실제로 바꾼 사례 (발표 기준)')
b+=Q('오케이 실제로 그러면 사람들이 기존 방식을 jev로 바꾼 실제 예제를 한 번 설명해줘')
b+=P('당사자가 직접 낸 자료로 확인되는 것 두 가지만 적습니다.','수치는 모두 당사자의 발표입니다.')
b+=H2('Browser Use의 jev-ultrafast')
b+=IMG(11,'목_11_GitHub_jev-ultrafast.png','GitHub 저장소 browser-use/jev-ultrafast의 README: A browser agent with a dynamic, indexed action space. Give it one goal. TypeSafe\'s Jev picks an operation and an element. A small LLM writes text only when the operation is TYPE_TEXT. Zürich → London on Google Flights in 7.1 seconds',S_GH)
b+=P('브라우저를 대신 조작하는 에이전트입니다.','README의 설명은 두 문장입니다.','"**목표 하나를 주면, TypeSafe의 Jev가 동작과 대상 요소를 고른다.**"','"**작은 LLM은 동작이 TYPE_TEXT일 때만 글을 쓴다.**"')
b+=P('고를 수 있는 동작은 CLICK, TYPE_TEXT, SELECT, SCROLL_UP, SCROLL_DOWN, WAIT, DONE, BLOCKED로 정해져 있습니다.','**"무엇을 누를지 고르는 일"은 판정 모델이, "입력칸에 넣을 글을 쓰는 일"만 LLM이** 맡는 분업입니다.','6장의 2단계와 3단계가 그대로 나뉘어 있습니다.')
b+=P('README에는 Google Flights에서 취리히 → 런던 항공편을 찾는 데 7.1초가 걸렸다는 측정이 실려 있습니다. (저장소가 밝힌 수치)','지금은 이 방식이 Browser Use의 ultrafast 모드로 들어갔고, 저장소는 처음의 실험으로 남겨 둔다고 적혀 있습니다.','(그 모드가 지금도 Jev를 쓰는지는 README에서 확인하지 못했습니다.)')
b+=H2('Jack & Jill의 후보 1차 선별')
b+=P('TypeSafe 블로그의 사례 글(2026-10-07)입니다.','Jack & Jill은 AI 에이전트가 구직자와 채용 팀을 이어 주는 인재 매칭 서비스입니다.')
b+=P('바꾸기 전에는 채용 건마다 후보 6,000명을 저가 LLM(Gemini 3.1 Flash Lite)으로 채점해 2,000명으로 줄이고,','그 2,000명을 더 높은 성능의 모델이 다시 검토했습니다.','이 가운데 **앞의 1차 채점만** Jev로 바꿨다고 합니다.')
b+=TABLE(['항목','이전 (Gemini 3.1 Flash Lite)','이후 (Jev)'],[
['후보 1,000명당 비용','$0.755','$0.092'],
['한 채용 건의 후보를 모두 거르는 시간 (중앙값)','20.3초','10.3초'],
['채용 담당자가 만나자고 한 후보를 남긴 비율','93.9%','94.6%']])
b+=P('읽을 때 붙여야 할 단서가 있습니다.','TypeSafe가 낸 사례 글이고, 품질 차이(93.9% → 94.6%)는 통계적으로 유의하지 않다고 글에 적혀 있습니다.','그리고 2,000명을 다시 검토하는 뒷단계는 여전히 더 높은 성능의 모델이 맡습니다.','**싼 것부터 거르는 구조는 그대로 두고, 앞단의 부품만 바꾼 사례**입니다.')
b+=P('Vercel은 AI Gateway에서 Jev를 제공한다고 공지했습니다(2026-09-16).','다만 Vercel이 자기 서비스에 적용했다는 이야기는 Vercel 공식 페이지에서 확인하지 못해 싣지 않았습니다.')
b+=HR()
b+=H1('8. 정리')
b+=IMG(12,'목_12_정리카드.png','정리 카드: 층이 다르다(LangGraph는 보내는 배선, Jev는 정하는 부품), 형식은 둘 다 지킨다, 갈리는 것은 확률이다(returns 0.61 / billing 0.35, confidence 0.42), 싼 것부터 쓴다(코드·버튼 → 판정 모델 → LLM·사람)')
b+=TABLE(['내가 처음 생각한 것','확인한 것'],[
['Jev는 StateGraph 라우팅과 자리를 다투는 도구다','층이 다르다. 그래프는 배선이고, Jev는 라우팅 노드 안에 끼우는 판정 부품이다'],
['Jev의 강점은 형식이 보장된다는 것이다','LLM structured output도 스키마를 따른다. 갈리는 것은 선택지마다의 확률이 같이 오느냐다'],
['confidence는 모델이 따로 내는 점수다','확률 분포에서 계산되는 통계다. 문서의 공식으로 검산하니 0.005 안에서 맞았다'],
['버튼으로 고르게 하는 편이 더 낫지 않나','버튼으로 되는 일에는 맞는 말이다. 판정 모델은 자유롭게 쓴 글이 들어오는 자리에 쓴다']])
b+=BOX('**확인된 것과 확인되지 않은 것**','확인됨(공식 문서): LangGraph Routing 예제의 구성, OpenAI Structured Outputs의 스키마 준수 설명, Jev의 Choice 응답 형식과 예제 문의의 응답 기록, confidence 공식과 세 구간 안내, "코드로 할 수 있으면 코드로" 원칙, Choice가 반드시 하나를 고른다는 점','확인됨(당사자 발표): 발표문의 속도·가격 수치와 단서, Browser Use 저장소의 구조와 7.1초 측정, Jack & Jill 사례의 비용·시간·품질 수치','확인됨(실제 실행): 문서의 확률로 confidence 공식을 검산한 계산 다섯 건','확인 필요: 이 글의 LangGraph·Jev 코드가 그대로 실행되는지, 같은 문의에서 두 방식의 실제 속도·비용·정확도, 한국어 문의에서의 판정 품질, OpenAI 외 제공자의 structured output 보장 범위')
b+=HR()
b+=H1('알게 된 것')
b+=P('**질문이 "A냐 B냐"로 보일 때, 둘이 같은 층에 있는지부터 봐야 했습니다.**','LangGraph와 Jev는 고르는 관계가 아니라 끼우는 관계였습니다.','그래프는 그대로 두고, 라우팅 노드 안의 모델 호출만 바꾸는 것입니다.')
b+=P('**"형식 보장"은 차이가 아니었습니다.**','그 부분은 LLM의 structured output도 합니다.','차이는 답 옆에 확률이 같이 오느냐였고, 그 확률이 있어야 "2등 팀에도 알린다", "애매하면 되묻는다" 같은 분기를 코드로 짤 수 있습니다.')
b+=P('**그리고 버튼으로 되는 일은 버튼으로 하는 것이 맞습니다.**','판정 모델이 들어갈 자리는 그 다음,','자유롭게 쓴 글을 읽어야 하지만 글을 써낼 필요는 없는 칸이었습니다.')
b+=HR()
b+=H1('참고자료')
b+=P('[[LangChain 공식 문서 - Workflows and agents (Routing)|https://docs.langchain.com/oss/python/langgraph/workflows-agents]]')
b+=P('[[OpenAI 공식 문서 - Structured Outputs|https://developers.openai.com/api/docs/guides/structured-outputs]]')
b+=P('[[TypeSafe 공식 문서 - Choice|https://docs.typesafe.ai/primitives/choice]]')
b+=P('[[TypeSafe 공식 문서 - Confidence|https://docs.typesafe.ai/confidence]]')
b+=P('[[TypeSafe 공식 문서 - How to build with TypeSafe|https://docs.typesafe.ai/concepts/how-to-build-with-system-one]]')
b+=P('[[TypeSafe 공식 문서 - Companion Noul|https://docs.typesafe.ai/patterns/companion-noul]]')
b+=P('[[TypeSafe 공식 문서 - Screen with a Noul first|https://docs.typesafe.ai/patterns/noul-screen]]')
b+=P('[[TypeSafe 공식 문서 - Model jaggedness|https://docs.typesafe.ai/model-jaggedness]]')
b+=P('[[TypeSafe 공식 블로그 - Introducing System One Models & Jev|https://typesafe.ai/blog/introducing-system-one-models-and-jev]]')
b+=P('[[TypeSafe 공식 블로그 - How Jack & Jill Cut Candidate Screening Costs By 88% With Jev|https://typesafe.ai/blog/jack-jill-jev-case-study]]')
b+=P('[[GitHub - browser-use/jev-ultrafast|https://github.com/browser-use/jev-ultrafast]]')
b+=P('[[Vercel Changelog - TypeSafe AI\'s Jev now available on AI Gateway|https://vercel.com/changelog/typesafe-ai-jev-now-available-on-ai-gateway]]')
b+=P('#Jev #TypeSafe #LangGraph #structuredoutput #라우팅 #StateGraph #판정모델 #LLM기초 #AI활용 #개발입문')
import os
PAGE(T,b,os.environ.get('OUT','/home/claude/out/thu/2026-11-26_목_Jev_vs_LLM_structured_output.html'))
print('ok')

from lib import *
# 대표 예시: api-sdk-lab — 로컬 Ollama의 같은 모델(llama3.2)을 01_api_direct.py(requests) / 02_sdk_example.py(openai) / 03_langchain_example.py(ChatOpenAI)로 호출
T='[AI활용] API 직접 호출 vs SDK vs LangChain 차이: 같은 Ollama 서버를 세 가지로 호출하면'
SO='출처: Ollama 공식 문서(docs.ollama.com), 2026-11-15 캡처'
SK='출처: openai-python 공식 저장소 README(github.com/openai/openai-python), 2026-11-15 캡처'
SL='출처: LangChain 공식 문서(docs.langchain.com), 2026-11-15 캡처'
SQ='출처: Requests 공식 문서(requests.readthedocs.io, 2.34.2), 2026-11-15 캡처'
SX='샌드박스에서 OpenAI 형식으로 응답하는 로컬 시험 서버를 띄우고 requests로 실제 요청한 결과 (Ollama 자체는 설치되지 않아 답변 문장은 시험 서버의 고정 응답입니다)'
b=''
b+=IMG(1,'수_01_썸네일.png','대표 이미지(썸네일)')
b+=P('LLM을 부르는 방법이 세 가지나 됩니다.','`requests`로 직접 부르기, `openai` SDK로 부르기, LangChain의 `ChatOpenAI`로 부르기.','셋이 뭐가 다른지 말로만 들어서는 감이 안 와서,','**로컬 Ollama의 같은 모델을 세 파일로 따로 호출**해 보는 실습(`api-sdk-lab`)을 했습니다.')
b+=Q('sdk, api, langchain(프레임워크) 사이에서의 개념과 각자의 장단점에 대해서 정확하게 인지하고 사용한다.')
b+=P('결론부터 적으면,','**==세 파일의 최종 목적지는 완전히 같은 주소(`/v1/chat/completions`)였습니다.==**','차이는 "무엇을 하느냐"가 아니라 **"얼마나 감추느냐"**였습니다.','편해지는 만큼, 안 보이게 됩니다.')
b+=BOX('**이 글의 기준**','확인 날짜: 2026-11-15 (실습 기록은 2026-08-11)','근거: 제 실습 학습 기록(api-sdk-lab) + Requests 공식 문서(Quickstart), Ollama 공식 문서(OpenAI compatibility), openai-python 공식 README, LangChain 공식 문서(ChatOpenAI integration)','실행 화면: 1단계(requests)는 이번에 샌드박스에서 OpenAI 형식으로 응답하는 로컬 시험 서버를 띄워 실제로 다시 실행했습니다. 2·3단계는 `openai`·`langchain-openai`를 설치할 수 없어 공식 문서의 코드 형태를 옮겨 적은 것이고 실행 화면은 없습니다.','예시 이름은 실습 당시의 `api-sdk-lab`과 파일 세 개(01_api_direct.py, 02_sdk_example.py, 03_langchain_example.py)로 통일했습니다.')
b+=HR()
b+=H1('먼저 그림 하나')
b+=IMG(2,'수_02_도식_세계층.png','requests, openai SDK, LangChain ChatOpenAI 세 파일의 대표 코드와, 셋이 모두 같은 POST /v1/chat/completions 주소로 간다는 것을 보여 주는 도식')
b+=P('이게 실습에서 가장 중요한 깨달음이었습니다.','`01_api_direct.py`에는 주소가 **문자열로 그대로** 드러나 있고,','`02_sdk_example.py`에서는 `OpenAI(base_url=...)` 안에, `03_langchain_example.py`에서는 `ChatOpenAI(base_url=...)` 안에 **숨어** 있을 뿐입니다.')
b+=P('SDK도 LangChain도 마법을 부리는 게 아니라,','내부에서 결국 1단계와 똑같은 HTTP 요청을 만들어 보내고 있었습니다.','추상화가 감춰 주는 것은 "일의 내용"이 아니라 **"일의 번거로움"**입니다.')
b+=HR()
b+=H1('1단계. requests로 직접 부르기: 전부 내가 쓴다')
b+=CODE('''# 01_api_direct.py — requests로 REST API를 직접 호출
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
print("content:", data["choices"][0]["message"]["content"])   # 답을 꺼내는 경로도 내가 안다''',[('requests.post','#8ce99a'),('raise_for_status','#ffd43b'),('OLLAMA_CHAT_URL','#74c0fc')])
b+=P('한 줄씩 보면, **내가 책임지는 것**이 전부 드러납니다.','주소 문자열, 헤더, 본문 JSON의 모양, 상태 코드 확인, 응답 JSON에서 답을 꺼내는 경로.','API 문서가 바뀌면 이 줄들을 제가 고쳐야 합니다.')
b+=IMG(3,'수_03_requests_실행결과.png','01_api_direct.py를 실행한 출력(status_code 200, content)과 같은 시각 시험 서버가 남긴 로그(POST /v1/chat/completions, Authorization 헤더, model과 messages)',SX)
b+=P('이번에 다시 실행해 보니, 서버 쪽 로그에 **코드에 쓴 주소 그대로** 요청이 도착했습니다.','`Authorization: Bearer ollama` 헤더와 `model`, `messages`도 제가 적은 그대로입니다.','투명하다는 말이 이런 뜻이었습니다. 오가는 것이 전부 보입니다.')
b+=IMG(4,'수_04_공식문서_requests.png','Requests 공식 문서 Quickstart: json 파라미터로 dict를 넘기면 자동으로 인코딩된다는 설명과, 4XX·5XX 응답은 raise_for_status()로 예외를 낼 수 있다는 설명',SQ)
b+=P('이 두 줄의 근거는 Requests 문서에 있습니다.','"**`json` 파라미터로 직접 넘기면 자동으로 인코딩된다**"(단, `data`나 `files`가 있으면 무시),','"**잘못된 요청(4XX, 5XX)이면 `Response.raise_for_status()`로 예외를 낼 수 있다**".','문서에는 `r.json()`이 성공했다고 응답이 성공한 건 아니라는 주의도 있습니다. 서버가 오류 내용을 JSON으로 줄 수도 있으니 상태 코드를 따로 봐야 합니다.')
b+=HR()
b+=H1('2단계. openai SDK로 부르기: 주소는 한 번만, 오류는 예외로')
b+=IMG(5,'수_05_공식문서_Ollama_OpenAI호환.png','Ollama 공식 문서 OpenAI compatibility의 /v1/chat/completions 예시: OpenAI(base_url=http://localhost:11434/v1/, api_key=ollama # required but ignored)와 chat.completions.create',SO)
b+=P('Ollama 문서의 예시가 2단계 코드 그 자체입니다.','"**Ollama는 OpenAI API의 일부를 지원한다**"고 하면서,','`OpenAI(base_url="http://localhost:11434/v1/", api_key="ollama")`로 클라이언트를 만듭니다.','`api_key`는 "**필요하지만 무시된다(required but ignored)**"고 적혀 있습니다.')
b+=CODE('''# 02_sdk_example.py — openai SDK로 호출 (공식 문서의 형태를 옮겨 적음)
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1/",   # 주소는 여기 한 번만
    api_key="ollama",                        # 형식상 필요, Ollama는 무시
)
response = client.chat.completions.create(
    model="llama3.2",
    messages=[{"role": "user", "content": "한 문장으로 자기소개 해 주세요."}],
)
print(response.choices[0].message.content)   # dict 키가 아니라 속성으로 꺼낸다''',[('OpenAI(','#8ce99a'),('base_url','#ffd43b'),('.choices[0].message.content','#74c0fc')])
b+=IMG(6,'수_06_공식문서_OpenAI_SDK.png','openai-python 공식 README의 Chat Completions 사용 예시: OpenAI() 클라이언트와 client.chat.completions.create, completion.choices[0].message.content',SK)
b+=P('1단계와 비교하면 사라진 줄이 보입니다.','주소 조립, 헤더 작성, 상태 코드 확인, JSON 파싱이 코드에서 없어졌습니다.','대신 `response.choices[0].message.content`처럼 **속성**으로 답을 꺼냅니다. 오타를 내면 바로 에러가 나서 빨리 발견됩니다.')
b+=IMG(7,'수_07_공식문서_OpenAI_오류.png','openai-python README의 Handling errors: 연결 실패는 APIConnectionError, 4xx·5xx는 status_code와 response를 가진 APIStatusError, 모든 오류는 APIError를 상속',SK)
b+=P('오류 처리도 SDK가 맡습니다. README에 이렇게 있습니다.','"**연결할 수 없으면 `openai.APIConnectionError`의 하위 클래스가 발생한다.**"','"**4xx·5xx 응답이면 `status_code`와 `response`를 가진 `openai.APIStatusError`의 하위 클래스가 발생한다.**"','"특정 오류는 기본 2회 자동 재시도", "기본 타임아웃 10분"도 README에 적혀 있습니다. 1단계에서는 이걸 전부 제가 짜야 합니다.')
b+=P('그 대가는 **블랙박스**입니다.','SDK가 실제로 어떤 요청을 보내는지는 코드만 봐서는 모릅니다.','1단계를 한 번 해 봤기 때문에 "어차피 같은 POST를 보낸다"는 걸 알고 쓰는 것과, 모르고 쓰는 것은 다릅니다.')
b+=HR()
b+=H1('3단계. LangChain으로 부르기: 한 겹 더, 대신 제공자를 갈아 끼운다')
b+=CODE('''# 03_langchain_example.py — langchain-openai의 ChatOpenAI로 호출 (공식 문서의 형태를 옮겨 적음)
from langchain_openai import ChatOpenAI     # 설치는 langchain-openai(하이픈), import는 langchain_openai(밑줄)

llm = ChatOpenAI(
    model="llama3.2",
    base_url="http://localhost:11434/v1/",   # 역시 한 번만
    api_key="ollama",
)
response = llm.invoke("한 문장으로 자기소개 해 주세요.")
print(response.content)                      # AIMessage의 content''',[('ChatOpenAI','#8ce99a'),('invoke','#ffd43b'),('response.content','#74c0fc')])
b+=IMG(8,'수_08_공식문서_LangChain_invoke.png','LangChain 공식 문서 ChatOpenAI integration의 Invocation: llm.invoke(messages)의 결과가 AIMessage(content=...)로 나오고 ai_msg.text로 본문을 출력하는 예시',SL)
b+=P('LangChain 문서의 호출 예시입니다.','`llm.invoke(messages)`의 결과는 `AIMessage(content="...")` 객체이고,','본문은 `.content`(문서 예시에서는 `.text`)로 꺼냅니다.','2단계의 `choices[0].message.content`보다 경로가 한 번 더 짧아졌습니다. 그만큼 한 겹이 더 늘어난 겁니다.')
b+=IMG(9,'수_09_공식문서_LangChain_baseurl.png','LangChain 공식 문서: base_url 결정 순서 — 1) 명시적 base_url(또는 openai_api_base) kwarg, 2) OPENAI_API_BASE 환경변수, 3) OPENAI_BASE_URL은 밑에 있는 openai SDK 클라이언트가 읽는다',SL)
b+=P('문서에 "한 겹 더"의 증거가 있습니다.','주소를 정하는 순서가 "**1) 명시적 `base_url` kwarg, 2) `OPENAI_API_BASE`(LangChain이 읽음), 3) `OPENAI_BASE_URL`(밑에 있는 `openai` SDK 클라이언트가 읽음)**"입니다.','즉 `ChatOpenAI` 아래에는 **2단계의 `openai` SDK가 그대로** 있고, SDK 아래에는 1단계의 HTTP 요청이 있습니다.')
b+=HR()
b+=H1('세 단계를 나란히 놓으면')
b+=IMG(10,'수_10_비교표.png','대표 코드, URL을 다루는 법, 답을 꺼내는 경로, 오류 처리, 제공자 교체, 장점, 단점을 세 단계로 비교한 표')
b+=TABLE(['','1단계 API 직접 호출','2단계 SDK','3단계 LangChain'],[
['대표 코드','`requests.post(url, headers=…, json=…)`','`client.chat.completions.create(…)`','`llm.invoke(prompt)`'],
['URL','매번 전체 주소를 직접','`base_url`로 한 번만','`base_url`로 한 번만'],
['답 꺼내기','`data["choices"][0]["message"]["content"]`','`response.choices[0].message.content`','`response.content`'],
['오류 처리','상태 코드를 내가 확인','SDK가 예외로 던져 줌','SDK 예외가 그대로 전달됨'],
['제공자 교체','코드 전체 재작성','클라이언트 설정 변경','클래스만 교체, 나머지 유지'],
['장점','가장 투명함','짧고 읽기 쉬움','여러 LLM을 같은 코드 모양으로'],
['단점','번거롭고 API 변경 시 직접 수정','내부가 블랙박스','추상화가 한 겹 더 늘어 더 안 보임']])
b+=IMG(11,'수_11_도식_제공자교체.png','ChatOpenAI로 Ollama를 부르는 코드와 ChatAnthropic으로 바꾼 코드를 나란히 놓고, 클래스 이름만 바뀌고 invoke와 .content 줄은 그대로임을 보여 주는 도식')
b+=P('3단계의 진짜 이점은 **제공자를 바꿀 때** 드러납니다.','Anthropic의 API는 OpenAI와 요청·응답 형식이 달라서 `ChatOpenAI`로는 부를 수 없고 전용 패키지(`langchain-anthropic`)가 필요합니다.','그런데 클래스 이름만 `ChatOpenAI` → `ChatAnthropic`으로 바꾸면 **`invoke`와 `.content` 줄은 그대로** 재사용됩니다.','1단계였다면 URL, 헤더, JSON 구조를 전부 다시 써야 합니다.')
b+=Q('왜 langchain.openai가 아니라 langchain_openai인가?')
b+=P('실습 중에 걸렸던 질문입니다. 점(`.`)이 아니라 밑줄(`_`)인 게 이상해 보였습니다.','답은 `langchain_openai`가 `langchain` 안의 하위 모듈이 아니라 **따로 설치되는 독립 패키지**라는 것이었습니다.','설치할 때는 `langchain-openai`(하이픈), import할 때는 `langchain_openai`(밑줄)입니다. 파이썬 식별자에 하이픈을 쓸 수 없기 때문이고, `scikit-learn` → `sklearn`과 같은 관례입니다.')
b+=HR()
b+=H1('그래서 무엇을 고르나')
b+=IMG(12,'수_12_선택기준.png','직접 호출·SDK·LangChain 각각을 고르는 상황과 공식 문서에서 확인한 근거를 정리한 카드')
b+=P('**직접 호출**은 오가는 데이터를 눈으로 확인해야 할 때. 공부, 디버깅, SDK가 없는 서버, 한 번만 부르는 작업.','**SDK**는 한 제공자(또는 호환 서버)를 안정적으로 쓸 때. 재시도·타임아웃·오류 클래스를 맡길 수 있습니다.','**LangChain**은 여러 모델을 같은 코드 모양으로 다루거나 그 위에 체인·에이전트를 쌓을 때. 단 한 번 호출하는 작업에는 오히려 과할 수 있습니다.')
b+=P('그리고 위 단계가 막히면 **한 단계 아래로 내려가** 요청을 직접 봅니다.','세 층이 같은 요청을 보낸다는 걸 알고 있으면 내려갈 수 있습니다.')
b+=BOX('**확인된 것과 확인되지 않은 것**','확인됨(실제 실행): requests로 보낸 요청이 코드에 쓴 주소·헤더·본문 그대로 서버에 도착하는 것(로컬 시험 서버 로그)','확인됨(공식 문서): json= 자동 인코딩과 raise_for_status(Requests), Ollama의 OpenAI 호환 엔드포인트와 api_key 무시(Ollama), SDK의 오류 클래스·재시도 2회·타임아웃 10분(openai-python), invoke 결과가 AIMessage이고 base_url 결정 순서의 마지막을 밑의 openai SDK가 읽는 것(LangChain)','확인됨(실습 기록): 세 파일의 목적지가 같은 주소였다는 것, 비교표의 내용, langchain_openai 이름 규칙','확인 필요: 2·3단계 코드는 이번에 실행하지 못했습니다(패키지 설치 불가). 실제 Ollama 응답 문장도 이번 글에는 없습니다.')
b+=HR()
b+=H1('알게 된 것')
b+=P('**세 방법은 같은 요청을 보내는 세 가지 두께의 포장이었습니다.**','SDK는 번거로움을 치우고, LangChain은 제공자 차이를 치웁니다.','치운 만큼 안 보이게 되는 것도 같이 받아들이는 겁니다.')
b+=P('**한 번은 1단계로 직접 보내 보는 게 남는 공부였습니다.**','그 뒤로는 SDK나 LangChain이 "무엇을 대신해 주는지"가 보였습니다.','막히면 내려가서 볼 수 있다는 자신감도 거기서 왔습니다.')
b+=HR()
b+=H1('참고자료')
b+=P('[[Requests 공식 문서 - Quickstart|https://requests.readthedocs.io/en/latest/user/quickstart/]]')
b+=P('[[Ollama 공식 문서 - OpenAI compatibility|https://docs.ollama.com/api/openai-compatibility]]')
b+=P('[[openai-python 공식 README|https://github.com/openai/openai-python/blob/main/README.md]]')
b+=P('[[LangChain 공식 문서 - ChatOpenAI integration|https://docs.langchain.com/oss/python/integrations/chat/openai]]')
b+=P('#API #SDK #LangChain #Ollama #OpenAI호환 #requests #ChatOpenAI #LLM입문 #AI활용 #개발입문')
import os
PAGE(T,b,os.environ.get('OUT','/home/claude/out/wed/2026-11-18_수_API_vs_SDK_vs_LangChain.html'))
print('ok')

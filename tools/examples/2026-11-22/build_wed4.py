from lib import *
# 대표 예시: 도서관 문의 한 줄 "반납일이 어제까지였는데 오늘 반납해도 되나요?" + 판정할 질문 "이 문의는 연체에 관한 것인가?" (질문 이름표 is_overdue_inquiry, 설명용 값 0.91)
T='[AI활용] Jev란? 글을 쓰지 않는 System One 모델이 예/아니오를 확률로 답하는 방식'
S_SO='출처: TypeSafe 공식 문서 "System One"(docs.typesafe.ai/concepts/system-one), 2026-11-22 캡처'
S_NOUL='출처: TypeSafe 공식 문서 "Noul"(docs.typesafe.ai/primitives/noul), 2026-11-22 캡처'
S_BLOG='출처: TypeSafe 공식 블로그 "Introducing System One Models & Jev"(typesafe.ai/blog, 2026-09-15 글), 2026-11-22 캡처'
S_HF='출처: Hugging Face Transformers 공식 문서 "BERT"(huggingface.co/docs/transformers/model_doc/bert), 2026-11-22 캡처'
S_JAG='출처: TypeSafe 공식 문서 "Model jaggedness"(docs.typesafe.ai/model-jaggedness), 2026-11-22 캡처'
S_X='샌드박스(Python 3.13.17, numpy 2.5.3)에서 실제로 실행한 출력을 옮긴 화면. 숫자는 제가 정한 장난감 예시이며 실제 모델의 값이 아닙니다'
b=''
b+=IMG(1,'수_01_썸네일.png','대표 이미지(썸네일)')
b+=P('Jev라는 AI 모델 이야기를 처음 들었을 때,','가장 이상했던 점은 "글을 쓰지 않는다"는 것이었습니다.','질문을 보내면 문장이 아니라 숫자가 돌아온다고 했습니다.')
b+=P('AI 모델이라면 다음 토큰을 계속 골라','글을 이어 쓰는 물건인 줄 알았는데,','어떻게 그게 되는 걸까요.')
b+=P('결론부터 적으면,','**==Jev는 TypeSafe가 만든 모델의 이름이고, System One은 그 모델이 속한 종류의 이름입니다. 질문하는 쪽이 미리 정해 준 답의 칸에 대해서만 값과 확률을 돌려주고, 글은 만들지 않습니다. 예/아니오 질문의 답도 true/false가 아니라 "예일 확률" 숫자 하나입니다.==**')
b+=BOX('**이 글의 기준**','확인 날짜: 2026-11-22','근거: TypeSafe 공식 문서(System One, Primitives, Noul, Models, Model jaggedness, How to build with TypeSafe, AI primer), TypeSafe 공식 블로그의 발표문(2026-09-15), Transformer Explainer의 설명문, Hugging Face Transformers 문서(BERT)','**사용 후기가 아니라 공식 자료를 읽고 정리한 글입니다.** Jev를 직접 호출해 보지 못했습니다. Jev용 코드는 공식 문서의 형식을 따라 적은 것이고 실행하지 않았습니다.','실행 화면: 5장의 장난감 예시(numpy)만 샌드박스에서 실제로 실행했습니다. 실제 모델이 아닙니다.','속도와 가격은 모두 TypeSafe가 발표한 수치입니다. 직접 재 보지 못했습니다.','확인하지 못한 것: Jev의 내부 구조, 파라미터 수, 학습 방법의 상세. 공개된 자료에서 찾지 못했습니다.')
b+=HR()
b+=H1('1. 처음에 헷갈렸던 것')
b+=P('Jev를 처음 들여다보면서 이렇게 물었습니다.')
b+=Q('jev라는 게 모델이름인가?')
b+=Q('내가 알기로는 모델 학습 파라미터 자체가 계속 토큰을 확률적으로 선택할텐데 제브는 출력이 어떻게 불리언이랑 단어 하나만 나오는거지?')
b+=BOX('**당시의 생각**','Jev가 개발사 이름인지, 모델 이름인지, 서비스 이름인지 구분하지 못했다.','AI 모델은 파라미터가 토큰을 하나씩 확률로 고르는 물건이라고 알고 있었다.','그래서 불리언이나 단어 하나만 내놓는 모델이 어떻게 가능한지 이해되지 않았다.')
b+=P('그래서 세 가지를 순서대로 확인했습니다.','이름이 각각 무엇을 가리키는가.','무엇이 돌아오는가.','글 없이 답만 나오는 것이 왜 가능한가.')
b+=HR()
b+=H1('2. 이름 세 개부터: TypeSafe, Jev, System One')
b+=IMG(2,'수_02_도식_이름셋.png','이름 세 개가 가리키는 것: TypeSafe는 만든 곳(개발사), Jev는 모델 이름(API에서는 jev-1.14.0, 별칭 jev-latest), System One은 모델의 종류(글 대신 빠르고 구조화된 판단을 돌려주는 모델을 묶어 부르는 이름). 만든 곳 : 모델 이름 : 종류의 자리에 TypeSafe : Jev : System One이 들어간다')
b+=P('먼저 이름입니다.','세 단어가 같이 나와서 헷갈렸는데,','가리키는 층이 서로 달랐습니다.')
b+=IMG(3,'수_03_공식문서_SystemOne_정의.png','TypeSafe 공식 문서 System One 페이지 첫 부분: System One 모델은 소프트웨어가 바로 쓸 수 있는 빠르고 구조화된 판단을 내리도록 만든 AI 모델의 한 종류다. Jev는 TypeSafe의 대표 모델이자 첫 번째 System One 모델이다. LLM처럼 자연어 입력을 이해하지만 생성된 글이 아니라 타입이 정해진 판단과 확률을 돌려준다',S_SO)
b+=P('TypeSafe 공식 문서의 첫 문단입니다.','"**System One 모델은 소프트웨어가 바로 쓸 수 있는, 빠르고 구조화된 판단을 내리도록 만든 AI 모델의 한 종류다.**"','"**Jev는 TypeSafe의 대표 모델이자 첫 번째 System One 모델이다.**"')
b+=TABLE(['이름','가리키는 것','공식 자료에서 확인한 내용'],[
['TypeSafe','만든 곳','Jev를 만든 개발사. 사이트와 발표문에서는 TypeSafe AI라고도 적는다'],
['Jev','모델 이름','모델 ID는 `jev-1.14.0`, `jev-1.13.0`. 별칭 `jev-latest`가 최신 정식 버전을 가리킨다'],
['System One','모델의 종류','글 대신 타입이 정해진 판단과 확률을 돌려주는 모델을 묶어 부르는 이름']])
b+=P('"jev라는 게 모델이름인가?"의 답은 **"예, 모델 이름"**입니다.','System One은 "LLM"과 같은 자리에 놓이는 말이었습니다.')
b+=P('이름의 유래도 발표문에 적혀 있습니다.','System One은 대니얼 카너먼의 책 Thinking, Fast and Slow에 나오는,','빠르고 직관적인 System 1 사고에서 따왔다고 합니다.','Jev는 경제학자 윌리엄 스탠리 제번스(William Stanley Jevons)의 이름에서 따왔다고 합니다.')
b+=P('이어서 이것도 물었습니다.')
b+=Q('그러면 제브 자체가 쓰는 모델은 뭐야?')
b+=P('다른 LLM을 감싸서 만든 서비스인지가 궁금했던 것인데요.','공식 자료에서 확인되는 것은 여기까지입니다.')
b+=BOX('**공식 자료에 적힌 것**','발표문: "새 모델 구조, 병렬 샘플러, RLCD라는 학습 방법"으로 새로 만들었다고 한다.','발표문의 FAQ "Jev는 그냥 작은 LLM인가?" → "**Jev는 작지도 않고 LLM도 아니다.**"','AI primer 문서: RLCD를, 사전 학습된 언어 모델을 다듬는 세 번째 방법으로 소개한다. (RLHF는 챗봇을, RLVR은 추론 모델을 만든 방법)','Models 문서: 고객 데이터로 따로 미세 조정하지 않고, 같은 가중치가 모든 계정에 쓰인다.','**공개되지 않은 것**: 구조의 상세, 파라미터 수, 어떤 사전 학습 모델에서 출발했는지. (확인 필요)')
b+=P('"다른 LLM 위에 얹은 서비스"라는 설명은 공식 자료에 없고,','TypeSafe는 **자기 모델**이라고 밝히고 있습니다.','다만 속을 들여다볼 자료는 공개되어 있지 않습니다.')
b+=HR()
b+=H1('3. 무엇이 돌아오나: 글이 아니라 값과 확률')
b+=P('방금 본 문서 캡처의 마지막 문단부터 다시 읽어 보겠습니다.','"**LLM처럼 System One 모델도 자연어 입력을 이해한다. 다만 생성된 글이 아니라, 타입이 정해진 판단과 확률을 돌려준다.**"')
b+=IMG(4,'수_04_공식문서_SystemOne_LLM과차이.png','TypeSafe 공식 문서 How it differs from an LLM: System One 모델은 보정된 판단을 하도록 학습되며, 답장을 쓰지 않고 코드를 만들지 않고 추론 과정의 설명도 만들지 않는다. 가능한 답은 primitive로 정한다. 표: Choice(choice: "billing"), Score(score: 1.4), Noul(noul: 0.95), Box(box: top, bottom, left, right)',S_SO)
b+=P('이어지는 "LLM과 어떻게 다른가" 부분입니다.','"**System One 모델은 답장을 쓰지 않고, 코드를 만들지 않고, 추론 과정의 설명도 만들지 않는다. 가능한 답은 primitive를 통해 당신이 정한다.**"')
b+=P('"가능한 답을 내가 정한다"가 핵심입니다.','질문을 보낼 때 **답이 들어갈 칸의 종류**를 같이 정해서 보냅니다.','그 종류가 네 가지입니다.')
b+=TABLE(['질문 타입','묻는 것','돌아오는 값'],[
['Choice','이 선택지 중 무엇인가','`choice`(고른 것), `probabilities`(선택지별 확률), `confidence`'],
['Score','어느 수준인가','`score`, `probabilities`, `confidence`'],
['Noul','이 말이 맞는가 (예/아니오)','`noul` — 0에서 1 사이의 숫자 하나'],
['Box','이미지의 어디에 있는가','`box`(위·아래·왼쪽·오른쪽), `confidence`']])
b+=P('이 글에서는 가장 단순한 **Noul** 하나만 따라가 보겠습니다.','예시는 도서관에 들어온 문의 한 줄입니다.')
b+=BOX('**이 글의 예시**','문의: "반납일이 어제까지였는데 오늘 반납해도 되나요?"','판정할 질문: "이 문의는 연체에 관한 것인가?"')
b+=P('공식 문서의 Noul 예제 형식에 이 예시를 넣으면 이런 모양이 됩니다.','(형식을 따라 적어 본 것이고, 실행해 보지는 못했습니다.)')
b+=CODE('''from typesafe_sdk import Noul, TypeSafeClient

with TypeSafeClient() as client:
    response = client.system_one(
        model="jev-latest",
        state="반납일이 어제까지였는데 오늘 반납해도 되나요?",
        questions={
            "is_overdue_inquiry": Noul(
                instructions="이 문의는 연체에 관한 것인가?",
            ),
        },
    )

print(response.answers["is_overdue_inquiry"].noul)''',[('from ','#74c0fc'),('import','#74c0fc'),('with ','#74c0fc'),(' as ','#74c0fc'),('state=','#ffd43b'),('questions=','#ffd43b'),('.noul','#8ce99a')])
b+=P('`state`는 판정할 대상입니다. 여기서는 문의 글 한 줄입니다.','`questions`는 묻고 싶은 것의 목록입니다.','`is_overdue_inquiry`는 제가 붙인 이름표이고, 답도 이 이름표 아래로 돌아옵니다.','`Noul(instructions=...)`가 질문 본문입니다.','타입을 Noul로 정했으니 답의 칸은 "예/아니오"로 고정됩니다.','`model="jev-latest"`는 2장에서 본 모델 별칭입니다.','마지막 줄은 돌아온 답에서 `noul` 값을 꺼내 출력합니다.')
b+=P('돌아오는 모양은 공식 문서의 응답 예에서 볼 수 있습니다.','("고객이 사람 상담원을 원하는가"를 물은 예제의 답 부분입니다.)')
b+=CODE('''"is_human_escalation": {
  "type": "noul",
  "noul": 0.99
}''',[('0.99','#8ce99a')])
b+=P('문장이 없습니다. **타입 이름과 숫자 하나**가 전부입니다.','제 예시라면 `"noul": 0.91` 같은 값이 돌아올 것입니다.','(0.91은 설명을 위해 제가 적은 숫자입니다. 실제 응답이 아닙니다.)')
b+=HR()
b+=H1('4. true/false가 아니라 "예일 확률"')
b+=P('저는 예/아니오 질문이면','불리언(true/false)이 돌아오는 줄 알았습니다.','문서를 읽어 보니 아니었습니다.')
b+=IMG(5,'수_05_공식문서_Noul_읽는법.png','TypeSafe 공식 문서 Reading a Noul: 숫자가 답이자 확신의 정도다. 1에 가까우면 강한 예, 0에 가까우면 강한 아니오. is_human_escalation 질문에 대한 jev-1.13.0의 기록: Thanks, that fixed it! 0.02 / How do I reset my password? 0.07 / I need this sorted today, whatever it takes. 0.26 / Are you a bot? 0.40 / Is there any way to speak to someone about my invoice? 0.84 / I have asked three times now. Can I please just talk to a real person? 0.99',S_NOUL)
b+=P('"**Noul의 답은 숫자 하나이고, 답이 \'예\'일 확률을 나타낸다. 0은 아니오, 1은 예다.**"','"**1에 가까우면 강한 예, 0에 가까우면 강한 아니오다. 0.5 근처면 예와 아니오에 비슷한 확률을 준 것이다.**"')
b+=P('캡처의 표는 "고객이 사람 상담원을 원하는가?"에 대한 기록입니다.','"고마워요, 해결됐어요"는 0.02,','"청구서 건으로 누군가와 얘기할 방법이 있나요?"는 0.84,','"세 번이나 물었어요. 제발 진짜 사람과 얘기하게 해 주세요"는 0.99입니다.')
b+=P('눈에 띄는 것은 가운데 줄입니다.','**"당신 봇인가요?"는 0.40**입니다.','사람을 원한다는 뜻 같기도 하고 아닌 것 같기도 한 문장에,','모델이 그대로 애매한 숫자를 줍니다.')
b+=IMG(6,'수_06_공식문서_Noul_기준값.png','TypeSafe 공식 문서: Most often your code thresholds noul into a boolean. 코드 wants_human = response.answers["is_human_escalation"].noul > 0.9, if wants_human: route_to_agent(ticket) else: route_to_bot(ticket). 시작점은 예 0.7, 아니오 0.3이며 0.3과 0.7 사이의 값은 사람에게 보낼 수 있다',S_NOUL)
b+=P('그럼 불리언은 어디서 만들까요.','같은 문서의 다음 부분입니다.','"**대부분은 코드에서 noul에 기준값을 걸어 불리언으로 바꾼다.**"','"**시작점으로는 예 0.7, 아니오 0.3이 좋다. 0.3과 0.7 사이의 값은 어느 쪽 코드로도 보내지 않고 사람에게 보낼 수 있다.**"')
b+=P('**==불리언은 모델이 주는 것이 아니라, 기준값을 건 내 코드가 만듭니다.==**','제 예시로 옮기면 이렇게 됩니다.')
b+=CODE('''p = response.answers["is_overdue_inquiry"].noul

if p > 0.7:
    send_overdue_guide()     # 연체 안내를 보낸다
elif p < 0.3:
    send_general_guide()     # 일반 안내를 보낸다
else:
    hand_to_librarian()      # 사서에게 넘긴다''',[('if ','#74c0fc'),('elif ','#74c0fc'),('else','#74c0fc'),('0.7','#ffd43b'),('0.3','#ffd43b'),('# 연체 안내를 보낸다','#868e96'),('# 일반 안내를 보낸다','#868e96'),('# 사서에게 넘긴다','#868e96')])
b+=P('첫 줄은 돌아온 확률을 `p`에 담습니다.','`p > 0.7`이면 "예"로 보고 연체 안내로 보냅니다.','`p < 0.3`이면 "아니오"로 보고 일반 안내로 보냅니다.','그 사이면 어느 쪽으로도 보내지 않고 사람에게 넘깁니다.')
b+=P('(세 함수는 설명을 위해 붙인 이름입니다.','0.7과 0.3은 문서가 권하는 시작점이고,','틀렸을 때 치르는 비용에 따라 올리거나 내리라고 적혀 있습니다.)')
b+=P('참고로 Noul에는 `confidence`가 따로 붙지 않습니다.','결과가 예/아니오 둘뿐이라','**숫자 하나가 확률 분포 전체**이기 때문이라고 문서는 설명합니다.','Choice와 Score에는 붙습니다.')
b+=HR()
b+=H1('5. 글 없이 답만 나오는 것이 왜 가능한가')
b+=P('가장 이해가 안 됐던 부분입니다.','"모델은 파라미터가 토큰을 확률로 고르는 것 아닌가"라는 생각이 걸림돌이었습니다.')
b+=H2('"토큰을 고른다"를 둘로 나눠 보기')
b+=P('GPT-2를 브라우저에서 보여 주는 도구,','Transformer Explainer의 설명을 다시 읽었습니다.','"**모든 Transformer 블록을 지난 뒤, 마지막 층에서 logits가 나온다. 50,257개의 숫자이고, GPT-2 어휘의 토큰마다 하나씩이다.**"','"**그 점수를 확률로 바꾸고, 허용된 후보 가운데 토큰 하나를 뽑는다.**"')
b+=P('여기서 두 가지가 구분됩니다.','① **모델의 계산**: 한 번 계산하면 "어휘 전체에 대한 점수표" 한 장이 나온다.','② **점수표를 쓰는 절차**: 거기서 토큰 하나를 뽑아 입력 뒤에 붙이고, 다시 계산시킨다.')
b+=P('제가 "파라미터가 토큰을 계속 고른다"고 뭉쳐서 알던 것은','①과 ②를 합친 것이었습니다.','**파라미터가 하는 일은 ①까지**이고, "계속"은 ②의 반복에서 나옵니다.')
b+=IMG(7,'수_07_도식_두방식.png','글을 쓰는 방식과 판정만 하는 방식 비교: LLM은 한 번 계산하면 어휘 전체에 대한 점수표(GPT-2 small은 50,257칸)가 나오고, 토큰 하나를 뽑아 입력 뒤에 붙인 뒤 끝날 때까지 다시 계산한다. 판정 방식은 정해 준 답에 대한 확률표(예/아니오면 2칸)를 한 번 계산해 그대로 돌려주며 반복이 없다')
b+=P('그러면 두 군데를 바꾸면 됩니다.','점수표의 칸을 "어휘 전체"가 아니라 **"미리 정해 준 답"**으로 두고,','뽑아서 붙이는 **반복을 빼는 것**입니다.','그러면 글이 아니라 "답마다의 확률"이 한 번에 나옵니다.')
b+=H2('이런 구조는 전부터 있었다')
b+=IMG(8,'수_08_공식문서_HuggingFace_BERT.png','Hugging Face Transformers 공식 문서 BertForSequenceClassification: Bert Model transformer with a sequence classification/regression head on top (a linear layer on top of the pooled output) e.g. for GLUE tasks',S_HF)
b+=P('글을 쓰지 않고 분류 점수만 내는 구조는 새로 생긴 것이 아닙니다.','Hugging Face Transformers 문서는 BERT의 분류용 모델을 이렇게 설명합니다.','"**BERT 모델 위에 문장 분류용 head를 얹은 것. (모아진 출력 위에 놓인 linear layer 하나)**"')
b+=P('같은 문서 첫머리에는,','BERT가 익힌 언어 표현을 "층이나 head를 추가로 미세 조정해서" 다른 작업에 맞출 수 있다고 적혀 있습니다.','글을 읽는 몸통은 두고 **마지막에 작업용 출력 층을 얹어 학습시키면**,','나오는 것이 "다음 토큰"이 아니라 "분류 점수"가 된다는 뜻입니다.')
b+=H2('모양만 직접 돌려 보기')
b+=P('두 방식의 차이를 작은 코드로 확인해 봤습니다.','진짜 모델이 아니라,','**점수표의 칸 수와 계산 횟수**만 비교하는 장난감입니다.','점수는 제가 정한 숫자입니다.')
b+=CODE('''import numpy as np

def softmax(scores):
    # 점수 여러 개를 "합이 1인 확률"로 바꾼다
    e = np.exp(scores - scores.max())
    return e / e.sum()

# (가) 글을 쓰는 방식: 점수표의 칸 = 어휘 전체
vocab = ["<시작>", "연체", "문의", "입니다", "<끝>"]
# 앞 토큰을 보고 다음 토큰의 점수를 내는 표 (직접 정한 숫자)
next_scores = np.array([
    [-9.0,  2.0,  0.5, -1.0, -2.0],   # <시작> 다음
    [-9.0, -2.0,  2.5,  0.5, -1.0],   # 연체 다음
    [-9.0, -2.0, -2.0,  2.5,  0.0],   # 문의 다음
    [-9.0, -2.0, -2.0, -2.0,  3.0],   # 입니다 다음
    [-9.0, -9.0, -9.0, -9.0,  9.0],   # <끝> 다음
])

tokens = [0]   # <시작>에서 출발
steps = 0
while vocab[tokens[-1]] != "<끝>":
    probs = softmax(next_scores[tokens[-1]])   # 어휘 5칸에 대한 확률
    tokens.append(int(probs.argmax()))         # 가장 높은 칸 하나를 골라 붙인다
    steps += 1                                 # 그리고 다시 계산한다

# (나) 판정만 하는 방식: 점수표의 칸 = 미리 정해 준 답
answers = ["예", "아니오"]
answer_scores = np.array([2.3, 0.0])   # 직접 정한 숫자
p = softmax(answer_scores)''',[('import','#74c0fc'),('def ','#74c0fc'),('return','#74c0fc'),('while ','#ffd43b'),('tokens.append','#ffd43b'),('p = softmax(answer_scores)','#8ce99a')])
b+=P('`softmax`는 점수 여러 개를 합이 1인 확률로 바꾸는 함수입니다.','(가)와 (나)가 **같은 함수**를 씁니다.','`vocab`은 장난감 어휘 5개입니다. GPT-2 small이라면 50,257개입니다.','`next_scores`는 "앞 토큰이 이것일 때 다음 토큰의 점수"를 적은 표입니다.','진짜 모델이라면 파라미터가 계산해 낼 값인데, 여기서는 제가 숫자를 적어 넣었습니다.')
b+=P('`while` 반복이 (가)의 핵심입니다.','마지막 토큰이 `<끝>`이 될 때까지 돕니다.','한 바퀴마다 5칸짜리 확률을 계산하고,','가장 높은 칸 하나를 골라(`argmax`) 뒤에 붙입니다(`append`).')
b+=P('(나)에는 반복문이 없습니다.','칸이 "예", "아니오" 둘뿐이고,','점수 2개를 확률로 바꾸면 끝입니다.','(결과를 출력하는 `print` 줄은 줄였습니다.)')
b+=IMG(9,'수_09_실행결과_두방식.png','장난감 예시 실행 결과: (가) 점수표의 칸 수 5, 계산 횟수 4, 나온 것 "연체 문의 입니다". (나) 점수표의 칸 수 2, 계산 횟수 1, 나온 것 "예 0.91, 아니오 0.09"',S_X)
b+=P('(가)는 점수표가 5칸이고,','토큰이 하나 나올 때마다 다시 계산해서 4번 돌았습니다.','나온 것은 "연체 문의 입니다"라는 글입니다.')
b+=P('(나)는 점수표가 2칸이고, 한 번 계산하고 끝났습니다.','나온 것은 "예 0.91, 아니오 0.09"입니다.','**같은 계산인데, 칸을 무엇으로 두느냐와 반복하느냐에 따라 글이 되기도 하고 판정이 되기도 합니다.**')
b+=H2('TypeSafe가 공식으로 밝힌 것')
b+=IMG(10,'수_10_공식블로그_표.png','TypeSafe 발표문의 비교표 Frontiers, Old And New: Outputs 줄에서 기존 LLM은 Strings / generated text, System One + Jev는 Type-safe structured values(가능한 출력과 구조를 미리 정한다). Sampling 줄에서 기존 LLM은 Sequential(토큰을 하나씩, 앞의 것에 따라), System One + Jev는 Parallel(모든 출력을 한 번의 질의에서 만든다)',S_BLOG)
b+=P('그럼 Jev는 실제로 어떻게 한다고 밝혔을까요.','발표문의 비교표에서 Outputs와 Sampling 줄을 보면 됩니다.')
b+=TABLE(['','기존 LLM','System One + Jev'],[
['Outputs','문자열, 생성된 글. 소프트웨어가 쓰려면 파싱과 검증이 필요하다','타입이 정해진 구조화된 값. **가능한 출력과 구조를 미리 정한다**'],
['Sampling','**순차.** 토큰을 하나씩 만들고, 각 토큰은 앞의 것에 따라 정해진다','**병렬.** 모든 출력을 한 번의 질의에서 만든다']])
b+=P('본문에는 이렇게도 적혀 있습니다.','"**Jev는 토큰 단위로 이어서 생성하지 않고, 모든 확률을 병렬로 내놓는다.**"')
b+=P('앞에서 본 두 가지,','**칸을 미리 정하는 것과 반복을 빼는 것**이','공식 설명과 맞닿아 있습니다.')
b+=BOX('**여기서 선을 그어야 하는 부분**','BERT 문서와 장난감 코드는 "글을 쓰지 않는 모델이 원리상 가능하다"는 것을 보여 주는 일반적인 예입니다.','**Jev의 내부가 그런 구조라는 뜻이 아닙니다.** TypeSafe는 새 구조와 병렬 샘플러를 썼다고만 밝혔고, 상세는 공개하지 않았습니다.','위의 연결은 공식 문구를 바탕으로 한 제 이해(추론)입니다. Jev의 실제 구조는 확인 필요로 남깁니다.')
b+=HR()
b+=H1('6. 그 확률은 믿어도 되나')
b+=P('숫자가 돌아온다면,','그 숫자가 믿을 만한지가 다음 질문입니다.')
b+=P('TypeSafe는 Jev를 "보정된(calibrated) 판단"을 하도록 학습시켰다고 설명합니다.','학습 방법의 이름이 RLCD(Reinforcement Learning for Calibrated Decisions)입니다.')
b+=P('보정의 뜻은 공식 문서(AI primer)에 풀이되어 있습니다.','**확률 0.8을 붙인 예측들을 모아 보면, 그중 약 80%가 실제로 맞아야 한다**는 뜻입니다.')
b+=P('다만 같은 문서가 바로 단서를 답니다.','"**이 비율은 예측의 묶음에 대한 것이다. 답 하나하나에 대한 보장이 아니다.**"')
b+=P('발표문의 "환각하지 않는다"는 표현도 범위를 확인해 둘 필요가 있습니다.','근거로 든 것은 **형식의 보장**입니다.','정해 준 칸 밖의 값이 나오지 않는다는 뜻이고,','발표문도 이 0%가 실험으로 잰 수치가 아니라고 직접 적었습니다.')
b+=P('**답이 항상 옳다는 뜻은 아닙니다.**','0.91이 나와도 틀릴 수 있습니다.')
b+=HR()
b+=H1('7. 못하는 일도 공식 문서에 적혀 있다')
b+=IMG(11,'수_11_공식문서_약점표.png','TypeSafe 공식 문서 Model jaggedness의 실패 유형 표: 1 Literal reading, 2 Math and Numbers(Keep the arithmetic in code), 3 Date and time comparison(Extract components; compare in code), 4 Indirection, 5 Large state full of irrelevant detail, 6 Adversarial content, 7 Contradictory instructions and criteria, 8 Choice option order, 9 Generation(Use a generative model)',S_JAG)
b+=P('TypeSafe 문서에는 "Model jaggedness"라는 페이지가 따로 있습니다.','Jev가 잘 못하는 유형 9가지와,','그때 대신 할 일을 적어 둔 표입니다.')
b+=TABLE(['문서가 꼽은 약점','대신 할 일 (문서의 안내)'],[
['글자 그대로 읽는다 (Literal reading)','조건을 정확히 적고, 선택지마다 기준을 적는다'],
['계산과 숫자 (Math and Numbers)','산수는 코드에 둔다'],
['날짜·시간 비교 (Date and time comparison)','요소만 뽑게 하고, 비교는 코드에서 한다'],
['생성 (Generation)','생성 모델을 쓴다']])
b+=P('이 표를 보고 제 예시를 하나 고쳤습니다.','처음 메모에 적어 둔 질문은 **"이 책은 연체인가?"**였습니다.')
b+=P('그런데 연체 여부는 반납 예정일과 오늘 날짜를 비교하는 일입니다.','문서는 날짜 비교를 약점으로 꼽으며 이렇게 적습니다.','"**Jev는 날짜를 순서가 있는 값이 아니라 글자로 읽는다.**"')
b+=P('TypeSafe의 설계 안내 문서도 첫 원칙이 "코드로 할 수 있으면 코드로"이고,','거기 실린 예시가 마침 연체 일수를 날짜 뺄셈으로 구하는 코드입니다.')
b+=P('그래서 이 글의 질문을 "이 책은 연체인가?"가 아니라','**"이 문의는 연체에 관한 것인가?"**로 잡았습니다.','**==며칠 늦었는지는 코드가 계산하고, 글이 무슨 뜻인지만 판정 모델에 묻습니다.==**')
b+=HR()
b+=H1('8. 내가 한 줄로 정리했던 것 검증하기')
b+=P('공부를 마치며 이렇게 한 줄로 정리했었습니다.')
b+=Q('제브란? 기존에 텍스트 기반으로 생성형 사용되는 기존 모델 대신 불리언과 타입으로만 형성된 학습파라미터를 기준으로 컨피던스값과 함께 라우팅에 최적화된 모델임. 제브는 기존 llm을 대체하는 것이 아니라 특정 질문에 대해서 판단하고 분기시킬 때, 더 빠른 그리고 저비용의 판단이 가능함')
b+=P('공식 자료와 한 구절씩 맞춰 봤습니다.')
b+=TABLE(['내가 적은 표현','공식 자료로 확인한 것'],[
['불리언과 타입으로만 형성된 학습 파라미터','**고칠 곳.** 파라미터가 불리언으로 된 것이 아니다. 타입으로 제한되는 것은 **출력**이다. 예/아니오의 답도 불리언이 아니라 0~1 확률이다'],
['컨피던스값과 함께','**절반만 맞다.** Choice·Score·Box에는 `confidence`가 붙는다. Noul에는 따로 없고 값 자체가 확률이다'],
['라우팅에 최적화된 모델','**대체로 맞다.** 발표문은 분류·라우팅·채점·추출·분기를 묶어 "smart if-statements"라고 부른다. 라우팅은 그중 하나다'],
['LLM을 대체하는 것이 아니라','**맞다.** 문서는 생성이 필요하면 생성 모델을 쓰라고 적는다'],
['더 빠르고 저비용','**발표 기준으로만 확인.** 응답 70~500ms(프런티어 LLM은 3~329초), 입력 100만 토큰당 $0.042, 출력 무료. 직접 재 보지 못했다']])
b+=P('속도와 가격에는 발표문이 직접 단 단서도 있습니다.','측정은 대체로 미국 서부에 있는 자기들 노트북에서 했고,','가격이 보조금으로 유지되는 것이 아님은 "증명할 수 없다"고 적었습니다.','공개 벤치마크 점수는 일부러 발표하지 않았다고 합니다.')
b+=P('고쳐 쓴 한 줄은 이렇습니다.','**==Jev는 글을 만들지 않고, 내가 정해 준 답의 칸에 대해서만 값과 확률을 돌려주는 판정 전용 모델(System One)이다. 그 확률로 무엇을 할지는 내 코드가 정한다.==**')
b+=HR()
b+=H1('9. 정리')
b+=IMG(12,'수_12_정리카드.png','정리 카드: Jev는 모델 이름이다, 돌아오는 것은 글이 아니다, 예/아니오도 확률로 온다, 맡기지 않는 일이 있다. 내부 구조와 파라미터 수는 공개되지 않았고 속도와 가격은 개발사 발표 기준')
b+=TABLE(['내가 처음 생각한 것','확인한 것'],[
['Jev가 개발사 이름인지 모델 이름인지 모르겠다','Jev는 모델 이름. 만든 곳은 TypeSafe, 종류의 이름이 System One'],
['모델은 파라미터가 토큰을 계속 고르는 것이다','파라미터는 점수표를 계산한다. "계속"은 뽑아서 붙이는 반복 절차에서 나온다'],
['예/아니오 질문이면 불리언이 돌아온다','"예일 확률" 숫자 하나가 돌아온다. 불리언은 기준값을 건 내 코드가 만든다'],
['"연체인가?"를 모델에 물으면 된다','날짜 비교는 문서가 꼽은 약점. 날짜는 코드로, 글의 뜻만 모델에 묻는다']])
b+=BOX('**확인된 것과 확인되지 않은 것**','확인됨(TypeSafe 공식 문서·발표문): Jev와 System One의 정의, 네 가지 질문 타입과 돌아오는 값, Noul이 0~1 확률이라는 것과 기준값 안내(0.7 / 0.3), 출력을 미리 정한 구조로 제한하고 병렬로 내놓는다는 설명, 보정의 뜻과 단서, 약점 9가지, 모델 ID와 발표 가격','확인됨(다른 공식 자료): GPT-2가 어휘 50,257칸의 점수에서 토큰을 하나씩 뽑는다는 것(Transformer Explainer), 분류용 head를 얹는 구조(Hugging Face 문서)','확인됨(실제 실행): 장난감 예시의 칸 수와 계산 횟수. 구조만 보인 것이고 실제 모델이 아닙니다.','확인 필요: Jev의 내부 구조와 파라미터 수, 실제 속도와 정확도, 한국어 문의에서의 판정 품질, 이 글의 Jev용 코드가 그대로 실행되는지')
b+=HR()
b+=H1('알게 된 것')
b+=P('**"모델이 토큰을 고른다"는 말을 둘로 나누니 풀렸습니다.**','점수표를 계산하는 것과,','그 점수표에서 뽑아 붙이기를 반복하는 것.','앞의 것만 남기고 칸을 답으로 바꾸면 판정이 됩니다.')
b+=P('**예/아니오조차 숫자로 온다는 점이 가장 달랐습니다.**','모델은 확률까지만 말하고,','어디서 선을 그을지는 제가 정합니다.','0.4처럼 애매한 값이 나오면 사람에게 넘길 수 있는 것도 그 덕분입니다.')
b+=P('**예시를 공식 문서에 대어 보니, 예시가 틀려 있었습니다.**','"연체인가?"는 판정 모델이 아니라 날짜 뺄셈이 할 일이었습니다.')
b+=P('다음 글에서는 이 판정 모델을','LLM의 structured output과 나란히 놓고,','어디에 무엇을 쓸지 비교해 보겠습니다.')
b+=HR()
b+=H1('참고자료')
b+=P('[[TypeSafe 공식 문서 - System One|https://docs.typesafe.ai/concepts/system-one]]')
b+=P('[[TypeSafe 공식 문서 - Primitives (Questions)|https://docs.typesafe.ai/primitives]]')
b+=P('[[TypeSafe 공식 문서 - Noul|https://docs.typesafe.ai/primitives/noul]]')
b+=P('[[TypeSafe 공식 문서 - Models|https://docs.typesafe.ai/models]]')
b+=P('[[TypeSafe 공식 문서 - Model jaggedness|https://docs.typesafe.ai/model-jaggedness]]')
b+=P('[[TypeSafe 공식 문서 - How to build with TypeSafe|https://docs.typesafe.ai/concepts/how-to-build-with-system-one]]')
b+=P('[[TypeSafe 공식 문서 - AI primer|https://docs.typesafe.ai/introduction/machine-learning-primer]]')
b+=P('[[TypeSafe 공식 블로그 - Introducing System One Models & Jev|https://typesafe.ai/blog/introducing-system-one-models-and-jev]]')
b+=P('[[Transformer Explainer (GPT-2 시각화 도구)|https://poloclub.github.io/transformer-explainer/]]')
b+=P('[[Hugging Face Transformers 공식 문서 - BERT|https://huggingface.co/docs/transformers/model_doc/bert]]')
b+=P('#Jev #TypeSafe #SystemOne #판정모델 #LLM기초 #AI모델 #structuredoutput #라우팅 #AI활용 #개발입문')
import os
PAGE(T,b,os.environ.get('OUT','/home/claude/out/wed/2026-11-25_수_Jev란_System_One_모델.html'))
print('ok')

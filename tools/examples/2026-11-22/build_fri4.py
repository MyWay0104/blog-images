from lib import *
# 대표 예시: 직접 넣은 영어 문장 "I went to the library to borrow a" (토큰 8개, 예측된 다음 토큰 book 56.33%)
T='[AI활용] Transformer Explainer 사용법: GPT-2가 다음 단어를 고르는 과정을 브라우저에서 보기'
S_TE='출처: Transformer Explainer(poloclub.github.io/transformer-explainer), 2026-11-22 캡처'
S_TE2='출처: Transformer Explainer(poloclub.github.io/transformer-explainer), 2026-11-22 캡처. 화면이 가로로 길어 왼쪽과 오른쪽을 따로 찍어 이어 붙였습니다'
S_TE3='출처: Transformer Explainer(poloclub.github.io/transformer-explainer), 2026-11-22 캡처. 설명 상자와 표를 따로 찍어 위아래로 붙였습니다'
S_TE4='출처: Transformer Explainer(poloclub.github.io/transformer-explainer), 2026-11-22 캡처. Temperature 0.2일 때와 2일 때를 나란히 붙였습니다'
S_X='샌드박스(Python 3.13.17)에서 실제로 실행한 출력을 옮긴 화면. 입력 숫자는 도구 화면에 표시된 logit과 확률입니다'
b=''
b+=IMG(1,'금_01_썸네일.png','대표 이미지(썸네일)')
b+=P('LLM이 글을 만드는 과정을 그림으로 보여 주던 사이트가 있었는데,','이름이 기억나지 않았습니다.','기억나는 것은 화면 하나뿐이었습니다.')
b+=Q('이거 말고 약간 그 레이어 계속 몇 층의 레이어를 뛰어넘어가지고 화살표로 시각화된 페이지가 있었는데 그건 뭐야?')
b+=P('찾아보니 Transformer Explainer였습니다.','이번에는 이름만 확인하고 넘어가지 않고, 직접 문장을 넣어 끝까지 눌러 봤습니다.')
b+=P('결론부터 적으면,','**==Transformer Explainer는 GPT-2 (small)를 브라우저 안에서 실제로 돌리면서, 넣은 문장의 "다음 토큰 하나"가 정해지는 과정을 그림으로 보여 주는 도구입니다. 설치는 필요 없고, 영어 문장을 넣고 Generate를 누르면 됩니다. 레이어를 건너뛰던 그 선은 residual connection이었습니다.==**')
b+=BOX('**이 글의 기준**','확인 날짜: 2026-11-22','대상: Transformer Explainer (poloclub.github.io/transformer-explainer). 안에서 도는 모델은 GPT-2 (small)','환경: Windows PC의 데스크톱 브라우저','근거: 도구 화면의 안내문과 아래쪽 설명 글, 도구의 공개 소스 코드 일부(GitHub의 poloclub/transformer-explainer)','실행: 문장 하나를 직접 넣어 Generate, 돋보기, Temperature를 눌러 본 화면을 실었습니다. 확률 계산은 화면의 숫자로 따로 검산했습니다.','확인하지 못한 것: 한국어 문장, Top-p, 다른 head와 다른 블록 넘겨 보기, 모바일 화면, 단어 수 제한에 걸리는 경우')
b+=HR()
b+=H1('1. 처음에 헷갈렸던 것')
b+=P('이름을 찾은 뒤에도 한 가지가 걸렸습니다.')
b+=Q('트랜스포머, 익스플레이너 이거 맞는 것 같아. 근데 내가 봤던 화면은 이거랑 거의 똑같은데 내가 원하는 예제를 직접 입력해가지고 그게 생성되는 걸 볼 수 있었거든.')
b+=BOX('**당시의 생각**','"화살표가 레이어를 건너뛰는 그림이 있는 사이트"로만 기억하고 있었다.','정해진 예시만 보여 주는 설명 페이지인지, 내 문장을 넣어 볼 수 있는 도구인지 헷갈렸다.','그 화살표가 무엇을 뜻하는지는 몰랐다.')
b+=P('그래서 세 가지를 확인했습니다.','내 문장을 넣을 수 있는가.','화면의 각 부분은 무엇인가.','건너뛰는 화살표는 무엇인가.')
b+=HR()
b+=H1('2. Transformer Explainer는 무엇인가')
b+=IMG(2,'금_02_첫화면_안내팝업.png','Transformer Explainer를 처음 연 화면: 위쪽에 Examples, 입력칸(Data visualization empowers users to + 보라색 visualize), Generate 버튼. 가운데에 Embedding과 Transformer Block 1의 Multi-head Self Attention 그림. 아래에 What is Transformer? 안내 상자(1 / 20)',S_TE)
b+=P('처음 열면 기본 예시 문장과 함께 안내 상자가 뜹니다.','안내문은 이 도구를 이렇게 소개합니다.','"**여기서는 GPT-2 (small)을 쓴다. 최신 모델보다 단순하지만 기본을 익히기에는 알맞다.**"','"**Transformer는 마법이 아니다. \'이 입력 다음에 올 가장 그럴듯한 단어는 무엇인가\'를 물으며 글을 한 단계씩 만든다.**"')
b+=P('아래쪽 설명 글에는 구현 방식도 적혀 있습니다.','"**브라우저 안에서 직접 실행되는 GPT-2 (small) 모델을 담고 있다.**"','GPT-2 (small)의 파라미터는 1억 2,400만 개라고 합니다.','만든 곳은 미국 조지아 공대(Georgia Institute of Technology)의 연구진입니다.')
b+=H2('준비물과 환경')
b+=TABLE(['항목','내용'],[
['주소','poloclub.github.io/transformer-explainer'],
['설치','없음. 브라우저로 열면 된다'],
['기기','데스크톱 브라우저. 소스 코드에는 모바일에서 예시만 쓰도록 안내하는 문구가 있다 (모바일에서 확인하지는 못함)'],
['첫 접속','모델을 내려받는 동안 "Try the examples while GPT-2 model is being downloaded (600MB)" 안내가 뜬다'],
['입력','영어 문장. 소스 코드에 단어 수 제한(12)이 있다 (직접 넘겨 보지는 않음)']])
b+=P('**600MB**라는 숫자는 미리 알고 여는 편이 좋습니다.','처음 한 번은 내려받는 시간이 걸리고,','그동안에는 Examples의 예시 문장만 쓸 수 있습니다.')
b+=HR()
b+=H1('3. 1단계: 문장을 넣고 Generate 누르기')
b+=IMG(3,'금_03_전체화면_내문장.png','직접 넣은 문장 I went to the library to borrow a의 전체 화면: 위쪽 입력칸 끝에 보라색 book, 왼쪽부터 Embedding(I, went, to, the, library, to, borrow, a), Transformer Block 1의 Multi-head Self Attention(Key, Query, Value, Attention, Out), MLP, 11 more identical Transformer Blocks, Probabilities(book 56.33%, copy 26.53%, few 12.70%, couple 2.77%, bunch 1.67%)',S_TE2)
b+=P('첫 번째 확인, **내 문장을 넣을 수 있는가**부터 해 봤습니다.','넣은 문장은 이것입니다.')
b+=CODE('''I went to the library to borrow a''')
b+=P('순서는 네 번입니다.')
b+=TABLE(['순서','하는 일','화면에서 일어나는 일'],[
['①','안내 상자 오른쪽 위의 ✕를 눌러 닫는다','그림 전체가 보인다'],
['②','위쪽 입력칸을 누른다','끝에 있던 보라색 단어가 입력 글에 합쳐진다'],
['③','글을 모두 지우고 문장을 넣는다','그림은 아직 예전 문장 그대로다'],
['④','Generate를 누른다 (Enter도 같다)','그림이 내 문장으로 바뀌고, 입력칸 끝에 보라색 단어가 붙는다']])
b+=IMG(4,'금_04_입력줄.png','입력 줄을 둘로 나눠 본 모습: 윗줄은 Transformer Explainer 로고, Examples, 입력칸(...he library to borrow a + 보라색 book), Generate. 아랫줄은 Generate 오른쪽의 Temperature 슬라이더(0.8), Sampling(Top-k 선택, Top-p), k=5 슬라이더',S_TE2)
b+=P('몇 초 뒤 입력칸 끝에 보라색으로 **book**이 붙었습니다.','"도서관에 빌리러 갔다, 무엇을?"에 모델이 고른 답이 "책"입니다.')
b+=P('**==정해진 예시만 보는 페이지가 아니라, 내 문장으로 GPT-2를 직접 돌려 보는 도구가 맞았습니다.==**')
b+=P('보라색 단어는 아직 "예측"입니다.','문장에 들어간 것이 아니라, 다음에 올 토큰으로 뽑힌 후보 하나를 보여 주는 것입니다.')
b+=HR()
b+=H1('4. 2단계: 화면을 왼쪽에서 오른쪽으로 읽기')
b+=P('두 번째 확인은 화면의 각 부분입니다.','안내문은 Transformer를 세 부분으로 나눕니다.','"**Embedding은 글을 숫자로 바꾼다. Transformer 블록은 Self-Attention으로 정보를 섞고 MLP로 다듬는다. Probabilities는 다음 토큰 각각의 가능성을 정한다.**"')
b+=P('3장의 전체 화면이 바로 이 순서로 놓여 있습니다.')
b+=TABLE(['화면의 위치','이름','하는 일 (도구의 안내문 기준)'],[
['맨 왼쪽','Embedding','문장을 토큰으로 쪼개고, 토큰마다 숫자 묶음(벡터)으로 바꾼다'],
['가운데','Multi-head Self Attention','토큰끼리 정보를 주고받게 한다'],
['그 오른쪽','MLP','토큰 하나하나의 표현을 다듬는다'],
['MLP 오른쪽의 띠','11 more identical Transformer Blocks','같은 블록이 11개 더 있다. GPT-2 (small)은 모두 12개'],
['맨 오른쪽','Probabilities','다음 토큰 후보마다의 확률']])
b+=P('Attention과 MLP를 묶은 것이 "Transformer Block" 하나이고,','화면에 크게 그려진 것은 그중 첫 번째 블록입니다.','나머지 11개는 띠 하나로 접혀 있습니다.')
b+=P('이름 옆에 **돋보기**가 붙은 곳이 세 군데 있습니다.','Embedding, Attention, Probabilities.','누르면 그 부분의 계산이 펼쳐집니다. 하나씩 눌러 봤습니다.')
b+=HR()
b+=H1('5. 3단계: Embedding 펼쳐 보기')
b+=IMG(5,'금_05_Embedding_펼침.png','Embedding을 펼친 화면: Tokenization(I, went, to, the, library, to, borrow, a) → Token Embedding(id 40, 1816, 284, 262, 5888, 284, 8804, 257) + Positional Encoding(position 0~7) = 토큰마다의 벡터',S_TE)
b+=P('Embedding 옆 돋보기를 누르면 세 칸이 나옵니다.','**Tokenization → Token Embedding + Positional Encoding.**')
b+=P('제 문장은 토큰 8개로 쪼개졌고, 토큰마다 `id`가 붙었습니다.')
b+=TABLE(['토큰','I','went','to','the','library','to','borrow','a'],[
['id','40','1816','**284**','262','5888','**284**','8804','257'],
['position','0','1','2','3','4','5','6','7']])
b+=P('눈에 띄는 것은 **"to"가 두 번** 나온다는 점입니다.','"went to"의 to와 "to borrow"의 to는 쓰임이 다르지만, **id는 둘 다 284**입니다.','같은 id이니 Token Embedding에서 꺼낸 값도 같습니다.')
b+=P('두 to를 구별해 주는 것은 옆 칸의 position입니다.','하나는 2, 하나는 5.','안내문은 "**위치 인코딩은 토큰마다 문장 안에서의 자리 정보를 준다**"고 설명합니다.')
b+=P('그래도 이 단계에서는 "앞뒤 단어가 무엇인지"는 아직 들어 있지 않습니다.','그 일은 다음 칸인 Attention이 합니다.')
b+=HR()
b+=H1('6. 4단계: Attention 펼쳐 보기')
b+=IMG(6,'금_06_Attention_펼침.png','Attention을 펼친 화면: Key, Query, Value에서 나온 선이 격자로 모이고, Dot product(Q·K^T, 값 범위 -28.1~6.3) → Scaling · Mask(-3.0~3.0) → Softmax(0.0~1.0) 세 격자가 차례로 놓인다. Scaling · Mask와 Softmax 격자는 오른쪽 위 절반이 회색으로 비어 있다. 아래에 Head 1 of 12',S_TE)
b+=P('Attention 옆 돋보기를 누르면 격자 세 개가 나옵니다.','**Dot product → Scaling · Mask → Softmax.**')
b+=TABLE(['격자','안내문의 설명'],[
['Dot product','Query와 Key 벡터의 맞는 자리끼리 곱해서 더한다. attention 점수가 된다'],
['Scaling · Mask','뒤에 올 토큰을 가린다. 미리 엿보지 못하게 하기 위해서다'],
['Softmax','점수를 확률로 바꾼다. 가로줄마다 합이 1이 된다']])
b+=P('캡처를 보면 두 번째와 세 번째 격자는 **오른쪽 위 절반이 회색으로 비어** 있습니다.','가로줄 하나가 토큰 하나인데, 각 토큰이 자기보다 뒤에 있는 토큰은 보지 못하게 가린 자리입니다.','"다음 단어를 맞히는" 모델이라 답을 미리 볼 수 없게 해 둔 것입니다.')
b+=P('격자 아래의 `Head 1 of 12`는 이런 attention 계산이 12벌 있고,','지금 보는 것이 그중 첫 번째라는 뜻입니다.','옆의 화살표로 넘겨 볼 수 있게 되어 있습니다. (이번에 넘겨 보지는 않았습니다.)')
b+=HR()
b+=H1('7. 5단계: 건너뛰는 화살표의 정체')
b+=IMG(7,'금_07_Residual_점선.png','Residual 글자에 마우스를 올린 화면: Embedding 열 위에서 시작한 점선이 Multi-head Self Attention 블록 위를 가로질러 MLP 열 앞에서 내려온다. MLP 위에도 Residual 표시가 하나 더 있다',S_TE2)
b+=P('세 번째 확인, 제가 기억하던 **"레이어를 뛰어넘는 화살표"**입니다.','Embedding 열 바로 위에 작게 `Residual`이라고 적혀 있습니다.','그 글자에 마우스를 올리면 점선이 나타납니다.')
b+=P('점선은 Embedding 열에서 위로 올라가,','Attention 블록을 통과하지 않고 **그 위를 가로질러**,','MLP 앞에서 다시 내려옵니다.')
b+=P('안내문의 설명입니다.','"**residual connection은 층의 입력을 그 층의 출력에 더한다. 여러 블록을 지나는 동안 정보가 흐려지지 않게 한다. GPT-2에서는 블록마다 두 번 쓰인다.**"')
b+=P('**==건너뛰는 선은 "Attention을 거친 결과"에 "Attention에 들어가기 전의 값"을 그대로 더해 주는 길이었습니다.==**','블록마다 두 번이라는 말대로, MLP 위에도 같은 표시가 하나 더 있습니다.')
b+=P('안내문에는 dropout과 layer normalization도 함께 나옵니다.','그중 dropout은 학습 때 쓰는 것이고, **추론에서는 꺼져 있다**고 적혀 있습니다.')
b+=HR()
b+=H1('8. 6단계: Probabilities에서 다음 토큰이 정해진다')
b+=IMG(8,'금_08_Probabilities_펼침.png','Probabilities를 펼친 화면. 위: Probability of " book" token being sampled 설명 상자 — Scaled logit(logit -100.94 ÷ temperature 0.8) → Top-k Filtering(k=5, Top-5 안이면 -126.17, 아니면 -∞) → Softmax = 56.33%. 아래: Tokens / Logits / Scaled logits / Top-k / Softmax 표 — book -100.94, -126.17, -126.17, 56.33% / copy -101.54, -126.93, -126.93, 26.53% / few -102.13, -127.66, -127.66, 12.70% / couple -103.35, -129.19, 2.77% / bunch -103.76, -129.70, 1.67% / little부터는 Top-k가 -∞, 0%',S_TE3)
b+=P('맨 오른쪽 Probabilities의 돋보기를 누르면 표가 펼쳐집니다.','안내문은 이 숫자들을 이렇게 설명합니다.','"**모든 블록을 지난 뒤 마지막 층에서 logits가 나온다. 50,257개의 숫자이고, GPT-2 어휘의 토큰마다 하나씩이다.**"','"**logit은 그냥 점수다. 읽기 쉽게 0에서 1 사이의, 모두 더하면 1이 되는 확률로 바꾼다.**"')
b+=P('표의 칸은 왼쪽에서 오른쪽으로 계산 순서입니다.')
b+=TABLE(['칸','하는 일','book의 값'],[
['Logits','모델이 낸 원래 점수','-100.94'],
['Scaled logits','점수를 temperature로 나눈다 (0.8)','-126.17'],
['Top-k','상위 k개만 남기고 나머지는 -∞로 만든다 (k=5)','-126.17'],
['Softmax','남은 점수를 확률로 바꾼다','56.33%']])
b+=P('제 문장의 상위 다섯은 이렇게 나왔습니다.')
b+=TABLE(['토큰','book','copy','few','couple','bunch'],[
['확률','56.33%','26.53%','12.70%','2.77%','1.67%']])
b+=P('여섯 번째 `little`부터는 Top-k 칸이 -∞이고 확률이 0%입니다.','점수가 낮아서가 아니라 **"상위 5개만 쓴다"는 설정 때문에 잘린 것**입니다.')
b+=P('그리고 보라색 book은 "1등이라서 고정"이 아닙니다.','안내문에 따르면 남은 후보 가운데 **하나를 확률에 따라 뽑습니다.**','56.33%로 가장 유력했을 뿐, 다시 뽑으면 copy가 될 수도 있습니다. 실제로 이번에 눌러 보는 동안 copy가 뽑힌 적도 있었습니다.')
b+=HR()
b+=H1('9. 7단계: Temperature를 바꿔 보기')
b+=IMG(9,'금_09_Temperature_비교.png','Temperature 비교. 왼쪽 0.2: book 95.08%, copy 4.68%, few·couple·bunch는 <0.01%로 표시. 오른쪽 2: book 35.27%, copy 26.09%, few 19.44%(보라색으로 뽑힘), couple 10.58%, bunch 8.62%',S_TE4)
b+=P('위쪽 Temperature 슬라이더를 움직이면 확률이 바로 바뀝니다.','모델을 다시 돌리지 않고, **같은 logit에서 확률만 다시 계산**하는 것입니다.')
b+=TABLE(['Temperature','book','copy','few','couple','bunch'],[
['0.2','95.08%','4.68%','<0.01%','<0.01%','<0.01%'],
['0.8 (기본)','56.33%','26.53%','12.70%','2.77%','1.67%'],
['2','35.27%','26.09%','19.44%','10.58%','8.62%']])
b+=P('낮추면 1등에 확률이 몰리고, 올리면 후보들이 비슷해집니다.','2로 올렸을 때는 뽑힌 토큰이 book에서 **few**로 바뀌었습니다.','안내문의 표현으로는 "**낮은 temperature는 점수가 높은 토큰을 더 유리하게 해 예측하기 쉬운 선택으로, 높은 temperature는 차이를 평평하게 해 더 다양한 출력으로**" 이끕니다.')
b+=H2('화면의 숫자로 검산해 보기')
b+=P('표에 logit이 그대로 나와 있으니, 직접 계산해서 맞는지 확인해 봤습니다.')
b+=CODE('''import math

# Transformer Explainer 화면에 표시된 상위 5개 토큰의 logit
logits = {"book": -100.94, "copy": -101.54, "few": -102.13, "couple": -103.35, "bunch": -103.76}

def probabilities(temperature: float) -> list[float]:
    # 1) logit을 온도로 나눈다  2) top-5만 남긴 상태에서 softmax를 계산한다
    scaled = [value / temperature for value in logits.values()]
    biggest = max(scaled)
    exps = [math.exp(value - biggest) for value in scaled]
    total = sum(exps)
    return [100 * value / total for value in exps]

for temperature in (0.2, 0.8, 2.0, 10.0):
    print(temperature, [round(value, 2) for value in probabilities(temperature)])''',[('import','#74c0fc'),('def ','#74c0fc'),('return','#74c0fc'),('for ','#74c0fc'),('value / temperature','#ffd43b'),('math.exp','#8ce99a')])
b+=P('`logits`는 화면의 Logits 칸에서 옮겨 적은 다섯 숫자입니다.','`value / temperature`가 표의 Scaled logits 칸에 해당합니다.','`math.exp`로 지수를 구하고 전체 합으로 나누는 부분이 Softmax 칸입니다.','가장 큰 값을 먼저 빼는 것(`value - biggest`)은 숫자가 너무 작아지지 않게 하는 처리이고, 결과는 같습니다.','(실제로 돌린 코드는 화면의 확률과 나란히 출력하도록 몇 줄이 더 있습니다.)')
b+=IMG(10,'금_10_실행결과_온도검산.png','검산 실행 결과: 온도 0.2 계산 95.02, 4.73, 0.25, 0.00, 0.00 / 화면 95.08, 4.68, 0.00, 0.00, 0.00 / 최대 차이 0.25. 온도 0.8 계산 56.28, 26.58, 12.72, 2.77, 1.66 / 화면 56.33, 26.53, 12.70, 2.77, 1.67 / 최대 차이 0.05. 온도 2.0 최대 차이 0.03. 온도 10.0 최대 차이 0.01',S_X)
b+=P('0.8, 2, 10에서는 화면의 값과 0.05 안에서 맞았습니다.','(화면의 logit이 소수 둘째 자리까지만 보여서 생기는 차이로 보입니다.)')
b+=P('0.2에서만 few가 달랐습니다.','계산으로는 **0.25%**인데 화면에는 **<0.01%**라고 적혀 있습니다.','화면의 95.08%와 4.68%를 더해도 99.76%라서, 나머지 0.24%가 어딘가에 있어야 합니다.')
b+=P('도구의 소스 코드를 찾아보니 이유가 있었습니다.','확률이 **0.01(= 1%)보다 작으면** 숫자 대신 `<0.01%`라는 글자를 쓰게 되어 있습니다.','**==화면의 "<0.01%"는 "0.01% 미만"이 아니라 "1% 미만"으로 읽어야 합니다.==**')
b+=HR()
b+=H1('10. 8단계: Generate를 한 번 더 누르면')
b+=IMG(11,'금_11_Generate_한번더.png','Generate를 한 번 더 누른 화면: 입력칸이 ...library to borrow a copy + 보라색 of로 바뀌고, Embedding의 토큰이 I, went, to, the, library, to, borrow, a, copy 아홉 개가 됐다',S_TE)
b+=P('이 상태에서 Generate를 한 번 더 눌렀습니다.','그때 보라색으로 떠 있던 단어는 copy였습니다.')
b+=P('보라색이던 **copy가 문장 안으로 들어가고**, 토큰이 8개에서 9개가 됐습니다.','그리고 그 9개를 가지고 다음 토큰을 다시 예측합니다.','이번에는 **of**가 93.38%로 나왔습니다. "a copy of ..."로 이어지는 흐름입니다.')
b+=P('**==Generate 한 번이 "토큰 하나 뽑아서 붙이고, 처음부터 다시 계산"의 한 바퀴입니다.==**','LLM이 긴 글을 쓴다는 것은 이 한 바퀴를 계속 도는 일이었습니다.')
b+=HR()
b+=H1('11. 이 도구가 보여 주지 않는 것')
b+=P('쓰다가 범위도 확인해 뒀습니다.')
b+=Q('그러면 여기 이 사이트에서 얘기하는 건 트랜스포머 구조에 대한 것만, 어떤 식으로 다음 토큰을 예측하는지 … 설명하는 거지')
b+=TABLE(['보여 주는 것','보여 주지 않는 것'],[
['학습이 끝난 모델이 다음 토큰 하나를 정하는 과정','학습 과정. 안내문도 "학습된 모델이 글을 생성하는 과정을 본다"고 적는다'],
['GPT-2 (small)의 구조','최신 모델. 안내문은 위치 정보를 넣는 방식부터 최신 모델은 다를 수 있다고 적는다'],
['입력한 문장 하나','대화 이력, 문서 검색 같은 모델 바깥의 구성 요소']])
b+=P('구조를 익히는 용도로는 충분하지만,','"요즘 쓰는 모델도 숫자까지 똑같이 이렇다"고 읽으면 안 됩니다.')
b+=HR()
b+=H1('12. 써 보면서 걸렸던 지점')
b+=TABLE(['걸린 지점','알게 된 것'],[
['처음에 내 문장이 안 들어간다','모델(600MB)을 내려받는 중에는 예시 문장만 쓸 수 있다. 안내 문구가 사라질 때까지 기다린다'],
['입력칸을 눌렀더니 글이 바뀐다','끝에 있던 보라색 예측 단어가 입력 글에 합쳐진다. 새 문장을 넣으려면 전체를 지우고 쓴다'],
['같은 문장인데 보라색 단어가 달라진다','1등 고정이 아니라 확률에 따라 뽑기 때문이다. Temperature를 0.2로 내리면 거의 1등만 나온다'],
['<0.01%가 너무 많다','1% 미만은 모두 이렇게 적힌다. 정확한 값은 logit으로 계산해야 한다'],
['화면이 잘려 보인다','그림이 가로로 길다. 창을 넓히거나 가로로 스크롤한다']])
b+=HR()
b+=H1('13. 정리')
b+=IMG(12,'금_12_정리카드.png','정리 카드: 설치 없이 브라우저에서 돈다, 문장을 넣고 Generate, 돋보기로 속을 펼친다, 건너뛰는 선은 Residual이다. 보여 주는 것은 학습이 끝난 GPT-2가 다음 토큰 하나를 정하는 과정')
b+=TABLE(['내가 처음 생각한 것','확인한 것'],[
['예시만 보여 주는 설명 페이지일지도 모른다','내 문장을 넣어 GPT-2 (small)를 브라우저에서 직접 돌리는 도구다'],
['레이어를 건너뛰는 화살표가 뭔지 모르겠다','residual connection. 층의 입력을 출력에 그대로 더해 주는 길이고, 블록마다 두 번 있다'],
['모델은 1등 단어를 내놓는다','상위 k개만 남겨 확률로 바꾼 뒤 그중 하나를 뽑는다. 다시 뽑으면 달라질 수 있다'],
['화면의 <0.01%는 0.01% 미만이다','1% 미만이면 모두 그렇게 표시된다 (소스 코드로 확인)']])
b+=BOX('**확인된 것과 확인되지 않은 것**','확인됨(도구의 안내문·설명 글): GPT-2 (small)을 브라우저에서 직접 실행한다는 것, 세 부분의 구성, 어휘 50,257개, 블록 12개와 head 12개, residual connection과 dropout의 설명, temperature·top-k·top-p의 설명','확인됨(직접 눌러 본 화면): 내 문장의 토큰 8개와 id, attention의 세 격자, Residual 점선, 확률 표와 Temperature 0.2 / 0.8 / 2에서의 값, Generate를 한 번 더 눌렀을 때의 변화','확인됨(소스 코드): 입력칸을 누르면 예측 토큰이 합쳐지는 동작, "<0.01%" 표기의 기준, 단어 수 제한과 모바일 안내 문구가 있다는 것','확인됨(실제 실행): 화면의 logit으로 온도별 확률을 검산한 계산','확인 필요: 한국어 문장을 넣었을 때의 결과, Top-p로 바꿨을 때, 다른 head·다른 블록의 모습, 단어 수 제한에 실제로 걸리는 문장 길이, 모바일 화면')
b+=HR()
b+=H1('알게 된 것')
b+=P('**기억 속의 "건너뛰는 화살표"에 이름이 생겼습니다.**','residual connection.','층을 거친 결과로 원래 값을 덮어쓰는 것이 아니라, 원래 값에 더해 가는 구조였습니다.')
b+=P('**"다음 단어를 고른다"는 말의 실제 순서도 눈으로 봤습니다.**','점수(logit) → 온도로 나누기 → 상위 k개만 남기기 → 확률로 바꾸기 → 하나 뽑기.','Temperature와 Top-k가 이 줄의 어디에 끼어드는지가 표 한 장에 다 있었습니다.')
b+=P('**그리고 화면의 숫자도 그대로 믿지 말고 한 번은 계산해 볼 만했습니다.**','검산해 보지 않았다면 "<0.01%"를 글자 그대로 읽었을 것입니다.')
b+=HR()
b+=H1('참고자료')
b+=P('[[Transformer Explainer (도구)|https://poloclub.github.io/transformer-explainer/]]')
b+=P('[[GitHub - poloclub/transformer-explainer (소스 코드)|https://github.com/poloclub/transformer-explainer]]')
b+=P('#TransformerExplainer #GPT2 #Transformer #Attention #LLM기초 #temperature #topk #residual #AI활용 #개발입문')
import os
PAGE(T,b,os.environ.get('OUT','/home/claude/out/fri/2026-11-27_금_Transformer_Explainer_사용법.html'))
print('ok')

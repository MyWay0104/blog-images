from lib import *
# 대표 예시: 두 문장 "배가 고프다" / "배를 타다" (같은 '배', 다른 뜻). 문장 단위 비교에는 "허기가 진다"를 더한다
T='[AI활용] 토큰 임베딩 vs RAG 임베딩 차이: 토크나이저는 벡터를 만들지 않는다'
SO='출처: OpenAI Tokenizer(platform.openai.com/tokenizer), 2026-11-22 캡처. 제가 넣은 예시 문장의 Text 보기와 Token IDs 보기를 이어 붙였습니다'
ST='출처: Transformer Explainer(poloclub.github.io/transformer-explainer), 2026-11-22 캡처. 기본 예시 문장의 Embedding 단계를 펼친 화면'
SPt='출처: PyTorch 공식 문서 "Embedding"(docs.pytorch.org, 2.15 문서), 2026-11-22 캡처'
SOE='출처: OpenAI 공식 문서 "벡터 임베딩"(developers.openai.com/api/docs/guides/embeddings, 한국어 화면), 2026-11-22 캡처'
SS='출처: Sentence Transformers 공식 문서 "Creating Custom Models"(sbert.net), 2026-11-22 캡처'
SL='출처: LangChain 공식 문서 "Retrieval"(docs.langchain.com), 2026-11-22 캡처'
SX='샌드박스(Python 3.13.17, numpy)에서 실제로 실행한 출력을 옮긴 화면. 구조만 보여 주는 장난감 예시이며 실제 모델의 값이 아닙니다'
b=''
b+=IMG(1,'화_01_썸네일.png','대표 이미지(썸네일)')
b+=P('LLM 공부를 하다 보면 "임베딩"이라는 말이 두 군데에서 나옵니다.','모델이 글자를 숫자로 바꿀 때도 임베딩, RAG에서 문서를 검색할 때도 임베딩.','저는 이 둘을 같은 것으로, 그것도 **토크나이저가 만드는 벡터**라고 뭉뚱그려 알고 있었습니다.')
b+=P('결론부터 적으면,','**==토크나이저는 벡터를 만들지 않습니다. 정수 ID까지만 만듭니다. 그 ID로 표에서 꺼낸 "토큰마다의 벡터"가 토큰 임베딩이고, 임베딩 모델이 "문장 하나를 벡터 하나로" 내놓은 것이 RAG 임베딩입니다.==**','이름만 같고 단위도, 만드는 모델도, 쓰임도 다릅니다.')
b+=BOX('**이 글의 기준**','확인 날짜: 2026-11-22','근거: OpenAI Tokenizer와 임베딩 가이드, Transformer Explainer(GPT-2 small 시각화 도구)의 설명문, PyTorch 문서(Embedding), Sentence Transformers 문서, LangChain 문서(Retrieval, Embedding models)','실행 화면: 토큰 ID는 OpenAI 공식 도구에 문장을 직접 넣어 확인했습니다. 벡터의 "모양"은 numpy로 만든 장난감 예시를 샌드박스에서 실행했습니다(실제 모델 아님).','확인하지 못한 것: 실제 임베딩 모델로 문장 사이의 유사도 값을 계산해 보지는 못했습니다. 임베딩 모델 구조 설명은 공개 문서가 있는 Sentence Transformers 기준이고, OpenAI 임베딩 모델의 내부 구조는 공개 문서에서 확인하지 못했습니다.')
b+=HR()
b+=H1('1. 처음에 헷갈렸던 것')
b+=P('얼마 전 이렇게 물었습니다.')
b+=Q('토크나이저에서 벡터 사용해가지고 하는 거랑, RAG에서 임베딩으로 사용하는 벡터들 사이의 차이점')
b+=BOX('**당시의 생각**','토크나이저가 글자를 벡터로 바꾼다고 알고 있었다.','그 벡터와 RAG에서 쓰는 임베딩 벡터가 어떻게 다른지가 궁금했다.')
b+=P('돌아온 답의 첫 줄이 전제부터 고쳐 줬습니다.','"토크나이저는 벡터를 만들지 않는다."','그래서 질문을 셋으로 나눠 다시 확인했습니다.','토크나이저는 어디까지 하나. 토큰 임베딩은 누가 만드나. RAG 임베딩은 그것과 무엇이 다른가.')
b+=IMG(2,'화_02_도식_두모델흐름.png','같은 문장이 LLM과 임베딩 모델을 지나가는 길: 두 모델 모두 토크나이저(정수 ID) → 임베딩 표(토큰마다 벡터) → Transformer 층을 거치지만, LLM은 다음 토큰 확률을 내고 임베딩 모델은 풀링으로 합쳐 벡터 1개를 낸다. 토큰 임베딩은 모델 안의 첫 재료, RAG 임베딩은 임베딩 모델의 최종 결과물')
b+=P('전체 그림을 먼저 놓고, 칸을 하나씩 공식 자료로 확인해 보겠습니다.')
b+=HR()
b+=H1('2. 토크나이저는 ID까지만 만든다')
b+=P('대화 중에 이런 것도 물었습니다.')
b+=Q('토크나이저를 실습해볼 수 있는 사이트가 있었던 거 같은데')
b+=P('OpenAI가 공식으로 제공하는 Tokenizer 페이지가 있습니다.','예시 문장 두 개를 넣어 봤습니다. **"배가 고프다"**와 **"배를 타다"**. 같은 글자 "배"가 다른 뜻으로 쓰인 문장입니다.')
b+=IMG(3,'화_03_OpenAI_토크나이저.png','OpenAI Tokenizer에 "배가 고프다 / 배를 타다"를 넣은 결과: 12글자가 토큰 10개로 나뉘어 색으로 표시되고, Token IDs 보기에는 [27798, 4081, 22652, 18554, 2276, 198, 27798, 4831, 57380, 2276]이 나온다',SO)
b+=P('페이지의 설명은 이렇습니다.','"**OpenAI의 대형 언어 모델은 토큰을 사용해 텍스트를 처리한다. 토큰은 텍스트에서 흔히 나오는 글자 묶음이다.**"')
b+=P('결과를 보면 12글자가 토큰 10개로 나뉘었고, `Token IDs`를 누르면 이렇게 나옵니다.')
b+=CODE('[27798, 4081, 22652, 18554, 2276, 198, 27798, 4831, 57380, 2276]',[('27798','#ffd43b')])
b+=P('**화면 어디에도 벡터는 없습니다. 정수 열 개가 전부입니다.**','그리고 첫 번째 숫자와 일곱 번째 숫자가 `27798`로 같습니다. 두 문장 맨 앞의 "배"입니다.','(가운데 `198`은 두 문장 사이의 줄바꿈으로 보입니다.)')
b+=P('"배가 고프다"의 배와 "배를 타다"의 배는 뜻이 다르지만, **토크나이저에게는 같은 조각이고 같은 번호**입니다.','토크나이저는 뜻을 모릅니다. 사전에서 번호를 찾아 줄 뿐입니다.')
b+=HR()
b+=H1('3. ID가 벡터가 되는 곳: 임베딩 표')
b+=IMG(4,'화_04_TransformerExplainer_임베딩.png','Transformer Explainer의 Embedding 단계를 펼친 화면: Tokenization(Data, visualization, em, powers, users, to) → Token Embedding(id 6601, 32704, 795, 30132, 2985, 284) + Positional Encoding(position 0~5) = 각 토큰의 벡터',ST)
b+=P('ID가 벡터로 바뀌는 곳은 토크나이저 다음 칸입니다.','GPT-2 small을 브라우저에서 보여 주는 시각화 도구 Transformer Explainer는 Embedding 단계를 세 칸으로 나눠 그립니다.','**Tokenization → Token Embedding → Positional Encoding.**')
b+=P('도구의 설명문은 이렇게 적습니다.','"**토큰화는 입력 텍스트를 토큰으로 쪼갠다. GPT-2 small의 어휘는 50,257개이고 각각 고유한 ID가 있다.**"','"**토큰 임베딩 단계에서는 모든 토큰이 큰 lookup table에서 768개 숫자로 된 벡터와 짝지어진다. 이 벡터들은 학습 중에 익혀진다.**"')
b+=P('화면에서도 토큰 옆에 `id`가 먼저 붙고(6601, 32704 …), 그 ID에 해당하는 벡터가 꺼내진 뒤, 자리 번호(position) 정보가 더해집니다.','**==ID로 표에서 꺼낸 "토큰 하나의 벡터" — 이것이 토큰 임베딩입니다.==**')
b+=IMG(5,'화_05_공식문서_PyTorch_Embedding.png','PyTorch 공식 문서 torch.nn.Embedding: 정해진 크기의 사전에 대한 임베딩을 저장하는 단순한 lookup table. 입력은 인덱스 목록이고 출력은 그에 해당하는 임베딩. num_embeddings는 사전 크기, embedding_dim은 벡터 하나의 크기',SPt)
b+=P('이 "표"가 코드에서는 어떤 모습인지 PyTorch 문서가 한 줄로 정리합니다.','"**정해진 크기의 사전에 대한 임베딩을 저장하는 단순한 lookup table.**"','"**이 모듈의 입력은 인덱스의 목록이고, 출력은 그에 해당하는 임베딩이다.**"')
b+=P('입력이 "인덱스(번호)"라는 점이 핵심입니다.','번호로 줄을 꺼내는 표이니, **같은 번호를 넣으면 언제나 같은 벡터가 나옵니다.**','"배가 고프다"의 배(27798)와 "배를 타다"의 배(27798)는 이 단계에서 **똑같은 벡터**입니다. 문맥은 아직 들어 있지 않습니다.')
b+=P('두 "배"가 달라지는 것은 그 뒤입니다.','Transformer Explainer의 설명으로는 "Transformer 블록의 self-attention이 **토큰끼리 정보를 나누게** 하고", 블록을 지날수록 토큰의 표현이 풍부해집니다.')
b+=HR()
b+=H1('4. 모양으로 확인해 보기')
b+=P('말로만 두기 아쉬워서, 구조만 흉내 낸 작은 코드를 돌려 봤습니다.','진짜 모델이 아니라 **"번호 → 표에서 꺼내기 → 하나로 합치기"의 모양**만 보는 장난감입니다.')
b+=CODE('''import numpy as np

# 1) 장난감 토크나이저: 글자 조각을 정수 ID로 바꾼다
vocab = {"배": 0, "가": 1, "를": 2, "고프다": 3, "타다": 4}

def tokenize(pieces):
    return [vocab[p] for p in pieces]

ids_a = tokenize(["배", "가", "고프다"])
ids_b = tokenize(["배", "를", "타다"])

# 2) 임베딩 표: 어휘 5개 x 4차원 (GPT-2 small은 50,257 x 768)
rng = np.random.default_rng(0)
table = rng.normal(size=(len(vocab), 4)).round(2)

tok_a = table[ids_a]   # ID로 표에서 줄을 꺼낸다 (lookup)
tok_b = table[ids_b]

# 3) 벡터 하나로 합치기 (평균 풀링)
sent_a = tok_a.mean(axis=0)''',[('import','#74c0fc'),('def ','#74c0fc'),('return','#74c0fc'),('table[ids_a]','#ffd43b'),('table[ids_b]','#ffd43b'),('.mean(axis=0)','#8ce99a')])
b+=P('`vocab`은 조각마다 번호를 붙인 사전이고, `tokenize`는 조각을 번호로 바꿉니다. 여기까지가 토크나이저 역할입니다.','`table`은 "어휘 5개 x 4차원"짜리 숫자 표입니다. 값은 아무 숫자로 채웠습니다.','`table[ids_a]`가 핵심 줄입니다. **번호 목록으로 표의 줄을 꺼냅니다.** 토큰이 3개면 줄이 3개 나옵니다.','`tok_a.mean(axis=0)`은 그 3줄을 평균 내어 한 줄로 합칩니다. 풀링(pooling)의 가장 단순한 형태입니다.')
b+=IMG(6,'화_06_실행결과_모양.png','장난감 예시 실행 결과: 문장 A의 ID [0, 1, 3], 문장 B의 ID [0, 2, 4], 토큰 임베딩 모양 (3, 4), A의 배 벡터와 B의 배 벡터가 [0.13 -0.13 0.64 0.1]로 같음, 두 배가 같은가 True, 문장 벡터 모양 (4,)',SX)
b+=P('토큰 임베딩의 모양은 `(3, 4)` — **토큰 수만큼 벡터가 있습니다.**','문장 A의 "배"와 문장 B의 "배"는 벡터가 같습니다(`True`). 표에서 같은 줄을 꺼냈으니 당연합니다.','합친 뒤의 모양은 `(4,)` — **벡터가 하나**입니다.')
b+=P('다만 이 예시의 마지막 줄은 실제 임베딩 모델과 다릅니다.','실제 모델은 표에서 꺼낸 값을 바로 평균 내지 않고, **그 전에 Transformer 층으로 문맥을 섞습니다.** 다음 장에서 확인합니다.')
b+=HR()
b+=H1('5. RAG 임베딩은 문장 하나를 벡터 하나로')
b+=IMG(7,'화_07_공식문서_OpenAI_임베딩.png','OpenAI 공식 문서(한국어) 임베딩이란?: 텍스트 임베딩은 문자열 간의 관련성을 측정하며 검색·군집화·추천 등에 쓰인다. 임베딩은 부동 소수점 수로 이루어진 벡터이고 두 벡터 사이의 거리로 관련성을 측정한다. 임베딩 API에 텍스트와 임베딩 모델 이름(text-embedding-3-small)을 보낸다',SOE)
b+=P('RAG에서 말하는 임베딩은 OpenAI 문서의 이 정의에 해당합니다.','"**OpenAI의 텍스트 임베딩은 문자열 간의 관련성을 측정합니다.**"','"**임베딩은 부동 소수점 수로 이루어진 벡터(리스트)입니다. 두 벡터 사이의 거리로 관련성을 측정합니다.**"')
b+=P('단위가 "문자열"입니다. 토큰 하나가 아니라 **넣은 글 전체에 대해 벡터 하나**가 돌아옵니다.','같은 문서에 따르면 `text-embedding-3-small`은 기본으로 1536개 숫자짜리 벡터를 냅니다.')
b+=P('그리고 캡처 아래쪽을 보면, 임베딩을 얻으려면 **임베딩 모델 이름**을 따로 지정합니다.','글을 쓰는 모델과는 다른, 임베딩 전용 모델입니다.')
b+=IMG(8,'화_08_공식문서_SentenceTransformers.png','Sentence Transformers 공식 문서 Modular Architecture: 모델은 순서대로 실행되는 모듈의 모음이며 가장 흔한 구조는 Transformer 모듈과 Pooling 모듈의 조합. Transformer는 입력 텍스트를 처리해 문맥이 반영된 임베딩을 만들고, Pooling은 그 임베딩을 모아 차원을 줄인다(mean pooling, CLS pooling)',SS)
b+=P('그럼 임베딩 모델 안에서는 무슨 일이 일어날까요.','구조가 공개된 Sentence Transformers 문서를 보면 이렇게 적혀 있습니다.','"**Sentence Transformer 모델은 순서대로 실행되는 모듈의 모음이다. 가장 흔한 구조는 Transformer 모듈과 Pooling 모듈의 조합이다.**"')
b+=TABLE(['모듈','하는 일 (공식 문서)'],[
['Transformer','입력 텍스트를 처리해 **문맥이 반영된 임베딩**을 만든다'],
['Pooling','Transformer의 출력을 **모아서(aggregating) 차원을 줄인다**. mean pooling, CLS pooling이 흔하다']])
b+=P('즉 임베딩 모델도 안에서는 토큰별 벡터를 다룹니다.','거기에 **① 문맥을 섞고 ② 하나로 합치는** 단계가 더 붙어서, 바깥으로는 벡터 하나가 나오는 것입니다.','4장의 장난감 예시에 빠져 있던 것이 ①입니다.')
b+=P('그래서 문장 단위에서는 이런 일이 기대됩니다.','"배가 고프다"와 **"허기가 진다"**는 겹치는 글자가 없어도 벡터가 가깝게,','"배가 고프다"와 **"배를 타다"**는 같은 "배"가 있어도 벡터가 멀게.','LangChain 문서의 표현으로는 "**임베딩 모델은 텍스트를 숫자 벡터로 바꿔서, 뜻이 비슷한 글이 그 공간에서 가까이 놓이게 한다.**"','(이 세 문장의 실제 거리는 계산해 보지 못했습니다. 모델마다 값이 다릅니다. 확인 필요)')
b+=HR()
b+=H1('6. 나란히 놓고 보기')
b+=IMG(9,'화_09_비교표.png','토큰 임베딩과 RAG 임베딩 비교표: 단위(토큰 1개 / 문장·문단 1개), 벡터 수(토큰 수만큼 / 1개), 문맥(없음 / 반영됨), 어디에 있나(모델 안의 첫 단계 / 임베딩 모델의 출력), 무엇에 쓰나(뒤따르는 계산의 재료 / 벡터 DB 저장과 검색), 만드는 것(임베딩 표 / 임베딩 모델 전체)')
b+=TABLE(['','토큰 임베딩','RAG 임베딩'],[
['단위','토큰 1개','문장·문단(청크) 1개'],
['벡터 수','토큰 수만큼','1개'],
['문맥','없음 (표에서 꺼낸 값)','반영됨 (Transformer 층을 거친 뒤 합친 값)'],
['어디에 있나','모델 안의 첫 단계','임베딩 모델의 출력'],
['무엇에 쓰나','뒤따르는 계산의 재료','벡터 DB에 저장하고 가까운 글을 찾는다']])
b+=P('제가 처음에 한 덩어리로 알던 것이 실제로는 세 칸이었습니다.','**토크나이저(ID) → 토큰 임베딩(토큰마다 벡터) → RAG 임베딩(문장에 벡터 하나).**')
b+=HR()
b+=H1('7. 같이 헷갈리기 쉬운 두 가지')
b+=H2('RAG는 LLM의 임베딩을 그대로 쓰는가')
b+=P('아닙니다. 보통 **별도의 임베딩 모델**을 씁니다.','OpenAI 문서에서 임베딩 API에 `text-embedding-3-small` 같은 임베딩 모델 이름을 따로 보내는 것,','LangChain 문서가 RAG의 구성 요소로 "Embedding models"를 따로 두는 것이 그 근거입니다.')
b+=H2('검색된 벡터가 LLM에 들어가는가')
b+=IMG(10,'화_10_공식문서_LangChain_파이프라인.png','LangChain 공식 문서의 Retrieval pipeline 도식: Sources → Document Loaders → Documents → Split into chunks → Turn into embeddings, User Query → Query embedding → Vector Store → Retriever → LLM uses retrieved info → Answer',SL)
b+=P('이것도 아닙니다.','LangChain 문서의 흐름도를 보면, 임베딩은 **Vector Store에 넣고 찾는 데**까지 쓰이고, 그 뒤 칸은 "**LLM uses retrieved info**"입니다.','본문에도 "**찾은 내용을 context로 LLM에 제공한다**"고 적혀 있습니다.')
b+=IMG(11,'화_11_도식_벡터와_텍스트의_길.png','RAG에서 벡터가 가는 길과 텍스트가 가는 길: 질문 텍스트 → 임베딩 모델 → 벡터 DB → 찾은 벡터에 딸린 원문 조각을 꺼냄(벡터는 여기까지). 찾은 원문 조각 → 프롬프트에 글자로 붙임 → LLM(자기 토크나이저, 자기 임베딩 표) → 답변')
b+=P('**벡터는 찾는 데만 쓰이고, LLM에는 찾아낸 원문이 글자로 들어갑니다.**','LLM은 그 글자를 받아 자기 토크나이저로 다시 쪼개고, 자기 임베딩 표에서 다시 꺼냅니다.','임베딩 모델의 1536차원 벡터를 LLM에 그대로 꽂는 것이 아닙니다.')
b+=HR()
b+=H1('8. 정리')
b+=IMG(12,'화_12_정리카드.png','정리 카드: 토크나이저는 ID까지만, 토큰 임베딩은 표에서 꺼낸 값, RAG 임베딩은 문장에 벡터 하나, 두 모델을 잇는 것은 글자')
b+=TABLE(['내가 처음 생각한 것','확인한 것'],[
['토크나이저가 글자를 벡터로 바꾼다','토크나이저는 정수 ID까지만 만든다. OpenAI Tokenizer 화면에는 ID만 나온다'],
['모델의 임베딩과 RAG의 임베딩은 같은 종류의 벡터다','토큰 임베딩은 토큰마다 하나, RAG 임베딩은 문장에 하나. 단위와 쓰임이 다르다'],
['같은 글자면 뜻이 달라도 구별된다','토큰 임베딩 단계에서는 같은 ID면 같은 벡터다. 문맥은 Transformer 층에서 섞인다'],
['(막연히) 검색에 쓴 벡터가 모델로 넘어간다','벡터는 검색까지만. LLM에는 찾은 원문이 글자로 들어간다']])
b+=BOX('**확인된 것과 확인되지 않은 것**','확인됨(공식 도구·문서): OpenAI Tokenizer가 문장을 토큰 ID로 바꾼다는 것과 예시 문장의 실제 ID, GPT-2 small의 어휘 50,257개와 768차원 lookup table(Transformer Explainer 설명문), PyTorch Embedding이 인덱스를 받아 임베딩을 돌려주는 lookup table이라는 것, OpenAI 임베딩의 정의와 text-embedding-3-small의 기본 1536차원, Sentence Transformers의 Transformer + Pooling 구조, LangChain의 retrieval 흐름','확인됨(실제 실행): numpy 장난감 예시의 모양 (3, 4)와 (4,). 구조만 보인 것이고 실제 모델의 값은 아닙니다.','확인 필요: 세 예시 문장의 실제 임베딩 유사도, OpenAI 임베딩 모델의 내부 구조, 다른 토크나이저에서 "배"가 어떻게 쪼개지는지')
b+=HR()
b+=H1('알게 된 것')
b+=P('**"임베딩"이라는 한 단어가 서로 다른 칸을 가리키고 있었습니다.**','앞으로는 이 말을 들으면 먼저 묻기로 했습니다. "토큰 하나의 것인가, 문장 하나의 것인가."')
b+=P('**토크나이저에 대한 오해가 뿌리였습니다.**','"토크나이저가 벡터를 만든다"고 알고 있으니 그 뒤의 칸들이 전부 뭉개져 보였습니다.','공식 도구에 문장을 넣어 숫자 열 개만 나오는 것을 보고 나서야 칸이 나뉘었습니다.')
b+=HR()
b+=H1('참고자료')
b+=P('[[OpenAI Tokenizer (공식 도구)|https://platform.openai.com/tokenizer]]')
b+=P('[[OpenAI 공식 문서 - 벡터 임베딩|https://developers.openai.com/api/docs/guides/embeddings]]')
b+=P('[[Transformer Explainer (GPT-2 시각화 도구)|https://poloclub.github.io/transformer-explainer/]]')
b+=P('[[PyTorch 공식 문서 - torch.nn.Embedding|https://docs.pytorch.org/docs/stable/generated/torch.nn.Embedding.html]]')
b+=P('[[Sentence Transformers 공식 문서 - Creating Custom Models|https://sbert.net/docs/sentence_transformer/usage/custom_models.html]]')
b+=P('[[LangChain 공식 문서 - Retrieval|https://docs.langchain.com/oss/python/langchain/retrieval]]')
b+=P('[[LangChain 공식 문서 - Embedding models|https://docs.langchain.com/oss/python/integrations/embeddings]]')
b+=P('#임베딩 #토큰임베딩 #RAG #토크나이저 #벡터DB #LLM기초 #OpenAI #SentenceTransformers #AI활용 #개발입문')
import os
PAGE(T,b,os.environ.get('OUT','/home/claude/out/tue/2026-11-24_화_토큰임베딩_vs_RAG임베딩.html'))
print('ok')

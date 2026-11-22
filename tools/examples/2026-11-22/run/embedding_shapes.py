import numpy as np

# 1) 장난감 토크나이저: 글자 조각을 정수 ID로 바꾼다 (실제 토크나이저의 어휘는 수만 개)
vocab = {"배": 0, "가": 1, "를": 2, "고프다": 3, "타다": 4}

def tokenize(pieces):
    return [vocab[p] for p in pieces]

ids_a = tokenize(["배", "가", "고프다"])
ids_b = tokenize(["배", "를", "타다"])
print("문장 A의 ID :", ids_a)
print("문장 B의 ID :", ids_b)

# 2) 임베딩 표: 어휘 5개 x 4차원 (GPT-2 small은 50,257 x 768)
rng = np.random.default_rng(0)
table = rng.normal(size=(len(vocab), 4)).round(2)

tok_a = table[ids_a]   # ID로 표에서 줄을 꺼낸다 (lookup)
tok_b = table[ids_b]
print("토큰 임베딩 모양 :", tok_a.shape)
print("A의 '배' 벡터   :", tok_a[0])
print("B의 '배' 벡터   :", tok_b[0])
print("두 '배'가 같은가 :", bool((tok_a[0] == tok_b[0]).all()))

# 3) 벡터 하나로 합치기 (평균 풀링)
sent_a = tok_a.mean(axis=0)
print("문장 벡터 모양   :", sent_a.shape)

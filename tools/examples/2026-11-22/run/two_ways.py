import numpy as np


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

print("(가) 점수표의 칸 수:", len(vocab), "/ 계산 횟수:", steps)
print("(가) 나온 것:", " ".join(vocab[t] for t in tokens[1:-1]))

# (나) 판정만 하는 방식: 점수표의 칸 = 미리 정해 준 답
answers = ["예", "아니오"]
answer_scores = np.array([2.3, 0.0])   # 직접 정한 숫자
p = softmax(answer_scores)

print("(나) 점수표의 칸 수:", len(answers), "/ 계산 횟수: 1")
print("(나) 나온 것:", ", ".join(f"{a} {v:.2f}" for a, v in zip(answers, p)))

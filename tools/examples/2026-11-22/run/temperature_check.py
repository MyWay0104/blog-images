import math

# Transformer Explainer 화면에 표시된 상위 5개 토큰의 logit (소수 둘째 자리까지 표시된 값)
logits = {"book": -100.94, "copy": -101.54, "few": -102.13, "couple": -103.35, "bunch": -103.76}

# 화면에 표시된 확률(%) — 온도별로 직접 읽은 값
shown = {
    0.2: [95.08, 4.68, 0.00, 0.00, 0.00],
    0.8: [56.33, 26.53, 12.70, 2.77, 1.67],
    2.0: [35.27, 26.09, 19.44, 10.58, 8.62],
    10.0: [22.89, 21.55, 20.31, 17.99, 17.27],
}


def probabilities(temperature: float) -> list[float]:
    # 1) logit을 온도로 나눈다  2) top-5만 남긴 상태에서 softmax를 계산한다
    scaled = [value / temperature for value in logits.values()]
    biggest = max(scaled)
    exps = [math.exp(value - biggest) for value in scaled]
    total = sum(exps)
    return [100 * value / total for value in exps]


print("온도   " + "".join(f"{name:>9}" for name in logits))
for temperature, shown_values in shown.items():
    calc = probabilities(temperature)
    print(f"{temperature:<5} 계산 " + "".join(f"{value:>9.2f}" for value in calc))
    print(f"      화면 " + "".join(f"{value:>9.2f}" for value in shown_values))
    print(f"      최대 차이 {max(abs(c - s) for c, s in zip(calc, shown_values)):.2f}")

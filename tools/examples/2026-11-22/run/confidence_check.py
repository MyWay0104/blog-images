from decimal import Decimal, ROUND_HALF_UP

from pydantic import BaseModel


class ChoiceAnswer(BaseModel):
    # 공식 문서에 실린 응답 한 건: 질문 이름, 선택지별 확률, 문서에 적힌 confidence
    name: str
    probabilities: dict[str, Decimal]
    confidence: Decimal


def choice_confidence(probabilities: dict[str, Decimal]) -> Decimal:
    # 공식 문서의 Choice 공식: (가장 큰 확률 - 1/n) / (1 - 1/n)
    n = Decimal(len(probabilities))
    p_max = max(probabilities.values())
    return (p_max - 1 / n) / (1 - 1 / n)


D = Decimal
answers = [
    ChoiceAnswer(name="department", confidence=D("0.42"),
                 probabilities={"shipping": D("0.04"), "billing": D("0.35"), "returns": D("0.61")}),
    ChoiceAnswer(name="return_reason", confidence=D("1.0"),
                 probabilities={"other": D("0.0"), "wrong_size": D("1.0"), "changed_mind": D("0.0"),
                                "damaged": D("0.0"), "wrong_item": D("0.0")}),
    ChoiceAnswer(name="shipping_issue", confidence=D("0.67"),
                 probabilities={"wrong_address": D("0.0"), "other": D("0.26"), "not_delivered": D("0.0"),
                                "damaged_in_transit": D("0.0"), "delayed": D("0.74")}),
    ChoiceAnswer(name="requested_resolution", confidence=D("0.2"),
                 probabilities={"replacement": D("0.34"), "refund": D("0.4"), "information": D("0.02"),
                                "exchange": D("0.24")}),
    ChoiceAnswer(name="tone", confidence=D("0.76"),
                 probabilities={"frustrated": D("0.84"), "angry": D("0.16"), "calm": D("0.0")}),
]

print(f"{'질문':<22}{'선택지':>4}{'최대확률':>8}{'계산값':>9}{'문서값':>8}{'차이':>8}")
for a in answers:
    calc = choice_confidence(a.probabilities).quantize(D("0.001"), rounding=ROUND_HALF_UP)
    diff = abs(calc - a.confidence)
    print(f"{a.name:<22}{len(a.probabilities):>6}{max(a.probabilities.values()):>12}{calc:>12}{a.confidence:>11}{diff:>10}")

# Day 14. 추론, 검정, 회귀와 2주차 숙달

## 1. 오늘의 위치
Week 2의 학습 주제입니다. 이전 개념을 다시 사용하고 이후 데이터, tensor, LLM 흐름으로 연결합니다.

## 2. 학습 목표
- 신뢰구간을 한 문장으로 설명한다.
- 코드 실행 전 출력과 shape를 예측한다.
- 오류 메시지를 읽고 최소 수정안을 제시한다.
- AI가 만든 설명을 실행 결과로 검증한다.

## 3. 선수지식 자가점검
1. 이전 날짜에서 배운 변수와 타입을 떠올립니다.
2. 코드가 위에서 아래로 실행된다는 점을 설명합니다.
3. 실제 개인정보를 사용하지 않는 이유를 말합니다.

## 4. 핵심 개념
| 용어 | 설명 |
| --- | --- |
| 신뢰구간 | 오늘 코드에서 확인할 핵심 개념입니다. |
| p-value | 오늘 코드에서 확인할 핵심 개념입니다. |
| t-test | 오늘 코드에서 확인할 핵심 개념입니다. |
| 카이제곱검정 | 오늘 코드에서 확인할 핵심 개념입니다. |
| 상관 | 오늘 코드에서 확인할 핵심 개념입니다. |
| 회귀 | 오늘 코드에서 확인할 핵심 개념입니다. |

## 5. 예측하고 실행하기
```python
patient_rows = [
    {"patient_id": "P001", "age": 21, "sbp": 118, "group": "A"},
    {"patient_id": "P002", "age": 24, "sbp": 132, "group": "B"},
    {"patient_id": "P003", "age": 23, "sbp": 126, "group": "A"},
]
sbp_values = [row["sbp"] for row in patient_rows]
print("shape-like:", (len(patient_rows), len(patient_rows[0])))
print("mean_sbp:", round(sum(sbp_values) / len(sbp_values), 2))
try:
    import pandas as pd
    df = pd.DataFrame(patient_rows)
    print(df.groupby("group")["sbp"].mean())
except ModuleNotFoundError:
    print("pandas가 없는 환경에서는 list of dict로 먼저 구조를 이해합니다.")
```

## 6. 흔한 오해
- 출력만 보고 타입과 shape를 확인하지 않는 실수를 피합니다.
- 합성 데이터는 실제 환자 정보가 아닙니다.

## 7. 참고자료
- Python 공식 문서: https://docs.python.org/3/
- NumPy 공식 문서: https://numpy.org/doc/
- pandas 공식 문서: https://pandas.pydata.org/docs/
- PyTorch 공식 문서: https://pytorch.org/docs/stable/index.html
- Hugging Face 문서: https://huggingface.co/docs/transformers/index

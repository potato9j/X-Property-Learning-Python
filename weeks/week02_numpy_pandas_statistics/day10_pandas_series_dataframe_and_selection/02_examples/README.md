# Day 10 예제. pandas Series, DataFrame과 선택

## 예제 목표
Series, DataFrame, loc, iloc, filter, sort를 코드 실행 결과와 함께 확인합니다.

## 실행 순서
1. notebook을 엽니다.
2. 출력과 shape를 예측합니다.
3. 실행 후 차이를 기록합니다.

## 핵심 예제 코드
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

## 확인 질문
- 첫 출력의 자료구조는 무엇인가요?
- shape-like 값은 무엇을 뜻하나요?
- AI 설명에서 검증해야 할 부분은 무엇인가요?

"""
Day 01 lesson.py

이 파일은 "코드를 직접 많이 작성하는" 자료가 아니라
"이미 작성된 Python 코드를 읽고 해석하는" 자료입니다.

Colab에서는 같은 폴더에 이 파일을 둔 뒤 다음 중 하나로 실행합니다.

%run lesson.py
!python lesson.py
"""


# 1. records는 네 명의 가상 환자 행을 담은 list입니다.
#    실제 환자 정보가 아니라 수업용 합성 데이터입니다.
#    바깥쪽 []는 "여러 행을 순서대로 담는다"는 뜻입니다.
records = [
    {"patient_id": "P001", "age": 19, "glucose": 91, "group": "A"},
    {"patient_id": "P002", "age": 21, "glucose": 107, "group": "B"},
    {"patient_id": "P003", "age": 22, "glucose": 86, "group": "A"},
    {"patient_id": "P004", "age": 20, "glucose": 118, "group": "B"},
]


# 2. type은 값의 종류를 확인하는 함수입니다.
#    records 자체는 list이고, records 안의 첫 번째 행은 dict입니다.
print("records의 타입:", type(records).__name__)
print("첫 번째 행의 타입:", type(records[0]).__name__)
print("전체 행 개수:", len(records))


# 3. 아래 코드는 각 행에서 glucose 값만 꺼내 새 list를 만듭니다.
#    for row in records는 records 안의 dict를 하나씩 row라는 이름으로 꺼냅니다.
#    row["glucose"]는 한 행에서 glucose 열에 해당하는 값을 꺼냅니다.
glucose_values = [row["glucose"] for row in records]

print("glucose 값 목록:", glucose_values)
print("glucose_values의 타입:", type(glucose_values).__name__)


# 4. 평균은 "합계 / 개수"입니다.
#    sum(glucose_values)는 glucose 값들의 합계를 계산합니다.
#    len(glucose_values)는 glucose 값이 몇 개인지 계산합니다.
mean_glucose = sum(glucose_values) / len(glucose_values)

print("glucose 평균:", mean_glucose)
print("mean_glucose의 타입:", type(mean_glucose).__name__)


# 5. threshold는 기준값입니다.
#    기준값을 변수로 빼 두면, 나중에 100을 95나 110으로 바꿔 비교하기 쉽습니다.
threshold = 100


# 6. 각 환자의 glucose가 기준 이상인지 해석합니다.
#    row["glucose"] >= threshold는 True 또는 False를 만듭니다.
#    즉 is_high의 타입은 bool입니다.
for row in records:
    patient_id = row["patient_id"]
    glucose = row["glucose"]
    is_high = glucose >= threshold

    print(patient_id, "glucose:", glucose, "기준 이상인가?", is_high)


# 7. 마지막 summary는 수업에서 말로 설명할 최종 요약입니다.
#    dictionary는 이름과 값을 짝으로 묶어서 결과를 정리할 때 유용합니다.
summary = {
    "patient_count": len(records),
    "threshold": threshold,
    "mean_glucose": round(mean_glucose, 2),
    "high_count": sum(row["glucose"] >= threshold for row in records),
}

print("요약:", summary)


# 8. 읽기 과제:
#    아래 네 질문에 답할 수 있으면 Day 1 목표를 달성한 것입니다.
#    - records는 어떤 타입인가?
#    - records[0]은 어떤 타입인가?
#    - glucose_values는 어떤 과정을 거쳐 만들어졌는가?
#    - high_count는 어떤 기준으로 계산되었는가?

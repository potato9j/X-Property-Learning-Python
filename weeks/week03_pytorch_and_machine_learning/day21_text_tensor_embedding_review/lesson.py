"""
Day 21. 텍스트 tensor, embedding과 3주차 숙달

이 파일은 학생이 코드를 처음부터 직접 작성하기 위한 파일이 아닙니다.
이미 작성된 코드를 읽고, 주석을 따라가며, 값의 흐름을 해석하기 위한 파일입니다.

오늘의 중심 생각:
텍스트도 모델 안에서는 숫자 tensor와 embedding으로 변환되어 처리된다.

핵심 용어:
text, token id, embedding, sequence, batch
"""


# 1. 수업용 합성 데이터입니다.
#    실제 환자 정보가 아니며, 코드 읽기 연습을 위한 작은 표라고 보면 됩니다.
#    records는 list이고, list 안의 각 원소는 dict입니다.
records = [
    {"patient_id": "P001", "age": 19, "glucose": 91, "group": "A", "tokens": ["patient", "stable"]},
    {"patient_id": "P002", "age": 21, "glucose": 107, "group": "B", "tokens": ["glucose", "high"]},
    {"patient_id": "P003", "age": 22, "glucose": 86, "group": "A", "tokens": ["follow", "up"]},
    {"patient_id": "P004", "age": 20, "glucose": 118, "group": "B", "tokens": ["review", "needed"]},
]


# 2. 먼저 전체 데이터의 크기와 타입을 확인합니다.
#    초보자는 계산보다 먼저 "무엇을 들고 있는지" 확인해야 합니다.
print("DAY:", 21)
print("TOPIC:", "텍스트 tensor, embedding과 3주차 숙달")
print("records type:", type(records).__name__)
print("row count:", len(records))
print("first row type:", type(records[0]).__name__)


# 3. 한 행에서 값을 꺼내 봅니다.
#    dict는 key를 이용해 값을 꺼냅니다.
first_row = records[0]
print("first patient id:", first_row["patient_id"])
print("first glucose:", first_row["glucose"])


# 4. 여러 행에서 같은 열의 값만 모읍니다.
#    이 줄은 나중에 pandas 열 선택, tensor feature 추출, token id 목록 만들기의 기초가 됩니다.
glucose_values = [row["glucose"] for row in records]
ages = [row["age"] for row in records]
groups = [row["group"] for row in records]

print("glucose values:", glucose_values)
print("ages:", ages)
print("groups:", groups)


# 5. 요약값을 계산합니다.
#    평균은 합계를 개수로 나눈 값입니다.
mean_glucose = sum(glucose_values) / len(glucose_values)
mean_age = sum(ages) / len(ages)

print("mean glucose:", round(mean_glucose, 2))
print("mean age:", round(mean_age, 2))


# 6. 기준값을 변수로 둡니다.
#    숫자를 코드 곳곳에 직접 쓰지 않고 이름을 붙이면 해석하기 쉬워집니다.
threshold = 100


# 7. 각 행이 기준을 만족하는지 읽습니다.
#    비교식은 True 또는 False를 만듭니다.
for row in records:
    is_high = row["glucose"] >= threshold
    print(row["patient_id"], "glucose >=", threshold, "?", is_high)


# 8. 수업용 최종 요약입니다.
#    이 dict를 보고 어떤 계산이 있었는지 거꾸로 설명하는 것이 오늘의 과제입니다.
summary = {
    "topic": "텍스트 tensor, embedding과 3주차 숙달",
    "core_idea": "텍스트도 모델 안에서는 숫자 tensor와 embedding으로 변환되어 처리된다.",
    "patient_count": len(records),
    "mean_glucose": round(mean_glucose, 2),
    "high_glucose_count": sum(row["glucose"] >= threshold for row in records),
    "unique_groups": sorted(set(groups)),
}

print("summary:", summary)


# 9. 읽기 과제입니다.
#    아래 질문에 답해 보세요. 답을 새 코드로 쓰기보다 말로 설명하는 것이 먼저입니다.
#    1. records와 first_row의 타입은 각각 무엇인가?
#    2. glucose_values는 어느 줄에서 어떤 방식으로 만들어졌는가?
#    3. threshold를 110으로 바꾸면 어떤 출력이 달라지는가?
#    4. summary의 각 key는 어떤 계산 결과를 담고 있는가?

"""
Day 15. 머신러닝 workflow와 데이터 분할

이 파일은 학생이 처음부터 코드를 작성하기 위한 파일이 아닙니다.
이미 작성된 코드를 읽고, 주석을 따라가며, 값의 흐름을 해석하기 위한 수업 파일입니다.

오늘의 중심 생각:
머신러닝은 데이터를 나누고 기준 모델과 비교하며 일반화 성능을 확인하는 절차다.

핵심 용어:
feature, label, train, validation, baseline
"""

print("DAY:", 15)
print("TOPIC:", "머신러닝 workflow와 데이터 분할")
print("CORE IDEA:", "머신러닝은 데이터를 나누고 기준 모델과 비교하며 일반화 성능을 확인하는 절차다.")

# 1. 수업용 합성 데이터입니다.
#    실제 환자 정보가 아니라, 오늘 개념을 읽기 위한 작은 예제입니다.
# 4. 여러 행에서 같은 열의 값만 모읍니다.
#    일차별 주제가 달라도 "입력 -> 중간 값 -> 출력" 흐름을 찾는 연습은 같습니다.

    # 머신러닝은 데이터를 나누고 기준 모델과 비교하는 절차부터 시작합니다.
rows = [{"x": 1, "y": 3}, {"x": 2, "y": 5}, {"x": 3, "y": 7}, {"x": 4, "y": 9}]
train = rows[:3]
validation = rows[3:]
baseline_prediction = sum(row["y"] for row in train) / len(train)
error = abs(validation[0]["y"] - baseline_prediction)

print("train rows:", train)
print("validation rows:", validation)
print("baseline prediction:", baseline_prediction)
print("validation absolute error:", error)
print("reading task:", "검증 데이터는 학습에 쓰지 않은 데이터여야 일반화 질문을 할 수 있습니다.")

# 9. 읽기 과제입니다.
# 마지막 확인 질문입니다.
# 1. 이 파일에서 가장 먼저 만들어진 값은 무엇인가?
# 2. 중간 변수 중 하나를 골라 어느 줄에서 만들어졌는지 설명하세요.
# 3. 출력값 하나를 골라 어떤 입력과 규칙으로 만들어졌는지 설명하세요.
# 4. 기준값이나 입력값 하나를 바꾸면 어떤 출력이 바뀔지 예측하세요.

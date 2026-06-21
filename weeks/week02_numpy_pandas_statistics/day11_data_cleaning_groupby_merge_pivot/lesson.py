"""
Day 11. 결측치, groupby, merge와 reshape

이 파일은 학생이 처음부터 코드를 작성하기 위한 파일이 아닙니다.
이미 작성된 코드를 읽고, 주석을 따라가며, 값의 흐름을 해석하기 위한 수업 파일이다.

이 장의 중심 생각:
데이터 정리는 잘못되거나 비어 있거나 흩어진 표를 분석 가능한 형태로 바꾸는 과정이다.

읽을 용어:
missing value, groupby, merge, pivot, reshape
"""

print("DAY:", 11)
print("TOPIC:", "결측치, groupby, merge와 reshape")
print("CORE IDEA:", "데이터 정리는 잘못되거나 비어 있거나 흩어진 표를 분석 가능한 형태로 바꾸는 과정이다.")

# 1. 수업용 합성 데이터이다.
#    실제 환자 정보가 아니라, 오늘 개념을 읽기 위한 작은 예제이다.
# 4. 여러 행에서 같은 열의 값만 모읍니다.
#    일차별 주제가 달라도 "입력 -> 중간 값 -> 출력" 흐름을 찾는 연습은 같습니다.

    # 결측치, groupby, merge를 작은 표 두 개로 해석한다.
labs = [{"id": "P001", "glucose": 91}, {"id": "P002", "glucose": None}, {"id": "P003", "glucose": 118}]
groups = {"P001": "A", "P002": "B", "P003": "A"}
cleaned = [row for row in labs if row["glucose"] is not None]
merged = [{**row, "group": groups[row["id"]]} for row in cleaned]
group_a_mean = sum(row["glucose"] for row in merged if row["group"] == "A") / 2

print("cleaned:", cleaned)
print("merged:", merged)
print("group A mean:", group_a_mean)
print("reading task:", "결측치를 처리한 뒤에야 groupby나 merge 결과를 믿을 수 있습니다.")

# 9. 읽기 과제이다.
# 마지막 확인 질문이다.
# 1. 이 파일에서 가장 먼저 만들어진 값은 무엇인가?
# 2. 중간 변수 중 하나를 골라 어느 줄에서 만들어졌는지 설명하라.
# 3. 출력값 하나를 골라 어떤 입력과 규칙으로 만들어졌는지 설명하라.
# 4. 기준값이나 입력값 하나를 바꾸면 어떤 출력이 바뀔지 예측한다.

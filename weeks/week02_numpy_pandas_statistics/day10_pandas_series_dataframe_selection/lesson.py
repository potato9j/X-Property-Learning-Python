"""
Day 10. pandas Series, DataFrame과 선택

이 파일은 학생이 처음부터 코드를 작성하기 위한 파일이 아닙니다.
이미 작성된 코드를 읽고, 주석을 따라가며, 값의 흐름을 해석하기 위한 수업 파일입니다.

오늘의 중심 생각:
DataFrame은 행과 열로 구성된 표이며, 분석은 필요한 행과 열을 정확히 고르는 일에서 시작한다.

핵심 용어:
Series, DataFrame, row, column, loc
"""

print("DAY:", 10)
print("TOPIC:", "pandas Series, DataFrame과 선택")
print("CORE IDEA:", "DataFrame은 행과 열로 구성된 표이며, 분석은 필요한 행과 열을 정확히 고르는 일에서 시작한다.")

# 1. 수업용 합성 데이터입니다.
#    실제 환자 정보가 아니라, 오늘 개념을 읽기 위한 작은 예제입니다.
# 4. 여러 행에서 같은 열의 값만 모읍니다.
#    일차별 주제가 달라도 "입력 -> 중간 값 -> 출력" 흐름을 찾는 연습은 같습니다.

    # DataFrame을 배우기 전, 행과 열 선택을 list와 dict로 해석합니다.
table = [
    {"id": "P001", "group": "A", "glucose": 91},
    {"id": "P002", "group": "B", "glucose": 118},
    {"id": "P003", "group": "A", "glucose": 86},
]
glucose_column = [row["glucose"] for row in table]
group_a_rows = [row for row in table if row["group"] == "A"]

print("glucose column:", glucose_column)
print("group A rows:", group_a_rows)
print("reading task:", "pandas의 열 선택과 행 필터링도 결국 이름과 조건으로 값을 고르는 일입니다.")

# 9. 읽기 과제입니다.
# 마지막 확인 질문입니다.
# 1. 이 파일에서 가장 먼저 만들어진 값은 무엇인가?
# 2. 중간 변수 중 하나를 골라 어느 줄에서 만들어졌는지 설명하세요.
# 3. 출력값 하나를 골라 어떤 입력과 규칙으로 만들어졌는지 설명하세요.
# 4. 기준값이나 입력값 하나를 바꾸면 어떤 출력이 바뀔지 예측하세요.

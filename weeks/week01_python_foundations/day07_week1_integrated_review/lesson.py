"""
Day 07. 1주차 통합 숙달

이 파일은 학생이 처음부터 코드를 작성하기 위한 파일이 아닙니다.
이미 작성된 코드를 읽고, 주석을 따라가며, 값의 흐름을 해석하기 위한 수업 파일이다.

이 장의 중심 생각:
값, 타입, 조건, 반복, 함수, 오류를 연결해 작은 Python 프로그램을 읽는다.

읽을 용어:
review, trace, input, process, output
"""

print("DAY:", 7)
print("TOPIC:", "1주차 통합 숙달")
print("CORE IDEA:", "값, 타입, 조건, 반복, 함수, 오류를 연결해 작은 Python 프로그램을 읽는다.")

# 1. 수업용 합성 데이터이다.
#    실제 환자 정보가 아니라, 오늘 개념을 읽기 위한 작은 예제이다.
# 4. 여러 행에서 같은 열의 값만 모읍니다.
#    일차별 주제가 달라도 "입력 -> 중간 값 -> 출력" 흐름을 찾는 연습은 같습니다.

    # 1주차 내용을 연결해 작은 입력-처리-출력 흐름을 읽습니다.
records = [{"id": "P001", "glucose": 91}, {"id": "P002", "glucose": 118}]

def needs_review(row: dict) -> bool:
    return row["glucose"] >= 100

report = []
for row in records:
    report.append({"id": row["id"], "review": needs_review(row)})

print("records:", records)
print("report:", report)
print("reading task:", "list, dict, function, for, if의 역할을 한 줄씩 분리해 설명한다.")

# 9. 읽기 과제이다.
# 마지막 확인 질문이다.
# 1. 이 파일에서 가장 먼저 만들어진 값은 무엇인가?
# 2. 중간 변수 중 하나를 골라 어느 줄에서 만들어졌는지 설명하라.
# 3. 출력값 하나를 골라 어떤 입력과 규칙으로 만들어졌는지 설명하라.
# 4. 기준값이나 입력값 하나를 바꾸면 어떤 출력이 바뀔지 예측한다.

"""
Day 03. dictionary, tuple, set과 객체 모델

이 파일은 학생이 처음부터 코드를 작성하기 위한 파일이 아닙니다.
이미 작성된 코드를 읽고, 주석을 따라가며, 값의 흐름을 해석하기 위한 수업 파일이다.

이 장의 중심 생각:
dict는 이름으로 값을 찾고, tuple과 set은 데이터의 성격을 다르게 표현한다.

읽을 용어:
dict, key, value, tuple, set
"""

print("DAY:", 3)
print("TOPIC:", "dictionary, tuple, set과 객체 모델")
print("CORE IDEA:", "dict는 이름으로 값을 찾고, tuple과 set은 데이터의 성격을 다르게 표현한다.")

# 1. 수업용 합성 데이터이다.
#    실제 환자 정보가 아니라, 오늘 개념을 읽기 위한 작은 예제이다.
# 4. 여러 행에서 같은 열의 값만 모읍니다.
#    일차별 주제가 달라도 "입력 -> 중간 값 -> 출력" 흐름을 찾는 연습은 같습니다.

    # dict는 key로 값을 찾고, tuple과 set은 데이터의 성격을 다르게 표현한다.
patient = {"id": "P001", "age": 21, "group": "A"}
immutable_pair = ("glucose", 107)
observed_groups = {"A", "B", "A"}

print("patient keys:", list(patient.keys()))
print("age by key:", patient["age"])
print("tuple item:", immutable_pair[0], immutable_pair[1])
print("unique groups:", sorted(observed_groups))
print("reading task:", "dict는 순서보다 이름으로 값을 찾는 데 초점을 둡니다.")

# 9. 읽기 과제이다.
# 마지막 확인 질문이다.
# 1. 이 파일에서 가장 먼저 만들어진 값은 무엇인가?
# 2. 중간 변수 중 하나를 골라 어느 줄에서 만들어졌는지 설명하라.
# 3. 출력값 하나를 골라 어떤 입력과 규칙으로 만들어졌는지 설명하라.
# 4. 기준값이나 입력값 하나를 바꾸면 어떤 출력이 바뀔지 예측한다.

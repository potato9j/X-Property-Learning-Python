"""
Day 24. attention, QKV, mask와 multi-head

이 파일은 학생이 처음부터 코드를 작성하기 위한 파일이 아닙니다.
이미 작성된 코드를 읽고, 주석을 따라가며, 값의 흐름을 해석하기 위한 수업 파일입니다.

오늘의 중심 생각:
attention은 한 위치가 다른 위치의 정보를 얼마나 참고할지 계산하는 방식이다.

핵심 용어:
query, key, value, mask, multi-head
"""

print("DAY:", 24)
print("TOPIC:", "attention, QKV, mask와 multi-head")
print("CORE IDEA:", "attention은 한 위치가 다른 위치의 정보를 얼마나 참고할지 계산하는 방식이다.")

# 1. 수업용 합성 데이터입니다.
#    실제 환자 정보가 아니라, 오늘 개념을 읽기 위한 작은 예제입니다.
# 4. 여러 행에서 같은 열의 값만 모읍니다.
#    일차별 주제가 달라도 "입력 -> 중간 값 -> 출력" 흐름을 찾는 연습은 같습니다.

    # attention은 query가 key를 보고 value를 얼마나 참고할지 정합니다.
query = [1.0, 0.0]
keys = [[1.0, 0.0], [0.0, 1.0]]
values = ["current token", "previous token"]
scores = [sum(q * k for q, k in zip(query, key)) for key in keys]
selected_index = scores.index(max(scores))

print("attention scores:", scores)
print("selected value:", values[selected_index])
print("reading task:", "QK 점수는 참고할 위치를 고르고, V는 실제로 가져오는 정보입니다.")

# 9. 읽기 과제입니다.
# 마지막 확인 질문입니다.
# 1. 이 파일에서 가장 먼저 만들어진 값은 무엇인가?
# 2. 중간 변수 중 하나를 골라 어느 줄에서 만들어졌는지 설명하세요.
# 3. 출력값 하나를 골라 어떤 입력과 규칙으로 만들어졌는지 설명하세요.
# 4. 기준값이나 입력값 하나를 바꾸면 어떤 출력이 바뀔지 예측하세요.

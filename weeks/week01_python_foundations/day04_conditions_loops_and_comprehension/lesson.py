"""
Day 04. 조건문, 반복문과 comprehension

이 파일은 학생이 처음부터 코드를 작성하기 위한 파일이 아닙니다.
이미 작성된 코드를 읽고, 주석을 따라가며, 값의 흐름을 해석하기 위한 수업 파일이다.

이 장의 중심 생각:
조건과 반복은 여러 행을 같은 기준으로 해석하게 해 준다.

읽을 용어:
if, for, while, condition, comprehension
"""

print("DAY:", 4)
print("TOPIC:", "조건문, 반복문과 comprehension")
print("CORE IDEA:", "조건과 반복은 여러 행을 같은 기준으로 해석하게 해 준다.")

# 1. 수업용 합성 데이터이다.
#    실제 환자 정보가 아니라, 오늘 개념을 읽기 위한 작은 예제이다.
# 4. 여러 행에서 같은 열의 값만 모읍니다.
#    일차별 주제가 달라도 "입력 -> 중간 값 -> 출력" 흐름을 찾는 연습은 같습니다.

    # 조건문과 반복문은 여러 행을 같은 기준으로 읽게 한다.
glucose_values = [91, 107, 86, 118]
threshold = 100
flags = []

for value in glucose_values:
    if value >= threshold:
        flags.append("review")
    else:
        flags.append("ok")

compact_flags = ["review" if value >= threshold else "ok" for value in glucose_values]
print("flags:", flags)
print("compact flags:", compact_flags)
print("reading task:", "for는 값을 하나씩 꺼내고 if는 기준에 따라 갈림길을 만듭니다.")

# 9. 읽기 과제이다.
# 마지막 확인 질문이다.
# 1. 이 파일에서 가장 먼저 만들어진 값은 무엇인가?
# 2. 중간 변수 중 하나를 골라 어느 줄에서 만들어졌는지 설명하라.
# 3. 출력값 하나를 골라 어떤 입력과 규칙으로 만들어졌는지 설명하라.
# 4. 기준값이나 입력값 하나를 바꾸면 어떤 출력이 바뀔지 예측한다.

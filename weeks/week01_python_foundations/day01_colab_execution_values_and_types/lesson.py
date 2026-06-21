"""
Day 01. Colab 실행, 값, 표현식과 타입

이 파일은 학생이 처음부터 코드를 작성하기 위한 파일이 아닙니다.
이미 작성된 코드를 읽고, 주석을 따라가며, 값의 흐름을 해석하기 위한 수업 파일이다.

이 장의 중심 생각:
Python 코드는 값을 만들고 이름을 붙이며 위에서 아래로 실행된다.

읽을 용어:
value, expression, variable, type, execution order
"""

print("DAY:", 1)
print("TOPIC:", "Colab 실행, 값, 표현식과 타입")
print("CORE IDEA:", "Python 코드는 값을 만들고 이름을 붙이며 위에서 아래로 실행된다.")

# 1. 수업용 합성 데이터이다.
#    실제 환자 정보가 아니라, 오늘 개념을 읽기 위한 작은 예제이다.
# 4. 여러 행에서 같은 열의 값만 모읍니다.
#    일차별 주제가 달라도 "입력 -> 중간 값 -> 출력" 흐름을 찾는 연습은 같습니다.

    # 값, 표현식, 변수, 타입을 한 줄씩 확인한다.
systolic = 118
diastolic = 76
label = "stable"
is_normal_range = systolic < 120 and diastolic < 80

print("systolic value:", systolic)
print("systolic type:", type(systolic).__name__)
print("label type:", type(label).__name__)
print("comparison result:", is_normal_range, type(is_normal_range).__name__)
print("reading task:", "오른쪽 값이 먼저 계산되고 왼쪽 이름에 붙습니다.")

# 9. 읽기 과제이다.
# 마지막 확인 질문이다.
# 1. 이 파일에서 가장 먼저 만들어진 값은 무엇인가?
# 2. 중간 변수 중 하나를 골라 어느 줄에서 만들어졌는지 설명하라.
# 3. 출력값 하나를 골라 어떤 입력과 규칙으로 만들어졌는지 설명하라.
# 4. 기준값이나 입력값 하나를 바꾸면 어떤 출력이 바뀔지 예측한다.

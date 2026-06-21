"""
Day 05. 함수, scope와 type hint

이 파일은 학생이 처음부터 코드를 작성하기 위한 파일이 아닙니다.
이미 작성된 코드를 읽고, 주석을 따라가며, 값의 흐름을 해석하기 위한 수업 파일입니다.

오늘의 중심 생각:
함수는 반복되는 해석 절차에 이름을 붙이고 입력과 출력을 분명히 한다.

핵심 용어:
function, parameter, return, scope, type hint
"""

print("DAY:", 5)
print("TOPIC:", "함수, scope와 type hint")
print("CORE IDEA:", "함수는 반복되는 해석 절차에 이름을 붙이고 입력과 출력을 분명히 한다.")

# 1. 수업용 합성 데이터입니다.
#    실제 환자 정보가 아니라, 오늘 개념을 읽기 위한 작은 예제입니다.
# 4. 여러 행에서 같은 열의 값만 모읍니다.
#    일차별 주제가 달라도 "입력 -> 중간 값 -> 출력" 흐름을 찾는 연습은 같습니다.

    # 함수는 반복되는 절차에 이름을 붙이고 입력과 출력을 분명하게 만듭니다.
def classify_glucose(value: int, threshold: int = 100) -> str:
    if value >= threshold:
        return "review"
    return "ok"

values = [91, 107, 86, 118]
labels = [classify_glucose(value) for value in values]

print("labels:", labels)
print("custom threshold:", classify_glucose(107, threshold=110))
print("reading task:", "parameter는 함수 안에서만 쓰이는 이름이고 return은 밖으로 나가는 값입니다.")

# 9. 읽기 과제입니다.
# 마지막 확인 질문입니다.
# 1. 이 파일에서 가장 먼저 만들어진 값은 무엇인가?
# 2. 중간 변수 중 하나를 골라 어느 줄에서 만들어졌는지 설명하세요.
# 3. 출력값 하나를 골라 어떤 입력과 규칙으로 만들어졌는지 설명하세요.
# 4. 기준값이나 입력값 하나를 바꾸면 어떤 출력이 바뀔지 예측하세요.

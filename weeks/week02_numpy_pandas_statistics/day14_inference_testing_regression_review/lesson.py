"""
Day 14. 추론, 검정, 회귀와 2주차 숙달

이 파일은 학생이 처음부터 코드를 작성하기 위한 파일이 아닙니다.
이미 작성된 코드를 읽고, 주석을 따라가며, 값의 흐름을 해석하기 위한 수업 파일이다.

이 장의 중심 생각:
추론과 검정은 차이를 보았을 때 그 차이가 우연인지 구조인지 묻는 절차다.

읽을 용어:
confidence interval, p-value, test, correlation, regression
"""

print("DAY:", 14)
print("TOPIC:", "추론, 검정, 회귀와 2주차 숙달")
print("CORE IDEA:", "추론과 검정은 차이를 보았을 때 그 차이가 우연인지 구조인지 묻는 절차다.")

# 1. 수업용 합성 데이터이다.
#    실제 환자 정보가 아니라, 오늘 개념을 읽기 위한 작은 예제이다.
# 4. 여러 행에서 같은 열의 값만 모읍니다.
#    일차별 주제가 달라도 "입력 -> 중간 값 -> 출력" 흐름을 찾는 연습은 같습니다.

    # 추론과 회귀는 차이와 관계를 조심스럽게 읽는 절차이다.
x_age = [19, 21, 22, 20]
y_glucose = [91, 107, 86, 118]
x_mean = sum(x_age) / len(x_age)
y_mean = sum(y_glucose) / len(y_glucose)
numerator = sum((x - x_mean) * (y - y_mean) for x, y in zip(x_age, y_glucose))
denominator = sum((x - x_mean) ** 2 for x in x_age)
slope = numerator / denominator

print("age mean:", x_mean)
print("glucose mean:", y_mean)
print("simple regression slope:", round(slope, 2))
print("reading task:", "기울기는 x가 1 증가할 때 y가 평균적으로 어떻게 움직이는지 읽는 값이다.")

# 9. 읽기 과제이다.
# 마지막 확인 질문이다.
# 1. 이 파일에서 가장 먼저 만들어진 값은 무엇인가?
# 2. 중간 변수 중 하나를 골라 어느 줄에서 만들어졌는지 설명하라.
# 3. 출력값 하나를 골라 어떤 입력과 규칙으로 만들어졌는지 설명하라.
# 4. 기준값이나 입력값 하나를 바꾸면 어떤 출력이 바뀔지 예측한다.

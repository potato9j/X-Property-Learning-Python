"""
Day 13. 확률, 표본추출과 기술통계

이 파일은 학생이 처음부터 코드를 작성하기 위한 파일이 아닙니다.
이미 작성된 코드를 읽고, 주석을 따라가며, 값의 흐름을 해석하기 위한 수업 파일이다.

이 장의 중심 생각:
통계는 일부 관찰값에서 전체 경향을 조심스럽게 설명하는 언어다.

읽을 용어:
population, sample, mean, variance, distribution
"""

print("DAY:", 13)
print("TOPIC:", "확률, 표본추출과 기술통계")
print("CORE IDEA:", "통계는 일부 관찰값에서 전체 경향을 조심스럽게 설명하는 언어다.")

# 1. 수업용 합성 데이터이다.
#    실제 환자 정보가 아니라, 오늘 개념을 읽기 위한 작은 예제이다.
# 4. 여러 행에서 같은 열의 값만 모읍니다.
#    일차별 주제가 달라도 "입력 -> 중간 값 -> 출력" 흐름을 찾는 연습은 같습니다.

    # 표본, 평균, 분산은 일부 관찰값으로 전체를 조심스럽게 설명하는 언어이다.
values = [82, 91, 94, 107, 118]
mean = sum(values) / len(values)
squared_errors = [(value - mean) ** 2 for value in values]
variance = sum(squared_errors) / len(values)

print("sample values:", values)
print("mean:", round(mean, 2))
print("variance:", round(variance, 2))
print("reading task:", "평균은 중심을, 분산은 값들이 중심에서 얼마나 퍼졌는지를 설명한다.")

# 9. 읽기 과제이다.
# 마지막 확인 질문이다.
# 1. 이 파일에서 가장 먼저 만들어진 값은 무엇인가?
# 2. 중간 변수 중 하나를 골라 어느 줄에서 만들어졌는지 설명하라.
# 3. 출력값 하나를 골라 어떤 입력과 규칙으로 만들어졌는지 설명하라.
# 4. 기준값이나 입력값 하나를 바꾸면 어떤 출력이 바뀔지 예측한다.

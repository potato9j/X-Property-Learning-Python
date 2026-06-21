"""
Day 16. tensor, autograd와 gradient

이 파일은 학생이 처음부터 코드를 작성하기 위한 파일이 아닙니다.
이미 작성된 코드를 읽고, 주석을 따라가며, 값의 흐름을 해석하기 위한 수업 파일이다.

이 장의 중심 생각:
tensor는 모델 학습의 숫자 그릇이고 gradient는 손실을 줄이는 방향 정보다.

읽을 용어:
tensor, gradient, autograd, loss, parameter
"""

print("DAY:", 16)
print("TOPIC:", "tensor, autograd와 gradient")
print("CORE IDEA:", "tensor는 모델 학습의 숫자 그릇이고 gradient는 손실을 줄이는 방향 정보다.")

# 1. 수업용 합성 데이터이다.
#    실제 환자 정보가 아니라, 오늘 개념을 읽기 위한 작은 예제이다.
# 4. 여러 행에서 같은 열의 값만 모읍니다.
#    일차별 주제가 달라도 "입력 -> 중간 값 -> 출력" 흐름을 찾는 연습은 같습니다.

    # gradient는 손실을 줄이기 위해 어느 방향으로 움직일지 알려 주는 숫자이다.
weight = 0.5
x = 2.0
target = 5.0
prediction = weight * x
loss = (prediction - target) ** 2
gradient = 2 * (prediction - target) * x

print("prediction:", prediction)
print("loss:", loss)
print("gradient dloss/dweight:", gradient)
print("reading task:", "autograd는 이런 미분 계산을 tensor 연산 기록에서 자동으로 따라갑니다.")

# 9. 읽기 과제이다.
# 마지막 확인 질문이다.
# 1. 이 파일에서 가장 먼저 만들어진 값은 무엇인가?
# 2. 중간 변수 중 하나를 골라 어느 줄에서 만들어졌는지 설명하라.
# 3. 출력값 하나를 골라 어떤 입력과 규칙으로 만들어졌는지 설명하라.
# 4. 기준값이나 입력값 하나를 바꾸면 어떤 출력이 바뀔지 예측한다.

"""
Day 18. loss, optimizer와 학습 루프

이 파일은 학생이 처음부터 코드를 작성하기 위한 파일이 아닙니다.
이미 작성된 코드를 읽고, 주석을 따라가며, 값의 흐름을 해석하기 위한 수업 파일입니다.

오늘의 중심 생각:
학습 루프는 예측, 손실 계산, gradient 계산, 파라미터 갱신을 반복한다.

핵심 용어:
loss, optimizer, backward, step, epoch
"""

print("DAY:", 18)
print("TOPIC:", "loss, optimizer와 학습 루프")
print("CORE IDEA:", "학습 루프는 예측, 손실 계산, gradient 계산, 파라미터 갱신을 반복한다.")

# 1. 수업용 합성 데이터입니다.
#    실제 환자 정보가 아니라, 오늘 개념을 읽기 위한 작은 예제입니다.
# 4. 여러 행에서 같은 열의 값만 모읍니다.
#    일차별 주제가 달라도 "입력 -> 중간 값 -> 출력" 흐름을 찾는 연습은 같습니다.

    # 학습 루프는 예측, 손실, gradient, 업데이트를 반복합니다.
weight = 0.0
learning_rate = 0.1
x = 2.0
target = 4.0
for epoch in range(3):
    prediction = weight * x
    loss = (prediction - target) ** 2
    gradient = 2 * (prediction - target) * x
    weight = weight - learning_rate * gradient
    print("epoch", epoch, "loss", round(loss, 3), "weight", round(weight, 3))

print("reading task:", "optimizer.step은 파라미터를 gradient 반대 방향으로 조금 움직입니다.")

# 9. 읽기 과제입니다.
# 마지막 확인 질문입니다.
# 1. 이 파일에서 가장 먼저 만들어진 값은 무엇인가?
# 2. 중간 변수 중 하나를 골라 어느 줄에서 만들어졌는지 설명하세요.
# 3. 출력값 하나를 골라 어떤 입력과 규칙으로 만들어졌는지 설명하세요.
# 4. 기준값이나 입력값 하나를 바꾸면 어떤 출력이 바뀔지 예측하세요.

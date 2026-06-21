"""
Day 17. nn.Module, layer, activation과 forward

이 파일은 학생이 처음부터 코드를 작성하기 위한 파일이 아닙니다.
이미 작성된 코드를 읽고, 주석을 따라가며, 값의 흐름을 해석하기 위한 수업 파일이다.

이 장의 중심 생각:
신경망은 layer를 통과하며 입력을 출력으로 바꾸는 함수로 읽을 수 있다.

읽을 용어:
nn.Module, layer, activation, forward, logits
"""

print("DAY:", 17)
print("TOPIC:", "nn.Module, layer, activation과 forward")
print("CORE IDEA:", "신경망은 layer를 통과하며 입력을 출력으로 바꾸는 함수로 읽을 수 있다.")

# 1. 수업용 합성 데이터이다.
#    실제 환자 정보가 아니라, 오늘 개념을 읽기 위한 작은 예제이다.
# 4. 여러 행에서 같은 열의 값만 모읍니다.
#    일차별 주제가 달라도 "입력 -> 중간 값 -> 출력" 흐름을 찾는 연습은 같습니다.

    # layer와 activation은 입력을 다음 표현으로 바꾸는 함수로 읽습니다.
inputs = [0.5, -1.0, 2.0]
weights = [0.2, 0.4, -0.3]
bias = 0.1
linear_output = sum(x * w for x, w in zip(inputs, weights)) + bias
relu_output = max(0, linear_output)

print("linear output:", round(linear_output, 3))
print("relu output:", round(relu_output, 3))
print("reading task:", "forward는 입력이 layer를 지나 출력으로 바뀌는 경로이다.")

# 9. 읽기 과제이다.
# 마지막 확인 질문이다.
# 1. 이 파일에서 가장 먼저 만들어진 값은 무엇인가?
# 2. 중간 변수 중 하나를 골라 어느 줄에서 만들어졌는지 설명하라.
# 3. 출력값 하나를 골라 어떤 입력과 규칙으로 만들어졌는지 설명하라.
# 4. 기준값이나 입력값 하나를 바꾸면 어떤 출력이 바뀔지 예측한다.

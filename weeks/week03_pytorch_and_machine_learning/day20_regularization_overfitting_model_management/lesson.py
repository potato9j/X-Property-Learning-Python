"""
Day 20. 검증, overfitting과 모델 관리

이 파일은 학생이 처음부터 코드를 작성하기 위한 파일이 아닙니다.
이미 작성된 코드를 읽고, 주석을 따라가며, 값의 흐름을 해석하기 위한 수업 파일이다.

이 장의 중심 생각:
overfitting은 훈련 데이터는 잘 맞히지만 새 데이터에는 약한 상태다.

읽을 용어:
overfitting, regularization, validation, checkpoint, model.eval
"""

print("DAY:", 20)
print("TOPIC:", "검증, overfitting과 모델 관리")
print("CORE IDEA:", "overfitting은 훈련 데이터는 잘 맞히지만 새 데이터에는 약한 상태다.")

# 1. 수업용 합성 데이터이다.
#    실제 환자 정보가 아니라, 오늘 개념을 읽기 위한 작은 예제이다.
# 4. 여러 행에서 같은 열의 값만 모읍니다.
#    일차별 주제가 달라도 "입력 -> 중간 값 -> 출력" 흐름을 찾는 연습은 같습니다.

    # overfitting은 훈련 점수와 검증 점수가 갈라질 때 의심한다.
history = [
    {"epoch": 1, "train_loss": 0.80, "val_loss": 0.90},
    {"epoch": 2, "train_loss": 0.40, "val_loss": 0.55},
    {"epoch": 3, "train_loss": 0.20, "val_loss": 0.70},
]
best = min(history, key=lambda row: row["val_loss"])

print("history:", history)
print("best checkpoint:", best)
print("reading task:", "훈련 손실만 낮아지는 모델보다 검증 손실이 낮은 시점의 모델을 봐야 한다.")

# 9. 읽기 과제이다.
# 마지막 확인 질문이다.
# 1. 이 파일에서 가장 먼저 만들어진 값은 무엇인가?
# 2. 중간 변수 중 하나를 골라 어느 줄에서 만들어졌는지 설명하라.
# 3. 출력값 하나를 골라 어떤 입력과 규칙으로 만들어졌는지 설명하라.
# 4. 기준값이나 입력값 하나를 바꾸면 어떤 출력이 바뀔지 예측한다.

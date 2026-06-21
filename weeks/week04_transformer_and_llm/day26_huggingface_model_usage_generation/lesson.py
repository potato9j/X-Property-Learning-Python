"""
Day 26. Hugging Face 모델 추론과 생성

이 파일은 학생이 처음부터 코드를 작성하기 위한 파일이 아닙니다.
이미 작성된 코드를 읽고, 주석을 따라가며, 값의 흐름을 해석하기 위한 수업 파일이다.

이 장의 중심 생각:
사전학습 모델을 사용할 때는 입력 형식, 출력 의미, 라이선스, 한계를 함께 읽어야 한다.

읽을 용어:
model card, tokenizer, pipeline, inference, license
"""

print("DAY:", 26)
print("TOPIC:", "Hugging Face 모델 추론과 생성")
print("CORE IDEA:", "사전학습 모델을 사용할 때는 입력 형식, 출력 의미, 라이선스, 한계를 함께 읽어야 한다.")

# 1. 수업용 합성 데이터이다.
#    실제 환자 정보가 아니라, 오늘 개념을 읽기 위한 작은 예제이다.
# 4. 여러 행에서 같은 열의 값만 모읍니다.
#    일차별 주제가 달라도 "입력 -> 중간 값 -> 출력" 흐름을 찾는 연습은 같습니다.

    # 사전학습 모델 사용은 입력 형식, 출력 의미, 한계 확인이 함께 필요한다.
model_card = {"task": "text-classification", "license": "teaching-only", "trained_on": "synthetic notes"}
input_text = "patient glucose high"
fake_output = {"label": "review", "score": 0.82}

print("model card:", model_card)
print("input:", input_text)
print("output:", fake_output)
print("reading task:", "모델 출력은 근거와 한계를 함께 읽어야 하며 임상 판단으로 바로 바꾸면 안 된다.")

# 9. 읽기 과제이다.
# 마지막 확인 질문이다.
# 1. 이 파일에서 가장 먼저 만들어진 값은 무엇인가?
# 2. 중간 변수 중 하나를 골라 어느 줄에서 만들어졌는지 설명하라.
# 3. 출력값 하나를 골라 어떤 입력과 규칙으로 만들어졌는지 설명하라.
# 4. 기준값이나 입력값 하나를 바꾸면 어떤 출력이 바뀔지 예측한다.

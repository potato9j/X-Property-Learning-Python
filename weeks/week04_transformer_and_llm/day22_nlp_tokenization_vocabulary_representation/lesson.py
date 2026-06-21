"""
Day 22. NLP, tokenization과 어휘 표현

이 파일은 학생이 처음부터 코드를 작성하기 위한 파일이 아닙니다.
이미 작성된 코드를 읽고, 주석을 따라가며, 값의 흐름을 해석하기 위한 수업 파일이다.

이 장의 중심 생각:
tokenization은 문장을 모델이 처리할 수 있는 작은 단위로 바꾸는 첫 단계다.

읽을 용어:
token, vocabulary, token id, unknown, mask
"""

print("DAY:", 22)
print("TOPIC:", "NLP, tokenization과 어휘 표현")
print("CORE IDEA:", "tokenization은 문장을 모델이 처리할 수 있는 작은 단위로 바꾸는 첫 단계다.")

# 1. 수업용 합성 데이터이다.
#    실제 환자 정보가 아니라, 오늘 개념을 읽기 위한 작은 예제이다.
# 4. 여러 행에서 같은 열의 값만 모읍니다.
#    일차별 주제가 달라도 "입력 -> 중간 값 -> 출력" 흐름을 찾는 연습은 같습니다.

    # tokenization은 문장을 모델이 처리할 수 있는 작은 단위로 바꾸는 첫 단계이다.
text = "patient glucose high"
vocab = {"[PAD]": 0, "patient": 1, "glucose": 2, "high": 3}
tokens = text.split()
token_ids = [vocab.get(token, 0) for token in tokens]
attention_mask = [1 if token_id != 0 else 0 for token_id in token_ids]

print("tokens:", tokens)
print("token ids:", token_ids)
print("attention mask:", attention_mask)
print("reading task:", "mask는 실제 token과 padding을 구분하게 해 줍니다.")

# 9. 읽기 과제이다.
# 마지막 확인 질문이다.
# 1. 이 파일에서 가장 먼저 만들어진 값은 무엇인가?
# 2. 중간 변수 중 하나를 골라 어느 줄에서 만들어졌는지 설명하라.
# 3. 출력값 하나를 골라 어떤 입력과 규칙으로 만들어졌는지 설명하라.
# 4. 기준값이나 입력값 하나를 바꾸면 어떤 출력이 바뀔지 예측한다.

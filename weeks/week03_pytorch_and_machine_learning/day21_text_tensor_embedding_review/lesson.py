"""
Day 21. 텍스트 tensor, embedding과 3주차 숙달

이 파일은 학생이 처음부터 코드를 작성하기 위한 파일이 아닙니다.
이미 작성된 코드를 읽고, 주석을 따라가며, 값의 흐름을 해석하기 위한 수업 파일입니다.

오늘의 중심 생각:
텍스트도 모델 안에서는 숫자 tensor와 embedding으로 변환되어 처리된다.

핵심 용어:
text, token id, embedding, sequence, batch
"""

print("DAY:", 21)
print("TOPIC:", "텍스트 tensor, embedding과 3주차 숙달")
print("CORE IDEA:", "텍스트도 모델 안에서는 숫자 tensor와 embedding으로 변환되어 처리된다.")

# 1. 수업용 합성 데이터입니다.
#    실제 환자 정보가 아니라, 오늘 개념을 읽기 위한 작은 예제입니다.
# 4. 여러 행에서 같은 열의 값만 모읍니다.
#    일차별 주제가 달라도 "입력 -> 중간 값 -> 출력" 흐름을 찾는 연습은 같습니다.

    # 텍스트는 모델 안에서 token id와 embedding 벡터로 바뀝니다.
vocab = {"patient": 1, "stable": 2, "review": 3}
sentence = ["patient", "review"]
token_ids = [vocab[token] for token in sentence]
embeddings = {1: [0.2, 0.1], 2: [0.0, 0.3], 3: [0.4, -0.2]}
sentence_vector = [sum(embeddings[i][j] for i in token_ids) / len(token_ids) for j in range(2)]

print("token ids:", token_ids)
print("sentence vector:", sentence_vector)
print("reading task:", "텍스트도 결국 숫자 목록으로 바뀐 뒤 모델에 들어갑니다.")

# 9. 읽기 과제입니다.
# 마지막 확인 질문입니다.
# 1. 이 파일에서 가장 먼저 만들어진 값은 무엇인가?
# 2. 중간 변수 중 하나를 골라 어느 줄에서 만들어졌는지 설명하세요.
# 3. 출력값 하나를 골라 어떤 입력과 규칙으로 만들어졌는지 설명하세요.
# 4. 기준값이나 입력값 하나를 바꾸면 어떤 출력이 바뀔지 예측하세요.

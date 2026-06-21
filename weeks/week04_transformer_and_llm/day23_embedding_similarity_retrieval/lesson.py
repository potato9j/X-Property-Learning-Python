"""
Day 23. embedding, similarity와 위치 정보

이 파일은 학생이 처음부터 코드를 작성하기 위한 파일이 아닙니다.
이미 작성된 코드를 읽고, 주석을 따라가며, 값의 흐름을 해석하기 위한 수업 파일입니다.

오늘의 중심 생각:
embedding은 의미나 관계를 숫자 벡터 공간에 놓고 비교하게 해 준다.

핵심 용어:
embedding, vector, cosine similarity, retrieval, position
"""

print("DAY:", 23)
print("TOPIC:", "embedding, similarity와 위치 정보")
print("CORE IDEA:", "embedding은 의미나 관계를 숫자 벡터 공간에 놓고 비교하게 해 준다.")

# 1. 수업용 합성 데이터입니다.
#    실제 환자 정보가 아니라, 오늘 개념을 읽기 위한 작은 예제입니다.
# 4. 여러 행에서 같은 열의 값만 모읍니다.
#    일차별 주제가 달라도 "입력 -> 중간 값 -> 출력" 흐름을 찾는 연습은 같습니다.

    # embedding similarity는 질문과 문서가 얼마나 가까운지 비교합니다.
def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = sum(x * x for x in a) ** 0.5
    norm_b = sum(y * y for y in b) ** 0.5
    return dot / (norm_a * norm_b)

query = [0.2, 0.8]
docs = {"glucose note": [0.1, 0.9], "surgery note": [0.9, 0.1]}
scores = {name: round(cosine(query, vector), 3) for name, vector in docs.items()}

print("similarity scores:", scores)
print("reading task:", "retrieval은 점수가 높은 문서를 먼저 가져오는 절차입니다.")

# 9. 읽기 과제입니다.
# 마지막 확인 질문입니다.
# 1. 이 파일에서 가장 먼저 만들어진 값은 무엇인가?
# 2. 중간 변수 중 하나를 골라 어느 줄에서 만들어졌는지 설명하세요.
# 3. 출력값 하나를 골라 어떤 입력과 규칙으로 만들어졌는지 설명하세요.
# 4. 기준값이나 입력값 하나를 바꾸면 어떤 출력이 바뀔지 예측하세요.

"""
Day 27. decoding, prompting, RAG와 fine-tuning

이 파일은 학생이 처음부터 코드를 작성하기 위한 파일이 아닙니다.
이미 작성된 코드를 읽고, 주석을 따라가며, 값의 흐름을 해석하기 위한 수업 파일입니다.

오늘의 중심 생각:
LLM 응답은 decoding과 prompt, 검색 문맥, 학습 방식의 영향을 받는다.

핵심 용어:
decoding, temperature, prompt, RAG, fine-tuning
"""

print("DAY:", 27)
print("TOPIC:", "decoding, prompting, RAG와 fine-tuning")
print("CORE IDEA:", "LLM 응답은 decoding과 prompt, 검색 문맥, 학습 방식의 영향을 받는다.")

# 1. 수업용 합성 데이터입니다.
#    실제 환자 정보가 아니라, 오늘 개념을 읽기 위한 작은 예제입니다.
# 4. 여러 행에서 같은 열의 값만 모읍니다.
#    일차별 주제가 달라도 "입력 -> 중간 값 -> 출력" 흐름을 찾는 연습은 같습니다.

    # decoding, prompting, RAG, fine-tuning은 응답이 만들어지는 조건을 바꿉니다.
prompt = "Summarize the synthetic lab note."
retrieved_context = "P002 has glucose 118 in the toy dataset."
decoding = {"temperature": 0.2, "top_k": 3}
answer_plan = [prompt, retrieved_context, str(decoding)]

print("answer inputs:", answer_plan)
print("reading task:", "RAG는 외부 근거를 넣고, decoding은 후보 중 무엇을 고를지 조절합니다.")

# 9. 읽기 과제입니다.
# 마지막 확인 질문입니다.
# 1. 이 파일에서 가장 먼저 만들어진 값은 무엇인가?
# 2. 중간 변수 중 하나를 골라 어느 줄에서 만들어졌는지 설명하세요.
# 3. 출력값 하나를 골라 어떤 입력과 규칙으로 만들어졌는지 설명하세요.
# 4. 기준값이나 입력값 하나를 바꾸면 어떤 출력이 바뀔지 예측하세요.

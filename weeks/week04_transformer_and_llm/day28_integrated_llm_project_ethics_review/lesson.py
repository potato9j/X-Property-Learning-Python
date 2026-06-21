"""
Day 28. 통합 LLM 프로젝트, 윤리와 최종 숙달

이 파일은 학생이 처음부터 코드를 작성하기 위한 파일이 아닙니다.
이미 작성된 코드를 읽고, 주석을 따라가며, 값의 흐름을 해석하기 위한 수업 파일이다.

이 장의 중심 생각:
최종 목표는 LLM을 맹신하지 않고 입력, 출력, 근거, 위험을 검증하는 것이다.

읽을 용어:
hallucination, privacy, verification, ethics, final review
"""

print("DAY:", 28)
print("TOPIC:", "통합 LLM 프로젝트, 윤리와 최종 숙달")
print("CORE IDEA:", "최종 목표는 LLM을 맹신하지 않고 입력, 출력, 근거, 위험을 검증하는 것이다.")

# 1. 수업용 합성 데이터이다.
#    실제 환자 정보가 아니라, 오늘 개념을 읽기 위한 작은 예제이다.
# 4. 여러 행에서 같은 열의 값만 모읍니다.
#    일차별 주제가 달라도 "입력 -> 중간 값 -> 출력" 흐름을 찾는 연습은 같습니다.

    # 최종 프로젝트는 입력, 처리, 출력, 위험을 한 장의 보고서로 검증한다.
project = {
    "input": "synthetic patient table",
    "processing": ["clean", "summarize", "retrieve evidence", "draft answer"],
    "output": "teaching-only explanation",
    "risks": ["privacy", "hallucination", "over-trust"],
}
checks = {risk: "must review" for risk in project["risks"]}

print("project:", project)
print("risk checks:", checks)
print("reading task:", "LLM 프로젝트는 정확도뿐 아니라 개인정보, 근거, 검증 절차까지 함께 평가한다.")

# 9. 읽기 과제이다.
# 마지막 확인 질문이다.
# 1. 이 파일에서 가장 먼저 만들어진 값은 무엇인가?
# 2. 중간 변수 중 하나를 골라 어느 줄에서 만들어졌는지 설명하라.
# 3. 출력값 하나를 골라 어떤 입력과 규칙으로 만들어졌는지 설명하라.
# 4. 기준값이나 입력값 하나를 바꾸면 어떤 출력이 바뀔지 예측한다.

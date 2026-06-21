"""
Day 02. 문자열, 리스트와 순서형 자료

이 파일은 학생이 처음부터 코드를 작성하기 위한 파일이 아닙니다.
이미 작성된 코드를 읽고, 주석을 따라가며, 값의 흐름을 해석하기 위한 수업 파일입니다.

오늘의 중심 생각:
문자열과 리스트는 여러 값을 순서대로 읽는 첫 번째 자료구조다.

핵심 용어:
str, index, slice, list, append
"""

print("DAY:", 2)
print("TOPIC:", "문자열, 리스트와 순서형 자료")
print("CORE IDEA:", "문자열과 리스트는 여러 값을 순서대로 읽는 첫 번째 자료구조다.")

# 1. 수업용 합성 데이터입니다.
#    실제 환자 정보가 아니라, 오늘 개념을 읽기 위한 작은 예제입니다.
# 4. 여러 행에서 같은 열의 값만 모읍니다.
#    일차별 주제가 달라도 "입력 -> 중간 값 -> 출력" 흐름을 찾는 연습은 같습니다.

    # 문자열은 글자의 순서, 리스트는 값의 순서를 다룹니다.
note = "glucose high"
tokens = note.split()
first_word = tokens[0]
shortened = note[:7]
tokens.append("review")

print("original note:", note)
print("tokens:", tokens)
print("first word:", first_word)
print("slice note[:7]:", shortened)
print("reading task:", "index는 0부터 시작하고 slice의 끝 위치는 포함되지 않습니다.")

# 9. 읽기 과제입니다.
# 마지막 확인 질문입니다.
# 1. 이 파일에서 가장 먼저 만들어진 값은 무엇인가?
# 2. 중간 변수 중 하나를 골라 어느 줄에서 만들어졌는지 설명하세요.
# 3. 출력값 하나를 골라 어떤 입력과 규칙으로 만들어졌는지 설명하세요.
# 4. 기준값이나 입력값 하나를 바꾸면 어떤 출력이 바뀔지 예측하세요.

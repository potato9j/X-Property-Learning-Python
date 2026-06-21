"""
Day 08. NumPy 배열, shape, dtype과 indexing

이 파일은 학생이 처음부터 코드를 작성하기 위한 파일이 아닙니다.
이미 작성된 코드를 읽고, 주석을 따라가며, 값의 흐름을 해석하기 위한 수업 파일입니다.

오늘의 중심 생각:
배열은 같은 종류의 값을 축과 위치로 다루는 방식이다.

핵심 용어:
array, shape, dtype, axis, indexing
"""

print("DAY:", 8)
print("TOPIC:", "NumPy 배열, shape, dtype과 indexing")
print("CORE IDEA:", "배열은 같은 종류의 값을 축과 위치로 다루는 방식이다.")

# 1. 수업용 합성 데이터입니다.
#    실제 환자 정보가 아니라, 오늘 개념을 읽기 위한 작은 예제입니다.
# 4. 여러 행에서 같은 열의 값만 모읍니다.
#    일차별 주제가 달라도 "입력 -> 중간 값 -> 출력" 흐름을 찾는 연습은 같습니다.

    # 2차원 리스트로 배열의 shape, dtype, indexing 감각을 먼저 익힙니다.
matrix = [[91, 19], [107, 21], [86, 22]]
row_count = len(matrix)
column_count = len(matrix[0])
first_row = matrix[0]
glucose_column = [row[0] for row in matrix]

print("shape:", (row_count, column_count))
print("first row:", first_row)
print("glucose column:", glucose_column)
print("value type:", type(matrix[0][0]).__name__)
print("reading task:", "shape는 데이터가 몇 행 몇 열인지 말해 주는 약속입니다.")

# 9. 읽기 과제입니다.
# 마지막 확인 질문입니다.
# 1. 이 파일에서 가장 먼저 만들어진 값은 무엇인가?
# 2. 중간 변수 중 하나를 골라 어느 줄에서 만들어졌는지 설명하세요.
# 3. 출력값 하나를 골라 어떤 입력과 규칙으로 만들어졌는지 설명하세요.
# 4. 기준값이나 입력값 하나를 바꾸면 어떤 출력이 바뀔지 예측하세요.

"""
Day 25. Transformer와 언어모델링

이 파일은 처음부터 코드를 작성하기 위한 파일이 아니다.
이미 작성된 코드를 읽고, 주석을 따라가며, 값의 흐름을 해석하기 위한 수업 파일이다.
"""

print("DAY:", 25)
print("TOPIC:", "Transformer와 언어모델링")

# 1. 수업용 합성 데이터
# 실제 환자 정보가 아니라 코드 읽기를 위한 작은 표본 데이터이다.
# 각 dict는 한 행이다. key는 열 이름처럼 읽고 value는 그 열의 값으로 읽는다.
records = [{'student_id': 'S01', 'glucose': 92, 'pulse': 72, 'note_count': 2}, {'student_id': 'S02', 'glucose': 107, 'pulse': 81, 'note_count': 4}, {'student_id': 'S03', 'glucose': 86, 'pulse': 69, 'note_count': 1}, {'student_id': 'S04', 'glucose': 118, 'pulse': 88, 'note_count': 5}]

# 2. 입력 구조 확인
# records는 여러 행을 담은 list이다. len(records)는 행의 개수를 계산한다.
row_count = len(records)
print("row_count:", row_count)

# 3. 기준값 만들기
# threshold는 뒤의 조건문에서 비교 기준으로 쓰이는 값이다.
threshold = 100

# 4. 여러 행에서 같은 열의 값만 모은다
# for row in records는 records 안의 행을 하나씩 row라는 이름으로 꺼낸다는 뜻이다.
glucose_values = []
for row in records:
    glucose_values.append(row["glucose"])

# 5. 조건문으로 값을 해석한다
# value >= threshold가 참이면 review, 거짓이면 ok라는 문자열을 붙인다.
flags = []
for value in glucose_values:
    if value >= threshold:
        flags.append("review")
    else:
        flags.append("ok")

# 6. 같은 흐름을 comprehension으로 압축한 형태이다.
# 긴 반복문과 같은 결과를 만들지만, 처음 배울 때는 위의 긴 형태를 먼저 읽는다.
compact_flags = ["review" if value >= threshold else "ok" for value in glucose_values]

# 7. 오늘의 용어를 코드 안의 값으로 둔다
# terms는 설명용 list이다. 코드 실행 결과보다 용어의 위치를 읽는 데 목적이 있다.
terms = ['decoder', 'logit', 'next token', 'causal mask', 'language model']

# 8. 출력은 계산 결과이다
# 출력이 곧 의학적 결론이라는 뜻은 아니다. 어떤 입력과 규칙이 결과를 만들었는지 읽는다.
print("glucose_values:", glucose_values)
print("flags:", flags)
print("compact_flags:", compact_flags)
print("terms:", terms)

# 9. 읽기 과제
# 1. records의 타입과 records 안의 첫 번째 행 타입을 말한다.
# 2. threshold가 어느 줄에서 만들어지고 어느 줄에서 다시 쓰이는지 찾는다.
# 3. flags와 compact_flags가 같은 결과를 만드는 이유를 설명한다.
# 4. Transformer와 언어모델링에서 오늘의 핵심 일반식이 어느 줄에 나타나는지 표시한다.

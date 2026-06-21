"""
Day 06. module, 오류, 파일과 디버깅

이 파일은 학생이 처음부터 코드를 작성하기 위한 파일이 아닙니다.
이미 작성된 코드를 읽고, 주석을 따라가며, 값의 흐름을 해석하기 위한 수업 파일이다.

이 장의 중심 생각:
파일과 오류 메시지를 읽는 힘은 코드 작성보다 먼저 필요한 실전 기초다.

읽을 용어:
module, import, exception, traceback, path
"""

print("DAY:", 6)
print("TOPIC:", "module, 오류, 파일과 디버깅")
print("CORE IDEA:", "파일과 오류 메시지를 읽는 힘은 코드 작성보다 먼저 필요한 실전 기초다.")

# 1. 수업용 합성 데이터이다.
#    실제 환자 정보가 아니라, 오늘 개념을 읽기 위한 작은 예제이다.
# 4. 여러 행에서 같은 열의 값만 모읍니다.
#    일차별 주제가 달라도 "입력 -> 중간 값 -> 출력" 흐름을 찾는 연습은 같습니다.

    # 오류 메시지와 파일 경로는 코드를 고칠 때 먼저 읽어야 하는 정보이다.
from pathlib import Path

data_path = Path("datasets") / "synthetic_patients.csv"
print("path text:", str(data_path))
print("file exists:", data_path.exists())

raw_value = "107"
try:
    glucose = int(raw_value)
    print("converted value:", glucose, type(glucose).__name__)
except ValueError as error:
    print("conversion failed:", error)

print("reading task:", "traceback이 나오면 마지막 줄의 오류 종류와 위치부터 읽습니다.")

# 9. 읽기 과제이다.
# 마지막 확인 질문이다.
# 1. 이 파일에서 가장 먼저 만들어진 값은 무엇인가?
# 2. 중간 변수 중 하나를 골라 어느 줄에서 만들어졌는지 설명하라.
# 3. 출력값 하나를 골라 어떤 입력과 규칙으로 만들어졌는지 설명하라.
# 4. 기준값이나 입력값 하나를 바꾸면 어떤 출력이 바뀔지 예측한다.

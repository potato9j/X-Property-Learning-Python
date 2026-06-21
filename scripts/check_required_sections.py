from pathlib import Path
from course_config import DAYS, WEEKS

ROOT = Path(__file__).resolve().parents[1]
required_sections = [
    "## 1. 이 장에서 배우는 내용이 무엇인지",
    "## 2. 전체개념",
    "## 3. 전체 구조",
    "## 4. 전체용어",
    "## 5. 설명",
    "## 6. py파일과 별개로 예제",
]

for day, week, slug, _title in DAYS:
    concept = (ROOT / "weeks" / WEEKS[week] / slug / "concept.md").read_text(encoding="utf-8")
    lesson = (ROOT / "weeks" / WEEKS[week] / slug / "lesson.py").read_text(encoding="utf-8")
    if len(concept) < 4500:
        raise AssertionError(f"concept too short: day {day}")
    for section in required_sections:
        if section not in concept:
            raise AssertionError(f"missing {section}: day {day}")
    forbidden_sections = [
        "오늘의 " + "위치",
        "왜 이 개념을 " + "먼저 배우는가",
        "교과서식 " + "설명",
        "코드 해석 " + "질문",
        "수업 중 " + "활동",
    ]
    for phrase in forbidden_sections:
        if phrase in concept:
            raise AssertionError(f"forbidden old concept heading remains: {phrase}: day {day}")
    for marker in ["# 1. 수업용 합성 데이터", "# 4. 여러 행에서 같은 열의 값만 모읍니다", "# 9. 읽기 과제"]:
        if marker not in lesson:
            raise AssertionError(f"missing lesson marker {marker}: day {day}")

print("check_required_sections: OK")

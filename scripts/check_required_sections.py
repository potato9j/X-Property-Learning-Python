from pathlib import Path
from course_config import DAYS, WEEKS

ROOT = Path(__file__).resolve().parents[1]
required_sections = [
    "## 1. 오늘의 위치",
    "## 2. 왜 이 개념을 먼저 배우는가",
    "## 3. 핵심 용어",
    "## 5. 교과서식 설명",
    "## 7. Colab에서 실행하는 방법",
    "## 14. 오늘의 정리",
]

for day, week, slug, _title in DAYS:
    concept = (ROOT / "weeks" / WEEKS[week] / slug / "concept.md").read_text(encoding="utf-8")
    lesson = (ROOT / "weeks" / WEEKS[week] / slug / "lesson.py").read_text(encoding="utf-8")
    if len(concept) < 4500:
        raise AssertionError(f"concept too short: day {day}")
    for section in required_sections:
        if section not in concept:
            raise AssertionError(f"missing {section}: day {day}")
    for marker in ["# 1. 수업용 합성 데이터", "# 4. 여러 행에서 같은 열의 값만 모읍니다", "# 9. 읽기 과제"]:
        if marker not in lesson:
            raise AssertionError(f"missing lesson marker {marker}: day {day}")

print("check_required_sections: OK")

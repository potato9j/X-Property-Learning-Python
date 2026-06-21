from pathlib import Path
from course_config import DAYS, WEEKS

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_SECTIONS = [
    "## 1. 이 장에서 배우는 내용이 무엇인지",
    "## 2. 전체개념",
    "## 3. 전체 구조",
    "## 4. 전체용어",
    "## 5. 설명",
    "## 6. py파일과 별개로 예제",
]

FORBIDDEN_OLD_SECTIONS = [
    "오늘의 위치",
    "왜 이 개념을 먼저 배우는가",
    "교과서식 설명",
    "코드 해석 질문",
    "수업 중 활동",
    "오늘의 정리",
]

FORBIDDEN_POLITE_STYLE = [
    "합니다",
    "습니다",
    "입니다",
    "됩니다",
    "하세요",
    "주세요",
    "인가요?",
    "나요?",
    "십시오",
]

LESSON_MARKERS = [
    "# 1. 수업용 합성 데이터",
    "# 4. 여러 행에서 같은 열의 값만 모은다",
    "# 9. 읽기 과제",
]

OVER_INDENTED_SYNTAX = [
    "```python\n    if ",
    "```python\n    for ",
    "```python\n    def ",
    "```python\n    class ",
    "```python\n    try:",
    "```python\n    with ",
]


def assert_no_forbidden_style(text: str, label: str) -> None:
    for phrase in FORBIDDEN_POLITE_STYLE:
        if phrase in text:
            raise AssertionError(f"polite style remains in {label}: {phrase}")


def assert_markdown_heading(text: str, heading: str, day: int) -> None:
    lines = text.splitlines()
    if heading not in lines:
        raise AssertionError(f"heading must start at column 1: {heading}: day {day}")


def assert_no_indented_headings(text: str, day: int) -> None:
    in_fence = False
    for line_no, line in enumerate(text.splitlines(), start=1):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence and line.startswith("    #"):
            raise AssertionError(f"markdown heading is indented as code block: day {day}, line {line_no}")


for day, week, slug, _title in DAYS:
    base = ROOT / "weeks" / WEEKS[week] / slug
    concept = (base / "concept.md").read_text(encoding="utf-8")
    lesson = (base / "lesson.py").read_text(encoding="utf-8")

    if len(concept) < 4500:
        raise AssertionError(f"concept too short: day {day}")

    for section in REQUIRED_SECTIONS:
        assert_markdown_heading(concept, section, day)
    assert_no_indented_headings(concept, day)

    for phrase in FORBIDDEN_OLD_SECTIONS:
        if phrase in concept:
            raise AssertionError(f"forbidden old concept heading remains: {phrase}: day {day}")

    if "일반식" not in concept:
        raise AssertionError(f"concept should explain syntax as a general form: day {day}")
    if "```python" not in concept:
        raise AssertionError(f"concept should include a Python syntax example: day {day}")
    for marker in OVER_INDENTED_SYNTAX:
        if marker in concept:
            raise AssertionError(f"syntax example starts over-indented: {marker!r}: day {day}")

    assert_no_forbidden_style(concept, f"concept day {day}")
    assert_no_forbidden_style(lesson, f"lesson day {day}")

    for marker in LESSON_MARKERS:
        if marker not in lesson:
            raise AssertionError(f"missing lesson marker {marker}: day {day}")

print("check_required_sections: OK")

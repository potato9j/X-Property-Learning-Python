from pathlib import Path
from course_config import DAYS, WEEKS

ROOT = Path(__file__).resolve().parents[1]
for day, week, slug in DAYS:
    base = ROOT / "weeks" / WEEKS[week] / slug
    if day == 1:
        checks = {
            "concept.md": ["## 1. 오늘 수업의 목적", "## 3. 값이란 무엇인가", "## 6. 타입은 값의 종류다", "## 10. 수업 진행 방식"],
            "lesson.py": ["# 1. records는", "# 3. 아래 코드는", "# 8. 읽기 과제"],
        }
    else:
        checks = {
            "01_concepts/README.md": ["## 1. 오늘의 위치", "## 2. 학습 목표", "## 4. 핵심 개념"],
            "02_examples/README.md": ["## 예제 목표", "## 실행 순서"],
            "03_practice/README.md": ["## 실습 원칙", "## 문제 1", "## 문제 5"],
            "04_quiz/README.md": ["## 객관식", "## 단답형", "## 코드 읽기", "## 디버깅"],
        }
    for rel, headings in checks.items():
        text = (base / rel).read_text(encoding="utf-8")
        for heading in headings:
            if heading not in text:
                raise AssertionError(f"missing {heading} in {base / rel}")
print("check_required_sections: OK")

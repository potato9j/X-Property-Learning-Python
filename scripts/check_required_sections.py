from pathlib import Path
from course_config import DAYS

ROOT = Path(__file__).resolve().parents[1]
WEEK_SLUGS = {
    1: "week01_python_foundations",
    2: "week02_numpy_pandas_statistics",
    3: "week03_pytorch_and_machine_learning",
    4: "week04_transformer_and_llm",
}
REQUIRED = {
    "01_concepts/README.md": ["## 1. 오늘의 위치", "## 2. 학습 목표", "## 4. 핵심 개념"],
    "02_examples/README.md": ["## 예제 목표", "## 실행 순서"],
    "03_practice/README.md": ["## 실습 원칙", "## 문제 1", "## 문제 5"],
    "04_quiz/README.md": ["## 객관식", "## 단답형", "## 코드 읽기", "## 디버깅"],
}

for day, week, slug in DAYS:
    base = ROOT / "weeks" / WEEK_SLUGS[week] / slug
    for rel, headings in REQUIRED.items():
        text = (base / rel).read_text(encoding="utf-8")
        for heading in headings:
            if heading not in text:
                raise AssertionError(f"missing section {heading} in {base / rel}")
print("check_required_sections: OK")

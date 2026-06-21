from pathlib import Path
from course_config import DAYS, WEEKS

ROOT = Path(__file__).resolve().parents[1]
standard_required = [
    "01_concepts/README.md",
    "02_examples/README.md",
    "03_practice/README.md",
    "04_quiz/README.md",
    "answers/practice_answers.md",
    "answers/quiz_answers.md",
]

for day, week, slug in DAYS:
    base = ROOT / "weeks" / WEEKS[week] / slug
    required = ["concept.md", "lesson.py"] if day == 1 else standard_required
    for rel in required:
        if not (base / rel).exists():
            raise AssertionError(f"missing {base / rel}")

day1 = ROOT / "weeks" / WEEKS[1] / DAYS[0][2]
old_day1_dirs = ["01_concepts", "02_examples", "03_practice", "04_quiz", "answers"]
for name in old_day1_dirs:
    if (day1 / name).exists():
        raise AssertionError(f"Day 1 should not keep split subfolder: {day1 / name}")

notebooks = list((ROOT / "weeks").rglob("*.ipynb"))
if len(notebooks) != 81:
    raise AssertionError(f"expected 81 notebooks after Day 1 py conversion, found {len(notebooks)}")
print("validate_structure: OK")

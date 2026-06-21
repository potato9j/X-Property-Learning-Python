from pathlib import Path
from course_config import DAYS, WEEKS
ROOT = Path(__file__).resolve().parents[1]
required = ["01_concepts/README.md", "02_examples/README.md", "03_practice/README.md", "04_quiz/README.md", "answers/practice_answers.md", "answers/quiz_answers.md"]
for day, week, slug in DAYS:
    base = ROOT / "weeks" / WEEKS[week] / slug
    for rel in required:
        if not (base / rel).exists():
            raise AssertionError(f"missing {base / rel}")
notebooks = list((ROOT / "weeks").rglob("*.ipynb"))
if len(notebooks) != 84:
    raise AssertionError(f"expected 84 notebooks, found {len(notebooks)}")
print("validate_structure: OK")

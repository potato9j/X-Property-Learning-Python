from pathlib import Path
from course_config import DAYS, WEEKS

ROOT = Path(__file__).resolve().parents[1]
count = 0
for day, week, slug, _title in DAYS:
    path = ROOT / "weeks" / WEEKS[week] / slug / "lesson.py"
    env = {"__name__": "__lesson__"}
    exec(compile(path.read_text(encoding="utf-8"), str(path), "exec"), env)
    count += 1
print(f"execute_lessons: OK ({count} lessons)")

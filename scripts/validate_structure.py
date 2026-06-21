from pathlib import Path
from course_config import DAYS, WEEKS

ROOT = Path(__file__).resolve().parents[1]

for day, week, slug, _title in DAYS:
    base = ROOT / "weeks" / WEEKS[week] / slug
    expected = {"concept.md", "lesson.py"}
    actual_files = {p.name for p in base.iterdir() if p.is_file()}
    actual_dirs = [p.name for p in base.iterdir() if p.is_dir()]
    if actual_files != expected:
        raise AssertionError(f"{base.relative_to(ROOT)} should contain only {expected}, found {actual_files}")
    if actual_dirs:
        raise AssertionError(f"{base.relative_to(ROOT)} should not contain subdirectories: {actual_dirs}")

if list((ROOT / "weeks").rglob("*.ipynb")):
    raise AssertionError("ipynb files should not remain in the simplified curriculum")

allowed_root_md = {"README.md", "TEACHING_GUIDE.md"}
root_md = {p.name for p in ROOT.glob("*.md")}
if root_md != allowed_root_md:
    raise AssertionError(f"unexpected root markdown files: {sorted(root_md - allowed_root_md)}")

print("validate_structure: OK")

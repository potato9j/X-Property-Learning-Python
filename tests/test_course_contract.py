from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_every_day_has_only_concept_and_lesson():
    days = list((ROOT / "weeks").glob("week*/day*"))
    assert len(days) == 28
    for day in days:
        assert (day / "concept.md").exists()
        assert (day / "lesson.py").exists()
        assert not [p for p in day.iterdir() if p.is_dir()]


def test_no_notebooks_remain():
    assert not list(ROOT.rglob("*.ipynb"))


def test_root_markdown_is_minimal():
    assert {p.name for p in ROOT.glob("*.md")} == {"README.md", "TEACHING_GUIDE.md"}


def test_concepts_are_textbook_length():
    for path in (ROOT / "weeks").rglob("concept.md"):
        assert len(path.read_text(encoding="utf-8")) >= 4500

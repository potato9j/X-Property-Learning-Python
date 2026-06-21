from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def test_readme_renders_as_markdown():
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    assert text.startswith("# 서울대학교")
    assert "```" in text

def test_all_days_have_answers():
    days = list((ROOT / "weeks").glob("week*/day*"))
    assert len(days) == 28
    assert all((day / "answers" / "practice_answers.md").exists() for day in days)

def test_datasets_are_synthetic():
    text = (ROOT / "datasets" / "README.md").read_text(encoding="utf-8")
    assert "합성 데이터" in text

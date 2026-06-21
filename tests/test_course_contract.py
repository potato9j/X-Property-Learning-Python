from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_readme_renders_as_markdown():
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    assert text.startswith("# 서울대학교")
    assert "day01_colab_execution_values_and_types/concept.md" in text


def test_day1_is_two_file_lesson():
    day1 = ROOT / "weeks" / "week01_python_foundations" / "day01_colab_execution_values_and_types"
    assert (day1 / "concept.md").exists()
    assert (day1 / "lesson.py").exists()
    assert not (day1 / "01_concepts").exists()
    assert not (day1 / "answers").exists()


def test_remaining_days_keep_answer_materials():
    days = list((ROOT / "weeks").glob("week*/day*"))
    assert len(days) == 28
    for day in days:
        if day.name.startswith("day01_"):
            continue
        assert (day / "answers" / "practice_answers.md").exists()


def test_datasets_are_synthetic():
    text = (ROOT / "datasets" / "README.md").read_text(encoding="utf-8")
    assert "합성 데이터" in text

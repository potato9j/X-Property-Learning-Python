import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
count = 0
for path in ROOT.rglob("*.ipynb"):
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("nbformat") != 4:
        raise AssertionError(f"invalid notebook: {path}")
    if not data.get("cells"):
        raise AssertionError(f"empty notebook: {path}")
    joined = json.dumps(data, ensure_ascii=False)
    for token in ["TODO", "placeholder", "추후 작성", "생략"]:
        if token in joined:
            raise AssertionError(f"banned token {token}: {path}")
    if "practice_student" in path.name and "풀이 예시입니다" in joined:
        raise AssertionError(f"solution leak: {path}")
    count += 1
if count != 84:
    raise AssertionError(f"expected 84 notebooks, found {count}")
print("validate_notebooks: OK")

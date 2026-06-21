import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
errors = []

for md in ROOT.rglob("*.md"):
    text = md.read_text(encoding="utf-8")
    for target in link_re.findall(text):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        clean = target.split("#", 1)[0]
        if clean and not (md.parent / clean).exists():
            errors.append(f"{md.relative_to(ROOT)} -> {target}")

if errors:
    raise AssertionError(chr(10).join(errors[:50]))
print("validate_markdown_links: OK")

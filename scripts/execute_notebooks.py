import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
executed = 0
for path in ROOT.rglob("*.ipynb"):
    data = json.loads(path.read_text(encoding="utf-8"))
    env = {"__name__": "__notebook__"}
    for cell in data["cells"]:
        if cell["cell_type"] == "code":
            source = "".join(cell["source"])
            exec(compile(source, str(path), "exec"), env)
    executed += 1
print(f"execute_notebooks: OK ({executed} notebooks)")

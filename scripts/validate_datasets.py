import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / "datasets" / "synthetic_patients.csv"
rows = list(csv.DictReader(path.open(encoding="utf-8")))
if len(rows) < 10:
    raise AssertionError("synthetic dataset should contain at least 10 rows")
if len({row["patient_id"] for row in rows}) != len(rows):
    raise AssertionError("duplicate patient_id")
print("validate_datasets: OK")

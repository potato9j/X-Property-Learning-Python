import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
files = ["synthetic_patients.csv", "synthetic_labs.csv", "synthetic_visits.csv", "synthetic_notes.csv"]
patient_ids = set()
for name in files:
    path = ROOT / "datasets" / name
    rows = list(csv.DictReader(path.open(encoding="utf-8")))
    if not rows:
        raise AssertionError(f"empty dataset: {name}")
    if name == "synthetic_patients.csv":
        patient_ids = {row["patient_id"] for row in rows}
        if len(patient_ids) != len(rows):
            raise AssertionError("duplicate patient_id")
    else:
        for row in rows:
            if row["patient_id"] not in patient_ids:
                raise AssertionError(f"orphan patient_id in {name}")
print("validate_datasets: OK")

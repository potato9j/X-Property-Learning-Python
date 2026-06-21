import csv
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
patient_rows = list(csv.DictReader((ROOT / "datasets" / "synthetic_patients.csv").open(encoding="utf-8")))
patient_ids = {row["patient_id"] for row in patient_rows}
if len(patient_ids) != len(patient_rows):
    raise AssertionError("duplicate patient_id")
for name in ["synthetic_labs.csv", "synthetic_visits.csv", "synthetic_notes.csv"]:
    rows = list(csv.DictReader((ROOT / "datasets" / name).open(encoding="utf-8")))
    if not rows:
        raise AssertionError(f"empty dataset: {name}")
    for row in rows:
        if row["patient_id"] not in patient_ids:
            raise AssertionError(f"orphan patient_id in {name}")
print("validate_datasets: OK")

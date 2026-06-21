import subprocess, sys

def test_datasets_are_valid():
    subprocess.run([sys.executable, "scripts/validate_datasets.py"], check=True)

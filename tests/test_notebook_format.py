import subprocess, sys

def test_notebooks_are_valid():
    subprocess.run([sys.executable, "scripts/validate_notebooks.py"], check=True)

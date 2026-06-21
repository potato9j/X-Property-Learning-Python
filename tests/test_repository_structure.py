import subprocess, sys

def test_repository_structure():
    subprocess.run([sys.executable, "scripts/validate_structure.py"], check=True)

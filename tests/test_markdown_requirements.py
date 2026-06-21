import subprocess, sys

def test_markdown_links_and_sections():
    subprocess.run([sys.executable, "scripts/validate_markdown_links.py"], check=True)
    subprocess.run([sys.executable, "scripts/check_required_sections.py"], check=True)

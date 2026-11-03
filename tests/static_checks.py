"""Dependency-free structural smoke checks for the static calculator.

This does not verify the mathematical correctness of the isomer counts.
"""
from html.parser import HTMLParser
from pathlib import Path
import re
import subprocess
import tempfile


class TagChecker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = set()

    def handle_starttag(self, tag, attrs):
        self.tags.add(tag)


root = Path(__file__).resolve().parents[1]
html = (root / "index.html").read_text(encoding="utf-8")
parser = TagChecker()
parser.feed(html)

for required in ("html", "head", "body", "title", "script", "input", "button"):
    if required not in parser.tags:
        raise SystemExit(f"Missing required HTML element: {required}")

scripts = re.findall(r"<script(?:\s[^>]*)?>(.*?)</script\s*>", html, re.I | re.S)
if not scripts:
    raise SystemExit("No inline JavaScript found")

with tempfile.TemporaryDirectory() as directory:
    for i, script in enumerate(scripts, start=1):
        path = Path(directory) / f"inline_{i}.js"
        path.write_text(script, encoding="utf-8")
        subprocess.run(["node", "--check", str(path)], check=True)

print(f"Static HTML structure and {len(scripts)} inline JavaScript block(s): OK")

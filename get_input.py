#!/usr/bin/python3
import argparse
import shutil
import subprocess
from pathlib import Path

import requests

SESSION = Path("session").read_text()

parser = argparse.ArgumentParser(description="Read input")
parser.add_argument("day", type=str)
parser.add_argument("--year", "-y", type=str, default="2025")
args = parser.parse_args()

path = Path(f"{args.year}/d{args.day.zfill(2)}/")
url = f"https://adventofcode.com/{args.year}/day/{args.day}/input"

res = requests.get(url, cookies={"session": SESSION})

if not path.parent.exists():
    print(f"Creating folder {path.parent}")
    path.parent.mkdir()

if not path.exists():
    print(f"Creating folder {path}")
    path.mkdir()

if not (path / "input.txt").exists():
    print("Writing to input.txt file")
    with open(path / "input.txt", "w") as f:
        f.write(res.text)

if not (path / "script.py").exists():
    print(f"Copying template file")
    shutil.copy("template/template.py", path / "script.py")

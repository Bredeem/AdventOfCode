#!/usr/bin/python3
import argparse
import subprocess
from pathlib import Path

parser = argparse.ArgumentParser(description='Read input')
parser.add_argument('day', type=str)
parser.add_argument('--year', '-y', type=str, default='2024')
args = parser.parse_args()

cmd = ['aocd', args.day, args.year]
path = Path(f"{args.year}/d{args.day.zfill(2)}/")

output = subprocess.run(cmd, capture_output=True, check=True)

if not path.exists():
    path.mkdir()

with open(path / "input.txt", "wb") as f:
    f.write(output.stdout)


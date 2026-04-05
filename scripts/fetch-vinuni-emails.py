#!/usr/bin/env python3
"""
Fetch VinUni emails via amy mail CLI.
Usage: python3 scripts/fetch-vinuni-emails.py [query]
Default query: vonhatcuongyy
"""
import subprocess
import sys
import os
import re

QUERY = sys.argv[1] if len(sys.argv) > 1 else "vonhatcuongyy"

def run(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
    return r.stdout + r.stderr

def main():
    # Search
    results = run(f'amy mail search "{QUERY}"')
    print(results)

    # Extract sequence numbers
    seqs = re.findall(r'^\s+(\d+)\s+', results, re.MULTILINE)
    if not seqs:
        print("No emails found.")
        return

    # Read each and save
    lines = [f"# VinUni Emails — query: {QUERY}\n"]
    for seq in seqs:
        body = run(f'amy mail read {seq}')
        lines.append(body)
        lines.append("\n---\n")

    output = "\n".join(lines)
    out_file = "private/vinuni-emails.md"
    os.makedirs("private", exist_ok=True)
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(output)
    print(f"\nSaved {len(seqs)} emails to {out_file}", file=sys.stderr)

if __name__ == "__main__":
    main()

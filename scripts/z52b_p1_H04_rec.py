#!/usr/bin/env python3
"""Append one outcome record to data/z52b/pass1/outcome_H04.jsonl. Usage: rec.py <json-file-or-'-'>"""
import json, sys
d = json.load(sys.stdin if sys.argv[1] == '-' else open(sys.argv[1]))
assert d["outcome"] in {"nothing", "covered", "interesting", "needs-compute", "skipped"}
assert set(d) == {"mid", "outcome", "summary", "evidence", "next"}, set(d)
with open("data/z52b/pass1/outcome_H04.jsonl", "a") as f:
    f.write(json.dumps(d, ensure_ascii=False) + "\n")
print("ok", d["mid"], d["outcome"])

#!/usr/bin/env python3
"""Append outcome records for batch U06 (helper). Usage: emit.py <chunk-file.json>  (list of [mid,outcome,summary,evidence,next])"""
import json, sys
OUT = "data/z52b/pass1/outcome_U06.jsonl"
recs = json.load(open(sys.argv[1]))
with open(OUT, "a") as f:
    for mid, oc, summ, ev, nxt in recs:
        assert oc in {"nothing", "covered", "interesting", "needs-compute", "skipped"}, (mid, oc)
        f.write(json.dumps({"mid": mid, "outcome": oc, "summary": summ, "evidence": ev, "next": nxt}, ensure_ascii=False) + "\n")
print("appended", len(recs))

"""Writes Pass-1 U01 outcomes (one JSON line per item) into data/z52b/pass1/outcome_U01.jsonl. Idempotent per mid (re-run rebuilds)."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from z52b_p1_U01_common import OUT
ROWS = []
def R(mid, outcome, summary, evidence, nxt=""):
    ROWS.append({"mid": mid, "outcome": outcome, "summary": summary, "evidence": evidence, "next": nxt})
D = os.path.dirname(os.path.abspath(__file__))
for fn in ("z52b_p1_U01_items_c.py", "z52b_p1_U01_items_b.py", "z52b_p1_U01_items_a.py"):
    exec(open(os.path.join(D, fn)).read())
seen = set(); out = []
for r in ROWS:
    if r["mid"] in seen: continue
    seen.add(r["mid"]); out.append(r)
with open(OUT, "w") as f:
    for r in out: f.write(json.dumps(r, ensure_ascii=False) + "\n")
print("wrote", len(out), "outcomes to", OUT)

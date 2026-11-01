# Append one outcome record (JSON on stdin) to data/z52b/pass2/outcome_SK1.jsonl after validation.
import json, sys
OUT = "data/z52b/pass2/outcome_SK1.jsonl"
rec = json.loads(sys.stdin.read())
need = {"mid", "outcome", "summary", "evidence", "not_done", "next", "prev_outcome"}
assert need <= set(rec), need - set(rec)
assert rec["outcome"] in {"nothing", "covered", "interesting", "needs-compute", "skipped"}
assert len(rec["summary"].split(". ")) <= 5, "summary too long"
with open(OUT, "a") as f:
    f.write(json.dumps(rec, ensure_ascii=False) + "\n")
print("ok", rec["mid"], rec["outcome"])

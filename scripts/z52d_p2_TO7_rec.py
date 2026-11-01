# Append one validated outcome line to data/z52b/pass2/outcome_TO7.jsonl. Reads one JSON object from stdin.
import json, sys
OUT = "data/z52b/pass2/outcome_TO7.jsonl"
rec = json.loads(sys.stdin.read())
assert rec["outcome"] in {"nothing","covered","interesting","needs-compute","skipped"}, rec["outcome"]
for k in ("mid","summary","evidence","not_done","next","prev_outcome"):
    assert k in rec, k
with open(OUT, "a") as f:
    f.write(json.dumps(rec, ensure_ascii=False) + "\n")
print("ok", rec["mid"], rec["outcome"])

# append one audit record (JSON object on stdin) to data/z52d/audit2/opus_B0.jsonl, validating fields
import json,sys
r=json.loads(sys.stdin.read())
assert set(r)=={"mid","outcome","summary","content","evidence","next"}, r.keys()
assert r["outcome"] in "nothing covered interesting needs-compute skipped".split()
assert r["content"] in (0,1,2,3)
with open("data/z52d/audit2/opus_B0.jsonl","a") as f: f.write(json.dumps(r,ensure_ascii=False)+"\n")
print("ok",r["mid"])

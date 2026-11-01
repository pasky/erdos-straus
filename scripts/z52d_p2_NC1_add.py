# Append one outcome record (JSON on stdin) to data/z52b/pass2/outcome_NC1.jsonl, validating fields.
import json, sys
OUT = 'data/z52b/pass2/outcome_NC1.jsonl'
r = json.loads(sys.stdin.read())
assert r['outcome'] in ('nothing', 'covered', 'interesting', 'needs-compute', 'skipped'), r['outcome']
for k in ('mid', 'summary', 'evidence', 'not_done', 'next', 'prev_outcome'):
    assert k in r, k
assert len(r['summary']) > 0
with open(OUT, 'a') as f:
    f.write(json.dumps(r, ensure_ascii=False) + '\n')
print('ok', r['mid'], r['outcome'])

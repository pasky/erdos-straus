"""Append outcome lines for batch U02 (validated). Usage: python scripts/z52b_p1_U02_emit.py < file.py-literal-list"""
import json, sys
ALLOWED = {'nothing', 'covered', 'interesting', 'needs-compute', 'skipped'}
OUT = 'data/z52b/pass1/outcome_U02.jsonl'
rows = eval(sys.stdin.read())
seen = set()
for r in rows:
    if len(r) == 4:
        r = (r[0], r[1], r[2], [], r[3])
    mid, outc, summ, ev, nxt = r
    assert outc in ALLOWED, (mid, outc)
    assert mid not in seen, mid
    seen.add(mid)
    assert len(summ) < 900
    with open(OUT, 'a') as f:
        f.write(json.dumps({'mid': mid, 'outcome': outc, 'summary': summ, 'evidence': ev, 'next': nxt}, ensure_ascii=False) + '\n')
print('appended', len(rows))

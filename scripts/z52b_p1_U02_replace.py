"""Replace outcome lines (one per mid) in outcome_U02.jsonl with fix-pass results; unprocessed items get explicit NOT-RUN lines."""
import json, sys
OUT = 'data/z52b/pass1/outcome_U02.jsonl'
rows = {json.loads(l)['mid']: json.loads(l) for l in open(OUT)}
new = json.load(open(sys.argv[1]))
for mid, outc, summ, ev, nxt in new:
    rows[mid] = {'mid': mid, 'outcome': outc, 'summary': summ, 'evidence': ev, 'next': nxt}
with open(OUT, 'w') as f:
    for m in rows: f.write(json.dumps(rows[m], ensure_ascii=False) + '\n')
print('rows', len(rows), 'replaced', len(new))

import json, collections
mids = [json.loads(l)['mid'] for l in open('data/z52b/pass1/batch_U04.jsonl')]
rows = {}
for l in open('data/z52b/pass1/U04/outcomes_src.txt', encoding='utf8'):
    l = l.rstrip('\n')
    if not l.strip(): continue
    parts = l.split('|')
    mid, outcome = parts[0], parts[1]
    evidence, nxt = parts[-2], parts[-1]
    summary = '|'.join(parts[2:-2])
    ev = [] if evidence.strip() in ('', 'none') else [e.strip() for e in evidence.split(';') if e.strip()]
    if outcome not in ('nothing', 'covered', 'interesting', 'needs-compute', 'skipped'):
        raise SystemExit(f'bad outcome {mid} {outcome}')
    if mid in rows: raise SystemExit(f'dup {mid}')
    rows[mid] = {'mid': mid, 'outcome': outcome, 'summary': summary.strip(),
                 'evidence': ev, 'next': nxt.strip() if outcome in ('interesting', 'needs-compute') else ''}
missing = [m for m in mids if m not in rows]; extra = [m for m in rows if m not in mids]
print('missing', missing, 'extra', extra, 'n', len(rows))
print(collections.Counter(r['outcome'] for r in rows.values()))
with open('data/z52b/pass1/outcome_U04.jsonl','w',encoding='utf8') as f:
    for m in mids:
        f.write(json.dumps(rows[m], ensure_ascii=False) + '\n')

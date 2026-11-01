"""Merge ZF0 part files (data/z52b/pass2/ZF0_part{0..7}.jsonl) into data/z52b/pass2/outcome_ZF0.jsonl in batch order,
applying the coordinator's review relabels (interesting -> nothing where the sub-worker's own summary reports a clean
negative or expected answer rather than a surprising/promising lead). Checks: exactly one record per batch mid."""
import json, collections
B = 'data/z52b/pass2/'
order = [json.loads(l)['mid'] for l in open(B + 'batch_ZF0.jsonl')]
prev = {json.loads(l)['mid']: (json.loads(l).get('pass1') or {}).get('outcome', 'none') for l in open(B + 'batch_ZF0.jsonl')}
recs = {}
for i in range(8):
    for l in open(B + 'ZF0_part%d.jsonl' % i):
        r = json.loads(l)
        assert r['mid'] not in recs, ('duplicate', r['mid'])
        recs[r['mid']] = r
missing = [m for m in order if m not in recs]; extra = [m for m in recs if m not in order]
assert not missing and not extra, (missing, extra)
RELABEL = {  # mid: reason (all interesting -> nothing)
    'Z0307': 'signed (+,−,−) solvability is the trivial construction the title anticipates',
    'Z0873': 'the powers-of-two failure is a 2-adic triviality',
    'Z2780': 'premise correction + Farey statistics; no lead',
    'Z2875': 'bounded split-cubic census; discriminant counterexample is elementary',
    'Z0984': 'bounded split/merge graph; one curiosity at n=11, no lead',
    'Z3167': 'K(p)=∞ cases are the 14 known R-zeros; finite maxima are the known C_min records',
    'Z1597': 'weak variance bound; rich levels failing is the expected class-restriction effect',
    'Z1721': 'min-u envelope matches the known C-form census; no Siegel-type bound',
    'Z2819': 'modest co-hit excess, zero primes not distinguished',
    'Z0016': 'abc gives no denominator window (negative)',
    'Z0272': 'units are never needed (negative, proved)',
    'Z0524': 'every admissible residue fails somewhere (negative)',
    'Z2708': 'requested table computed; no surprise',
    'Z2860': 'Galois-forcing densities computed; Mordell-type covering, no surprise',
    'Z2814': 'geometry of the nodal cubic computed; matches known F1/F2/F3, no ES lead',
    'Z2851': 'failure list empty (no obstruction found)',
    'Z2836': 'δ=1 for the closure, but the ES slice is a different finite alphabet (negative)',
    'Z2825': 'sign is not a narrow-class/genus invariant (negative)',
    'Z2843': 'embedding census; no lead',
    'Z2881': 'same genus, opposite signs (negative)',
    'Z2412': 'literature statistic is a different one (correction, negative)',
    'Z2561': 'tiny correlation; the positivity bias is structural',
    'Z2901': 'explicit main-term threshold 10^1000 only; remainder untouched',
    'Z1227': 'learned ranker re-learns exact residue rules; no ES lead',
    'Z1391': 'census of a reconstructed ordering; no surprise',
    'Z1434': 'conference leads, none ES',
    'Z1518': 'family transcription/verification; partial genuine coverage, no surprise',
    'Z2539': 'ten small Lean checks; no lead',
}
out = []
cnt = collections.Counter()
for m in order:
    r = dict(recs[m])
    if m in RELABEL:
        assert r['outcome'] == 'interesting', (m, r['outcome'])
        r['outcome'] = 'nothing'
        r['not_done'] = ('Coordinator review relabel interesting→nothing (' + RELABEL[m] + '). ' + (r.get('not_done') or '')).strip()
    r['prev_outcome'] = prev[m] if prev[m] else 'none'
    keys = ['mid', 'outcome', 'summary', 'evidence', 'not_done', 'next', 'prev_outcome']
    out.append({k: r.get(k, '') for k in keys})
    cnt[r['outcome']] += 1
with open(B + 'outcome_ZF0.jsonl', 'w') as f:
    for r in out: f.write(json.dumps(r, ensure_ascii=False) + '\n')
print(len(out), dict(cnt))
print('interesting:', [r['mid'] for r in out if r['outcome'] == 'interesting'])
print('covered:', [r['mid'] for r in out if r['outcome'] == 'covered'])
print('needs-compute:', [r['mid'] for r in out if r['outcome'] == 'needs-compute'])

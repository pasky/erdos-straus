# append outcome records: python3 scripts/z52d_p2_TO8_rec.py  (reads JSON list from data/z52b/pass2/TO8/pending.json, appends to outcome_TO8.jsonl)
import json, sys
OUT = 'data/z52b/pass2/outcome_TO8.jsonl'
recs = json.load(open(sys.argv[1]))
with open(OUT, 'a') as f:
    for r in recs:
        r.setdefault('prev_outcome', 'none')
        assert set(['mid','outcome','summary','evidence','not_done','next']) <= set(r), r.get('mid')
        assert r['outcome'] in ('nothing','covered','interesting','needs-compute','skipped'), r['outcome']
        f.write(json.dumps(r, ensure_ascii=False) + '\n')
print('appended', len(recs))

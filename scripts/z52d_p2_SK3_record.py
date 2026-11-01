# z52d pass2 SK3: append outcome records. Usage: python3 scripts/z52d_p2_SK3_record.py <chunk.json>
import json, sys
B = 'SK3'
OUT = f'data/z52b/pass2/outcome_{B}.jsonl'
recs = json.load(open(sys.argv[1]))
with open(OUT, 'a') as f:
    for r in recs:
        assert set(r) >= {'mid','outcome','summary','evidence','not_done','next','prev_outcome'}, r['mid']
        assert r['outcome'] in {'nothing','covered','interesting','needs-compute','skipped'}
        f.write(json.dumps(r, ensure_ascii=False) + '\n')
print('appended', len(recs))

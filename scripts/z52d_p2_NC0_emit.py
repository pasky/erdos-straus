# z52d Pass 2 NC0 — append validated outcome lines (stdin: one JSON object per line) to data/z52b/pass2/outcome_NC0.jsonl
import sys, json
IN='data/z52b/pass2/batch_NC0.jsonl'; OUT='data/z52b/pass2/outcome_NC0.jsonl'
mids={json.loads(l)['mid']:json.loads(l)['pass1']['outcome'] for l in open(IN)}
done={json.loads(l)['mid'] for l in open(OUT)} if __import__('os').path.exists(OUT) else set()
allowed={'nothing','covered','interesting','needs-compute','skipped'}
n=0
for line in sys.stdin:
    line=line.strip()
    if not line: continue
    o=json.loads(line)
    assert o['mid'] in mids, o['mid']
    assert o['mid'] not in done, 'duplicate '+o['mid']
    assert o['outcome'] in allowed, o['outcome']
    o.setdefault('prev_outcome', mids[o['mid']]); o.setdefault('evidence',[]); o.setdefault('not_done','')
    o.setdefault('next','')
    assert len(o['summary'])<=900
    open(OUT,'a').write(json.dumps(o,ensure_ascii=False)+'\n'); done.add(o['mid']); n+=1
print('appended',n,'total',len(done))

"""Build proof-avenue batches (z52d): P* = proof-attempt items (excl. pilot), Q* = structural-screen keeps.
Contiguous chunks after sorting by primary area, so a worker sees related items together."""
import json
m = [json.loads(l) for l in open('data/z52b/master.jsonl')]
pilot = {json.loads(l)['mid'] for l in open('data/z52d/avenue/batch_PILOT.jsonl')}
keys = ['mid', 'title', 'connection', 'why', 'first_step', 'alt_first_steps', 'refs', 'tags', 'areas', 'flags', 'lanes']
keep = set(json.load(open('data/z52d/avenue/screen_overrides.json'))['keep'])
for i in range(2):
    for l in open(f'data/z52d/avenue/screened_S{i}.jsonl'):
        r = json.loads(l)
        if r['s'] == 1:
            keep.add(r['mid'])
area = lambda d: (d['areas'][0] if d['areas'] else 'zz', d['mid'])
pa = sorted([d for d in m if 'proof-attempt' in d['flags'] and d['mid'] not in pilot], key=area)
st = sorted([d for d in m if 'proof-attempt' not in d['flags'] and d['mid'] in keep], key=area)
def dump(prefix, lst, n):
    k = -(-len(lst) // n)
    for i in range(n):
        with open(f'data/z52d/avenue/batch_{prefix}{i:02d}.jsonl', 'w') as f:
            for d in lst[i * k:(i + 1) * k]:
                f.write(json.dumps({k2: d.get(k2) for k2 in keys}, ensure_ascii=False) + '\n')
dump('P', pa, 7)
dump('Q', st, 20)
print(len(pa), len(st))

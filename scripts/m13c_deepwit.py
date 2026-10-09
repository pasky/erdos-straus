import json, random, sys, time
from m13c_witness import witness_all
T = json.load(open(sys.argv[1])); opens = []; st = list(T['roots'])
while st:
    nd = st.pop()
    if 'children' in nd: st += nd['children']
    elif nd.get('open'): opens.append((nd['x'], nd['L']))
random.seed(1); S = random.sample(opens, int(sys.argv[2])); t0 = time.time(); c = 0
for x, L in S:
    w = witness_all(x, L)
    if w: c += 1
print(f"{len(opens)} open; sample {len(S)}: complete witness (all M | L) covers {c}; {time.time()-t0:.0f}s")

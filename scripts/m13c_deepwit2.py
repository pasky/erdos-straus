import json, random, sys, time
from collections import Counter
from m13c_witness import witness_all
T = json.load(open(sys.argv[1])); opens = []; st = list(T['roots'])
while st:
    nd = st.pop()
    if 'children' in nd: st += nd['children']
    elif nd.get('open'): opens.append((nd['x'], nd['L']))
random.seed(2); S = random.sample(opens, int(sys.argv[2])); C = Counter()
for x, L in S:
    t0 = time.time(); w = witness_all(x, L)
    if w:
        fam, P = w[0]; C[fam] += 1
        print(fam, P, f"{time.time()-t0:.1f}s")
    else: print("none", f"{time.time()-t0:.1f}s", x, L)
print(C)

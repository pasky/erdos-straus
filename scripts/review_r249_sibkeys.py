"""R249: Case-B-only sibling pairs (distinct balls of depth d in one depth-(d-1) cylinder) and whether any two
generating tuples share (m', g') or the full key (m', g', s, a). Input: dump files from review_r249_dump.py."""
import sys
from collections import defaultdict
import review_r249_caseb as cb
def P(x): return tuple(int(c) for c in x)
gen = defaultdict(list)
for f in sys.argv[2:]:
    for line in open(f):
        s, m, g, w1, C1 = line.split(); s = int(s); m, g, w1, C1 = map(P, (m, g, w1, C1))
        N = (s + 1) // 2; E = cb.E_of(m, g, w1)
        gen[(N + 1, cb.trim(cb.neg(E)[:N + 1]))].append((m, g, s, len(w1)))
D = int(sys.argv[1])
byparent = defaultdict(list)
for (d, c) in gen:
    if d <= D: byparent[(d, cb.trim(c[:d - 1]))].append(c)
npairs = shared_mg = shared_key = 0
for (d, par), ch in sorted(byparent.items()):
    if len(ch) >= 2:
        for i in range(len(ch)):
            for j in range(i + 1, len(ch)):
                npairs += 1
                A = {(k[0], k[1]) for k in gen[(d, ch[i])]}; B = {(k[0], k[1]) for k in gen[(d, ch[j])]}
                if A & B: shared_mg += 1
                if set(gen[(d, ch[i])]) & set(gen[(d, ch[j])]): shared_key += 1
        if len(ch) == 3: print("TRIPLE (all parents) at depth", d, par)
print("Case B sibling pairs (all parents, both slices, depth <= %d): %d; sharing (m',g'): %d; sharing full key: %d" % (D, npairs, shared_mg, shared_key))

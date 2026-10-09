"""O103 §4: are the 'square-mimicking off T={11,13}' open leaves explained by T-generic survivors?
usage: m13d_tgen_test.py tree.json.gz nsample seed
For each open leaf x mod L: QR(off T) := x is a square mod q^{v_q(L)} for every q | L, q not in T
(2-adic: x = 1 mod 8 if 8 | L).  For the QR leaves: online := x = 1 mod q^{v_q(L)} for all q not in T;
T-projection x' = CRT(x mod 11^a 13^b, 1 mod rest of L) (the T-generic point with the leaf's T-coordinates),
tested by the complete engine (classes M | L) — covered => that T-generic point is not a survivor at level L.
"""
import sys, json, gzip, random
from collections import Counter
from sympy import factorint
from m13d_wit import Engine
T = json.load(gzip.open(sys.argv[1], 'rt')); opens = []; st = list(T['roots'])
while st:
    nd = st.pop()
    if 'children' in nd: st += nd['children']
    elif nd.get('open'): opens.append((nd['x'], nd['L']))
def qr(x, q, e):
    if q == 2: return e < 3 or x % 8 == 1
    return pow(x % q, (q - 1) // 2, q) == 1
FC = {}
def fac(L):
    if L not in FC: FC[L] = factorint(L)
    return FC[L]
Q = [(x, L) for x, L in opens if all(qr(x, q, e) for q, e in fac(L).items() if q not in (11, 13))]
print(f"open leaves {len(opens)}, QR off T: {len(Q)}")
random.seed(int(sys.argv[3])); S = random.sample(Q, min(int(sys.argv[2]), len(Q)))
E = Engine(); C = Counter(); fams = Counter(); t11 = Counter()
for x, L in S:
    F = fac(L); mT = 11 ** F.get(11, 0) * 13 ** F.get(13, 0); R = L // mT
    online = all(x % (q ** e) == 1 for q, e in F.items() if q not in (11, 13))
    xp = (x % mT + mT * (((1 - x % mT) * pow(mT, -1, R)) % R)) % L
    assert xp % mT == x % mT and xp % R == 1
    w = E.query(xp, L)
    C[(online, bool(w))] += 1
    if w: fams[w[0][0]] += 1
    t11[(x % 11, x % 13)] += 1
print("(on T-generic line, T-projection covered):", dict(C)); print("covering families:", dict(fams))
print("(x mod 11, x mod 13):", dict(t11))

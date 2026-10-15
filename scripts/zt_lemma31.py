"""zt_lemma31.py (O227): check FF_THIRDS_CORNER Lemma 3.1 on the exact census: for every tuple, every polynomial u of
degree 1..HMAX with u(0)=1, and every m <= s-2:  E == -u (mod T^m)  <=>  m'w1^2 + u v1 == 0  <=>  u m'C1^2 + v1 == 0 (mod T^m).
usage: python zt_lemma31.py CENSUS [HMAX]"""
import itertools, re, sys
from zt_poly import add, mul, sub, mono, tval, norm
pat = re.compile(r"s=(\d+) .*? w=\[(.*?)\] C=\[(.*?)\] m'=\[(.*?)\] g'=\[(.*?)\] E=\[(.*?)\]")
L = lambda x: norm([int(v) for v in x.split(",")]) if x else []
H = int(sys.argv[2]) if len(sys.argv) > 2 else 3
us = [[1] + list(t) for h in range(1, H + 1) for t in itertools.product(range(3), repeat=h) if t[-1]]
n = bad = 0
for line in open(sys.argv[1]):
    m = pat.search(line)
    if not m:
        continue
    s = int(m[1]); w, C, mp, gp, E = (L(m[i]) for i in range(2, 7))
    v = sub(mul(mp, mul(w, C)), mono(s)); w1, C1, v1 = w[1:], C[1:], v[2:]
    for u in us:
        d0 = min(tval(add(E, u)), s - 2)
        d1 = min(tval(add(mul(mp, mul(w1, w1)), mul(u, v1))), s - 2)
        d2 = min(tval(add(mul(u, mul(mp, mul(C1, C1))), v1)), s - 2)
        n += 1
        if not (d0 == d1 == d2):
            bad += 1
print(f"(tuple, u) pairs {n}; depth mismatches (capped at s-2) {bad}")

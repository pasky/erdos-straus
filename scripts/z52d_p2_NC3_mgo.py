# Z2783: Morier-Genoud–Ovsienko q-rationals [a1,...,an]_q of the regular CF of A/p (or p/A), evaluated at q = i and
# q = e^{i pi/4}; sanity q->1 gives the rational. Test: phase / sign pattern vs Legendre (A/p) on words (p = 1 (8), p<=300).
import sys, cmath, math
from fractions import Fraction
sys.path.insert(0, 'scripts')
import z52d_p2_NC3_lib as L
def qint(a, q):
    return sum(q**k for k in range(a))
def mgo(seq, q):
    # [a1,...,an]_q = [a1]_q + q^{a1} / ( [a2]_{q^-1} + q^{-a2} / ( [a3]_q + ... ) )
    def rec(i, qq):
        if i == len(seq) - 1:
            return qint(seq[i], qq)
        return qint(seq[i], qq) + qq**seq[i] / rec(i+1, 1/qq)
    return rec(0, q)
def regcf(p, a):
    out = []; x, y = p, a
    while y:
        out.append(x // y); x, y = y, x % y
    return out
def check(seq, q): return mgo(seq, q)
# q->1 sanity
for p, a in [(13, 5), (17, 3), (101, 37)]:
    seq = regcf(p, a)
    val = mgo(seq, 1 + 1e-9)
    assert abs(val - p/a) < 1e-4, (val, p/a)
print("q->1 sanity OK")
P = int(sys.argv[1]) if len(sys.argv) > 1 else 300
from collections import Counter
stats = Counter()
for p in L.primes_upto(P):
    if p < 17 or p % 8 != 1: continue
    for (t, u, v) in L.words(p):
        A = t*u - 1
        s = L.legendre(A, p)
        for name, q in [('i', 1j), ('e^{i pi/4}', cmath.exp(1j*math.pi/4))]:
            # MGO of p/A (regular CF of p/A)
            try:
                val = mgo(regcf(p, A), q)
            except ZeroDivisionError:
                stats[(name, 'pole', s, 'pole')] += 1
                continue
            if abs(val) < 1e-12:
                stats[(name, 'zero', s, 'zero')] += 1; continue
            ph = cmath.phase(val) / math.pi
            stats[(name, 'sign', s, round(ph, 6))] += 1
# summarise: for each q, does the sign separate by phase/ |val| ?
for name in ['i', 'e^{i pi/4}']:
    keys = [k for k in stats if k[0] == name and k[1] == 'sign']
    print("  poles:", sum(v for k, v in stats.items() if k[0] == name and k[1] == 'pole'), " zeros:", sum(v for k, v in stats.items() if k[0] == name and k[1] == 'zero'))
    ph_s = {}
    for k in keys:
        ph_s.setdefault(k[3], set()).add(k[2])
    mixed = sum(1 for v in ph_s.values() if len(v) > 1)
    print(name, "distinct phases:", len(ph_s), "phases shared by both signs:", mixed)
    print("  examples:", sorted(ph_s.items(), key=lambda kv: kv[0])[:6])
# majority-vote accuracy of phase(q=e^{i pi/4}) -> sign, and of phase(q=e^{i pi/4}) -> (t,u,v) mod 4 pattern
from collections import defaultdict
q = cmath.exp(1j*math.pi/4)
cls = defaultdict(Counter)
tot = 0
for p in L.primes_upto(P):
    if p < 17 or p % 8 != 1: continue
    for (t, u, v) in L.words(p):
        A = t*u - 1
        try:
            val = mgo(regcf(p, A), q)
        except ZeroDivisionError:
            continue
        ph = round(cmath.phase(val)/math.pi, 6)
        cls[ph][L.legendre(A, p)] += 1; tot += 1
acc = sum(max(c.values()) for c in cls.values())
print("e^{i pi/4}: words", tot, "majority accuracy phase->sign:", round(acc/tot, 4))
# is the phase a function of (t,u,v) mod 4 ?  and of the regular CF of p/A mod 4 ?
g1 = defaultdict(set); g2 = defaultdict(set)
for p in L.primes_upto(P):
    if p < 17 or p % 8 != 1: continue
    for (t, u, v) in L.words(p):
        A = t*u - 1
        try:
            val = mgo(regcf(p, A), q)
        except ZeroDivisionError:
            continue
        ph = round(cmath.phase(val)/math.pi, 6)
        g1[(t % 4, u % 4, v % 4)].add(ph)
        g2[tuple(x % 4 for x in regcf(p, A))].add(ph)
print("phase determined by (t,u,v) mod 4:", all(len(s) == 1 for s in g1.values()), "classes", len(g1), "conflicting", sum(1 for s in g1.values() if len(s)>1))
print("phase determined by regular CF of p/A mod 4:", all(len(s) == 1 for s in g2.values()), "classes", len(g2), "conflicting", sum(1 for s in g2.values() if len(s)>1))

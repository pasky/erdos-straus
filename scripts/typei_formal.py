"""O31 (POINTWISE_TYPEI.md §6.2): formal ck_min at an H-generic point.

Point: p* with prescribed residues p = a_l (mod l^{e_l}) at finitely many primes (argument list l:a:e),
and p = 1 (mod l^E) at every other prime l <= B.  At such a point, for every slice (c,k) with ck<=X the
B-part f_{c,k} of N=p^2+4ck^2 is fixed (we check v_l(N(p*)) < exponent used), and under Schinzel's H
there are infinitely many primes p in the class with every cofactor N/f_{c,k} prime (Thm 2.1 steps 3-4;
needs B >= 2*#slices+2, B >= X, every prescribed class reduced).  For those p,
M_{c,k}(p) = 2 #{D | f : D = -p (mod 4ck)}   (Thm 2.1 step 5),
so ck_min(p) = formal ck_min computed here, and n_p is the formal least non-residue.
Usage: typei_formal.py X B l:a:e [l:a:e ...]"""
import sys
from math import log
from sympy import primerange, factorint, divisors

X, B = int(sys.argv[1]), int(sys.argv[2])
presc = {}
for t in sys.argv[3:]:
    l, a, e = (int(u) for u in t.split(':'))
    presc[l] = (a % l ** e, e)
P = list(primerange(2, B + 1))
# exponent: big enough that l^E exceeds 1+4X^3 (so v_l(N) < E is checkable)
mods, res = [], []
for l in P:
    if l in presc:
        a, e = presc[l]
        m = l ** e
    else:
        e = 1
        while l ** e <= 4 * X ** 3 + 1:
            e += 1
        m, a = l ** e, 1
    mods.append(m)
    res.append(a)
Q, p = 1, 0
for m, a in zip(mods, res):
    t = ((a - p) * pow(Q, -1, m)) % m
    p, Q = p + Q * t, Q * m
assert p % 24 == 1, "need p = 1 (24)"
modof = dict(zip(P, mods))


def leg(a, q):
    a %= q
    return 0 if a == 0 else (1 if pow(a, (q - 1) // 2, q) == 1 else -1)


n_formal = next((q for q in P if q > 2 and leg(p, q) == -1 and True), None)
# least non-residue: (q/p) = (p/q) for p = 1 (4); q=2: (2/p)=1 iff p=1,7 (8)
nres = [q for q in P if (q == 2 and p % 8 not in (1, 7)) or (q > 2 and leg(p, q) == -1)]
print(f"formal point: p mod Q, Q has {len(P)} primes <= {B}; formal n_p = {nres[0] if nres else '>B'}")
nslices = 0
for Pck in range(1, X + 1):
    for c in divisors(Pck):
        k = Pck // c
        fc = factorint(c)
        s = 1
        for q, e in fc.items():
            if e % 2:
                s *= q
        if s in (1, 2, 3, 6):
            continue
        nslices += 1
        # genus: chi_s(p) = prod (q/p) over q | s  (p = 1 (8) assumed for q=2 handled by nres)
        chi = 1
        for q in factorint(s):
            chi *= -1 if q in nres else 1
        if chi == 1:
            continue
        h = 4 * c * k
        for l, e in factorint(h).items():
            assert modof[l] % l ** e == 0, ("target class not fixed by the point at", l, c, k)
        N = p * p + 4 * c * k * k
        f = 1
        for l in P:
            v = 0
            while N % l == 0:
                N //= l
                v += 1
            if v:
                assert l ** v < modof[l] and (p * p + 4 * c * k * k) % modof[l] != 0, ("exponent too small", l, c, k)
                f *= l ** v
        hits = [D for D in divisors(f) if (D + p) % h == 0]
        if hits:
            print(f"formal ck_min = {Pck}  slice (c,k)=({c},{k}) fixed part {factorint(f)} target D={hits[:3]}")
            assert B >= 2 * nslices + 2 and B >= X, "B too small for the H-construction"
            sys.exit(0)
print(f"formal ck_min > {X} (no target in fixed parts; {nslices} slices)")
assert B >= 2 * nslices + 2, "B too small for the H-construction"

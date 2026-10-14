#!/usr/bin/env python3
"""R217: (1) random-polynomial check of the §5 expansion over F_3 (c in {1,2}):
   with w1 = c g' v1 (1+cT) + T^n w, C1 = -c g' v1 - T^n w, P = m' g'^2 v1 (1+cT) + 1:
   m' w1 C1 - v1 == -v1 P - c m' g' v1 T^n w (cT - 1) - m' T^{2n} w^2   and  w1 + C1 == T g' v1,
   w1 + (1+cT) C1 == -c T^{n+1} w.
(2) the cyclotomic family of §5 (M2 repair) at h = 3: all ordered factorisations m' w1 C1 = T^26 - 1 over F_3 (s = 28,
   v1 = -1, v = -T^2) that give genuine Case B tuples (B) (w = T w1, C = T C1, g' = (w + C)/v monic, T not| g')."""
import random, itertools, sys
sys.path.insert(0, 'scripts')
from review_fs_tuples import add, neg, mul, divmod_, trim
p = 3
def rnd(d): return trim([random.randrange(p) for _ in range(d)] + [1])
def sc(c, a): return trim([(c * x) % p for x in a])
def Tn(n): return [0] * n + [1]
random.seed(7); ok = 0
for trial in range(3000):
    n = random.randint(2, 9); c = random.choice([1, 2])
    mp, gp, v1, om = rnd(random.randint(0, 6)), rnd(random.randint(0, 6)), rnd(random.randint(0, 6)), trim([random.randrange(p) for _ in range(random.randint(0, 6))])
    u = [1, c]
    w1 = add(mul(sc(c, mul(gp, v1, p)), u, p), mul(Tn(n), om, p), p)
    C1 = add(neg(sc(c, mul(gp, v1, p)), p), neg(mul(Tn(n), om, p), p), p)
    P = add(mul(mul(mp, mul(gp, gp, p), p), mul(v1, u, p), p), [1], p)
    lhs = add(mul(mp, mul(w1, C1, p), p), neg(v1, p), p)
    rhs = add(add(neg(mul(v1, P, p), p), neg(sc(c, mul(mul(mp, gp, p), mul(mul(v1, Tn(n), p), mul(om, [p - 1, c], p), p), p)), p), p),
              neg(mul(mp, mul(Tn(2 * n), mul(om, om, p), p), p), p), p)
    e2 = add(w1, C1, p) == mul([0, 1], mul(gp, v1, p), p)
    e3 = add(w1, mul(u, C1, p), p) == neg(sc(c, mul(Tn(n + 1), om, p)), p)
    ok += (lhs == rhs) and e2 and e3
print('§5 expansion identities hold on', ok, 'of 3000 random instances')
# (2) cyclotomic family, h = 3
def monic_irred(deg):
    out = []
    for co in itertools.product(range(p), repeat=deg):
        f = list(co) + [1]
        if all(divmod_(f, g, p)[1] for d in range(1, deg // 2 + 1) for g in ([list(cc) + [1] for cc in itertools.product(range(p), repeat=d)])):
            out.append(f)
    return out
irr = [f for f in monic_irred(1) if f != [0, 1]] + monic_irred(3)
F = add(Tn(26), [p - 1], p)
prod = [1]
for f in irr: prod = mul(prod, f, p)
assert prod == F, 'factorisation of T^26 - 1'
s = 28; v = neg(Tn(2), p); cnt = 0; pats = {}
for assign in itertools.product(range(3), repeat=len(irr)):
    parts = [[1], [1], [1]]
    for f, k in zip(irr, assign): parts[k] = mul(parts[k], f, p)
    mp, w1, C1 = parts
    w, C = [0] + w1, [0] + C1
    gq, r = divmod_(add(w, C, p), v, p)
    if r or not gq or gq[-1] != 1 or gq[0] == 0: continue
    # (B): m' w C = T^s + v holds by construction (m' w1 C1 = T^26 - 1); check it anyway
    assert mul(mp, mul(w, C, p), p) == add(Tn(s), v, p)
    cnt += 1; key = (len(w) - 1, len(mp) - 1, len(gq) - 1); pats[key] = pats.get(key, 0) + 1
print(f'cyclotomic h=3 (s=28, v1=-1): {cnt} genuine Case B tuples; patterns (a, z, y): {sorted(pats.items(), key=lambda kv: -kv[1])[:6]}')

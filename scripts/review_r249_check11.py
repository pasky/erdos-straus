"""R249: checks of SIBLING Lemma 1.1 and Prop 1.3 on from-scratch Case B tuples (q = 3)."""
import sys
from collections import defaultdict
import review_r249_caseb as cb
Q = 3
def P(sx): return tuple(int(c) for c in sx)
def deg(p): return len(p) - 1
def modT(p, n): return cb.trim(p[:n])
def sigma(p, sign_exp):  # (-1)^e p(-T)
    r = [c * (-1) ** i for i, c in enumerate(p)]
    return cb.trim([c * (-1) ** sign_exp for c in r])
def inv_modT(p, n):  # inverse of unit p mod T^n
    r = [0] * n; p = list(p) + [0] * n
    inv0 = pow(p[0], Q - 2, Q)
    for i in range(n):
        acc = (1 if i == 0 else 0) - sum(p[j] * r[i - j] for j in range(1, i + 1))
        r[i] = acc * inv0 % Q
    return cb.trim(r)
tuples = []
for f in sys.argv[1:]:
    for line in open(f):
        s, m, g, w1, C1 = line.split(); tuples.append((int(s), P(m), P(g), P(w1), P(C1)))
print("tuples", len(tuples))
# Lemma 1.1
grp = defaultdict(set); par = 0; balls = set()
for (s, m, g, w1, C1) in tuples:
    N = (s + 1) // 2
    E = cb.E_of(m, g, w1)
    a = deg(w1) + 1
    V = modT(cb.neg(E), N)
    grp[(m, g, s, a, V)].add(E)
    z, y, b = deg(m), deg(g), deg(C1) + 1
    v1 = cb.sub(cb.mul(cb.mul(m, w1), C1), cb.Tpow(s - 2)); t = deg(v1) + 2
    if not (z % 2 == t % 2 == s % 2): par += 1
    assert y + t == max(a, b), (s, m, g, w1, C1)
    # sigma map
    ms, gs, ws, Cs = sigma(m, z), sigma(g, y), sigma(w1, a - 1), sigma(C1, b - 1)
    assert cb.check_tuple(s, ms, gs, ws, Cs) is not None, "sigma fails"
    Es = cb.E_of(ms, gs, ws); assert Es == sigma(E, 0), "E^sigma"
    balls.add((N + 1, modT(cb.neg(E), N + 1)))
mx = max(len(v) for v in grp.values())
print("Lemma1.1: max distinct E per (key, parent) =", mx, "; #(key,parent) with 2:", sum(len(v) == 2 for v in grp.values()))
print("parity violations", par)
# ball-set invariance
def neg_T(c): return sigma(c, 0)
bad = defaultdict(int); fixedI = 0
for (d, c) in balls:
    if (d, modT(neg_T(c), d)) not in balls: bad["u(-T)"] += 1
    ci = inv_modT(c, d)
    if (d, ci) not in balls: bad["1/u"] += 1
    io = inv_modT(neg_T(c), d)
    if (d, io) not in balls: bad["iota"] += 1
    if io == c: fixedI += 1
print("balls", len(balls), "by depth", sorted(defaultdict(int, {}).items()) or "", dict(bad), "iota-fixed", fixedI)
from collections import Counter
print(Counter(d for d, c in balls))

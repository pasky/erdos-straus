"""Three-coset Kneser bound (z52 bank §1(c)).  For primes p = 1 (4) <= LIM and forced windows q = 3 (4) prime, q <= QMAX,
(q/p) = -1, x = (p+q)/4: if the full window fails (-1 not in R(px) = R(x) u pR(x) u p^-1 R(x)), check for both stabilisers
H = Stab(R(x)) (astra) and H = Stab(R(px)) (argon): H <= U, d = [U:H] >= 3, 1 <= Omega_out(x) <= d - 2, no prime factor of
x in -H, x and p not in -H (for Stab(R(px))).  Also records how often the bound is attained (Omega_out = d - 2)."""
import sys
from sympy import primerange, factorint, primitive_root, legendre_symbol
LIM, QMAX = int(sys.argv[1]), int(sys.argv[2])
def setup(q):
    g = primitive_root(q); lg = {}; v = 1
    for e in range(q - 1): lg[v] = e; v = v * g % q
    return lg
LG = {q: setup(q) for q in primerange(3, QMAX + 1) if q % 4 == 3}
def box(n, q, lg):
    o = q - 1; B = {0}
    for s, v in factorint(n).items():
        a = lg[s % q]; steps = {(j * a) % o for j in range(-v, v + 1)}
        B = {(b + c) % o for b in B for c in steps}
    return B
def stab(B, o):
    return {h for h in range(o) if all((b + h) % o in B for b in B)}
stats = dict(fail=0, viol=0, sharp_x=0, sharp_px=0)
for p in primerange(5, LIM):
    if p % 4 != 1: continue
    for q, lg in LG.items():
        if q >= p or legendre_symbol(q, p) != -1: continue
        o = q - 1; half = o // 2           # -1 has log half; U = even logs
        x = (p + q) // 4
        Bx = box(x, q, lg); lp = lg[p % q]
        Bpx = Bx | {(b + lp) % o for b in Bx} | {(b - lp) % o for b in Bx}
        if half in Bpx: continue
        stats['fail'] += 1
        if q == 7:
            stats['q7'] = stats.get('q7', 0) + 1
            fx7 = factorint(x)
            if p % 7 != 5 or sum(v for s, v in fx7.items() if s % 7 != 1) != 1: stats['q7bad'] = stats.get('q7bad', 0) + 1
        fx = factorint(x)
        for name, B in (('x', Bx), ('px', Bpx)):
            H = stab(B, o)
            ok = all(h % 2 == 0 for h in H)                       # H <= U
            d = (o // 2) // len(H)
            out = sum(v for s, v in fx.items() if lg[s % q] not in H)
            ok &= d >= 3 and 1 <= out <= d - 2
            ok &= all((lg[s % q] - half) % o not in H for s in fx)  # no prime factor in -H
            if name == 'px': ok &= (lg[x % q] - half) % o not in H and (lp - half) % o not in H
            if not ok: stats['viol'] += 1; print('VIOLATION', p, q, name, H, d, out)
            if out == d - 2: stats['sharp_' + name] += 1
print(f'p <= {LIM}, forced q <= {QMAX}:', stats)

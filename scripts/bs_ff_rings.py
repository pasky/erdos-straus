"""Other rings (BRAINSTORM/other_rings.md): positive ES over a real quadratic O_K via units.
If e >> 0 divides 1 + eta (eta a totally positive unit) and e ≡ -n (mod 4 O_K), then
4/n = 1/x + 1/y + 1/z with x = (n+e)/4, y = k n x / eta, z = k n x, k = (1+eta)/e (all >> 0).
We list which classes of (O_K/4)^* are hit by such e (box search), and verify one identity exactly.
usage: bs_ff_rings.py D [J] [B]
"""
import sys, math
from fractions import Fraction

D = int(sys.argv[1]); J = int(sys.argv[2]) if len(sys.argv) > 2 else 12
B = int(sys.argv[3]) if len(sys.argv) > 3 else 60
CASE1 = D % 4 == 1          # omega = (1+sqrt D)/2, omega^2 = omega + (D-1)/4
s = math.sqrt(D)
w1, w2 = ((1 + s) / 2, (1 - s) / 2) if CASE1 else (s, -s)


def mul(x, y):
    a, b = x; c, d = y
    if CASE1:
        return (a * c + b * d * (D - 1) // 4, a * d + b * c + b * d)
    return (a * c + b * d * D, a * d + b * c)


def conj(x):
    a, b = x
    return (a + b, -b) if CASE1 else (a, -b)


def norm(x):
    return mul(x, conj(x))[0]


def emb(x):
    return (x[0] + x[1] * w1, x[0] + x[1] * w2)


def divides(e, m):
    n = norm(e)
    t = mul(m, conj(e))
    return t[0] % n == 0 and t[1] % n == 0, (t[0] // n, t[1] // n)


def totpos(x):
    u, v = emb(x)
    return u > 1e-9 and v > 1e-9


# fundamental unit by brute force
eps = None
for b in range(1, 10 ** 6):
    for a in range(-10 ** 3, 10 ** 3):
        if abs(norm((a, b))) == 1 and emb((a, b))[0] > 1:
            eps = (a, b); break
    if eps:
        break
eta1 = eps if (norm(eps) == 1) else mul(eps, eps)
units = [(1, 0)]
for _ in range(J):
    units.append(mul(units[-1], eta1))


def cls(x):
    return (x[0] % 4, x[1] % 4)


unit_classes = {(a, b) for a in range(4) for b in range(4) if norm((a, b)) % 2 == 1}
hit = {}
for j, eta in enumerate(units):
    M = (eta[0] + 1, eta[1])
    for a in range(-B, B + 1):
        for b in range(-B, B + 1):
            e = (a, b)
            if norm(e) == 0 or not totpos(e) or norm(e) % 2 == 0:
                continue
            ok, k = divides(e, M)
            if ok and cls(e) not in hit:
                hit[cls(e)] = (j, e, k)
print(f"D={D} eps={eps} N(eps)={norm(eps)}; unit classes mod 4: {len(unit_classes)}, hit: {len(hit)}")
missing = sorted(unit_classes - set(hit))
print("  missing classes:", missing)
for c, (j, e, k) in sorted(hit.items()):
    print(f"  class {c}: eta=eta1^{j}, e={e}, kappa={k}")
# exact check of the identity for n = 1 + 4*m rational with e chosen in class -n
for n in (5, 13, 17, 29, 101):
    c = ((-n) % 4, 0)
    if c not in hit:
        print("  n", n, "class not hit"); continue
    j, e, k = hit[c]; eta = units[j]
    x = ((n + e[0]) // 4, e[1] // 4)
    assert (n + e[0]) % 4 == 0 and e[1] % 4 == 0
    nk = mul((n, 0), mul(k, x))
    ok, y = divides(eta, nk)
    z = nk
    def inv(v):  # 1/v as pair of Fractions in basis (1, omega)
        cv = conj(v); nv = norm(v)
        return (Fraction(cv[0], nv), Fraction(cv[1], nv))
    tot = [sum(t) for t in zip(inv(x), inv(y), inv(z))]
    assert ok and tot == [Fraction(4, n), 0] and all(totpos(v) for v in (x, y, z)), (n, x, y, z)
    print(f"  n={n}: x={x}, y={y}, z={z} verified, all totally positive")

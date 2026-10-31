"""z52c_bmL_identity_check.py — exact/floating checks of the algebraic steps of BM_LVALUE.md §2.

(a) f = h * tau exactly (Fractions) for m <= 3000, where f(m) = 1[2|m] 2^omega(m) m/phi(m) and h is the multiplicative
    function of Lemma 2.2 (h(2)=4, h(4)=-4, h(odd)=0; h(l)=2/(l-1), h(l^2)=-(l+1)/(l-1) at odd l).
(b) For several primes p: T(p) (definition, phi(4uB) computed directly) == (sigma/4)(S(p/4) + S_B) (Lemma 2.1),
    S(x) == sum_d h(d)chi(d)/d A(x/d) (Lemma 2.2), and the hyperbola identity (Lemma 2.4) for A(y) at several y.
(c) E(chi) recomputed as the Euler product over l < 10^6 (cross-check of z52c_bmL_Tp.c; err printed).
phi(4uB) = 4 phi(u) phi(B) is asserted for q = 4uB <= 10^5.
Usage: uv run python scripts/z52c_bmL_identity_check.py
"""
from fractions import Fraction as F
from math import gcd, isqrt, log, sqrt
from sympy import factorint, totient, primerange


def omega(m):
    return len(factorint(m))


def h_val(d):
    if d % 2:
        return F(0)
    r = F(1)
    for l, k in factorint(d).items():
        if l == 2:
            r *= {1: F(4), 2: F(-4)}.get(k, F(0))
        else:
            r *= {1: F(2, l - 1), 2: F(-(l + 1), l - 1)}.get(k, F(0))
    return r


def tau(n):
    r = 1
    for k in factorint(n).values():
        r *= k + 1
    return r


# (a)
HV = {d: h_val(d) for d in range(1, 3001)}
for m in range(1, 3001):
    f = F(2**omega(m) * m, totient(m)) if m % 2 == 0 else F(0)
    conv = sum(HV[d] * tau(m // d) for d in range(1, m + 1) if m % d == 0)
    assert f == conv, m
print("(a) f = h*tau exact for m <= 3000: OK")


def legendre_table(p):
    c = [-1] * p
    c[0] = 0
    for i in range(1, p // 2 + 1):
        c[i * i % p] = 1
    return c


for p in [409, 1009, 2729, 10007, 10009, 20011]:
    ch = legendre_table(p)
    chi = lambda n: ch[n % p]
    sig = chi(p - 1)
    N = p // 3 + 3
    phi = list(range(N + 1))
    for i in range(2, N + 1):
        if phi[i] == i:
            for j in range(i, N + 1, i):
                phi[j] -= phi[j] // i
    T = 0.0; SB = 0.0
    u = 1
    while 3 * u - 1 <= p:
        B = 1
        while 4 * u * B - u - B <= p:
            if (u + B) % 2 == 1 and gcd(u, B) == 1:
                q = 4 * u * B
                assert 4 * phi[u] * phi[B] == totient(q) or q > 10**5  # spot check phi(4uB) = 4 phi(u) phi(B)
                T += sig * chi(u * B) / (4 * phi[u] * phi[B])
                if 4 * u * B > p:
                    SB += chi(u) * chi(B) / (phi[u] * phi[B])
            B += 1
        u += 1
    x = p / 4
    S = sum(chi(m) * 2**omega(m) / phi[m] for m in range(2, int(x) + 1, 2))
    assert abs(T - sig / 4 * (S + SB)) < 1e-9, p
    # A(y) by direct double sum, and via hyperbola
    def A_direct(y):
        return sum(chi(a) / a * sum(chi(b) / b for b in range(1, int(y / a) + 1)) for a in range(1, int(y) + 1))
    Gc = [0.0]
    for k in range(1, p * 40):
        Gc.append(Gc[-1] + chi(k) / k)
    G = lambda t: Gc[int(t)]
    Lval = -sum(ch[a] * log(2 * __import__("math").sin(__import__("math").pi * a / p)) for a in range(1, p)) / sqrt(p) if sig == 1 else None
    if Lval is None:
        hneg = -sum(a * ch[a] for a in range(1, p)) / p
        Lval = __import__("math").pi * hneg / sqrt(p)
    for y in [7.3, 50.0, x / 3, x]:
        r = isqrt(int(y))
        hyp = 2 * sum(chi(a) / a * G(y / a) for a in range(1, r + 1)) - G(r) ** 2
        alt = Lval**2 - (Lval - G(r))**2 + 2 * sum(chi(a) / a * (G(y / a) - Lval) for a in range(1, r + 1))
        ad = A_direct(y)
        assert abs(hyp - ad) < 1e-9 and abs(alt - ad) < 1e-9, (p, y)
    S2 = sum(float(HV[d]) * chi(d) / d * A_direct(x / d) for d in range(2, int(x) + 1) if d <= 3000 and HV[d] != 0)
    if int(x) <= 3000:
        assert abs(S - S2) < 1e-9, p
    # (c)
    E_prod = (2 * chi(2) - 1)
    for l in primerange(3, 10**6):
        if l != p:
            c = chi(l)
            E_prod *= 1 + 2 * c / (l * (l - 1)) - c * c * (l + 1) / (l * l * (l - 1))
    print(f"p={p} (σ={sig:+d}): T={T:.6f} = σ/4·(S(p/4)+S_B) [S={S:.6f}, S_B={SB:.6f}]; "
          f"{'S = Σ_d h(d)χ(d)/d·A(x/d) checked; ' if int(x) <= 3000 else ''}hyperbola checked; "
          f"E={E_prod:.6f}, σ·E·L²/4={sig*E_prod*Lval**2/4:.6f}, err={T - sig*E_prod*Lval**2/4:+.6f}")
print("(b),(c) OK")

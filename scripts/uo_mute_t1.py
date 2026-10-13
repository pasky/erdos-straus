"""O186: T1 control for ES^(S) (UNIT_ORBIT_ES.md Lemma 1.1, Cor 1.2).
Box search: x <= y integers in (n/4, XM*n] x [x, YM*n], z = nxy/(4xy - n(x+y)) normalised (denominator = S-unit with
even exponents). For each solution: Hilbert-symbol invariants of alpha = (-x/z, -y/z) at oo, 2, q in S, primes of n;
shape (I/II/other) at each prime of n. usage: uo_mute_t1.py XM YM n... (XM < 0: control run without parity normalisation) (S fixed below)."""
import sys, numpy as np
from fractions import Fraction
S = [3, 5, 7, 11]
XM, YM = float(sys.argv[1]), float(sys.argv[2])
PAR = 1 if XM < 0 else 2  # negative XM: drop the parity normalisation (control)
XM = abs(XM)
def v(N, p):
    k = 0
    while N % p == 0: N //= p; k += 1
    return k, N
def vf(a, p): return v(a.numerator, p)[0] - v(a.denominator, p)[0]
def unitpart(a, p):
    return Fraction(v(a.numerator, p)[1], v(a.denominator, p)[1])
def leg(a, p):  # a integer coprime to p
    return 1 if pow(a % p, (p-1)//2, p) == 1 else -1
def hilbert(a, b, p):  # a, b nonzero Fractions; returns +-1
    if p == 'oo': return -1 if (a < 0 and b < 0) else 1
    al, be = vf(a, p), vf(b, p); u, w = unitpart(a, p), unitpart(b, p)
    if p == 2:
        un = lambda f: (f.numerator * f.denominator) % 8  # same class mod squares of units
        u8, w8 = un(u), un(w)
        eps = lambda t: ((t - 1)//2) % 2; om = lambda t: ((t*t - 1)//8) % 2
        e = eps(u8)*eps(w8) + al*om(w8) + be*om(u8)
        return -1 if e % 2 else 1
    s = (-1)**(al*be * ((p-1)//2))
    t = u**be / w**al
    tt = (t.numerator * pow(t.denominator, -1, p)) % p
    return s * leg(tt, p)
def factors(n):
    out, p = [], 2
    while p*p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0: n //= p
        p += 1
    if n > 1: out.append(n)
    return out
for n in map(int, sys.argv[3:]):
    P = factors(n); sq = int(round(n**0.5))**2 == n
    sols = []
    for x in range(n//4 + 1, int(XM*n) + 1):
        y = np.arange(x, int(YM*n) + 1, dtype=np.int64)
        D = 4*x*y - n*(x + y); m = D > 0; y, D = y[m], D[m]
        N = n*x*y; g = np.gcd(N, D); den = D // g
        r = den.copy()
        for q in S:
            q2 = q**PAR
            for _ in range(30):
                mm = r % q2 == 0; r[mm] //= q2
        for i in np.nonzero(r == 1)[0]:
            sols.append((x, int(y[i]), Fraction(int(N[i]), int(D[i]))))
    stats = {}; badq = 0; badsum = 0
    for (x, y, z) in sols:
        x, y = Fraction(x), Fraction(y)
        assert Fraction(4, n) == 1/x + 1/y + 1/z
        a, b = -x/z, -y/z
        inv = {p: hilbert(a, b, p) for p in ['oo', 2] + S + P}
        if any(inv[q] == -1 for q in S): badq += 1
        prod = 1
        for val in inv.values(): prod *= val
        if prod != 1: badsum += 1
        sh = []
        for p in P:
            k = v(n, p)[0]; vals = [vf(t, p) for t in (x, y, z)]
            big = sum(1 for t in vals if t >= k); unit = sum(1 for t in vals if t == 0)
            sh.append('I' if (big == 1 and unit == 2) else 'II' if (big == 2 and unit == 1) else 'o')
        key = (inv['oo'], tuple(inv[p] for p in P), tuple(sh))
        stats[key] = stats.get(key, 0) + 1
    nonint = sum(1 for s in sols if s[2].denominator > 1)
    print(f"n={n} square={sq} sols={len(sols)} (z non-integral: {nonint}) nonzero inv_q(q in S): {badq} reciprocity failures: {badsum}")
    for k, c in sorted(stats.items(), key=lambda t: -t[1]): print("   inv_oo, inv_(p|n), shapes:", k, c)

"""zc_caseA9.py (O226): fz1_caseA.py restricted to alpha == 0 mod MOD (FF_ODD_ABSENCE Thm 1.4: on the primitive slices of F_9,
E(0)^{2 alpha} = 1 forces 4 | alpha; use MOD = 4 there). Extra argv[4] = MOD (default 1 = no restriction).
Original header: fz1_caseA.py (O220): Case A mass for A = T (k = 1), q = 3^r >= 9, on the slices u0 in F_q^* minus F_3^* (FF_STERILE_SMALL §7).
Data (a1', b1, K) with T^alpha || a1 (WLOG), T not dividing a1' b1 K, E = a1' b1 K - 1, F = (a1 + b1)/E; pattern
(alpha; lam, be, ka), f = alpha - be - ka >= 0, zeta = max(f, be) - lam >= 0; cylinder mass q^{-alpha} (relative to a slice).
Routes (FF_STERILE_SMALL Lemma 7.2):
 (i)   (a1', b1, K)                                   2 N*(lam) N*(be) N*(ka)
 (ii)  (a1', K, F) -> b1 (A4)                         4 N*(lam) N*(ka) N*(f)
 (iii) (b1, K): E | T^alpha + b1^2 K, E == -1 (b1 K)  4 N*(be) N*(ka) clsr(max(alpha, 2be+ka), lam+be+ka, be+ka)
 (iv)  (a1', b1): E | T^alpha a1' + b1, E == -1 (a1' b1)   2 N*(lam) N*(be) clsr(alpha+lam, lam+be+ka, lam+be)
       (factor 2: lc(E) in {1, 2} and the C(n, d) fallback of clsr counts monic divisors only)
 (v)   z, then (b1, K, F) | T^alpha + z               2 (q-1) q^zeta multinomial(alpha; be, ka, f)
 (vi)  (a1', z, K): b1 + F = a1' z, b1 F = (T^alpha + z)/K   4 (q-1) q^zeta N*(lam) N*(ka)
clsr = FF_STERILE_SMALL Lemma 1.4 (q^j cls(n, d, rho + j)), cls = min(trivial, Lenstra 2, Coppersmith m + k, C(n, d)).
Tail alpha > AMAX (Lemma 7.2(b)): count <= (alpha+1)^3 sqrt(8) q^{(alpha+1)/2} 3^{alpha/2}.
usage: fz1_caseA.py r[,r...] [AMAX=40] [exact_file]"""
import sys, math
from fractions import Fraction as Fr
from math import comb, factorial
from functools import lru_cache

def run(q, AMAX, EX=None, MOD=1):
    Ns = lambda d: 1 if d <= 0 else q**d - q**(d - 1)
    @lru_cache(None)
    def cop(n, d, rho):
        X = d - rho; best = None
        for m in range(1, 61):
            for k in range(0, 201 - m):
                if n * m * (m + 1) + X * (m * (m + 1) + 2 * k * m + k * (k + 1)) < 2 * (m + k + 1) * m * d:
                    if best is None or m + k < best: best = m + k
                    break
        return best
    @lru_cache(None)
    def cls(n, d, rho, both):
        if d < rho or (both and n - d < rho): return 1
        c = [comb(n, d)]
        if 3 * rho > n: c.append(2)
        x = cop(n, d, rho) if rho >= 1 else None
        if x: c.append(x)
        if both and rho >= 1:
            x = cop(n, n - d, rho)
            if x: c.append(x)
        return min(c)
    @lru_cache(None)
    def clsr(n, d, rho, both):
        best = comb(n, d)
        for j in range(0, max(0, d - rho + 1) + 1):
            if q**j >= best: break
            best = min(best, q**j * cls(n, d, rho + j, both))
        return best
    tot = Fr(0)
    for al in range(1, AMAX + 1):
        acc = 0
        if al % MOD: continue
        for be in range(0, al + 1):
            for ka in range(0, al - be + 1):
                f = al - be - ka
                for la in range(0, max(f, be) + 1):
                    ze = max(f, be) - la
                    B = [2 * Ns(la) * Ns(be) * Ns(ka), 4 * Ns(la) * Ns(ka) * Ns(f),
                         4 * Ns(be) * Ns(ka) * clsr(max(al, 2 * be + ka), la + be + ka, be + ka, 1),
                         2 * Ns(la) * Ns(be) * clsr(al + la, la + be + ka, la + be, 1),
                         2 * (q - 1) * q**ze * (factorial(al) // (factorial(be) * factorial(ka) * factorial(f))),
                         4 * (q - 1) * q**ze * Ns(la) * Ns(ka)]
                    acc += EX[(al, la, be, ka)] if EX is not None and (al, la, be, ka) in EX else min(B)
        tot += Fr(acc, q**al)
    a0 = AMAX + 1
    rho = ((a0 + 2) / (a0 + 1))**3 * math.sqrt(3 / q)
    tail = float('inf') if rho >= 1 else (a0 + 1)**3 * math.sqrt(8) * q**((1 - a0) / 2) * 3**(a0 / 2) / (1 - rho) * (1 + 1e-9)
    return tot, tail

if __name__ == '__main__':
    AMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 40
    EX = None
    MOD = int(sys.argv[4]) if len(sys.argv) > 4 else 1
    if len(sys.argv) > 3 and sys.argv[3] != '-':   # exact counts from fz1_caseA_enum (filtered): lines "A alpha lam be ka count"; complete levels only
        EX = {}; lev = {}
        for l in open(sys.argv[3]):
            f = l.split(); k = tuple(map(int, f[1:5])); EX[k] = int(f[5]); lev[k[0]] = lev.get(k[0], 0) + 1
        for al, n in lev.items():   # every pattern of a listed level must be present
            need = sum(1 for be in range(al + 1) for ka in range(al - be + 1) for la in range(max(al - be - ka, be) + 1))
            if n != need: sys.exit(f"incomplete Case A level {al}: {n} of {need}")
    for r in [int(x) for x in sys.argv[1].split(',')]:
        q = 3**r; tot, tail = run(q, AMAX, EX, MOD)
        print(f"r={r} q={q} k=1: Case A exact-pattern mass (alpha<={AMAX}) = {float(tot)*(1+1e-12):.10e}  tail <= {tail:.10e}")

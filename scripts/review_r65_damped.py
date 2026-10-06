"""R65 from-scratch checks for sieve-limits-note v5 §14.6.

(1) Lemma 14.16 (damped collisions): random probability sigma on Z/M, M = prod l^E;
    w_l chosen so that |sigma^(theta)|^{2beta} <= prod_{l in supp theta} w_l holds; check
    R_{2+2beta}(sigma) <= E_T R_2(sigma_T) (exact enumeration over T).
    Also check the two-copy identity sum_{supp theta = S}|sigma^|^2 = E prod_{l in S} h_l.
(2) Thm 14.18 examples: for M = 3 mod 4, A = (M+1)/4, the classes -4, -1, -1/4, -4d, -1/(4d)
    (d | A^2) lie in R(M) = {-4D mod M : D | A^2}; and every n in such a class (n>0) has a
    4/n = 1/x+1/y+1/z solution (forcedness), brute force for small n.
"""
import itertools, math
from fractions import Fraction
import numpy as np

rng = np.random.default_rng(6516)


def factor_pp(M):
    out = []; m = M; p = 2
    while p * p <= m:
        if m % p == 0:
            e = 0
            while m % p == 0:
                m //= p; e += 1
            out.append((p, e))
        p += 1
    if m > 1:
        out.append((m, 1))
    return out


def supp(a, M, pps):
    den = M // math.gcd(a, M)
    return frozenset(p for p, _ in pps if den % p == 0)


worst = 0.0; worst_id = 0.0; ntest = 0
for trial in range(400):
    M = int(rng.choice([6, 10, 12, 15, 18, 20, 30, 36, 42, 45, 60, 84, 90]))
    pps = factor_pp(M)
    beta = float(rng.uniform(0.02, 0.5))
    sig = rng.random(M) ** int(rng.integers(1, 6)) * (rng.random(M) < 0.7)
    if sig.sum() == 0:
        sig[0] = 1
    sig /= sig.sum()
    f = np.fft.fft(sig)
    S_of = [supp(a, M, pps) for a in range(M)]
    # two-copy identity
    for r in range(len(pps) + 1):
        for S in itertools.combinations([p for p, _ in pps], r):
            S = frozenset(S)
            lhs = sum(abs(f[a]) ** 2 for a in range(M) if S_of[a] == S)
            rhs = 0.0
            for x in range(M):
                for y in range(M):
                    pr = 1.0
                    for p, e in pps:
                        if p in S:
                            q = p ** e
                            pr *= (q * ((x - y) % q == 0) - 1)
                    rhs += sig[x] * sig[y] * pr
            worst_id = max(worst_id, abs(lhs - rhs))
    # weights: w_l = s^{2beta} with s = max_{theta!=0} |f|^{1/|supp|}, times a random factor >=1 capped at 1
    s = max(abs(f[a]) ** (1 / len(S_of[a])) for a in range(1, M))
    w = {p: min(1.0, s ** (2 * beta) * float(rng.uniform(1, 1.5))) for p, _ in pps}
    ok = all(abs(f[a]) ** (2 * beta) <= np.prod([w[p] for p in S_of[a]]) + 1e-12 for a in range(1, M))
    assert ok
    R = np.sum(np.abs(f) ** (2 + 2 * beta))
    ET = 0.0
    for r in range(len(pps) + 1):
        for T in itertools.combinations(pps, r):
            Tset = {p for p, _ in T}
            pT = np.prod([w[p] if p in Tset else 1 - w[p] for p, _ in pps])
            MT = int(np.prod([p ** e for p, e in T])) if T else 1
            marg = np.zeros(MT)
            for x in range(M):
                marg[x % MT] += sig[x]
            ET += pT * MT * np.sum(marg ** 2)
    worst = max(worst, R / ET); ntest += 1
print(f"(1) two-copy identity max abs err {worst_id:.2e}; damped lemma max ratio {worst:.6f} over {ntest}")
assert worst_id < 1e-9 and worst <= 1 + 1e-9


def has_rep(n):
    # 4/n = 1/x+1/y+1/z, x<=y<=z positive integers
    t = Fraction(4, n)
    for x in range(n // 4 + 1, 3 * n // 4 + 2):
        r1 = t - Fraction(1, x)
        if r1 <= 0:
            continue
        for y in range(max(x, math.floor(1 / r1)), math.floor(2 / r1) + 1):
            r2 = r1 - Fraction(1, y)
            if r2 > 0 and r2.numerator == 1:
                return True
    return False


bad = 0; cnt = 0
for M in range(3, 400, 4):
    A = (M + 1) // 4
    RM = {(-4 * D) % M for D in range(1, A * A + 1) if (A * A) % D == 0}
    inv = lambda a: pow(a, -1, M)
    ex = {(-4) % M, (-1) % M, (-inv(4)) % M}
    for d in range(1, 6):
        if (A * A) % d == 0 and math.gcd(d, M) == 1:
            ex |= {(-4 * d) % M, (-inv(4 * d)) % M}
    assert ex <= RM, (M, ex - RM)
    for b in RM:
        for n in range(b if b > 0 else M, 1200, M):
            cnt += 1
            if not has_rep(n):
                bad += 1
print(f"(2) H-small examples in R(M) for all M<400; forcedness brute force: {cnt} n checked, {bad} failures")
assert bad == 0
print("OK")

"""R28 from-scratch checks for EXCEPTIONAL_KARY3 (independent of the author's scripts).

Checks (EVIDENCE only):
 1. Lemma 2.1: for all y-smooth M <= X: S_y(M) squarefull and log M <= log S_y(M) + Z_y(M) log y.
 2. Lemma 2.2: exact value of sum_{d_1..d_k in P_y} prod Lambda(d_i) Gamma(D)/D, divided by (log y)^k.
 3. ElT (7.10): sum_{a<=A} sum_{m<=B} rho_{ka}(m)/m / (A log B log(1+k)) for many k (incl. squares, huge k).
 4. Shiu step of Lemma 2.3: max_q q*T(q)/(K log^2 K), T(q) = sum_{K<M<=2K, M=3(4), q|M} tau(A_M^2).
 5. Sigma_2 of Lemma 2.3: sum_{K<M<=2K, M=3(4)} tau(A^2) Gamma(M) Z_y(M)^4 / (K log^2 K) for several y.
Usage: PYTHONPATH=scripts uv run --with numpy --with sympy python scripts/review_k3_checks.py [which]
"""
import math
import sys

import numpy as np
from sympy import primerange, jacobi_symbol

W = 16


def gam(p):
    if p == 2:
        return 8.0
    if p <= W:
        return 2 * p / (p - 1)
    return 1 / (1 - p ** -0.5)


def smooth_numbers(y, X):
    ps = list(primerange(2, y + 1))
    out = [1]
    for p in ps:
        new = []
        for m in out:
            q = m * p
            while q <= X:
                new.append(q)
                q *= p
        out += new
    return ps, out


def check1(y, X):
    ps, ms = smooth_numbers(y, X)
    ly = math.log(y)
    bad = 0
    worst = 0.0
    for M in ms:
        logS = 0.0
        Z = 0.0
        sqfull = True
        m = M
        for p in ps:
            if m % p:
                continue
            v = 0
            while m % p == 0:
                m //= p
                v += 1
            # prime powers p^nu <= y dividing M
            nu = 0
            pp = p
            while nu < v and pp <= y:
                Z += math.log(p)
                nu += 1
                pp *= p
            if p ** v > y:
                logS += v * math.log(p)
                if v < 2:
                    sqfull = False
        slack = logS + Z - math.log(M)
        worst = min(worst, slack)
        if slack < -1e-9 or not sqfull:
            bad += 1
    print(f"[1] y={y} X={X:.0e}: {len(ms)} smooth M, violations={bad}, min slack={worst:.3g}")


def check2(ys, kmax=4):
    # exponential formula: total_k = k! [z^k] prod_p (1 + sum_m c_p(m) z^m/m!),
    # c_p(m) = gamma'(p) (log p)^m sum_{nu in N^m} p^{-max nu}
    for y in ys:
        poly = np.zeros(kmax + 1)
        poly[0] = 1.0
        for p in primerange(2, y + 1):
            lp = math.log(p)
            f = np.zeros(kmax + 1)
            f[0] = 1.0
            for m in range(1, kmax + 1):
                # sum_{t>=1} (t^m - (t-1)^m) p^{-t}, truncated where p^{-t} tiny
                s = 0.0
                t = 1
                while True:
                    term = (t ** m - (t - 1) ** m) * float(p) ** (-t)
                    s += term
                    if term < 1e-18 or t > 200:
                        break
                    t += 1
                f[m] = gam(p) * lp ** m * s / math.factorial(m)
            poly = np.convolve(poly, f)[: kmax + 1]
        ly = math.log(y)
        print(f"[2] y={y:.0e}: " + ", ".join(
            f"k={k}: {math.factorial(k) * poly[k] / ly ** k:.3f}" for k in range(1, kmax + 1)))


def rho_ka(ka, m_max):
    """rho_{ka}(m) for m <= m_max via multiplicativity (spf sieve)."""
    spf = np.zeros(m_max + 1, dtype=np.int64)
    rho = np.zeros(m_max + 1)
    rho[1] = 1.0
    for n in range(2, m_max + 1):
        if spf[n] == 0:
            spf[n::n][spf[n::n] == 0] = n
    for n in range(2, m_max + 1):
        p = spf[n]
        m = n
        j = 0
        while m % p == 0:
            m //= p
            j += 1
        if p == 2:
            if ka % 2 == 0:
                r = 0
            elif j == 1:
                r = 1
            elif j == 2:
                r = 2 if ka % 4 == 3 else 0
            else:
                r = 4 if ka % 8 == 7 else 0
        else:
            r = 0 if ka % p == 0 else 1 + jacobi_symbol((-ka) % p, p)
        rho[n] = rho[m] * r
    return rho


def check3(A, B, ks):
    inv = 1.0 / np.arange(1, B + 1)
    # rho depends on ka; cache per value
    spf = None
    for k in ks:
        tot = 0.0
        for a in range(1, A + 1):
            r = rho_ka_fast(k * a, B)
            tot += float(np.dot(r[1:], inv))
        print(f"[3] A={A} B={B} k={k}: ratio to A logB log(1+k) = "
              f"{tot / (A * math.log(B) * math.log(1 + k)):.4f}; ratio to A logB = {tot / (A * math.log(B)):.4f}")


_SPF = {}


def rho_ka_fast(ka, B):
    if B not in _SPF:
        spf = np.zeros(B + 1, dtype=np.int64)
        for n in range(2, B + 1):
            if spf[n] == 0:
                sl = spf[n::n]
                sl[sl == 0] = n
        pw = np.zeros(B + 1, dtype=np.int64)  # exponent of spf
        rest = np.ones(B + 1, dtype=np.int64)
        for n in range(2, B + 1):
            p = spf[n]
            m = n // p
            if m % p == 0:
                pw[n] = pw[m] + 1
                rest[n] = rest[m]
            else:
                pw[n] = 1
                rest[n] = m
        primes = [int(p) for p in range(2, B + 1) if spf[p] == p]
        _SPF[B] = (spf, pw, rest, primes)
    spf, pw, rest, primes = _SPF[B]
    rp = {}
    for p in primes:
        if p == 2:
            continue
        rp[p] = 0 if ka % p == 0 else 1 + jacobi_symbol((-ka) % p, p)
    rho = np.zeros(B + 1)
    rho[1] = 1.0
    for n in range(2, B + 1):
        p = int(spf[n])
        j = int(pw[n])
        if p == 2:
            if ka % 2 == 0:
                r = 0
            elif j == 1:
                r = 1
            elif j == 2:
                r = 2 if ka % 4 == 3 else 0
            else:
                r = 4 if ka % 8 == 7 else 0
        else:
            r = rp[p]
        rho[n] = rho[rest[n]] * r
    return rho


def tau_sq_table(N):
    """tau(A^2) for A <= N."""
    spf = np.zeros(N + 1, dtype=np.int64)
    for n in range(2, int(N ** 0.5) + 1):
        if spf[n] == 0:
            sl = spf[n * n::n]
            sl[sl == 0] = n
    idx = np.arange(N + 1)
    spf[spf == 0] = idx[spf == 0]
    t = np.ones(N + 1, dtype=np.int64)
    pw = np.zeros(N + 1, dtype=np.int64)
    rest = np.ones(N + 1, dtype=np.int64)
    for n in range(2, N + 1):
        p = spf[n]
        m = n // p
        if m % p == 0:
            pw[n] = pw[m] + 1
            rest[n] = rest[m]
        else:
            pw[n] = 1
            rest[n] = m
        t[n] = t[rest[n]] * (2 * pw[n] + 1)
    return t


def check4(K):
    N = (2 * K + 1) // 4 + 1
    tA = tau_sq_table(N)
    M = np.arange(K + 1, 2 * K + 1)
    M = M[M % 4 == 3]
    tw = tA[(M + 1) // 4].astype(float)
    norm = K * math.log(K) ** 2
    best = (0, 0)
    vals = []
    for q in range(1, int(K ** 0.5) + 1, 2):
        T = tw[M % q == 0].sum()
        v = q * T / norm
        vals.append(v)
        if v > best[0]:
            best = (v, q)
    print(f"[4] K={K}: max_q odd<=K^1/2 q T(q)/(K log^2K) = {best[0]:.4f} at q={best[1]}; "
          f"mean = {np.mean(vals):.4f}; q=1 value = {vals[0]:.4f}")


def check5(K, ys):
    N = (2 * K + 1) // 4 + 1
    tA = tau_sq_table(N)
    M = np.arange(K + 1, 2 * K + 1)
    sel = M % 4 == 3
    M = M[sel]
    tw = tA[(M + 1) // 4].astype(float)
    # Gamma(M) via primes dividing M
    G = np.ones(len(M))
    for p in primerange(3, 2 * K + 1):
        idx0 = (-(M[0]) % p)
        if idx0 >= len(M) * 4:
            continue
        hit = M % p == 0 if p < 5000 else None
        if p < 5000:
            G[hit] *= gam(p)
        else:
            break
    # primes >= 5000: contribute gam(p) <= 1.0143 each; at most 3 such factors -> handled crudely by bound
    for y in ys:
        ly = math.log(y)
        Z = np.zeros(len(M))
        for p in primerange(2, y + 1):
            pp = p
            while pp <= y:
                Z[M % pp == 0] += math.log(p)
                pp *= p
        Z /= ly
        s2 = (tw * G * Z ** 4).sum() / (K * math.log(K) ** 2)
        s0 = (tw * G).sum() / (K * math.log(K) ** 2)
        print(f"[5] K={K} y={y}: Sigma2/(K log^2K) = {s2:.4f}  (k=0 analogue {s0:.4f}; G truncated at p<5000, "
              f"true G larger by factor <= 1.015^3)")


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which in ("1", "all"):
        for y in (7, 13, 31):
            check1(y, 10 ** 9)
    if which in ("2", "all"):
        check2([10, 100, 10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6])
    if which in ("3", "all"):
        check3(60, 20000, [1, 4, 9, 12, 100, 4 * 999, 10 ** 6, 4 * 10 ** 9 + 4, 10 ** 15 + 3])
    if which in ("4", "all"):
        check4(2 ** 22)
    if which in ("5", "all"):
        check5(2 ** 21, [3, 5, 11, 31, 101])


def check6(y, X):
    """Block profile b(K) = sum_{K<M<=2K, P(M)<=y, M=3(4)} tau(A^2) / (K log^2 K), K = 2^t, max u^4 b."""
    from sympy import factorint
    _, ms = smooth_numbers(y, X)
    ly = math.log(y)
    blocks = {}
    S = 0.0
    for M in ms:
        if M % 4 != 3:
            continue
        A = (M + 1) // 4
        t = 1
        for e in factorint(A).values():
            t *= 2 * e + 1
        S += t / M
        b = (M - 1).bit_length() - 1  # K = 2^b < M <= 2^{b+1}
        blocks[b] = blocks.get(b, 0) + t
    best = (0, 0)
    for b, s in blocks.items():
        K = 2 ** b
        if 2 * K > X or K < y:
            continue
        u = math.log(K) / ly
        v = u ** 4 * s / (K * math.log(K) ** 2)
        if v > best[0]:
            best = (v, u)
    print(f"[6] y={y} X={X:.0e}: S/(log y)^3 = {S / ly ** 3:.3f}; max u^4 b = {best[0]:.3f} at u={best[1]:.2f}")


if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == "6":
    for y in (7, 13, 23, 31):
        check6(y, 10 ** 12)

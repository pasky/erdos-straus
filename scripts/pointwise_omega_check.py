#!/usr/bin/env python3
"""POINTWISE_OMEGA.md machine checks (EVIDENCE; the theorems do not depend on them).

  local  T nsamp seed : the prime-local reduction (Lemma 2.1).  For y=sqrt(T) and Q_y, draw random
                        n = 1 (mod Q_y) and compare  W(n)>T  (direct, all M<=T, M=3 mod 4, via (58.3))
                        with  "n mod l not in F_l for every prime y<l<=T".  Also re-checks every
                        sampled survivor directly.  Must report 0 mismatches.
  lemma  X            : brute-force check of the algebra in Lemma 2.3 for all M<=X:
                        (i) D -> A^2/D preserves m | 4D+1;  (ii) for D<=A, D=s r^2 (s squarefree),
                        A = s r k with k>=r and m | r+k.
  primes T K          : the first K primes p = 1 (mod Q_y) passing the prime-local sieve (hence W(p)>T),
                        with log p, T/log p, log T/log log p and the actual W(p) (scan to 50*T).
Usage: PYTHONPATH=scripts uv run python scripts/pointwise_omega_check.py local 4095 20000 1
"""
import sys
import random
from math import log, gcd, isqrt
from sympy import isprime, primerange
from pointwise_omega_S import spf_table, factor, divisors_from, residual_system


def Qy(T, y):
    Q = 24
    for l in primerange(2, int(y) + 1):
        e = 1
        while l ** (e + 1) <= T:
            e += 1
        Q = Q * l ** e // gcd(Q, l ** e)
    return Q


def R_tables(Tmax, spf):
    """M -> set R(M) = {-4D mod M : D | A^2}, A=(M+1)/4, all M<=Tmax, M=3 (4)."""
    R = {}
    for M in range(3, Tmax + 1, 4):
        A = (M + 1) // 4
        f = {p: 2 * e for p, e in factor(A, spf).items()}
        R[M] = {(-4 * D) % M for D in divisors_from(f)}
    return R


def W_direct(n, R, Tmax):
    for M in range(3, Tmax + 1, 4):
        if n % M in R[M]:
            return M
    return None  # > Tmax


def cmd_local(T, nsamp, seed):
    y = isqrt(T)
    if y * y < T:
        y += 0  # y = floor(sqrt T); prime-locality needs l > y >= T/l
    spf = spf_table(4 * T + 8)
    F = residual_system(T, y, spf)
    Q = Qy(T, y)
    R = R_tables(T, spf)
    rng = random.Random(seed)
    mism = surv = 0
    for _ in range(nsamp):
        n = 1 + Q * rng.randrange(1, 10 ** 30)
        avoid = all((n % l) not in Fl for l, Fl in F.items())
        wbig = W_direct(n, R, T) is None
        if avoid != wbig:
            mism += 1
        surv += avoid
    # force survivors: sample n residue-wise (CRT) conditioned on avoidance, check directly
    forced_fail = 0
    for _ in range(min(2000, nsamp)):
        n, mod = 1, Q
        for l, Fl in F.items():
            a = rng.randrange(1, l)
            while a in Fl:
                a = rng.randrange(1, l)
            # CRT: n = 1 (Q...), n = a (l)
            t = ((a - n) * pow(mod, -1, l)) % l
            n, mod = n + mod * t, mod * l
        if W_direct(n, R, T) is not None:
            forced_fail += 1
    print(f"local T={T} y={y} log Q_y={log(Q):.2f} #free primes={len(F)} samples={nsamp} "
          f"survivors={surv} mismatches={mism} forced-survivor failures={forced_fail}")


def cmd_lemma(X):
    spf = spf_table(4 * X + 8)
    bad1 = bad2 = cnt = 0
    for M in range(3, X + 1, 4):
        A = (M + 1) // 4
        f = {p: 2 * e for p, e in factor(A, spf).items()}
        Ds = divisors_from(f)
        for m in range(1, M + 1):
            if M % m:
                continue
            for D in Ds:
                if (4 * D + 1) % m:
                    continue
                cnt += 1
                if (4 * (A * A // D) + 1) % m:
                    bad1 += 1
                if D <= A:
                    fd = factor(D, spf) if D > 1 else {}
                    s = 1
                    r = 1
                    for p, e in fd.items():
                        if e % 2:
                            s *= p
                        r *= p ** (e // 2)
                    if A % (s * r):
                        bad2 += 1
                        continue
                    k = A // (s * r)
                    if k < r or (r + k) % m:
                        bad2 += 1
    print(f"lemma X={X}: checked {cnt} (M,m,D) with m|M, D|A^2, m|4D+1; "
          f"involution failures={bad1}; (s,r,k) failures={bad2}")


def cmd_primes(T, K):
    y = isqrt(T)
    spf = spf_table(4 * 50 * T + 8)
    F = residual_system(T, y, spf)
    Q = Qy(T, y)
    R = R_tables(50 * T, spf)
    print(f"primes T={T} y={y} log Q_y={log(Q):.2f}  (class of one: log L*(T) ~ {2*T/3:.0f})")
    found, k = 0, 0
    while found < K:
        k += 1
        p = 1 + k * Q
        if any((p % l) in Fl for l, Fl in F.items()):
            continue
        if not isprime(p):
            continue
        found += 1
        W = W_direct(p, R, 50 * T)
        assert W is None or W > T
        lp = log(p)
        print(f"  k={k} log p={lp:.2f} T/log p={T/lp:.2f} log T/log log p={log(T)/log(lp):.3f} "
              f"W(p)={W if W else '>'+str(50*T)} W/log p={'' if W is None else round(W/lp, 1)}")


if __name__ == "__main__":
    c = sys.argv[1]
    if c == "local":
        cmd_local(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    elif c == "lemma":
        cmd_lemma(int(sys.argv[2]))
    elif c == "primes":
        cmd_primes(int(sys.argv[2]), int(sys.argv[3]))

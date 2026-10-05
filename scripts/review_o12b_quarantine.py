"""R45b from-scratch check of OMEGA12 Lemma 6.2 (pre-quarantine l<=L) at small T.

Independent implementation (does not import the author's scripts).
Atoms (M,D): M<=T, M=3 mod 4, A=(M+1)/4, D | A^2.  g=gcd(M,4D+1).
Graded quarantine: exponents a_l, Q=8*prod l^a_l.  Survive: gcd(M,Q) | 4D+1 and M does not divide Q.
P(E) exact = prod_{l in supp} (l^{-(v-a)} if a>=1 else 1/phi(l^v)).
Checks: (1) P(E) <= e^3 g/M for every surviving atom at every stage (pre-quarantine start);
(2) termination LLL: max_E sum_{l in supp E} w_l <= c;
(3) log Q <= log(840)+theta(L)+(L/c)*sum s_1*h  with s_1=e^3 g/M (Lemma 6.2 cost);
(4) start cost log Q_start <= 1.02L+7.
Usage: review_o12b_quarantine.py T c_inv [start [y]]   start in {pre, o11}; y = pre-quarantine bound (default L;
larger y stress-tests the Euler-factor mechanism, which needs only "a_l>=1 for l<=y", y>=L)
"""
import math, sys
from math import gcd, log

def factor_sieve(n):
    spf = list(range(n + 1))
    for i in range(2, int(n ** 0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf

def fac(m, spf):
    out = {}
    while m > 1:
        p = spf[m]; e = 0
        while m % p == 0:
            m //= p; e += 1
        out[p] = e
    return out

def divisors_from(f):
    ds = [1]
    for p, e in f.items():
        ds = [d * p ** k for d in ds for k in range(e + 1)]
    return ds

def main():
    T = int(sys.argv[1]); cinv = int(sys.argv[2]); start = sys.argv[3] if len(sys.argv) > 3 else "pre"
    y = float(sys.argv[4]) if len(sys.argv) > 4 else None  # pre-quarantine bound (default L)
    c = 1.0 / cinv
    L = log(T)
    spf = factor_sieve(T)
    atoms = []  # (M, fM(dict), D, g, h)
    for M in range(3, T + 1, 4):
        A = (M + 1) // 4
        fA = fac(A, spf) if A > 1 else {}
        fA2 = {p: 2 * e for p, e in fA.items()}
        fM = fac(M, spf)
        h = sum(sum(1.0 / i for i in range(1, v + 1)) for v in fM.values())
        for D in divisors_from(fA2):
            g = gcd(M, 4 * D + 1)
            atoms.append((M, fM, D, g, h))
    primes = [p for p in range(3, T + 1) if spf[p] == p]
    f = {p: int(L // log(p)) for p in primes}
    # guard against float floor issues
    for p in primes:
        while p ** (f[p] + 1) <= T: f[p] += 1
        while f[p] > 0 and p ** f[p] > T: f[p] -= 1
    a = {p: 0 for p in primes}
    for p in (3, 5, 7):
        a[p] = 1
    if start == "pre":
        for p in primes:
            if p <= (L if y is None else y):
                a[p] = 1
    logQ_start = log(8) + sum(a[p] * log(p) for p in primes)
    e3 = math.e ** 3
    worst_ratio = 0.0
    rounds = 0
    while True:
        w = {}
        surv = []
        for (M, fM, D, g, h) in atoms:
            gq = 1
            for p, v in fM.items():
                gq *= p ** min(v, a[p])
            if (4 * D + 1) % gq != 0 or gq == M:
                continue
            P = 1.0
            supp = []
            for p, v in fM.items():
                if v > a[p]:
                    supp.append(p)
                    P *= p ** (-(v - a[p])) if a[p] >= 1 else 1.0 / ((p - 1) * p ** (v - 1))
            if start == "pre":
                worst_ratio = max(worst_ratio, P / (e3 * g / M))
            surv.append((P, supp))
            for p in supp:
                w[p] = w.get(p, 0.0) + P
        viol = [p for p, x in w.items() if a[p] < f[p] and x > c * (a[p] + 1) * log(p) / L]
        if not viol:
            break
        for p in viol:
            a[p] += 1
        rounds += 1
    logQ = log(8) + sum(a[p] * log(p) for p in primes)
    lll = max((sum(w[p] for p in supp) for P, supp in surv), default=0.0)
    S1 = sum(e3 * g / M for (M, fM, D, g, h) in atoms)
    Om1 = sum(e3 * g / M * h for (M, fM, D, g, h) in atoms)
    Stot = sum(P for P, s in surv)
    theta = sum(log(p) for p in range(2, int(L) + 1) if p >= 2 and all(p % q for q in range(2, int(p ** 0.5) + 1)))
    bound = log(840) + theta + (L / c) * Om1
    print(f"T={T} c=1/{cinv} start={start} L={L:.3f} atoms={len(atoms)} surviving={len(surv)} rounds={rounds}")
    print(f"  logQ_start={logQ_start:.2f} (<=1.02L+7={1.02*L+7:.2f}: {logQ_start <= 1.02*L+7}) logQ_final={logQ:.2f}")
    print(f"  max_E sum w = {lll:.5f} <= c={c:.5f}: {lll <= c + 1e-12}")
    print(f"  S_tot={Stot:.3f}  S_1={S1:.2f}  Omega_1={Om1:.2f}  cost bound={bound:.1f}  logQ<=bound: {logQ <= bound}")
    if start == "pre":
        print(f"  max P(E)/(e^3 g/M) over surviving atoms, all stages = {worst_ratio:.5f}  (<=1: {worst_ratio <= 1})")
    print(f"  #primes in Q={sum(1 for p in primes if a[p] > 0)} max exponent={max(a.values())}")

if __name__ == "__main__":
    main()

"""O236 goal 3: window caps for all primes p = 1 (mod 4), p <= N.

Window m (Thm 1.1/1.1'): m = 4 - p (mod 8), every prime factor q of m has q = 3 (mod 4) and (q/p) = -1.
K = (p+m)/4 (odd), b_s = v_s(K).  A shot Q = prod s^{a_s}, Q^2 = -K (mod m) has cap exactly
max_s (a_s - b_s)^+  (Lemma 3.1), so the window cap is
   cap(m) = min{e : -K in {prod s^{2 a_s} : 0 <= a_s <= b_s + e} mod m}.
cap(m) = 0 is an ES (Type II) solution.  Reports, per p: q*(p) (least prime window), cap(q*), least cap over all
windows m <= M0 (prime / all), least window with cap 0 and with cap <= 1.  Every 'verify'-th solution is rebuilt and
checked exactly (Fraction) via z12_selfmute.shot_cap.  Odd squares: counts windows (T1: must be 0).

usage: z12_window_scan.py N M0 [verify]
"""
import sys
from math import gcd, isqrt
from sympy import jacobi_symbol, primerange

from z12_selfmute import shot_cap

N, M0 = int(sys.argv[1]), int(sys.argv[2])
VER = int(sys.argv[3]) if len(sys.argv) > 3 else 0
LIM = (N + M0) // 4 + 2
spf = list(range(LIM + 1))
for i in range(2, isqrt(LIM) + 1):
    if spf[i] == i:
        for j in range(i * i, LIM + 1, i):
            if spf[j] == j:
                spf[j] = i


def fac(k):
    f = {}
    while k > 1:
        s = spf[k]
        f[s] = f.get(s, 0) + 1
        k //= s
    return f


def mfac(m):
    f, d = [], 3
    while d * d <= m:
        if m % d == 0:
            f.append(d)
            while m % d == 0:
                m //= d
        d += 2
    if m > 1:
        f.append(m)
    return f


WIN = []  # (m, primefactors, isprime)
for m in range(3, M0 + 1, 2):
    pf = mfac(m)
    if all(q % 4 == 3 for q in pf):
        WIN.append((m, pf, len(pf) == 1 and pf[0] == m))


def window_cap(p, m, emax):
    """least cap e <= emax at window m, with a witness Q; None if > emax."""
    K = (p + m) // 4
    f = fac(K)
    S = sorted(f)
    target = (-K) % m
    for e in range(emax + 1):
        reach = {1: ()}
        for s in S:
            sq = s * s % m
            new = {}
            for v, ex in reach.items():
                w = v
                for a in range(f[s] + e + 1):
                    if w not in new:
                        new[w] = ex + (a,)
                    w = w * sq % m
            reach = new
        if target in reach:
            Q = 1
            for s, a in zip(S, reach[target]):
                Q *= s ** a
            return e, Q
    return None


def windows_of(p):
    out = []
    for m, pf, isp in WIN:
        if m % 8 == (4 - p) % 8 and gcd(m, p) == 1 and all(jacobi_symbol(q, p) == -1 for q in pf):
            out.append((m, isp))
    return out


if __name__ == "__main__":
    import collections
    H_qstar_cap = collections.Counter()
    H_min_prime = collections.Counter()
    H_min_all = collections.Counter()
    rec_q, rec_cap, nowin = [], [], []
    first0 = collections.Counter()
    cnt = verified = 0
    for p in primerange(5, N + 1):
        if p % 4 != 1:
            continue
        cnt += 1
        W = windows_of(p)
        Wp = [m for m, isp in W if isp]
        if not Wp:
            nowin.append(p)
            continue
        qs = Wp[0]
        r = window_cap(p, qs, qs)
        assert r is not None, (p, qs)  # Thm 1.1 guarantees cap <= qs - 3
        assert r[0] <= qs - 3
        H_qstar_cap[r[0]] += 1
        rec_q.append((qs, p)); rec_q.sort(reverse=True); rec_q = rec_q[:6]
        rec_cap.append((r[0], qs, p)); rec_cap.sort(reverse=True); rec_cap = rec_cap[:6]
        if VER and cnt % VER == 0:
            assert shot_cap(p, qs, r[1]) == r[0]
            verified += 1
        best_p, best_a, f0 = r[0], r[0], None
        for m, isp in W:
            rr = window_cap(p, m, best_a)
            if rr is None:
                continue
            if rr[0] < best_a:
                best_a = rr[0]
            if isp and rr[0] < best_p:
                best_p = rr[0]
            if rr[0] == 0 and f0 is None:
                f0 = m
            if VER and cnt % VER == 0:
                assert shot_cap(p, m, rr[1]) == rr[0]
                verified += 1
        H_min_prime[best_p] += 1
        H_min_all[best_a] += 1
        first0['none<=M0' if f0 is None else ('<=50' if f0 <= 50 else '>50')] += 1
    sq_win = sum(1 for a in range(3, isqrt(N) + 1, 2) if a % 4 in (1, 3) and windows_of(a * a))
    print(f"primes p=1(4) <= {N}: {cnt}; windows m <= {M0}; exact checks: {verified}")
    print("no prime window <= M0:", len(nowin), nowin[:10])
    print("cap at least prime window q*:", sorted(H_qstar_cap.items()))
    print("min cap over prime windows <= M0:", sorted(H_min_prime.items()))
    print("min cap over all windows <= M0:", sorted(H_min_all.items()))
    print("least cap-0 window:", dict(first0))
    print("records q*(p):", rec_q)
    print("records cap at q*:", rec_cap)
    print("odd squares a^2 <= N with any window (T1 => 0):", sq_win)

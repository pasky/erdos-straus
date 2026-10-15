"""R243 from-scratch recomputation of CAP_DOWN §1/§5 numerics.

Lemma-1.1 cap at window m for n: least e such that some K-smooth d ≡ -K (mod m) has
c_2 <= 2 b_2, and for odd s: c_s <= 2 b_s, or c_s even <= 2 b_s + 2e.  (K = (n+m)/4, gcd(m,n)=gcd(K,n)=1.)
Computed by residue-set products mod m (no lists > m entries). Best solutions rebuilt with exact Fractions
and checked against EXPONENT_CAP Def 1.1 directly.
Usage: PYTHONPATH=scripts uv run python scripts/review_r243_caps.py N M EMAX mode   (mode: primes | all | forced)
"""
import sys
from array import array
from fractions import Fraction
from math import gcd, isqrt


def spf_sieve(N):
    spf = array("i", [0]) * (N + 1)
    for i in range(2, N + 1):
        if spf[i] == 0:
            for j in range(i, N + 1, i):
                if spf[j] == 0:
                    spf[j] = i
    return spf


def fac(n, spf):
    f = {}
    while n > 1:
        p = spf[n]
        f[p] = f.get(p, 0) + 1
        n //= p
    return f


def exps(s, b, e):
    if s == 2:
        return list(range(0, 2 * b + 1))
    return list(range(0, 2 * b + 1)) + [c for c in range(2 * b + 2, 2 * b + 2 * e + 1, 2)]


def window_solution(n, m, e, spf):
    """Return a d achieving cap <= e at window m, or None."""
    K = (n + m) // 4
    fK = fac(K, spf)
    target = (-K) % m
    reach = {1 % m: 1}
    for s, b in fK.items():
        new = {}
        for c in exps(s, b, e):
            sc = s ** c
            r = sc % m
            for res, d in reach.items():
                key = res * r % m
                if key not in new:
                    new[key] = d * sc
        reach = new
    return reach.get(target)


def def11_cap(n, x, y, z):
    assert Fraction(4, n) == Fraction(1, x) + Fraction(1, y) + 1 / z
    den = z.denominator
    e = 0
    for l, v in fac_trial(den).items():
        if l == 2 or n % l == 0 or y % l or v % 2:
            return None
        e = max(e, v // 2)
    return e


def fac_trial(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def verify(n, m, d, e):
    K = (n + m) // 4
    A = (K + d) // m
    assert (K + d) % m == 0
    got = def11_cap(n, K, n * A, Fraction(n * K * A, d))
    assert got is not None and got <= e, (n, m, d, e, got)
    return got


def windows(n, M):
    for m in range(3, M + 1, 4) if n % 4 == 1 else range(1, M + 1, 4):
        if gcd(m, n) == 1 and gcd((n + m) // 4, n) == 1:
            yield m


def best_cap(n, M, EMAX, spf):
    """Least cap over windows m <= M (cap <= EMAX), and least window achieving it; also least window for cap 0, cap<=1."""
    wl = list(windows(n, M))
    for e in range(EMAX + 1):
        for m in wl:
            d = window_solution(n, m, e, spf)
            if d is not None:
                got = verify(n, m, d, e)
                return e, m, got
    return None, None, None


def main():
    N, M, EMAX, mode = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    spf = spf_sieve(N + M)
    if mode in ("primes", "all"):
        hist = {}
        worst0 = (0, 0)
        worst1 = (0, 0)
        bad = []
        cnt = 0
        for n in range(5, N + 1, 4):
            f = fac(n, spf)
            if any(p % 4 != 1 for p in f):
                continue
            if mode == "primes" and f != {n: 1}:
                continue
            if isqrt(n) ** 2 == n:
                continue
            cnt += 1
            e, m, got = best_cap(n, M, EMAX, spf)
            hist[e] = hist.get(e, 0) + 1
            if e == 0:
                worst0 = max(worst0, (m, n))
            else:
                bad.append((n, e, m, got))
            # least window with cap <= 1
            for mm in windows(n, M):
                if window_solution(n, mm, 1, spf) is not None:
                    worst1 = max(worst1, (mm, n))
                    break
        print("mode", mode, "N", N, "M", M, "count", cnt)
        print("best-cap histogram", hist)
        print("max least cap-0 window (m, n)", worst0, " max least cap<=1 window", worst1)
        print("non-cap-0 n:", bad[:50], "total", len(bad))
        # odd squares (T1)
        hits = 0
        for a in range(1, isqrt(N) + 1, 2):
            n = a * a
            for m in windows(n, min(M, 400)):
                if window_solution(n, m, 3, spf) is not None:
                    hits += 1
        print("odd squares a^2 <= N: windows m <= 400 with cap <= 3:", hits)


if __name__ == "__main__" and sys.argv[4] != "forced":
    main()


def jac(a, m):
    a %= m
    r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if m % 8 in (3, 5):
                r = -r
        a, m = m, a
        if a % 4 == 3 and m % 4 == 3:
            r = -r
        a %= m
    return r if m == 1 else 0


def ordm(s, q):
    o, t = 1, s % q
    while t != 1:
        t = t * s % q
        o += 1
    return o


def forced_stats(N):
    """Primes p ≡ 1 (4) <= N: q_old (least prime q ≡ 4-p (8), (q/p)=-1), q_new (least Thm-1.2 window),
    excluded-first count, Prop 1.3 caps (min / first-s) and exhaustive least Lemma-1.1 cap at q_new."""
    spf = spf_sieve(N + 2000)
    primes_q = [q for q in range(3, 2000, 4) if spf[q] == q]
    out = {}
    for p in range(5, N + 1, 4):
        if spf[p] != p:
            continue
        r = p % 8
        st = out.setdefault(r, {"cnt": 0, "sold": 0, "snew": 0, "exclfirst": 0, "q3fires_in_excl": 0,
                                "max_qold": (0, 0), "max_qnew": (0, 0), "max_p13min": (0, 0), "max_best": (0, 0)})
        st["cnt"] += 1
        qold = qnew = None
        first = True
        for q in primes_q:
            if jac(q, p) != -1:
                continue
            K = (p + q) // 4
            t = (K & -K).bit_length() - 1
            if first:
                first = False
                if not (q % 8 == 7 or t % 2 == 0):
                    st["exclfirst"] += 1
                    if q == 3:
                        st["q3fires_in_excl"] += window_solution(p, 3, 0, spf) is not None
            if qold is None and K % 2 == 1:
                qold = q
            if qnew is None and (q % 8 == 7 or t % 2 == 0):
                qnew = q
                fK = fac(K, spf)
                caps = [max(0, (ordm(s, q) // 2 - b) // 2) for s, b in fK.items()
                        if s != 2 and b % 2 == 1 and jac(s, q) == -1]
                p13 = min(caps)
                e = 0
                while window_solution(p, q, e, spf) is None:
                    e += 1
                st["max_p13min"] = max(st["max_p13min"], (p13, p))
                st["max_best"] = max(st["max_best"], (e, p))
            if qold is not None and qnew is not None:
                break
        st["sold"] += qold
        st["snew"] += qnew
        st["max_qold"] = max(st["max_qold"], (qold, p))
        st["max_qnew"] = max(st["max_qnew"], (qnew, p))
    for r, st in sorted(out.items()):
        print("p mod 8 =", r, st, "mean qold %.2f qnew %.2f" % (st["sold"] / st["cnt"], st["snew"] / st["cnt"]))


if __name__ == "__main__" and sys.argv[4] == "forced":
    forced_stats(int(sys.argv[1]))

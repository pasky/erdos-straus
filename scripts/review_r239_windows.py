#!/usr/bin/env python3
"""R239 from-scratch check of CAP_POINTWISE (O236) window claims.

Does NOT import any author code.  Usage:
  review_r239_windows.py N MMAX [VERIFY_EVERY]
For every prime p = 1 (mod 4), p <= N:
  * q*(p): least prime q = 4-p (mod 8), (q/p) = -1   (Thm 1.1 conditions)
  * mincap at q*: min e such that -K in {prod s^(2a_s): 0<=a_s<=b_s+e} mod q   (exact search)
  * explicit Thm-1.1 construction (proof's Q) exponent bound e_thm <= q-3
  * best cap over windows m <= MMAX: (A) Thm 1.1' windows, (B) all odd m = 4-p (mod 8), gcd(m,p)=1
  * every solution at q* is rebuilt and checked against EXPONENT_CAP Def 1.1 with exact Fractions
    (den z = square of odd primes, coprime to n, dividing y, v <= e), and the measured e equals the predicted cap.
"""
import sys, math
from fractions import Fraction


def sieve_spf(M):
    spf = list(range(M + 1))
    for i in range(2, int(M ** 0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, M + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf


def jacobi(a, n):
    assert n > 0 and n % 2 == 1
    a %= n
    r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            r = -r
        a %= n
    return r if n == 1 else 0


def factor(k, spf):
    f = {}
    while k > 1:
        s = spf[k]
        f[s] = f.get(s, 0) + 1
        k //= s
    return f


def vval(x, l):
    c = 0
    while x % l == 0:
        x //= l
        c += 1
    return c


def check_def11(n, x, y, z, allowed_primes):
    """Return measured cap e (max over l of v_l(den z)/2) if (x,y,z) is an ES^{(y,e)}(n) solution, else raise."""
    assert x > 0 and y > 0 and z > 0
    assert Fraction(4, n) == Fraction(1, x) + Fraction(1, y) + 1 / z, "not a solution"
    d = z.denominator
    e = 0
    for l in allowed_primes:
        if d % l == 0:
            v = vval(d, l)
            assert v % 2 == 0, "odd valuation"
            assert l != 2 and n % l != 0, "bad prime"
            assert y % l == 0, "denominator prime not dividing y"
            e = max(e, v // 2)
            d //= l ** v
    assert d == 1, "denominator has primes outside allowed set"
    return e


def min_cap(n, m, Kf, emax):
    """min e<=emax with -K in prod_s {s^(2a): 0<=a<=b_s+e} mod m; returns (e, exps) or (None,None)."""
    K = (n + m) // 4
    target = (-K) % m
    S = sorted(s for s in Kf if s != 2)
    for e in range(emax + 1):
        R = {1 % m: ()}
        for s in S:
            hi = Kf[s] + e
            pw = []
            cur = 1 % m
            s2 = (s * s) % m
            seen = set()
            for a in range(hi + 1):
                if cur in seen:
                    break  # periodic; larger a never needed for minimality
                seen.add(cur)
                pw.append((cur, a))
                cur = cur * s2 % m
            NR = {}
            for r, ex in R.items():
                for c, a in pw:
                    t = r * c % m
                    if t not in NR:
                        NR[t] = ex + (a,)
            R = NR
        if target in R:
            return e, dict(zip(S, R[target]))
    return None, None


def build(n, m, exps):
    Q = 1
    for s, a in exps.items():
        Q *= s ** a
    assert (n + 4 * Q * Q) % m == 0
    g = (n + 4 * Q * Q) // m
    x = (n + m) // 4
    y = n * (g + 1) // 4
    assert n * (g + 1) % 4 == 0
    z = 1 / (Fraction(4, n) - Fraction(1, x) - Fraction(1, y))
    return x, y, z


def thm_construction(n, q, Kf):
    """Q exactly as in the proof of Thm 1.1: (-K)^((o+1)/2) written in <S>.  Return max a_s - 1 bound (e_thm)."""
    K = (n + q) // 4
    S = sorted(Kf)
    # discrete-log representation: BFS over exponent vectors with a_s < ord_q(s)
    t = pow(-K % q, 1, q)
    o = 1
    while pow(t, o, q) != 1:
        o += 1
    assert o % 2 == 1
    root = pow(t, (o + 1) // 2, q)
    assert root * root % q == t
    # find representation of root as prod s^a_s, 0<=a_s<ord(s); minimise max a_s
    reach = {1: ()}
    for s in S:
        os_ = 1
        while pow(s, os_, q) != 1:
            os_ += 1
        new = {}
        for r, ex in reach.items():
            c = r
            for a in range(os_):
                if c not in new or max(ex + (a,)) < max(new[c]):
                    new[c] = ex + (a,)
                c = c * s % q
        reach = new
    assert root in reach, "Thm 1.1 group step failed!"
    ex = reach[root]
    return max(0, max(ex) - 1) if ex else 0


def main():
    N = int(sys.argv[1]); MMAX = int(sys.argv[2]); VE = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    spf = sieve_spf(max(N + MMAX, 1000))
    isprime = lambda k: k > 1 and spf[k] == k
    qhist = {}; caphist = {}; bestA = {}; bestB = {}; bestP = {}
    rec_q = (0, 0); rec_ratio = (0, 0, 0); rec_cap = (0, 0, 0); nchk = 0; thm_bad = 0
    cnt = 0
    for p in range(5, N + 1, 4):
        if not isprime(p):
            continue
        cnt += 1
        q = 3 if (4 - p) % 8 == 3 else 7
        while not (isprime(q) and jacobi(q, p) == -1):
            q += 8
        assert q < MMAX
        K = (p + q) // 4
        Kf = factor(K, spf)
        e, ex = min_cap(p, q, Kf, q)
        assert e is not None and e <= q - 3
        eth = thm_construction(p, q, Kf)
        if not (e <= eth <= q - 3):
            thm_bad += 1
        x, y, z = build(p, q, ex)
        em = check_def11(p, x, y, z, sorted(Kf))
        assert em == e, (p, q, em, e)
        nchk += 1
        caphist[e] = caphist.get(e, 0) + 1
        if q > rec_q[0]:
            rec_q = (q, p)
        r = q / math.log(p) ** 2
        if r > rec_ratio[0]:
            rec_ratio = (r, p, q)
        if e > rec_cap[0]:
            rec_cap = (e, p, q)
        # best caps over windows m <= MMAX
        for label, best, allm in (("A", bestA, False), ("B", bestB, True), ("P", bestP, False)):
            found = None
            for ee in range(0, 6):
                for m in range(3 if (4 - p) % 8 == 3 else 7, MMAX + 1, 8):
                    if math.gcd(m, p) != 1:
                        continue
                    if label == "P" and not isprime(m):
                        continue
                    if not allm:
                        mf = factor(m, spf)
                        if any(qi % 4 != 3 or jacobi(qi, p) != -1 for qi in mf):
                            continue
                    Km = (p + m) // 4
                    Kmf = factor(Km, spf)
                    e2, ex2 = min_cap(p, m, Kmf, ee)
                    if e2 is not None:
                        found = e2
                        if cnt % VE == 0:
                            x, y, z = build(p, m, ex2)
                            assert check_def11(p, x, y, z, sorted(Kmf)) == e2
                            nchk += 1
                        break
                if found is not None:
                    break
            best[found] = best.get(found, 0) + 1
    print("primes p=1 mod 4 <=", N, ":", cnt)
    print("record q*:", rec_q, " max q*/log^2 p:", rec_ratio)
    print("mincap at q* histogram:", dict(sorted(caphist.items())), " record:", rec_cap)
    print("Thm-construction bound violations (need mincap <= e_thm <= q-3):", thm_bad)
    print("best cap over Thm1.1' windows m<=%d:" % MMAX, dict(sorted(bestA.items(), key=lambda t: (t[0] is None, t[0] or 0))))
    print("best cap over ALL odd windows m<=%d:" % MMAX, dict(sorted(bestB.items(), key=lambda t: (t[0] is None, t[0] or 0))))
    print("best cap over PRIME Thm1.1 windows q<=%d:" % MMAX, dict(sorted(bestP.items(), key=lambda t: (t[0] is None, t[0] or 0))))
    print("exact Def 1.1 checks:", nchk)


if __name__ == "__main__":
    main()

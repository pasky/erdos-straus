"""R204 from-scratch checks for SIGN_IDENTITY Lemma 1.1, 1.2, 2.1 (cells), Prop 4.1 Gram/Diff.
Independent of scripts/si_*.  Usage: PYTHONPATH=scripts uv run python scripts/review_si_lemmas.py NMAX
"""
import sys
from math import gcd, isqrt
from collections import Counter


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


def factor(n):
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


def words_bruteforce(n):
    """all (t,u,v)>=1 with tuv-u-v=n, by scanning u,v with (u-1)(v-1)<=n+1 directly (no divisor trick)."""
    out = []
    for u in range(1, n + 3):
        for v in range(1, n + 3):
            if (u - 1) * (v - 1) > n + 1:
                break
            s = n + u + v
            if s % (u * v) == 0:
                out.append((s // (u * v), u, v))
    return out


def hilbert(a, b, p):
    """Hilbert symbol (a,b)_p for nonzero integers a,b, p prime (p=2 included)."""
    def split(x):
        k = 0
        while x % p == 0:
            x //= p
            k += 1
        return k, x
    al, au = split(a)
    be, bu = split(b)
    if p != 2:
        s = (-1) ** (al * be * ((p - 1) // 2) % 2)
        s *= jacobi(au % p, p) ** be if True else 1
        s *= jacobi(bu % p, p) ** al
        return s
    eps = lambda x: ((x - 1) // 2) % 2
    om = lambda x: ((x * x - 1) // 8) % 2
    e = (eps(au % 8) * eps(bu % 8) + al * om(bu % 8) + be * om(au % 8)) % 2
    return -1 if e else 1


def main(N):
    tot = 0; mism_chi = 0; mism_bound = 0; maxratio = 0
    diff_mis = 0; gram_mis = 0
    for n in range(1, N + 1, 2):
        W = words_bruteforce(n)
        tot += len(W)
        fac = factor(n)
        # bound |X_n| <= 2 sum_{u<=sqrt(n+1)+1} d(n+u)
        U = isqrt(n + 1) + 1
        bd = 2 * sum(sum(1 for d in range(1, n + u + 1) if (n + u) % d == 0) for u in range(1, U + 1)) if n <= 600 else None
        if bd is not None and len(W) > bd:
            mism_bound += 1
        Ts = set()
        for (t, u, v) in W:
            A, As = t * u - 1, t * v - 1
            assert A * As == t * n + 1 and (n + u) % v == 0 and A == (n + u) // v and As == (n + v) // u
            chi = jacobi(-A, n)
            n0 = 1
            for l, e in fac.items():
                if (u * v) % l:
                    n0 *= l ** e
            if chi != jacobi(-u * v, n0):
                mism_chi += 1
            # prime-sharing claim: l|n, l|u => l|v
            for l in fac:
                if (u % l == 0) != (v % l == 0):
                    mism_chi += 1
            # Prop 4.1: T_w and Diff
            T = (As, 1, A)
            if (T[0], T[2]) != (t * v - 1, t * u - 1) or T[0] * T[2] - 1 != t * n:
                gram_mis += 1
            Ts.add(T)
            a, b = -As, -t * n * As
            ram = set()
            for p in set(factor(abs(a))) | set(factor(abs(b))) | {2}:
                if hilbert(a, b, p) == -1:
                    ram.add(p)
            pred = {l for l, e in fac.items() if jacobi(-A, l) ** e == -1}
            if chi == 1:
                pred.add(2)
            if ram != pred or len(ram) % 2 == 0:
                diff_mis += 1
        if len(Ts) != len(W):
            gram_mis += 1
    print(f"odd n<={N}: words={tot} chi/n0 mismatches={mism_chi} bound violations={mism_bound} "
          f"gram/injectivity mismatches={gram_mis} Diff mismatches={diff_mis}")


def cells():
    c = Counter()
    for t in range(8):
        for u in range(8):
            for v in range(8):
                K = (t * u * v - u - v) % 8
                if K % 2 == 0:
                    continue
                # sample chi on many lifts to test cell-function property
                vals = set()
                for dt in range(0, 48, 8):
                    for du in range(0, 48, 8):
                        for dv in range(0, 48, 8):
                            T, U, V = t + dt or 8, u + du or 8, v + dv or 8
                            n = T * U * V - U - V
                            if n <= 0:
                                continue
                            vals.add(jacobi(-(T * U - 1), n))
                assert len(vals) == 1, (t, u, v, vals)
                c[vals.pop()] += 1
    print("cells mod 8 with K odd:", sum(c.values()), "chi=-1:", c[-1], "chi=+1:", c[1])


def lemma12(N):
    bad = 0
    for n in range(3, N, 2):
        if n % 4 == 3:
            t, u, v = 1, 2, n + 2
        elif n % 8 == 5:
            t, u, v = 1, 3, (n + 3) // 2
        else:
            continue
        if t * u * v - u - v != n or jacobi(-(t * u - 1), n) != -1:
            bad += 1
    # q-certificate
    primes = [p for p in range(3, N) if all(p % d for d in range(2, isqrt(p) + 1))]
    for p in primes:
        if p % 4 != 1:
            continue
        for q in primes:
            if q % 4 == 3 and (p + 1) % q == 0 and q < p:
                t, u, v = 1, q + 1, (p + 1) // q + 1
                if t * u * v - u - v != p or jacobi(-(t * u - 1), p) != -1:
                    bad += 1
    print("Lemma 1.2 certificate failures:", bad)


if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 401
    cells()
    lemma12(20000)
    main(N)

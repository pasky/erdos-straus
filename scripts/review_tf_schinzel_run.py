"""R194 drivers for §5 checks (see review_tf_schinzel.py)."""
import sys, time
from fractions import Fraction as Fr
from review_tf_schinzel import *

mode = sys.argv[1]
if mode == "small":       # all n in [2, 299], m = 8: both solvers
    fails = []
    for n in range(2, 300):
        a = solve_div(8, n)
        if n <= 299:
            b = solve_brute(8, n)
            assert a == b, n
        if not a:
            fails.append(n)
    print("8/n fails, 2<=n<=299:", fails)
    for n in (127, 239, 131, 241):
        print(" 8 /", n, len(solve_div(8, n)), "| 4 /", n, len(solve_div(4, n)))
elif mode == "primes":    # odd primes up to X, m = 8: first-solution search (complete when it fails)
    X = int(sys.argv[2]); fails = []
    t0 = time.time()
    sieve = bytearray([1]) * (X + 1); sieve[0] = sieve[1] = 0
    for i in range(2, int(X ** .5) + 1):
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
    for p in range(3, X + 1, 2):
        if sieve[p] and not solve_div(8, p, first_only=True):
            fails.append(p)
    print("8/p fails, odd primes <= %d:" % X, fails, "%.0fs" % (time.time() - t0))
elif mode == "squares":   # odd squares k^2 <= X solvable; Type I/II count at q^2
    X = int(sys.argv[2])
    uns = [k for k in range(3, int(X ** .5) + 1, 2) if not solve_div(8, k * k, first_only=True)]
    print("unsolvable odd squares k^2 <=", X, ":", uns)
elif mode == "t1":        # n = q^2, q prime <= Q; BL Lemma 3.9 shapes; Hilbert reciprocity check
    m, Q = int(sys.argv[2]), int(sys.argv[3])
    tot = t1 = t2 = 0
    for q in range(3, Q + 1, 2):
        if not is_prime(q) or m % q == 0:
            continue
        n = q * q
        for u in solve_div(m, n):
            tot += 1
            for i in range(3):
                a, b, c = u[i], u[(i + 1) % 3], u[(i + 2) % 3]
                if a % n == 0 and b % q and c % q:
                    t1 += 1; break
                if a % q and b % n == 0 and c % n == 0:
                    t2 += 1; break
    print(f"m={m}, n=q^2, q<={Q}: {tot} solutions, Type I {t1}, Type II {t2}")
elif mode == "hilb":      # Prop 5.1 law on all solutions of 8/n, + full reciprocity as symbol test
    for n in map(int, sys.argv[2:]):
        cnt = 0
        for u in solve_div(8, n):
            P = primes_of(*u) | set(factor_int(n)) | {2}
            inv = {p: alpha(u, p) for p in P}
            inf = alpha(u, 0)
            prod_all = inf
            for v in inv.values():
                prod_all *= v
            assert prod_all == 1, ("reciprocity", n, u)
            pn = 1
            for p in factor_int(n):
                pn *= inv[p]
            assert pn == -1 and inv[2] == 1 and inf == -1, (n, u)
            assert all(inv[p] == 1 for p in P if n % p and p != 2), (n, u)
            cnt += 1
        print(f"8/{n}: {cnt} solutions: prod_(p|n) = -1, inv_2 = +1, inv_inf = -1, inv_p = +1 (p ∤ 2n): OK")
elif mode == "cert":      # Thm 5.3 certificates: P0 = (x, y) > 0 with z0 > 0, T(P0) = {q}; P1 q-integral, same inv_q
    def bad(u, n):
        # places p where u not in U(Z_p): some coordinate non-integral
        return sorted(p for p in primes_of(*u) if any(Fr(t).denominator % p == 0 for t in u))
    def chk(n, P0, P1):
        x, y = P0
        z0 = 1 / (Fr(8, n) - Fr(1, x) - Fr(1, y))
        u0 = (x, y, z0)
        assert all(Fr(t) > 0 for t in u0)
        T = bad(u0, n)
        assert len(T) == 1, T
        q = T[0]
        assert Fr(8, n) == sum(1 / Fr(t) for t in P1)
        assert all(Fr(t).denominator % q for t in P1)
        a0, a1 = alpha(u0, q), alpha(P1, q)
        print(f"n={n}: P0={u0} T={T} inv_q(P0)={a0}  P1={P1} inv_q(P1)={a1}  {'OK' if a0 == a1 else 'FAIL'}")
        return a0 == a1
    assert chk(131, (23, 57), (30, 36, -23580))
    assert chk(241, (36, 185), (36, 180, -7230))
    # own search for 3, 11, 17 (and re-search 131, 241): P0 from small positive (x, y), P1 from small integer points
    for n in (3, 11, 17, 131, 241):
        found = None
        for x in range(1, 400):
            for y in range(x, 400):
                r = Fr(8, n) - Fr(1, x) - Fr(1, y)
                if r <= 0:
                    continue
                u0 = (x, y, 1 / r); T = bad(u0, n)
                if len(T) != 1:
                    continue
                q = T[0]; a0 = alpha(u0, q)
                # q-integral P1 (any signs): x1, y1 in small range, z1 = 1/(8/n - 1/x1 - 1/y1)
                for x1 in range(-60, 61):
                    for y1 in range(-60, 61):
                        if x1 == 0 or y1 == 0:
                            continue
                        r1 = Fr(8, n) - Fr(1, x1) - Fr(1, y1)
                        if r1 == 0:
                            continue
                        P1 = (x1, y1, 1 / r1)
                        if all(Fr(t).denominator % q for t in P1) and alpha(P1, q) == a0:
                            found = (u0, q, P1); break
                    if found: break
                if found: break
            if found: break
        print(f"n={n}: own certificate", found)
        assert found

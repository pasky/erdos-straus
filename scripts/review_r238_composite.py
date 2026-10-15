"""R238 from-scratch: Thm 1.1 for composite n, Thm 1.1' composite windows, Cor 1.2(c) odd squares, T1 check.

usage: review_r238_composite.py N
(1) every odd non-square n = 1 (4) <= N, all primes = 1 (4) [case (b)] AND also n with primes = 3 (4) (Thm 1.1 as
    stated only needs n = 1 (4) non-square): least prime window q; cap via dict BFS (worst-case full group);
    solution built from the equation and checked against Def 1.1; check e <= q-3.
(2) every Thm 1.1' composite window m <= 300 for n <= N/10: firing (-K in <S>^2 mod m) and e <= lambda(m)-2.
(3) odd squares a^2 <= N: no window (q/a^2) = -1 exists; Cor 1.2(c) solution via p | a scaled by k = a^2/p, checked.
"""
import sys
from math import gcd, lcm
from review_r238_core import factor, is_prime, jacobi, def11_cap, solution_from_Q


def carmichael(m):
    L = 1
    for q, k in factor(m).items():
        L = lcm(L, (q - 1) * q ** (k - 1))  # odd q only
    return L


def min_cap_Q(n, m, emax):
    """min e<=emax with -K in {prod s^{2a}, a<=b_s+e} mod m; returns (e, Q) or (None, None)."""
    K = (n + m) // 4
    fk = factor(K)
    for e in range(emax + 1):
        D = {1 % m: 1}
        for s, b in fk.items():
            s2 = s * s % m
            D2 = {}
            for r, Q in D.items():
                rr, QQ = r, Q
                for a in range(b + e + 1):
                    D2.setdefault(rr, QQ)
                    rr = rr * s2 % m
                    QQ *= s
            D = D2
        Q = D.get((-K) % m)
        if Q is not None:
            return e, Q
    return None, None


def main():
    N = int(sys.argv[1])
    primes = [q for q in range(3, 5000) if is_prime(q)]
    cnt = bad = 0
    worst = (0, 0, 0)
    for n in range(5, N + 1, 4):
        r = int(n ** 0.5)
        if r * r == n:
            continue
        q = next(q for q in primes if q % 8 == (4 - n) % 8 and n % q and jacobi(q, n) == -1)
        e, Q = min_cap_Q(n, q, q)
        if e is None:
            print("NO FIRING", n, q); bad += 1; continue
        x, y, z = solution_from_Q(n, q, Q)
        ee = def11_cap(n, x, y, z)
        cnt += 1
        if ee != e or e > max(0, q - 3):
            print("BAD", n, q, e, ee); bad += 1
        worst = max(worst, (e, n, q))
    print(f"(1) non-squares n=1(4)<={N}: {cnt} exact checks, bad={bad}, worst cap at least window {worst}")
    cnt = bad = 0
    for n in range(5, N // 10 + 1, 4):
        r = int(n ** 0.5)
        if r * r == n:
            continue
        for m in range(3, 301, 2):
            if is_prime(m) or m % 8 != (4 - n) % 8 or gcd(m, n) != 1:
                continue
            f = factor(m)
            if not all(qq % 4 == 3 and jacobi(qq, n) == -1 for qq in f):
                continue
            lam = carmichael(m)
            e, Q = min_cap_Q(n, m, lam)
            if e is None or e > max(0, lam - 2):
                print("THM1.1' FAIL", n, m, e); bad += 1; continue
            x, y, z = solution_from_Q(n, m, Q)
            if def11_cap(n, x, y, z) != e:
                print("BAD'", n, m); bad += 1
            cnt += 1
    print(f"(2) Thm 1.1' composite windows m<=300, n<={N//10}: {cnt} exact checks, bad={bad}")
    cnt = bad = wins = 0
    for a in range(3, int(N ** 0.5) + 1, 2):
        n = a * a
        fa = factor(a)
        wins += sum(1 for q in primes[:200] if n % q and q % 8 == (4 - n) % 8 and jacobi(q, n) == -1)
        if any(l % 4 == 3 for l in fa):
            continue
        p = min(fa)
        k = n // p
        q = next(q for q in primes if q % 8 == (4 - p) % 8 and jacobi(q, p) == -1
                 and all((q + p) % l for l in fa if l != p))
        e, Q = min_cap_Q(p, q, q)
        x, y, z = solution_from_Q(p, q, Q)
        ee = def11_cap(n, k * x, k * y, k * z)
        cnt += 1
        if ee != e:
            print("BAD sq", a, p, q, e, ee); bad += 1
    print(f"(3) odd squares a^2<={N}: windows found {wins} (expect 0); Cor1.2(c) exact checks {cnt}, bad={bad}")


if __name__ == "__main__":
    main()

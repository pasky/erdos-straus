"""R238 from-scratch: best square-shot window cap over windows m <= M for primes p = 1 (4) <= N.

usage: review_r238_best.py N M
Window m: m = 4-p (mod 8), gcd(m,p)=1, K=(p+m)/4. cap(m) = min e with -K = Q^2 (mod m), Q = prod_{s|K} s^{a_s},
a_s <= v_s(K)+e. Three window families: prime m; Thm 1.1' m (all prime factors = 3 (4) with (q_i/p) = -1);
all m. Every reported minimum's witness is built and checked exactly against Def 1.1.
"""
import sys
from collections import Counter
from review_r238_core import factor, is_prime, jacobi, def11_cap, solution_from_Q

EMAX = 8


def witness(p, m, e):
    K = (p + m) // 4
    fk = factor(K)
    D = {1 % m: 1}
    for s, b in fk.items():
        s2 = s * s % m
        D2 = {}
        for r, Q in D.items():
            rr, QQ = r, Q
            for a in range(b + e + 1):
                if rr not in D2:
                    D2[rr] = QQ
                rr = rr * s2 % m
                QQ *= s
        D = D2
    return D.get((-K) % m)


def main():
    N, M = int(sys.argv[1]), int(sys.argv[2])
    fam = {}  # m -> (is_prime, is_thm11prime_shape)
    for m in range(3, M + 1, 2):
        f = factor(m)
        fam[m] = (is_prime(m), all(q % 4 == 3 for q in f))
    H = {k: Counter() for k in ("prime", "thm11p", "all")}
    worst = {k: (0, 0, 0) for k in H}
    nchk = bad = 0
    for p in range(5, N + 1, 4):
        if not is_prime(p):
            continue
        wins = [m for m in fam if m % 8 == (4 - p) % 8 and m % p]
        best = {}
        for e in range(EMAX + 1):
            for m in wins:
                isp, sh = fam[m]
                kinds = ["all"]
                if sh and all(jacobi(q, p) == -1 for q in factor(m)):
                    kinds.append("thm11p")
                    if isp:
                        kinds.append("prime")
                need = [k for k in kinds if k not in best]
                if not need:
                    continue
                Q = witness(p, m, e)
                if Q is None:
                    continue
                x, y, z = solution_from_Q(p, m, Q)
                ee = def11_cap(p, x, y, z)
                nchk += 1
                if ee is None or ee > e:
                    bad += 1
                    print("BAD", p, m, e, Q, ee)
                for k in need:
                    best[k] = (e, m)
            if len(best) == 3:
                break
        for k in H:
            e, m = best.get(k, (None, None))
            H[k][e] += 1
            if e is not None and e > worst[k][0]:
                worst[k] = (e, p, m)
    print(f"N={N} M={M} exact checks={nchk} bad={bad}")
    for k in H:
        print(k, sorted(H[k].items(), key=lambda t: (t[0] is None, t[0] or 0)), "worst", worst[k])


if __name__ == "__main__":
    main()

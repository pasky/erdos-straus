"""bsE_qpow_complete.py (O178, R-fix): complete re-check of the primes reported "both-empty" by bsE_qpow.c, whose Type I
loop was truncated at t <= n+2 (that cutoff is only valid for the a = 1 slice). Here t = q^s runs to the complete bound
t <= 9n^2/4 + 1 (ET Lemma 2.8, as cited by the O178 review) and e = q^s to e <= n (Type II needs e <= (n+4)/3 anyway).
Every found solution is rebuilt and checked exactly.  usage: uv run --with sympy python scripts/bsE_qpow_complete.py q failfile"""
import sys, re
from fractions import Fraction as Fr
from sympy import divisors

def has_solution(n, q):
    t = 1
    while 4 * t <= 9 * n * n + 4:
        if (t * n + 1) % 4 == 0:
            M = (t * n + 1) // 4
            for a in divisors(M):
                for b in divisors(M // a):
                    if (a + b) % t == 0:
                        d = M // (a * b); c = (a + b) // t
                        assert Fr(4, n) == Fr(1, a*b*d*n) + Fr(1, a*c*d) + Fr(1, b*c*d)
                        return ("I", t, a, b)
        t *= q
    e = 1
    while e <= n:
        if (n + e) % 4 == 0:
            M = (n + e) // 4
            for a in divisors(M):
                for b in divisors(M // a):
                    if (a + b) % e == 0:
                        return ("II", e, a, b)
        e *= q
    return None

if __name__ == "__main__":
    q = int(sys.argv[1]); ns = [int(m) for m in re.findall(r"n=(\d+)", open(sys.argv[2]).read())]
    rescued = {}
    for n in ns:
        r = has_solution(n, q)
        if r: rescued[n] = r
    still = [n for n in ns if n not in rescued]
    print("q=%d: %d reported empty, %d rescued by t > n+2, %d still empty (first: %s)" % (q, len(ns), len(rescued), len(still), still[:12]))
    for n in list(rescued)[:5]: print("  rescued", n, rescued[n])

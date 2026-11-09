"""NL7: search for explicit failures of polynomial-divisor rules along p = t^2 + beta, restricted to the
"H-shaped" sub-family t = c0 * q (q prime) where the theorem predicts failures.
usage: hsearch.py FAMILY RULE c0 Q0 Q1 out
FAMILY: t2p1 (beta = 1; data a=1, b=t, Pell (t,1))   |  fixb:B (beta = B^2; data a=t, b=B)
For each prime q in [Q0,Q1) with p = (c0 q)^2 + beta prime: candidate letters = divisors of the rule expressions;
report t where NO U7 word has a letter dividing any expression (every candidate letter is tested as x, y and z
by full factorisation of p + L and L p + 1).
"""
import sys
sys.path.insert(0, 'scripts')
from z69_nl7_lib import *
from z69_nl7_polyrule import RULES
from sympy import divisors, isprime, primerange

def main(fam, rule, c0, Q0, Q1, out):
    E = RULES[rule]
    B = 1 if fam == 't2p1' else int(fam.split(':')[1])
    nprime = nfail = 0
    hist = {}
    fh = open(out, 'w')
    fh.write(f"# family {fam} rule {rule} t = {c0}*q, q prime in [{Q0},{Q1})\n# FAIL lines: t p #letters least_letter_overall(<=60 or -1)\n")
    for q in primerange(Q0, Q1):
        t = c0 * q
        p = t * t + B * B
        if p % 8 != 1 or not isprime(p):
            continue
        nprime += 1
        letters = set()
        for e in E(t, B):
            if e > 0:
                letters |= {d for d in divisors(e) if d <= p + 2}
        ok = None
        for L in sorted(letters):
            if words_with_letter(p, L):
                ok = L
                break
        key = ok if (ok is None or ok <= 60) else 'big'
        hist[key] = hist.get(key, 0) + 1
        if ok is None:
            nfail += 1
            m = -1
            for L in range(1, 61):
                if words_with_letter(p, L):
                    m = L; break
            fh.write(f"FAIL {t} {p} {len(letters)} {m}\n"); fh.flush()
    fh.write(f"# primes {nprime} failures {nfail}\n# histogram of least successful candidate letter: {sorted(hist.items(), key=lambda kv: str(kv[0]))}\n")
    fh.close()
    print(f"{fam} {rule} c0={c0} q in [{Q0},{Q1}): primes {nprime}, failures {nfail}, hist {sorted(hist.items(), key=lambda kv: str(kv[0]))}")

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6])

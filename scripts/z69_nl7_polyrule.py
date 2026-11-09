"""NL7: finite polynomial-divisor rules along a quadratic prime curve p = P(t).
Rule R_E: "p has a U7 word with a letter dividing some E_i(t)".
usage: polyrule.py FAMILY RULE T0 T1 [out]
FAMILY: t2p1 (p=t^2+1, t≡0 mod 4)  |  fixb:B (p=t^2+B^2, t odd)
RULE:   name in RULES below (polynomials in t given as python lambdas)
"""
import sys
sys.path.insert(0, 'scripts')
from z69_nl7_lib import *
from sympy import divisors, isprime

RULES = {
 # on t2p1: (a,b)=(1,t); Pell (t,1); Bezout A=t, g=1.  on fixb: a=t, b=B.
 'G':   lambda t, B: [t, B, t + B, abs(t - B)],                         # z68 R-G: a, b, a±b
 'G2':  lambda t, B: [t, B, t + B, abs(t - B), t*t + 2*B*B, 2*t*t + B*B, t*B + 1, abs(t*B - 1),
                      t*t + 2, t*t + 3, B*B + 2, t + 2*B, abs(t - 2*B), 2*t + B, abs(2*t - B)],
 'Pm':  lambda t, B: [t + 1, t - 1],                                   # Pell T±1 (S = 1) on t^2+1; = a±b there
 'P':   lambda t, B: [t, t + 1, t - 1, t + 2, t - 2, t + 3, t - 3, 2*t*t + 1, 2*t],   # Pell t±c, positive Pell (2t^2+1, 2t)
}

def run(fam, rule, T0, T1, out=None):
    E = RULES[rule]
    if fam == 't2p1':
        B = 1; ts = range(T0 + (-T0) % 4, T1, 4)
    else:
        B = int(fam.split(':')[1]); ts = range(T0 | 1, T1, 2)
    nprime = nfail = 0
    fails = []
    for t in ts:
        p = t * t + B * B
        if p % 8 != 1 or not isprime(p):
            continue
        nprime += 1
        letters = set()
        for e in E(t, B):
            if e > 0:
                letters |= {d for d in divisors(e) if d <= p + 2}
        ok = False
        for L in sorted(letters):
            if words_with_letter(p, L):
                ok = True
                break
        if not ok:
            nfail += 1
            fails.append((t, p, len(letters)))
    print(f"family {fam} rule {rule} t in [{T0},{T1}): primes {nprime}, rule failures {nfail}")
    for f in fails[:40]:
        print("  FAIL t=%d p=%d #letters=%d" % f)
    if out:
        with open(out, 'w') as fh:
            fh.write(f"# family {fam} rule {rule} t in [{T0},{T1}): primes p=P(t)≡1 (8): {nprime}, rule failures: {nfail}\n# t p #candidate_letters\n")
            for f in fails:
                fh.write("%d %d %d\n" % f)

if __name__ == '__main__':
    run(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5] if len(sys.argv) > 5 else None)

"""NL7 Theorem NL-W illustration: witness rules "some U7 witness f (f ≡ 7 mod 8, (-p mod f) | f+1) divides E(t)".
families: fixb:B (p = t^2 + B^2, t = c0*q), t2p1 (p = t^2+1, t = c0*q);  E(t) = product of the rule expressions.
usage: witness.py FAMILY RULE c0 Q0 Q1 out
"""
import sys
sys.path.insert(0, 'scripts')
from sympy import factorint, isprime, primerange
from z69_nl7_polyrule import RULES

def divisors_from(fac):
    ds = [1]
    for p, e in fac.items():
        ds = [d * p**i for d in ds for i in range(e + 1)]
    return ds

def main(fam, rule, c0, Q0, Q1, out):
    B = 1 if fam == 't2p1' else int(fam.split(':')[1])
    nprime = nfail = nskip = 0
    fails = []
    for q in primerange(Q0, Q1):
        t = c0 * q
        p = t * t + B * B
        if p % 8 != 1 or not isprime(p):
            continue
        nprime += 1
        fac = {}
        for e in RULES[rule](t, B):
            if e > 0:
                for pr, ex in factorint(e).items():
                    fac[pr] = fac.get(pr, 0) + ex
        wit = None
        ndiv = 1
        for ex in fac.values():
            ndiv *= ex + 1
        if ndiv > 200000:      # memory guard: skip (counted separately), never build huge divisor lists
            nskip += 1
            continue
        for f in divisors_from(fac):
            if f % 8 == 7:
                r = (-p) % f
                if r > 0 and (f + 1) % r == 0:
                    wit = f; break
        if wit is None:
            nfail += 1
            fails.append((t, p))
    with open(out, 'w') as fh:
        fh.write(f"# witness rule: family {fam} rule {rule} (f | product of the expressions), t = {c0}*q, q prime in [{Q0},{Q1})\n")
        fh.write(f"# primes {nprime} (skipped for > 2e5 divisors: {nskip}), primes with NO witness f dividing E(t): {nfail}\n# first failures (t p):\n")
        for t, p in fails[:50]:
            fh.write(f"{t} {p}\n")
    print(f"witness rule {fam} {rule} c0={c0} q in [{Q0},{Q1}): primes {nprime}, skipped {nskip}, no-witness failures {nfail}; first {fails[:3]}")

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6])

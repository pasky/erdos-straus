# z58 DISPROOF §3: local profile of the known zeros vs controls.
# For each n: n mod 840, is n a square mod 840 (any square, not nec. unit), n mod 8, the "square depth"
#   sd(n) := least odd prime l such that n is a quadratic NON-residue mod l (Legendre/(n mod l) = -1; l | n counts as square),
#   and for composites the factorisation.  Controls: all primes p = 1 (4) in matching ranges (sd distribution), and all
#   composites n = 1 (4) <= 8e6 that are not squares.
# Run: uv run --with sympy python scripts/z58_disproof_profile.py > data/z58/disproof/profile.txt
import sys, collections
from sympy import factorint, isprime, primerange
SQ840 = {(x * x) % 840 for x in range(840)}
OP = list(primerange(3, 400))
def sd(n):
    for l in OP:
        r = n % l
        if r and pow(r, (l - 1) // 2, l) == l - 1: return l
    return 999
def load(fn, col=0):
    out = []
    for line in open(fn):
        if line.startswith('#') or not line.strip(): continue
        out.append(int(line.split()[col]))
    return out
S = 'data/z58/screens/'
star = load(S + 'star_prime_zeros.txt'); gst = load(S + 'gstar_zeros.txt'); r8 = load(S + 'r8_zeros_1e10.txt')
comp = load(S + 'composite_zeros_le8e6.txt')
def row(n):
    return f"{n} mod840={n%840} sq840={int(n%840 in SQ840)} mod8={n%8} sd={sd(n)}"
print("# (★)-zeros"); [print(row(p)) for p in star]
print("# G*-zeros not (★)-zeros"); [print(row(p)) for p in gst if p not in star]
print("# R8 zeros in [1e10,1.1e10]"); [print(row(p)) for p in r8]
# distributions
def dist(xs):
    c = collections.Counter(sd(x) for x in xs); n = len(xs)
    return ' '.join(f"{k}:{c[k]/n:.3f}" for k in sorted(c)[:12]), sum(x % 840 in SQ840 for x in xs) / n, sum(x % 8 == 1 for x in xs) / n
print("\n# distribution of sd (least odd prime non-residue), share square mod 840, share = 1 mod 8")
for name, xs in [("star14", star), ("gstar38", gst), ("r8_12", r8)]:
    print(name, *dist(xs))
ctrl = [p for p in range(5, 9_000_000, 4) if isprime(p)]
print("ctrl primes 1(4) <= 9e6", *dist(ctrl))
print("comp285", *dist(comp))
cc = [n for n in range(5, 8_000_000, 4) if not isprime(n) and int(n ** 0.5 + 0.5) ** 2 != n]
print("ctrl nonsq composites 1(4) <= 8e6", *dist(cc))
# composites: factor structure
print("\n# composite zeros: omega, smallest prime factor, factorisations of the first 40, share with all prime factors = 1 (4)")
om = collections.Counter(); spf = collections.Counter(); all1 = 0; sqf = 0
for n in comp:
    f = factorint(n); om[len(f)] += 1; spf[min(f)] += 1
    all1 += all(q % 4 == 1 for q in f); sqf += all(e == 1 for e in f.values())
print("omega", dict(sorted(om.items())), "spf(top)", spf.most_common(8), "all factors 1(4):", all1, "squarefree:", sqf, "of", len(comp))
print(' '.join(f"{n}={'.'.join(f'{q}^{e}' if e > 1 else str(q) for q, e in sorted(factorint(n).items()))}" for n in comp[:40]))
# class of composite zeros by (n mod 3)
print("comp zeros n mod 3:", collections.Counter(n % 3 for n in comp), " n mod 5:", collections.Counter(n % 5 for n in comp), " n mod 7:", collections.Counter(n % 7 for n in comp))

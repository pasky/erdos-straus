"""Z2835: test 'Theorem 1(b)' — on the Mordell-curve fibres 4k + n^3 = s^2 the class A = (-q,-d) is unramified;
claimed obstruction: n ≡ 5 (8), gcd(n,k) = 1, (n/l) = 1 for odd l | k, (-n/l) = 1 for l | s, l ∤ k  =>  S_{n,k}(N) = ∅.
Generates all (n,k) with n odd, 9 <= n <= NMAX, s odd, k = (s^2 - n^3)/4 in [1, KMAX], runs the complete search
(z52d_p2_ZF1_Z2835_pencilk), and tabulates FAIL vs the hypothesis (also n ≡ 1 (8), k even, for exploration)."""
import sys, subprocess
from math import isqrt, gcd
from sympy import factorint, jacobi_symbol
NMAX, KMAX, BIN = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
pairs = []
for n in range(9, NMAX + 1, 2):
    s = isqrt(n ** 3) + 1
    while True:
        if s % 2 == 1 and (s * s - n ** 3) % 4 == 0:
            k = (s * s - n ** 3) // 4
            if k > KMAX: break
            if k >= 1: pairs.append((n, k, s))
        elif (s * s - n ** 3) // 4 > KMAX: break
        s += 1
def hyp(n, k, s):
    if n % 8 != 5 or gcd(n, k) != 1: return False
    for l in factorint(k):
        if l > 2 and jacobi_symbol(n % l, l) != 1: return False
    for l in factorint(s):
        if k % l and jacobi_symbol((-n) % l, l) != 1: return False
    return True
inp = "".join(f"{n} {k}\n" for n, k, s in pairs)
out = subprocess.run([BIN], input=inp, capture_output=True, text=True, timeout=1700).stdout.split("\n")
res = {}
for line in out:
    if not line: continue
    t = line.split(); res[(int(t[0]), int(t[1]))] = (t[2] == "FAIL")
from collections import Counter
tab = Counter()
for n, k, s in pairs:
    tab[(n % 8, hyp(n, k, s), res[(n, k)])] += 1
print(f"Mordell-fibre pairs (n odd 9..{NMAX}, 1 <= k <= {KMAX}, 4k+n^3 = s^2): {len(pairs)}")
print("n mod 8 | hypothesis | S(N) empty : count")
for key in sorted(tab): print("  ", key, tab[key])
for n, k, s in pairs:
    if n % 8 == 5 and res[(n, k)] != hyp(n, k, s):
        print("   n≡5(8) mismatch:", n, k, s, "FAIL" if res[(n, k)] else "solvable", "hyp", hyp(n, k, s))

# feature split of the Mordell pairs (which local conditions matter)
def feats(n, k, s):
    c1 = gcd(n, k) == 1
    c2 = all(jacobi_symbol(n % l, l) == 1 for l in factorint(k) if l > 2)
    c3 = all(jacobi_symbol((-n) % l, l) == 1 for l in factorint(s) if k % l)
    return (n % 8, c1, c2, c3)
ft = Counter()
for n, k, s in pairs:
    ft[(feats(n, k, s), res[(n, k)])] += 1
print("features (n mod 8, gcd(n,k)=1, (n/l)=1 all odd l|k, (-n/l)=1 all l|s,l∤k) -> [solvable, empty]")
for f in sorted(set(x[0] for x in ft)):
    print("  ", f, [ft[(f, False)], ft[(f, True)]])

# refine: bad primes l | s, l ∤ k, (-n/l) = -1 (where A could have a non-zero local invariant)
bt = Counter()
for n, k, s in pairs:
    if gcd(n, k) != 1: continue
    fs = factorint(s)
    bad = sorted((l, e) for l, e in fs.items() if k % l and jacobi_symbol((-n) % l, l) == -1)
    if not bad: continue
    key = ("all bad e even" if all(e % 2 == 0 for l, e in bad) else "some bad e odd",
           "bad l=3 only" if [l for l, e in bad] == [3] else ("3 among bad" if 3 in [l for l, e in bad] else "3 not bad"))
    bt[(key, res[(n, k)])] += 1
print("gcd(n,k)=1 and some bad prime l|s with (-n/l)=-1: (v_l(s) parity, role of 3) -> [solvable, empty]")
for key in sorted(set(x[0] for x in bt)):
    print("  ", key, [bt[(key, False)], bt[(key, True)]])

# control: adjacent non-Mordell, non-square k' = k+1..3 for a random sample of 4000 Mordell pairs (A ramified there)
import random
random.seed(1)
smp = random.sample([(n, k) for n, k, s in pairs], min(4000, len(pairs)))
ctrl = [(n, k + dk) for n, k in smp for dk in (1, 2, 3)
        if isqrt(k + dk) ** 2 != k + dk and isqrt(4 * (k + dk) + n ** 3) ** 2 != 4 * (k + dk) + n ** 3]
o2 = subprocess.run([BIN], input="".join(f"{n} {k}\n" for n, k in ctrl), capture_output=True, text=True).stdout.split("\n")
emp = sum("FAIL" in l for l in o2)
print(f"control (n, k+1..3), same sizes, non-Mordell non-square: {emp} empty of {len(ctrl)}")

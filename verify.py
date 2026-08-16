#!/usr/bin/env python3
"""Erdős–Straus conjecture: numerical companion to notes.md.

All computations are cheap (seconds). We verify:
  (a) the Case-B/Case-A witness criterion resolves every prime p < LIMIT,
      recording minimal witnesses;
  (b) explicit solutions reconstructed from witnesses are exact (Fraction check);
  (c) the Jacobi obstruction lemma is consistent with observed witness failures;
  (d) a concrete finite system of "guaranteed" congruence families covers all
      primes except a residue concentrated in the six square classes mod 840,
      and every leftover prime is nevertheless solvable (factorization luck);
  (e) the classical identity families are exactly valid (symbolic spot checks).
"""
from fractions import Fraction
from sympy import primerange, factorint, jacobi_symbol
from collections import Counter

LIMIT = 100_000
SIX = {1, 121, 169, 289, 361, 529}  # squares of units mod 840, all ≡ 1 mod 24


def divisors_of_square(x):
    f = factorint(x)
    divs = [1]
    for r, e in f.items():
        divs = [d * r**k for d in divs for k in range(2 * e + 1)]
    return divs


def caseB_witness(p, qmax=400):
    """Smallest q ≡ -p (mod 4) with a divisor d | x², x=(p+q)/4, q | d+x."""
    q0 = (-p) % 4
    for q in range(q0, qmax + 1, 4):
        if q == 0:
            continue
        x = (p + q) // 4
        for d in sorted(divisors_of_square(x)):
            if (d + x) % q == 0:
                return q, d, x
    return None


def caseB_failed_qs(p, qfound):
    q0 = (-p) % 4
    return [q for q in range(q0, qfound, 4) if q != 0]


def caseB_solution(p, q, d, x):
    y1 = (x + d) // q
    z1 = (x + x * x // d) // q
    return (x, p * y1, p * z1)


def check_solution(p, sol):
    x, y, z = sol
    assert Fraction(1, x) + Fraction(1, y) + Fraction(1, z) == Fraction(4, p), (p, sol)


# ---------------------------------------------------------------- (a)+(b)
print("== (a) witness search over all primes 3 <= p < %d ==" % LIMIT)
minq = {}
worst = (0, 0)
six_primes = []
for p in primerange(3, LIMIT):
    w = caseB_witness(p)
    assert w is not None, f"no Case-B witness for {p} below qmax -- investigate!"
    q, d, x = w
    minq[p] = w
    sol = caseB_solution(p, q, d, x)
    check_solution(p, sol)          # (b) every reconstructed solution exact
    if q > worst[1]:
        worst = (p, q)
    if p % 840 in SIX:
        six_primes.append(p)
print(f"all primes solvable; every reconstructed solution verified exactly")
print(f"worst minimal q: p={worst[0]}, q={worst[1]}")

hist = Counter(minq[p][0] for p in six_primes)
print(f"\nprimes in the six hard classes mod 840: {len(six_primes)}")
print("minimal-q histogram (hard classes):",
      dict(sorted(hist.items())[:10]), "... max q =", max(hist))

p = 1201  # stubborn example from the play session
q, d, x = minq[p]
print(f"\np=1201 witness: q={q}, d={d}, x={x}, solution {caseB_solution(p,q,d,x)}")

# ---------------------------------------------------------------- (c)
print("\n== (c) Jacobi obstruction lemma consistency (hard-class primes) ==")
jac_obstructed = coset_miss = 0
for p in six_primes:
    qf = minq[p][0]
    for q in caseB_failed_qs(p, qf):
        x = (p + q) // 4
        if all(jacobi_symbol(r, q) == 1 for r in factorint(x)):
            jac_obstructed += 1     # provably no witness for this q (Lemma)
        else:
            coset_miss += 1         # QNR factor exists but coset still missed
tot = jac_obstructed + coset_miss
print(f"failed (p,q) pairs: {tot}; Jacobi-obstructed: {jac_obstructed} "
      f"({100*jac_obstructed/tot:.1f}%), coset-miss: {coset_miss}")

# sanity: the lemma claims Jacobi obstruction => no witness. Verify directly on
# a sample: recheck that no divisor works for obstructed pairs.
sample = 0
for p in six_primes[:200]:
    qf = minq[p][0]
    for q in caseB_failed_qs(p, qf):
        x = (p + q) // 4
        if all(jacobi_symbol(r, q) == 1 for r in factorint(x)):
            assert not any((d0 + x) % q == 0 for d0 in divisors_of_square(x))
            sample += 1
print(f"lemma re-verified directly on {sample} obstructed pairs")

# ---------------------------------------------------------------- (d)
print("\n== (d) coverage by guaranteed congruence families ==")


def rad_root(d):
    return 1 if d == 1 else __import__("math").prod(
        r ** -(-e // 2) for r, e in factorint(d).items())


families = []
for q in range(1, 60, 2):                    # constant-(q,d) Case-B families
    for d in range(1, 101):
        families.append(("B", q, d, rad_root(d)))
for j in range(1, 51):                       # linear d=1 families p≡-4 (4j-1)
    families.append(("L", 4 * j - 1, None, None))
for u in range(1, 21):                       # F1: p ≡ -(u+v) (mod 4uv)
    for v in range(u, 21):
        families.append(("F1", 4 * u * v, u + v, None))


def covered(p):
    for kind, a, b, c in families:
        if kind == "B":
            q, d, R = a, b, c
            if (p + q) % 4 == 0:
                x = (p + q) // 4
                if x % R == 0 and (x + d) % q == 0:
                    return True
        elif kind == "L":
            if p % a == (-4) % a and p > a:
                return True
        else:
            m, s = a, b
            if p % m == (-s) % m and p > m:
                return True
    return False


unc = [p for p in primerange(3, LIMIT) if not covered(p)]
cls = Counter(p % 840 for p in unc)
n_six = sum(1 for p in primerange(3, LIMIT) if p % 840 in SIX)
print(f"primes uncovered by the finite family system: {len(unc)} "
      f"of {len(minq)} ({100*len(unc)/len(minq):.2f}%)")
print("their classes mod 840:", dict(cls.most_common(8)))
print("all uncovered classes inside six hard classes?",
      set(cls) <= SIX)
print(f"(for scale: {n_six} primes < {LIMIT} lie in the six classes; "
      f"{n_six - sum(cls[c] for c in SIX)} of them got covered 'accidentally')")
# every uncovered prime is still solvable (checked in (a)); state it:
print("every uncovered prime nevertheless has a witness (checked in (a))")

# ---------------------------------------------------------------- (e)
print("\n== (e) identity family exactness (symbolic) ==")
from sympy import symbols, simplify, Rational

g, u, v = symbols("g u v", positive=True)
pF1 = 4 * g * u * v - u - v
expr = 1 / (g * u * v) + 1 / (pF1 * g * u) + 1 / (pF1 * g * v) - 4 / pF1
assert simplify(expr) == 0
print("F1: p = 4guv - u - v  =>  4/p = 1/(guv) + 1/(pgu) + 1/(pgv)   [exact]")

k = symbols("k", positive=True)
pm3 = 3 * k - 1  # p ≡ 2 (mod 3), k = (p+1)/3
expr = 1 / pm3 + 1 / k + 1 / (k * pm3) - 4 / pm3
assert simplify(expr) == 0
print("mod 3: p = 3k-1  =>  4/p = 1/p + 1/k + 1/(kp)                 [exact]")

h = symbols("h", positive=True)
pm4 = 4 * h - 1  # p ≡ 3 (mod 4), h = (p+1)/4
expr = 1 / h + 1 / (2 * h * pm4) + 1 / (2 * h * pm4) - 4 / pm4
assert simplify(expr) == 0
print("mod 4: p = 4h-1  =>  4/p = 1/h + 1/(2hp) + 1/(2hp)            [exact]")
print("\nall checks passed")

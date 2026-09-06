# Hostile review of §74 and block (bu)

Verdict: **SOUND-AFTER-REPAIRS** (one minor expository correction; the
mathematical theorems and `verify.py` survive unchanged).

Scope: the original `notes.md:28517–28857`, `verify.py:14579–14867`, and
the necessary definitions and analytic input in §70; §72's quoted census
entries were also checked. Line numbers in the defect list refer to the
pre-repair text at commit `0e71d6b`.

## Numbered defect list

1. **LOW — incorrect identification of the budget-refined majorant.**
   `notes.md:28677–28678`, exact quote:
   “The \(a=23\) proper F3 entry is in fact zero; its displayed numbers count
   only the containing \(\{\pm1\}\)-semigroup.”
   The pure-confinement number 0.07988 is the scale factor
   \(L^{-10/11}\) of the two-class semigroup. The budget-refined number
   0.07040 is \(L^{-21/22}\): with \(B_{23,K_1}=0\), its majorant permits
   only class 1, not both classes \(\pm1\). Neither scale factor is a
   count, and the exact-generation condition makes the F3 stratum empty.
   **Exact fix applied:** replace the passage through “real
   additional channel” with:

   > The \(a=23\) proper F3 count is in fact zero. Its pure-confinement
   > entry is only a scale factor for the containing \(\{\pm1\}\)-semigroup;
   > the budget-refined entry instead uses the class-\(1\) semigroup, since
   > \(B_{23,K_1}=0\) forbids every class-\(-1\) factor. Neither entry counts
   > proper F3 failures. At \(a=43\), the much larger proper semigroup is a
   > real additional channel.

No fatal, high-, or medium-severity defect was found. In particular, there
is no missing quantifier or independence hypothesis in Theorem 74.6.

## Hostile proof audit

**Stratification and budget transfer.** A realized nonresidue has even
order, because its image in the quotient by Q is nontrivial. Its subgroup
therefore contains the unique involution -1. The cyclic ambient group has
exactly one subgroup of each order 2d, d dividing odd n. Assigning the
*generated* subgroup makes (74.3) both exhaustive and disjoint; mere
containment would not, but that is not what the definition says. The d=1
case requires a factor of class -1 and hence cannot fail. In K of order 2d,
Q intersect K has order d and is exactly K's odd-order subgroup. Orders of
elements and the involution do not change on restricting to K. Inversion
orbits are wholly contained in K or wholly outside it. For each such orbit,
the signed valuation intervals add to every integer in [-V,V], including
when the two residue classes are carried by different primes. Thus
V >= ord(g)/2 realizes -1. Summing the caps proves (74.5), and also
B_(a,K) <= K_a. No independence or exact-generation probability is used.

**Pair exclusion, including the diagonal.** Choose *any* realized
nonresidue g. Failure excludes g=-1, so t=-g^(-1) is a nonidentity element
of Q. On odd-order Q, c -> t/c is an involution with unique fixed point
c0=t^((n+1)/2), since 2((n+1)/2)=1 modulo n. Therefore the other n-1
classes form exactly (n-1)/2 disjoint pairs. Two realized distinct paired
classes supply two distinct primes; the prime in class g is a third,
since g is not quadratic. The three positive exponent-one choices are
inside the signed valuation box and have product -1. For c0, total
multiplicity at least two supplies either two different primes, or one
prime of valuation at least two. Exponent two on that prime is legitimate
in Rat(h), not just in the unrestricted generated group. The g-prime is
again different. Thus m_c0 <= 1 is a multiplicity cap, not an unjustified
bound on the number of distinct factors. The pair {1,t} is non-diagonal;
Lemma 70.6 excludes t even if no class-1 factor is present. Not exploiting
that extra exclusion only enlarges the majorant.

**Quantifier chain and overlaps.** For every F3 integer there exists a
realized g != -1; in fact the lemma holds for every such g. For fixed g,
one can choose one side of each pair to cover all realized QR classes
except c0: when neither side is present, choose arbitrarily. Fix those
choices *before counting*. Let P0 be precisely the chosen sides, and P1
be all nonresidues together with c0. The actual integers for that choice
are contained in the event “all factors in P0 union P1 and Omega_P1 <=
K_a+1”. This containment discards exact generation, the requirement that
g be realized, and the separate individual caps; discarding them is safe
for an upper bound. The union over at most (n-1)2^((n-1)/2) events contains
all F3, including every proper stratum. An integer may belong to several
events, but summing their counts is an upper bound, not a disjointness
claim. There is no probabilistic independence assumption and no
conditioning-on-a-data-dependent-prime sieve argument.

**Analytic input and uniformity.** For every fixed event, P0 and P1 are
disjoint unions of reduced classes modulo the same fixed a. The Euler
series with one marker is

    product_(p in P0) (1-p^(-s))^(-1)
      * product_(p in P1) (1-z*p^(-s))^(-1).

Near s=1 this has pole exponent delta0+delta1*z and an analytic factor
locally uniform for z on a sufficiently small fixed circle about zero.
The fixed-order Selberg–Delange coefficient expansion gives the factor
(log H)^(delta0-1) and a polynomial of degree at most K_a+1 in loglog H.
This is exactly the fixed-mark upper bound (70.7), not a bare assertion
that a numerical Dirichlet density is sufficient. Here delta0=(n-1)/(4n)
is strictly positive (a>=7); in the subgroup application it is d/(2n)>0.
There is no zero-density endpoint issue. The prime a is excluded, and no
progression of h is selected, so neither exceptional content nor tied
nonprincipal twists enter. Exact generation is dropped for (74.7); its
unmarked set is Q_K, of density d/(2n), and its marked budget is fixed.
Taking a maximum of analytic constants over finitely many subgroups,
g's, and side choices is legitimate at fixed a. No uniformity as a grows
follows. No use of §70's two-form sieve is necessary for these integer
bounds; the honest-walls restrictions correctly prevent a shifted-prime
or growing-modulus conclusion.

**Exponents and dominance.** There are (n-1)/2 unrestricted classes out
of 2n; subtracting their density from 1 gives (3n+1)/(4n), exactly the
headline exponent. Subtracting 70.7's 1/2+1/(2n) gives (n-1)/(4n)>0 for
all a>=7 (at a=7: 5/6 versus 2/3). The extra loglog factor is asymptotically
smaller than this positive fixed log-power gain, so the *bounds*, not
merely the exponents, strictly improve asymptotically. Dividing by the
positive F1 asymptotic H/(log H)^(1/2) gives precisely the relative error
in (74.20). For proper strata d<=n/3, the refined saving is at least 5/6.
For composite n the largest proper d is n/iota(n), giving both entries
of (74.10). If n is prime, d=1 is the only proper option and it is empty,
so all F3 is full-group, exactly, not asymptotically. At a=43, d=7 gives
B=18 and exponent -5/6; all displayed budget and numerical scale tables
agree with independent arithmetic. These are upper bounds, not asymptotics
for nonempty F3 channels or explanations of the conditional census shares.
The recursion assessment only reuses disjoint NR/QR prime sets and makes
no further theorem claim.

## Computational results

The required foreground command was run with a 900-second timeout:

    timeout 900 uv run --with sympy,numpy,scipy python verify.py

Exit status 0; the complete verifier ended with `all checks passed`.
Block (bu) took 2.97 seconds and reproduced (74.21), (74.22), and (74.12).
Its default target checks cover only full-group rows, exactly as its prose
says; this is not computational coverage of the headline's whole domain.
The independent scan below closes that finite-coverage gap for four
coefficients, checking *every* realized g on *every* F3 row through 10^6.

| a | units | F1 | F3 strata d:count | all g checks | proper-stratum g checks |
|---|---:|---:|---|---:|---:|
| 7 | 857143 | 141538 | 3:87960 | 107427 | 0 |
| 19 | 947369 | 102682 | 3:10420, 9:311586 | 472987 | 10918 |
| 23 | 956522 | 205007 | 11:292995 | 408650 | 0 |
| 43 | 976745 | 82036 | 3:5097, 7:37325, 21:490734 | 921922 | 52987 |

Zero exceptions. The scan also independently matches both the 20,000
and 200,000 stratum pins in (bu), checks the individual inversion-orbit
caps and total within-K budgets, constructs valid side choices, and
checks the density arithmetic using exact fractions. Realized self-paired
classes of multiplicity one occur in 30,490, 32,348, and 22,227 g-checks
at a=19,23,43 respectively, so the diagonal test is not wholly vacuous.
Runtime: 33.65 seconds; peak RSS: 44,972 KiB, under the 512 MiB limit.
Finite checks support the algebraic implementation; they do not establish
the analytic estimates. `verify.py` needs no repair. After the notes repair,
the complete verifier and the embedded independent script were rerun;
both again exited 0 with identical census counts.

Reproduce the independent run from the worktree root with:

    timeout 900 uv run python -c 'from pathlib import Path; t = Path("reviews/wave31-sec74-review.md").read_text(); exec(compile(t.split("```python\n", 1)[1].split("```", 1)[0], "independent-sec74", "exec"))'

## Independent census source

This standalone program imports nothing from `verify.py`. It uses divisor
residues of `h²`, represented by cyclic bitsets in discrete-log coordinates,
and tests for `-h`, rather than copying the verifier's signed-product sets.
It constructs generated subgroups both by a gcd and by multiplicative closure.
The SPF array occupies about 4 MB; apart from the current integer's short
factorization, remaining working sets are O(a), not O(Ha). A 512 MiB
address-space limit is imposed before allocating the SPF.

```python
from array import array
from collections import Counter
from fractions import Fraction
from math import gcd, isqrt, log
import resource
from time import perf_counter

resource.setrlimit(resource.RLIMIT_AS, (512 * 1024**2, 512 * 1024**2))
H = 1_000_000
started = perf_counter()
spf = array('I', range(H + 1))
for p in range(2, isqrt(H) + 1):
    if spf[p] == p:
        for v in range(p * p, H + 1, p):
            if spf[v] == v:
                spf[v] = p


def phi(r):
    return sum(gcd(j, r) == 1 for j in range(1, r + 1))


def budget(d):
    # Order 2r contributes phi(r)/2 inversion pairs, each with cap r-1.
    return sum(phi(r) * (r - 1) // 2
               for r in range(3, d + 1, 2) if d % r == 0)


expected20 = {
    7: {3: 2149}, 19: {3: 275, 9: 7391},
    23: {11: 6722}, 43: {3: 139, 7: 1007, 21: 11039},
}
expected200 = {
    7: {3: 18992}, 19: {3: 2296, 9: 66426},
    23: {11: 61744}, 43: {3: 1135, 7: 8300, 21: 102673},
}
for a in (7, 19, 23, 43):
    m = a - 1
    n = m // 2
    root = next(r for r in range(2, a)
                if len({pow(r, j, a) for j in range(m)}) == m)
    residues = [pow(root, j, a) for j in range(m)]
    logs = {r: j for j, r in enumerate(residues)}
    allbits = (1 << m) - 1
    data = {}
    for k in range(1, m, 2):
        if k == n:
            continue
        T = (n - k) % m
        c0 = T * ((n + 1) // 2) % m
        assert T != 0 and T % 2 == c0 % 2 == 0
        assert 2 * c0 % m == T
        pairs = [(c, (T - c) % m) for c in range(0, m, 2)
                 if c < (T - c) % m]
        assert len(pairs) == (n - 1) // 2
        assert {c0} | {x for pair in pairs for x in pair} == set(range(0, m, 2))
        data[k] = (T, c0, pairs)
    budgets = {d: budget(d) for d in range(1, n + 1) if n % d == 0}
    strata, c20, c200 = Counter(), Counter(), Counter()
    f1 = successes = units = checked_g = proper_g = self_one = 0
    for h in range(1, H + 1):
        if h % a == 0:
            continue
        units += 1
        value = h
        factors = []
        while value > 1:
            p = spf[value]
            e = 0
            while value % p == 0:
                value //= p
                e += 1
            factors.append((p, e, logs[p % a]))
        # Divisors D of h^2, not signed products D/h.
        mask = 1
        hlog = 0
        divisor_gcd = m
        for p, e, k in factors:
            old = mask
            mask = 0
            for j in range(2 * e + 1):
                shift = j * k % m
                mask |= ((old << shift) | (old >> (m - shift))) & allbits
            hlog = (hlog + e * k) % m
            divisor_gcd = gcd(divisor_gcd, k)
        assert residues[hlog] == h % a
        failed = not ((mask >> ((n + hlog) % m)) & 1)
        all_qr = all(k % 2 == 0 for _, _, k in factors)
        if all_qr:
            assert failed
            f1 += 1
            continue
        if not failed:
            successes += 1
            continue
        order = m // divisor_gcd
        assert order % 2 == 0
        d = order // 2
        assert d in budgets and d != 1
        predicted = {residues[j] for j in range(0, m, divisor_gcd)}
        generated = {1}
        todo = [1]
        while todo:
            x = todo.pop()
            for p, _, _ in factors:
                y = x * p % a
                if y not in generated:
                    generated.add(y)
                    todo.append(y)
        assert generated == predicted and a - 1 in generated
        assert all(p % a in generated for p, _, _ in factors)
        # Exactly one canonical even subgroup contains this exact generation.
        assert sum(predicted == {residues[j] for j in range(0, m, n // dd)}
                   for dd in budgets) == 1
        counts = [0] * m
        orbits = Counter()
        for p, e, k in factors:
            counts[k] += e
            if k % 2:
                orbits[min(k, (-k) % m)] += e
        for k, V in orbits.items():
            assert V <= (m // gcd(m, k)) // 2 - 1
        omega = sum(counts[1::2])
        assert 1 <= omega <= budgets[d] <= budgets[n]
        strata[d] += 1
        if h <= 20_000:
            c20[d] += 1
        if h <= 200_000:
            c200[d] += 1
        for k in range(1, m, 2):
            if not counts[k]:
                continue
            checked_g += 1
            proper_g += d != n
            assert k != n
            T, c0, pairs = data[k]
            assert counts[T] == 0 and counts[c0] <= 1
            self_one += counts[c0] == 1
            sides = set()
            for c, mate in pairs:
                assert not (counts[c] and counts[mate])
                sides.add(c if counts[c] else mate)
            assert len(sides) == (n - 1) // 2
            assert all(not counts[c] or c in sides or c == c0
                       for c in range(0, m, 2))
            assert omega + counts[c0] <= budgets[n] + 1
    assert dict(c20) == expected20[a]
    assert dict(c200) == expected200[a]
    assert units == f1 + successes + sum(strata.values())
    if phi(n) == n - 1:
        assert set(strata) == {n}
    else:
        least = next(r for r in range(3, n + 1, 2) if n % r == 0)
        assert max(d for d in strata if d < n) == n // least
        assert Fraction(n // least, 2 * n) - 1 == -1 + Fraction(1, 2 * least)
    beta = 1 - Fraction((n - 1) // 2, m)
    assert beta == Fraction(3, 4) + Fraction(1, 4 * n)
    assert beta - (Fraction(1, 2) + Fraction(1, 2 * n)) == Fraction(n - 1, 4 * n) > 0
    print('a=', a, 'units=', units, 'F1=', f1, 'success=', successes,
          'F3 strata=', dict(sorted(strata.items())),
          'g checks=', checked_g, 'proper g checks=', proper_g,
          'self multiplicity-one checks=', self_one, 'budgets=', budgets,
          flush=True)
L = log(10**7)
assert abs(L ** (1 / 11 - 1) - 0.07988) < 0.000005
assert abs(L ** (1 / 22 - 1) - 0.07040) < 0.000005
print('independent census passed; seconds=', perf_counter() - started,
      'peak RSS KiB=', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
```

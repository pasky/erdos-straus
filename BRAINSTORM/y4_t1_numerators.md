# y4_t1_numerators — which numerators carry T1, and which are blind? (O212, goal (c))

## Idea
O208 Thm 1.1 proved, for M ≡ 0 (mod 4), that the relaxed M^□ is a theorem at every odd non-square and that its shot
family keeps T1. O208 spark 2 asks for ALL numerators. The shot identity (SYNTHESIS_SPARKS3 Lemma 1.0) is valid for
every M ≥ 1. The only numerator-dependent input of Thm 1.1 is the key sign (∗): (−M/g) = −1 for every odd g ≡ −1 (mod M).

**Prop 1 (PROVED, reciprocity only).** Let M ≥ 3. The sign (−M/g) (Jacobi) is the constant −1 on the odd g ≡ −1 (mod M)
⟺ **M ≡ 0 or 3 (mod 4)**, i.e. ⟺ −M is a discriminant (≡ 0, 1 mod 4); equivalently the Kronecker character χ_{−M} of
ℚ(√−M) has conductor dividing M, so that χ_{−M}(g) = χ_{−M}(−1) = −1.
*Proof.* M ≡ 0 (4): O208 (∗). M ≡ 3 (4), g odd, g ≡ −1 (M): (−M/g) = (−1/g)(g/M)(−1)^{((M−1)/2)((g−1)/2)}
= (−1/g)·(−1/M)·(−1/g) = (−1/M) = −1 ((M−1)/2 odd; (g/M) = (−1/M) as Jacobi symbols). M ≡ 1 (4): the same computation
gives (−M/g) = (−1/g)(−1/M) = (−1/g), and g mod 4 is free (M odd), so both signs occur. M ≡ 2 (4), M = 2M′: g mod 8 is
free subject to g ≡ −1 (M′); (−2/g) differs between g ≡ 1 and g ≡ 5 (mod 8), which have the same g mod 4, so the sign
is not constant. ∎

**Cor 2 (PROVED; Dirichlet + Lemma 1.0).** For odd n prime to M:
(a) n not a square ⇒ M^□(n) holds for every M ≥ 3 (choose a prime g ≡ −1 (mod M) with (n/g) = −(−M/g) — possible
because (n₀/g) varies with g mod n₀ (or mod 8 if 2 | n₀) independently of g mod M; then −n/M is a square mod g).
(b) **T1 (odd g):** for M ≡ 0, 3 (mod 4) no odd g > 1, g ≡ −1 (mod M), divides k² + MQ² (gcd(Q, k) = 1, gcd(k, M) = 1):
every odd prime ℓ of k² + MQ² has (−M/ℓ) = 1, contradicting Prop 1. For M ≡ 3 (mod 8) EVEN g can occur
(χ_{−M}(2) = −1 and k² + MQ² ≡ 4 mod 8 for k, Q odd; e.g. M = 3: 25 + 3 = 28, g = 2); restricting to Q even
(n + MQ² odd) restores T1. For M ≡ 7 (mod 8), 2 splits and T1 holds for all g.
(c) For M ≡ 1, 2 (mod 4) the relaxation holds at odd squares too (choose g with (−M/g) = +1): no T1 at all.

So the T1-bearing numerators are exactly the M with −M a discriminant: 3, 4, 7, 8, 11, 12, 15, 16, 19, 20, 23, 24, …
Among them, **failure-free to 10⁸ (primes): 3 (trivial: 3/n = 1/n+1/n+1/n), 4, and 7**. 7/n is the honest
"non-trivial sibling of 4": same T1 structure in the Type II shot family, blind relaxation, no failure ≤ 10⁸
(MODEL_SPECIFIC census), and **not** a character fibre on the length-3 slices ((J)32 Thm 3.1(c); S_7(p) = ∅ at 10
primes ≤ 10⁵ while 7/p is solvable there).

## Literature
Bright–Loughran (sources/bright-loughran-1908.02526.pdf) Remark 1.10: for Schinzel's m/n every positive solution
satisfies ∏_{p | 2nm}(−u₁/u₃, −u₂/u₃)_p = −1 (analogue of their Thm 1.2); they do not tabulate which m give an
obstruction at squares. Pomerance–Weingartner (sources/pw.txt) Table 1 for failures. Prop 1 is an elementary
reciprocity computation; I did not find it stated, but it is surely folklore-level.

## Barrier screen
Prop 1 is a classification of the B5/T1 structure across numerators; it is numerator-uniform within each class
mod 4, hence by O208 Cor 2.1 extended (harness below) it gives no input. New harness entries (beyond 8/131): **11/37**
and **11/3** (M ≡ 3 mod 4, T1-bearing, relaxation true, exact problem false):
`11/37 = 1/8 + 1/148 + 49/296` (g = 43, Q = 14), `11/3 = 1/7 + 1/12 + 289/84` (g = 43, Q = 17).

## Cheap numerics (`scripts/y4_t1_numerators.py`, ~2 min)
For M = 3..24: odd squares k² (k ≤ 99, gcd(k, M) = 1), Q ≤ 40: odd-g shots = 0 exactly for M ≡ 0, 3 (mod 4)
(M = 3, 4, 7, 8, 11, 12, 15, 16, 19, 20, 23, 24), and 162–1711 for M ≡ 1, 2 (mod 4). Even-g shots at squares occur
exactly for M ∈ {3, 11, 19} (≡ 3 mod 8) and for odd M ≡ 1 (mod 4). An M^□ certificate (exact rational check) exists at
every one of the failing pairs (M ≤ 24; M = 21–23 to 10⁷): max Dirichlet g per M from 23 (M = 8) to 919 (M = 23).

## Assessment
PROVED classification (Prop 1, Cor 2); harness extended to the M ≡ 3 (mod 4) family. The comparison it forces:
any "input specific to 4" must be checked against **7** as well. An input true for 4 and false for 7 is not
refuted, but an input that is TRUE for 7 and false for 8 and 11 would be the more natural "no-failure" mechanism; the
length-3 χ-fibre is false for 7 (S_7 can be empty), so the slice route is not what keeps 7 failure-free —
evidence (not proof) that "no failure" for small numerators is count-driven (MODEL_SPECIFIC §5.3), and that
the χ-fibre is a structural, not a "why it never fails", property.

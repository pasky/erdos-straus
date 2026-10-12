# BRAINSTORM: Erdős–Straus in other rings (O140, angle c)

Script: `scripts/bs_ff_rings.py D [J] [B]` (real quadratic O_K; exact verification of identities).

## 1. Idea
Find rings R with a positivity notion in which positive ES (4/n = 1/x+1/y+1/z, x, y, z in the
positive cone C ⊂ R) is *provable*. Then identify the mechanism and ask whether it transfers to Z.

## 2. Literature anchor
* Bradford–Ionascu, *Unit fractions in norm-Euclidean rings of integers*, arXiv:1405.4025 (verified
  2026-10-12, abstract and §1–3 read). Without a cone condition, ES is trivial over Z (eq. (2):
  `4/(4k+1) = 1/k − 1/(k(4k+1))`). In norm-Euclidean quadratic rings ES has solutions outside a
  finite exceptional set (Thm 2.1). For d ∈ {2,3,5,…,73}, even `4/n = 1/a + 1/b` holds (Thm 3.1).
  Their Gaussian version with a cone condition (Conj. 1.1: denominators with Re, Im of equal sign) is
  open, and does not reduce to primes.
* No literature found on *totally positive* ES over real quadratic fields or on positive ES over
  S-integers (three web searches; absence not proved).

## 3. Results

**Lemma 3.1 (unit-sum mechanism; PROVED).** Let R be a domain in a field with a multiplicatively
closed positive cone C ⊆ R∖{0}, with 4 ∉ R^×. Suppose e ∈ C satisfies e = 1/u + 1/v with u, v ∈ C.
Then for every n ∈ C with n + e ∈ 4C, ES_C(n) holds:
`4/n = 1/x + 1/(unx) + 1/(vnx)`, x = (n+e)/4.
In particular this holds if e | 1 + η with η a unit in C and κ = (1+η)/e ∈ C: take u = κ/η, v = κ.
*Proof.* 4/n − 1/x = e/(nx). ∎

Over Z (C = ℕ): sums of two positive unit fractions are ≤ 2, so the only integer e are 1 = ½+½ and 2 = 1+1.
They give exactly the classical easy classes n ≡ 3 (mod 4) and n ≡ 2 (mod 4). The class n ≡ 1 (mod 4)
would need some e ≡ 3 (mod 4) in 1/ℕ + 1/ℕ, and no such e exists. **This is the archimedean crux:
ℕ is bounded away from 0 (x ≥ 1).** The divisors needed in the e-slice must then come from the
p-dependent integer N = n·x (the B2 lottery). The units ±1 supply only the divisor pair (1,1).

**Proposition 3.2 (S-integers; PROVED).** Let R = Z[1/3] and C = R_{>0}. Then positive ES holds for
every integer n ≥ 2. For n ≡ 1 (mod 4) take e = 7 = 1/(4/27) + 1/4 (7 | 1 + 3³). Explicitly,
`4/n = 1/x + 27/(4nx) + 1/(4nx)` with x = (n+7)/4; the classes n ≢ 1 (mod 4) are classical.
The same works for Z[1/ℓ] whenever some 1 + ℓ^k has a divisor e ≡ 3 (mod 4) with e ∈ ℓ^ℤ·ℕ. For example,
ℓ = 5 gives e = 3 | 6. If 2 ∈ S, ES is trivial outright, since 4 is a unit.

**Proposition 3.3 (real quadratic fields with N(ε) = −1; PROVED).** Let K = Q(√D) be real quadratic
with fundamental unit ε of norm −1, and C the totally positive elements of O_K. Then every rational
integer n ≥ 2 satisfies positive ES over O_K. Hence ES "holds" over O_K, uniformly, by one identity
per class mod 4.
*Proof.* n even or n ≡ 3 (mod 4): classical. n ≡ 1 (mod 4): by Dirichlet pick a prime ℓ ≡ 3 (mod 4)
inert in K; the conditions (D/ℓ) = −1 and χ₋₄(ℓ) = −1 involve distinct characters. In
O_K/ℓ = F_{ℓ²}, Frobenius is conjugation, so ε^{ℓ+1} ≡ N(ε) = −1. Hence ord(ε) = 2^{s+1}m with
s = v₂(ℓ+1) ≥ 2, so ord(ε²) is even, and η := ε^{2j} ≡ −1 (mod ℓ) for j = ord(ε²)/2. Now η is
totally positive, ℓ | 1 + η, and κ = (1+η)/ℓ is totally positive. Apply Lemma 3.1 with e = ℓ;
x = (n+ℓ)/4 ∈ ℤ. ∎
Example (D = 2): ℓ = 3, η = ε⁴ = 17+12√2, κ = 6+4√2, and `3 = 1/(6−4√2) + 1/(6+4√2)`. So for
n ≡ 1 (mod 4), `4/n = 1/((n+3)/4) + 1/((6−4√2)nx) + 1/((6+4√2)nx)`, with 6 − 4√2 ≈ 0.34 ≫ 0.

**EVIDENCE (bs_ff_rings.py, box |a|,|b| ≤ 40, η = η₁^j, j ≤ 10, identities verified exactly with
fractions for n = 5, 13, 17, 29, 101).** For D = 3, 6, 7 (N(ε) = +1) the rational classes are
covered as well, so positive ES holds for all rational n. For D = 3, 6 *every* class of (O_K/4)^* is hit,
so positive ES holds for every totally positive n ∈ O_K prime to 2. For D = 2, 5, 7, 13 some
non-rational classes are not hit within the box.

## 4. The principle, and the barrier screen
**Assessment (unifying principle).** Positive ES is a genuine lottery problem exactly when the
positive cone is *discrete at infinity*: |x|_v ≥ 1 at an archimedean (or the ∞) place for all
x ∈ C. This holds for ℕ, for monic F_q[t] (BRAINSTORM/ff_erdos_straus.md), and for Bradford–Ionascu's
Gaussian cone (open, consistent). When C contains elements arbitrarily close to 0 at some place
(units of infinite order in C, S-units, totally positive integers < 1 in one embedding), Lemma 3.1
gives a p-independent supply of "universal divisors" (η, 1). ES then collapses to a finite
covering of classes mod 4, as in Props 3.2–3.3.
* **Transfer to Z: none.** ℕ^× = {1}. The only substitutes for universal divisors in Z are
  divisors forced by congruence: these are the covering families, i.e. B1. Through B1 one hits the
  odd-square / class-1 obstruction.
* **B5/T1.** Over O_K, odd squares n = m² are solved by Prop 3.3 (n ≡ 1 mod 4). The step that is
  false over Z at m² is "e = ℓ ∈ 1/C + 1/C". It uses a totally positive element of O_K of size < 1 at
  one place, and ℕ has none. This also explains why such rings are useless as models for the hard core.
* **B2/B3/B6.** Not reached: the mechanism never needs divisors of p-dependent integers. That is
  precisely why it cannot inform the Z problem.
* **Imaginary quadratic / Gaussian with cone.** The cone is discrete (|x| ≥ 1), so the problem is a
  lottery again. The Type I/II structure becomes a 2-dimensional lattice-sign problem, and there is
  no evidence of a mechanism that Z lacks. Bradford–Ionascu note it does not even reduce to primes.

## 5. Viability Assessment: **PARTIAL** (new exact reformulation of the crux; no route to ES)
By-products: Lemma 3.1 (PROVED), Prop 3.2 (PROVED), Prop 3.3 (PROVED: positive ES over every real
quadratic O_K with N(ε) = −1, for all rational n), EVIDENCE for D = 3, 6, 7. The crisp statement for
the campaign: **ES over Z is hard because ℕ has no element below 1. The "missing" universal divisor
pairs (η, 1) must be replaced by divisors of p-dependent integers (the B2 lottery).** Collapses (for
Z) to B1 at the step "find universal divisors": in Z these are congruence-forced divisors only.

## Errata (triage O156/O157)

Appended by O160; the memo body above is unchanged. Source: reviews/triage-brainstorm-B.md (per-memo paragraph).
Scope corrections only; no computational counterexample is involved.

* §4's "positive ES is a lottery problem exactly when …" (line 60) is an Assessment, not a result: arbitrarily small
  positive elements alone do not show that the unit-sum mechanism covers the required residue classes.
* Prop 3.3 is proved for rational integer inputs (not every totally positive element of O_K) and uses N(ε) = −1
  (memo line 81); shortcut: η = ε^{ℓ+1} for an inert ℓ ≡ 3 (4) gives η ≡ N(ε) = −1 (mod ℓ), totally positive.
* The norm-Euclidean theorem cited in §2 does not by itself establish the positivity claim.

# BRAINSTORM: polynomial method / auxiliary polynomials / lattices at a single p (O140, angle b)

## 1. Idea
At fixed p every encoding reduces to (B2): *one integer N = N_θ(p) has a divisor d ≡ r (mod s)*, with
s part of the solution (e-slice: −1 ∈ {ab⁻¹ mod e : ab | N}, N = (p+e)/4). Could an
auxiliary-polynomial argument (Stepanov, Thue–Siegel, Coppersmith/Howgrave-Graham lattices,
Chevalley–Warning / Combinatorial Nullstellensatz / zero-sum theory, Thue–Minkowski geometry of
numbers) prove that such a divisor EXISTS? Four sub-ideas, screened separately.

## 2. Literature anchor
* Lenstra 1984 (Math. Comp. 42): for s ≥ N^{1/3} at most 11 divisors d ≡ r (mod s).
  Coppersmith–Howgrave-Graham–Nagaraj 2008 ("Divisors in residue classes, constructively",
  Math. Comp. 77): for s > N^{α}, α > 1/4, O((α − 1/4)^{−3/2}) such divisors, all found in polynomial
  time by lattice reduction. (From memory; bibliographic details unverified here.) Both are
  *upper bounds + enumeration*. POINTWISE_MORDELL17.md already uses Lenstra's bound.
* Stepanov's method: upper bounds for point counts; lower bounds arise only through an exact
  identity (sum over twists) combined with upper bounds for the complement.
* Zero-sum theory: Davenport constant via Chevalley–Warning (Olson 1969 for p-groups); Olson /
  Erdős–Heilbronn / Szemerédi–Vu type results: subset sums of a set of L elements in Z_m cover Z_m
  only when L ≳ √m, unless extra non-degeneracy is assumed. (From memory, unverified.)
* Thue's lemma / Minkowski: x ≡ λy (mod m) with 0 < |x|, |y| ≤ √m, signs uncontrolled.

## 3. Barrier screen, per sub-idea

**(b1) Coppersmith / CHN lattices.** These count and find divisors in a class; they prove at most
O(1) of them in the regime s > N^{1/4}. In that regime the expected number is < 1 (B2's lottery),
so an upper bound is the true answer. The lattice finds a root *if one exists*; the existence is
the open question. **Collapses** (no positive main term; useful only as a fast search tool).

**(b2) Stepanov-type "upper bound on the complement".** Exact total: Σ_{r mod s} #{d | N : d ≡ r} = d(N).
Forcing the target class to be nonempty needs Σ_{r ≠ target} #{…} < d(N), so we need per-class upper
bounds below d(N)/φ(s)·(1 + o(1)) for all classes simultaneously, i.e. near-equidistribution of
the divisors of the single integer N mod s. That needs d(N) ≫ φ(s). For the witness moduli forced by
(H) rate (`W(p) ≥ exp(c(log p)^{1/4}(log log p)^{−1/4})` i.o.), N must have ≥ c(log p)^{1/4} prime
factors in non-degenerate position. That is precisely the deterministic small-prime-factor covering
of LONGSHOT_PIGEONHOLE, which fails for a positive proportion of primes (B4, Thm 2.2).
**Collapses to B4/B3.**

**(b3) Polynomial method in additive combinatorics (Chevalley–Warning, Alon's CN, Olson).** The ratio
set {ab⁻¹} of divisors of N = ∏ℓ_i^{e_i} is the set of ±1-weighted subset products of the ℓ_i in
G = (Z/e)^*. Chevalley–Warning / Davenport-constant arguments produce a *zero-sum*: a nontrivial
ab⁻¹ ≡ **+1**. That is the signed problem (a ≡ b, solved by a = b = 1, the "pigeonhole collisions
give only signed solutions" of LONGSHOT_PIGEONHOLE). The ES target is the *specific non-identity
element −1*, and hitting a prescribed element needs the full ratio set to be G. Deterministic
covering theorems need L ≳ √|G| elements in general position: a counterexample is L elements whose
discrete logs lie in [1, L], with ± sums in [−L², L²]. So a CN-type certificate produces witnesses with
e ≤ C·ω(N)² ≤ C(log p)². By the (H) rate result (STATUS "Pointwise state", POINTWISE_OMEGA13
Thm 5.1, PROVED modulo cited inputs), no pointwise mechanism whose witness moduli are
≤ exp((log p)^{1/4−ε}) proves ES. **Collapses to B1, with a precise reason:** zero-sum methods
certify the identity element, but positivity asks for −1.

**(b4) Thue / Minkowski geometry of numbers.** For the Type I chart, f | p² + 4c²d with
f ≡ −p (mod 4cd) is a representation problem for the binary form x² + 4c²dy². Minkowski's theorem
represents a multiple of f by *some* form of the right discriminant. To get the required form you
need a class-group / genus condition — exactly (I)1/(I)3 — and Thue's lemma gives no control of signs.
**Collapses to B2** (genus data at Planck scale).

**T1 (odd squares).** At n = m² the divisors of N_θ(m²) still have rich subset products. The step
that must fail is "the ratio set contains −1". (b2) and (b3) give no reason why it should hold at
p but fail at m²: they see only multiplicative statistics of N, which are the same in the two cases.
Any of them that claimed −1 ∈ ratio set from such statistics alone would therefore be refuted
by T1 (ET Prop 1.6). This is the same Jacobi-symbol phenomenon as Lemma CT.

**T7.** Not applicable: all four are genuinely pointwise. Their weakness is the missing main term.

## 4. Experiment
None needed. The collapse is structural, and the per-class counts are those of B2 (EVIDENCE in
(I)8, red team 2 §2). No script.

## 5. Viability Assessment: **COLLAPSES** — (b1) no main term; (b2) to B4/B3; (b3) to B1 (zero-sum
gives +1 instead of −1; CN-type witnesses have moduli ≤ (log p)², below the proved
exp(c(log p)^{1/4−}) rate); (b4) to B2 (genus).
By-product (Assessment, folklore-level): a clean slogan for why ES is not a zero-sum problem.
The e-slice ratio set always contains +1 (signed ES is trivial). ES asks for a prescribed
non-identity element, and only full-coverage (equidistribution) results can supply that.

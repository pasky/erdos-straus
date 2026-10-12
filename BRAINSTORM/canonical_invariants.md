# BRAINSTORM O153 / W1 — canonical invariants of p as algebraic seeds (units, class groups, Cornacchia)

**Verdict: COLLAPSES.** Unit seeds collapse to B3 (size). Representation seeds collapse to B2 (their content
modulo p is a square root of −d, and their angle is Planck-scale). EVIDENCE: no measurable seed effect on
slice success. No case of ES is claimed.

## 1. Idea

The campaign's barriers (Thms M, C, F, Prop A; (I)8) exclude inputs that see p only through congruences.
A prime p ≡ 1 (mod 4) also carries canonical **non-congruence** objects:
* **(U)** the fundamental unit `ε_p = (t + u√p)/2` of ℚ(√p). Its norm is −1 (Legendre: `x² − py² = −1` is
  solvable for prime p ≡ 1 (4)).
* **(R)** for every d with (−d/p) = +1, a representation `p = u² + dv²` (with d = 1 always available; Cornacchia).
  More generally, the ideal classes above p.
* **(H)** class numbers h(p), h(−4p), and the class of the ideals above p.

Algebraic forcing would then read: *build an ES solution as an explicit algebraic function of (t,u) or (u,v).*
This is not a counting argument. It also passes T1 at the first step for (U): at n = m², ℚ(√n) = ℚ, so no
unit seed exists. A proof would need a uniform recipe that is valid for every prime p ≡ 1 (24), or at least
for every prime in some class of positive density.

## 2. Literature anchor

* Negative Pell for prime p ≡ 1 (4): classical (Legendre; any textbook, e.g. Ireland–Rosen; standard).
* Sizes of regulators: "most" p have `log ε_p ≍ √p` up to `L(1,χ_p)` and h(p) (class number formula
  `h(p) log ε_p = √p L(1,χ_p)`). Hooley (J. reine angew. Math. 353 (1984)) conjectured that
  `#{d ≤ X : ε_d ≤ d^{1/2+α}}` has order `X^{1/2} log² X`. Fouvry–Jouve have related lower bounds.
  *(from memory, unverified; not used in any PROVED statement below.)*
* Class-group / Frobenius data of the factors of N_e: BRAINSTORM/nonab_frobenius_redei.md D1. CM-torus coefficient
  0: EXACT_FORMULA Thm 5.2 ((I)5).

## 3. Statements

**Lemma A (size of solutions; PROVED, elementary, folklore).** If `4/n = 1/x + 1/y + 1/z` with `x ≤ y ≤ z`
positive integers, then `x ≤ 3n/4`, `y ≤ 3n²/2` and `z ≤ (9/8)n⁴`.
*Proof.* `4/n ≤ 3/x`. Next, `r := 4/n − 1/x = (4x−n)/(nx) ≥ 1/(nx)` and `r ≤ 2/y`, so `y ≤ 2nx`.
Finally `1/z = (4xy − n(x+y))/(nxy)`, whose numerator is a positive integer, so `z ≤ nxy`. ∎
Every ET parameter (a, b, c, d, e, f) is therefore `≤ p^{O(1)}`: in ET's parametrisation each one is bounded by a
fixed polynomial in the coordinates.

**Prop B (unit seeds: archimedean use is power-sparse, otherwise residues; PROVED part + EVIDENCE + Assessment).**
Let R be a rule that produces, for a prime p, an ES solution one of whose coordinates is `≥ ε_p^{δ}/p^{K}`
(this is "using the unit as a number": the unit or a power of it appears in the output). By Lemma A, R can
only apply when `log ε_p ≤ ((4+K)/δ) log p + O(1)`. **EVIDENCE** (`scripts/bs_wild_units.py`,
`logs/bs_wild_units.txt`): the number of primes p ≡ 1 (4), p ≤ X, whose fundamental solution of `x² − py² = −1`
is `≤ p⁴` is 721, 2184 and 4394 for X = 10⁵, 10⁶ and 4·10⁶. That is a ratio of ≈ 0.010–0.017 to
`X^{1/2}log²X`, out of 4783, 39175 and 141502 primes. So the set is power-sparse, as Hooley's heuristic predicts.
*Assessment.* For the remaining primes, R can use ε_p only through quantities of size `p^{O(1)}`: residues
`(t mod M, u mod M)` with M ≤ p^{O(1)}, or gcds with such moduli. A residue of ε_p modulo a prime q is a
power-residue symbol of the unit, i.e. Frobenius data in `ℚ(√p, ζ_m, ε_p^{1/m})`. The slice event is abelian
Frobenius data of the factors of N_θ(p) (nonab D1). So such data can enter only by *choosing* θ (H-D), and the
per-slice event stays the lottery (B2).

**Prop C (representation seeds carry only √−d mod p plus a Planck-scale angle; PROVED observation).**
Let `p = u² + dv²` with `p ∤ v`. Then `(u v⁻¹)² ≡ −d (mod p)`. So the residue class of the seed modulo p is one of
the two square roots of −d mod p, i.e. the choice of a prime of ℚ(√−d) above p, which is congruence data in that
field. The rest of the information is
* the archimedean angle `arg(u + v√−d)` (a Hecke angle). The fixed-p ES conditions sit in tubes of width ≍ 1/p
  ((I)3, POINTWISE_SPECTRAL Props 3.1/3.2, 5.4), and that is the Planck-scale barrier;
* the residues `(u, v) mod q` for q ≠ p. These are ray-class data of ℚ(√−d) of conductor q (dihedral Frobenius),
  which have coefficient 0 in the Type I count on the CM torus (EXACT_FORMULA Thm 5.2).
*Proof of the congruence.* `u² ≡ −dv² (mod p)` and v is invertible. ∎

**Is there a polynomial (u,v)-recipe?** If `4/Q(u,v) = Σ 1/φ_i(u,v)` held for (u,v) on a Zariski-dense set of
prime representations, with φ_i ∈ ℚ(u,v) and `Q = u² + dv²`, then it would hold identically in ℚ(u,v)
(LONGSHOT_FIBRED Lemma 2.1 style). The Pythagorean points `Q = m²` would then give solutions at odd squares. To
contradict ET Prop 1.6 one also has to transport the Type I/II coprimality pattern to those points, and that is
not a congruence statement. So this sub-route is **UNCLEAR as a theorem**. It is not pursued: by Prop C the seed
supplies nothing beyond √−d mod p and a Planck angle, so even a valid family would be a two-variable polynomial
family. Such families fall under Thm M / Cor 2.4 heuristics. Note that LONGSHOT_FIBRED Cor 2.4 does **not**
apply verbatim: the seeds are finitely many points per fibre, not a Zariski-dense subset of it.

## 4. Experiment (EVIDENCE): do seeds carry slice information beyond congruences?

`scripts/bs_wild_seeds.py 5000000 71` (`logs/bs_wild_seeds.txt`, 11 s). The setup:
* primes p ≡ 1 (24), p ≤ 5·10⁶, written as `p = u² + v²`;
* primes e ≡ 3 (4), e ≤ 71, restricted to (p/e) = +1, so the congruence data mod e are held fixed;
* the e-slice success `−1 ∈ Σ_e(N)` for Type II (N = (p+e)/4) and Type I (N = (pe+1)/4), split by the
  non-congruence events e | v, e | u, or neither.

Sample rows, Type II rates as v / u / neither:
* e = 7: .540 / .539 / .538
* e = 11: .448 / .442 / .443
* e = 23: .615 / .590 / .583
* e = 31: .270 / .280 / .281
* e = 43: .121 / .102 / .111

Of 20 comparisons, all lie within ≈ 2σ except Type II at e = 47 (.525 vs .469, n = 793, ≈ 3σ). That is
consistent with noise under multiple testing. **No detectable seed effect.** By-product (EVIDENCE): the slice
success rate depends strongly on e (≈ .1 for e = 19, 43, 67; ≈ .6 for e = 23). That is congruence structure of the
small primes that can divide N_e, not seed information.

## 5. Barrier screen

* **B1.** (U): residue use is congruence/Frobenius data, which Thm M/C cover after one chooses θ. (R): the
  mod-p content is √−d mod p.
* **B2.** In every case the final event is "N_θ(p) has a divisor in a class". Seeds can only steer the choice of θ
  (H-D), and the experiment shows they do not even improve the odds.
* **B3.** (U) archimedean use is limited by Lemma A to power-sparse primes (Prop B). This is the scale constraint
  in its most literal form: the seed is exponentially larger than any solution.
* **B4/B6.** Not applicable. No averaging is used.
* **B5/T1.** (U) passes T1 at the first step (no unit at n = m²), and this is the only angle in this list with
  that property. It dies at B3 instead. (R) at odd squares: representations of m² exist (Pythagorean and
  trivial), so the failing step must be the slice event, as everywhere else.
* **T4.** (H) data: the 2-part of the class groups is genus/Rédei data (nonab memo). Odd parts give no handle.

## 6. Viability Assessment

**COLLAPSES**: (U) to B3 at the step "use the unit as a number" (Lemma A + Prop B); (U) residues, (R) and (H) to
B2 at the step "seed data decide the slice" (Prop C, nonab D1, EXACT_FORMULA Thm 5.2). By-products: Lemma A
(folklore), Prop C (elementary observation), and two EVIDENCE items (power-sparsity of small units; no seed effect
on slice success).

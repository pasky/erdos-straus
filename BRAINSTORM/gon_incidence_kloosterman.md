# Brainstorm O148(c): incidences, sum-product, Siegel/Thue, Kloosterman boxes, small-exponent moduli

ES is not solved; nothing here proves any case of it. Labels as in DISCOVERIES.md.

## 1. Idea and exact forms

All sub-ideas start from two compact forms (PROVED, elementary; from ET's parametrisation with b = ce − a):
* **Type I(p) ⟺ ∃ a,b,d ≥ 1 with (4abd − 1) | p(a+b)** (⇒: p(a+b) = pce = c(4abd−1). ⇐: 4abd−1 > a+b for
  a,b,d ≥ 1, so (4abd−1) ∤ (a+b) and hence p | 4abd−1; put e = (4abd−1)/p, then e | a+b, c = (a+b)/e).
  Equivalently: a point of the modular hyperbola 4abd ≡ 1 (mod p) whose quotient
  e = (4abd−1)/p divides a+b.
* **Type II(p) ⟺ ∃ a,b,d ≥ 1 with 4abd > p and (4abd − p) | (a+b)** (e = 4abd − p).
  Equivalently ⟺ ∃ a ≤ b such that r := (−p mod 4ab) satisfies 0 < r and r | a+b (since e ≤ a+b < 4ab
  forces e = r): a *fractional-part* statement, {p/(4ab)} = 1 − r/(4ab) with r | a+b.

Sub-ideas: (c1) existence of hyperbola points in boxes is a theorem (Weil/Kloosterman), so maybe ES follows
by adding the divisibility e | a+b; (c2) incidence bounds (Szemerédi–Trotter, Pach–Sharir, Bombieri–Pila) on
the curves above; (c3) sum-product existence theorems (Bourgain–Glibichuk–Konyagin: kH = 𝔽_q for multiplicative
subgroups H with |H| > q^δ); (c4) Siegel's lemma / Thue's lemma producing small auxiliary solutions;
(c5) "small-exponent moduli": in an e-slice, if G_e = (ℤ/e)^* has tiny exponent, the box condition of
`gon_lll_relation_lattice.md` becomes free.

## 2. Literature anchor (from memory unless marked)

Weil bound for Kloosterman sums and the resulting equidistribution of xy ≡ c (mod p) in boxes of side
≫ p^{1/2+ε} (standard; e.g. Shparlinski's survey on the modular hyperbola). Szemerédi–Trotter (1983);
Pach–Sharir (curves with k degrees of freedom); Bombieri–Pila (1989). Bourgain–Glibichuk–Konyagin, J. LMS 73
(2006). Thue's lemma; Siegel's lemma (Bombieri–Vaaler form). Lenstra/CHN as in memo (b).
The fractional-part form of Type II is in the spirit of POINTWISE_SIZE §4 item 1 ("E2" tests).

## 3. Barrier screen

**(c1) Kloosterman boxes — collapses to the moving modulus (H-A/B2).** For a dyadic box a ~ A, b ~ B, d ~ D
the number H₁ of hyperbola points is ≈ ABD/p with a Weil-type error, so H₁ ≥ 1 is a *theorem* once the box is
large. The extra condition e | a+b has a modulus e ≈ 4ABD/p that is a function of the point; it holds with
"probability" ≈ 1/e only when e ≤ a+b, i.e. AD ≲ p/4. The expected count per box is
Σ 1/e ≈ (ABD/p)·κ(p/4ABD) = κ/4 with κ = O(1) from averaging 1/e over the dyadic range of e (κ/4 ≈ 0.07),
*independent of the box*, times the fraction of points with e ≤ a+b — and halved again by genus (Lemma 1.2 of
LONGSHOT_PIGEONHOLE). So the Weil step is idle: it controls the fixed-modulus part (mod p), while all the
content is in a moving-modulus divisibility with expectation O(1) per box. Experiment (§4): boxes with ≥ 100
hyperbola points have no solution in ≈ 99 % of cases. **B3:** a box-wise certificate has main term ≤ 0.04
per box, so it must aggregate ≫ 1 boxes — H-A, no technology. **B5:** the Weil step holds verbatim at n = m²
(the hyperbola 4abd ≡ 1 (mod m²) is as populated); the failing step is "e | a+b", which is genus-forbidden at m².

**(c2) Incidence geometry — upper bounds only.** For fixed p the witnesses are lattice points on the curves of
Lemma 3.1 of memo (a) (hyperbolas XY = N_θ(p)), i.e. incidences of ℤ² with a family of curves. Szemerédi–Trotter,
Pach–Sharir and Bombieri–Pila *upper*-bound such incidences; lower bounds for incidences exist only for
structured (grid-like) configurations, where they come from explicit constructions, i.e. identities (B1).
By-product potential: none for existence; upper bounds on f(p) are a different (known, Browning–Elsholtz /
ET p^{3/5+o(1)}) problem.

**(c3) Sum-product existence — collapses to B4.** BGK-type theorems cover *all* of 𝔽_q by k-fold sums of a
subgroup H with |H| > q^δ. ES needs a *specific* element (0 ∈ D + D mod e, D = divisors of N, i.e. −1 ∈ D·D⁻¹)
with k = 2, and D is not a subgroup but a box in H_e (memo (b)). A theorem forcing a specific element of D+D
from structure alone is a Kneser/Cauchy–Davenport covering statement, which needs |D| linear in the index
(LONGSHOT_PIGEONHOLE Prop 1.4) — B4. Also |D| = τ(N) ≤ p^{o(1)}, so the hypothesis |D| > e^δ confines e to
e ≤ p^{o(1)}, a finite-looking set of small slices — B2 Thm 2.2(iii).

**(c4) Siegel/Thue — linear existence, bilinear target.** Thue's lemma gives |u|,|v| ≤ √m with u ≡ sv (m) for
every s; Siegel's lemma gives small solutions of underdetermined linear systems. The ES conditions are
bilinear-plus-divisibility (4abd ≡ 1 (p) is a hyperbola, not a line; e | a+b has a moving modulus). Linearising
(e.g. unknowns P = yz, S = y+z in (4x−p)P = pxS) leaves the condition "S² − 4P is a square", which on the 1-dim
solution lattice is again "a specific integer has a divisor in a class" (B2). Thue's lemma *does* produce
4ab ≡ s (p)-type points with a, b⁻¹ small, but b⁻¹ mod p small does not make b small.

**(c5) Small-exponent moduli — a finite set of slices.** If every prime ℓ | N has order ≤ 2v_ℓ(N)+1 in G_e
then Σ_e(N) = H_e (each factor {ℓ^t : |t| ≤ v_ℓ} is the whole cyclic group ⟨ℓ⟩), and the e-slice holds iff
−1 ∈ H_e: pure linear algebra/genus (PROVED, elementary). For squarefree N this needs exponent(G_e) ≤ 3, i.e.
G_e of exponent 2 (as −1 has order 2, exponent 3 is impossible), i.e. e | 24; with e ≡ 3 (4) only **e = 3**:
Type II(p) via e = 3 ⟺ (p+3)/4 has a prime factor ≡ 2 (mod 3) (for (p+3)/4 coprime to 3). Larger e need prime
powers in N or accept a box. Any fixed finite set of such slices fails infinitely often (B2 Thm 2.2(iii),
CONDITIONAL on H; e.g. the Type II e = 3 slice fails whenever all primes of (p+3)/4 are ≡ 1 (3); the Type I
e = 3 slice, N = (3p+1)/4, likewise). Moduli with small Carmichael λ(e) (Erdős–Pomerance–Schmutz) are
huge relative to N's few prime factors, so the box is not free there either. **Collapses to B1/B2.**

**B6/T7:** none of (c1)–(c5) averages over p; their failures are structural.

## 4. Experiment (`scripts/bs_gon_boxes.py`, ≈ 5 s)

Hard prime p = 20161 (≡ 1 (24), square class mod 840); dyadic boxes in (a, b, d) with a ≤ b-box, ad ≤ p,
b < 16p (resp. 128p): 1194 (1554) boxes contain hyperbola points (total 5.9·10⁶ (4.8·10⁷) points with
4abd ≡ 1 (p)); only 38 (39) Type I witnesses in total, ≤ 2 per box; among boxes with ≥ 100 hyperbola points,
685/694 (1034/1044) are empty. The naive Σ_{e ≤ a+b} 1/e predicts 74 (98), about twice the truth (genus factor ½,
Lemma 1.2). No box has expectation ≥ ½. EVIDENCE only: the witnesses sit at ≈ 0.03 per dyadic box, so no
box-wise argument can work, and Weil-controlled abundance of hyperbola points is irrelevant.

## 5. Viability Assessment

(c1) **COLLAPSES** to H-A/B3 at "e | a+b" (moving modulus, expectation O(1) per box, genus-killed at squares).
(c2) **COLLAPSES**: incidence theorems are upper bounds. (c3) **COLLAPSES** to B4 (specific element, k = 2, D not a
subgroup). (c4) **COLLAPSES** to B2 (bilinear + divisibility). (c5) **COLLAPSES** to B2 Thm 2.2(iii)/B1 (only e = 3
has a free box for squarefree N).
By-products (PROVED, elementary, folklore-level): the compact divisibility forms of §1, in particular the
fractional-part form of Type II, and the (c5) criterion Σ_e(N) = H_e when orders are small.

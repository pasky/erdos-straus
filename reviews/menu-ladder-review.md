# Review R255 of O245 (MENU_LADDER.md, memos BRAINSTORM/z18_*) — hostile review

Reviewer: R255 side agent (branch side-agent/review-menu-ladder, merged side-agent/menu-ladder at 7ecab42c).
From-scratch scripts: `scripts/review_r255_*.py`. ES is not solved; nothing below changes that.

**Repairs applied (author quiet):** D1–D11 applied directly in MENU_LADDER.md and memos z18_primes_slices, z18_real_place,
z18_exp_cover_criterion, each marked '(R255 repair)' / 'R255:'. D5 (MAJOR) repaired by withdrawing the finite-cover clause.

## Summary verdicts

| claim | verdict |
|---|---|
| Prop 1.1 (μ = 0 ∈ Ster iff θ(θ−1) ∈ (A⊗ℚ₂)^{×2}) | SOUND |
| Computation 1.2 (D = 2…10, six (c₀, k)) | SOUND (independently reproduced, different method) |
| Lemma 2.1 (specialisation) | SOUND |
| Lemma 2.2 (normal form) | SOUND |
| Lemma 2.3 (real place) | SOUND-AFTER-REPAIRS (minor: t = t′ case; label of consequence (ii)) |
| Prop 3.1 (witness localisation) | SOUND |
| Lemma 6.1, Theorem 6.2 (compactness, s₀ large) | SOUND |
| Prop 6.3 | SOUND (one implicit step, D6) |
| §6 "pointwise converse fails" | SOUND for the pointwise statement; GAP for the added finite-cover refutation (D5) |
| Prop 7.1 (slices collapse to ET) | SOUND-AFTER-REPAIRS (primitivity, D8) |
| §7 Answer (Assessment) | label appropriate |
| §5 searches (EVIDENCE) | labels appropriate; independently corroborated at D = 4 |
| §8 rung-2 s-deformation (PROVED, Type II) | SOUND |
| Cor 4.2 table | SOUND as labelled (inherits D7) |
| Theorem 4.1 (rung 2, Type II) | SOUND (shape analysis redone; from-scratch exhaustive-per-(a,b) search, 0 violations; negative control fires) |

## Claim-by-claim

### Prop 1.1 — SOUND
Re-derived against MENU_STERILITY Theorem A's definition of Ster(φ).
* φ = c₀Y^D + k is separable (c₀k ≠ 0), positive leading coefficient: Theorem A applies.
* (i): φ(Y*) = c₀ + k = 4^J is an ℓ-adic unit for ℓ odd; φ(Y*) = k ≡ 1 (8) in ℤ₂. ✓
* (ii) ⇒: γ(1 − θ) ∈ (A⊗ℚ_ℓ)^{×2} for all odd ℓ means, in each component field K, a local square at all places above
  odd primes, i.e. all finite places but finitely many. If it were not a square, K(√·)/K would be a quadratic extension with
  a positive density of inert primes (Chebotarev) — contradiction. So γ ∈ (1 − θ)A^{×2} (1 − θ is a unit of A since
  φ(1) = 4^J ≠ 0). ✓
* Real places: D even — none; D odd — the single real root −(k/c₀)^{1/D} < 0, where 1 − θ > 1. So every γ ∈ (1 − θ)A^{×2}
  is totally positive, and total positivity imposes nothing extra. ✓
* At ℓ = 2: γ(0 − θ) ∈ (1 − θ)(−θ)A^{×2}, so (ii) at 2 ⟺ θ(θ − 1) ∈ (A⊗ℚ₂)^{×2} (θ is a unit as φ(0) = k ≠ 0). ✓
* ⇐ with γ = 1 − θ. ✓   D = 1: θ(θ − 1) = k·4^J/c₀², a 2-adic square iff k ≡ 1 (8). ✓
* "Reading": for odd D the x − θ map J(ℚ₂)/2J(ℚ₂) → (A⊗ℚ₂)^×/□ is injective (odd-degree model), and the image of
  P₁ − P₀ is (1 − θ)/(−θ) ≡ θ(θ − 1) mod squares, so the [P₁ − P₀] ∈ 2J(ℚ₂) reading is correct. The heuristic sentence
  has a wrong formula (D1 below).
* Hand check D = 2, c₀ = 15 re-done: (−7)² = 49 ≡ −15 (mod 64) so σ ≡ −7 (mod 32) is consistent; v₂(1 + σ) = 1,
  v₂(1 − σ) = 3, sum 4 = v₂(1 − σ²) = v₂(16). ✓

### Computation 1.2 — SOUND (CERTIFIED label acceptable)
`scripts/review_r255_descent.py` uses a method independent of the author's `nfislocalpower`: β is a square in K_𝔭 iff
β is a global square (nffactor of x² − β) or 𝔭 splits in K(√β)/K (`rnfidealprimedec`, two primes above 𝔭). The integral
representative c₀²·θ(θ − 1) = η(η − c₀) (η = c₀θ, monic model) is used. In all 6 × 9 cases φ is irreducible over ℚ.
Output (per prime above 2): every D ∈ 2…10 for every pair has at least one NS; the square components are exactly the ones
the author reports (D = 9: one sq component for all six pairs; D = 4: one sq for (63,1), (31,33), (7,57)); D = 1 is
square for all six (Schinzel). Full agreement with Computation 1.2.

### Lemma 2.1 — SOUND
R = R₁/N. Odd ℓ^e ∥ N: on s/D ≡ 0 (mod ord_{ℓ^e} 2), Y ≡ 1 (ℓ^e), so R₁(Y) ≡ R₁(1); 2^e ∥ N: for s/D ≥ e, Y ≡ 0 (2^e).
Sufficiency and necessity both follow (the class s ≡ 0 (L), s ≥ s₀ contains s with s/D divisible by any given order and
arbitrarily large). Only classes s ≡ 0 (mod L) have μ = 0 in their closure, so "clopen neighbourhood" = such a class. ✓

### Lemma 2.2 — SOUND
1/(abd) + 1/(acdn) + 1/(bcdn) = (cn + a + b)/(abcdn) = 4/n ⟺ cn + a + b = 4abcd. With m = 4abd − n: a + b = c·m. ✓
With a = λ, σ = c/λ (a polynomial in general), T = 4λ²d, T′ = m: b = cm − λ = λ(σT′ − 1), 4abd = T(σT′ − 1) = n + T′, so
n = σTT′ − T − T′; f = 4acd − 1 = σT − 1. Converse: d := T/(4λ²), c := σλ, b := λ(σT′ − 1) satisfies the relation. ✓
(Wording: "gives a family" means a polynomial identity; integrality/positivity of b (needs σT′ > 1 eventually) is separate.)

### Lemma 2.3 — SOUND-AFTER-REPAIRS (minor)
n(t) = −T′(t) at T(t) = 0 and n(t′) = −T(t′) at T′(t′) = 0 are immediate from n = σTT′ − T − T′. T = 4λ²d and T′ = m =
(a + b)/c have positive leading coefficients. Largest real root t* of TT′ (say of T): T′(t*) ≥ 0, so n(t*) ≤ 0; for even D
(n > 0 on ℝ) impossible ⇒ no real roots. For odd D, n is increasing, so t* ≤ the real root of n. ✓
Consequence (i), odd D: with roots t ≠ t′, n(t) and n(t′) have signs inconsistent with monotonicity ✓; the case t = t′
(then t is the real root of n) is not addressed — see D2. Consequence (ii): for even D it is immediate from the lemma (m
linear has a real root); for odd D it is only grid EVIDENCE but sits inside a "PROVED" lemma — see D3.

### Theorem 4.1 — SOUND
Re-derived independently.
* m = 4abd − n = (a + b)/c, lc(m) > 0. deg(abd) < 2 ⇒ lc(m) = −c₀ < 0 ✗. deg(abd) > 2 ⇒ deg a + deg b + deg d =
  max(deg a, deg b) − deg c, so (say deg a ≥ deg b) b, c, d are constants and a(4bd − 1/c) = n + b/c with deg a > 2 forces
  4bcd = 1 and n = −b/c ✗. So deg(abd) = 2, deg m ≤ 2. ✓
* Key identity (not stated by the author, but it is what makes "witness ≡ constant" meaningful and handles the a ↔ b
  mirror shapes): (4acd − 1)(4bcd − 1) = 4cd(4abcd − a − b) + 1 = 4c²dn + 1 ≡ 1 (mod n). Hence f is a unit mod n, and f is
  ≡ a constant iff 4bcd − 1 is — so the reduction "up to a ↔ b" is legitimate (D4).
* deg m = 2 ⇒ max(deg a, deg b) ≥ 2 + deg c, so shape (2,0,0), c constant; a(4bcd − 1) = cn + b gives
  f ≡ 4bcd/(4bcd − 1) − 1 = 1/(4bcd − 1) (mod n). ✓
* deg m ≤ 1: (0,0,2) c, m constant, f ≡ cm/b − 1 ✓; (2,0,0) m constant ⇒ f ≡ const ✓, m linear ⇒ −4b²d = n(Y₀) > 0 ✗ ✓;
  (1,1,0) ✓; (1,0,1) ✓ (each uses n > 0 on ℝ, i.e. c₀, k > 0, at a rational real root). The list of (deg a, deg b, deg d)
  with sum 2 up to a ↔ b is complete. ✓
* Final step: f − f₀ = n·h in ℚ[Y]; clearing denominators, (f(Y)/n(Y)) = product of fixed Jacobi symbols (q/n(Y)), q ∈
  {−1, 2, odd primes}; near μ = 0, n ≡ 1 (8) and n ≡ 4^J mod every fixed odd q, so each symbol is +1 (reciprocity), against
  the Type II witness value −1 (NEAR_SQUARE Lemma 1.3; f₀ ≠ 0 by the key identity). ✓
* `scripts/review_r255_rung2.py` (from scratch; for each (a, b) it finds ALL (c, d) ∈ ℚ[Y]: m runs over positive multiples of
  monic divisors of a + b, the multiple forced by 4ab | n + m): (15,1) deg a, b ≤ 2, |coeff| ≤ 2, lc ∈ {1,2}, scalars
  {1, 2, 1/2, 3, 1/3, 1/4, 4}: 2156 families, shapes only (0,0,·,2,0), (2,0,·,0,2), (2,0,2,0,0) and mirrors; (3,1) deg a ≤ 3,
  deg b ≤ 1: 1372; (7,9) deg a, b ≤ 3, |coeff| ≤ 1: 588. **0 violations** (deg(abd) = 2 always, f mod n constant always).
  Negative control n = Y² − 3 (indefinite): 3710 of 8414 families have non-constant witness, shapes (1,1,·), (1,0,1), …
  appear — so the search can detect escapes and positivity is indeed the operative hypothesis.

### Prop 3.1 — SOUND
* First form: in Theorem A's proof, (D̃(u)/φ(u)) = Π_{v∈S∪∞}(α, u − θ)_v; letting u → Y*, the odd S-places see 1 − θ and
  the 2-places see −θ. The product formula for (α, 1 − θ) (unit outside S, since N(1 − θ) = ±4^J/c₀ and c₀ ∈ S) moves the
  odd-S part to the 2-places and real places; real symbols are 1 (1 − θ, u − θ > 0). So (f(u)/n(u)) = Π_{v|2}(α, θ(θ − 1))_v
  (the denominator g contributes (g/n) = +1). This first form needs neither k = 1 nor c₀ squarefree. ✓
* Second form: real place (D odd) θ_r < 0 ⇒ β > 0 ✓. q | c₀ (q ∥ c₀): ϖ = 1/θ is a root of x^D + c₀, Eisenstein, so
  A⊗ℚ_q is a totally ramified field; β = ϖ^{−2}(1 − ϖ); the tame symbol is ((αϖ^{−v(α)})^{−2}(1 − ϖ)^{−v(α)} mod 𝔮 / 𝔮) = 1. ✓
  Other odd v: θ is a unit (N θ = ±1/c₀) and θ − 1 is a unit, so (α, β)_v = (β/v)^{v(α)}. ✓
* From-scratch `scripts/review_r255_witness.py` (own Type II decomposition of Theorem B: a = 3, b = 2X² + 2X + 1,
  d = 2X² − 2X + 1, c = 2(X² + X + 2)/11, identity checked): W = −1 with parts (2: −1, c₀: +1, other odd: −1); constant
  sign changed: all +1. Matches the memo. (Observation: replacing f by −f never changes W here, since (−1, β) is trivial
  at all places other than 2 — so W does not see the overall sign of the witness.)

### Lemma 6.1 / Theorem 6.2 — SOUND
* (μ − r)/D ∈ (L/D)Ẑ, and x ↦ b^x extends continuously from ℤ to Ẑ in ℤ_ℓ^× (ℓ ∤ b); at ℓ | b, Y → 0 as s → ∞. Integrality
  of R₁(Y*)/N is a clopen condition, so V_F is clopen. ✓
* ⇐: Λ compact, finitely many D_q, V_F cover it. An integer s ∈ V_F gives integrality at the actual Y = b^{(s−r)/D} only once
  Y ≡ 0 mod ℓ^e for ℓ^e ∥ N, ℓ | b, i.e. s large — so s₀ must be chosen AFTER the finite subcover (max of these depths and of
  the positivity thresholds). The repaired wording "for some sufficiently large s₀" is exactly right; the statement is
  "∃ s₀ ∃ finite cover of {n_s : s ≥ s₀} ⟺ condition". ✓
* ⇒: for μ ∈ Λ take s_j → μ, s_j → ∞; infinitely many s_j in one class; D_q closed ⇒ μ ∈ D_q; or F integral at infinitely
  many actual Y_j → Y*(μ), integrality closed ⇒ μ ∈ V_F. ✓ ET classes are degree-1 root classes. ✓

### Prop 6.3 — SOUND
Theorem A needs a family valid on a full residue class of u, while the root class is a priori only valid on the sparse set
u = b^{(s−r)/D}. This is fine but should be said: if μ ∈ V_F then R₁(Y*) ≡ 0 (mod N) for every parameter, so F is integral
on the whole class u ≡ Y* (mod N) (any modulus N clearing all denominators), positive for large u, and the closure of that
class contains Y*. Theorem A applied to φ_{D,r}(u) = c₀b^r u^D + k gives the claim. (S_D depends on (r, L) through φ_{D,r};
notation only.) See D6.

### §6 "pointwise converse fails" — SOUND (pointwise), GAP (finite-cover add-on)
* For 15·4^s + 1, the base-4 degree-D menu uses the same φ = 15Y^D + 1 and the same Y* as Computation 1.2, so μ = 0 ∉ S_2,
  S_4 ✓; n → 16 at odd q, so μ = 0 ∉ ∪D_q ✓; O239 Cor 2.8 (branch side-agent/exp-105, under review; scope "z14 menu, unsplit
  pieces") says no window reaches μ = 0. So the POINTWISE converse fails for that sub-menu ✓, conditional on Cor 2.8.
* The rung-2 Type II counterexample (Theorem 4.1 + Computation 1.2 at D = 2) is correct. ✓
* GAP: "and since μ = 0 ∈ Λ, this also refutes the finite-cover equivalence for that menu". The naive finite-cover
  equivalence is "covering ⟺ Λ ∩ (∩_D S_D) ⊆ ∪_q D_q". Absence of a covering (O239) refutes its ⇐ direction only if
  Λ ∩ (∩_D S_D) \ ∪D_q = ∅, i.e. if NO other μ ∈ Ẑ lies in every S_D. Only μ = 0 is examined. Since ∩S_D ⊆ S_1 =
  unit-square points, it would suffice that μ = 0 is the only unit-square point of 15·4^μ + 1. EVIDENCE for that
  (`scripts/review_r255_s1points.py 15 1 …`): the QR constraints from the primes of 4^60 − 1 already force μ ≡ 0 (mod 60);
  mod 2^a the survivors are {0, 3, 19}, killed by μ ≡ 0 (mod 10). This is not a proof for all moduli. See D5.

### Prop 7.1 — SOUND-AFTER-REPAIRS
On P_e, g ≡ 2^e, so F is a polynomial-in-n identity on the progression n ≡ 1 + 2^e u₀ (mod 2^{e+1}M) (M odd). Near the
unit-square point this class contains a square coprime to its modulus (mod M: ≡ 4^J; mod 2^{e+1}: 1 + 2^e ≡ 1 (8) is an odd
square for e ≥ 3). ET p. 8 (checked in sources/elsholtz-tao-1107.1010.pdf): "a primitive congruence class n = r mod q which is a
perfect square cannot be solved by polynomials ([44], [68]; also follows from Proposition 1.6)"; ET Prop 1.6 (vanishing of
f_I, f_II at odd squares) is quoted correctly. ✓ But the general sentence "P_e must contain no odd square" is false as
written — non-primitive classes containing odd squares ARE polynomially solvable (n ≡ 0 (mod 3) ∋ 9: 4/n = 1/(n/3) +
1/(4n/3) + 1/(4n)). In the application the squares are units, so the proof is fine. See D8.

### §5 — labels appropriate
All §5 statements are EVIDENCE with stated ranges, and the coverage caveats (skipped underdetermined/zero-resultant systems,
reduced residue only) are disclosed. Hand checks: σ = 4/11 at D = 4: 4(15Y⁴ + 1) + 11 = 15(4Y⁴ + 1) ✓; no κ | 75 with
κ ≡ −1 (mod 176) ✓. Independent corroboration with a different search shape (`review_r255_rung2.py c0 k 2 2 2 4`: for each
small (a, b), ALL Type II (c, d) ∈ ℚ[Y] on c₀Y⁴ + k, then x, y, z tested by Lemma 2.1 at μ = 0): (3,1) finds 8 integral
families, all O240 Theorem B and rescalings/mirrors (sanity ✓); (15,1): 2352 algebraic Type II families, **0 integral at
μ = 0**. Consistent with "Status of 15·2^s + 1: NOT decided" — correctly not overclaimed.

### §8 rung 2 under s-deformation — SOUND
An identity in s and 2^{s/2} on an infinite progression holds in ℚ[s, Y] (exponential polynomials vanishing on an AP vanish).
Positivity of P(s, 2^{s/2}) for large s forces the top Y-coefficient (in ℚ[s]) to be eventually positive, so for each fixed
large s Theorem 4.1's hypotheses hold in Y (degrees in Y are eventually constant). Remainders mod n (n s-free with constant
leading coefficient) lie in ℚ[s]; F·G = 1 by the key identity of D4, so F is constant. ✓ "Higher rungs": Assessment, fine.

### Cor 4.2 / Assessment
The table is labelled row by row. Base-4 results (O239, 15·4^s + 1) are used for the base-2 family 15·2^s + 1; this is legitimate
for non-existence near μ = 0 (restrict a base-2 class near μ = 0 to even s), but deserves a word (D9). The "fourth kind
(positivity) of obstruction" reading in the memo is an Assessment and is supported by the negative control in my rung-2 search
(indefinite n gives escaping witnesses).

## Defects

1. (MINOR) §1 "Heuristic" line: "J(ℚ₂)/2J(ℚ₂) has order ≈ 2^{g + #J[2](ℚ₂)}" is wrong. The correct formula is
   #J(ℚ₂)/2J(ℚ₂) = #J(ℚ₂)[2] · 2^g (since |2|₂^{−g} = 2^g). Also at D = 2 the curve is a conic (g = 0, trivial Jacobian),
   so the "J" reading does not apply literally there (even-degree model; the obstruction is the x − θ class of P₁ vs P₀
   in A^×/A^{×2}ℚ₂^×-type quotient). Repair: correct the formula and say "Heuristic (D odd)".

2. (MINOR) Lemma 2.3 consequence (i), odd D: the case t = t′ (common root, then the real root of n) is omitted. Repair: it
   would make −(k/c₀)^{1/D} rational, i.e. k = gu^D, c₀ = gv^D; then g(u^D + v^D) = 4^J with g, u, v odd and D odd gives
   u^D + v^D = (u + v)·(odd) = 2^{2J}/g ⇒ the odd cofactor is 1 ⇒ u = v = 1 ⇒ 2g = 4^J, impossible for odd g. (Or simply
   restrict (i) to the standing hypotheses and add this line.)
3. (MINOR) Lemma 2.3 consequence (ii) is labelled under "PROVED" but for odd D it is only the grid count (EVIDENCE); for
   even D it is a one-line corollary of the lemma (m linear has a real root), which makes the D = 4 sentence about
   b = Y² + pY + q redundant. Repair: "(ii) for even D PROVED (m linear has a real root); for odd D EVIDENCE (grid)".
4. (MINOR) Theorem 4.1 proof: "the four shapes up to a ↔ b" silently uses that the witness is not a ↔ b symmetric. Repair:
   add the identity (4acd − 1)(4bcd − 1) = 4c²dn + 1, so f ≡ const ⟺ 4bcd − 1 ≡ const (mod n); it also shows f₀ ≠ 0.
5. (MAJOR — overclaim inside a PROVED paragraph) §6, "…this also refutes the finite-cover equivalence for that menu".
   Unproven: needs that no μ ≠ 0 in Λ lies in ∩_D S_D \ ∪_q D_q (e.g. that μ = 0 is the only profinite unit-square point
   of 15·4^μ + 1). Repair: delete the clause, or replace by "(the finite-cover equivalence would also fail if μ = 0 were the
   only unit-square point of 15·4^μ + 1 — EVIDENCE: forced mod 60 by the primes of 4^60 − 1, R255)". Same caveat for the
   memo z18_exp_cover_criterion "counterexamples to the naive converse": say "pointwise".
6. (MINOR) Prop 6.3: make explicit the passage from the sparse set u = b^{(s−r)/D} to a full residue class
   u ≡ Y* (mod N) (Theorem A is stated for residue classes), and note S_D = S_{D,r} depends on the class through
   φ_{D,r} = c₀b^r Y^D + k.
7. (MINOR) §6 / Cor 4.2 cite O239 Cor 2.8 as PROVED; it lives on side-agent/exp-105 (under review) and is stated for the
   z14 menu with UNSPLIT SG pieces. Repair: add "(O239 Cor 2.8, unsplit pieces; pending review)".
8. (MINOR) Prop 7.1 proof: "P_e must contain no odd square" — must read "no odd square coprime to the modulus (P_e is then a
   primitive square class)"; counterexample to the literal sentence: n ≡ 0 (mod 3). The application is unaffected.
9. (MINOR) Cor 4.2 table / §5 quote O239 results proved for 15·4^s + 1 (base 4) as statements about 15·2^s + 1. Add one
   line: a base-2 class near μ = 0 restricts to a base-4 class near μ = 0 (s ↦ 2s), so base-4 non-existence implies base-2
   non-existence for the corresponding sub-menu.
10. (MINOR) Memo z18_primes_slices "Result (PROVED…)": "(n, Y)-polynomial families can escape Schinzel only where u is
    frozen or thin, i.e. on density-0 sets" goes beyond Prop 7.1 (which only covers valid sets containing a FULL slice
    progression). Repair: move that sentence to the Assessment section.
11. (MINOR) Reproducibility: MENU_LADDER Lemma 2.3 (ii) and memo z18_real_place cite "0 of 5041–33489 grid points pass
    positivity" from "the POS counter in the debug copy" of `z18_quad.py`; the committed script has no positivity counter.
    Repair: commit the counter or drop the numbers (for even D the statement is proved anyway, D3).

## Overall assessment
No FATAL defects. The mathematical core — Prop 1.1, Computation 1.2, Lemmas 2.1–2.3, Prop 3.1, **Theorem 4.1**, Thm 6.2,
Prop 6.3, Prop 7.1 (narrow), §8 rung 2 — re-derives correctly; Computation 1.2 and Theorem 4.1 are independently reproduced
from scratch (different 2-adic method; exhaustive-per-(a, b) Type II search with a firing negative control). One MAJOR
overclaim (D5: the finite-cover refutation in §6 is unproven; the pointwise refutation stands), the rest are MINOR wording /
scope / reproducibility issues. Labels in §5, §7 (Assessment), Cor 4.2 are appropriate. ES is not solved; 15·2^s + 1 remains
undecided, as the document correctly says.

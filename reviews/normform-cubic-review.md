# R259 — hostile review of O248 (NORMFORM_CUBIC.md, BRAINSTORM/z20_*.md, AGENT_REPORT_O248)

Reviewer: R259 side agent (branch side-agent/review-normform, merged side-agent/normform-cubic at 7f070f22).
From-scratch scripts: `scripts/review_r259_identities.py` (sympy: every rearrangement in Thms 1.1′/1.2′/3.1),
`scripts/review_r259_search.py` (python-flint exact brute-force search for Type I/II families over 9 forms incl. controls).
Status: IN PROGRESS (written claim by claim).

## Verdict table
(filled in below, claim by claim)

## Claim-by-claim

### Thm 1.1′ (Type II, P* irreducible, valid at one point) — SOUND
Re-derived independently. Setting check: "leading form" P* is the top-degree homogeneous part (§1 "Setting"), and the
hypothesis is irreducibility of P* over ℚ, not of P. Note P* irreducible ⇒ P irreducible (P = FG ⇒ P* = F*G*), not
conversely. Steps:
* s ≤ max(α, β, γ + k) and case (a) (s ≤ α ⇒ β = γ = δ = 0, A(4BCD − 1) = B + CP, 4BCD = 1 impossible as CP non-constant):
  correct.
* (b): if γ + k > s the top C*P* survives (no other term reaches that degree), if γ + k < s the RHS has degree < s; so
  4A*B*D* = P* with α + β + δ = k. (F1) for a 3-fold product: grouping two factors, at most one of A*, B*, D* has positive
  degree, so exactly one has degree k. Correct.
* (b1) C(4ABD − P) = A + B, A + B ≠ 0 ⇒ deg C + deg(4ABD − P) = 0. Correct.
* (b2) the identity E(4BDC − 1) = P + 4B²D is verified symbolically (review_r259_identities.py). If deg E ≥ 1 then
  deg C = k − deg E ≥ 1 and E*·4BD·C* = P* with both factors of positive degree: contradicts (F1). Correct.
* The positivity remark ("used only through A + B ≠ 0") is correct; with A + B = 0 the never-valid family
  A = −B = κ, D = −P/(4κ²), C arbitrary is the only escape (case (b1)), as in the degree-2 Remark.
Edge cases (from-scratch search, see §Numerics): for P irreducible with P* reducible the conclusion FAILS —
P = 4uv − u − 1 has the valid Type II family (A, B, C, D) = (u, 1, 1, v) (n = 4uv − u − 1, 4uv = u + 1 + n), not in ℚ[P].
So irreducibility of the *top part* is the hypothesis that does the work; irreducibility of P alone is not enough. The
hypothesis is sufficient, not necessary: P = v + u² (P* = u² reducible) also collapses, trivially, since ℚ[u, v] = ℚ[P][u]
and a u-degree count over the domain ℚ[P] kills u-dependence (reviewer's argument; search confirms).

### Thm 1.2′ (Type I, P* irreducible, valid on a lattice coset in an open cone) — SOUND-AFTER-REPAIRS (minor)
Re-derived every case; all algebraic rearrangements verified symbolically (review_r259_identities.py: (c1) B/C/D cases,
(c2) μ = k expansion incl. the "P²-coefficient" step).
* The "coefficient of P²" step in (c2) μ = k is not a coefficient comparison in a polynomial ring in P (E_A, E_B ∉ ℚ[P]);
  it is a degree argument: (4CDκκ′ − κ − κ′)P² has degree 2k while P·G and C − 4CD·E_A·E_B have degree ≤ 2k − 1. Correct,
  but should be said (MINOR D3).
* (c1) B-case: E* | P*² ⇒ E* = λP*^i by unique factorisation (P* prime), 0 < deg E* < k impossible. Correct; this is
  genuinely degree-free (the degree-2 proof's "Q on a rational line" is replaced correctly).
* (c2) 0 < μ < k: γ, δ ≤ k − μ < k, μ < k, so P* divides a product of forms of degree < k. Correct.
* Positivity paragraph: it says every coordinate "is positive" at valid points. Validity (POINTWISE_BINARYFORM §1) allows
  the sign pattern (A, B, C) < 0 < D; the R256 repair to SYNTHESIS_SPARKS7 Thm 1.2 handles it by the dilation
  (A, B, C) ↦ −(A, B, C) (preserves the Type I identity and the conclusion). That repair was not carried over (MINOR D1).
* The cone/direction argument needs L to be a coset of a *full-rank* sublattice of ℤ^r (otherwise L need not have points
  tending to infinity in an open set of directions). Implicit; state it (MINOR D2).
Edge case: P irreducible, P* reducible — the conclusion FAILS: P = 4u² − 4v² − 1 (P* = 4(u − v)(u + v)) carries the Type I
family (A, B, C, D) = (u − v, u + v, 2u, 1), valid on the open cone u > |v| (e.g. (u, v) = (1, 0): n = 3,
4/3 = 1/(abdn) + 1/(acd) + 1/(bcd) = 1/3 + 1/2 + 1/2), and not in ℚ[P]. So again P* irreducible is the operative
hypothesis. (Search found 18 such non-ℚ[P] families, all with valid points.)

### Thm 3.1 (Type I unit-group criterion, valid at one point) — SOUND
Re-proved line by line; all five rearrangements and the degenerate family re-verified symbolically from scratch
(review_r259_identities.py, "3.1" lines).
* Dichotomy. (e0) P ∤ 4ABD − 1 ⇒ (P prime, P | C(4ABD − 1)) P | C, and C/P·(4ABD − 1) = A + B, so 4ABD − 1 | A + B.
  Degree count deg(4ABD − 1) = α + β + δ ≤ deg(A + B) ≤ α gives β = δ = 0; then C/P = λ is a constant (both sides have
  degree α ≥ 1) and A(1 − 4λbd) = λ + b: either A constant (contradiction) or 4λbd = 1, λ = −b, d = −1/(4b²), C = −bP.
  Correct. (e1) P | 4ABD − 1 ⇒ A, B, D units of ℚ[x]/(P) ⇒ constant mod P (this is the ONLY use of the unit hypothesis).
  H ≠ 0 (else A + B = 0), β + δ ≤ k, and a non-constant B ≡ b has β ≥ k: correct; (β, δ) ∈ {(0,0), (k,0), (0,k)} with
  B − b, D − d of degree exactly k, hence κP. Correct.
* Sub-cases (i)–(iii), including A₁ = 0 (A = a constant; then (i) has H = 0, excluded; (ii)/(iii) have H constant and
  C = (A + B)/H ∈ ℚ[P]): correct. In (ii)/(iii) with α > k, deg H = α forces C = G constant; the brackets
  4dGb + (4dGκ − 1)P and 4bGd + (4bGκ − 1)P are non-zero (G ≠ 0 as A + B ≠ 0, and b, d ≠ 0); then A₁ ∈ ℚ(P) ∩ ℚ[x].
  Correct. ℚ(P) ∩ ℚ[x] = ℚ[P] (root τ of g, P − τ has a ℚ̄-zero as P is non-constant): correct.
* Degenerate families are never valid: validity forces abd, acd, bcd > 0, hence d > 0 and a, b of one sign
  (POINTWISE_BINARYFORM §1), excluding D = −1/(4b²) < 0 and A + B = 0. Correct. Note validity is used ONLY to exclude the
  degenerate list, so the theorem is really "every non-degenerate Type I family lies in ℚ[P]".
* What "(ℚ[x]/(P))^× = ℚ^×" covers (checked): (1) every homogeneous prime P — ℚ[x]/(P) is an ℕ-graded domain with degree-0
  part ℚ, and in a graded domain a unit's lowest and highest components multiply to 1, so units are homogeneous of degree 0;
  correct. (2) MORE: every P with irreducible top part P* (homogeneous or not): the initial ideal of (P) for the degree
  filtration is (P*), so gr(ℚ[x]/(P)) = ℚ[x]/(P*) is a graded domain and σ(f)σ(g) = σ(fg) = 1 forces filtration degree 0
  (reviewer's argument). E.g. P = u² − 2v² − 1 qualifies (also directly: over ℚ̄ the ring is ℚ̄[t, t⁻¹], t = u + v√2, and
  Galois sends t to t⁻¹, so only constants descend). Hence Thm 3.1 subsumes Thm 1.2′ *entirely*, not only "for
  homogeneous prime P" as Cor 3.2(c) says (MINOR D4: understatement). (3) NOT covered: one-variable P of degree ≥ 2
  (ℚ[u]/(φ) is a field / étale algebra, every non-zero-divisor is a unit — consistent with O145 Prop 3.4's one-variable
  families outside ℚ[P]); P with split top part such as 4u² − 4v² − 1, where u − v is a unit mod P.
* Necessity of the unit hypothesis (from-scratch control): P = 4u² − 4v² − 1 is prime, has units u ± v mod P, and carries
  the valid non-ℚ[P] Type I family (u − v, u + v, 2u, 1) (search: 20 non-collapsing Type I families, all valid somewhere).
  So the unit criterion is sharp in the sense that dropping it breaks the conclusion.
* Brute force (review_r259_search.py; A ≤ B, D ∈ S, |S| = 215 polynomials c₀ + linear(±1, 0) + κP, c₀ ∈
  {0, ±1, ±2, ½, ¼, −¼}, κ ∈ {0, ±1}; C by exact division): for u³ + 2v³, u² + v², u² − 2v² − 1, u² + v: 875 Type I
  families each, 299 in ℚ[P], the other 576 are exactly the theorem's degenerate list, 0 others. Exactly as Thm 3.1 predicts.
  (The author's random search found no Type I family at all; this search is the informative complement.)

### Cor 1.3′ and Cor 3.2 / the combined claim "every polynomial ET family for any norm form (any degree, any signature) or any irreducible binary form, valid anywhere, is an ET identity in n" — SOUND-AFTER-REPAIRS (scope wording)
* Scope check of the two ingredients: Type II needs P* irreducible (Thm 1.1′); Type I needs P prime with constant units
  (Thm 3.1). A *full* norm form N(x) = N_{K/ℚ}(Σ x_iω_i) (ω a ℚ-basis of K) and an irreducible binary form are homogeneous
  and irreducible, so both hold. Irreducibility proof in Cor 1.3′ re-checked: the k linear forms L_σ = Σ x_iσ(ω_i) are
  pairwise non-proportional (det(σ(ω_i)) ≠ 0), a ℚ-factor is c·Π_{σ∈S} L_σ with S Galois-stable by unique factorisation
  over ℚ̄, and transitivity forces S = ∅ or all. Correct.
* "Polynomial ET family" = quadruple (A, B, C, D) ∈ (ℚ[x] ∖ 0)⁴; the sextuple families of POINTWISE_BINARYFORM §1 are a
  special case, so the claim covers them. Not covered (and correctly excluded in Cor 3.2(c)/report): rational-function
  families and (x, y, z)-families whose ET coordinates are not polynomial.
* "ET identity in n": A = f_A(N) etc. with f ∈ ℚ[t]; since N is non-constant (transcendental over ℚ) the identity holds in
  ℚ[t]. Correct.
* MINOR D5 (scope wording): "every norm form N of every number field" (Cor 3.2, report) must mean the FULL norm form in
  [K:ℚ] variables (or any form that is irreducible over ℚ). Incomplete norm forms can be reducible:
  N_{K/ℚ}(x + y√2) for K ⊋ ℚ(√2) of degree 4 equals (x² − 2y²)², which is not prime — then neither theorem applies
  (and Thm 3.1's ℚ[x]/(P) is not a domain). Binary cubics such as x³ + 2y³ are covered as "irreducible binary forms".
* Cor 3.2(b) (POINTWISE_BINARYFORM §4.3 settled for polynomial ET families): correct as stated — §4.3 asks whether a
  family can be valid on a cusp; for polynomial ET families validity at a single point already forces ℚ[Q]. Rational
  families in cusps remain open (the report's spark says so).
* Cor 3.2(c): "Thm 1.2′ is subsumed for homogeneous prime P" — true, and in fact for every P with irreducible top part
  (see D4 above).

### Lemma 2.1 (orbit finiteness via Skolem–Mahler–Lech) — SOUND-AFTER-REPAIRS (minor)
* Finiteness of solutions of 4/n and finite-to-one-ness of (x, y, z) ↦ ET coordinates (a, b, c, d all divide x, y or z,
  so are bounded): correct; the latter should be stated (MINOR D6a).
* e(j) = F_i(ε^j x₀) − c is a constant-coefficient exponential polynomial in j with non-zero roots (products of
  σ_s(ε)); SML on j ≥ 0 or j ≤ 0 (one of them has infinitely many zeros) gives an infinite progression; vanishing on
  {qi + r : i ≥ 0} ⇒ all grouped coefficients vanish ⇒ vanishing for all i ∈ ℤ. Correct.
* Orbit closure: the orbit map g ↦ g·y is a morphism, so closure(⟨ε^q⟩)·y ⊂ closure(⟨ε^q⟩y), and closure(⟨ε^q⟩) has
  finite index in closure(⟨ε⟩), hence contains T_ε. Correct.
* Cubic K: with N(ε) = 1, T_ε ⊂ T = R¹_{K/ℚ}𝔾_m; X(T) ⊗ ℚ = (permutation module on 3 embeddings)/(trivial), ℚ-irreducible
  for C₃ (≅ ℚ(ζ₃)) and S₃ (standard rep); ℚ-subtori ↔ Galois-stable quotients, so T_ε = T. T acts simply transitively on
  the irreducible {l₁l₂l₃ = n/c}; N − n is irreducible over ℂ, so (N − n) | (F_i − c). Correct.
  The leftover "(N(ε) = ±1; replace ε by ε²)" in the proof contradicts nothing but is redundant since the statement now
  assumes N(ε) = 1 (MINOR D6b).
* From-scratch numerical check (review_r259_orbit_closure.py): K = ℚ(∛2), ε = ∛2 − 1 (N(ε) = 1), x₀ ∈ {(1,0,0), (1,1,0),
  (3,1,1)} (n = 1, 3, 15), sub-progressions q ∈ {1, 2}: the polynomials of degree ≤ D (D = 3, 4, 5) vanishing on 60 orbit
  points are exactly (N − n)·(degree ≤ D − 3) (dimensions 1, 4, 10); same for ℚ(√2), ε = 3 + 2√2. Consistent with
  "Zariski closure of any infinite sub-progression of the orbit = {N = n}".
* Scope: the lemma is stated for cubic (and real quadratic) K only; for degree ≥ 4 with intermediate fields (e.g.
  K ⊃ ℚ(√2), ε = 1 + √2 with N_{K/ℚ}(ε) = 1) T_ε is a proper subtorus and the conclusion fails. The text correctly restricts.

### Cor 2.2 (orbit-tail families collapse) — SOUND-AFTER-REPAIRS (minor)
* Jacobian step (dF_i ∧ dN vanishes on the Zariski-dense union of infinitely many level sets ⇒ algebraic dependence),
  N − t irreducible over ℚ(t)‾ (linear in l₁ with coprime coefficients), ℚ(N) algebraically closed in ℚ(x), and
  ℚ(N) ∩ ℚ[x] = ℚ[N]: correct. (I could not check the exact section of the Schinzel citation; the statement used —
  "N − t absolutely irreducible over ℚ(t) ⇒ ℚ(N) algebraically closed in ℚ(x)" — is standard and easy: if F is algebraic
  over ℚ(N) then ℚ(N, F) is a finite extension inside ℚ(x), and the generic fibre N = t, being geometrically irreducible,
  forces degree 1.)
* MINOR D7a ("several units" is needed): "one unit orbit" for a totally real cubic is an orbit of a rank-2 group; infinitely
  many valid points there need not lie in a single cyclic orbit (e.g. ε₁^j ε₂^{j²}·x₀). The text calls Laurent's theorem
  "Not needed below", but Cor 2.2 needs it in that case (or restrict the hypothesis to a cyclic orbit). Laurent's theorem
  (zero sets of constant-coefficient exponential polynomials on ℤ^d are finite unions of cosets) — Astérisque 147–148:
  source NOT accessed by the reviewer; the statement is the standard one (equivalent to the S-unit theorem setting).
* MINOR D7b: Cor 2.2 is stated for "infinitely many primes p", but the proof only uses infinitely many distinct values n
  (Lemma 2.1 holds for any n ≠ 0). The "in particular" (family valid on L ∩ U, εU ⊂ U, ε ≡ 1 mod M) needs exactly that:
  validity on all of L ∩ U gives valid orbit tails at every point of L ∩ U, and N takes infinitely many values on L ∩ U
  (U open, L full rank) — not that infinitely many *primes* are represented in L ∩ U (which is the unproved accessibility
  issue the author flags). Restate for infinitely many values n; then the "in particular" is proved as written, provided
  N(ε) = 1 and εL = L are added.
* Superseded for ET families by Thm 3.1; its genuine remaining content is (x, y, z)-families (correctly noted, Cor 3.2(c)).

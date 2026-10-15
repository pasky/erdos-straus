# R259 — hostile review of O248 (NORMFORM_CUBIC.md, BRAINSTORM/z20_*.md, AGENT_REPORT_O248)

Reviewer: R259 side agent (branch side-agent/review-normform, merged side-agent/normform-cubic at 7f070f22).
From-scratch scripts: `scripts/review_r259_identities.py` (sympy: every rearrangement in Thms 1.1′/1.2′/3.1),
`scripts/review_r259_search.py` (python-flint exact brute-force search for Type I/II families over 9 forms incl. controls).
Status: round 1 complete. No FATAL or MAJOR defect; 10 MINOR defects (D1–D10), all wording/scope/argument-completion.

## Verdict table
| Claim | Verdict |
|---|---|
| Thm 1.1′ (Type II, irreducible top part, one valid point) | SOUND |
| Thm 1.2′ (Type I, irreducible top part, cone) | SOUND-AFTER-REPAIRS (D1–D3, minor) |
| Cor 1.3′ (norm forms / binary cubics collapse) | SOUND (scope wording D5) |
| Remark 1.4 (SPARKS7 Cor 1.3 scope remark wrong) | SOUND |
| Lemma 2.1 (orbit finiteness, SML) | SOUND-AFTER-REPAIRS (D6, minor) |
| Cor 2.2 (orbit-tail families collapse) | SOUND-AFTER-REPAIRS (D7: rank-2 orbits need Laurent; "in particular" needs N unbounded on L ∩ U) |
| Thm 3.1 (Type I unit criterion, one valid point) | SOUND (understated: covers every P with irreducible top part, D4) |
| Cor 3.2 / combined claim (all polynomial ET families for full norm forms & irreducible binary forms valid anywhere are ET identities in n) | SOUND-AFTER-REPAIRS (D5: "norm form" = full norm form / ℚ-irreducible form) |
| Remark 3.3 (dictionary) | SOUND as Assessment |
| §4 identification (pull-back containment) | SOUND-AFTER-REPAIRS (D8: pointwise witness argument; D9/D10 labels) |
| Labels overall | OK after D9/D10; nothing overclaimed at FATAL/MAJOR level |

Key hypothesis answer (brief): "leading form" = top-degree homogeneous part P*; Thms 1.1′/1.2′ need irreducibility of P*,
NOT of P, and this is sharp in the sense that P irreducible with P* reducible admits valid non-collapsing families
(P = 4u² − 4v² − 1 Type I, P = 4uv − u − 1 Type II). Thm 3.1's unit hypothesis holds for every P with irreducible P*
(and some others), fails for one-variable P and for P with split top part; with units the conclusion fails (same controls).

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
  validity on all of L ∩ U gives valid orbit tails at every point of L ∩ U, and one needs N to take infinitely many
  values on L ∩ U. That is NOT automatic for an ε-invariant open U: U = {0 < N < 10} ∩ (any ε-stable region) is open and
  ε-invariant, and a family valid there only becomes constant on finitely many level sets (no collapse). Add "N unbounded
  on L ∩ U" (true for the power-cusp regions {0 < N ≤ g(|x|)}, g → ∞) — not that infinitely many *primes* are represented in L ∩ U (which is the unproved accessibility
  issue the author flags). Restate for infinitely many values n; then the "in particular" is proved as written, provided
  N(ε) = 1 and εL = L are added.
* Superseded for ET families by Thm 3.1; its genuine remaining content is (x, y, z)-families (correctly noted, Cor 3.2(c)).

### §4 identification (descent pull-back; "w² = n, not w² = N(u, v)") — SOUND-AFTER-REPAIRS (argument to be written; label split)
* M[N] = M₁[linear] ∘ N: immediate from Cor 3.2. Correct.
* Pull-back of MENU_STERILITY Thm A with φ linear: for φ(u) = u, A = ℚ, and condition (ii) forces γ ∈ ℚ_{>0} with
  γ·n* ∈ ℚ_ℓ^{×2} for all ℓ, i.e. v_ℓ(γ) even for all ℓ, γ a square; so Ster(linear) = {n* ∈ Ẑ^{×2}, n* ≡ 1 (8)}, matching
  the text. BUT Thm A is stated for a family valid at all large u of a *class C of the parameter*; the set {N(x) : x in a
  class of x} is not a class of n, so Thm A does not apply verbatim (MINOR D8). Repair: use the pointwise form of the
  witness computation, which for linear φ is one line — at a valid n ≡ 1 (8) the witness gives (D(n)/n) = −1
  (POINTWISE_BINARYFORM Lemma 1.1), while for D = D̃/g, D̃ ∈ ℤ[n], (D̃(n)/n) = (D̃(0)/n) = +1 and (g/n) = +1 by
  reciprocity as soon as n is a square modulo 8·|D̃(0)·g| (if D̃(0) = 0 then (D/n) = 0 ≠ −1 for n > |D̃|-content). Then choose
  x in the class, close to x* at the finitely many relevant primes, with N(x) large and positive (possible since the
  class is a full-rank coset and N takes large positive values near x* in the real topology on an open cone). With this
  pointwise lemma the containment statement is PROVED.
* "The double cover carrying the obstruction is w² = n (genus 0), not w² = N(u, v)": the mathematical content (the
  obstructed set is the pull-back of the rung-0 set) is proved after D8; the phrasing "is not the relevant object /
  no 2-descent on the genus-1 cover enters" is interpretation and should be labelled Assessment (MINOR D9, label).
* "positive proportion … for full norm forms it follows from Chebotarev/Hecke": plausible and essentially standard
  (principal degree-1 primes of O_K splitting completely in K(ζ_M) have N𝔭 = p ≡ 1 (mod M), a square class); it is unlabelled
  — label it Assessment or give the 2-line argument incl. that the ω_i must be a ℤ-basis of O_K (else the
  representable set is an order's) (MINOR D10). The x³ + 2y³ caveat is correct.

### Remark 1.4 (SYNTHESIS_SPARKS7 Cor 1.3's "top-part step fails for degree 3" is wrong) — SOUND
Checked against SYNTHESIS_SPARKS7 §1: the only degree-2-specific steps are Thm 1.2 (c1) α = 3 ("Q on the rational line
E = 0 has degree exactly 2") and (c2) μ = 2 / γ = δ = 1 / μ = 1 (products of linear forms); each is replaced by (F1)–(F3)
as claimed. The Cor 1.3 parenthesis was an over-cautious scope remark, not a proved obstruction. Correction justified.

### Remark 3.3 (dictionary Type I ↔ units of ℚ[x]/(P)) — SOUND as Assessment
The precise part (non-collapsing Type I needs non-constant units mod P with 4ABD ≡ 1, or 4ABD − 1 | A + B) is exactly
the proof's dichotomy; the (e0) branch only yields the degenerate family, so "or divisibility 4ABD − 1 | A + B" is
vacuous for prime P (could be dropped). The from-scratch controls confirm the dictionary: 4u² − 4v² − 1 (units u ± v)
has non-collapsing valid families; u³ + 2v³, u² + v², u² − 2v² − 1, u² + v (constant units) have none in the search.
The "rungs sorted by (ℚ[x]/(P))^×" sentence is correctly labelled Assessment.

### §2 "What is left" and AGENT_REPORT_O248 — SOUND (labels OK after D9/D10)
"What is left" is labelled Assessment. Report summarises the document faithfully; its label list "Thm 1.1′ … §4
identification: PROVED" should carry D8/D9 (the §4 pull-back needs the pointwise witness argument; its "relevant object"
phrasing is Assessment). Report's iteration I4 self-correction (windows not a lower bound) is correct: for N = u³ + 2v³ + 4w³ − 6uvw,
N(u + 1, v, v) − N(u, v, v) = 3(u² − 2v²) + 3u + 1 = 3u + 4 when u² − 2v² = 1 (re-derived by hand).

## Numerics (from-scratch; EVIDENCE for consistency only)
* `review_r259_identities.py` (sympy): all rearrangements in 1.1′ (b2), 1.2′ (c1 B/C/D, c2 μ = k), 3.1 (e0, e1 i–iii,
  degenerate family) hold identically; three positive controls satisfy their identities and are valid at a point:
  P = uv: (1, 1, 2u, (v + 1)/4) at (5, 7), n = 35; P = 4u² − 4v² − 1: (u − v, u + v, 2u, 1) at (5, 2), n = 83 (prime:
  4/83 = 1/1743 + 1/30 + 1/70); P = 4uv − u − 1 Type II: (u, 1, 1, v) at (3, 4), n = 44.
* `review_r259_search.py` (python-flint, exact division; S = c₀ + Σ ε_i x_i + κP):
  | P | Type I: total / in ℚ[P] / degenerate list / other | Type II: total / in ℚ[P] / other |
  |---|---|---|
  | u³ + 2v³ | 875 / 299 / 576 / 0 | 119 / 119 / 0 |
  | u² + v² | 875 / 299 / 576 / 0 | 119 / 119 / 0 |
  | u² − 2v² − 1 (non-homog., P* irred.) | 875 / 299 / 576 / 0 | 119 / 119 / 0 |
  | v + u² (P* = u² reducible, no units) | 875 / 299 / 576 / 0 | 119 / 119 / 0 |
  | u³+2v³+4w³−6uvw (ℚ(∛2) norm; smaller S) | 44 / 44 / 0 / 0 | 15 / 15 / 0 |
  | u² + v² + w² (smaller S) | 44 / 44 / 0 / 0 | 15 / 15 / 0 |
  | control 4u² − 4v² − 1 | 895 / 299 / 576 / 20 (all valid somewhere) | 149 / 119 / 30 |
  | control 4uv − u − 1 | 895 / 299 / 576 / 20 | 148 / 119 / 29 (incl. valid (u, 1, 1, v)) |
  | control uv (reducible) | 1055 / 299 / 576 / 180 (none valid in [−4,4]², search space lacks v/4) | 119 / 119 / 0 |
  Everything predicted by Thms 1.1′/3.1 holds; controls show the hypotheses are doing work.
* `review_r259_orbit_closure.py`: Zariski closure of unit orbits = level set, ℚ(∛2) and ℚ(√2) (see Lemma 2.1).

## Defects (all MINOR; none FATAL/MAJOR)
1. **D1 (MINOR) Thm 1.2′ positivity paragraph.** Says all coordinates are positive at valid points; validity allows
   (A, B, C) < 0 < D. Repair: add the R256 sentence — on U the signs are constant; replace (A, B, C) by −(A, B, C), which
   preserves the Type I identity and the conclusion.
2. **D2 (MINOR) Thm 1.2′ hypothesis.** "lattice coset L ⊂ ℤ^r" must be a coset of a full-rank sublattice. Repair: say so.
3. **D3 (MINOR) Thm 1.2′ (c2) μ = k.** "Coefficient of P²" is a degree comparison (2k vs ≤ 2k − 1), not a coefficient
   comparison (E_A, E_B ∉ ℚ[P]). Repair: one clause.
4. **D4 (MINOR, understatement) Thm 3.1 / Cor 3.2(c).** (ℚ[x]/(P))^× = ℚ^× holds whenever P* is irreducible (gr of the
   degree filtration is ℚ[x]/(P*), a graded domain), so Thm 3.1 subsumes Thm 1.2′ for every P of §1, not only homogeneous
   P. Repair: add this to the "e.g." list and to Cor 3.2(c).
5. **D5 (MINOR, scope) Cor 3.2 / report "every norm form".** Must be the full norm form (k variables, ℚ-basis of K) or
   any ℚ-irreducible form; incomplete norm forms can be powers ((x² − 2y²)² for K ⊋ ℚ(√2)). Repair: say "full norm form".
6. **D6 (MINOR) Lemma 2.1.** (a) state that (x, y, z) ↦ ET coordinates is finite-to-one (a, b, c, d divide x, y, z);
   (b) drop the stale "(N(ε) = ±1; replace ε by ε²)".
7. **D7 (MINOR) Cor 2.2.** (a) For totally real cubic K the "unit orbit" is a rank-2 orbit; Laurent's theorem IS needed
   (delete "Not needed below", or restrict to cyclic orbits). (b) Restate for infinitely many values n (primes not needed);
   the "in particular" additionally needs N(ε) = 1, εL = L and N unbounded on L ∩ U (U = {0 < N < 10} is an ε-invariant
   open counterexample to the sentence as written).
8. **D8 (MINOR) §4 pull-back of Thm A.** Thm A is stated for classes of the parameter; {N(x)} over an x-class is not an
   n-class. Repair: insert the pointwise witness argument (see §4 above) and the choice of x near x* with N(x) large.
9. **D9 (MINOR, label) §4.** "w² = n, not w² = N(u, v) is the relevant object / no 2-descent enters" → Assessment; keep
   PROVED for the containment.
10. **D10 (MINOR, label) §4 last paragraph.** Chebotarev/Hecke positive proportion: label Assessment or give the argument
   (needs ω a ℤ-basis of O_K, principal degree-1 primes split in K(ζ_M)).

Cited sources: SYNTHESIS_SPARKS7, POINTWISE_BINARYFORM §1/§4.3, MENU_STERILITY Thm A read and checked against usage.
Skolem–Mahler–Lech: standard statement used correctly. Laurent (Astérisque 147–148) and Schinzel §3.3: NOT accessed;
the statements as used are standard, and the reviewer supplied a self-contained argument for the Schinzel step.

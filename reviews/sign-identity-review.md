# R204 — hostile review of SIGN_IDENTITY.md (O205, checkpoint 1)

Reviewer branch side-agent/review-sign-identity (merged side-agent/sign-identity at review start).
From-scratch scripts: `scripts/review_si_lemmas.py`, `scripts/review_si_avg.py` (+ further `review_si_*` below).
None reuse `scripts/si_*`.

## Summary verdicts (filled in claim by claim)

| Claim | Verdict |
|---|---|
| Lemma 1.1 ((u,v)-form, χ = (−uv/n₀), size bound) | SOUND |
| Lemma 1.2 (trivial certificates; Dirichlet/Chebotarev form) | SOUND (classical; novelty nil — see D1) |
| Lemma 2.1 (averages, 240/512, 80/512) | SOUND |
| Thm 2.2 (no holomorphic modular generating function) | SOUND-AFTER-REPAIRS (minor: D2, D3, D4) |
| Prop 2.3 (T1 kills finite twisted d_k combinations) | SOUND (minor D5; elementary) |
| Prop 2.4 (Waldspurger zero-set, non-square conductor) | SOUND-AFTER-REPAIRS (MAJOR D6 hidden trivial-character hypothesis; D7 citation form) |
| §3 rank screen (CERTIFIED) | SOUND — reproduced from scratch, all 32 certificates, same column ranks |
| Prop 4.1 (a)–(d) (Gram T_w, Diff formula, n = p dichotomy, squares) | SOUND (novelty: (b)/(c) are CHI_FLIP Thm 1.1 + CONSTRUCTIVE Thm 1.2(c) restated; D9) |
| §4 log-separation (CONDITIONAL) | GAP — mis-normalized index (Z(T_w) ≠ the cycle meant; need 2p·T_w), wrong/missing citation (SSY needs N odd; Zhu 2023 covers N = 2p), label misplaced; content tautological (MAJOR D10) |
| §4 moduli reading, GK genus-3 reading (Assessment) | SOUND as Assessment |

## Claim-by-claim

### Lemma 1.1 — SOUND
Re-derived. t·uv = n + u + v; Av = (tu−1)v = n + u, A*u = n + v; t ≥ 1 is automatic from positivity, so the bijection
holds. AA* = tn + 1 ⇒ gcd(A, n) = 1. If ℓ | n, ℓ | u: ℓ | Av, ℓ ∤ A ⇒ ℓ | v, and A ≡ −1 (ℓ) ⇒ (−A/ℓ) = 1; for ℓ | n,
ℓ ∤ uv: A ≡ u v⁻¹ ⇒ (−A/ℓ) = (−uv/ℓ). Size: t ≥ 1 ⇔ uv ≤ n + u + v ⇔ (u−1)(v−1) ≤ n + 1; for u ≤ v, v | n + u.
From-scratch brute force (`review_si_lemmas.py`, words found by scanning (u, v) directly, not via the divisor trick):
odd n ≤ 2000, 50 008 words (35 184 for n ≤ 1500 — matches the author's census total); χ = (−uv/n₀), the prime-sharing
claim, and the bound |X_n| ≤ 2Σ d(n+u) (n ≤ 600): 0 mismatches.
(The author's "50 003 words of odd n ≤ 2000" in Prop 4.1 excludes the 5 words of n = 1; cosmetic, D-minor below.)

### Lemma 1.2 — SOUND
All three word families re-verified by hand and by script (n < 20 000, all p ≡ 1 (4), q ≡ 3 (4), q | p + 1: 0 failures).
The Dirichlet/CRT and Chebotarev statements are correct: K′ ⊇ ℚ(i) Galois, q unramified in K′ ⇒ K′ ∩ ℚ(ζ_q) = ℚ, so
Frobenius (id, −1) in Gal(K′)×Gal(ℚ(ζ_q)) has positive density; p split in K′ ⇒ p ≡ 1 (4).
Overlap: the n ≡ 3 (4), 5 (8) words are Mordell's classical identities (already CHI_FLIP §3.1, (J)9/(J)32 mod-8 sign
law: they are χ = −1 cells), and "certificates exist for infinitely many p in every admissible class" is folklore (any
single Mordell–type family p ≡ −1 (q) does it). The document says this ("No certificates beyond the Mordell mechanism"),
so no overclaim; it should not be listed as a result in the report's PROVED list without "(classical)". D1.

### Lemma 2.1 — SOUND
Cells recomputed from scratch, and the *cell-function* property re-tested on 216 lifts per cell: 320 odd-K cells,
240 with χ = −1, 80 with χ = +1 (same as MODEL_SPECIFIC Thm 3.1(a)/CHI_FLIP Cor 1.2 — not new). Leading-term
uniformity over residue classes of #{tuv ≤ X} is standard (hyperbola method). The error analysis (t ≤ 2 words
O(X log X); t ≥ 3 ⇒ K ≥ tuv/3; boundary layer X < tuv ≤ X + u + v contributes Σ_{uv≤X}((u+v)/uv + 1) = O(X log X))
is correct. Numerical fit (`review_si_avg.py 200000`, exact counts, fit aX log²X + bX log X + cX on X/16…X):
a(N₋) = 0.23433 vs 15/64 = 0.234375; a(N₊) = 0.07820 vs 5/64 = 0.078125. Ratio ΣN₋/ΣN₊ = 2.43 at 2·10⁵,
consistent with the author's 2.40 (10⁵) / 2.50 (10⁶).

### Thm 2.2 — SOUND-AFTER-REPAIRS (mathematics correct; projection step and scope sentence need fixing)
*Short proof (cusp 0), re-derived.* For a holomorphic modular form f_k of weight k ∈ ½ℤ_{>0} on a finite-index
subgroup with any multiplier, f_k|S is holomorphic modular for S⁻¹ΓS, with expansion Σ_{m≥0} c_m q^{(m+κ)/h}; at
z = i/y every term but the κ = 0 constant decays like e^{−2π/(hy)}. Hence f(iy) = Σ_k b_k(iy)^{−k} + O(y^{−K}e^{−c/y}),
a finite sum of distinct powers: either ≍ y^{−k₀} or exponentially small. With Σ_{n≤X} a(n) ~ c·X log²X/2, c ≠ 0 for all
four a (c(S) = −5/16), Abel summation gives Σ a(n)e^{−2πny} ~ (c/2)(2πy)^{−1}log²(1/y). Contradiction. Correct.
The same computation along x = a/c (z = a/c + iy, γ(∞) = a/c, j(γ, γ⁻¹z) = i/(cy)) gives
f(a/c + iy) = Σ_k (i/(cy))^k (b_{k,γ} + exp. small), which is what step (i) of the long proof needs: cusp components of
*higher* weight are exponentially small on that ray (the sup-norm bound y^{−K/2} would NOT suffice if K > 2k — the
parenthetical "slash by γ" must be read this way; D3).
*Brief's specific worries.*
* E₂: quasi-modular, not a modular form, so outside the hypothesis; its cusp-0 expansion does carry an extra
  6/(πy) term (`review_si_cusp.py`: E₂(iy) + y⁻² = 6/(πy) to 8 digits). The holomorphic weight-2 Eisenstein series
  E₂(z) − NE₂(Nz) have the y⁻¹ terms cancel exactly (checked: y²(E₂(iy) − 2E₂(2iy)) = −1/2 to 8 digits, no y⁻¹ term).
  Even if a y⁻¹ term occurred it would be y⁻¹, not y⁻¹log²(1/y).
* Weight 1 Eisenstein: coefficients Σ_{d|n}χ₁(d)χ₂(n/d) with χ₁χ₂ odd, so not both trivial; Dirichlet series
  L(s,χ₁)L(s,χ₂) has at most a simple pole: average c·X, no log; expansions at every cusp are genuine q-expansions
  with constant terms (L-values), no log terms. Logs (d(n), X log X) arise only from the *non-holomorphic* weight-0
  Eisenstein series, outside the theorem.
* Weight ½: Serre–Stark (unary theta series), ≍ y^{−1/2} or exp. small at each cusp. Half-integral-weight Eisenstein
  series of weight ≥ 3/2: constant terms at cusps, covered by the same expansion.
* Oldforms, all cusps: the short proof needs only cusp 0 applied to each slash; level-raising f(dz) is again a modular
  form, nothing changes.
* Long proof (iii): Rankin–Selberg Σ_{n≤X}|a_g(n)|² ~ c_g X^K (c_g ∝ Petersson norm > 0) holds for cusp forms of
  half-integral weight with multiplier; the lower-weight mean squares (cusp X^{k′}, weight-1 Eisenstein X log³X,
  weight-½ X^{1/2}) are O(X^{K−1/2}); the triangle inequality in ℓ² finishes; the bound Σ|a(n)|² ≪ X^{3/2+ε} is correct
  (|a(n)| ≤ |X_n| ≪ n^{1/2+ε}). Correct, but redundant given the short proof.
*Defects:* D2 (projection to odd n), D3 (step (i) wording), D4 (scope sentence about Thm 9.1 and "log¹" is wrong).

### Prop 2.3 — SOUND
Re-derived: on n composed of primes ≡ 1 (L) every ψ(d) = 1, d_k(ℓ^{2a}) = binom(2a+k−1, k−1), a polynomial in a of
degree k − 1 with leading coefficient 2^{k−1}/(k−1)!; vanishing for all a ≥ 0 kills C_k (k ≥ 2) top-down and leaves
C₀ + C₁ = 0, so E ≡ C₀ + C₁ = 0 on the semigroup. T1 for N₋ is trivial ((x/m²) = 1 for gcd(x, m) = 1; gcd(A, n) = 1).
With Lemma 1.2, E(p) = 0 ≠ N₋(p) for infinitely many p. Correct.
Remarks. (a) The proof uses only *one* prime ℓ and a = 0, …, K (K = max rank); the Reading's "ℓ⁴, ℓ²ℓ′² are needed"
is inaccurate — ℓ²ℓ′² is never used (D5). (b) It is elementary and does not use any automorphy, so "GL(k)-Eisenstein"
is only a name for the coefficient class; fine as stated ("exponent 0"). (c) Relation to Thm 9.1 is correctly
qualified (Thm 9.1: rank 2, exponents; Prop 2.3: rank k, exponent 0). Mixed rank-and-exponent combinations
d_k with d_j^{s_j} weights are covered by neither; the doc doesn't claim them.

### Prop 2.4 — SOUND-AFTER-REPAIRS
Re-derived the restricted statement. For F a newform of level N with **trivial character** and D a fundamental
discriminant prime to N, ε(F ⊗ χ_D) = ε(F)χ_D(−N) (IK Prop 14.20 with τ(χ_D)² = χ_D(−1)|D|); for D < 0 this is
−ε(F)(D/N). For D ≡ 1 (4): if N_odd is not a square, D ↦ (D/N_odd) is a non-principal character mod N_odd, independent
of D mod 8 by CRT, so (D/N) is non-constant; if N_odd = □ and v₂(N) odd, (D/2) separates D ≡ 1, 5 (8); otherwise N = □.
So a class Z mod 8N_odd ⊂ {n ≡ 3 (4)} with ε = −1 exists and contains infinitely many squarefree n prime to N. The
121b1 counterexample to the original version is right (and the root-number formula reproduces it). The comparison
uses only the PROVED N₋ ≥ 1 on n ≡ 3 (4). Logic correct, with two repairs:
* **D6 (MAJOR, hidden hypothesis).** The statement allows any "weight-3/2 Hecke eigenform"; with a nebentypus ψ the
  Shimura lift has character ψ², and if ψ² ≠ 1 the twisted L-values are not self-dual — no root-number vanishing at
  all; if ψ is quadratic the relevant twist is ψχ_{−n}, whose conductor may share primes with N and the formula
  ε = ε(F)χ_D(−N) is not the right one. The proof is valid for g ∈ S_{3/2}(Γ₀(4M)) with trivial character (the
  Kohnen–Zagier/Waldspurger setting). Repair: add "trivial character" (and, if desired, a remark that quadratic ψ
  can be handled by replacing χ_{−n} with ψχ_{−n} when gcd(cond ψ, n) = 1 — not checked here).
* **D7 (MINOR, citation form).** "a(n)² = c(n)·L(F ⊗ χ_D, 1), c depending only on square classes" is the
  Corollaire-2 / explicit (Kohnen–Zagier, Baruch–Mao) form. Waldspurger's Théorème 1 alone (the ratio identity
  c(n₁)²L(χ_{n₂})n₂^{1/2} = c(n₂)²L(χ_{n₁})n₁^{1/2} within a square class) gives nothing on a class where *all* L-values
  vanish, which is exactly the class Z used here. The needed input is the full Waldspurger statement (a(n) = 0
  whenever ε(F ⊗ χ_{−n}) disagrees with the local signs of g's packet, equivalently a(n)² = (local factor)·L(1/2)
  with the local factor possibly 0); cite it precisely (Waldspurger 1981, Thm 1 + Cor 2; or Baruch–Mao 2007). I could
  not access the PDFs (not in sources/); the statement is standard and I believe it holds as used.
* The "Kohnen plus space" remark is right: weight 3/2 plus space supports −n ≡ 0, 1 (4), i.e. n ≡ 0, 3 (4).

### §3 rank screen — SOUND (reproduced from scratch)
`review_si_rank.py 120`: all 48 columns rebuilt from the verbal description (Hurwitz numbers by reduced-form count,
Kronecker symbols, ternary counts, words) without using si_*; exact Fraction elimination on the first 120 rows
(n ≥ 3) of each class mod 8. Column ranks 37, 32, 32, 34 (identical to the author's), and **all 32 (class, target)
pairs are certified not in the ℚ-span** (8 targets: N₊, N₋, S, |X|, interior N_±, t-weighted N_±). Sanity: Hurwitz table
checked at 10 values; a planted in-span target is correctly not certified. The label "CERTIFIED finite statement" is
right; the AGENT_REPORT still says "(exact rank mod 2⁶¹−1)" in the CERTIFIED bullet — stale wording (D8).

### Prop 4.1 — SOUND (a)–(d); novelty modest
Re-derived. (a) t·diag(v,u) − R = [[tv−1, 1], [1, tu−1]] = [[A*, 1], [1, A]], det = AA* − 1 = tn; injective for fixed n.
Clifford check by hand: with e_i² = G_ii, e_ie_j + e_je_i = 2G_ij, x = e₁e₂ satisfies x² = −2x − vt, so i = 1 + x has
trd 0, i² = 1 − tv = −A*; similarly j² = −A; and ij + ji = −2 (expand; the e₁e₃ terms cancel because G₁₃ = 0). Hence
(i, i)/2 = A*, (i, j)/2 = −(ij + ji)/2 = 1: Gram T_w. (b) Orthogonalising, ℚ⟨i, j⟩ = (−A*, −A*·det T_w) = (−A*, −tnA*). Local
computation: ℓ | t, ℓ ∤ n ⇒ −A* ≡ 1 square; ℓ | A* ⇒ (−A*, tn)(−A*, −1) = (−1/ℓ)^{2v} = 1; ℓ | n ⇒ (−A*/ℓ)^{v_ℓ(tn)} =
(−A/ℓ)^{v_ℓ(n)} (also when ℓ | t, both sides 1); 2 by the product formula with ∞ ramified. From-scratch check
(`review_si_lemmas.py 2000`, own Hilbert-symbol routine incl. ℓ = 2): ramification of (−A*, −tnA*) equals the formula,
odd size, on all 50 008 words of odd n ≤ 2000 (= author's 50 003 + the 5 words of n = 1), 0 mismatches.
(c) is (b) at n = p plus CONSTRUCTIVE Thm 1.2(c) (E(L_w) Eichler of level 2 in B_{p,∞} if χ = −1, level p in B_{2,∞}
if χ = +1) — that theorem already contains the full dichotomy, and CHI_FLIP Thm 1.1 is (b) in quadratic-form language
(Ram C₀(Q_w) = anisotropic places). KUDLA_ES Thm 1.2/1.4 already has "certificate ⇒ Diff(T) = {p}" for its indices.
(d) trivial ((x/m²) = 1). So Prop 4.1 is correct; what is new is the explicit Gram T_w = tD − R and the uniform
"both signs are |Diff| = 1" packaging. D9: say so and cite.

### §4 log-separation — GAP (MAJOR D10)
I fetched the arithmetic Siegel–Weil literature (`sources/r204/`: Zhu arXiv 2304.10696, SSY arXiv 2206.05823;
abstracts of Du–Yang 1702.07917 and Zhu 2401.06368). Findings:
1. **Citations.** SSY treat X₀(N) for **N > 3 odd** squarefree — X₀(2p) is not covered. Du–Yang (N squarefree) is the
   genus-1/divisor statement. KRY is Shimura curves (D(B) > 1). **Zhu, "Arithmetic Siegel–Weil formula on 𝒳₀(N)"
   (arXiv 2304.10696), Thm 1.2.1, covers arbitrary N**, incl. N = 2p and the bad fibres — the doc's "not verified for
   the bad fibres here" hypothesis is, modulo normalization, a published-preprint theorem it does not cite.
2. **Normalization.** Zhu's special cycles Z(T, ϕ) parametrize pairs x₁, x₂ ∈ Hom(E, E′) ⊥ π with T = ½((x_i, x_j)), in
   the lattice ∆(N) = {[[−Na, b], [c, a]]}, Q = det; ∆(N) ⊗ ℚ_ℓ ≅ N·(M₂(ℚ_ℓ)^{tr=0}, det), so
   Diff(T, ∆(N)) = Ram(algebra of Gram T/N). The pair (i, j) are *endomorphisms* of E (elements of the Eichler order),
   not elements of Hom(E, E′); the matching special-cycle data are (πi, πj) with Gram **2p·T_w**, and indeed
   Diff(2pT_w, ∆(2p)) = Ram(T_w). Using T_w itself is wrong: `review_si_scale.py` finds Diff(T_w, ∆(2p)) ≠ Ram(T_w) on
   1604 of 2958 words of primes p < 400 (e.g. (3,1,2) ∈ X₃: Ram(T_w) = {2} but Diff(T_w, ∆(6)) = {3}). So "ĉ(T_w)"
   on X₀(2p) as written is either undefined (no lattice specified) or, in the standard normalization, a different cycle
   whose Diff does not follow χ.
3. **Label / content.** For T positive definite with Diff(T) = {ℓ}, Ẑ(T) is a 0-cycle supported on the supersingular
   locus in characteristic ℓ, and its arithmetic degree is Σ (lengths/|Aut|)·log ℓ — rational·log ℓ, ≥ 0, > 0 iff
   Z(T) ≠ ∅ — *without any Siegel–Weil formula*. So the displayed decomposition N₋^μ log p + N₊^μ log 2 is
   unconditional geometry (given Z(2pT_w) ∋ (E→E′, πi, πj), which is Prop 4.1(c) + the moduli reading); Siegel–Weil
   (Zhu) only adds that the same number is a derivative of an Eisenstein coefficient. And the "⟺" is tautological:
   N₋(p) > 0 ⟺ some χ = −1 word ⟺ some term carries log p. It adds no information beyond Prop 4.1(c).
*Repair.* Replace T_w by 2p·T_w (state the lattice ∆(2p) and ϕ = 1_{∆(2p)²}), cite Zhu 2304.10696 Thm 1.2.1 (SSY only
for odd N), relabel: the geometric decomposition as PROVED-modulo-moduli-reading (Assessment for the identification of
points), the Eisenstein-derivative form as CONDITIONAL on Zhu's theorem (preprint; local identity not re-checked
here), and call the "⟺" a reformulation (tautological), not a "transcendence-separated form" with content.
The barrier screen (i)–(iii) after it is fine and matches GROWING_IDENTITIES/DIFF_DEEP.

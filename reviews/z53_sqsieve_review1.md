# Hostile review 1 — `Z53_SQSIEVE.md` (branch side-agent/z53-sqsieve, HEAD b291d871)

Reviewer mode: deep. ES remains OPEN; the memo claims nothing about the existence of solutions, which is correct.

## Overall verdict: **CORRECT WITH FIXES**

Theorem A (R(n) ≪ n^{12/37+ε}) holds. I re-derived every power in Lemma 1′, Lemma W, Lemma P, Prop D and §4.5, and
found no gap that changes an exponent. Theorem A′ and Cor A″ follow, subject to the small hygiene points in F6.
The weak spots are elsewhere:
- **Prop B2.** It is labelled PROVED, but its "implementation class" (iv) is defined so that it excludes the ℓ-dependent
  bounds §4 actually uses (F1).
- **Reverse-direction rhetoric.** "dead", "only through BM", and "cannot touch positivity" go beyond what Lemma C3 proves (F2).
- **Two pieces of evidence.** The (H) certificate is computed incorrectly (F3), and the F3-falsifier mean is misread (F4).

## What I checked and found correct

- **Lemma 1′.**
  - s ∈ (U+V, 2U+2V] ⊂ (V, 4V], so Φ = 1. Each (C,k) has at most 2 ordered preimages, and u = B contributes ≤ τ(n).
  - ω ≠ 0 implies k ≥ 1 and f ≤ 25V².
  - n ≥ 2uBC, n/32 ≤ UVW < n/2, and |α+β+γ−1| ≤ 5/log n.
  - S₁ ≥ Σ_a w(a), because the f = 0 points sit in S₁ only. Σ_a w(a)χ_Q(a) = S_Q. Constants 4, 4 are inherited from
    HYPSUMPROD Lemma 1.2 (pairs ≤ P₀²).
- **Lemma W.**
  - Completing the square gives r = (8cn+4)/(2A) and d = 16(4cn+1)/(4A²).
  - The Gauss-sum opening and Σ_x e((tx²+ℓx)/q) = (t/q) g e(−4̄t̄ℓ²/q) give H = S(−d, −4̄ℓ²; q). This agrees with LIT_CHECK's S(1, 4̄ℓ²d; p).
  - Cases checked: d ≡ 0 gives −1; q | c gives a Gauss sum; q | ℓ gives K_q ∈ {0, −1, q−1}; Σ_c|G| ≤ 2q − 3 when q | ℓ.
  - CRT identity: 1/(qq′) ≡ q̄′/q + q̄/q′ (mod 1). Independent numerics (my script, not in the repo):
    - G^{(Q)}_c(ℓ) = G^{(q)}_c(ℓq̄′) G^{(q′)}_c(ℓq̄) in 92 409 cases (Q ∈ {15, 35, 33, 77}), max error 5·10⁻¹².
    - H = S(−d, −4̄ℓ²; q) for all d, ℓ ≢ 0 and q ≤ 17, max error 7·10⁻¹².
    - The repo's `z53_sqsieve_checks.py 23 20000` reproduces 27 962 = Σ q³ cases and 87 388 triples (it runs in 3 s, not "~2 min").
- **Lemma P.** The substitution and the signs e(−ℓn/(4CQ)) e(ℓk₀/Q) are consistent with Φ̂(ξ) = ∫Φ e(−ξt). The Poisson rerun
  (n = 999²) reproduces `poisson_check.txt` exactly.
- **Prop D.**
  - (i) Σ_C|K(C)| ≤ 4W + 3Q, so the ℓ = 0 term is ≤ |Φ̂(0)|(V/Q + 3V/(4W)).
  - (ii) Formula for a_ℓ′, ∫|a′| ≤ (V/(8QW))Ψ, Abel constant 3V/(8QW).
  - (iii) g‴ = (3/2)ℓnQ²/C⁴ with ratio 16. Titchmarsh 5.11 is monotone in b − a, so sub-intervals J are covered.
  - (iv) The ℓ-sum lemma holds for every M > 0 and σ ∈ {±1/6, 0}. Powers after inserting M = 8QW/V:
    - Q^{−1+3/2+7/6−2/3} = Q¹ and Q^{−1+3/2+5/6−5/6} = Q^{1/2}.
    - V^{−1/6}, V^{1/6}; W^{1/2}, W¹.
    - So (4.2) is exact.
- **§4.5.**
  - ρ* balances β − ρ against 2ρ + 1/6 + γ/2 − β/6, which gives β − ρ* = (12 − 11α − 8γ)/18.
  - The region {α ≥ θ*, γ ≥ θ*, 2α + γ ≤ 1} is a genuine triangle. All terms are affine in (α, γ), and so is ρ*.
  - The O(1/log n) slack (including points slightly outside the triangle because β ≠ 1 − α − γ exactly) costs O(1).
  - Side conditions: min ρ* = 4/333 and max 2ρ* = 2/37 < γ.
  - Nothing is missing from the error list: ℓ = 0 terms, τ(n), the S₁/P terms, the V/W term when W < V, and small n
    (absorbed by n ≥ n₀). Two terms are omitted from the printed list, β − γ − ρ and −ρ; they are trivially dominated.
- **Exponents, independent check.** My own sympy script (`/tmp/rv/indep.py`) includes all terms. Results:
  - Vertices give maxima 12/37, 104/333 and 421/1332. Only (12/37, 13/37, 12/37) is tight, so it is the worst block, as claimed.
  - Cube: ρ* = 1/54, giving 17/54.
  - General κ: β − ρ* = (2 − (2−κ)α − (3/2−κ)γ)/3, which gives θ = 4/(13−4κ). This yields 12/37 (κ = 1/6),
    21/65 (κ = 13/84) and 4/13 (κ = 0).
  - All terms stay ≤ θ(κ) for κ ∈ [0, 1/4]; ρ* reaches 0 only at κ = 1/4, where θ = 1/3 is trivial.
  - `exponents.py` and `reach.py` reproduce byte-identically.
- **§5.1 table, verified exactly.**
  - On the diagonal, ρ* = ((2+κ)β − κ − 1/2)/3 and the main term is ((1−κ)β + κ + 1/2)/3.
  - Endpoints: 4/13 and 14/41; 55/181 and 197/575; 1/4 and 5/14.
  - Cube values: 5/18 + 2κ/9 gives 17/54, 59/189 and 5/18.
  - Secondary terms and 2ρ* < γ (β < 13/31 for κ = 1/6) hold on these intervals.
- **Prop B2, arithmetic parts.**
  - Fejér: L + 1 ≥ 2N gives max|X_ℓ| ≥ √N/2.
  - Bad classes ≤ 2q + 2q′, and Q − 2q − 2q′ ≥ Q/2 ⇔ (q−4)(q′−4) ≥ 16.
  - Parseval Σ_ℓ|G_c|² = Q·#{k : (f, Q) = 1} ≥ Q(q−2)(q′−2) ≥ Q²/2.
  - For good c, |G_c| ≤ 4√Q (when q | ℓ, |K_q| = 1 ≤ 2√q). Hence Σ ≥ Q^{5/2}/16.
  - Final product: (V/(QW))·(ξ₀W/V)·Q²·W^{1/2} = ξ₀QW^{1/2}. Φ̂(0) = ∫Φ ≥ 3 is correct.
  - Numerically, for (q,q′) = (11,13) and (13,17) the sums are about 7–8× the bound Q^{5/2}/16, and max|G|/√Q ≤ 3.4.
- **Theorem C1.** xy = 4Cn + 1, x ≡ 3 (mod 4), (2/x) = 1 when C is even, reciprocity gives (C′/x) = 1, so (n/x) = −1.
  For (ii), x(x+1)(y+1) ≡ (x+1)² (mod n) and gcd(4Cu, n) = gcd(4CB, n) = 1. All correct.
- **Lemma C3 and C4(a).**
  - C3: both cases C ≥ 0 and C < 0 are right, and the σ² identity holds.
  - C4(a): (2Cs−1)² − (2Cr)² = 4Cn + 1, with factor pair (4Cu−1, 4CB−1). Correct.
- **§7 tables.** Every entry matches `strip_balanced.txt` and `strip_nearcube_controls.txt`.
  - Prime counts: P₀ = 135, 21, 10, 7; 9 045 and 210 pairs.
  - I recompiled `z53_sqsieve_strip.c` and reran n = 1 000 000 007 and n = 31 623²; the output is identical.
  - F3 numbers match `lambda_falsifier.txt`.

## Findings

**F1 — MAJOR. §5.2 Prop B2, definition (iv) and its parenthetical.**
- *Problem.*
  - Class (iv) requires E_Q(ℓ) ≤ e(W/Q), a function of the length alone, valid for all ℓ ≥ 1, "as every exponent-pair or
    k-th-derivative bound is". That is false: the third-derivative bound in §4.4(iii) and every exponent-pair bound grow
    with |ℓ| (through λ₃ or y).
  - So, as written, B2 does not cover the implementation of Theorem A itself. Part (a) only bounds max over ℓ ≤ L of
    |X_ℓ|, which says nothing about an ℓ-dependent e_ℓ at small ℓ.
  - The gap is real at the edges. When ℓn < 4W² (e.g. W = K√n with K large), Kusmin–Landau, a first-derivative test,
    gives E_Q(ℓ) ≪ W²/(ℓn) = O(1) for small ℓ, which is well below √N.
- *Fix.*
  - Redefine (iv) as: E_Q(ℓ) ≤ e(ℓ, W/Q) with e(ℓ, N) ≥ c√N for every ℓ with |ℓ|n ≥ 4W².
  - Then prove membership. Exponent-pair bounds satisfy it because y ≥ N² and λ ≥ 1/2 give (y/N²)^κ N^λ ≥ N^{1/2}.
    The k ≥ 2 derivative tests satisfy it by AM–GM; for example, Nλ^{1/6} + N^{1/2}λ^{−1/6} ≥ 2N^{3/4}.
  - In (b), sum only over Q-blocks of ℓ ∈ [4W²/n, L₀]. At the balanced block this drops only O(1) values of ℓ against
    L₀/Q ≍ n^{1/4}, so the conclusion n^{1/4−o(1)} survives.
  - Keep (a) as the statement that no ℓ-uniform bound beats √N/2. Also note there that the number of points is
    ⌊W/Q⌋ or ⌈W/Q⌉, not W/Q.

**F2 — MAJOR (overclaim). §1 (S3), §6 opening and "Verdict for (S3)", §9, §10 FRONTIER text, §11.**
- *Problem.* The phrases at issue are:
  - "square-sensitivity is exactly the BM twist" and "available only through the BM twist";
  - "lower bounds are not available through the square sieve at all";
  - "dead";
  - "the square sieve cannot touch positivity" / "cannot reach positivity".
- What is proved is narrower:
  - (C1) squares at coprime points lie in 𝒜⁻.
  - (C3) under hypothesis (H), any *quadratic-in-σ, equal-weight* minorant has principal part ≤ 0.
- Neither statement excludes other square-sensitive weights. Neither excludes a positive lower bound coming from the signed
  auxiliary sums, a route the memo itself names in C3. "Only" and "cannot" are therefore not theorems.
- *Fix.*
  - Relabel these sentences as Assessment.
  - In the FRONTIER text, replace "the square sieve cannot touch positivity" with: "Heath-Brown-type quadratic minorants
    have non-positive main coefficient (Lemma C3), so any lower bound must come from signed estimates of the auxiliary
    character sums; the only square-sensitive ingredient identified is the BM twist."
  - Change (S3) "dead (scoped)" to "closed for quadratic σ-minorants; open otherwise".

**F3 — MINOR. §6 after C3, and §7.2 "(H) holds in every run; CERTIFIED".**
- *Problem.* In `z53_sqsieve_strip.c` (line 45) the flag `has0` is set if *some* non-square has |σ| ≤ 1. Hypothesis (H)
  needs either σ = 0, or *both* σ = +1 and σ = −1 (the C < 0 case uses D(ε₀) + D(−ε₀)). The printed flag therefore does
  not certify (H).
- Separately, "±⌈√P₀⌉" is inaccurate. The code uses the least x₀ ≥ √P₀ with x₀ ≡ P₀ (mod 2), which is 13, not 12, for P₀ = 135.
- *Fix.* Record σ = 0, σ = +1 and σ = −1 separately and rerun, or downgrade the claim to EVIDENCE. Fix the x₀ wording.

**F4 — MINOR. §6 F3 "Reading".**
- *Problem.* The memo says "difference ≈ the mean square count", but:
  - Mean Z is −2.124 for primes and −3.068 for squares, a difference of 0.944. The mean square count is 0.407.
  - The standard error of the difference is about 4.87·√(2/150) ≈ 0.56, so the gap is about 1.7σ and not significant.
  - Prime strips with no squares already average −2.322. Most of the gap is therefore the −Σν/P₀² term or class effects, not squares.
- *Fix.* Say instead that the n-average does not resolve the square contribution at this sample size, and that the
  pointwise conclusion stands.

**F5 — MINOR. §5.2(b), the general-shape statement.**
- *Problem.* "every implementation has block exponent ≥ (2β + γ/2)/3 − o(1)" is proved only when L₀ ≥ Q, i.e. W ≥ V/ξ₀
  (roughly γ ≥ β). It also implicitly needs at least one pair q, q′ ≥ 11 in 𝒫, i.e. P ≥ 11; if P < 11 only V/P remains.
- *Fix.* Add the hypothesis γ ≥ β (or W ≥ V/ξ₀). The balanced-block claim is unaffected.

**F6 — MINOR. Theorem A′ / §4.5, last paragraph.**
- (a) The condition y ≥ N^s with s = 2 is |ℓ|n ≥ 4W². It holds because γ ≤ 13/37 + o(1) < 1/2 in Case 2 (and for S₁),
  not "for N = W/Q ≥ N₀". N ≥ N₀ is a separate requirement, needed for the shifted phase −X/(j + c₀/Q) to lie in
  F(N, P, 2, X, c). State both.
- (b) The j-range ((W−c₀)/Q, (2W−c₀)/Q] is not contained in [N, 2N]. Peel off the ≤ 1 integer below N. Treat ℓ < 0 by conjugation.
- (c) Bourgain's Theorem 6 has only a sketched proof, and its "suitable F" hypotheses are not listed (LIT_CHECK §1).
  Write "relative to Bourgain's Thm 6 as an exponent pair in the G-K / Tao–Trudgian–Yang model-phase sense".
  That is a conditional-on-literature label, not a plain PROVED.
- (d) In the general statement, note κ < 1/4: at κ = 1/4, ρ* = 0 at the vertex and θ = 1/3 is trivial.

**F7 — MINOR. §1 (S3): "every square-sieve datum of fixed (auxiliary) conductor is the same at odd squares".**
- *Problem.* Only the complete sums G and the ℓ = 0 terms depend on n through n mod Q (§6 states this correctly). The S_Q
  themselves depend on n through e(−ℓn/(4CQ)). §7.2 shows different values, all of the same square-root size.
- *Fix.* Use the §6 wording.

**F8 — MINOR. §1 (S2) versus §5.2 and §9.**
- *Problem.* §1 says the route "needs beyond-square-root cancellation in the dual C-sums". B2(a) shows that ℓ-uniform
  beyond-√N bounds are impossible, and §9 says the missing input is a *bilinear* (ℓ, C) estimate.
- *Fix.* Align §1 with §9.

**F9 — NIT.**
- Prop D assumes Q ≤ W but never uses it: with W/Q < 1 the trivial bound "+2" applies. Say "not needed", or drop the hypothesis.
- §4.4(i): #((W, 2W] ∩ ℤ) = W only for integer W. W = 1/2 gives 1. This is irrelevant in Case 2.
- Lemma C3 uses the letters B and C for coefficients, which clash with the triple variables B and C. Rename them (e.g. D(x) = a₀ + a₁x + a₂x²).
- §3, Lemma W sketch: "Ramanujan-type sum of modulus 1" should read "absolute value 1".
- §5.1 says "no grid", while `reach.txt` is a 1/20000 grid. The endpoints are exact (verified above), so cite the hand solution.
- §5.2 Remark 3: "the Heath-Brown–Pierce paper of that title area" is garbled.
- §4.5 omits the dominated terms β − γ − ρ and −ρ from the printed list. Mention them for completeness.
- §1 announces "Proposition B" and "Theorem C", but the body has only B2 and C1/C3/C4 (there is no B1 or C2). Harmonise the names.
- §4 compares the cube "n^{8/25}" with "n^{17/54+ε}". HYPSUMPROD's bound carries (log n)², not n^ε.
- §12 reproduction: the checks script takes about 3 s, not "~2 min". Lemma W(d) (CRT) is not covered by any repo check;
  add one (I verified it).
- Lemma P's numerical check uses a Gaussian, which is not C_c^∞. Note that Lemma P holds for Schwartz Φ.

## Labels
- **Theorem A.** PROVED (relative to Weil and Titchmarsh 5.11). Justified.
- **Theorem A′.** Should carry a conditional-on-literature qualifier (F6c).
- **Cor A″.** CONDITIONAL. Correct.
- **§5.1.** PROVED. Fine; exact.
- **B2.** Justified as PROVED only after F1 (and F5).
- **C1, C3, C4(a).** PROVED. Fine.
- **"(H) CERTIFIED".** Not justified as written (F3).
- **F3 falsifier.** EVIDENCE. Fine, after the F4 fix.
- **S3 "dead", "cannot".** Should be Assessment (F2).
- **Novelty.** The memo makes no explicit priority claim; LIT_CHECK records a negative search only. Acceptable, but keep
  the "internal, unrefereed; no predecessor found" wording in the FRONTIER text. Poisson in the sieved variable followed by
  complete sums is the standard square-sieve technique (Heath-Brown 1984); the new part is only its application to this strip.

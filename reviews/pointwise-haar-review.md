# Hostile review R46 of POINTWISE_HAAR.md (branch side-agent/haar-exponent)

Reviewer branch `side-agent/review-haar`. Reviewed commit: 6f4ca8b.
Status: IN PROGRESS.

## Verdicts per claim

* **Lemma 1.1** — SOUND. Re-derived: given A, each compatible C becomes
  C' ⊇ C independent of S_A; ⋂C̄' ⊂ ⋂C̄.
* **Lemma 1.3** — SOUND (re-derived). Lopsided condition P(E|Av(S')) ≤ P(E)
  for S' ∩ Γ(E) = ∅ is exactly Lemma 1.1. Split S = S1 (conflicting with A) ∪ S2;
  P(A|Av(S)) ≤ P(A|Av(S2))/P(Av(S1)|Av(S2)); numerator ≤ P(A) (Lemma 1.1),
  denominator ≥ ∏(1−x_E) by the LLL induction (valid for every subfamily S').
* **Theorem 1.4** — SOUND. Re-derived line by line: P(E_i|B_i) ≥ P(E_i)P(B_i|E_i)/P(B_i^d)
  (B_i ⊂ B_i^d); given E_i, conflicting E_j vanish, compatible E_j become E_j' independent
  of S_i; P(E_j'|B_i^d) ≤ K P(E_j') by Lemma 1.3 (conflicts with E_j' ⊂ Γ(E_j)); sum with
  −log(1−p) ≥ p. Second bound: random thinning, p = min(1, μ/(2KΔ)); K, x_E inherited
  by subfamilies. Directions of all inequalities correct.
  From-scratch exact brute force `scripts/review_haar_janson_bf.py` (Fractions, random
  non-uniform marginals, one-hot coordinates, ranges 2–6, 2–10 events, all subfamilies S
  for Lemma 1.3, plus random external atomic A): seed 1×1500 instances (454 with valid
  LLL weights x_E = tP(E)) and ADV seed 2×300 (292 valid, 6–10 events with ≥2 coordinates
  each): **0 failures** of Lemma 1.1, Lemma 1.3, both bounds of Thm 1.4. Tightest
  (μ−KΔ) − (−log P(Av)) = −2.6e-5 (single-event-like instances).
  Scope caveat (author states it): single-value atomic events only; prime-power moduli not
  covered. §2 uses squarefree y-rough M, so fine.
* **Event system §0 vs δ*(T)** — SOUND. Matches POINTWISE_SIZE §7 Prop 7.1(a)
  definition verbatim (Haar on Ẑ^×, n ≡ 1 (24), forbidden n ≡ −4D (M), M ≡ 3 (4), M ≤ T,
  D | A_M²). gcd(A_M, M) = 1 so residues are units; ℓ | M ⇒ ℓ ∤ D. 𝓕 ⊂ full system, so
  δ*(T) ≤ P(Av(𝓕)) is the correct direction. Coordinates at ℓ > 3 independent uniform on
  (ℤ/ℓ)^× under the 1 (24) normalisation.
* **Lemma 2.2 (mass)** — SOUND (re-derived). D | A² ⟺ D* | A, exactly 2^{ω(n)} D with
  D* = n; n | A_M ⟺ M ≡ −1 (4n). Sieve: modulus 4n ≤ 4X^{1/5}, z = y = 𝓛^5, level X^{1/2},
  s ≥ 𝓛/(20 log 𝓛) → ∞, |r_d| ≤ 1 so remainder ≤ X^{1/2}; main X^{4/5}/(log 𝓛) dominates.
  Hypotheses of the fundamental lemma (dimension 1, g(p) = 1/p for p ∤ 2n) hold uniformly in n.
  Non-squarefree removal fine. Σ_{n≤x} 2^{ω(n)}/n ~ (3/π²) log² x correct.
* **Lemma 2.3 (LLL hypothesis)** — SOUND (re-derived). w_q bound via F2/F4/F3 correct;
  Σ_Γ ≤ (𝓛/log y)(𝓛³/(2y) + 4𝓛T^{−2/5}) = O(1/(𝓛 log 𝓛)). Remark (iii) check:
  ∏(1−2p) ≥ exp(−(8/3)Σp) ≥ e^{−1/3} > 1/2 for p ≤ 1/8, Σp ≤ 1/8. OK.
* **Lemma 2.4 (Δ)** — SOUND (re-derived). Compatible ⇒ g | D−D'; M = M' ⇒ same event by
  (F1); P(E∩E') = 1/φ(gvv') (squarefree). (a) uniform-in-v bound on Σ_g is legitimate;
  Δ_a ≪ 𝓛^4/y + 𝓛³ log N_0/N_0 ≪ 𝓛 log 𝓛. (b) algebra of the bracket checked
  term-by-term (= (16𝓛/y)[𝓛²(ΣD 1/n)²/16 + …]); main term 𝓛^7/y = 𝓛² exactly at y = 𝓛^5
  (so "≪ 𝓛²" is with constant ≈ 10^{−4}, since Σ_D 1/n ≤ (1+𝓛/10)²). Ordered-pair
  overcount only helps.

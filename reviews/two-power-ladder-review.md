# R283 — hostile review of O272 (TWO_POWER_LADDER.md, 2-power ladder)

Reviewer: side-agent/review-two-power. Reviewed: `side-agent/two-power-ladder` at aff44704. Author's document NOT edited.
From-scratch scripts: `scripts/review_r283_*.py` (no reuse of `scripts/z41_*`). ES is not solved; nothing reviewed claims otherwise.

## Summary verdicts
(filled in claim by claim below; final table at the end)

## Thm 3.2 (Stickelberger dictionary) — verdict: SOUND (m = 3, 4), with MINOR scope/label defects

**Re-derivation.** K = ℚ(ω) or ℚ(i), ℓ ≡ 1 (m), λ primary, ℓ = λλ̄ exactly (both conjugates primary, N > 0); q = ππ̄ exactly.
(q/λ)_m = (π/λ)_m(π̄/λ)_m. Cubic reciprocity (primary, distinct norms) gives (σ_cπ/λ)₃ = (λ/σ_cπ)₃; biquadratic reciprocity gives
the sign (−1)^{((ℓ−1)/4)((q−1)/4)} for c = 1 and for c = 3 — the same sign twice, so it cancels. Galois equivariance
σ_c((α/𝔮)_m) = (σ_cα/σ_c𝔮)_m gives (λ/σ_c𝔮)_m = σ_c((σ_c⁻¹λ/𝔮)_m) = x_{c⁻¹}^c; reindexing a = c⁻¹ gives S = ∏x_a^{a⁻¹}.
D = (ℓ/𝔮)_m = ∏x_a trivially. m = 3: S = x₁x₂², D/S = x₂⁻¹ (free). m = 4: S = x₁x₃⁻¹, D/S = x₃², D² = S² (= quadratic reciprocity,
q ≡ 1 (4)). All correct.

**Sharpness, re-derived independently (stronger than the author's one-line sketch).** B = ⟨σ_aλ⟩ ⊂ K^×/K^{×m} is free over ℤ/m
(valuations). For cyclic H = Gal(K/ℚ) (m = 3, 4), K(β^{1/m})/ℚ is abelian iff σ_cβ ≡ β^c (mod K^{×m}) for all c (central
extension with cyclic quotient ⇒ abelian). Writing β = ∏(σ_aλ)^{i_a}, the condition is i_{c⁻¹a} ≡ c·i_a, i.e. i_a = a⁻¹·i₁: the
maximal abelian-over-ℚ subfield of K((σ_aλ)^{1/m} : a) is K(β₀^{1/m}), β₀ = ∏(σ_aλ)^{a⁻¹}, whose Frobenius at 𝔮 is exactly S.
Hence NO congruence on q (any modulus) sees more of the vector (x_a) than S, and by Chebotarev every vector with prescribed S
occurs with equal density. So "S determines D exactly mod μ_m^{gcd(2,m)}" is sharp for m = 3, 4. ✔

**From-scratch numerics** (`scripts/review_r283_stickel.py`, `logs/review_r283_stickel.txt`; own ℤ[ω], ℤ[i] arithmetic, symbols by
reduction ζ ↦ r mod p, both primes 𝔮 | q tested):
* m = 3: 4 120 pairs (ℓ < 80, q < 3000) + 18 078 pairs (ℓ < 20, q < 6·10⁴): **0 failures** of k_S = k₁ + 2k₂; S ≠ D in 2 754 / 12 070
  of them (the identity is discriminating, not a disguised S = D).
* m = 4: 3 780 + 18 102 pairs: **0 failures** of k_S = k₁ + 3k₃ (the exact sign cancellation holds).
* Primarity of λ is essential: replacing λ by a non-±1 unit multiple breaks the identity in ≈ 2/3 (m = 3) resp. ≈ 1/2 (m = 4) of
  pairs. The theorem does say "λ primary", so fine, but see D2.
* Sharpness: in every cell (ℓ, q mod ℓ) with ≥ 4m² samples (36 cells m = 3, 32 cells m = 4) S is constant and **all m vectors**
  (x₁, x_{−1}) with that S occur.

**Defects.**
* **D1 (MINOR, §3 Thm 3.2 bullet 3 and "Hence …").** "The exponents 1 − a⁻¹ generate gcd(2, m)·ℤ/m … for m odd S says nothing
  about D" is phrased for general m, but the identity S = ∏x_a^{a⁻¹} is only proved for m = 3, 4 (for general m Eisenstein
  reciprocity needs m = odd prime, ideal-theoretic symbols, and the primary normalisation of λ is not available as an element
  identity). Repair: state the conclusion for m = 3, 4, and say for general m odd only the conjugacy-invariant consequence
  that Thm 3.1 already gives.
* **D2 (MINOR, Thm 3.2 statement).** The x_a depend on the element λ, not just the ideal (unit change multiplies S-prediction by
  (uū^{−1}… )/𝔮 symbols; confirmed numerically). Add "(x_a depend on the primary normalisation; D does not)".
* **D3 (MINOR, Thm 3.2 proof, *Realisability*).** "the commutator argument of Thm 3.1 applied to β" only gives the necessary
  condition; the identification of the abelian subfield as exactly K(β₀^{1/m}) needs the converse (central + cyclic quotient
  ⇒ abelian) and the computation i_a = a⁻¹i₁ above. Repair: insert those two lines.
* **D4 (MINOR, label, "Reading").** "that is the whole reason the BM layer is free … and the whole reason T1 exists" is an
  interpretation (Assessment), not part of the PROVED statement. Relabel.

## §5 census (2-group levels) — verdict: SOUND (numbers reproduced exactly); Assessment label appropriate

From scratch (`scripts/review_r283_census.py`, `logs/review_r283_census.txt`): own T2 generator, residue-class **sieve** via Lemma 1.1
(mark n ≡ −u mod tu − 1, n ≥ 2(tu−1) − u) instead of the author's enumeration, plus an **independent divisor-based** check
(factor tp + 1, look for d ≡ −1 (t), d, N/d ≥ 2t − 1) on 150 random failing and 150 random hit primes per range.
* |T2 ∩ [4, X+2]| = 169 (X = 10⁶), 237 (X = 10⁷) ✔. Failing primes: **1 298** ≤ 10⁶ (largest 999 979), **5 320** ≤ 10⁷ (largest
  9 994 727) ✔. Decade rates 0.2168, 0.0688, 0.0293, 0.0136, 0.0069 ✔. Odd non-squares ≤ 10⁶ failing: 20 325 ✔. Squares hit: 0 (10⁶
  and 10⁷) ✔. Baseline all 4 | t: 118 primes, 1 939 non-squares, 0 squares; 1 180 T2-failing primes have a 4 | t word ✔.
  131: no 8 | t word, has a 4 | t word; 241: neither ✔.
* Divisor spot check: 0/150 failing primes actually have a word, 0/150 hit primes lack one (both X) ✔.
* **D5 (MINOR, §7 "rate halving per decade").** The ratios are ÷3.2, ÷2.3, ÷2.2, ÷2.0 — "roughly halving in the last decades" is
  accurate; "halving per decade" overstates the regularity on 5 data points. The heuristic "expected hits ≍ c·log n ⇒ infinitely
  many failures" is correctly labelled Assessment (failure rate ≈ n^{−0.3} under a naive Poisson model; Lemma 5.1 shows the hits
  are not Poisson-independent, so this is a heuristic only).
* **D6 (MINOR, §5 bullet 1).** "(of 499 500)" counts odd non-squares including n = 1 as a square and n = 3,… — fine, but the census
  ranges are "odd non-squares n ≤ 10⁶" vs primes "5 ≤ p" (2, 3 excluded silently; 3 has no T2 word). Cosmetic.

## Lemma 1.1 — verdict: SOUND
a(tn+1) − n(ta−1) = n + a and t(n+a) = (tn+1) + (ta−1), with gcd(a, ta−1) = gcd(t, ta−1) = 1: both directions ✔. MINOR (D7): the
lemma is stated for D⁻_t > 0 (a ≥ 1, includes the boundary d = t − 1); the ES word event R_t > 0 is the sub-union a ≥ 2 with the
extra condition n + a ≥ 2(ta − 1). Still a congruence union (above a threshold), so the conclusion stands; say so.

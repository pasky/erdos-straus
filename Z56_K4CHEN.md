# Z56_K4CHEN — Chen-type switching and weighted sieves for K(4) (p + 4 ∈ S exact, Ω_𝒬(4p + 1) small)

**ES is OPEN.** Nothing here proves or disproves it. All results are internal (internally reviewed only).
Lane K4CHEN (wave z56). Scripts `scripts/z56_k4chen_*`, data `data/z56/k4chen/`.
Notation as in `Z55_P415.md`: 𝒬 = primes ≡ 3 (4); S = {n : all prime factors ≡ 1 (4)}; N₁ = p + 4, N₂ = 4p + 1;
Ω_𝒬 = number of 𝒬-prime factors with multiplicity; F, f semi-linear beta-sieve functions; units X𝔊W(z₁)W(z₂).

*(Checkpoint 1 skeleton — superseded sections will be rewritten in the final memo.)*

## 0.1 Statements attacked (precise)

* **C(r)** (r even ≥ 0): there are ≫ x/(log x)² primes p ≤ x, p ≡ 1 (mod 8), with p + 4 ∈ S and Ω_𝒬(4p + 1) ≤ r.
  (Ω_𝒬(4p + 1) is always even since 4p + 1 ≡ 1 (4); so "≤ r" with r odd is "≤ r − 1".)
  C(0) = P(4,15) = K(4) (HCKILL Lemma 1.1). Z55_P415 Theorem U (PROVED relative to BV + standard sieve inputs) gives
  C(r₀) for an unspecified absolute r₀; its *model* (Assessment) gives r = 10.
  **Chen-type target:** C(2) ("4p + 1 ∈ S or 4p + 1 = s·q·q′ with s ∈ S, q, q′ ∈ 𝒬"), the analogue of Chen's P₂.
* **Ledger L(r)**: the smallest level θ of distribution (for primes in the CRT classes of (p + 4)(4p + 1); switched
  sums at BV level 1/2 or at θ) for which the vector-sieve + switching + weighted-sieve model proves C(r).
* Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / Assessment. Model numerics are Assessment unless a step is
  derived.

## 0.2 Why not closed

P415 proved only "bounded" (unspecified δ) and gave an unaudited Richert-weight model number (Ω_𝒬 ≤ 10). Not in
FRONTIER §6 or the closed list: no weighted-sieve optimisation, no Chen-type (parity-aware) weights, no level ledger
r ↦ L(r), no derivation of the switched main term (the "pen = 1" model) has been done.

## 0.3 First falsifier (done): additive weights cannot beat Richert at BV — LP optimum

`scripts/z56_k4chen_lp.py`: for the P415 model, the *optimal additive weight* W(N₂) = 1 − Σ_{q|N₂, q≥z₂} w(log q/log x)
(any w ≥ 0, piecewise constant, h = 0.004) subject to the parity covering constraint "every multiset of r + 2
numbers α_i ≥ ζ with Σα_i ≤ 1 has Σw(α_i) ≥ 1" (⟹ W > 0 forces Ω_𝒬(N₂) ≤ r) is computed by an LP with an exact
knapsack separation oracle. Result (θ = λ_sw = 1/2, pen = 1; θ₁ ∈ {0.36,…,0.46}, ζ ∈ {0.004,…,0.03}):
* r = 10: margin +0.046 (θ₁ = 0.42, ζ = 0.008) — reproduces P415's Richert result (Ω_𝒬 < 10.44 ⟹ ≤ 10).
* r = 8: best margin −0.024 (same point): **fails on this grid**.
* The LP-optimal w is Richert's linear weight λ(1 − α/y) (y ≈ x^{0.34} for r = 8). So within additive weights the
  P415 model number is essentially optimal at BV; improvements must come from elsewhere (main term / switching /
  level). EVIDENCE (grid-limited), Assessment.
Budget at that point (units X𝔊W(z₁)W(z₂)): main fvec = 0.494, switched T₁ = 0.214, weighted cost 0.234 (r = 10) /
0.304 (r = 8); the "truth" of the exact count is ≈ F(1)√θ₁ ≈ 0.98: the exact-N₁ lower bound has efficiency
(0.494 − 0.214)/0.98 ≈ 29 %. This is the main inefficiency to attack.

## Plan
1. Fine optimisation at BV (all parameters jointly) — does C(8) hold in the model?
2. Ledger r ↦ L(r) incl. C(2) and C(0); compare with P415's 0.996.
3. Derive the switched main term (pen = 1) as an Euler-product identity (upgrade of the model's key assumption).
4. Structural levers: fixed-residue levels for the N₁ condition (p ≡ −4 mod d is a fixed residue: BFI/Maynard/Lichtman
   type inputs) — CONDITIONAL ledger; r(N₁)-weights (divisor-sum exactness at level exactly 1/2); Chen-type switching
   for N₂ configurations.

# Hostile review R81 of EXCEPTIONAL_WEIGHTS.md (O81, branch side-agent/weights-below-one)

Reviewer: R81 side agent (branch side-agent/review-weights). Round 1.
Scripts (from scratch, none of the author's code reused): `scripts/review_weights_*.py`.

## Summary verdicts (filled in progressively)

| claim | verdict |
|---|---|
| Lemma 1.1 | SOUND |
| Lemma 1.2 | SOUND (checked numerically, primal/dual brackets overlap) |
| Thm 2.1 / Lemma 2.0 | SOUND (constants re-derived; brute-force LP chain holds with ≥ 8× slack) |
| Cor 2.2 | (pending) |
| Lemma 3.1, 3.2 | (pending) |
| Thm 3.3 | (pending) |
| Lemma 4.1, 4.2 | (pending) |
| Prop 5.1 | (pending) |
| Rem 6.1 | (pending) |
| §5.1 EVIDENCE | (pending) |
| §0 table / labels | (pending) |

## Detailed checks

### Lemma 1.1, Lemma 1.2 (SOUND)
* 1.1: `Σ_n Ψ(n)ν(n+t) = Σ_θ ν̂(θ)e(tθ)Ψ̌(θ)` and `Ψ ≥ 1_{[1,N]}`, `ν ≥ 0` on ℤ: correct.
  The θ = 0 term needs `w(0) ≥ Ψ̌(0) = ΣΨ ≥ N`, which `w ≥ |Ψ̌|` gives.
* 1.2: Parseval normalisation `Σ_{n mod Q} gν = QΣ_θ ĝ·conj(ν̂)` is right; the equality
  case gives a real g because w is even and ν real; Sion applies with G compact convex
  and `{ν ≥ 1_𝒜}` convex; attainment of the min uses `w(0) > 0`. Verified numerically
  (`scripts/review_weights_thm21.py`): primal `min Σ|W_N||ν̂|` and dual `max⟨g,1_𝒜⟩`
  computed by independent polygon-LP brackets overlap on 10 toy systems (Q = 60, 90).

### Lemma 2.0, Theorem 2.1 (SOUND)
Re-derived line by line:
* Selberg/Beurling majorant `Φ_K(x) = ½[B(Kx) + B(K(1−x))]` (B = Beurling's function):
  numerically Φ ≥ 0, Φ ≥ 1 on [0,1], ∫Φ = 1 + 1/K to 5 digits (K = 1,2,3).
* Poisson: `W_N(θ) = Σ_k NΦ̂(N(k−θ))`; supp ⊂ `‖θ‖ ≤ K/N`, `W_N(0) = N(1+1/K)`. Numerically
  off-band |W_N| ≤ 3·10⁻⁹ (truncation), W(0) exact, and `max|W_N| = W_N(0)`.
* `k̂_δ = (1 − |ξ|/δ)_+`; `v̂ = 1` on |ξ| ≤ δ, 0 for |ξ| ≥ 2δ; periodisation equals 1 on
  `‖θ‖ ≤ δ` needs only δ ≤ 1/3 (author has δ ≤ 1/4). `|v| ≤ 2k_{2δ} + k_δ ≤ 5δ` and
  `≤ 2δ(πδx)⁻²` (so the stated envelope holds with room: numerically max ratio 0.60).
* Block sum: `5δM(L)(2 + 2·(1/6)) = (35/3)δM(L) ≤ 12δM(L)`; blocks j ≤ −2 use
  `|x| ≥ (|j|−1)L` — correct. Numerically the worst block-sum ratio is 0.52.
* `Σ_r g(r) = Qĝ(0) ≤ W_N(0)`; `12δN(1+1/K) = 12(K+1)`. Correct.
* Brute force (`scripts/review_weights_thm21.py`, 30 toy sets: random densities 0.3/0.05,
  one block, AP step 7, single point; (Q,N,K) ∈ {(60,12,1), …, (240,40,4)}): with the
  true |W_N| weights, `M(N) ≤ D ≤ RELAX ≤ 12(K+1)M(⌈N/K⌉)` in every case, where RELAX is
  the LP keeping only what the proof uses (g ≥ 0, band, mass). Observed `D/M(N) ∈ [1.09,
  1.58]`, `RELAX/(12(K+1)M(L)) ≤ 0.114`. The constant 12(K+1) is generous but correct;
  the (K+1) growth is real (single-point set: RELAX ≈ 1.05(K+1)).

## Defects

(pending)

# R198 — hostile review of CHI_FLIP.md (O198)

Reviewer: R198 (side agent). Document reviewed: CHI_FLIP.md at side-agent/chi-flip 42909547, with
reviews/agent-reports/AGENT_REPORT_O198.md. From-scratch scripts: scripts/review_cf_*.py (none reuse cf_*).
**ES is not solved here, nor any infinite case of it.**

## Summary verdicts
* **Thm 1.1** (χ = −ε₂(Q_w); local formulas) — **SOUND.** Re-derived every local invariant (see V1). From-scratch check
  `scripts/review_cf_hasse.py 2000`: all 50 008 positive words of all odd n ≤ 2000 (17 503 with n prime): det G_w = n,
  G_w positive definite, ε_∞ = −1, product formula, ε_ℓ = (−A/ℓ)^{v_ℓ(n)} at every odd ℓ | 2n·D₁D₂, and χ = −ε₂ with ε₂
  computed **two independent ways** (Hilbert symbols of a diagonalisation, and a brute-force mod-8 isotropy test):
  0 failures. Mutation tests (sign of the claim flipped; 2-adic Hilbert symbol replaced by 1) give 4 734 / 1 640
  failures at n ≤ 300, so the check has teeth. Author's counts 39 921 (letters ≤ 40) and 9 924 (prime n < 1200)
  reproduced; the "26 750" is the count for 3 ≤ n < 1200 (26 755 with the five words of n = 1) — immaterial.
* **Cor 1.2** (χ a 2-adic cell function, n-free) — **SOUND**; the period-8 statement can be made self-contained (D2).
* **Cor 1.3** (certificate ⟺ ℚ₂-isotropic ⟺ C₀ ≅ B_{p,∞} ≅ (−A*, −vA*p); else B_{2,∞}) — **SOUND** (wording minors D3).
  Ramification of (−A*, −vA*p) checked on all 17 503 prime-n words ≤ 2000: {p, ∞} iff χ = −1, {2, ∞} otherwise.
  Gross–Lucianovic: disc(Q_w) = 4tuv − 4u − 4v = 4n with their discriminant normalisation, Q_w primitive (n odd ⟹
  not all letters even), so the order is Gorenstein of reduced discriminant 4n — correct.
* **Cor 1.4** (χ n-free; scaling preserves χ; DK normalisation artefact) — **SOUND-AFTER-REPAIRS** (MAJOR D1: the
  correction is right about scaling but incomplete — in DK's own normalisation (A/n) *rotations* also flip, so
  "scaling is the only flip" was false in *both* normalisations; the ledger lines to fix are listed in D1).
  `scripts/review_cf_moves.py`: 60 480 scalings (a ∈ {3,…,15} odd, letters < 25): χ never changes, and (A/n) flips
  exactly when a ≡ 3 (mod 4).
* **Prop 1.5** (rotation law) — **SOUND** (proof relative to the cell lemma; D2 makes it unconditional).
  `review_cf_moves.py`: 78 213 positive odd→odd rotations, letters < 60, all 192 cells hit, 0 violations of
  "flip ⟺ t, u, v odd and t ≢ u (mod 4)". "Not a function of (n, n′) mod 8" confirmed: both values occur for each
  of the eight pairs (n, n′) mod 8 with n ≢ n′ (mod 4); χ is preserved on all eight pairs with n ≡ n′ (mod 4).

## Defects
(in progress)

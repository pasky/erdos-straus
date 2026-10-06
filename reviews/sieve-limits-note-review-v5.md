# Referee report R65 — paper/sieve-limits-note.tex, version 5

Branch reviewed: `side-agent/sieve-paper-v5-2` @ bdb61bc (merged ff into `side-agent/referee-sieve-v5`).
Referee: R65 (hostile). Scope: everything new/changed v4 → v5 (diff 66191c6..bdb61bc).

## Compilation
pdflatex ×3 in a clean dir: 71 pp., no undefined refs/citations, no multiply-defined labels;
one pre-existing overfull hbox 1.29pt (lines 3818–3825). OK.

## Verdicts per claim

### §14.5 Smooth–rough splitting
* **Thm 14.12 (smooth–rough splitting) — SOUND.** Re-derived: HY on Z/M_s with
  f = M_sπ_s(c)π̂_c(θ_r) gives Σ_{θ_s}|π̂|^{p'} ≤ (Σ_cπ_s(c)(M_sπ_s(c))^{p−1}|π̂_c|^p)^{p'/p}
  ≤ ρ^{(p−1)p'/p}(E|π̂_c|^p)^{p'/p} ≤ ρE|π̂_c|^{p'} (Jensen, p'/p ≥ 1; (p−1)p'/p = 1).
  Hölder with exponents p'/2, q=(1+β)/β and Σw^q ≤ N^{1−q} gives F_w ≤ (R/N)^{1/(1+β)}; then
  log(N/B) ≤ (β log N + log R)/(1+β) ≤ β log N + log R. From-scratch random check
  `scripts/review_r65_smoothrough.py` (3000 instances, (a) HY+Jensen, (b) Hölder, (c) per-prime
  bound Σ_{a≠0}|φ|^{p'} ≤ g^{1+2β}): worst ratios 1.000000 / 0.976 / 1.000000 (equality cases
  attained, never exceeded).
* **Lemma 2.1 of LS3 in prose (density of π_s) — SOUND** as a transcription (inputs (Q1)–(Q4) of
  KA2; R59 D6(a) about Q₀ ∤ M_s is not mentioned in the paper but is harmless by marginalisation —
  see minor point).
* **Thm 14.13 (rough-slice mixtures) — SOUND (given KA2 §§2–4).** Author's check point 1
  confirmed: 𝔐(y) in KA2 §3 is a sum over the *universe* 𝔘 of all classes of the four types with
  W < P(G) ≤ y, no size bound on G (only y-smoothness), and (Q1) holds for every family ⊆ 𝔘; the
  J-integral α∫_z^∞𝔐(y)y^{−1−α}dy ≪ α^{−3}(log 1/α)^3 (t = log y) is therefore uniform in moduli
  size. Chebyshev for E₁ (ℓ^{2−2κ}Ep_ℓ² = ℓ^{1/2}·ℓ^{−7/4+o(1)}, summable from z) and Markov for E₂
  are correct; the constant 64 = 4·16 matches the per-prime bound 4pℓ^{−α} (checked in (c)).
* **Hyp 14.14 (H_rough) — labels SOUND** (conjecture; sufficiency only, R59 D1 respected). See
  minor point on the added "primes ≤ N^{O(1)}".
* **Lemma 14.15 (residue concentration) — SOUND.** D=1 in Lemma 3.1's description of 𝓡(M)
  gives −4; Σ_{M'≤X, P⁻(M')>z, one class mod 4}1/M' ≍ log X/log z by Mertens/Buchstab
  (needs X ≥ z^{1+ε}, true for X = N^A).

## Defects
(in progress)

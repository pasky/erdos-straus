# R230 — hostile review of O229 (CAP_GROWING.md, BRAINSTORM/z5_*.md)

Reviewer: R230 side agent. Author branch merged: side-agent/cap-growing. From-scratch scripts: scripts/review_r230_*.py.
Status: in progress.

## Summary verdicts (filled in as checked)

### Prop 1.3 (overflow cube) — SOUND
Re-derived: 4(x + c₀²d₀R²) = E(ℓ+1) = 4EK ⇒ x + c₀²d₀R² = EK ⇒ 1/y + 1/z = (x + c₀²d₀R²)/(p c₀d₀j x) = E/(px) = 4/p − 1/x.
Integrality: Eℓ ≡ p (mod 4c₀d₀) and ℓ ≡ −1 ⇒ 4c₀d₀ | p + E. Valuations at s | R: s ∤ E (Eℓ ≡ p ≢ 0 mod s), v_s(x) = σ
because 2σ + 2ρ > σ, so v_s(z) = −2ρ; for s ∤ R, c₀ | x gives v_s(z) ≥ 0. All ES^{(y,e)} side conditions (s odd, s ∤ p,
s | y, even valuation ≥ −2e) hold. `scripts/review_r230_cube.py 2000`: sympy residual 0; brute force over EVERY prime
ℓ ≡ 3 (4) < 2000, every factorisation K = c₀d₀j (c₀, d₀ arbitrary), every odd R with rad R | c₀, v_s(R) ≤ 3, three primes
p per class: 78 852 hypothesis-satisfying cases, den z = R² and rad R | y in all. Negative control: all 20 250 cases
violating v_s(c₀) = v_s(K) have den z ≠ R² (smaller), so that hypothesis is genuinely needed for the *exact* den
claim (still harmless: the identity holds and the solution remains in ES^{(y,e)}). No defect.

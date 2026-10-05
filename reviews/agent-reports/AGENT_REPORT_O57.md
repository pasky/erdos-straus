# AGENT REPORT O57 — beyond the 1/4 ceiling? (branch side-agent/beyond-ceiling)

Deliverable: `POINTWISE_OMEGA15.md`, `scripts/omega15_pseudorandom.py`,
`data/omega15/pseudorandom.txt`. Outcome: **precise obstruction, no conditional improvement.**

## Main results
* **Lemma 1.1 (PROVED).** O14's deterministic planted law ν is exponentially pseudorandom: for
  every *reduced product* h (bounded, local factors of mean ≤1/4 at big primes: residue classes,
  Dirichlet characters, additive characters of any modulus) `|E_νh−E_Ph|≤(4r*)^{k+1}`, and 0 if h
  touches ≤k big primes. Exact checks: closed form vs brute force (40), bound (900 cases).
* **Thm 1.2 (Wiener-norm barrier; PROVED mod O14 Thm 4.5 inputs).** Every minorant B≤F (any
  level) on any fibre: `E_HB≤e^{−c𝓛^4/log𝓛}·‖B‖_×`. Contains O14 Thm 4.5.
* **Thm 2.2 + Lemma 2.3 + Cor 2.4 + Prop 2.5.** Linear certificates with full-orbit uniform
  accuracy (classes, characters, additive characters; any true accuracy, GRH included —
  Lemma 2.3: square-root/unit errors are forced on deep orbits; Hölder-averaged accounting too)
  need `log x≥c𝓛^4/log𝓛`. `‖ν−P‖_TV≤e^{−0.6μ*}`.
* **Thm 3.1 (Siegel).** The Siegel-model law `(1−εχ_1)P` has the fake `(1−εχ_1)ν`; for low
  level, `E_{P_1}B≤0` exactly — closes O14 Cor 4.6's "Siegel positivity" item for linear
  transfers.
* **Prop 4.1 (integers).** Same barrier for integer Type I sums `Σ_{n≤x,d|n}F(n)` (Haar on Ẑ, an
  exceptional set of measure `e^{−c𝓛^6}`), under full-orbit uniform accounting.
* **Prop 5.2.** Finite-range prime-only minorants of a single modulus `≤x^{1/5}/(QT)` have
  `E B≤0` (Linnik–Xylouris; uses the single-prime event `n≡−4 (ℓ_0)`).
* Reading (Assessment 4.3): the 1/4 ceiling is a sieve-*dimension* barrier (κ≍𝓛³/log𝓛,
  needed level superpolynomial `x^{𝓛^{1−o(1)}}`), a property of F; Type II / parity / Siegel
  input address the prime half. Maynard's restricted digits: complexity `≤X` (period = range)
  vs ES `x^{𝓛/polylog}`.

## Not covered (precise residual, §6)
(N1) non-periodic structure (integer analogue: squares avoid everything, Remark 4.2);
(N2) **support-aware / finite-range accounting** (e.g. classes mod q>x with least rep >x are
empty) — the main gap, flagged by the self-review; Prop 5.2 handles single moderate moduli only;
(N3) non-linear certificates (pair statistics, density increment); (N4) non-class-ℓ¹ evaluation
of integer Type I sums.

## Self-review
`review` (deep) over `main..`: no FATAL; MAJOR items (Siegel norm closure; "oblivious" overclaim;
Type I/II overreach; integer error-accounting rule) repaired by rescoping to "full-orbit uniform",
atom norm in Thm 3.1, Cor 4.3 → Assessment, and Prop 5.2 + (N2). Minors applied.

## Suggested ledger entry (H)28 (for the parent)
"Wiener-norm barrier (POINTWISE_OMEGA15): every minorant of F has `E B≤e^{−c𝓛^4/log𝓛}‖B‖_×`;
full-orbit uniform linear transfers (GRH, characters, additive characters, Siegel-model law,
integer Type I sums) cannot beat 1/4. PROVED mod (G), effective Page, fundamental lemma. Open:
support-aware/finite-range certificates (N2), non-periodic structure, non-linear methods."

Replay: `PYTHONPATH=scripts uv run python scripts/omega15_pseudorandom.py 1` (~1 min).

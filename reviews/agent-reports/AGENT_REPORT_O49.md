# AGENT REPORT O49 — junta bottleneck toward 1/3 (branch side-agent/junta-third)

Checkpoint 1. Deliverable: `POINTWISE_OMEGA14.md`, `scripts/omega14_planting.py`,
`data/omega14/planting.txt`. Merged: side-agent/beyond-fifth, then main (O13 final, Thm 5.1).

## Outcome: a proved negative result (the junta `𝓛·S` is forced for dense minorants)

The brief asked for a minorant with cell modulus `≪S·polylog`, or a proof that `≍𝓛·S` is
forced. Result: **forced, up to logs, for every bounded-level minorant B≤F that keeps a
non-negligible share of the avoider mass.** This is not specific to BRW.

* **Lemma 1.1 (planting; PROVED).** Independent bits with odds `r_i`. If `Σr_i≥(k+1)+(2k+1)max r_i`,
  there is an explicit law with the same `≤k`-marginals and no all-zero configuration. It is
  the LP dual of lower-bound sieves (in the spirit of BGP/PYY; no novelty claimed).
* **Theorem 1.3 (abstract level barrier; PROVED).** Suppose every event has exactly one "big"
  coordinate, and B≤F is a sum of functions each reading `≤k` big coordinates. Then
  `E B≤E[F·1{R(X_s)<k+1+o(k)}]`, where R is the conditional big-event odds mass given the
  small coordinates.
* **ES instance (§2; PROVED modulo BV and the fundamental lemma, via POINTWISE_HAAR Thm 1.4).**
  * *Big family* (Lemmas 2.1–2.2). Take ES atoms `M=vℓ` with ℓ prime `>T^{0.6}` and v y-rough
    (HAAR's family restricted). Each has exactly one big prime, and the family's mass is
    `μ≫𝓛³/log𝓛`.
  * *Lower tail of R under avoidance* (Lemma 2.3). Apply Janson to an m-copy system
    (`m≍𝓛/log𝓛` independent copies of the big coordinates).
  * *Theorem 2.4 / 2.6.* On O13 Thm 5.1's fibre, or on any fibre with `log Q≤𝓛^5`, take a
    minorant whose characters/cells have conductor `≤D` with `log D≤c𝓛^4/log𝓛`. It has
    `E B≤exp(−c'𝓛^4/(log𝓛)²)`, which is `≤δ·exp(−𝓛^{4−o(1)})`.
* **Consequences.**
  * O13 Thm 5.1's `log Z≪𝓛^4log𝓛` is optimal up to logs for BRW-type transfers (Cor 2.5).
  * EL_mod(τ) is false for `τ≤c𝓛^4/log𝓛` (Cor 3.1). So brief route (i) is impossible:
    no sharper C-1 weighting exists.
  * Routes (ii) (exact single-prime treatment) and (iii) (Selberg-type quadratic minorants)
    are covered by the same theorem. Single-prime events are not the issue: their mass is
    only `≍𝓛²`. The obstruction comes from events `M=vℓ` with one big prime.
  * Mechanism: conditioned on the coordinates below `T^{0.6}`, the problem is a sieve of
    dimension `κ≍μ` on the primes `>T^{0.6}`. The sieving limit `β_κ≳κ` forces level
    `≈e^{𝓛μ}`.

## Scope / what is NOT claimed

* **Open loophole (Prop 2.7, scope note).** O9 Thm 1.1's cost `(1+log A)log Z` is
  scale-invariant (`A=E|B|/E B`). So a *sparse* low-level minorant, with tiny mean but small
  A, is not excluded. Prop 2.7 shows that such a minorant's mean must sit on a set of Haar
  measure `≤e^{−3mμ/8}` that is not of low level. No such minorant is known.
  "1/4 is the ceiling of all minorant-based transfers" is therefore an **Assessment**.
  Proposed follow-up O49b: prove `log A·log Z≫𝓛^4/polylog` (or `log A≫𝓛^{…}`) for every
  level-D minorant.
* Nothing about ES itself, and nothing about arguments that bypass a Haar minorant of F
  (e.g. Type II / bilinear prime input, parity-sensitive input).

## Checks

* Exact rational verification of Lemma 1.1's ν: 100 instances, `k=0..3`, `n≤22`, including a
  zero-probability coordinate. 0 failures (asserted).
* Toy LP for the optimal level-k minorant of `1[all zero]`. The optimum vanishes already at
  `R≈k` to `R≈k+1`, below the sufficient threshold (1.1). So the constant in (1.1) is
  conservative only by a constant factor.
* Self-review (deep reviewer): no FATAL. One MAJOR: the universal-ceiling overclaim, now
  scoped to dense minorants with Prop 2.7 added. Minors fixed: script asserts, stratified k,
  `t^{1/5}`, and the truncation wording.

## Inputs to double-check in parent review

* POINTWISE_HAAR Lemmas 2.3–2.4 are inherited by the subfamily for `y∈[𝓛^5,𝓛^A]`.
* The cross-copy pair sum (β) in Lemma 2.3. Its `D=D'` case uses Brun–Titchmarsh in progressions
  mod `4n≤4T^{0.1}`.
* The BV application in Lemma 2.2 (exceptional moduli removed by Cauchy–Schwarz).

Replay: `PYTHONPATH=scripts uv run --with scipy python scripts/omega14_planting.py 1` (~1 min, ≤2 cores).

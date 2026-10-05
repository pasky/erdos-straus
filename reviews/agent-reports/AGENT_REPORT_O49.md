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

## Checkpoint 2 (O49b, §4): the sparse loophole is closed

* **Thm 4.5 (PROVED modulo Gallagher (G), the effective Page bound and the fundamental lemma).**
  Take any fibre with `log Q≤T^{0.05}` and any minorant `B≤F` of level `log D≤c𝓛^4/log𝓛`. Then
  `E B≤0`: no positive minorant exists at all, sparse or dense, for any A.
* **The proof's three ingredients.**
  * *Subfamily (Lemma 4.2).* Use `M=vℓ` with `v≤V=T^{ε/3}≤n=D*≤T^ε`. Then each pair (ℓ,D)
    has a unique v, so the big odds are an exact sum `R(x)=Σ_vΣ_{D≡−x/4 (v)}c(v,n_D)`.
  * *Class-uniform inputs.* The factor `c(v,n)` is bounded below for every residue class
    (Gallagher, Lemma 4.3; the exceptional modulus is removed with negligible loss). So is
    the count of the D's mod v (squarefree numbers in progressions, elementary, Lemma 4.4).
  * *Conclusion.* Hence `R(x)≥c𝓛³/log𝓛` for **every** small configuration x. The planting
    law then exists everywhere (Lemma 4.1), and the sieving limit is deterministic.
* **Cor 4.6.** Exponent 1/4 is the ceiling, up to a factor `(log log p)^{1/2}`, of the
  *certified* bound for every certificate through a Haar minorant of F with a transfer
  requiring `log x≫log Z` (O8/O9/O13 architecture, any A). Within that scope, Prop 2.7's
  loophole is closed.
* **Not covered.** Prime input beyond low-conductor minorants, e.g. bilinear/Type II or
  parity-sensitive input.
* **Please check.**
  * Lemma 4.3's use of (G): the induced-character reduction, and the exceptional-term case split at `q_1=𝓛^{1.9}`.
  * Lemma 4.4's removal of the exceptional set.
  * That Thm 1.3 legitimately treats fibre-fixed coordinates as constant small coordinates.
* **Self-review of §4.** No FATAL; Lemmas 4.1–4.5 hold. One MAJOR: Cor 4.6 is now scoped
  to transfers requiring `log x≳log Z` and stated as a limit on the certified bound. Minors
  fixed: the surrogate weight in Lemma 4.4, the Gallagher prefactor and `ε≤0.05/c`, `9/8+o(1)`,
  the heading, the O9 §1 reference, and section numbering.

## Checkpoint 3 (R49/R49b repairs, applied by O55)

Reviews: R49 (`reviews/pointwise-omega14-review.md`, §§1–3) and R49b
(`reviews/pointwise-omega14-review-2.md`, §4). Neither found a FATAL or MAJOR defect. All minors are
applied in POINTWISE_OMEGA14.md, one commit each. No new mathematics.

* **D1.** Deleted the stale duplicate §5/§4 copy (pre-self-review Cor 4.6).
* **m1 (Thm 1.3).** Added a remark: only finitely many b have `p_b>0`; `dν/dP≤2`, so `B≤F` a.e.
  suffices and integrability is preserved; measurability.
* **m2 (§2 numerics).** The toy-LP values 1.1/1.8/3.0 are now called grid values. R49's
  bisected thresholds 1.11/1.25/2.51 are cited.
* **m3 (Cor 2.5).** Selberg/β-sieve/Bonferroni are blocked only "when used as dense minorants".
* **m4 (§0, after Thm 2.6).** The dense-minorant obstruction needs
  `log(1/δ_fibre)≤c″𝓛^4/(log𝓛)²` (true on O13's fibre by I1(a)).
* **m5 (Lemma 2.3).** Added a separate bound on the unconditional
  `w_ℓ=Σ_{ℓ(E)=ℓ}P(E)≤T^{−0.49}`; the display now uses T^{−0.49}.
* **D2 (Lemma 4.3).** The (G) error terms are written separately for (G-a) no exceptional
  zero and (G-b) exceptional zero (no κ in the exponent), as in O9 §1. Both are `≤x/16` for small ε.
* **D3 (Lemma 4.3/4.4).** `τ(q'')/q''≤q''^{−0.95}≤4𝓛^{−1.8}`, via the divisor bound `τ(m)≤m^{1/20}`.
* **D4 (Cor 4.6).** For O9-type transfers, `log Q≤T^{0.05}` is vacuous (`log x≥C_2log Z≥log Q`),
  so the corollary covers every fibre.
* **D5 (Cor 4.6 "Not claimed").** Added three exclusions: transfers whose positivity comes from
  the Siegel-zero term rather than `E_Haar B>0`; minorants of unbounded O14-level; and
  majorant/minorant mixtures.
* **Status bookkeeping.**
  * §0 now points to §4 for the sparse case.
  * Prop 2.7's scope note is marked superseded.
  * The §5 table is updated with Cor 4.6's scope "(positivity from `E_Haar B>0`, transfer needs
    `log x≫log Z`)", and the header now reads CHECKPOINT 3.

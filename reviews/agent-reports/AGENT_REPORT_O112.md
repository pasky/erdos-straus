# AGENT_REPORT_O112 — repair round for EXCEPTIONAL_TYPEI_LOGLOG.md (branch side-agent/ttl-repair)

Merged `side-agent/heegner-typei` (O111) and `side-agent/review-ttl` (hostile review R111). All repairs are in
`EXCEPTIONAL_TYPEI_LOGLOG.md` and are marked "O112".

## Outcome
**Thm 8.1 (`Σ_{p≤N} f_I(p) ≪ N log² N`): CONDITIONAL on (SEL) for `Γ₀(4dq²)` with even nebentypus mod q.
The proof is now written in full relative to cited results.** The cited results are ET Prop 2.2/Lemma 2.8/(8.1)–(8.2),
MN3 Thm 3.8(1), MN3 Prop 2.3, the DI Thm 2 / Drappeau Prop 4.7 large sieve, the spectral theorem with nebentypus,
BT, the Selberg sieve, Weil and PV. It has **not** been re-reviewed, so the round-2 reviewer should decide the label.
The unconditional statement is unchanged: this argument gives no unconditional improvement of ET.

## Repairs per defect
* **D2 (BT outside R_bad), §8.0.** With `c ≤ N^η`, `b ≥ a/2` (from `f ≤ 2n`) makes `4ad`, `4bd` and the twin moduli
  long. So only `4ab`, `4acf`, `4cdf` can be short. That reduces the problem to three weighted sums:
  - Lemma 8.2: the fibre parametrisations plus Montgomery–Vaughan BT give `≪ η₁^{−1} N L²`.
  - Lemma 8.3 (elementary + PV): (b) `Σ τ(a+b)g(a)g(b)`; (c) `Σ_d g(d) Σ_f ρ_d(f)/φ(f) ≪ D` per dyadic box, via
    `ρ_d ≤ 1∗χ_d` and a PV mean square of `S_d(Y) = Σ χ_d(g)/g`.
  - Sanity checks: `scripts/o112_lemma83.py` (normalised sums ≈ 0.6) and `scripts/o112_checks.py`
    (identities on 43k tuples, 0 failures).
* **D1 (strip `1 < β ≤ 1+η₁`, `D < A`), (b5).** Each cell uses either the f-cusp with `λ = A/(qf) > 1` or BT on 4cdf.
  The saving is `C/max(k, k')`, and the per-cell masses are `≪ N` (Lemma 8.4(b), Lemma 8.3(c)). Summing gives
  `Σ_{k,k'} N/max(k,k') ≪ NL` per c-block, so no c-saving is needed there.
* **D3 (weighted masses).** Lemma 8.4:
  - (a1) single weight `g(s)`, uniform, from MN3 Prop 2.3 with `k = 4l` or `4k²`;
  - (a2) double weight (BT 4ad), split at `k ≤ A^{1/2}` with a trivial tail;
  - (b) per-cell bound when a divisor is `≤ 4A`.
  The model mass is handled by `X_σ ≤ #σ + |r_σ(1)|`.
* **D5.** Prop 5.1 and Thm 6.2 now hold for **all** `λ > 0` via the periodised test function, which has the same
  Fourier coefficients `λφ̂(λn)`. The "#periods" loss is exactly the `n = 0` term `λ²/Y`, i.e. the factor
  `(1 + A/(qF))`, with no `N^ε`. No period splitting is needed.
* **D4.** The strip is `0 < 2α−1+γ ≲ 7/32` (`≥ 0.16` at the smallest cusp parameters). DI Thm 5 is applied with
  `X = 1/(N₀Y)` per dyadic block. "No unconditional improvement" now reads "this argument gives none".
* **D6–D13.** Retired Prop 7.2 reference removed; Drappeau Prop 4.7 and its normalisation; `M = 4dq²` throughout,
  with Γ'' made explicit; Möbius index `½|SL₂(ℤ/q)|` (q > 1) and the stabiliser argument replacing "Witt";
  Siegel non-uniformity remark; the `j = 0` block; `r(d)` with no factor 4 at p = 2 (`(log D)²`).
* **Prop 5.1 at proof level.** One Mellin representation of `K_{it}`: the contour is at `Re s = 1/𝓛` for `|t| ≤ 1`
  and shifted to `Re s = −1` for `|t| ≥ 1`, picking up the residues at `±it`. The dyadic large sieve uses log
  weights over n-blocks, and Gallagher handles the `t_j`-dependent vectors. Eisenstein constant terms are handled
  by unitarity. All tails go through `‖b‖²` (this settles D8; no pointwise K-Bessel bounds).
* **Prop 7.1 at proof level.** Poisson mod `4a²q` and CRT; `|T_q| ≤ 2^{ω(q)}q`. Ramanujan terms use
  `|c_m(k)| ≤ (k,m)`, which gives `D/F + D/E`. Weil with the gcd sum `Σ_{δ|m} δ^{1/2}(r/δE)(r/δF)` gives
  `2^{ω(q)}τ(m) q a`. No cut-offs are needed.

## Self-review (the `review` tool, deep) and fixes
1. **MAJOR, fixed.** The `N^ε` of the large sieve sat in the cusp term exactly at the degenerate end of (b2)/(b5).
   I swapped the cusps: e-cusp in (b2), f-cusp with `λ > 1` in (b5). The degeneracy now sits in the `n = 0` term,
   which carries no ε, and the cusp terms have absolute margins.
2. **Minor, fixed.**
   - Mellin constant is `1/(8πi)`.
   - Gallagher step had an extra factor K, absorbed by `(1+K)^{−B}`.
   - q = 1 / Möbius normalisation in Lemma 6.1.
   - MN3 Prop 2.3 summation ranges must be ≥ 2.
   - The Prop 7.1 level remark (`QN^{−c₀} ≤ N^{−1/3}` in R_bad).

## Points for the round-2 reviewer
1. The e-cusp variant of Lemma 6.1/Thm 6.2 in (b2): same point set, functional `cB − C/d`. The density was
   checked by brute force mod ℓ ≤ 13.
2. The cell bookkeeping in §8 (2b)–(5): bands of width `O(1/L)`, layers `k ≤ C₁ log L`, `(b4)` only for `k ≤ L/3`.
3. Prop 5.1 Steps 5–6 constants and the use of Drappeau Prop 4.7 for each χ (conductor `q₀ ≤ q`).
4. DI Thm 6 / Humphries numerics in §3.2/§9 were not re-checked, and they are labelled that way.

STATUS.md and DISCOVERIES.md were not edited; the parent should set the ledger label after round 2.

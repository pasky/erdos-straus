# Agent report O99 — regime (v) at the sign point `x̂_9` (POINTWISE_TYPEI6.md)

Branch `side-agent/regime-v-units`. Log of Comp 4.1: `reviews/agent-reports/O99_vsearch_log.txt`. Goal: close regime (v) (TYPEI5 Thm 3.7) at `L = 7…10`. **Not closed.** Outcome:
a proved negative for the suggested route, a structural characterisation, a conditional finiteness theorem, and a new
complete engine that extends the `v_7(k)` bound.

## Results
1. **Lemma 1.1 (PROVED).** The gap parameters are norms: `ω = 4j² − uσ = 4mP_1`, `σ = 4λP_1 − 2Tj`,
   `8j − μu = −32c'δP_1X`, and `j = uθ − δ√P/ζ` with `θ = (T/2)(√d − c_oδ)/(√d + c_oδ)`. Regime (v) ⟺ `j² > mP_1`.
   Remark 1.2: the `L = 13`, `b = 1` certificate lies in regime (v) — any closing argument must use `T ≤ 64`.
2. **Prop 2.1 (PROVED).** Idea (1) of the brief fails: over `ℚ[δ]` the norm-1 units of `ℚ[δ][√d]` are `±ε_*^n`,
   `ε_* = (c_oδ + √d)²/(c_oT)`, and for `L ≥ 7` no `ε_*^n` (`n ≠ 0`) is an algebraic integer for any odd `δ` (2-adic
   valuation `n(6 − L)`); likewise with `c_o` as the variable. Schinzel's criterion (cited) gives unbounded CF periods
   along every progression in `δ` (`L ≥ 7`); evidence in `typei6_period.py`.
3. **Lemma 3.1 (PROVED).** `σ = 4uθ² − μδ√P/ζ` exactly; regime (v) forces `16PX² > 64c_o³δ⁷√d/T⁴` — regime (v) is the
   *large-unit* (generic) regime, regimes (ii)/(iii) the small-unit ones.
4. **Thm 3.2 (CONDITIONAL on abc).** abc (`c < K_ε rad^{1+ε}`, `ε < 1/7`) ⇒ finitely many fibre certificates at each
   level `L` (explicit inequality in `δ, a, P`). The abc input is exactly `u = 7^b` (radical 7). With idealised constant
   `K = 1` levels 7–10 would be empty; with published explicit abc forms emptiness is **not** obtained.
5. **Comp 4.1 / Cor 4.2 (CERTIFIED once replayed).** New engine `typei6_vsearch.c` (uses Lemma 3.1(b) as a field bound
   for fixed `b`; cost `≍ (49^bT⁴)^{1/3}`). Regressions: all 5 regime-(v) certificates of `typei4_lb` at `L = 11…18`,
   `b ≤ 3` found, nothing extra; relaxed mode recovers all 7 relaxed regime-(v) solutions incl. at `L = 7, 9, 10`.
   **No fibre certificate at `L ∈ {7,…,10}` with `v_7(k) ≤ 15`**, any height (total ≈ 5.4 h on one core; `L = 10`,
   `b = 15` alone 2.7 h) — previously `≤ 7` (two engines) / `≤ 9` (one engine). Single engine for `b = 10…15`.
6. **§5 (EVIDENCE).** Naive square-probability model, calibrated at `L = 11…20` (predicted 4.4, actual 7), predicts
   `10⁻⁵…10⁻²` regime-(v) certificates at each of `L = 7…10` (`b ≤ 15`), and `< 10⁻¹¹` for `b ≥ 16`.

## Open
Precise residual (§6): fields `d = c_o(c_oδ² + T)`, `c_oδ > 10⁶`, with `u_1(d) = 7^b`, `b ≥ 16`. Unconditional closure
needs control of fundamental units in a two-parameter family (Assessment: beyond current methods).

## Files
`POINTWISE_TYPEI6.md`; `scripts/typei6_identities.py`, `typei6_period.py`, `typei6_vsearch.c`, `typei6_regress.py`.

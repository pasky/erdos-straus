# Regime (v) at the sign point `x̂_9` (task O99)

Status: work in progress (side agent O99, branch `side-agent/regime-v-units`). Not reviewed.
Builds on POINTWISE_TYPEI4.md (Prop 1.2, Cor 1.4, Lemma 3.1) and POINTWISE_TYPEI5.md (Lemma 1.1, Cor 1.2,
Lemmas 3.1–3.2, Prop 3.3, Thm 3.7). Notation as there: a fibre certificate of level `L` is

```
16·P·X² − Q·u² = 1,  u = 7^b,  P = c'P_1,  Q = 7^a Q_1,  P_1Q_1 = M := c_oδ² + T,  T = 2^{L−4},
c_o = 7^a c',  d = PQ = c_o M,  m := c'δ²,  y := c'gδ,  g := 4P_1X − 7^a uδ,
case B: j := Tu/2 − y > 0,  ρ := (Tu/2 + j)/P_1 ∈ ℤ,  λ := (ρj − m)/u ∈ ℤ,
σ := 8·7^a m j + 4Tj − T²u  (= Δ − 2Tj of TYPEI5),  κ := 8·7^a λ.
```

Regime (v) of TYPEI5 Prop 3.3 is `λ ≥ 1`, `σ ≥ 1`.

## 1. The gap parameters are norms (PROVED)

**Lemma 1.1 (PROVED; exact identities, all `L ≥ 5`, case B, any odd `u` with `7 ∤ u`-free hypotheses as in (1.1)).**
(a) `8j − μu = −32·c'δP_1X`, where `μ := 8c_oδ² + 4T`.
(b) `ω := 4j² − uσ = 4mP_1` (so `ω ≥ 4` always; this is the quadratic form `4j² − μju + T²u²` of discriminant `64δ²d`).
(c) `σ = 4λP_1 − 2Tj`. Hence **regime (v) ⟺ `2λP_1 > Tj` ⟺ `j² > mP_1`**, regime (iii) ⟺ `0 < 2λP_1 < Tj`.
(d) `j = uθ − δ√P/ζ` with `θ := (T/2)(√d − c_oδ)/(√d + c_oδ)` and `ζ := 4X√P + u√Q` (the certificate unit, `ζ² = ν_0`).
*Proof.* (a) `j = Tu/2 − c'δ(4P_1X − 7^auδ) = Tu/2 − 4c'δP_1X + 7^a m u`; multiply by 8 and subtract `μu`.
(b) `16ω = 64j² − 16μju + 16T²u²` (expand `σ`; note `8·7^am = 8c_oδ² = μ − 4T`) `= (8j − μu)² − (μ² − 16T²)u²`, and
`μ² − 16T² = 64c_oδ²(c_oδ² + T) = 64δ²d`. By (a), `16ω = 64δ²(16c'²P_1²X² − d u²) = 64δ²c'P_1(16PX² − Qu²) = 64δ²c'P_1`,
i.e. `ω = 4mP_1`. (c) `uσ = 4j² − 4mP_1` by (b); and `4j(ρP_1) − 4P_1(ρj − m) = 4mP_1` with `ρP_1 = Tu/2 + j`, i.e.
`4j² + 2Tuj − 4λuP_1 = 4mP_1`; comparing, `uσ = u(4λP_1 − 2Tj)`. The equivalences: `σ > 0 ⟺ 2λP_1 > Tj`, and by (b)
`σ > 0 ⟺ j² > mP_1`. (d) `4PX = √P(4X√P) = √P(u√Q + ζ^{−1})`, so `c'g = 4PX − c_oδu = u(√d − c_oδ) + √P/ζ`, and
`j = Tu/2 − δ·c'g = (Tu/2)(1 − 2c_oδ(√d − c_oδ)/(c_oT))`… more simply: `√d − c_oδ = c_oT/(√d + c_oδ)` gives
`Tu/2 − uδ(√d − c_oδ) = (Tu/2)(√d + c_oδ − 2c_oδ)/(√d + c_oδ) = uθ`. ∎

*Check.* `scripts/typei6_identities.py` verifies (a)–(d) (and Lemma 1.3 below) exactly / to 50 digits on all
29 relaxed solutions of `typei5_relax` (`L = 7` to `u ≤ 6001`; `L = 8, 9, 10` to `u ≤ 2001`; `L = 11, 12, 13` to `u ≤ 401`;
21 in case B).

*Remark 1.2 (regime (v) is genuinely inhabited above `L = 10`).* The `L = 13`, `b = 1` fibre certificate of TYPEI4 Comp 3.4,
`(c',g,δ,P_1,X) = (79,19,1,1,17)`, `u = 7`, has `j = 291`, `λ = 86582`, `σ = 48344`: it lies in **regime (v)**.
So no argument that closes regime (v) can be uniform in `L`; it must use `T ≤ 64` (as Lemma 3.6 / Prop 3.3(iv) of TYPEI5 do).

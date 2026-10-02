# Hostile review: EXCEPTIONAL_TWIN2.md (task O3), commit 3ea1bcb

Reviewer: side agent (review-twin2). Subject files brought in from
`side-agent/twin-lambda2@3ea1bcb`: `EXCEPTIONAL_TWIN2.md`,
`reviews/agent-reports/AGENT_REPORT_O3.md`, `scripts/twin2_*.py`.
Context read: TW §6.6–6.8 (Lemma 6.6, Red 6.7, Conj 6.8, Lemma 6.10/6.11,
(6.2)/(6.3)), TW Lemma 1.3, ET Thm 5.5 / Cor 5.6.

Verdict scale: SOUND / SOUND-AFTER-REPAIRS / DEFECTIVE. Defects numbered
D1, D2, … (severity: **major** = claimed statement not proved as stated;
**minor** = local slip, fix is mechanical; **nit** = wording).

## Item 1. Lemma 1.1 and Corollary 1.2 (conditional local lemma) — SOUND

Checked line by line. (1) is the Erdős–Lovász induction. (2): with
`𝓢₁ = Γ(B)∩𝓢`, `𝓢₂ = 𝓢∖𝓢₁`, B is independent of `A_{𝓢₂}` (disjoint
coordinate sets), so the numerator is `≤ P(B)`; the denominator bound uses
only (1) applied to `F_i ∉ 𝓢₂ ∪ {F₁..F_{i−1}}`. Correct.
Cor 1.2: each edge at ℓ yields two events of probability `π_e`, so
`Σ_{F∈Γ(E_e)} x_F ≤ 4(w_ℓ+w_m) ≤ 8δ ≤ 1/2`; `x_F ≤ 2π_e ≤ 2δ ≤ 1/8`;
`(1−x)^{−1} ≤ e^{(8/7)x}` gives `exp((32/7)Σ_T w) ≤ exp(5Σ_T w)`. Correct.

## Item 2. Lemma 1.3 (derivative identity) — SOUND

There are no edges inside one coordinate (`ℓ ≠ m`), so "no bad event" is
exactly `A_{−j} ∩ {y_j ∉ F, y′_j ∉ F′}` with F, F′ functions of `Y_{−j}`.
`μ̃_j` is affine in `κ_j`; the slope evaluated on `F^c × F′^c` is
`ν(F∩F′) − ν(F)ν(F′)` (verified). Lower bound for Z₂ by the union bound with
both marginals ν. The point that only `E[J 1_{A₋ⱼ}]` (a number) is divided by
is correct and is a genuine improvement on ET Prop 5.7.

## Item 3. Theorem 1.4 (log form of (6.2)) — SOUND

Proof checked step by step:
* `ν(F∩F′) ≤ Σ_a ν(a) N_a N′_a` and `E[N_aN′_a 1_A] = P(A)Σ P(B|A)` over
  ordered partner pairs — correct (𝓔 is a set, so partners are not repeated).
* The three cases for `P(y_m=c, y′_{m′}=c′)` are exact for the coupling
  `μ̃_m(tρ̃_m)`; summing gives `tΣν_m(c)ρ̃_m + deg(j,a)²`. Correct.
* `A_{−j} = A_𝓢` with 𝓢 = events off j; Cor 1.2 with `|T| ≤ 2` gives
  `e^{10δ}`; the denominator uses `|T| = 1`. Correct.
* `e^{10δ}/(1−2δe^{5δ}) ≤ 1+25δ` on `[0,1/16]`: checked numerically on a
  grid of 1001 points (max of difference is 0, attained at δ = 0; value at
  1/16 is 2.254 vs 2.5625).
* Summing `ρ̃_j·tΣ_{e∋j}π_eρ̃_{e∖j}` over j counts each edge twice; with
  `∫2t dt = 1` and `∫dt = 1` this is exactly (1.2).
* `κ = ρ̃` reproduces TW's conditioned coupling (TW §6.8 "Unary part"), so
  `Z₂(ρ̃)` is TW's Z₂ and Ξ_c = unary factor + `log(Z₂/Z₁²)`.

**Independent numerics** (`reviews/twin2-review-scripts/thm14_check.py`,
reviewer's own code: Z₁ by product-space enumeration, Z₂ by brute-force
enumeration of the doubled space `Π(Ω_ℓ×Ω_ℓ)` — no contraction trick; 2–5
coordinates of size 3–6 incl. an edge-free "safe" residue used to set δ
uniformly in `(0.002, 1/16]`; random, hub and cycle-rich edge sets; random or
all-one ρ̃):
* random: seeds 1,5,6 (≈690 systems in range): worst `lhs/((1+25δ)rhs)` =
  0.88;
* adversarial hill-climb over (ν, ρ̃), 60 steps/system, seeds 2,3,4,7
  (≈950 systems): worst 0.9999, **no violation**. The near-1 maximisers are
  single edges with ρ̃ supported on one end, where exactly
  `lhs/rhs = (ν_c−π)/(ν_c(1−π)²) → 1` as `ν_a → 0`: the `q_j` term is sharp
  with constant 1, confirming the author's "sharp to leading order".

No defect.

## Item 4. Remark 1.6 (literal (6.2) false) — SOUND (one nit)

By TW Lemma 6.10, `E_S E_{ν_S}(r−1)² = Z₂/Z₁² − 1` exactly, and for n disjoint
edges with ρ̃ ≡ 1 the left side is `(1−π)^{−n} − 1`, exponential in n, while
the right side of (6.2) is linear in n. Correct; only the log form is consumed
by Lemma 6.6 (Ξ_c is a logarithm), and TW already used `log(1+x) ≤ x` to pass
to (6.2), so nothing downstream depended on the literal form.

* **D1 (nit).** The example uses endpoint masses 1/16, so `deg = 1/16`,
  which violates TW's own hypothesis `deg ≤ δ ≤ δ₀ = e^{−6}/8`. The
  counterexample survives verbatim with masses ε ≤ δ₀ (`(1−ε²)^{−n} − 1`
  vs `C n ε²(1+2ε)`); say so, so the remark refutes (6.2) *under its stated
  hypotheses*.

## Item 5. Lemma 2.1 (tilting with an arbitrary fibre law) — SOUND

Re-derived from TW Lemma 6.6's proof: with
`π_c = P(c)e^{−Ξ_c}/Z`, `Q_FΣπ_c²e^{Ξ_c} = Z^{−2}Σ_c (Q_FP(c))P(c)e^{−Ξ_c}
≤ ‖dP/dU_F‖_∞/Z`, and Jensen gives `Z ≥ e^{−E_PΞ}`. `P = U|R` recovers Lemma
6.6 exactly. The truncation `ρ_i = 0` for `s_i > λ/2` is correct: in ET Thm
5.5 `V_{λ/2}` is spanned by `H_T` with `c(T) = Σ_{i∈T}s_i ≤ λ/2`, all
`s_i ≥ 0`, so every such T has all `s_i ≤ λ/2`. `σ̃` is supported in
`∪A⁺_c ⊆ A`, so `E_U[g h] ≥ 1` needs only `g ≥ 1` on A. No defect.

## Item 6. Lemma 2.2 (free hub quarantine; author flag: constants) — SOUND

Checked every constant:
* `ν(H) ≤ w_ℓ ≤ 1/32` (Markov at 1); `U(H) = (1−p)ν(H) ≤ ν(H) ≤ S_ℓ`
  (hubs have `min(deg,1)² = 1`). `p⁺ ≤ 1/8 + 1/32 < 1/4`.
* Point-mass ratio `(1−p)/(1−p⁺) ≤ 4/3` (actually `≤ 28/27`); hence
  `deg⁺ ≤ (4/3)deg`, `π⁺ ≤ (16/9)π`, `w⁺ ≤ (16/9)(δ/2) ≤ δ ≤ 1/16`, and
  `q⁺_j ≤ (4/3)³Σ_{a∉H}ν(a)deg(a)² ≤ (4/3)³S_j` (non-hubs have `deg < 1`).
* `A⁺ ⊆ A`: a point of A⁺ avoids every hub, hence every deleted edge.
* Unary factor (TW §6.8, exact) `≤ Σρp⁺/(1−p⁺) ≤ (4/3)Σρ(p+S)`.
* `ρ̃⁺ = ρ/(1−p⁺+ρp⁺) ≤ (4/3)ρ`; Theorem 1.4 with constant
  `1+25/16 = 2.5625`: diagonal `2.5625·(4/3)²(16/9) = 8.10 ≤ 9`, q-part
  `2.5625·(4/3)(4/3)³ = 8.10 ≤ 9`. Total S-coefficient `2 + 9 = 11`, as used
  in Theorem 5.1.
No defect.

## Item 7. Lemmas 3.1, 3.2 (medium local lemma, inflation, density) — SOUND

* 3.1: every `F ∈ Γ(E_C)` contains a prime of `k₂(M_C)`, so
  `Π_{Γ(E_C)}(1−x_F) ≥ Π_{p|k₂}(1−μ_p) ≥ 2^{−ω(k₂)}` (needs μ_p ≤ 1/2), which
  is exactly the LLL hypothesis with `x_C = 2^{ω(k₂)}/k₂ ≤ 1/2`.
  `1−x ≥ e^{−2x}` on `[0,1/2]`; `(1−μ)^{−1} ≤ 1+2μ` on `[0,1/2]`. Correct.
* Stage logic: small classes with `k₂ = 1` are killed by TW Lemma 1.3(1);
  with `k₂ > 1` either inactive (c_s misses the class) or avoided by
  `Av(c_s)`. `Av(c_s) ≠ ∅` on `G_s` by 3.1(1).
* 3.2(1): `P′(c≡b (k)) ≤ P_QR(c_s≡b₁ (k₁))/P_QR(G_s)·sup_{G_s}P(c_m≡b₂ (k₂)|Av)`;
  TW Lemma 1.3(3) gives `Πγ(p)/k₁` incl. prime powers; on `G_s` the medium
  factor is `Π(1+2p^{−1/4})/k₂`. Dependency order `G_s → P′ → G_L → P` has
  no circularity (3.4 uses only the P′ bound). Correct.
* 3.2(2): `Q_F P(c) ≤ (Q_s/|R|)·2·e^{2T}·2`; `log(Q_s/|R|) = π(W₁)log2 +
  O(loglog) = o(L^{1/2})`, `2T ≤ 2L^{1/2}`. Correct.

## Item 8. Lemma 3.3 (Shiu along the top prime) and (3.1) — SOUND (nit D2)

* 3.3: `A = (qm+1)/4` runs over one class `a mod q` with `4a ≡ 1`, so
  `(a,q) = 1`; interval length `Y = qy/4`, `x ≤ 2Y+1`, so `Y ≤ x`.
  `q^β ≤ (2y)^{(B+2)/(2B+6)} < (2y)^{1/2}` gives `q < Y^{1−β}` for large y;
  `F = τ(·²)` is in Shiu's class; `exp(Σ3/p)/log x ≍ (log x)²`. Correct.
* (3.1): the inequality `(log 2k)^i ≤ i!(log w₂)^i(2k)^{1/log w₂}` is right
  and the Euler products are polylog. **D2 (nit).** "`p^{1/log w₂} ≤ e`, so
  … `+ O(p^{−2})`" is not literally true: with that crude bound the
  prime-power tail at p is `Σ_{e≥2} e^e/φ(p^e)`, which is a constant (≈ 40)
  at p = 3, not `O(3^{−2})`, and diverges at p = 2. It is harmless because
  all moduli are odd (k odd; also `Γ(2)` would be 4, not ≤ 3) and only
  finitely many p are affected; state "k odd" and "`≪ 1` for p ≤ 5".

## Item 9. Lemma 3.4 (good events likely; author flag: case splits) — SOUND

All case splits re-derived:
* small classes: `M ≤ P(M)^{1+B} ≤ w₂^{1+B}`, `τ(A²) ≤ C_εL^{8(1+B)ε} =
  C_εL^{1/32}` ✓. `E T ≪ L^{1/32+o(1)}` (classes with `k₁ = 1` are always
  active, weight `Π_{(W₁,w₂]}(1+2/(p−1)) ≍ 16²`, bounded) ✓.
* μ_p: pair activity is one congruence mod lcm (or impossible), so
  `≤ Γ(lcm)/lcm`; `E μ_p² ≪ L^{1/16+o(1)}p^{−2}`; Markov at `p^{−1/4}` and
  `Σ_{p>W₁}p^{−3/2} ≪ W₁^{−1/2}` give `L^{−3/16+o(1)}` ✓.
* p_j: `kj^v ≤ j^{1+B}`, `τ ≤ C_εj^{1/256}`, `E′p_j² ≪ j^{−2+1/128}` ✓.
* w^U_j: the three cases (j top, any u, v; m top u ≥ 2; m top u = 1) exhaust
  binary classes since there are ≤ 2 large primes. j-top: spare `j^{−2}`
  against `j^{1/128}(loglog j)²` ✓. m-top `u ≥ 2`: `Σ_{m>j}m^{−2+1/256}` ✓.
  m-top `u = 1`: `q = kj^v ≤ m^B ≤ (2y)^B` is within Lemma 3.3's range;
  ≤ L dyadic blocks each `≪ (q/φ(q))L²`, so `≪ (q/φ(q))L³/j^v`; the extra
  `k/φ(k) ≪ log w₂` weights not covered by (3.1) as stated are polylog ✓.
  `Σ_j 64²E′w² ≪ L^{6+o(1)}/w₂ = L^{−2+o(1)}` ✓.
* `w_j ≤ (8/7)²w^U_j ≤ 1/49 ≤ 1/32` (π in ν, `p ≤ 1/8`) ✓.
No defect beyond D2 (inherited from (3.1)).

## Item 10. Lemma 4.1 (unary/diagonal binary profiles) — SOUND

Unary `M = kj`: Lemma 3.3 on blocks `y = y₀2^t`, `y^{−α} ≤ 2^{−αt}`, gives
`(k/φ(k))(a²/α + a/α² + α^{−3})` with `a ≪ log 2k + log L`; summed against
`Γ(k)/k` via (3.1) ✓ (sanity: `∫(log t)²t^{−1−α}dt = 2α^{−3}`, so this is the
true order). `v ≥ 2` and binary `u ≥ 2`: pointwise τ with spare power ✓.
Binary m-top `u = 1`: `Σ_ℓ ℓ^{−1−2α}(log ℓ)^i ≪ (i−1)!(2α)^{−i}`, `i = 0`
gives `≪ log L`; the three terms give `α^{−3}, α^{−3}, α^{−3}log L` ✓.
Labelling "m = top prime" is WLOG ✓; for B = 0 there are no binary classes ✓.
Per-class weight `4(8/7)²Γ(k)/M` from Lemma 3.2(1) and `ν ≤ (8/7)U` ✓.

## Item 11. Theorem 5.1 (assembly) — SOUND-AFTER-REPAIRS (presentation only)

The assembly is correct: Lemma 2.1 with P of §3; `αλ/2 ≤ A₀L^{3/4}/2`;
`log‖dP/dU‖ ≤ 4L^{1/2}`; supp P ⊆ G_L so Lemma 2.2 applies fibrewise with
`A⁺_c ≠ ∅` (`Z₁⁺ > 0` by Lemma 1.1, unary densities `≤ 1/4`); `p`- and
`π`-parts by Lemma 4.1; S-coefficient `2 + 9 = 11`. `ρ_j = j^{−α}` for all j
is admissible (`ρ_i ≥ e^{−αs_i}`). Small classes: avoided on supp P; one-
and two-large-prime classes: unary/binary. Nothing is missing.
* **D3 (minor, scope).** The B-hypothesis `M ≤ P(M)^{1+B}` is a genuine
  restriction of the family relative to TW Reduction 6.7 / Conj 6.8, which
  promised the two-prime cap "with no windows and no B" (for fixed B, twins `kℓ₁ℓ₂`, `ℓ₁ ≈ ℓ₂`, are
  excluded once the w₂-smooth cofactor has `k > M^{(B−1)/(B+1)}`). The §0 *Bottom line* says the cap
  "is reduced … to a single arithmetic inequality (H_O)" without saying
  that B is added; and §4's closing paragraph says B "is what makes (ii)
  available", understating its use: Lemma 3.4 also needs it (small moduli
  `≤ w₂^{1+B}` for `τ ≤ L^{1/32}` in `G_s`; pointwise τ for unary and
  binary moments). Fix: add "for moduli with `M ≤ P(M)^{1+B}`" to the
  Bottom line, and list B's three uses.
* **D4 (nit).** Setting 3.0: "Every class with `N(M) ≤ τ(A²)` classes per
  modulus; we use only this count" is ungrammatical (meaning: each modulus
  carries `N(M) ≤ τ(A²)` classes, and only this count is used).

## Item 12. §5.1–5.2: Lemma 5.3, canonical labels, (H_O^=), (H_O^≠), numerics

* **Lemma 5.3 — SOUND.** `D/A = u′/v′` in lowest terms gives `v′ | A`,
  `u′ | A`; conversely; this is a bijection (per `p^e ∥ A`: `2e+1` choices
  either way, matching `τ(A²)`). `4A ≡ 1 (j)` and `(v′, j) = 1` give the
  residue `−u′/v′`. Correct.
* Canonical labels: correctly labelled heuristic. Spot checks: `D = A`,
  `D = 1`, `D = A²` give the universal labels 1, 4, 1/4 (residues −1, −4,
  −1/4) present for every modulus; the example `A = n(n+1)`, `D = n²`
  (label `n/(n+1)`, modulus `n(n+1) ≪ height²`) is right. The decomposition
  `j·q_j ≤ (8/7)[Σδ_λ² + Σ_{λ≠λ′≡λ′}δδ′]` (for `e_j = 1`) and `S ≤ q` are
  correct.
* **(H_O^=) — SKETCH, honestly labelled.** The admitted gap
  (cross-cofactor pairs `d | kj^vm − k′j^{v′}m′`) is real; the heuristic
  count (labels of modulus `d ≤ polylog` are the hubs, ≈ polylog many;
  non-hub `Σ_dδ²` converges) agrees with `α^{−1}(log L)^{O(1)}`.
* **(H_O^≠) — OPEN, honestly labelled.** Random and trivial benchmarks
  (`L^{6+o(1)}/w₂`, `L⁶/α`) re-derived ✓.
* **Numerics — reproduced.** `scripts/twin2_offdiag.py 1e7 30 45 1 1009
  10007 100003` reproduces the three X = 1e7 rows exactly (jw, jq, jS,
  same, cross, rand); `same + cross = jq` ✓; cross < rand in all 6 rows ✓.
  `twin2_binary_check.py 100 1` runs (max in-hypothesis ratio 0.93).
  Caveats in the text are adequate. Note (not a defect): at toy scale
  `jS` grows roughly like `(jw)^{0.7}`; (H_O) needs `F(log(X/j))`
  to be `≪ L^{3/4}` while the trivial bound is `≍ L³`, so the numerics can
  neither support nor refute it — as the author says.

## Summary

| item | verdict | defects |
|---|---|---|
| 1 Lemma 1.1, Cor 1.2 | SOUND | — |
| 2 Lemma 1.3 | SOUND | — |
| 3 Theorem 1.4 (+ independent exact/adversarial check, no violation) | SOUND | — |
| 4 Remark 1.6 | SOUND | D1 nit |
| 5 Lemma 2.1 | SOUND | — |
| 6 Lemma 2.2 (constants) | SOUND | — |
| 7 Lemmas 3.1, 3.2 | SOUND | — |
| 8 Lemma 3.3, (3.1) | SOUND | D2 nit |
| 9 Lemma 3.4 (case splits) | SOUND | — |
| 10 Lemma 4.1 | SOUND | — |
| 11 Theorem 5.1 | SOUND-AFTER-REPAIRS (wording/scope) | D3 minor, D4 nit |
| 12 Lemma 5.3; (H_O^=) SKETCH; (H_O^≠) OPEN; numerics | SOUND / labels honest | — |

No major defect. Every PROVED label survives; the mathematical content of
Theorem 5.1 stands as stated in its own Setting 3.0. Required before merge:
D3 (state the added B-hypothesis in the Bottom line / §0 and list its uses).
D1, D2, D4 are optional polish.

---

# Round 2 — commit bd0129c (§§5.3–5.4, §0, Cor 5.2)

Diff 3ea1bcb..bd0129c: §0 rows for Lemma 5.4 / (H_O^≠) / Cor 5.2, Bottom
line, new §5.3 (Lemma 5.4) and §5.4. §§1–5.2 are unchanged.

## R2.1 Lemma 5.4 ((H_O^=)) — SOUND-AFTER-REPAIRS

Checked and correct:
* **Data.** Type 0 / type 2 data with `g(D) = d` (resp. `g(D̄) = d`) number
  `2^{ω(d)}` each (`⌈e/2⌉ = f` has two solutions per `p^f ∥ d`); type 1:
  `2^{ω(d)}` coprime splittings. The map from data to labels is injective
  within each type, so `Σ_λδ_λ² ≤ 3Σ_θδ_θ²` holds.
* **The activity residue depends only on (θ, k).** This is the key point and
  the text doesn't say it. Since `4A ≡ 1 (mod k)`, the class `−4D` is
  `≡ −4D` (type 0), `−u′/v′` (type 1) or `−1/(4D̄)` (type 2) mod k,
  independently of m (and j). That is why
  `δ_θ ≤ C Σ_k 1[c ≡ r_θ(k) (k)]·b_θ(k)` and why (ii) works. **D8 (nit):**
  state this.
* (i): `d | A ⇔ 4d | kjm+1`; one reduced class mod 4d; consecutive elements
  are `4d` apart; BT `π(2y;4d,s) ≪ y/(φ(d)log(y/4d))` on blocks `y ≥ 8d`,
  O(1) elements below, and `Σ_t 1/t ≪ log L`. Correct.
* (ii): `Γ(lcm) ≤ Γ(k)Γ(k′)`, `lcm = kk′/gcd`; the Euler factor of h at
  `p^f ∥ k` is `≤ (1+Γ(p)f)(1+Γ(p)/(p−1))`. AM–GM on the symmetric kernel
  is valid, and incompatible congruence pairs only help. This does close the
  §5.1 cross-cofactor gap.
* (iii): `Σ_d 2^{ω(d)}/φ(d)² < ∞`; `Σ_kΓ(k)τ_Γ(k)/k` has Euler factor
  `1 + Γ(1+Γ)/p + O(p^{−2})`, so it is polylog. Correct.
* (iv): the number of data occurring for M is `≤ 3τ(A²)`
  (`3^{ω(A)} = τ(A²)` for type 1). m-top: `Σ_{m>j}τ/m² ≪ (q/φ(q))L²/j`.
  j-top: A is linear in j, `q = km ≤ j^B`, so Lemma 3.3 applies with j
  innermost. Both are `o(1)`. Correct.

Defects:
* **D5 (minor, prime powers).** The proof's prime-power sentence ("carry an
  extra factor `≤ j^{−1}` … absorbed by the pointwise bound") contradicts
  the reduction that Lemma 5.4 bounds. In §5.1, for `e_j ≥ 2` one uses
  `deg(j,a) ≤ Σ_{λ ≡ −a (j)} δ_λ`. That counts a class mod `j^v m` (v ≥ 2)
  with its *full* partner mass at all j-residues `≡ b (mod j)`, so the
  factor `j^{1−v}` is discarded. At full weight the pointwise route fails:
  for j the top prime, `Σ_j ρ_j j^{−1}·j^{1/256}` diverges (`1/256 > α`).
  Shiu along j is not available either, since A is quadratic in j.
  **Repair (mechanical, at the S_j level, which is all (H_O) needs):**
  `min(x+y,1)² ≤ min(x,1)² + 3y` for x, y ≥ 0. So
  `S_j ≤ S_j^{(u=v=1)} + 3w_j^{pp}`, where `w_j^{pp}` is the true
  binary mass of the prime-power classes at j. Then
  `E_PΣ_jρ_jw_j^{pp} ≪ L³/w₂ + w₂^{−1/2}(log L)^{O(1)}`, by the
  `v ≥ 2` / `u ≥ 2` cases of Lemma 4.1, re-run with weight `ρ_j` only
  (checked case by case):
  * pointwise τ works for the top-prime power (`v ≥ 2` with j top;
    `u ≥ 2` with m top);
  * the case "j top, `v = 1`, partner `m^u`, `u ≥ 2`" needs Shiu along j
    (`q = km^u ≤ j^B`, A linear in j). Pointwise τ fails there, since
    `Σ_j j^{−1+1/256}` diverges.
  * the case "m top, `u = 1`, `v ≥ 2`" needs Shiu along m.

  Lemma 5.4 should be stated for the `u = v = 1` classes, with
  this split added.
* **D6 (nit).** `m₀(θ,k)` must be the least m for which `kjm` is a *family*
  modulus, not just any prime in the class with `kjm ≤ X`. Otherwise (iv)'s
  "summed over binary moduli of the family" and the B-hypothesis used in the
  Lemma 3.3 step (`q = kj ≤ m^B`) are unjustified. With the family
  definition, (i)'s spacing argument is unchanged.

## R2.2 §5.4 ((H_O^≠) reduction) — DEFECTIVE as written (minor); OPEN label correct

* **D7 (minor).** "Agreement is `j | gcd(n+4D, n+4D′)`, hence
  `j | D − D′ ≠ 0` (equivalently `j | ab′ − a′b`)" is false. The canonical
  datum is chosen by least height, which depends on A, so the *same* D can
  carry different canonical labels for different moduli. Example:
  `A = n(n+1)s`, `D = n²`. The candidate heights are
  `4n², (n+1)s, 4(n+1)²s²`. So the label is `n/((n+1)s)` when
  `(n+1)s < 4n²`, and `4n²` otherwise (n = 2: `s = 1` gives label 2/3,
  `s = 7` gives 16). Two such classes through j have the same residue
  `−4n²` for every j, yet they sit in the cross-label part with `D = D′`.
  The same happens whenever two classes share any of their three candidate
  rationals across types. These agreements are deterministic, so for this
  sub-part:
  * the "random" benchmark of §5.1/§5.2 is the wrong heuristic;
  * the claimed equivalence "`D ≠ D′` ⇔ label difference ≠ 0" fails;
  * the incidence count in §5.4 has this deterministic piece mixed in.

  It is not fatal: these pairs can be grouped by the shared rational, e.g.
  by datum `(0,D)` with the condition `g(D) | A` irrespective of height,
  and then Lemma 5.4's argument bounds them. Repair: define the split by
  connected components of "shares a candidate rational" (or by D), move
  the deterministic pairs into the same-label part, and restate (H_O^≠)
  for genuinely distinct residue rationals.
* The rest of §5.4 is honest. With j-independent masses the margin is L.
  The j-dependence of the data (via `d_θ | A_{kjm}`) is correctly
  identified as the obstruction. The Lenstra/CHN remark is fair.

## R2.3 §0 / Cor 5.2 status — SOUND-AFTER-REPAIRS

`H_O = (H_O^=) + (H_O^≠)` via `S ≤ q`. With Lemma 5.4 repaired (D5),
"Cor 5.2 CONDITIONAL on (H_O^≠) alone" is correct, and it remains correct
after D7: moving deterministic pairs into the proved part only weakens
what (H_O^≠) must assert. The Lemma 5.4 row says "prime powers via
pointwise bound", which should cite the D5 split instead. **D3 (round 1)
is still open:** the Bottom line still omits the hypothesis
`M ≤ P(M)^{1+B}`.

## Round 2 summary

| item | verdict | defects |
|---|---|---|
| Lemma 5.4 (H_O^=) | SOUND-AFTER-REPAIRS | D5 minor, D6 nit, D8 nit |
| §5.4 (H_O^≠) reduction | DEFECTIVE as written (minor), OPEN label correct | D7 minor |
| §0 / Cor 5.2 conditional on (H_O^≠) | SOUND-AFTER-REPAIRS | D3 (still open), row wording |

No major defect. The same-label proof is a real proof once D5 is repaired.
D5, D7 and D3 should be fixed before merge.

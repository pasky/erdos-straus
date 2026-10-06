# Hostile review R60 of CEILINGS_UNIFIED.md (branch side-agent/unify-ceilings)

Reviewer branch: side-agent/review-unify. Status: IN PROGRESS.

## Verdict summary (filled in per claim)

## Defects

### Claim 1 — Prop 1.1 (`log(1/δ*(T)) ≫ 𝓛³`): **SOUND** (given the note)

Re-derived line by line against `paper/es-threequarter-note.tex`:
* Atoms are POINTWISE_HAAR events. For `A=(k,ℓ,u,v)`, `M=kℓ≡3 (4)`, `A_M=uvw`;
  since `4A_M≡1 (M)`, `v^{-1}≡4uw`, so `−uv^{-1}≡−4u²w (M)` with `D=u²w | A_M²`.
  Hence every atom is an event `E_{M,D}` with `M=kℓ≤KX≤X^{1+κ}=T`. ✔ (checked
  numerically from scratch: `scripts/review_unify_atoms.py`).
* Unit Haar: `ℓ>X^{1/2}>K`, so `ℓ∤L_K`; `n mod ℓ` (uniform on `(ℤ/ℓ)^×`) is
  independent of `c=n mod L_K` and across `ℓ`. Atom residue `−uv^{-1}` is a unit
  mod `ℓ` (`uv<z_j²<ℓ`). Activation depends only on `c` (`k|L_K`). Note Lemma 2.2
  gives distinct projections at fixed `ℓ`. So the exact product
  `∏(1−f_c(ℓ)/(ℓ−1)) ≤ e^{−μ_c}` holds. ✔
* Note Cor 4.3 is stated "uniformly in all `c`" (not only reduced), with
  `μ_c ≥ a_h t² h(J_c)`; for unit `c`, `J_c=K(K)` and Lemma 3.2 gives
  `h ≍ log K ≍ κt`. ✔ Constants depend only on `κ` (fixed, e.g. 1/480) and `D`.
* Normalisation `n≡1 (24)`: `9∈K(K)` so `3|L_K`; `L_K` odd so `n mod 8` independent;
  conditioning keeps `c` a unit. Factor `φ(24)=8` trivial. ✔

Minor point only: D1 below (label of the two-sided sandwich).

### Claim 2 — Thm 2.1 (`#{p≤x: W(p)>T} ≪ π(x)e^{−c𝓛³}`, `𝓛 ≤ c₁(log x)^{1/4}`): **SOUND** (given the note + Page)

Re-derived:
* `W(p)>T`, `p>y` ⇒ `S_y(p)=1`, `H_X(p)=0` (active atom ⇒ witness `kℓ≤KX≤X^{1+κ}=T`
  with `w=(kℓ+1)/(4uv)`), so `ν(p)=Q_r(0)=1`. ✔
* Case A: `t ≤ 𝓛 ≤ c₁(log x)^{1/4}` gives `log x ≥ C_0t⁴` once `c₁⁴≤1/C_0`; note
  Thm 8.2 (eq. integermean) then gives `≪ x e^{−c_at³} ≤ x e^{−c_at³/2}/log x`. ✔
* Case B, prime sum: split `p≤√x` (`≤T_abs√x`) and `p>√x` (`1 ≤ 2log p/log x`,
  `ν≥0`). Non-reduced terms `≤ T_abs(log x)²`. ✔
* Siegel factor: with `(a,q)=1`, `∫_{n≡a(q)} χ̃₁ dP_* = χ₁(a)/φ(q)·1[q₁|q]`. If
  `q₁∤q`, the fibre projects onto a coset of `ker((ℤ/q₁)^×→(ℤ/g)^×)`, `g=(q,q₁)`,
  and `χ₁` is non-trivial on that kernel by primitivity. ✔ (from-scratch
  exhaustive check of this identity for all real primitive characters with
  conductor `≤ 200` and `q ≤ 120`: `scripts/review_unify_page.py`.) So the main
  terms are `xE_*[ν(1−εχ̃₁)] ≤ (1+ε)xE_*ν`, `ε ≤ 1/β₁ ≤ 2`. This uses only
  `ν ≥ 0` pointwise on ℤ (Lemma 8.1 and `S_y ∈ {0,1}`), and `ν` is periodic. ✔
* Error: `T_abs·x·e^{−c₃√log x}`. In Case B, `log T_abs ≤ C_L t⁴ =
  O((log log x)^{4/3}) = o(√log x)`, so this is fine for any fixed `c₃`. The text's
  "`≤ exp(c₂√log x)` … `O(xe^{−c₃√log x/2})`" silently needs `c₂ ≤ c₃/2`. That is
  true here only because `T_abs` is far smaller (D3).
* Unit mean: `S_y≡1` on `Ẑ^×`; conditional factorial moment
  `m!e_m(p) ≤ (Σp_ℓ)^m ≤ (2μ_c)^m`; the note's Cor 4.3 upper bound is uniform in all
  `c`. With `r+1 ≥ D_Bt³ ≥ 2e²C_ut³` we get `(2eC_ut³/(r+1))^{r+1} ≤ e^{−(r+1)}`. ✔
  Enlarging `D_B` is legitimate: note Thm 8.2 only asks `D_B` large, and `C_0`, hence
  `c₁`, are chosen after `D_B`.
* Uniformity: all constants depend on the fixed `κ,D,B,D_B`. The case split is at
  `c_at³ = 2log log x`, and the thresholds `x_0, T_0` are absolute. ✔

Source caveat: Davenport Ch. 20 / MV Cor 11.17 are not in `sources/`; I could
not check them against a PDF either. The form used (one exceptional primitive
`χ₁ mod q₁ ≤ exp(c₂√log x)`, term present iff `q₁|q`, error `x e^{−c₃√log x}`) is
the standard one as I recall it. Only the weak range
`q ≤ exp(O((log log x)^{4/3}))` is used, so even a Siegel–Walfisz-plus-Page
version suffices.

### Claim 4 — Thm 4.1 (two-sided order-k limit): **SOUND** (statement and proof), with minor wording issues

Re-derived:
* (U−) Fix `x_s`. The unary patterns `X_b∈Ω_b(x_s)` have a constant activation
  rule (`F_b=Ω_b`), all light (`p_b≤1/4=δ`), so `M≡P` is deterministic and every
  path ends in the avoider set: `G(y) ≥ F(y)=1`. `G ≥ F ≥ 0`, so KARY Thm 2.5's
  hypothesis `f≥0` holds. `G(x_s,·)` is k-local. Thm 2.5 plus Jensen give
  `E_sG ≥ e^{−EΦ}`, and Cor 2.6 (`d=k`, `m̄=P`, `t=k/(P+4k) ≤ 1/4`) gives exactly the
  displayed bound. The consequence `k ≥ c₀P` holds with `c₀=min(c₀',1/P₀)` to cover
  `P<P₀`. ✔
* (U+)/(L+) `Σ_{j≤k}(−1)^jC(h,j) = (−1)^kC(h−1,k)` for `h ≥ 1`; `C(h−1,k) ≤ C(h,k+1)`
  (zero for `h≤k`, and the ratio is `h/(k+1)≥1` otherwise);
  `E_sC(H,k+1)=e_{k+1}(p) ≤ (eP/(k+1))^{k+1} ≤ e^{−(k+1)}` for `k+1 ≥ e²P`;
  `1−p ≥ e^{−4p/3}` for `p ≤ 1/4`. (L+) positivity needs `k+1 > 4P/3`, which holds. ✔
* (L−) Fibrewise planting: OMEGA14 Lemma 1.1 at fixed `x_s` gives `ν_{x_s}` with the true
  k-marginals and `ν(F=0)=1`, so `E_sB = E_νB ≤ E_νF = 0`. With `r* ≤ 1/3`,
  `(k+1)+(2k+1)/3 = (5k+4)/3 ≤ (5/3)(k+1)`. ✔
* Brute force from scratch (`scripts/review_unify_thm41.py`): exact multilinear LPs
  over `{0,1}^n` with heterogeneous `p_b ≤ 1/4`, `n ≤ 10`, `k ≤ 4`, random instances,
  checking (L−), (U−), (U+), (L+) and Lemma 1.1's planting condition. The reduction
  to bits is legitimate: averaging `B` over `X_b` given its bit preserves
  `B≤F` and k-junta structure. Results below.
  Output (120 random instances, `n ≤ 13`, `p_i ∈ [0.12,0.25]`, `k ≤ 3`):
  - (L−): 105 cases meet `P ≥ (5/3)(k+1)` or planting (1.1); in all of them the
    LP max of `E B` is `≤ 0`.
  - (U−): 360 cases; the bound is never violated (min slack 13.2, so very loose
    at small `P`).
  - (U+)/(L+): exact means on 200 random systems with `n ≤ 40` meet the stated
    bounds.
  - The Bonferroni identity and sandwich hold for `h<30`, `k<12`.

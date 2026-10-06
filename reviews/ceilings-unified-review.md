# Hostile review R60 of CEILINGS_UNIFIED.md (branch side-agent/unify-ceilings)

Reviewer branch: side-agent/review-unify. Status: ROUND 1 COMPLETE. Overall: no FATAL, no MAJOR; 10 MINOR (labels/wording). See verdict table at the end.

## Per-claim checks

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
the standard one as I recall it. Only the range
`q ≤ exp(O((log log x)^{4/3}))` is used. This still exceeds every
`(log x)^A`, so Siegel–Walfisz alone does **not** suffice; a Page/Landau-type
statement (or Gallagher) is genuinely needed, as the author says.

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

### Claim 5 — Prop 4.2 (no positive minorant below `log D ≤ c𝓛⁴` on every fibre with `log Q ≤ T^{0.05}`): **SOUND** (given the note), minor repairs

Re-derived:
* Atoms are ES events of modulus `kℓ ≤ T` (Claim 1), so `F_T ≤ F_𝓕`. Each atom is
  `{n mod k = −uv^{-1}} ∩ {n mod ℓ = −uv^{-1}}`. The first factor is a function of
  the small coordinate `c` (`k|L_K`, primes `≤ K < X^{1/2}`). This is Setting 1.2
  with one big coordinate per event. ✔
* `p_ℓ = f_c(ℓ)/(ℓ−1) ≤ ℓ^{1/3}/(ℓ−1) ≤ 2ℓ^{−2/3} ≤ 2X^{−1/3}` (`f_c(ℓ) ≤ z_j² ≤ ℓ^{1/3}`,
  note Lemma 2.2 proof). ✔
* Uniformity in `c`: note Cor 4.3 is stated for *every* residue `c mod L_K`.
  `J_c = K(K)` for unit `c`, and `a_h` depends only on `κ,D`. So `R(x_s) ≥ μ_c −
  #{big ℓ|Q}·p* ≥ a t³ − (2log Q/t)·2X^{−1/3}` for *every* small configuration. With
  `log Q ≤ T^{0.05}` and `X^{−1/3} ≈ T^{−0.33}` the loss is negligible. ✔
* Level → order: big primes exceed `e^{t/2}`, so `q ≤ D` has `< 2log D/t` of them;
  `k ≤ 2c(1+κ)⁴t³`, and `(k+1)(1+3r*) ≤ (5/3)(k+1) ≤ at³/2` for `c` small. OMEGA14
  Lemma 4.1 applies with an empty exceptional set. ✔
* The OMEGA14 Thm 4.5 / Cor 4.6 comparison is correct: `𝓛³/log𝓛 → 𝓛³` in the mass, so
  the minorant-architecture gap to OMEGA13 Thm 5.1 is `(log log p)^{1/4}` in `log W`.
  The "every fibre" scope is inherited from Cor 4.6's own remark (R49b D4). ✔

Defects: D4 (coordinate definition) and D5 (inputs list).

### Claim 7 — §4.4 toy LP (EVIDENCE): **SOUND** (reproduced exactly)

My own exact rational simplex on the dual moment LP
(`scripts/review_unify_toylp_exact.py`, no code shared with `unify_toy_lp.py`)
reproduces the table exactly:
* least order with a positive minorant: 3, 7, 11, 15 (`=2P−1`);
* least order with a ≥90% majorant saving: 6, 8, 12, 14;
* the per-`k` savings and `EB/EF` values agree to all printed digits.

A float HiGHS version (`scripts/review_unify_toylp.py`) agrees for `P=2,4` but is
numerically unreliable for `P ≥ 6`. That is a warning against float replays of
this LP; it does not affect the author's exact script. The label EVIDENCE is
correct.

### Claim 3 — §3 goal (a): Prop 3.1, Assessment 3.2, Cor 3.3: **SOUND**, minor scope wording

* Prop 3.1: `W(p) ≤ T` gives a representation (note Lemma 2.1 holds for any
  positive `k,ℓ`). So `E_pr(N) ≤ #{p ≤ N: W(p)>T}`, and Thm 2.1 at
  `T=exp(c₁(log N)^{1/4})` gives `π(N)e^{−cc₁³(log N)^{3/4}}`. ✔ The "reproof, not
  improvement" label is honest.
* Cor 3.3: KARY2/3's level is `Σ_{ℓ|d_i,ℓ>W} log ℓ ≤ log d_i`, so "all moduli
  `≤ e^λ`" implies level `≤ λ`. KARY3 Thm 4.1 holds for any finite mixture, so
  `s ≤ Cλ^{3/4}`. ✔ The note's `ν_X` is `≥ 1` on all of `𝒜(𝔊_T)`: avoiding the
  selectors gives `S_y=1`, and avoiding all `ℛ(M)`, `M ≤ T` (the atoms included)
  gives `H_X=0`. Its level is `≤ C_ϑBt³ + r(1+κ)t ≍ t⁴`. ✔ The parenthetical
  disclaimer about `δ*(T)` is correct and needed.
* D10 (minor): "cannot beat the note" (Assessment 3.2 / O60 report item 3) holds
  only within the K2 Cor 6.1 class (coefficient-sum CRT majorants of the whole
  avoider set). Say so.

### Claim 6 — Thm 4.3 + §4.2 + §0/§5 unification: **SOUND-AFTER-REPAIRS** (labels and wording only)

The theorem is honestly a conjunction: items 1–2 restate KARY3 Thm 4.1, the
note, Prop 4.2 and OMEGA13 §5. Item 2 is correctly quantified: the
obstruction holds on every fibre with `log Q ≤ T^{0.05}`, and OMEGA13's
`Q' = Q·ℓ_aux` satisfies this, so both bounds hold *on the same fibre*. ✔ The
`a/(a+1)`, `1/(a+1)` extrapolation is labelled CONDITIONAL and the mechanism is
labelled Assessment. ✔ "Product = level is an identity" is honest. The repairs
are D6–D9.

## Defects (all MINOR; no FATAL, no MAJOR found)

**D1 (MINOR; Prop 1.1 last sentence, §4.3 definition of `κ(𝓛)`, §5 first
by-product).** The sandwich `𝓛³ ≪ log(1/δ*) ≪ 𝓛³(log𝓛)^5` is stated without a
label. Its upper half is OMEGA13 Thm 3.4, which is PROVED *modulo
Nair–Tenenbaum*. *Repair:* add "(upper bound modulo NT)" at each occurrence.

**D2 (MINOR; Thm 2.1 header).** Page's theorem is quoted from memory. I could
not check it either (Davenport and MV are not in `sources/`). *Repair:* keep the
caveat. Add that Siegel–Walfisz alone would not suffice, since
`exp(C(log log x)^{4/3})` exceeds every power of `log x`. Ideally pin the exact
equation number once a copy is available.

**D3 (MINOR; Thm 2.1 Case B, "q, T_abs ≤ e^{Ct⁴} ≤ exp(c₂√log x)").** The
error `T_abs·x·e^{−c₃√log x}` becomes `O(xe^{−c₃√log x/2})` only if
`T_abs ≤ e^{c₃√log x/2}`, i.e. it needs `c₂ ≤ c₃/2`, which is not stated. It is
true because `log T_abs ≤ C_Lt⁴ = O((log log x)^{4/3}) = o(√log x)`. *Repair:* say
exactly that, instead of routing through `c₂`.

**D4 (MINOR; Prop 4.2 proof, "Big coordinates: `X_ℓ = n mod ℓ`").** A level-`D`
function of `n mod qQ` may read `n mod ℓ²` for a big `ℓ`. Then `X_ℓ` must be the
ℓ-adic unit component (as in POINTWISE_HAAR §0, `n mod ℓ^f`), not `n mod ℓ`.
Nothing else changes: the events still read `X_ℓ` only mod `ℓ`, `p_ℓ` is unchanged,
and a modulus still has `< 2log D/t` *distinct* big primes. *Repair:* one phrase.

**D5 (MINOR; Prop 4.2 label "inputs BV and Brun–Titchmarsh"; ledger proposal
(H)27 "inputs reduced to the note's BV"; Remark 1.2).**
* Note Cor 4.3 rests on Thm 4.2, which uses Lemma 3.3 (low-ω mass, via Shiu)
  in addition to BV and BT.
* The note's constants are explicitly *not* asserted effective (note §1).
  Prop 1.1, Thm 2.1 and Prop 4.2 therefore have ineffective `c, T_0`. That
  matters for Prop 4.2: OMEGA14 Thm 4.5 used an *effective* Page bound and FL.
  So the sharpening trades a `log𝓛` for effectivity of `T_0`.

*Repair:* list "BV, BT, Shiu (via the note); constants not effective" in the
label and in the ledger proposal. Say "replaces" rather than "removes" the
(G)/Page/FL inputs.

**D6 (MINOR; §5 bullet "For such a system, order-k certificates are trivial below
`k ≍ κ` on *both* sides: majorants save `≲ k log(κ/k)`").** On the minorant side,
the obstruction for the one-big-prime subfamily transfers to the full ES
avoider (`B ≤ F_T ≤ F_𝓕`). On the majorant side it does *not*: `F_T ≤ F_𝓕`, so a
majorant of `F_T` need not majorise `F_𝓕`, and (U−) for the subfamily says
nothing about majorants of the full avoider. The full-system cap is KARY3 Thm 4.1
(sequential coupling over all events and scales), as §4.3 "Status" correctly
says. *Repair:* in §5 write "majorants of the full avoider save
`≲ λ^{3/4}` (KARY3; (U−) is its one-scale, one-big-prime core)".

**D7 (MINOR; §0 dictionary).** The pointwise column still quotes OMEGA14's
`𝓛³/log𝓛` mass and "`log D ≍ κ𝓛 ≍ 𝓛⁴` (OMEGA14 Thm 4.5)". Thm 4.5 gives
`𝓛⁴/log𝓛`; the `𝓛⁴` lower bound is this file's Prop 4.2, which uses the note's
`t³` mass. *Repair:* update the two cells to point at Prop 4.2 and note Cor 4.3.

**D8 (MINOR; Thm 4.3 item 1, "KARY3 Thm 4.1 (PROVED, internal)").** For
mixtures containing Case-A classes, KARY3 Thm 4.1 relies on ElT §7 (published,
not re-proved). For ℛ(M)+selector families the only input is Shiu. *Repair:* copy
KARY3's proviso.

**D9 (MINOR; Thm 4.1 paragraph "the critical *level* is `λ* ≍_A L·P + λ_s`").**
The barriers (U−)/(L−) only force `λ ≥ c·L·P` from the big coordinates. Nothing
forces a certificate to pay `λ_s`, so the lower bound `λ* ≳ λ_s` is unproved.
*Repair:* "`c·L·P ≤ λ* ≤ C_A·L·P + λ_s`". This is `≍ L·P` when `λ_s ≪ L·P`, which
holds in both ES instances (`λ_s ≍ t⁴` with a smaller constant in the note
ledger, `≍ polylog` for OMEGA13).

**D10 (MINOR; §3).** See Claim 3.

## Points checked and found correct (parent's "check hardest" list)
* Thm 2.1 Case B: the χ₁-twist unit-Haar identity (exhaustive check,
  535 092 cases), `ν ≥ 0` on `Ẑ^×` (from `ν ≥ 0` on ℤ and periodicity), and the
  factor `1+ε ≤ 3`.
* Prop 1.1:
  - conditioning on `n≡1 (24)`;
  - Cor 4.3 holds for every unit `c` (the note states "all `c`");
  - `{no event ≤ T} ⊆ {H_X=0}`, via the atom → `E_{M,D}` identity (20 451
    triples, 0 mismatches).
* Thm 4.1 (U−): KARY Thm 2.5 / Cor 2.6 apply fibrewise. All coordinates are
  light, `M=P` is deterministic, and `G ≥ F ≥ 0` gives `f ≥ 0`.
* Prop 4.2:
  - Cor 4.3 is uniform over all `c`;
  - `f_c(ℓ) ≤ z_j² ≤ ℓ^{1/3}` (note Lemma 2.2 proof);
  - the `Q`-prime bookkeeping holds.
* §4.2 multi-scale reading: correctly labelled Assessment.

## Verdict summary

| Claim | Verdict |
|---|---|
| Prop 1.1 | SOUND (D1) |
| Thm 2.1 | SOUND (D2, D3 expository) |
| §3 Prop 3.1 / Cor 3.3 / goal (a) | SOUND (D10) |
| Thm 4.1 | SOUND (D9) |
| Prop 4.2 | SOUND (D4, D5) |
| Thm 4.3 / unification | SOUND-AFTER-REPAIRS (D6, D7, D8; labels/wording only) |
| §4.4 LP | SOUND (exact reproduction) |

Scripts (from scratch): `scripts/review_unify_atoms.py`,
`review_unify_page.py`, `review_unify_thm41.py`, `review_unify_toylp_exact.py`
(and the float `review_unify_toylp.py`, which shows that float LPs are
unreliable at `P≥6`).

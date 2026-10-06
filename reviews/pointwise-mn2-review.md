# Review of POINTWISE_MN2.md (task R74, hostile reviewer)

Reviewer branch `side-agent/review-mn2` (merged `side-agent/adm-m` at fb981ad). Author has quit;
wording/label repairs are applied directly to `POINTWISE_MN2.md` in this branch, marked
"applied by reviewer". From-scratch scripts: `scripts/review_mn2_*.py`.

## Verdict summary (filled in progressively)

| claim | verdict |
|---|---|
| Lemma 1.1 | SOUND (label: name inherited inputs, D6) |
| Lemma 1.2 | SOUND |
| Lemma 1.3 | SOUND |
| Input (H) as quoted | SOUND (matches Henriot Thm 5 / Cor 1; constants effective but not explicit) |
| Lemma 2.1 | SOUND modulo (H) (MINOR D7) |
| Thm 3.1 | SOUND-AFTER-REPAIRS modulo (H) + MN Thm 5.1(a),(d) ("ineffective" D2; D5, D8) |
| §4 data | SOUND (all 16 table entries reproduced exactly, `scripts/review_mn2_delta.py`) |
| §4 Assessment | GAP / OVERCLAIMED (D2, D3, D4) — conclusion only heuristic; repaired wording |
| Prop 5.1 | SOUND as implication modulo (H); SI not precisely stated (D9); table label (D1) |
| §5 class-one CONJECTURE | label honest; the `s | a+b` reduction re-derived ✓ |

**Overall.** No FATAL defect, no mathematical error in any PROVED item. The analytic core
(Lemma 2.1: q-uniform completed-atom sums via Rankin + Henriot with discriminant 1) is correct
and the q-uniformity claim checks out. The defects are in the *Assessment* (§4): "ineffective"
is the wrong word, the bold universal "every prefix law" claim is unproved, and the `q_0^{1/2}`
threshold is an artefact of Markov at levels ≥ 1 (Chebyshev plausibly gives `q_0^{1}`), so the
"circularity" is a heuristic assessment, not a demonstrated fact. ADM_m remains OPEN.

## Defects (numbered)

* **D1 (MINOR, §6 table row Prop 5.1).** "PROVED modulo (H), SI" omits (G), NT, OMEGA10 Thm 3.4
  and MN Thm 5.1's inputs for the `W_m` conclusion. Repair: "implication SI ⇒ ADM_m PROVED modulo
  (H); `W_m` consequence CONDITIONAL on SI, (G), (H), OMEGA10 Thm 3.4". *Applied by reviewer.*
* **D2 (MAJOR wording, Thm 3.1 statement, §4 item 1, §6 table, report).** `c_1` is called
  "ineffective" and §4 says "no finite computation can certify that a given q_0 is large
  enough". NT/Henriot constants are effective, only not explicit. Repair: "not explicit
  (effective in principle; no explicit value in the literature)" and "no *explicit* q_0 is
  available". *Applied by reviewer.*
* **D3 (MAJOR, §4 item 2 bold claim).** "Every pointwise-controlled prefix law has distortion
  growing faster than `q_0^{1/2}`" is an unproved universal statement supported by three
  examples, one heuristic and data with `q_0 ≤ 19`. Repair: restrict to the three laws
  discussed and label "heuristic (Assessment), not proved". *Applied by reviewer.*
* **D4 (MAJOR, §4 / Thm 3.1 case (b)).** The `q_0^{1/2}` threshold comes from Markov at levels
  `a ≥ 1`; a second moment there (sketch in §F) plausibly gives `q_0^{−1+ε}`. Repair: note this
  in §4; the circularity then needs `C_ν ≫ q_0^{1−ε}`, which the data (§F) neither confirm nor
  refute. *Note applied by reviewer* (no new claim, flagged as unverified sketch).
* **D5 (MINOR, Thm 3.1 proof "First moments").** MN Thm 5.1(a),(d) are stated for atoms, applied
  here to restricted events `E^-`. Valid (see §E) but must be said. *Applied by reviewer.*
* **D6 (MINOR, Lemma 1.1 label).** State that it inherits the inputs of MN Thm 5.1 / OMEGA13
  Thm 3.4. *Applied by reviewer.*
* **D7 (MINOR, Lemma 2.1(v)).** Replace `Σ 2^{−iσ}(i+1)^{3^j−2}` by
  `Σ 2^{−iσ}(log q + i)^{3^j−2} ≪ (log q)^{3^j−1}`. *Applied by reviewer.*
* **D8 (MINOR, Thm 3.1 (c),(d)).** (c): `Σ_{ℓ≤q_0}ℓ^{−1+2ε} ≪ q_0^{2ε}` (not `log log q_0`);
  (d): needs `ε < 3/(2(C_K+4))` for `Y^ε Z^{−1/2} → 0`. *Applied by reviewer.*
* **D9 (MAJOR, Prop 5.1 hypothesis SI).** "(the level-(≥a_ℓ+2) terms)" and "(the analogous pair
  sum for j = 2)" leave SI undefined. Repair: define SI as the ν-weighted versions of exactly the
  three bounds (a)–(c) in the proof of Thm 3.1 (text supplied). *Applied by reviewer.*

## A. §4 data (recomputed from scratch) — numbers SOUND, headline claim OVERCLAIMED

`scripts/review_mn2_delta.py` (independent CRT-tensor implementation; definition of `H_m(Q)` taken
from MN §0/§3: all `M | Q`, `M ≥ 3`, `M ≡ −1 (m)`, all `D | A²`). Output (exact fractions):

```
m=5 q0=8 Q=168 phi=48 hard=12 delta=1/4 1/delta=4 q0^-1/2/delta=1.414 (#M=4)
m=5 q0=9 Q=504 phi=144 hard=18 delta=1/8 1/delta=8 q0^-1/2/delta=2.667 (#M=6)
m=5 q0=11 Q=5544 phi=1440 hard=132 delta=11/120 1/delta=10.91 q0^-1/2/delta=3.289 (#M=12)
m=5 q0=13 Q=72072 phi=17280 hard=898 delta=449/8640 1/delta=19.24 q0^-1/2/delta=5.337 (#M=24)
m=5 q0=16 Q=144144 phi=34560 hard=1796 delta=449/8640 1/delta=19.24 q0^-1/2/delta=4.811 (#M=30)
m=5 q0=17 Q=2450448 phi=552960 hard=17510 delta=1751/55296 1/delta=31.58 q0^-1/2/delta=7.659 (#M=58)
m=5 q0=19 Q=46558512 phi=9953280 hard=163044 delta=4529/276480 1/delta=61.05 q0^-1/2/delta=14.01 (#M=120)
m=7 q0=8 Q=120 phi=32 hard=10 delta=5/16 1/delta=3.2 q0^-1/2/delta=1.131 (#M=2)
m=7 q0=11 Q=3960 phi=960 hard=234 delta=39/160 1/delta=4.103 q0^-1/2/delta=1.237 (#M=7)
m=7 q0=13 Q=51480 phi=11520 hard=1624 delta=203/1440 1/delta=7.094 q0^-1/2/delta=1.967 (#M=16)
m=7 q0=17 Q=1750320 phi=368640 hard=34930 delta=3493/36864 1/delta=10.55 q0^-1/2/delta=2.56 (#M=40)
m=7 q0=19 Q=33256080 phi=6635520 hard=460160 delta=719/10368 1/delta=14.42 q0^-1/2/delta=3.308 (#M=80)
m=6 q0=11 Q=385 phi=240 hard=84 delta=7/20 1/delta=2.857 q0^-1/2/delta=0.8615 (#M=4)
m=6 q0=13 Q=5005 phi=2880 hard=842 delta=421/1440 1/delta=3.42 q0^-1/2/delta=0.9487 (#M=8)
m=6 q0=17 Q=85085 phi=46080 hard=9110 delta=911/4608 1/delta=5.058 q0^-1/2/delta=1.227 (#M=16)
m=6 q0=19 Q=1616615 phi=829440 hard=128030 delta=12803/82944 1/delta=6.478 q0^-1/2/delta=1.486 (#M=32)
```

Every entry of the §4 table (all three rows m = 5, 7, 6, and the derived `q_0^{−1/2}/δ` row) is
reproduced to the printed precision; `δ_5(Q(8)) = 12/48 = 1/4` agrees with MN's `48/192` mod 840.
Remarks: (i) for m = 6, 7 the quantity `q_0^{−1/2}/δ` grows slowly (m = 6: 0.86 → 1.49 over
q_0 = 11..19) — seven/five data points with `q_0 ≤ 19` say nothing about growth "faster than
`q_0^{1/2}`" asymptotically; (ii) the heuristic `log(1/δ) ≍ (log q_0)³` is not visible at this
range either (m = 5, q_0 = 19: `log(1/δ) = 4.1`, `(log 19)³ = 25.5`). See defect D3.

## B. Input (H) vs. the source — SOUND as quoted (constants not explicit, but effective)

Checked against `sources/henriot-1102.1643.pdf` (pdftotext), §2 (definitions: `‖P‖` = sum of
|coefficients| of P; `M_k(A,B,ε)` via (2.10); `Q* = ∏R_h`, `D* = disc Q*`), Thm 5 (p. 6) and
Cor 1 (p. 7):
* hypotheses: Q primitive (no "no fixed prime divisor" needed — that is exactly Henriot's gain
  over NT Thm 1), `0 < ε < α/(50g(g+1/δ))`, `F ∈ M_k(A,B,ε)`, `x ≥ c_0‖Q‖^δ`, `x^α ≤ y ≤ x`;
  `c_0` and the implied constant depend at most on `g, α, δ, A, B` — quoted correctly;
* Cor 1's RHS carries the extra restrictions `(n_1⋯n_r, D*) = 1`, `(n_i,n_j) = 1`; MN2 drops them,
  which is legitimate for `F ≥ 0` (upper bound). Product is over `g < p ≤ x` — quoted correctly.
* Application in Lemma 2.1(i): `Q_1 = qX + c_1`, `Q_2 = mX + c_2`, `qc_2 − mc_1 = −1`. Re-derived:
  both primitive and coprime; `Q = Q_1Q_2 = qmX² + (qc_2+mc_1)X + c_1c_2` has discriminant
  `(qc_2+mc_1)² − 4qmc_1c_2 = (qc_2−mc_1)² = 1`, so `D* = 1`, `Δ_{D*} = 1` (empty product).
  `‖Q‖ ≤ ‖Q_1‖‖Q_2‖ ≤ (2q+1)·2m ≤ 6qm` ✓. `ρ(p) = 2` for `p ∤ qm` (distinct roots since the
  resultant is ±1), `ρ(p) = 1` for `p | qm` ✓; `ρ_{R_h}(n) ≤ 1` ✓. `ε_0 = 1/1001 < 1/800 =
  α/(50g(g+1/δ))` at `g = 2, α = δ = 1/2` ✓.
* "Ineffective": the source gives no explicit constants, but nothing in the NT/Henriot argument
  is ineffective (no Siegel-type input); the constants are computable in principle. MN2 calls
  `c_1` "ineffective" (§3 Thm 3.1, §4 item 1, §6 table) — wrong word, see defect D2.

## C. Lemmas 1.1–1.3 — SOUND (Lemma 1.1: label nuance, D6)

* **1.1.** Re-derived from MN Thm 5.1's proof (MN review §T51): the four bad events are failure,
  heavy late prime (`o(1)`), cost `> x`, `S_res > x`; with `x = 4E/s_0` Markov gives `s_0/4` each,
  total `≤ 1 − s_0 + s_0/2 + o(1) < 1` ✓. Prefix: `E_ν[p_0(E)] = Σ_r ν(r)·1[c ≡ r (g)]φ(g)/φ(M)
  ≤ C_ν/φ(M)` (`g = gcd(M,Q_0)`, `φ(lcm)φ(gcd) = φ(M)φ(Q_0)`) ✓; pairs likewise ✓. ν must be
  supported on hard classes (stated) so no prefix atom fires ✓. It is a modification of a proof
  that is itself "PROVED modulo the inputs of OMEGA13 Thm 3.4/5.1"; "PROVED" is fine for the
  implication but the inputs should be named (D6).
* **1.2.** Completed at q ⇔ `v_ℓ(M) = a+1` and every other `p^b ‖ M` has `p^b < q` (prefix
  powers are `≤ q_0 < q`) ⇔ `M = qM_1`, `M_1 | L(q)` ✓. `max M ≤ qL(q)` ✓. T-independence for
  `T ≥ T(q)` ✓ (all of `C_{q'}`, `q' ≤ q`, present). Not used later in Thm 3.1.
* **1.3.** Each forbidden lift is `−mD mod ℓ^{a+1}` of a completed atom consistent mod
  `M/ℓ^{a+1}` (and mod `ℓ^a`, since the forbidden class must lie in the fibre); `−mD` is a unit
  mod M (`gcd(M, mA) = 1`) so it is one of the N lifts; #forbidden `≤ Y` ⇒ `f ≤ Y/N` ✓. Check of
  N: at ℓ = 2 (odd m), level 0 has `N = 1` — any completed consistent atom at q = 2 kills the
  process, but `M = 2` needs `m | 3`, impossible for `m ≥ 4` ✓.

## D. Lemma 2.1 — SOUND modulo (H) (minor imprecisions D7)

Re-derived line by line:
* (i) see §B ✓. `c_1 = (qc_2+1)/m ≤ q+1` ✓ (`c_2 ≤ m`).
* (ii) Rankin: `u_q(M_1) ≤ u_q(M_1)(M_1/X)^σ` on `M_1 > X` ✓; `1/φ(M_1) ≤ (M_1/φ(M_1))/X` ✓.
* (iii) `F` multiplicative in the joint sense; `M_2` condition (2.10) for multiplicative F ⇔
  `F(p^{ν_1},p^{ν_2}) ≤ A^{ν_1+ν_2}` and `F(a) ≤ B a^ε`. `(2b+1)^j ≤ 9^b` for `j ≤ 2, b ≥ 1` ✓;
  `f_2(p^b) ≤ (b+1)^{j−1}K_1·2·p^{bσ} ≤ (4eK_1)^b` (in the L(q) case even `p^{bσ} < q^σ ≤ e`; in
  the Y-smooth case `p^{bσ}` is unbounded in b but `≤ e^b` as `p ≤ Y`) ✓; `f_2(n) ≪ n^{ε_0}` with
  B independent of q because `σ ≤ ε_0/2` ✓. **Uniformity in q** holds: nothing in `(A_0,B_0,ε_0)`
  depends on q — this is the key point and it is correct.
* (iv) `∏_{2<p≤x}(1−ρ(p)/p) ≪_m (log x)^{−2}` uniformly (the only q-dependent factor is
  `(1−1/ℓ)/(1−2/ℓ) ≤ 2`) ✓; `Σ_{n≤x}τ(n²)^j/n ≪ (log x)^{3^j}` ✓; `Σ f_2(n)/n ≤
  ∏_{p<q}(1 + e2^{j−1}K_1/(p−1) + O_{K_1}(p^{−3/2}))` ✓ (the `e` is wasteful: `Σ_{p<q}(p^σ−1)/p
  = O(1)`, so exponent `2^{j−1}K_1` suffices; harmless). Covering of an M_1-block by O(1)
  t-blocks ✓; requirement `x ≥ c_0‖Q‖^{1/2}` handled by (vi) ✓.
* (v) The displayed `Σ_i 2^{−iσ}(i+1)^{3^j−2}` is imprecise: the block at `X = X_0 2^i` carries
  `(log X)^{3^j−2} ≍ (log q + i)^{3^j−2}`; still `Σ_i 2^{−iσ}(log q + i)^k ≪ σ^{−1}(log q)^k +
  σ^{−k−1} ≪ (log q)^{k+1}` (σ ≍ 1/log q), so the final `(log q)^{3^j−1}` stands (D7).
* (vi) `A ≪ q^{3/2}` ⇒ `τ(A²)^jτ(M_1)^{j−1} ≪ q^ε` ✓; Euler product `≪ (log q)^{K_1}` (≤ stated
  `2K_1`) ✓.
* Y-smooth variant ✓ (σ = min(1/log Y, ε_0/2), Euler factors converge since σ ≤ ε_0/2).

## E. Theorem 3.1 — SOUND modulo (H) and MN Thm 5.1(a),(d) (wording repairs D1, D5, D8)

Re-derived:
* *No bad step ⇒ success.* Not bad ⇒ `f ≤ Y/N ≤ θ` at levels `a_ℓ, a_ℓ+1` and `f = 0` above
  (Lemma 1.3), so `Λ(ℓ) ≤ (1−θ)^{−2} = K`, no death (`f = 1 > θ`), stop rule never fires ✓.
  `a_ℓ` is the first post-prefix level (`ℓ^{a_ℓ} ‖ Q_0`) ✓; for `ℓ ≤ q_0`, `a_ℓ ≥ 1` so case (a)
  is only `ℓ > q_0` ✓.
* *First moment.* The bound uses `p(E^-)Ψ(E^-)` for the **restricted** event `E^-`
  (`n ≡ −mD mod M_1ℓ^a`), which is not an atom (`M_1ℓ^a ≢ −1 (m)` in general). MN Thm 5.1(a)
  is stated for atoms, but the per-event computation (MN review §T51) never uses atom-ness except
  to get `p_new = 0` for completed consistent atoms, an inequality in the safe direction; so each
  `p(F)Ψ(F)` is a supermartingale for **every** unit-class event F on quarantined coordinates ✓.
  The text should say so (D5). Optional stopping at the (stopping) time of the step ✓;
  `Ψ_0(E^-) = K^{ω(M_1ℓ^a)} ≤ K^{ω(M_1)+1}` ✓; prefix factor `C_ν/φ(M_1ℓ^a)` (§C) ✓;
  summing D gives `τ(A²)` ⇒ `C_νK S_1(q)/φ(ℓ^a)` ✓.
* *Second moment (a = 0).* Re-derived: parametrise `M_1' = g u'` (`g = gcd(M_1,M_1') | M_1`,
  map injective), `φ(M_1') ≥ φ(g)φ(u')`, `K^{ω(M_1')} ≤ K^{ω(g)+ω(u')}`; with
  `τ(A²)τ(A'²) ≤ (τ(A²)²+τ(A'²)²)/2` and the symmetric bound, `E[Y²1_alive] ≪
  C_ν(log ℓ)^{O(K)}S_2(ℓ)` with `K_1 = K²` (stated `4K²` is an upper bound) ✓. `Π = 1[both
  consistent]` just before the step since both restrictions are fully revealed ✓.
* *(a)* `≪ C_νℓ^{−2+ε}`, summed `≪ C_ν q_0^{−1+ε}` ✓. *(b)* Markov `≪ C_ν q^{−1+ε}`;
  `#{q = ℓ^{a+1} ∈ (x,2x], a ≥ 1} ≪ x^{1/2}` ⇒ `≪ C_ν q_0^{−1/2+ε}` ✓ (dominant term). *(c)* ✓
  (`Σ_{ℓ≤q_0}ℓ^{−1+2ε}` is `≪ q_0^{2ε}`, not `log log q_0`; absorbed in ε — D8). *(d)* stage B:
  for `ℓ ∈ (Z^{1/2}, Z]` level 1 is a stage-B step with Markov `≪ (log Y)^C(qY)^ε/q`, giving the
  `Z^{−1/2+ε}` term; `Y^ε = 𝓛^{(C_K+4)ε}` is beaten by `Z^{−1/2} ≤ 𝓛^{−3/2}` once
  `ε < 3/(2(C_K+4))` — fine since ε is free, but this ε-dependence on K should be said (D8).
  Primes `ℓ ∈ (Z, Y]` (level 0 only in stage B) are covered by (a) ✓. `Z < Y` (needed so stage A
  stays inside `ℓ ≤ Y`) holds as `C_K + 4 > 3` ✓.
* *Constants.* `c_1` depends on `m, θ, ε` and the (non-explicit but effective) constants of (H);
  "ineffective" is wrong (D2).
* *Uniformity in T* ✓ (all sums are over T-independent sets `M_1 | L(q)`; T enters only via
  `Z, Y` in (d)).

The "Consequently" clause ✓ (with Lemma 1.1, success ≥ 1/2).

## F. §4 Assessment — numbers SOUND; two of its three supporting statements OVERCLAIMED (D2, D3, D4)

* Item 1 ("`c_1` is not explicit ⇒ no finite computation can certify q_0"): the constants of
  NT/Henriot are effective (pure sieve/elementary arguments, no Siegel-type input) — just not
  written down. "No finite computation can certify" is false in principle; what is true is
  "no explicit q_0 is available from the literature, and an explicit one would be astronomically
  large". (D2)
* Item 2 (bold: "**Every** pointwise-controlled prefix law has distortion growing faster than
  `q_0^{1/2}`"): unproved universal statement. Only three laws are discussed; for the uniform law
  the text itself says "(Not proved …)"; the data stop at `q_0 = 19` and for m = 6 grow from 0.86
  to 1.49 only. (D3)
* The threshold `q_0^{1/2}` is an artefact of using **Markov** at the levels `a ∈ {a_ℓ, a_ℓ+1},
  a ≥ 1` (case (b)). Reviewer's sketch (same ingredients as the proof's a = 0 case, not part of
  the reviewed claims): the pair bound at level `a ≥ 1` gives `Π^{Haar} = φ(g)/(φ(M_1)φ(M_1')φ(ℓ^a))`
  (the `ℓ^a` part is shared), so `E[Y²1_alive] ≪ C_ν(log q)^{O(K)}S_2(q)/φ(ℓ^a)` and Chebyshev
  gives `P ≪ C_ν q^{−1+ε}ℓ^{−1}`, summing to `≪ C_ν q_0^{−1+2ε}` over case (b); case (c) is
  already `q_0^{−1+ε}`. So the circularity criterion is plausibly "`C_ν` grows faster than
  `q_0^{1−ε}`", not `q_0^{1/2}`. Against `q_0^{−1}/δ` the data are: m = 5: 0.50, 0.89, 0.99, 1.48,
  1.20, 1.86, 3.21; m = 7: 0.40, 0.37, 0.55, 0.62, 0.76; m = 6: 0.26, 0.26, 0.30, 0.34 — slow
  growth, inconclusive. The Assessment's conclusion survives only via the unproved heuristic
  `log(1/δ) ≍ (log q_0)³`. (D4)
* "This is an assessment of a proof method, not an obstruction to ADM_m" — correct and honest.

## G. Proposition 5.1 — SOUND as an implication; SI not precisely stated; label (D1, D9)

* The ν-weighted weight: `E_ν[p_0(E^-)] = E_ν[1[−mD ≡ r (g)]]·φ(g)/φ(M_1ℓ^a)`,
  `g = gcd(M_1ℓ^a, Q_0)`; at ν = Haar this gives back `1/φ(M_1ℓ^a)`, consistent with the
  normalisation `S^ν_1(q)/q` ✓.
* SI is stated with "(the level-(≥a_ℓ+2) terms)" and "(the analogous pair sum for j = 2)" left
  unspecified — not a well-defined hypothesis (D9). Stage B is not in SI but is `C_ν·o(1)` for
  fixed q_0 ✓.
* "with Lemma 1.1 and MN Thm 5.1 this gives `W_m(p) ≥ …`": the text lists (G), NT/(H), OMEGA10
  Thm 3.4 and SI ✓, but the §6 table says only "PROVED modulo (H), SI" (D1).
* Class-one computation re-derived: `mdab = M+1 ≡ 1 (mod s)` (s | M) ⇒ `mD+1 ≡ mda(a+b)` and
  `gcd(mda, s) = 1` ⇒ `s | mD+1 ⟺ s | a+b` ✓. CONJECTURE label honest.

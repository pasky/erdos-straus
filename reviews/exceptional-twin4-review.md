# Hostile review: EXCEPTIONAL_TWIN4.md (task O12), branch side-agent/twin-ternary @ e94ee5e

Scope: `EXCEPTIONAL_TWIN4.md` (TW4), `reviews/agent-reports/AGENT_REPORT_O12.md`,
`scripts/twin4_rough_bt.py`. Context: TW3 (Lemmas 3.1–3.4, 6.1–6.2, Prop 6.3,
§6.3), TW3 review rounds 1–2 (E10–E14), TW2 (Setting 3.0, Lemmas 2.1–2.2,
3.2–3.4, 4.1, 5.4). Defects are numbered F1, F2, … (severity: major / minor / nit).

## Item 1. Lemmas 2.1–2.3 (rough-partner Brun–Titchmarsh) — SOUND

Line-by-line check of the proof of Lemma 2.3.
* Split `R = d·n`, d = the Z-smooth part. `Ω(d) = Ω(R) ≤ s` would give
  `R = d ≤ Z^s = Y^{s/(s+1)} < Y ≤ x`, contradicting `R > x`. So
  `Ω(d) ≤ s−1`, `d ≤ Z^{s−1}`, and `n > 1` has all primes `> Z`. ✓
* `(d,q) = 1` from `(R,q) = 1`, so n lies in one reduced class mod q, in
  `(x/d, 2x/d]`; the k with `n = n₀ + qk` lie in `≤ x/(dq) + 1` consecutive
  integers. For `p ≤ Z`, `p ∤ q`, `p ∤ n` excludes exactly the class
  `k ≡ −n₀q̄ (p)`; `ω(p) = 0` for `p | q`. Then
  `J ≥ Σ_{d≤Z,(d,q)=1} μ²(d)/φ(d)` (`ω/(p−ω) = 1/(p−1)`), and
  van Lint–Richert plus `Σ_{d≤Z}μ²/φ ≥ log Z` (valid for `Z ≥ 1`; here
  `Z ≥ 2` because `Y ≥ 2^{s+1}`). ✓
* Numerator: `Y/d ≥ Y/Z^{s−1} = Z² ≥ 4`, so `Y/d + 1 + Z² ≤ 3Y/d`, giving
  `#{n} ≤ 3x/(dφ(q)log Z)` and `Σ 1/R ≤ 3/(dφ(q)log Z)` per d. ✓
* `Σ_d 1/d ≤ Σ_{i<s}(Σ_{w<p≤Z} 1/(p−1))^i` (ω(d) ≤ Ω(d) ≤ s−1; the
  expansion over-counts). `log Z = log Y/(s+1)`. ✓
* Lemma 2.1 (Montgomery's arithmetic large sieve, `(N+Q²)/J`; MV have
  `N−1+Q²`) and Lemma 2.2 (van Lint–Richert) are correctly quoted.
* Remarks (i), (iii) ✓: `Σ_{w<p≤Z}1/(p−1) ≤ log log Z − log log w + O(1/log w)`,
  and with `log Z ≤ L`, `log w ≥ log L` this is `≤ log L` for L large.

**Independent numerical test** (`reviews/exceptional-twin4-check-lemma23.py 4e6 7`;
own code, different sieve algorithms; < 1 min, < 1 GB). `s = 1…5`,
`w ∈ {2,3,7,50,300,2000}`, 30 moduli q (including 30030, 4620, powers of 2,
primes up to 65537, 12 random q < 10⁵), x at the threshold `x = q·2^{s+1}`,
at `x₀+1`, `1.5x₀` and on a ×4 grid up to 2·10⁶, all units b (or 300
random). **631 686 cases, worst `lhs/bound = 0.126`** (worst at the
threshold 0.096). The author's run replays (1228 cases, 0.128). The
constant is loose by ~8×, as expected from `log Z = log Y/(s+1)` and the
factor 3.

No defect.

## Item 2. Corollary 2.4 (dyadic sum) — SOUND (nit F1)

Blocks `(2^i x₀, 2^{i+1}x₀]`, `0 ≤ i ≤ 2L`, cover `(x₀, X]` (`2^{2L} ≥ X`);
each block meets `x ≥ q·2^{s+1}`; `log Y_i ≥ (s+1+i)log 2`, so
`Σ_i 1/log Y_i ≤ (1/log 2)·log(2L+s+2) ≤ 2 log L` for L large. With
`H ≤ log L` (Remark (iii), `Z ≤ X`, `w₂ = L^8 ≥ L`),
`Σ_{i<s}H^i ≤ s(log L)^{s−1}` in both cases `H ≥ 1`, `H < 1`. The product
is `6s(s+1)(log L)^s/φ(q)`; the stated `12s(s+1)` is a factor 2 generous.
* **F1 (nit, wording).** §2 says the large sieve gives the upper bound
  "losing nothing". It loses the factor `3(s+1)` and the `(log L)^{s−1}`
  harmonic factor (both harmless for fixed s). Say "losing only constants
  and a polylog".

## Item 3. Proposition 3.1 (reduction, bounded arity; r-ary inflation) — SOUND

Checked against TW2 Lemmas 2.1–2.2, TW3 Lemmas 6.1–6.2 and TW3 review
R2.4/E10.
* **δ_r arithmetic.** `(8/7)^r·(4/3)^r·δ_r = (32/21)^r(21/32)^r/(16r) = 1/(16r)`.
  So on supp P, `w_ℓ ≤ (8/7)^r w^U_ℓ ≤ (3/4)^r/(16r)` (needs `ν ≤ (8/7)U` at
  every coordinate of the event, i.e. `p_ℓ ≤ 1/8` for all large ℓ, which
  `G_L^{(r)}` includes), and after quarantine
  `w⁺_ℓ ≤ (4/3)^r w_ℓ ≤ 1/(16r)`, so `Σ_{ℓ∈S(E)}w⁺_ℓ ≤ 1/16` for every
  event (`|S(E)| ≤ r`). ✓ This is exactly the slack E10(c) asked for.
* **Quarantine.** `ν(H_ℓ) ≤ Σ_a ν(a)D_{(ℓ,a)} = w_ℓ`, `U(H) ≤ ν(H)` (ν is
  uniform off `U_ℓ`), so `p⁺ ≤ p + w ≤ 1/4` and every point mass grows by
  `(1−p)/(1−p⁺) ≤ 4/3`. An r-ary event's mass grows by `≤ (4/3)^{|S(E)|}`. ✓
  Hubs cost `ν(H_ℓ) ≤ S_ℓ` in the unary factor; `S_ℓ` is the vertex-star
  term with `min(D,1)²`. ✓
* **Star terms after quarantine.** For a non-hub vertex, `D < 1` in ν, so
  `(D⁺)² ≤ (4/3)^{2(r−1)}D² = (4/3)^{2(r−1)}min(D,1)²` (the uncapped vertex
  term of TW3 Lemma 6.2(3) is harmless). For `|σ| ≥ 2`,
  `min(D⁺,1)² ≤ min(cD,1)² ≤ c²min(D,1)²` with `c = (4/3)^{r−|σ|}`.
  With `π⁺_σ ≤ (4/3)^{|σ|}π_σ` and `ρ̃^σ ≤ (4/3)^{|σ|}ρ^σ` the total factor
  is `≤ (4/3)^{2r} ≤ (4/3)^{3r}` as stated. Promotion only lowers D and w
  (TW3 Lemma 6.2(1)–(2)). ✓
* TW3 Lemma 6.1 then needs (H_δ), δ = 1/16, for the quarantined + promoted
  system, which holds; `1+25δ ≤ 2.57`. The tilting cost `4L^{1/2}` needs
  only `P′(G_L^{(r)}) ≥ 1/2` (Lemma 4.1). ✓ `C_r = e^{O(r)}` is right.

**Splitting (3.1).** The inequality
`min(x+y+z,1)² ≤ 2min(x,1) + 2min(y,1)² + 6z` holds: if `x ≥ 1` or `z ≥ 1/6`
the right side is `≥ 1`; otherwise with `t = min(x+y+z,1)` and `b = min(y,1)`,
`t² ≤ t(x+b+z) ≤ x + (b+z)² ≤ x + 2b² + 2z`. The identity
`Σ_a π_{(V,a)}D^{pp}_{(V,a)} = Σ_{pp E ⊋ V}π_E` (via `π_σπ_{E∖σ} = π_E`, lifts
included) and `< 2^r` subsets per class give the `T_pp` bound; the `T_ev`
bound is `π_σρ^σ = π_Eρ^{S(E)}` for σ an event. ✓

No defect.

## Item 4. Lemma 4.1 (fibre law `G_L^{(r)}`, `w₂ = L^8`) — SOUND

* Expanding `E′(w^U_j)²` over pairs of classes: joint activity under P′ is
  `≤ 2Γ(lcm)/lcm` (TW2 Lemma 3.2(1) for P′; zero if the two congruences are
  inconsistent). With `f(k) ≤ (k/φ(k))F_j` uniformly in k, the k-double sum
  `Σ_{k,k′}(Γ(lcm)/lcm)(k/φ(k))(k′/φ(k′))` has Euler factors `1 + O(1/p)`
  over `p ≤ w₂`, so it is polylog. The three top-prime cases are combined by
  `(a+b+c)² ≤ 3(a²+b²+c²)`. ✓
* `P = j`: `M ≤ j^{1+B}`, `τ(A²) ≤ C_εj^{(1+B)ε} = C_εj^{1/256}`,
  `Σ_v j^{−v} ≤ 2/j`, and `≤ r−1` other prime powers give `(2log L)^{r−1}`
  (summing over the number of them costs a factor r). ✓
* `P ≠ j`, `P² | M`: `Σ_{P>j}Σ_{e≥2}P^{−e+1/256} ≪ j^{−1+1/256}`, times
  `2/j`. ✓
* `P ≠ j`, `P ∥ M`: `q = M/P ≤ P^B` (B-hypothesis), Lemma 3.3 needs
  `q ≤ (2y)^{B+2}` only on nonempty blocks (true), `≤ 2L` blocks above the
  largest other prime, each `≪ (q/φ(q))(log 2qy)² ≤ (q/φ(q))(2L)²` since
  `qy ≤ X`. `q/φ(q) ≤ (k/φ(k))(1+1/w₂)^r`. So `F_j ≪ j^{−1}L³(log L)^{r}`. ✓
* Markov: `Σ_j P′(w^U_j > δ_r) ≤ δ_r^{−2}Σ_j E′(w^U_j)² ≪_r L^{−2}(log L)^{O(r)}`;
  `δ_r^{−2} = e^{O(r)}`. The unary part is TW2 Lemma 3.4 verbatim. ✓

The Remark is right: TW3's `w₂ = L^{10}` came from the arity-uniform
condition `w_ℓ ≤ δlog ℓ/L`; for fixed r the per-vertex condition suffices.
Together with Cor 5.2(1) (whole-event stars) this discharges both inputs
that review E11 listed as missing, for every fixed r.

No defect.

## Item 5. Lemma 5.1, Corollary 5.2, (5.1) — SOUND

* (5.1): activity `≤ 4Γ(k)/k` and `π_{E_C} ≤ (8/7)^{|S(C)|}k/M`, at most
  `τ(A²)` classes per modulus. ✓ (Weights need only be `≥ 0`, not `≤ 1`;
  Lemma 5.3 uses `β = Σ_Vρ^V1[…] ≤ 2^r`. Harmless.)
* Lemma 5.1: `q = kq₀ ≤ P^B`; dyadic blocks from `y₀ = p₂/2`; the Shiu sum
  gives `(q/φ(q))p₂^{−α}(a²/α + a/α² + 1/α³)` with
  `a ≥ log(2qy₀)`, `a ≤ log 2k + r log p₂` (`q₀ ≤ p₂^{r−1}`). Summing
  `p₂^{−1−α}(log p₂)^i` gives `α^{−3}` for i = 1, 2 against the matching
  `1/α` powers and `α^{−3}log L` for the `1/α³` term; the `≤ r−2` other
  primes of `q₀` give `(log L)^{r−2}`; `q₀ = 1` is the case `p₂ := w₂`. ✓
* Cor 5.2(2): the two pp cases (top prime squared / top prime simple and
  another large prime squared) are exhaustive. In the first,
  `τ ≤ C_εP^{1/256}`, `Σ_k Γ(k)/k` is polylog (no constraint on k needed),
  `Σ_P P^{−2+1/256} ≪ w₂^{−1+1/256}`. In the second, Shiu along P
  (`≤ 2L` blocks, `L³`) and `Σ_{ℓ,e≥2}ℓ^{−e} ≪ 1/w₂`. Total `o(1)`. ✓

No defect.

## Item 6. Lemma 5.3 (small partners, every star) — SOUND (nit F2)

The author asked to check the Shiu hypotheses in (b).
* (a) `P ∈ V`: `ρ^V ≤ P^{−α}`, `< 2^r` sets V, Lemma 5.1. ✓
* (b) `P ∉ V`: `P | R ≤ (kQ_V)^{C₀}`. `q = kQ_VR′ = M/P ≤ P^B` (B-hypothesis),
  so on every nonempty block `q ≤ (2y)^B ≤ (2y)^{B+2}` — Lemma 3.3 applies,
  with constant depending on B only. P is the top prime, so the blocks start
  above the largest prime of `q` (`≥ w₂/2`), and stop at `(kQ_V)^{C₀}`.
  `log 2qy ≤ (C₀+1)log(2kQ_V) + log R′ ≤ (2C₀+1)log(2kQ_V)` uses
  `R′ ≤ R ≤ (kQ_V)^{C₀}`. ✓ The V-sum: power mean
  `(Σ_{i≤v+1}x_i)³ ≤ (v+1)²Σx_i³`, `Σρ_ℓ(log ℓ)³/ℓ ≪ α^{−3}`; V is nonempty,
  so the `α^{−3}` gain is always available. ✓ Weight bookkeeping:
  `Γ(k)/M·τ = (Γ(k)/(kQ_VR′))·(τ/P)` with `τ/P` summed by Shiu. ✓
* **F2 (nit, constants).** The number of blocks is
  `≤ C₀log₂(kQ_V) + 2`, not `C₀log(kQ_V) + 1`; and (5.1) is stated for
  `β_C ∈ [0,1]` but used with `β_C ≤ 2^r`. Neither affects the bound.

## Item 7. Lemma 6.1 (largest-variable reduction mod Q, any partner) and the ternary residual — SOUND

The author asked to check `R ≥ 2^r q`.
* *t largest.* `u, v | A` and `4A ≡ 1 (mod kQ)`, kQ odd, so `(q,kQ) = 1`
  for `q = 4uv`, and `q | kQR+1` is the single reduced class
  `R ≡ −(kQ)^{−1} (mod q)`. The residue mod Q is `−u/v` (TW3 (3.1) holds
  mod Q since `4A ≡ 1 (mod Q)`). Each R gives at most one triple
  (`t = A_R/(uv)`). ✓
* *Claim `R ≥ 2^r q`.* If `q ≤ 2^{−r}(kQ)^{C₀}`: `R > (kQ)^{C₀} ≥ 2^r q`.
  Otherwise `t ≥ max(u,v) ≥ (q/4)^{1/2}` gives `kQR+1 = 4A_R ≥ q^{3/2}/2`,
  so `R/q ≥ q^{1/2}/(2kQ) − 1 > 2^{−r/2−1}(kQ)^{C₀/2−1} − 1 ≥ 2^r` once
  `(kQ)^{C₀/2−1} ≥ 2^{3r/2+2}`, true for `C₀ ≥ 6`, `kQ > w₂`, r fixed
  (indeed any `C₀ > 2` works; TW3's `C₀ ≥ 5` constraint (E8) is no longer
  binding). ✓ If `2^r q > X` there is nothing to sum.
* Cor 2.4 with `s = r−h`, `s+1 ≤ r` (as `h ≥ 1`), so `x₀ = 2^r q ≥ 2^{s+1}q`;
  `s(s+1) ≤ r²`; `φ(4uv) = 2φ(uv)` (uv odd). This gives
  `6r²(log L)^{r−1}R₁(a)` — one log better than stated. u- and v-largest:
  same with `q = 4vt`, `4ut`, `max(v,t) ≥ (q/4)^{1/2}`; dropping `(u,v) = 1`
  only adds terms. ✓
* `𝓡_{Q,k}` does not exclude R sharing primes with Q or non-squarefree R;
  these only enlarge `V_{Q,k}`, which is used as an upper bound. ✓

**Ternary residual.** TW3's residual classes `M = kjℓ_aℓ_b`,
`R = ℓ_aℓ_b > (kj)^{C₀}`, at the vertex `V = {j}` have `R ∈ 𝓡_{j,k}` with
`h = 1`, `Ω(R) = 2 ≤ r−1`, so Lemma 6.1 covers them regardless of
`ℓ_b` vs `w₂q`. The point is genuine and correct: TW3 fixed `ℓ_a` and asked
for primes `ℓ_b` in a short progression (BFI range); sieving the whole
partner R over its class mod q needs only `R/q ≥ 2^{s+1}`, and the loss
for not using primality is the polylog `(log L)^{s−1}`. The toy table
(§8, replayed exactly) confirms the residual was 80–86% of the toy mass,
so this is a real closure, not a negligible piece.

No defect.

## Item 8. Lemma 6.2 and Corollary 6.3 (box counting mod squarefree Q) — SOUND

* (i) Q odd squarefree, `c/t` a unit: `v² ≡ c/t` has `≤ 2^h` roots (CRT).
  The box bound `min(V(T/Q+1), 2^hT(V/Q+1)) ≤ 2^h(VT/Q + min(V,T))` holds
  (split `V ≤ T` / `T < V`), so each box contributes
  `≤ 2^h(1/Q + 1/max(V,T))`. ✓ (ii) `N ≠ N′ ≡ (Q)`, both ≥ 1 ⇒ `max > Q`. ✓
  (iii) `u ≡ ρv`, ρ a unit; `Q | uv′−u′v ≠ 0`,
  `|uv′−u′v| ≤ max(u,v)max(u′,v′)`; fixing u fixes v mod Q. ✓
* Cor 6.3: `n/φ(n) ≤ 2log L` for `n ≤ X²`; `a ↦ c` bijective on units,
  `V(a) = 0` off units; with `Q > L^8`, `X = e^L`:
  `L⁴/Q ≤ L^{−4}`, and `(log Q)Q^{−1/3}` is decreasing for `Q > e³`, so
  `L²(log Q)Q^{−1/3} ≤ 8L^{−2/3}log L` uniformly in `Q ≤ X`. The `2^h ≤ 2^r`
  is absorbed in `C_r`. Exponent `2r+4` = `(log L)^{2r}` (Lemma 6.1 squared)
  × `(2log L)^4` (two `1/φ` conversions squared). ✓

No defect.

## Item 9. Lemma 6.4 (large part; lifted residues) — SOUND

The author asked to check the lifts.
* For an sf class C ⊋ V, the events of C containing a lifted star
  `σ = (V,a)` are the lifts at `S(C)∖V`; `Σπ_{E∖σ}` over them is
  `Π_{ℓ′∈S(C)∖V}ν_{ℓ′}(lifts of the class residue mod ℓ′) ≤ (8/7)^{s}/R`,
  independent of the lift a and of the alphabet exponents. So `z_V(a)`
  depends only on `a mod Q`. ✓ (Identical events from different classes are
  counted with multiplicity: upper bound.)
* `Σ_{a ≡ a₀ (Q)}π_{(V,a)} = Π_{ℓ∈V}ν_ℓ(a ≡ a₀ mod ℓ) ≤ Π(8/7)/ℓ` since
  `ν_ℓ ≤ (8/7)U_ℓ` pointwise on supp P. ✓
* Pair activity `≤ 4Γ(lcm)/lcm`, AM–GM with `Σ_{k′}Γ(lcm)/lcm ≤ Γ(k)h(k)/k`
  (TW2 Lemma 5.4(ii)), Cor 6.3 uniformly in Q, k, then
  `Σ_{|V|=h}ρ^V/Q_V ≤ (log L)^h`, `h ≤ r−1`. Total
  `(log L)^{2r+4+O(1)+r−1}`. ✓ (The factor is `(8/7)^{h+2s} ≤ (8/7)^{2r}`;
  `(8/7)^{3r}` is generous.)

No defect.

## Item 10. Theorem 7.1 and Corollary 7.2 (assembly) — SOUND (nit F3)

Prop 3.1 (Item 3) + Lemma 4.1 (supp P ⊆ `G_L^{(r)}`, TW2 Lemma 3.2 holds) +
TW2 Lemma 4.1 (unary) + (3.1) + Cor 5.2 + `min(x+z,1)² ≤ 2x + 2z²` with
Lemma 5.3 (x-part) and Lemma 6.4 (z-part). Small/large at V partition the
sf classes (`R ≤` vs `> (kQ_V)^{C₀}`). The total is
`L^{3/4}(log L)^{2r+O(1)} + (log L)^{3r+O(1)}`, within the stated
`L^{3/4}(log L)^{3r+O(1)}` (the `2r` form is also true). Every use of the
B-hypothesis is on the top prime (Shiu `q ≤ P^B`, pointwise `τ ≤ P^{1/256}`).
* **F3 (nit, citation).** Cor 7.2's "cannot give an exceptional-set
  exponent θ > 3/4" is the ET Lemma 2.9 translation (level `λ ≍ L`; TW
  review T7 on the λ-range), as in EXCEPTIONAL_TWIN.md §5. Cite it; the
  translation is inherited, not re-proved here. (Theorem 7.1 is uniform in
  `λ ≤ A₀L`, so the λ-range condition is met.)

## Item 11. §7.1 (unbounded r, dropping B) — honest Assessment

Labelled OPEN / Assessment in §0, §7.1 and the report. The sketch for
`r ≤ ε log L/log log L` is plausible: every r-dependence found in this
review is `e^{O(r)}`, `r^{O(1)}` or `(log L)^{O(r)} = L^{O(ε)}`; Lemma 4.1 needs
`L^{6+O(ε)}/w₂ = o(1)`; the `R ≥ 2^r q` claim needs `w₂² ≥ 2^{O(r)}`. Not
verified in detail, and correctly not claimed.

## Item 12. Numerics, script, report, labels — SOUND-AFTER-REPAIRS (nit F4)

* Both replays reproduce exactly: Part A 1228 cases, worst 0.1281; Part B
  table to all digits (24 s, ≤ 1.2 GB).
* **F4 (nits).** (a) Part B enumerates `ℓ_a ≤ ℓ_b` including `ℓ_a = ℓ_b`,
  so `R = ℓ²` (non-squarefree) partners are in the toy table; state it or
  use `prs[ia+1:]`. It uses `w₀ = 11` for both roughness and the
  proved/residual cut, and `C₀ = 1` (stated). (b) The report says
  `R/q ≥ 2^{s+1}` "always holds"; it holds for *large* partners
  (`R > (kQ)^{C₀}`, `C₀ > 2`, L large). (c) §0 "Thm 7.1 … not yet
  reviewed" should be updated after this review.
* Lemma 2.3 independently tested (Item 1): 631 686 cases, worst 0.126.

## Summary

| item | verdict | defects |
|---|---|---|
| 1 Lemmas 2.1–2.3 (rough-partner BT) | SOUND | — (independent check 631 686 cases, worst 0.126) |
| 2 Cor 2.4 | SOUND | F1 nit |
| 3 Prop 3.1 (r-ary inflation), (3.1) | SOUND | — |
| 4 Lemma 4.1 (fibre law, `w₂ = L^8`) | SOUND | — |
| 5 Lemma 5.1, Cor 5.2 | SOUND | — |
| 6 Lemma 5.3 (Shiu in (b)) | SOUND | F2 nit |
| 7 Lemma 6.1 (`R ≥ 2^r q`), ternary residual | SOUND | — |
| 8 Lemma 6.2, Cor 6.3 | SOUND | — |
| 9 Lemma 6.4 (lifts) | SOUND | — |
| 10 Thm 7.1, Cor 7.2 | SOUND | F3 nit |
| 11 §7.1 Assessment | honest | — |
| 12 Numerics, report, labels | SOUND-AFTER-REPAIRS | F4 nits |

No major or minor defect found. The four points the author flagged all
check out: the r-ary inflation closes with exactly the slack E10(c) asked
for (`(32/21)^r δ_r = 1/(16r)`); lifted residues cost `(8/7)^h/Q` and
leave `z_V` a function of `a mod Q`; Shiu in Lemma 5.3(b) has
`q = M/P ≤ P^B` on every nonempty block; and `R ≥ 2^r q` follows from
`R > (kQ)^{C₀}` with any `C₀ > 2`. Theorem 7.1 (fixed r, fixed B) and the
closure of the TW3 ternary residual by a large-sieve upper bound stand.
TW3 review E11 is discharged for every fixed r. F1–F4 are cosmetic.

Suggested ledger text (the author's, endorsed): "Moduli with ≤ r large
primes, r fixed: cap `≪ L^{3/4}(log L)^{O(r)}` PROVED (EXCEPTIONAL_TWIN4
Thm 7.1, reviewed SOUND). The ternary residual closes by a large-sieve
upper bound for rough partners. Open: r unbounded, and dropping B."

---

# Round 2 — commit b3244dd (§§9–11; repairs F1–F4)

New defects are numbered G1, G2, …

## R2.1 Repairs F1–F4 — all FIXED

| defect | fix at b3244dd | status |
|---|---|---|
| F1 "losing nothing" | "losing only constants and a polylog" (§2) | FIXED |
| F2 block count; β range | `C₀log₂(kQ_V)+2`; (5.1) note "valid for any `β_C ≥ 0`" | FIXED |
| F3 θ-translation citation | Cor 7.2 cites ET Lemma 2.9 / TW review T7, uniform in `λ ≤ A₀L` | FIXED |
| F4 toy `R = ℓ²`; "always"; §0 label | stated in §8; "for every large partner" (§6, report); §0 marks Thm 7.1 reviewed | FIXED |

## R2.2 Proposition 9.1 (explicit r-dependence) — SOUND

The loss table covers every r-dependence I found in round 1: inflations,
`δ_r^{−1}`, `2^r` subsets, harmonic sums `(2log L)^r`, `r²` from Lemmas 5.1,
5.3(b) and Cor 2.4, and `2^h`, `(8/7)^{3r}`, `(log L)^h` in §6. Shiu's
constant depends on B only. Side conditions that must stay true for
`r ≤ log L`, and do: `R ≥ 2^r q` in Lemma 6.1 needs
`(kQ)² ≥ L^{16} ≥ 2^{1.5r+2}`; `q/φ(q) ≤ 2k/φ(k)` needs
`(1+1/w₂)^r ≤ 2`; `p⁺ ≤ 1/4`. Lemma 4.1 needs
`e^{O(r)}(log L)^{O(r)}L^{6−8} = o(1)`, which holds for
`r ≤ ε₀log L/log log L`. Then `(C_Blog L)^{Cr} ≤ L^{Cε(1+o(1))}`. ✓

## R2.3 Lemma 9.2 (unweighted payment, LLL with mixed x) — SOUND (G1 minor)

* Monotonicity: `A⁺∩A⁺′ ⊆ A₁⁺∩A₁⁺′`. In the `ν⁺` product space the unary
  sets are null, so `P(A⁺) = P(A₁⁺)P(no 𝓔₂ | A₁⁺)` and the unary factors
  cancel. ✓
* LLL hypothesis (TW2 Lemma 1.1). For `F ∈ 𝓔₁`:
  `Σ_{Γ(F)}x ≤ Σ_{ℓ∈S(F)}(2w⁺_ℓ + y_ℓ)` (the 𝓔₁ neighbours through ℓ carry
  `2w⁺_ℓ`, the 𝓔₂ neighbours carry `y_ℓ`). All `x ≤ 1/8`, so
  `Π(1−x) ≥ e^{−(8/7)Σx} ≥ 1/2` and `P(F) = x_F/2`. For `G ∈ 𝓔₂`:
  `P(G) = 2^{−|S(G)|}x_G` and `Π(1−x) ≥ e^{−c|S(G)|} ≥ 2^{−|S(G)|}`. ✓
* Conclusion: the chain rule with Lemma 1.1(1), `𝓢 = 𝓔₁ ∪ G_{<i}`, gives
  `P(no 𝓔₂ | A₁⁺) ≥ Π(1−x_{G_i}) ≥ e^{−(8/7)m₂}`, so the cost is
  `(16/7)m₂ ≤ 3m₂`. ✓ TW2 Lemma 2.1 accepts any nonempty `A⁺ ⊆ A`. ✓
* **G1 (minor, hypothesis mismatch; the proof survives).** Lemma 9.2 assumes
  `Σ_{ℓ∈S(F)}w⁺_ℓ ≤ 1/32`, but Prop 3.1 (and Thm 10.4) deliver only `1/16`,
  and Cor 9.3 never checks this hypothesis. The proof works with `1/16`:
  `Σ_{Γ(F)}x ≤ 2/16 + 1/32 = 5/32` gives `Π ≥ e^{−0.18} ≥ 1/2`; per vertex
  `w⁺_ℓ ≤ 1/16`, so `Σ_{Γ(G)}x ≤ (5/32)|S(G)|` gives
  `e^{−0.18|S|} ≥ 2^{−|S|}`; `x_F ≤ 2w⁺ ≤ 1/8`. Fix: state the lemma with
  `1/16`, or halve `δ_r`.

## R2.4 Corollary 9.3 (Rankin, `ω_L ≥ 330 log L`) — SOUND

* On supp P: `ν⁺ ≤ (4/3)(8/7)U ≤ 2U`, so `2^{|S|}P_{ν⁺}(G) ≤ 4^{|S|}P_U(G)`.
  On `G_III`, `y_ℓ ≤ m₂ ≤ 1/L` and `Σ_{S(F)}y ≤ r/L ≤ 1/32`. ✓
* `E′m₂ ≤ 2Σ_{ω_L≥r₂}Γ(k)τ(A²)4^{ω_L}/M`, with activity `2Γ(k)/k` times
  `P_U = 1/M_L`. No B is used. ✓
* First factor, after Cauchy–Schwarz twice: `Γ(p) ≤ 3` gives
  `Γ(k)² ≤ 9^{ω(k)}`; `τ(p²)⁴ = 81`. Both mean values are `≍ L^{81}`, giving
  `L^{81/4}·L^{81/4}`. ✓
* Rankin: `16^ω1[ω≥r₂] ≤ 16^ωy^{ω−r₂}` needs `y ≥ 1`, and
  `y = 330/16 ≈ 20.6` qualifies. `Σ_k 1/k ≤ 2log w₂` over w₂-smooth k, and
  `Π(1+16y/(ℓ−1)) ≤ e^{16y(H₁+1)}`. The result is
  `(16e/C₁)^{C₁log L}e^{C₁}`, i.e. `L^{−668.8}` up to a constant, far below
  `L^{−81/2−2}`. ✓ (C₁ = 330 is very generous.) Markov then gives
  `P′(G_III^c) = o(1)`, and `P′(G_L ∩ G_III) ≥ 1/2` keeps TW2 Lemma 3.2's
  constants. ✓

## R2.5 §9.3 (middle range) — labels honest (G2 nit)

Marked OPEN / Assessment in §0, §9.3 and the report. The diagnosis is
coherent: the Poisson mean `≈ (1/4)log L` lies inside the window, and the
diagonal `Π_{ℓ∈S}(ρ_ℓ+1/ℓ) = ρ^S(1+O(rL^{−8}))` holds because
`ℓ^{α−1} ≤ w₂^{α−1}`. The genuine loss is the first moment over `2^r`
short-partner stars.
* **G2 (nits).** (a) The §0 label "sharp failure point" overstates it.
  Nothing shows that the first-moment route *must* fail there; call it
  "identified failure point of this method". (b) Item 1 claims that in
  good fibres `p_ℓ, w_ℓ ≪ L⁴/ℓ` for all ℓ. That cannot come from the Markov
  step as it stands: `Σ_ℓ (ℓ/L⁴)²E′w_ℓ² ≍ Σ_ℓ L^{−2}` diverges. A
  `log ℓ`, `ℓ^{η}` or dyadic-block slack is needed. This is harmless
  inside an Assessment. (c) Item 3 says "labels have height comparable to
  `Q_V^{1/2}`". The actual obstruction is that for short partners the
  long variable cannot be spent: R's class mod q need not have length
  `≥ 2^{s+1}`. Say that instead.

## R2.6 §10: Lemmas 10.1–10.3, Theorem 10.4 (B removed for fixed r) — SOUND (G3 nit)

* **(D)/(H)/(G) split.** If not (D), then `k ≤ M_L²`. If not (H), every
  exponent is `≤ 11`, so `M_L ≤ P^{11r}` and `M ≤ M_L³ ≤ P^{33r}`. So (G)
  satisfies B with `B = 33r−1` (unary: `M ≤ ℓ^{33}`). ✓
* **Lemma 10.1.** Cauchy–Schwarz on each block is correct. Rankin with
  `η = 1/log w₂` and `p^η ≤ e`: at `p = 3` the series
  `ΣC²(1+3e)²(e/3)^e` converges; for larger p the Euler product is
  `(log w₂)^{O(C²)}`. Shiu along k: `A = (km+1)/4` runs over one reduced
  class mod m (`4a ≡ 1`), interval length `y = mK/4 ≥ m³/4`. With `β = 1/4`,
  `m < y^{3/4}` and `x^{1/4} < y` hold; small K forces small m because
  `K ≥ m²`. `F = τ(n²)^{2i}` has `F(p) = 9^i`, giving `(log)^{9^i−1}`. In the
  dyadic sum, `e^{−u/2}u^{c′} ≪ e^{−u/3}` and `e^{−u₀/3} = m^{−2/(3log w₂)}`. ✓
* **Lemma 10.2.** (1) `Σ_m (m/φ(m))^{1/2}m^{−1−η/2} ≪ 1/η = log w₂`. ✓
  (2) `Σ_{ℓ^{12}|M}1/M ≤ 2L·w₂^{−11}`, and `L^{81/2}·L^{−43.5} = L^{−3}`. ✓ The
  heuristic worry that τ(A²) is large for smooth-dominated moduli is
  answered correctly: smooth sparsity `e^{−u}` beats `(u log w₂)^{O(1)}`.
* **Lemma 10.3.** In TW2 the B-hypothesis entered only through (a) Shiu
  along the top prime, (b) small moduli `≤ w₂^{1+B}`, and (c) pointwise τ
  bounds (review D3). Each is replaced:
  * T uses Lemma 10.1 with `m = 1` and `G = Γ2^ω`.
  * `μ_p`: the `k′`-sum gives `p^{−1}` through `2^{ω(k₂′)}/k₂′`, with
    activity depending only on `k₁`. The k-side with `p | k` gets `p^{−1/2}`
    from each Cauchy–Schwarz factor (Rankin at p; Shiu mod p for
    `K ≥ p^{4/3}`). For `k < p^{4/3}` the pointwise τ bound applies, with ε
    now free since B is gone.
  * (G) is verbatim with `B = 33r−1`.
  * (H): first moment `× 3δ_r^{−1}·2r = o(1)`.
  * (D): the AM–GM form `2Σ_k(Γh/k)f_j(k)²` is correct. Cauchy–Schwarz over
    m uses `Σ_{j|m,ω_L≤r}1/m ≤ 2j^{−1}(2log L)^r`. Lemma 10.1 (`i = 2`,
    `G = Γτ_Γ ≤ 3(1+3e)`) gives `(log L)^{O(r)}j^{−2}`, which is summable. ✓
  The medium LLL (TW2 Lemma 3.1), the QR base, and the density cost
  `e^{2T}` do not use B. ✓
* **G3 (nit).** The `μ_p` paragraph is compressed. It does not separate
  `p^e ∥ k` with `e ≥ 2` (bounded trivially by `p^{−2}`), and it does not
  write out the pair weight (activity on `k₁`, weight `2^{ω(k₂)}/k₂`).
  The argument is right; one more displayed line would make it checkable.
* **Theorem 10.4.** Prop 3.1 needs only the per-vertex bounds, which Lemma
  10.3 gives for all types. `min(x+y,1)² ≤ 2min(x,1)² + 2y` holds. The (G)
  part follows by §§5–6 and Cor 5.2. I re-checked that each of these uses B
  only through the class being summed: Lemmas 5.1 and 5.3(b) need
  `q = M/P ≤ P^B` of that class; Cor 5.2(2) needs pointwise τ of that
  class; §6 does not use B at all, since `V_{Q,k}` is a superset. The
  (D,H) part is `≤ 2^{r+1}Σπ_{E_C}` (whole events included through
  `π_∅ = 1`), which is polylog by Lemma 10.2. The unary terms split the
  same way. ✓ The many-prime add-on is subject to G1.

## R2.7 §11 (KARY coordination note) — labels honest

Marked SKETCH / Assessment / "Not done". I checked the citations against
`side-agent/kary-comparison:EXCEPTIONAL_KARY.md`:
* Thm 4.5 is the `S_λ ≪_B λ^{3/4}` claim.
* Lemma 4.2(2) is the first moment `K(W,B)(2(1+B)s)³`, by partial summation
  over `M ≤ e^{2(1+B)s}`.
* Lemma 4.2(3) is the second moment via ETw Lemma 4.0 (pointwise τ).
* "Still not covered" names `log M/log P(M)` unbounded.

All four are accurate. The transfer of Lemma 10.1 and the `λ^{3/4}log λ`
consequence are not verified here and are correctly not claimed.

## Round 2 summary

| item | verdict | defects |
|---|---|---|
| F1–F4 | all FIXED | — |
| Prop 9.1 | SOUND | — |
| Lemma 9.2 | SOUND | G1 minor (state with 1/16) |
| Cor 9.3 | SOUND | (G1 applies) |
| §9.3 | honest Assessment / OPEN | G2 nits |
| Lemmas 10.1–10.3 | SOUND | G3 nit |
| Thm 10.4 | SOUND | (G1 for the many-prime add-on) |
| §11 | honest SKETCH | — |

No major defect. G1 is a hypothesis that is stated but not supplied, and
the proof already covers the supplied constant. Thm 10.4 (no B-hypothesis,
fixed r) and Cor 9.3 stand after G1. The middle window `r ≍ log L`
remains OPEN.

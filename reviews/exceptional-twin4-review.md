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
own code, different sieve algorithms; ~1 min, < 1 GB). `s = 1…5`,
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

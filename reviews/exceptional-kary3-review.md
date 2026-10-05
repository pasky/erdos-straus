# Review R28 of EXCEPTIONAL_KARY3.md (O28) — hostile reviewer

Reviewer branch `side-agent/review-kary3`; author files merged ff from
`side-agent/kary2-loglog` (round 1, complete). Verdict table and defects at the end of
the pass.

## Checks done so far

### ElT (7.10), Thm 7.1, Cor 7.4 (sources/elsholtz-tao-1107.1010.pdf, pp. 25–32)

Verbatim statements match the author's §3 quotes:
* Thm 7.1: `N > 1`, P of degree D with non-negative integer coefficients
  `≤ N^l`, `ρ(p^j) ≤ C` for all p, j ⇒ `Σ_{n≤N}τ(P(n)) ≪_{D,l,C} N Σ_{m≤N}ρ(m)/m`.
  No irreducibility hypothesis. ✓
* Cor 7.4: `a, b ≪ N^{O(1)}` ⇒ `Σ_{n≤N}τ(an+b) ≪ τ((a,b)) N log N`. ✓
* (7.10): `Σ_{a≤A}Σ_{m≤B}ρ_{ka}(m)/m ≪ A log B log(1+k)`,
  `ρ_{ka}(m) = #{b mod m : kab²+1 ≡ 0}`. In the paper it sits inside the
  proof of Prop 1.4 (case A ≤ B), whose header has `k ≪ (AB)^{O(1)}`.

**Uniformity in k (hard check (i)).** I re-derived every step of the proof
(pp. 30–32) and tracked the k-dependence:
1. reduction to odd m: ρ_{ka}(2^j) ≤ 4, absolute. ✓
2. a = 2^l a₀, 2^l absorbed into k: `log(1+2^l k) ≤ log(1+k) + l`,
   weighted by `A/2^l`; summable in l, absolute. ✓
3. `q < A`: character `a ↦ (−ka/q)` on odd a, period 2q. It is principal
   iff q is a perfect square (Jacobi symbol `(·/q)` principal ⇔ q = □).
   ElT's "sums to zero" is false for square q (author's slip is real);
   square q give `≤ A Σ_{q=□} log(B/q)/q = O(A log B)`. Absolute. ✓
4. `A ≤ q ≤ kA`: trivial, `A log B·(log k + 1)`. ✓
5. `q > kA`: second slip (not flagged by the author): ElT's
   `c(q) = (−1)^{(q−1)/2 + m(q²−1)/8}` omits the reciprocity sign
   `(−1)^{((q−1)/2)((k′a−1)/2)}`; harmless, since for fixed a it is still
   8-periodic in q. Mean zero: the function `q ↦ (−ka/q)` (fixed a) is the
   Kronecker character of `−ka < 0`, never principal, so mean zero
   over period `8k′a` holds even when `k′a` is a square. Partial summation:
   `≤ 8k′a · log B/(kA) ≤ 8 log B`, absolute. ✓
6. `Σ_{m≤B, q|m}1/m = (log(B/q) + O(1))/q`, absolute. ✓

Verdict: (7.10) holds for all `A, B ≥ 2`, all `k ≥ 1`, with an absolute
implied constant. The `k ≪ (AB)^{O(1)}` hypothesis is needed only for the
Thm 7.1 / Cor 7.4 step converting τ-sums into ρ-sums. **Author's claim
SOUND.** (Suggest recording the second slip, item 5, for completeness.)

### Lemma 2.1 — SOUND
Re-derived: `log M = Σ_{p^v‖M, p^v≤y} v log p + log S_y(M) ≤ Z_y(M)log y + log S_y(M)`
(Z counts all `p^ν ≤ y` dividing M, including those with `p | S_y`, which
only increases Z). Squarefullness of S_y uses `P(M) ≤ y`. Constants: none.

### Lemma 2.2 — SOUND
`#{ν ∈ ℕ^m : max ν = t} ≤ m t^{m−1}`; `p^{−t} ≤ p^{−1}2^{1−t}`; c_m depends
on m only; Mertens + `γ'(p) ≤ 1 + 2p^{−1/2}`: `C_k(W)` depends on k, W
only, not on y. ✓

### Shiu, Theorem 1 (sources/shiu-1980.pdf, scanned; read pp. 161–163 as images)
Verbatim: f ∈ M (non-negative multiplicative, `f(p^l) ≤ A₁^l`,
`f(n) ≤ A₂(ε)n^ε`), `0 < α, β < 1/2`, `0 < a < k`, `(a,k) = 1`:
`Σ_{x−y<n≤x, n≡a(k)} f(n) ≪ (y/φ(k))(1/log x)exp(Σ_{p≤x, p∤k}f(p)/p)`
uniformly for `k < y^{1−α}`, `x^β < y ≤ x`; constants depend on α, β, f.
(Note `0 < a < k` forces `k ≥ 2`; the author treats q = 1 separately. ✓)

### Lemma 2.3 — SOUND
Re-derived line by line. Shiu data: `x = (2K+1)/4`, `y = K/4`,
`k = q ≤ K^{1/2} < (K/4)^{3/4}`, `f = τ(·²)` (`f(p^a) = 2a+1 ≤ 3^a`,
`f ≤ τ² ≪ n^ε`), residue `4^{−1} mod q` reduced for odd q. ✓
`(q/φ(q))Π_{p|q}e^{−3/p} ≤ 1` for odd q: `(1−x)^{−1} ≤ e^{3x}` on
`[0,1/3]` ✓. D-sizes: `D ≤ y^k ≤ K^{1/16}`, `lcm(D,e) ≤ K^{5/16} ≤ K^{1/2}` ✓.
Euler products: `Σ_e h(e)gcd(D,e)/e = Γ(D)Π_{p∤D}(1+h(p)/p)` exactly ✓;
for `p > W ≥ 16`, `h(p) = 1/(√p − 1)` and `h(p)p^{1/4} ≤ 0.66 < 1` ✓.
The Σ₁ count `≪ K^{3/4}` uses only that y-smooth M with `S_y > K^{1/2}`
have a squarefull divisor `> K^{1/2}` ✓. No hidden u- or y-dependence:
the Shiu constant depends on (α, β, f) = (1/4, 1/4, τ(·²)) only; `C_k(W)`
on k, W only; the y-dependence is entirely in `y ≥ y₀(k,W)` via
`K ≥ K₀(k)`, legitimate since `K ≥ y^{16k}`.

### Cor 2.4 — SOUND (hard check (iv))
Block `(K,2K]`, `K = 2^t ≥ X = y^{64}`: `Σ/K ≤ C₄(log 2K)²u_t^{−4}` and
`(log 2K)² ≤ 4u_t²(log y)²` (as `t ≥ 1`), so a block gives
`≤ 4C₄(log y)⁴(t log 2)^{−2}`; `Σ_{t≥t₀}t^{−2} ≤ 2/t₀`, `t₀ ≥ 64 log y/log 2`.
Total `≤ (C₄/(8 log 2))(log y)³`. The `u^{−4}` vs `u²` balance is right:
per unit of u there are `log y/log 2` blocks, each `≍ (log y)²u^{−2}`;
`∫_{64}^∞ u^{−2}du` converges. ✓ The body uses EK Lemma 4.2′ Steps 2–3
exactly as K2 Lemma 3.2 already did (not re-checked here; same use).

### Lemma 3.1 (Case A) — SOUND (hard check (v))
* Split (i) `r ≥ K^{1/4}`: S-threshold `K^{1/8}` gives
  `Z_y(r) ≥ (1/4 − 1/8)u = u/8`, matching `(8Z/u)^k` ✓. Exceptional
  pairs `≤ Σ_h Σ_{s□>K^{1/8}} 2K/(hs) ≪ K^{1−1/16}log K` ✓.
  Cor 7.4 data: `R' ≥ 2K/(2K^{3/4}K^{1/8}) = K^{1/8}`,
  `a = 4h²L ≤ 16K^{13/8} ≤ R'^{14}` ✓, `b = 1` ✓.
* Split (ii) `r < K^{1/4}`: `h > K^{3/4}`, `S_y(h) ≤ K^{1/4}` ⇒
  `Z_y(h) ≥ u/2` (the author's `4Z/u` is weaker, fine). Thm 7.1 data:
  `N = ⌊2K/(rL)⌋ ≥ K^{1/2}` (`r < K^{1/4}`, `L ≤ K^{1/8}`), coefficients
  `4rL² ≤ 4K^{1/2} ≤ N²` ✓, `ρ_P(p^j) ≤ 2` all p, j: p | 2rL ⇒ P ≡ 1;
  odd `p ∤ rL` ⇒ bijection `n ↦ Ln`, `ρ_P = ρ_{4r} ≤ 2` (Hensel, P′ unit)
  ✓. Constant `≪_{2,2,2}` absolute ✓. (7.10) applied with `k = 4s`
  (s unbounded, up to `K^{1/4}`) — legitimate by the uniformity check
  above; `A = 2R ≥ 2`, `B = 2K` ✓. `Σ_s h(s)log(1+4s)/s < ∞` ✓.
* Note: Prop 1.4 itself would only give a factor `log(1+4sL²)`, and L
  (built from the moment divisor D) is not summable against it; routing
  through Thm 7.1 (which strips L via the bijection `n ↦ Ln`) and then
  (7.10) with `k = 4s` is what makes the bound L-free. ✓

### Cor 3.2, Cor 3.3 — SOUND (pointer-level for the K2 body)
`X = y^{256} = y^{64k}` at k = 4 ✓; tail summation identical to Cor 2.4.
Body = K2 Lemma 3.6 body (ElT Prop 1.4 with k = 4 fixed) — unchanged use.

### Thm 4.1 — SOUND (given K2 Thm 5.1's framework)
Diffed against K2 Thm 5.1's proof (K2 l. 463–509): the only place
`(log λ)^{3/4}` enters is `𝔐(y) ≤ K₃(log y)³(log log y)³` through
`s₁ = λ^{1/4}(log λ)^{−3/4}`. With `𝔐 ≤ K₃′(log y)³` and `s₁ = λ^{1/4}`,
`(E M_{V_i} + 4d_i)/d_i ≤ 16K₃′16^i + 4` ✓ and the ledger sums to
`Cλ^{3/4} + O(log²λ)` ✓. Base (K2 Lemma 2.3) and leak (K2 Lemma 4.3) are
independent of 𝔐 ✓. `y₀(W)` is absorbed into λ₀ ✓.

### Thm 5.1 — SOUND (hard check (ii))
EK Thm 4.1's induction (EK l. 262–288) uses the level only in "given h,
`f = g_{j+1}(h,·)` is λ-level, ≥ 0", and (S_w) for that f. Re-derived for
truncated level: under U the coordinates (base, `n mod ℓ^{E_ℓ}`) are
independent by CRT, so `E_U[1[n≡b (d)] | H_{<j+1}]` is an indicator on
the known coordinates of T = primes of d, times a constant; restricted to
`V_j` it depends on `T ∩ V_j` only. Signs of the `a_i` are irrelevant
(EK Lemma 2.2 needs only `f ≥ 0` and the decomposition `f = Σ_T f_T`).
So 𝓕 is closed and the top block is `d₀`-local with `d₀ = ⌊λ/L₀⌋`
(`|T ∩ V_top|·L₀ ≤ λ`). ✓
* The top block may be arbitrarily wide: EK Thm 2.5 / Cor 2.6 are
  arithmetic-free (no condition on the range of the block), and the
  only arithmetic input is `m̄ = 𝔐(e^Λ) ≥ E[M_top|h]` (K2 §3, Step 1 of
  EK Lemma 4.2′ holds for any block, the bound not using its lower end). ✓
* Jensen over histories: `m ↦ log(C₀(m+4d)/d)` concave ✓, t chosen per
  history before the block ✓.
* Leak: per prime, increasing order ✓ (K2 Lemma 4.3 does not use the
  block shapes).
* Case `L₀ > λ/2`: the linear block `(e^{λ/2}, e^{L₀}]` is a subset of
  K2's `(e^{λ/2}, e^λ]`; I did not re-open ETw Cor 4.3 (pointer-level;
  same use as K2/EK). The top block then has `d₀ = 1` and pays the EK
  price `≈ 2 log(C₀(K₃′Λ³+4))` — weaker than necessary but valid.
* Arithmetic of the displayed bound: `2·[d₀log(C₀(K₃′Λ³+4d₀)/d₀) +
  (4/3)d₀ + ½log(22d₀+22) + 3]` = the displayed terms ✓.

### Cor 5.2 — SOUND
Both term types have truncated level `≤ λ = Λ` with `L₀ = λ/k` ✓;
`k > λ` (L₀ < 1): all primes `> W` in the top block, `d₀ = k` ✓;
`k ≤ Λ³` ⇒ `log((K₃′Λ³+4k)/k) ≪ log Λ ≍_A log log N` ✓. Projection to
the family lcm preserves `ν ≥ 1` on 𝒜 (𝒜 periodic mod the lcm) and Eν,
and shrinks prime sets ✓.

### Cor 5.3 — SOUND (statement and open window)
Prime order of a k-fold intersection `≤ kr` ✓. If `kr > Λ³` the top-block
term is `O(kr)`, so no size condition is needed ✓. Open-window algebra:
`(kL)^{3/4} ≳ L^θ ⇔ k ≳ L^{4θ/3−1}` ✓; window nonempty only for r → ∞ ✓.
Scope warning (moving cutoffs) is correct and important.

### §6 — SOUND as a pointer-level corollary
`(Σλ_S1[∩S])²` expands into single classes (or ∅) with moduli lcm's, level
`≤ 2×` sieve level; `= 1` on avoiders ✓. Valid provided TW4's "level"
dominates the K2 level (log of primes above W) — true for any
product-of-moduli convention. Not re-checked against TW4's text.

### From-scratch numerics (EVIDENCE) — `scripts/review_k3_checks.py`
Run: `PYTHONPATH=scripts uv run --with numpy --with sympy python scripts/review_k3_checks.py {1..6}`
(each < 15 min, < 2 GB, run under `ulimit -v 8000000`).
1. Lemma 2.1 on all y-smooth `M ≤ 10⁹`, y = 7, 13, 31 (5,194 / 27,365 /
   270,648 numbers): 0 violations; `S_y` always squarefull; for smooth M
   the inequality is in fact an equality.
2. Lemma 2.2, exact (exponential formula over primes `≤ y`, W = 16):
   ratio to `(log y)^k` for y = 10…10⁶ decreases monotonically
   (k = 4: 145.6, 54.4, 30.3, 21.6, 17.3, 14.9). Bounded in y ✓.
3. ElT (7.10), A = 60, B = 20,000, k ∈ {1, 4, 9, 12, 100, 3996, 10⁶,
   4·10⁹+4, 10¹⁵+3} (squares and k ≫ (AB)^{O(1)} included): ratio to
   `A log B log(1+k)` ≤ 0.93 and decreasing in k. (Ratio to `A log B`
   alone stays in [0.36, 0.69]: the `log(1+k)` is not even visible here,
   consistent with ElT Remark 1.5.) ✓
4. Shiu step of Lemma 2.3, K = 2²²: `max_{q odd ≤ K^{1/2}} qT(q)/(K log²K)
   = 0.098` (q = 1847), mean 0.073; no growth in q ✓.
5. Σ₂ of Lemma 2.3 (k = 4, Γ with W = 16), K = 2²¹: `Σ₂/(K log²K)` =
   0.11, 0.32, 0.91, 1.52, 1.58 for y = 3, 5, 11, 31, 101 — saturating in y,
   as Lemma 2.2 predicts (y = 101 already violates `D ≤ K^{1/16}`; still
   bounded).
6. Smooth block profile, independent re-implementation, X = 10¹²:
   `S/(log y)³ = 0.264, 0.211, 0.200, 0.192` and `max u⁴b = 0.385, 0.293,
   0.251, 0.248` for y = 7, 13, 23, 31 — **identical** to the author's §7.

## Verdict table

| claim | verdict |
|---|---|
| §1 diagnosis | Assessment, agreed |
| Lemma 2.1 | SOUND |
| Lemma 2.2 | SOUND |
| Lemma 2.3 | SOUND (D4 of self-review correctly applied) |
| Cor 2.4 | SOUND (body: pointer to EK Lemma 4.2′, unchanged use) |
| ElT inputs incl. (7.10) uniform in k | SOUND (two slips in ElT's proof, both harmless) |
| Lemma 3.1 | SOUND |
| Cor 3.2, 3.3 | SOUND (body: pointer to K2 Lemma 3.6 / ElT Prop 1.4, k = 4 fixed) |
| **Thm 4.1** | **SOUND** (given the K2/EK framework already reviewed) |
| Cor 4.2 | SOUND at pointer level (K2 Cor 6.1 not re-opened) |
| §4.3 | pointer-level, as the author says; not checked |
| **Thm 5.1** | **SOUND** |
| Cor 5.2 | SOUND |
| Cor 5.3 + open window | SOUND |
| §6 | SOUND (pointer to TW4 level convention) |
| §7 | EVIDENCE, reproduced exactly |

No FATAL or MAJOR defect found.

## Defects

1. **MINOR — §3 source caveat incomplete.** ElT p. 32, case `q > kA`:
   `c(q) = (−1)^{(q−1)/2 + m(q²−1)/8}` omits the reciprocity sign
   `(−1)^{((q−1)/2)((k′a−1)/2)}`, and "mean zero" for `q ↦ c(q)(q/k′a)`
   needs a justification when `k′a` is a square. Repair: add one sentence
   — for fixed a the corrected factor is still 8-periodic in q, and
   `q ↦ (−ka/q)` is the Kronecker character of the negative number −ka,
   never principal, so the mean-zero/partial-summation step holds with an
   absolute constant, uniformly in k.
2. **MINOR — §3 first paragraph vs Lemma 3.1.** The stated general form
   ("`m ≥ Y`, `S_y(m) ≤ m^{1/2}` ⇒ `Z_y(m) ≥ log Y/(2log y)`") is not the
   form used: Lemma 3.1 uses fixed thresholds (`r ≥ K^{1/4}`,
   `S_y(r) ≤ K^{1/8}` ⇒ `Z ≥ u/8`; `h > K^{3/4}`, `S_y(h) ≤ K^{1/4}` ⇒
   `Z ≥ u/2`). Repair: state "`m ≥ Y`, `S_y(m) ≤ T` ⇒
   `Z_y(m)log y ≥ log(Y/T)`" and cite it in (i), (ii).
3. **MINOR — Lemma 3.1(ii) wording.** "`h > K^{3/4}/2`" should be
   "`h > K^{3/4}`" (from `rh > K`, `r < K^{1/4}`); the factor `(4/u)^k`
   could be `(2/u)^k`. Cosmetic.
4. **MINOR — Thm 5.1, case `L₀ > λ/2`.** The top block then has `d₀ = 1`
   and could be treated by the linear-block bound; the EK price
   `2log(C₀(K₃′Λ³+4))` is valid but needlessly large. Also say explicitly
   that ETw Cor 4.3 applies to the sub-block `(e^{λ/2}, e^{L₀}]` (pointer).
5. **MINOR — pointer-level dependencies to be listed in the status line.**
   Thm 4.1's PROVED label rests on K2 Thm 5.1's framework (base, leak,
   EK Thm 4.1/Cor 2.6, ETw Prop 4.1/Cor 4.3) and on the bodies of EK
   Lemma 4.2′ and K2 Lemma 3.6, none re-proved here. Correct as labelled
   ("same proviso"), but the DISCOVERIES entry should say "PROVED given
   K2/EK as reviewed".

## Answers to the brief's hardest checks
(i) ET (7.10) uniform in k as used: **yes**, absolute constant, all
`A, B ≥ 2`, `k ≥ 1` (proof re-derived; numerics item 3).
(ii) EK Thm 4.1 for the truncated class with one wide top block: **yes**.
(iii) Lemma 2.1/2.3 constants: no hidden u- or y-dependence; Shiu's
hypotheses (k ≥ 2 reduced residue, `k < y^{1−α}`, `x^β < y ≤ x`,
`f ∈ M`) all verified against the scanned paper.
(iv) `u^{−4}` vs `u²`: correct, tail `≤ (C₄/(8log 2))(log y)³`.
(v) Case-A split `r ≷ K^{1/4}`: both halves correct; Thm 7.1's
bijection `n ↦ Ln` is what removes the moment modulus.

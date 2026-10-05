# Review R28 of EXCEPTIONAL_KARY3.md (O28) — hostile reviewer

Reviewer branch `side-agent/review-kary3`; author files merged ff from
`side-agent/kary2-loglog`. Work in progress; verdict table at the end of
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
* Note: if one tried Prop 1.4 instead of (7.10) here, `k = 4s ≤ 4K^{1/4}`
  would also be `≪ (AB)^{O(1)}` — but Prop 1.4 is for `τ(kab²+1)`
  summed over a *box* in b, whereas here b = Lh′ runs over a progression;
  routing through Thm 7.1 + (7.10) is the correct way. ✓

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

# POINTWISE_MORDELL17C — explicit P-count at prime powers, r = 17 (task O98)

Status: O98 (branch `side-agent/r17-explicit-et`), in progress. Builds on POINTWISE_MORDELL17.md (= M17) and
POINTWISE_MORDELL17B.md (= M17B; Theorem 4.1, hypotheses (H_P), (H_Q)). Labels as in DISCOVERIES.md.
`N = 17^K`, `F = 17^k`, K, k odd.

## 1. The hypotheses only need to hold on average over K (PROVED)

**Lemma 1.1 (cumulative form of (H_P), (H_Q)).** Put `S_P(K) = Σ_{13 ≤ K' ≤ K, K' odd} D_P(K')` and
`S_Q(k) = Σ_{9 ≤ k' ≤ k, k' odd} D_Q(k')`. In M17B Theorem 4.1, (H_P) may be replaced by
`(H_P^cum)  S_P(K) ≤ C·17^{θK}` for all odd `K ≥ 13` (θ < 1/2), and then `T_P ≤ 2·(16/17)·C·Σ_{K≥13 odd} 17^{θK+(1−K)/2}`.
Likewise (H_Q) may be replaced by `S_Q(k) ≤ 17^{3k/5}` (k ≥ 9), with `T_Q` multiplied by `1 − 17^{−2}`.
*Proof.* With `w_K = 17^{(1−K)/2}` (decreasing, `w_K − w_{K+2} = (16/17) w_K`), Abel summation gives for every odd `K₁`
`Σ_{K=13}^{K₁} w_K D_P(K) = w_{K₁} S_P(K₁) + Σ_{K=13}^{K₁−2} (w_K − w_{K+2}) S_P(K)`. Under (H_P^cum) the boundary term is
`≤ C·17^{1/2}·17^{(θ−1/2)K₁} → 0`, and all terms are ≥ 0; let `K₁ → ∞`. Use `NB_P ≤ 2D_P` (M17B Lemma 1.1). Same for Q
with `w_k = 17^{1−k}`, `w_k − w_{k+2} = (1 − 17^{−2}) w_k`. ∎

Since `S_P(K) ≥ D_P(K)`, (H_P) ⇒ (H_P^cum) with the same C, so the cumulative form is strictly weaker, and the
admissible constant grows by the factor 17/16 (`scripts/m17c_tail_cum.py`, floor-rounded; the pointwise column
reproduces M17B §4):

| θ | 0.25 | 0.30 | 0.35 | **0.40** | 0.42 | 0.45 |
|---|---|---|---|---|---|---|
| C*, pointwise (H_P), K ≥ 13, base ρ₁ (= M17B) | 619.2 | 87.88 | 11.76 | 1.409 | 0.5686 | 0.1275 |
| C*, cumulative (H_P^cum), K ≥ 13, base ρ₁ | 657.9 | 93.38 | 12.50 | **1.497** | 0.6042 | 0.1354 |
| C*, cumulative, K ≥ 15, base ρ₂ | 2712 | 290.0 | 29.25 | **2.639** | 0.9507 | 0.1798 |

(T_Q kept at the un-weakened `1.4106·10⁻³`, a safe over-estimate.) Data check: `S_P(13) = 1463 ≤ 1.497·17^{5.2}`.
The point of Lemma 1.1 is less the constant than the *shape*: a bound for `Σ_{K' ≤ K} D_P(K')` may be attacked by
averaging over the exponent `K'`, which a pointwise bound cannot (see §3).

## 2. Q side: a free regime (PROVED; brute-checked)

Q-data of level k are the N-points of `Σ^I_F` (`4abcd = F(a+b)+c`, `e = (a+b)/c`, `f = 4acd−F`, `ef = 4a²d+1`) with
`a ≤ b`, `17∤e` (M17 Lemma 2.1, §3); `D_Q(k)` counts them.

**Lemma 2.1.** For every N-point of `Σ^I_F`: (i) `4abd = eF + 1`; (ii) `f·b = aF + c`; (iii) `f·(4bcd−F) = F² + 4c²d`;
(iv) a fixed pair `(a,d)` carries at most 2 points.
*Proof.* (i) `eF+1 = e(4acd−f)+1 = 4acde − 4a²d = 4ad(ce−a) = 4abd`. (ii) `fb = 4abcd − Fb = Fa + c`. (iii) expand:
`16abc²d² − 4cdF(a+b) + F² = 4cd·c + F²`. (iv) c is determined by f (`4acd = f+F`), and `f | t := 4a²d+1`,
`f ≡ −F (mod s)`, `s = 4ad`, `gcd(f,s) | gcd(t,s) = 1`, and `s² = 16a²d² > t`. A divisor `f ≤ √t < s` is the least
positive residue of its class; a divisor `f > √t` has cofactor `t/f < √t < s` in the fixed class `t·(−F)^{−1} mod s`.
So at most one of each kind. ∎
`scripts/m17c_qcheck.py F` checks (i)–(iv) by brute force over all N-points (no `17∤e` filter): F = 17, 4913, 1001,
9999 give 2, 73 (= `D_Q(3)`), 10, 179 points, at most 1, 1, 1, 2 per pair.

**Corollary 2.2 (large-c part of D_Q is unconditional).** Since `F/4 < acd ≤ 3F/4`,
`#{Q-points of level k with c ≥ c₀} ≤ 2·#{(a,d): ad ≤ 3F/(4c₀)} ≤ 2Y(1 + ln Y)`, `Y = 3F/(4c₀)`.
E.g. `c₀ = F^{1/2}` gives `≤ 1.5·F^{1/2}(1 + ln F)`, whose contribution to `T_Q` is
`≤ 2Σ_{k≥9 odd} 17^{1−k}·1.5·17^{k/2}(1 + k ln 17) = 4.23·10⁻³ < 4.3·10⁻³`. Hence (H_Q) is only needed for the
points with `c < F^{1/2}`, at the price of `4.3·10⁻³` in the budget. *Proof.* Lemma 2.1(iv); `#{ad ≤ Y} ≤ Σ_{a≤Y} Y/a
≤ Y(1+ln Y)`; the sum is evaluated directly to k = 399 (later terms total < 10⁻²⁰⁰); command in Replay. ∎
This is only a partial reduction: the small-c Q-points (e.g. `c = 1`, `a ≈ d ≈ F^{1/2}`) need divisors-in-residue-classes bounds:
there `(a,c)` fixed gives `f | aF + c`, `f ≡ −F (mod 4ac)`, with modulus `4ac ≈ F^{1/2} = (aF+c)^{1/3}`, exactly Lenstra's
threshold.

**Assessment 2.3 (a route to an unconditional (H_Q); not carried out).** In log_F-coordinates `(α,γ,δ)` of `(a,c,d)`
(`α+γ+δ ≈ 1`), the regimes `(a,d)` [Lemma 2.1(iv), ≤ 2, cost `1−γ`], `(a,c)` [`f | aF+c`, mod `4ac`; Lenstra (≤ 11)
if `2α+3γ > 1`, exponent-1/4 bound if `3α+4γ > 1`; cost `α+γ`] and `(c,d)` [`f | F²+4c²d`, mod `4cd`; Lenstra if
`γ+δ > 2/3`, exponent-1/4 bound if `γ+δ > 1/2`; cost `γ+δ`], plus Nicolas–Robin τ-bounds for `τ(F²+4c²d)` when `cd`
is tiny, appear to cover the whole simplex with every cost `< 1`. Lenstra alone leaves the region `γ ≈ 0`,
`1/3 < α < 1/2` (e.g. `(0.4, 0, 0.6)`), so an explicit Lenstra/Coppersmith–Howgrave-Graham–Nagaraj constant
above exponent 1/4 is required. Q has margin 2/5 (needs only `θ_Q < 1`), so an explicit, `log`-lossy bound would
suffice for large k. A finite range of k would remain to be checked.

For P the analogous free regime does not exist: with `(a,d)` fixed, `f | N + 4a²d`, `f ≡ −1 (mod 4ad)`, and
`(4ad)² > N + 4a²d` needs `ad ≳ N^{1/2}/4`; with `(c,d)` fixed, `f | 4c²dN+1` needs `d ≳ N/4`. Neither regime is
sublinear in N.

## 3. P side: why an explicit ET-type count cannot reach M17B's constants (Assessment)

Recall (M17B Lemma 2.1) a P-point is `(a,c,d,e)` with `4abd = N+e`, `ce = a+b`, `a ≤ b`, hence
`(N+e)/4 ≤ acde ≤ (N+e)/2` (from `ce/2 ≤ b ≤ ce`).
* *Symmetric point (PROVED, exponent bookkeeping).* At `a ≍ c ≍ d ≍ e ≍ N^{1/4}` each of the six two-variable
  regimes (fix two of `a,c,d,e`, find the rest by a divisor-in-residue-class problem) ranges over `≍ N^{1/2}` parameter
  pairs. A bound that charges ≥ 1 per parameter pair (Lenstra, CHN, or the "≤ 2" trick of Lemma 2.1(iv)) therefore costs
  `≥ N^{1/2−o(1)}`, beyond any admissible θ < 1/2. A one-variable regime (`e` fixed, count factorisations of `(N+e)/4`,
  i.e. `τ_3`) is unavoidable, as in ET.
* *The θ = 0.4 row is out of reach of ET-type covers (Assessment).* ET's balance `X_e² X_ad X_ac X_cd ≥ N²` with
  `X_ad, X_ac, X_cd ≤ N^{0.4}` forces `X_e ≥ N^{0.4}`. The pair regime alone, charged ≥ 1 per pair, costs
  `#{ad ≤ X} ≥ X ln X − X`, i.e. more than `1.497·N^{0.4}` (cumulative C*, §1) as soon as `ln N^{0.4} > 2.5`. Any proved
  bound for the `e`-regime is of the form `Σ_{e ≤ X_e} τ_3`-type, of size `≫ X_e (ln N)²`. So the θ = 0.4 constant cannot
  be met at any K. Only θ close to 1/2 leaves room, with `C* ≤ 0.1354` at θ = 0.45. That requires
  `N^{0.05} ≫ (ln N)^{O(1)}`, i.e. K in the hundreds at least, and the range below it would need exact data.
* *Pointwise τ-bounds.* Nicolas–Robin `τ(n) ≤ n^{1.5379 ln 2/ln ln n}` gives exponent `≈ 1.07/ln ln n`, which is still
  `≈ 0.19` at `n ≈ 17^{100}`. Squared for `τ_3`, it is far above the margin `1/2 − θ`. This is the M17B §5
  bottleneck, unchanged.

Net: §1 weakens (H_P) to an averaged statement, which an attack via averaging over K could use. But averaging over
`K' ≤ K` of `τ_3(17^{K'}+e)` has no known explicit treatment either. Divisors `q ≤ X` of `17^{K'}+e` average fine, but
the large complementary divisors do not. **(H_P) remains CONDITIONAL; no unconditional sterile point.**

## Replay

```
W=<worktree>
python3 $W/scripts/m17c_tail_cum.py 13 9 16344335 24137569     # §1 table, rows 1–2 (row 1 = M17B §4)
python3 $W/scripts/m17c_tail_cum.py 15 9 961421 1419857        # §1 table, row 3
for F in 17 4913 1001 9999; do python3 $W/scripts/m17c_qcheck.py $F; done   # Lemma 2.1 (9999: ~1 min)
python3 -c "import math;print(sum(3*17**(1-k/2)*(1+k*math.log(17)) for k in range(9,401,2)))"  # Cor 2.2: 4.2254e-3
```

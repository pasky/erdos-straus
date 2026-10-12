# Brainstorm memo: are there hardness drivers beyond "local data + shifted divisors"? (O154(b))

Labels as in DISCOVERIES.md. ES is not solved, and nothing here proves any case of it. The numbers are
**EVIDENCE** (exact `f_II` from the 10⁸ dump); the readings are an **Assessment**.

## 1. Idea

The question is whether some feature of p predicts a small `f_II(p)` and is **neither**
* congruence data (`p mod q` for small q: square classes, `p ≡ 1 (mod q)`, the 2-adic valuation, Euler products
  of `χ_p`, which is B1), **nor**
* divisor data of specific shifted integers (`(p+e)/4`, `cp + a`, `p − 1`, which is the lottery of B2).

A genuinely global driver would be a signal worth chasing. Examples: the class number `h(−4p)`, the continued
fraction or regulator of `√p`, or the analytic tail of `L(1, χ)` beyond any fixed set of primes. A truly
non-congruence positive or negative force is exactly what the H-A/H-E escape hatches ask for.

## 2. Literature anchor

* Class-number formula and the fast series for `h(D)`: Cohen, *A Course in Computational Algebraic Number Theory*,
  §5.3 (from memory). The implementation in `scripts/bs_adv_global.c` is checked against brute-force
  reduced-form counting for all 1125 primes `p ≡ 1 (4)`, `p < 2·10⁴`, with 0 mismatches.
* O142 (`prob_lottery_model.md` §3.6): there, `log τ(p−1)` correlates −0.40 / −0.33, and the truncated
  `L(1, χ_p)` was "weak". Both readings are revisited below.

## 3. Structural remark (PROVED, elementary; known in disguise as the {a,c} row of the slice table)

Fix a and c. Then `f = 4acd − 1` divides `p + 4a²d` iff it divides `cp + a`. The proof is the identity
`cp + a = c(p + 4a²d) − a·f`, together with `gcd(c, f) = 1`. Moreover `cp + a = b·f` *is* the Type II cofactor.

So the Type II solutions with given (a,c) are exactly the factorisations `cp + a = b·f` with `f ≡ −1 (mod 4ac)`.
For these, `c | a + b` holds automatically, and `e = (a+b)/c`.

In this language the "dead modulus" driver of O142 is the signed slice `(a,c) = (−1,1)`:
* `f | p − 1` gives `f | cp + a ⟺ f | a + c`, which is impossible once `f > a + c`;
* the alive analogues are `p + 1, 2p + 1, p + 2, …`.

## 4. Experiment (`scripts/bs_adv_drivers.py`, `scripts/bs_adv_global.c`; log `logs/bs_adv_drivers.txt`)

The sample is 20 000 random primes `p ≡ 1 (mod 24)` in `[5·10⁷, 10⁸]`. The response is `y = log(f_II/L³)`, with
`Var y = 0.036`.
* Cell means of y mod 120120 explain R² = 0.347.
* Baseline: cells, plus `log τ(p−1)`, plus `log Σ_{e≤16} τ((p+e)/4)`. This gives R² = 0.433.

| feature | corr with y | partial corr beyond baseline | type |
|---|---|---|---|
| `log τ(p−1)` | −0.31 | (in baseline; coefficient ≈ 0 once cells are in) | mostly congruence |
| `log τ(p−1)`, 100-smooth part | −0.26 | −0.060 | congruence (growing moduli) |
| `v₂(p−1)` | −0.09 | −0.064 | congruence mod 2^k |
| truncated `log L(1, χ_p)` (q ≤ 2·10⁴) | −0.49 | **−0.140** | congruence (square class at 17 ≤ q ≤ 2·10⁴) |
| `log n_p` (least non-residue) | −0.44 | −0.042 | congruence |
| `log τ(2p+1)` | +0.20 | +0.076 | shifted divisor ((a,c) = (1,2) slice) |
| `log τ(p+2)`, `log τ(p+1)` | +0.13, +0.04 | +0.041, +0.008 | shifted divisor |
| `log L(1, χ_{−4p})` **exact** (h(−4p)) | 0.00 | +0.059 | (equal to its truncation, see next row) |
| tail: exact − truncated `log L(1,χ_{−4p})` | +0.016 | +0.004 | **global** |
| CF period of `√p` / `√p` | −0.17 | −0.043 → **−0.009** after stage 2 | **global** |
| `log ε` of `ℤ[√p]` / `√p` | −0.17 | −0.044 → **−0.010** after stage 2 | **global** |

* **Stage 2.** Add every local and shift feature above (10 regressors). This gives R² = 0.458. The global
  invariants then have partial correlations +0.003, −0.009 and −0.010, against a null standard error of 0.007.
* **Stage 3.** Add 27 crude shifted-divisor features: `τ((p+e)/4)` for e ≤ 63, and `τ(cp + a)` for a, c ≤ 4.
  This gives R² = 0.555. The residual variance is then 0.0160, while the compound-Poisson noise floor of O142 (§3.2:
  κ = 3.06, so `Var log f ≈ κ/f`) is ≈ 0.0115. The global invariants stay at |partial corr| ≤ 0.008.

Readings (Assessment):
1. The raw −0.17 correlation of the regulator and CF period with y is inherited from `L(1, χ_p)`, since
   `h⁺R ≍ √p L(1, χ_p)`. That is a square-class effect at moderate primes. Once `L(1, χ_p)` is in the baseline, the
   global part vanishes.
2. The largest effect beyond O142's baseline is the square class at primes 17…2·10⁴ (−0.14). The effect has the
   expected sign: residues at more primes make f smaller. It is **congruence-type** (B1), but at moduli growing
   with the truncation point. It is the same mechanism as square-mimicking.
   * *Correction to O142 §3.6.* O142 reported that the truncated `log L(1, χ_p)` correlates weakly and
     *positively* with f (+0.13 for f_II, within mod-24 cells). That is a Simpson's-paradox aggregate.
   * Re-running O142's code on primes in `[2²⁰, 3·10⁷]` (Y = 300, `scripts/bs_adv_simpson.py`, logic copied from
     `bs_prob_typecorr.py`) gives these within-cell correlations:

     | | value |
     |---|---|
     | pooled | +0.133 |
     | p ≡ 1 (24) | **−0.51** |
     | p ≡ 13 | −0.19 |
     | p ≡ 17 | −0.13 |
     | p ≡ 5 | −0.04 |
     | p ≡ 3 (mod 4) classes | +0.16 … +0.43 |

   * For `p ≡ 3 (mod 4)` the relevant genus character is not `(·/p)`, so the sign flips. In the hard class the
     naive sign holds, and strongly.
3. The `p − 1` driver is mostly congruence. Inside mod-120120 cells, `log τ(p−1)` has coefficient ≈ 0. What
   survives is the smooth part and `v₂` (−0.06 each), which is still congruence data at prime powers.
4. Everything else that is visible is shifted-divisor data (the lottery itself). After a crude linear model in
   these features, about 70% of the remaining variance is at the Poisson floor. The rest is plausibly the
   nonlinear residue structure of the divisors, which `τ` does not see.

## 5. Barrier screen

* **B1.** Every driver with |partial corr| > 0.02 is either a function of `p mod q` (B1, with q growing) or a
  divisor count of a shifted integer.
* **B2.** The shifted-divisor drivers are the per-slice lottery. Their {a,c}-slice form (§3) is one of the known
  encodings.
* **B5.** At odd squares the square-class factor is extreme. Every `L(1, χ_{m²})` head is maximal, and
  f_I = f_II = 0. So the strongest local driver extrapolates in the right direction to the T1 points. No feature
  found here distinguishes primes from squares except through the genus/square class.
* **B6.** These are correlations across p. At a single p they only describe the quenched mean.

## 6. Viability Assessment

**COLLAPSES** to B1 + B2. No global (non-local, non-divisor) driver is detectable: the class-number tail, the CF
period and the regulator all show |partial corr| ≤ 0.01 at n = 20 000. This is a clean negative. Within reach,
the hardness of a prime is fully explained by local data plus the divisor lottery of shifted integers plus Poisson
noise.

By-products (EVIDENCE): the revised ranking of drivers (§4 table), with the square class at moderate primes
largest; the {a,c}-slice reading of the `p − 1` driver as the signed slice (§3).

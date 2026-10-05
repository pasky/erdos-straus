# Hostile review of POINTWISE_OMEGA8.md (O30), reviewer 1 (R30a)

Reviewer branch `side-agent/review-omega8a-2`, reviewing
`side-agent/haar-primes-2` as merged at the start of this review.
Focus: the new machinery (Lemmas 3.1–3.3, Lemma 4.1, Thm 3.4, Thms
4.3/4.4 bookkeeping). From-scratch scripts: `scripts/review_o8a_*.py`,
output in `data/review_o8a/`.

## Verdict per claim (in progress)

| Claim | Verdict |
|---|---|
| Lemma 3.1 (BRW sandwich, error identity, `m²` bound) | SOUND |
| Lemma 3.2 (cell size, `M_1`) | SOUND |

## Claim-by-claim notes

### Lemma 3.1 — SOUND

Re-derived. `1−F=Σ_iA_iF_{<i}` (first occurring event). If `F_{<i}=1`
then `A_j=0` for all `j<i`, so `v_i=0` and the i-th summand of `F−B` is
`A_i−A_i=0`; if `F_{<i}=0` then `f_{<i}=1` and
`A_i(1−v_i)²=A_i(f_{<i}−v_i)²`. Hence `F−B=Σ_iA_i(f_{<i}−v_i)²≥0` with
`f_{<i}−v_i=Σ_{j<i}A_j(F_{<j}−u_j)`, Cauchy–Schwarz with at most m terms
gives the `m²` bound. Nothing about `u_j` is used (any real functions).
The step `E[A_je_j²]=P(E_j)·energy(F^{(j)};t)` needs (i) single-value
events (so that `F_{<j}=F^{(j)}` on `E_j`) and (ii) `u_j` a function of
the coordinates outside `supp E_j` (so it is independent of `A_j`); both
hold in Setting 3.0.

Check (`scripts/review_o8a_brw.py 60 7`, `data/review_o8a/brw.txt`):
random single-value systems on `∏ℤ/q_ℓ`, `q_ℓ∈{2,3,4}`, N≤5, m≤8,
random t. `u_j` computed as the least-squares projection onto all cell
indicators on ≤t coordinates (no formula). Over 60 trials:
`max(B−F)=0`, identity error `9·10^{−16}`,
`|E[A_je_j²]−P(E_j)energy_j| ≤ 3·10^{−17}`, and the `m²` bound holds in
all trials.

### Lemma 3.2 — SOUND

The `c_W` formula is the Möbius-inverted ES truncation;
`c_W=Σ_{i≤t−|W|}(−1)^i binom(N'−|W|,i)=(−1)^{t−|W|}binom(N'−|W|−1,t−|W|)`,
so `|c_W|≤(N+1)^t` (N' = number of non-pinned coordinates). The script
checks the formula against the least-squares projection (max deviation
`1.4·10^{−14}`), and `|c_W|≤(N+1)^t`, `M_1(u)≤(N+1)^{2t}` in every trial.
`P(C∩D)≤P(C)P(D)∏_{ℓ∈I∩J}φ(ℓ^{e_ℓ})` is exact for consistent cells
(`P(C∩D)=P(C)P(D)/P(C|_{I∩J})`), so `M_1(fg)≤M_1(f)M_1(g)T^{|I∩J|}`;
over a 5-fold product the exponents add to at most `3k+2t`, comfortably
inside the stated `8(3k+2t)𝓛`. Terms: `1−ΣA_i+2ΣA_iA_ju_j−ΣA_iA_jA_{j'}u_ju_{j'}`,
`≤m³+m²+m+1` of them with coefficients ≤2, so `+3` absorbs `log 2`
and the count. Cell products of unit cells are unit cells (or empty),
so `gcd(b_i,d_i)=1` is preserved.

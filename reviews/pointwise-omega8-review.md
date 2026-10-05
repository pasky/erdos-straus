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

### Lemma 4.1 — SOUND (minor presentation points D3, D4 below)

* **Switching lemma quote.** Checked against O'Donnell, *Analysis of
  Boolean Functions* (arXiv:2105.10386 edition, §4.4, p. 100): "Let f be
  computable by a DNF or CNF of width at most w and let (J|z) be a
  δ-random restriction. Then for any k, `Pr[DT(f_{J|z}) ≥ k] ≤ (5δw)^k`."
  So `C_H=5` and the form `Pr[DT≥s]≤(C_Hpw)^s` are quoted correctly; no
  dependence on size or n. Lovett's notes (Lemma 3.3/Cor 3.4) were not
  accessed; O'Donnell's own LMN step (Lemma 4.21) is the variant
  "3ε-concentrated up to degree 3k/δ" via Chernoff. The author's variant
  (2ε up to degree k/δ via the binomial median) is a different but valid
  derivation, re-derived and checked below; it does not rely on Lovett.
* **(a) width.** Fibres of `u↦⌊q·int(u)/2^b⌋` are integer intervals of
  size `⌊2^b/q⌋` or `⌈2^b/q⌉`; an interval in `[0,2^b)` is a disjoint
  union of `≤2b` dyadic subcubes, each a term of width `≤b`. A vertex
  condition `X_ℓ∈V` is an OR of such terms; an event is an AND over `≤k`
  coordinates; distributing gives terms of width `≤kb`. Restricting to
  pinned coordinates only deletes literals/terms. Width `≤kb` is correct
  regardless of |V| (|V| only increases the number of terms).
* **(b) LMN step.** `E_ρ[f̂_ρ(S)²]` summed gives
  `Σ_UPr[|U∩J|≥k_0]f̂(U)²` (O'Donnell Prop 4.17 / Cor 3.22 type identity,
  valid for real f); `DT<k_0 ⇒ deg<k_0`; `W^{≥k_0}[f_ρ]≤E f_ρ²≤1` for
  0/1 f; for `|U|≥k_0/p`, `⌊|U|p⌋≥k_0` and the binomial median is
  `⌊np⌋` or `⌈np⌉` (Kaas–Buhrman), so `Pr[Bin≥k_0]≥1/2`. Tail
  `≤2·2^{−k_0}` beyond degree `d=k_0/p=2C_Hwk_0`. Complementing
  (`φ̃=1−(1−φ̃)`) preserves all non-constant weights.
* **(c) pull-back.** `E[χ_S|π(U)]` factorises over blocks (π blockwise,
  blocks independent) and is constant (=0 or 1-dependent only on the
  block's x) on untouched blocks, so g is a sum of functions of `<d`
  coordinates. Jensen: `φ−g=E[φ̃−g̃|π]`. The junta class is measure
  independent, so `energy_Haar(φ;d) ≤ E_Haar(φ−g)² ≤ ρ·E_{π*}(φ−g)²` with
  `ρ=max dHaar/dπ_* ≤ ∏(1−q_ℓ2^{−b})^{−1}`; with `2^b≥4NT`, `q_ℓ≤T`,
  N' ≤ N factors each `≤(1−1/(4N))^{−1}`, so `ρ≤e^{1/3}<e^{1/2}`.
  Final: `e^{1/2}·2^{1−k_0}<4·2^{−k_0}`. ✓

Checks (`scripts/review_o8a_lmn.py`, `data/review_o8a/lmn.txt`):
(a) all `b≤10`, all `q≤2^b`: fibres are intervals with floor/ceil sizes,
dyadic covers use `≤b≤2b` cubes, 0 violations. (b) Exact enumeration over
all p-random restrictions of 36 toy DNFs (n=7, w∈{2,3}, p∈{.05,.1,.2}):
restriction identity to `6·10^{−16}`; `Pr[DT(f_ρ)≥s]≤(5pw)^s` never
violated. (c) `Pr[Bin(n,p)≥k_0]≥1/2` for `np≥k_0`, `p=1/(10w)`, 48000
cases, 0 violations. (d) Full chain on toy good-indicators
(`q=(3,5),(3,5,7),(7,5)`, b=4,5, every cut-off d): `E(φ̃−g̃)²=W^{≥d}`,
`E_{π*}(φ−g)²≤W^{≥d}`, g has ES-junta `<d` (projection residual
`≤5·10^{−15}`), `energy_Haar(φ;d−1)≤E_Haar(φ−g)²≤ρ·E_{π*}(φ−g)²`. All ✓.

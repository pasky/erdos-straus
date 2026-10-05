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

### Toy end-to-end logic check (B ≤ F ≤ 1[W>T] on n≡1 mod Q_Π)

`scripts/review_o8a_pipeline.py` (`data/review_o8a/pipeline.txt`) builds
the real ES atom system (Π = {ℓ≤z}, events `n≡−4D mod r_Π(M)` for atoms
surviving Π), takes **arbitrary random** `u_j` on 1–2 free coordinates,
samples `n≡1 (mod Q_Π)` coprime to the free primes (10% of them prime),
and computes `W(n)>T` by brute force from the definition. T=120, z=7
(121 events, 20000 samples, 450 with F=1) and T=250, z=11 (334 events,
5000 samples, 30 with F=1): (I) `F=1⇒W>T` and `B(n)≤F(n)≤1[W(n)>T]`
never violated; `B(n)>0` exactly on `F=1`; the expanded (cell-type)
form `1−ΣA_i+2ΣA_iA_ju_j−ΣA_iA_jA_{j'}u_ju_{j'}` equals the closed form.
This confirms the logic only (not the asymptotics); `F=1⟺W>T` held in
every sample, as expected (the converse of (I) also holds).

### Lemma 3.3 (twist) — SOUND (minor D2)

Re-derived. Since `B≤F`, `E|B−F|=E[F−B]≤EF/100`. For ψ real primitive
with `f|d_i` for some i and `gcd(f,Q)=1` (odd squarefree f, all its
primes free coordinates), `μ_ψ=E[Bψ]` for **any** cell representation
(a cell with `f∤d_i` has `E[1_cψ]=0` because ψ is primitive). Write
`F=F'·1[X_{ℓ_0}∉Forb(X_{−ℓ_0})]`; ψ's ℓ_0-factor (Legendre symbol mod
ℓ_0) has mean 0 over units mod `ℓ_0^{e}`, so
`|E[Fψ]|≤E[F'·P(Forb|X_{−ℓ_0})]≤Σ_{E∋ℓ_0}p_{ℓ_0}(E)P(E∖ℓ_0∩F')`.
HSS conditional LLL for the F'-family (`x=2P`, LLL condition holds since
neighbourhood sums `≤2k/(64k)`): `P(E∖ℓ_0|F')≤P(E∖ℓ_0)∏_{Γ}(1−x)^{−1}≤e^{1/31}P(E∖ℓ_0)`.
So `|E[Fψ]|≤1.033w_{ℓ_0}EF'≤0.0162EF'`, `EF≥0.983EF'`, and
`|μ_ψ|≤(0.01+0.0165)EF≤0.027μ/0.99<μ/4`. Only `w_{ℓ_0}≤1/64` and the
neighbourhood bound are used. Note F is defined over the **split**
family; splitting leaves `w_ℓ` unchanged, and split events at one prime
are mutually exclusive (dependent, but included in the neighbourhood
sum via `w_ℓ`).

### Theorem 3.4 — SOUND (minor D1, D5)

* (I) for the iterated-quarantine Π: re-derived. O2 Lemma 4.3 (I)'s proof
  uses only that every prime `≤T` is in Π or free, `ℓ^{e_ℓ}≤T`, `24|Q`,
  and M odd; it is valid for any Π ⊇ {2,3}. Vertex values `−4D` are
  units mod ℓ (`gcd(A_M,M)=1`). Toy check above.
* LLL: `x_E=2P(E)`, neighbourhood sums `≤2kc_0=1/32` ⇒
  `δ≥∏(1−2P(E))≥e^{−2.07S}≥e^{−2.2S}` ✓.
* EL ⇒ `E[F−B]≤m²·S·e^{−3S}/(100m²(S+1))<e^{−3S}/100≤δ/100` ✓.
* Counts: atoms `≤T·τ*(A²)≤T²`; splitting at `≤k` primes multiplies by
  `≤∏ℓ^{e_ℓ}≤T^k`; `m≤T^{k+2}` ✓.
* `K=1+log(M_1/μ) ≤ 1+log M_1+2.2S+0.01`, with Lemma 3.2 and `N≤T`:
  `K≤4S*+C'(k+t)𝓛` ✓ (`S=S_tot(Π)≤S*` by O2 Lemma 11.1's max over Π).
* PO Thm 4.1 hypotheses: unit cells, moduli coprime to `Q_Πℓ_0`
  (free primes ∉Π, `ℓ_0>T`), `B(n)≤1[W(n)>T]` (for primes `p≡1 (Q)`,
  which are `>T` and hence units at all free primes; that is all the
  proof of PO Thm 4.1 evaluates), `μ>0`, twist (Lemma 3.3). Number of
  cells is irrelevant (TZ's error is uniform in q). `x≥q_i^{12}` follows
  from `log x≥C_1K log Z` ✓.
* `log Z ≤ log Q_Π+log(2R)+log max d ≤ log Q_Π+2(3k+2t)𝓛+1`, which is
  up to a factor 2 the stated `(3k+2t+2)𝓛` (absorbed in C; D5).

### Theorem 4.3 — SOUND (modulo TZ, ET Prop 1.4, and the inherited O2 Lemma 11.1 ET-form)

Bookkeeping redone: `log m≤(k+2)𝓛`; `k_0≤4.33S+2.89(k+2)𝓛+O(log S)`;
`b≤2.89𝓛+3`; `t=10kbk_0≪k𝓛(S+k𝓛)`. With `z=𝓛²`, `k≤𝓛/(2log𝓛)`,
`S≤S*≪𝓛⁴log𝓛`: `t≪𝓛^6` (both `k𝓛S≪𝓛^6` and `k²𝓛²≪𝓛^4/log²𝓛`);
`K≪S*+t𝓛≪𝓛^7`; `log Q_Π≤(π(𝓛²)+64k²S*)𝓛+4≪𝓛^7/log𝓛`;
`log Z≪𝓛^7`; `log p≪K·max(log Z,K)≪𝓛^{14}`. With `W(p)>T=e^𝓛`:
`log W(p)≥𝓛≥c(log p)^{1/14}`; `p>ℓ_0>T` gives infinitely many p; `840|Q_Π`
gives Mordell-hard. No parameter-dependent constant: the switching
constant 5, the LMN factor 2, the density `e^{1/3}`, the LLL constants
and TZ's `C_0,c_4` are absolute; `k,t,b,k_0` enter only polynomially.

### Theorem 4.4 — SOUND

Unconditional `S*≤exp((log2+o(1))𝓛/log𝓛)` (O2 Lemma 11.1 + Wigert):
`t≪𝓛²S*`, `K,log Z≪𝓛³S*`, `log p≪𝓛^6S*²`, so
`log₂p≤2log S*+O(log𝓛)≤(2log2+o(1))𝓛/log𝓛`. Inverting the increasing
`x/log x`: `𝓛≥(1/(2log2)−o(1))log₂p·log(log₂p)`, i.e.
`log W(p)≥(1/(2log2)−o(1))log₂p·log₃p` ✓ (the o(1) is as T→∞ along the
constructed sequence; p≥T).

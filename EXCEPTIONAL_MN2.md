# EXCEPTIONAL_MN2 — the density transition for m/p (task O102)

Status labels as in DISCOVERIES.md. "MN" = `EXCEPTIONAL_MN.md` ((D)31; PROVED rel. the 3/4 note).
"The note" = `paper/es-threequarter-note.tex`. PW = Pomerance–Weingartner, arXiv:2511.16817v2
(`sources/pw.txt`). Notation: `m ≥ 4`, `L = log N`, `π*(N) = π(N) − π(N/2)`,
`π*(N; q, a)` the same in the class `a (mod q)`. A prime p is *m-exceptional* if
`m/p = 1/x+1/y+1/z` has no solution in positive integers. `A := L / m^{1/3}`.

## 0. Summary

Let `ρ_exc(m,N)` / `ρ_rep(m,N)` be the proportions of m-exceptional / m-representable primes in
(N/2, N], and `A = log N / m^{1/3}`.

* **Theorem U (upper side; PROVED rel. MN Cor 3.2, Bombieri–Vinogradov, Shiu; §1).**
  `ρ_exc → 0` as `A → ∞`, uniformly in m ≥ 4: for every ε > 0 there is `A_ε` (ineffective) with
  `ρ_exc ≤ ε` whenever `log N ≥ A_ε m^{1/3}`. Quantitatively (Thm 1.3) `ρ_exc ≤ 3e^{−a s}` for
  `log N ≥ C_1 s^{4/3} m^{1/3}`, `N ≥ N_0(s)`. This removes the `(log m)^{4/3}` of MN Cor D:
  **g ≡ 1 on the upper side.** Mechanism: bounded-depth Bonferroni in the *reduced* CRT model
  (every fibre is reduced for primes, so MN's void needs no selector) + BV at level `N^{0.45}`;
  the term multiplicities are polylog on average (Shiu), which BV absorbs.
* **Theorem L (lower side; PROVED rel. ET Thm 7.1/Prop 1.4 proof, BT, Shiu; §3).**
  `ρ_rep ≪ L³/m + (L³ + L² log² m) log L/φ(m) + m^{−0.35}` (for `log m ≤ L/10`, `L ≤ m^{1/2}`), so
  `ρ_rep → 0` whenever `L³ log L/φ(m) → 0`, in particular when `A·(m log m/φ(m))^{1/3} → 0`.
  Improves PW's `L³ log² m/φ(m)` by a factor log m: Type II is made sharp (`≪ L³/m`, ET's 3-way
  flip + coprimality of e to m); in Type I, ET Prop 1.4's `log(1+k)` is confined to a lower-order
  region by Pólya–Vinogradov. **What remains is exactly ET's Type I Brun–Titchmarsh `log log N`**
  (ET Thm 1.1's prime bound, open at m = 4) and `m/φ(m)` from Type I.
* **Remaining gap** in `log N`: factor `(m log m/φ(m))^{1/3} ≪ (log m · log log m)^{1/3}`
  (was `(log m)² (m/φ(m))^{1/3}`). Removing the Type I BT loss and tracking the coprimality gain in
  ET Prop 1.4 would give the exact scale: `ρ_rep → 0` if `A → 0`, with Theorem U's `ρ_exc → 0` if `A → ∞`.
* **Numerics (EVIDENCE; §2).** m ≤ 300: for even m ∈ [60, 300], `L_{1/2}/m^{1/3} = 1.95 ± 0.05`,
  local exponent 0.333; profile in A ≈ `1 − exp(−κA³)`, κ ≈ 0.094. Odd m: ratio 1.63–1.92, drifting up
  (local exponents 0.36–0.40) — a parity effect at these sizes.
* **Conjecture C2 (CONJECTURE; supported by §2).** `ρ_rep(m, N) = F(A) + o(1)` as `m → ∞`, for a
  continuous increasing F with F(0+) = 0, F(∞) = 1 (possibly depending on m only through
  bounded arithmetic data). In particular there is **no sharp threshold constant**: the
  transition window is of the same order `m^{1/3}` as its location. (Even the Poisson model with
  intensity `κ L³/m` predicts this; MN's fibre masses `μ_c ≍ t³/m` are two-sided only up to
  constants, and the data show strong overdispersion, so F is not expected to be exactly Poisson.)

## 1. Upper side: prime-model Bonferroni of bounded depth

**Why MN Cor D lost `(log m)^{4/3}`.** Theorem A counts *integers*: `E_m(N) ≤ CN e^{−c s}`,
`s ≍ A^{3/4}`. Primes have density `1/L`, so the integer bound says something about primes only
once `e^{−cs} ≪ 1/L`, i.e. `s ≫ log L ≍ log m`. At the transition only `s → ∞` (slowly) is
needed, but then the prime count must be handled *directly*. For primes the note's exact
transfer `#{n ≤ N : n ≡ a (q)} = N/q + O(1)` is unavailable, but with **bounded** Bonferroni depth
r the Bonferroni majorant has level `≤ N^{0.45}` and only polylog-many terms per modulus on
average, so Bombieri–Vinogradov (BV) suffices.

Setting. Use MN's atom family `𝒜 = 𝒜^{(m)}_X` (MN Def 1.2: `k ∈ 𝒦_m(K)`, `K = X^κ`, ℓ prime in
`(X^{1/2}, X]`, `H < u,v ≤ z_j`, `muv | kℓ+1`, ω-cutoff), `t = log X`, events
`E_A = {n ≡ a_A (mod kℓ)}`, `a_A = −u v^{−1}`, a unit mod kℓ; `H(n) = Σ_A 1_{E_A}(n)`;
`L_K = lcm 𝒦_m(K)`. By MN Lemma 1.1 every m-exceptional n has `H(n) = 0`.
Put `s = t³/m` (so `t = (sm)^{1/3}`), and `Q_r(h) = Σ_{j≤r}(−1)^j C(h,j)` (r even), so
`1_{h=0} ≤ Q_r(h) ≤ 1_{h=0} + C(h, r+1)` (note lem:Bonferroni).

**Lemma 1.1 (reduced CRT model; PROVED rel. MN Cor 3.2).** Let `𝓜 = L_K · Π_{X^{1/2}<ℓ≤X} ℓ`
and let ñ be uniform on `(Z/𝓜Z)^×`. There are absolute `X_1, a_u, C_u` such that for
`X ≥ X_1`, `4 ≤ m ≤ t³` and every even `r ≥ e² · 2C_u s`:
`E[Q_r(H(ñ))] ≤ e^{−a_u s} + e^{−(r+1)}`.

*Proof.* Write `c = ñ mod L_K` (uniform on reduced classes) and `ñ mod ℓ` (uniform on
`(Z/ℓ)^×`), all independent (CRT for unit groups; ℓ > X^{1/2} > K so `ℓ ∤ L_K`). Given c, atom A
is *active* iff `k | u + cv`; at a fixed ℓ the active atoms have pairwise distinct classes mod ℓ
(MN Lemma 1.3), all non-zero (`0 < u < ℓ`). Hence, given c, `H = Σ_ℓ ξ_ℓ` with independent
`ξ_ℓ ~ Bernoulli(f_c(ℓ)/(ℓ−1))`. Therefore
`P(H = 0 | c) = Π_ℓ (1 − f_c(ℓ)/(ℓ−1)) ≤ exp(−μ_c)` and
`E[C(H, r+1) | c] = Σ_{ℓ_1<…<ℓ_{r+1}} Π_i f_c(ℓ_i)/(ℓ_i−1) ≤ (μ'_c)^{r+1}/(r+1)!`,
with `μ_c = Σ_ℓ f_c(ℓ)/ℓ ≤ μ'_c = Σ_ℓ f_c(ℓ)/(ℓ−1) ≤ 2μ_c`. Since c is reduced mod L_K,
MN Cor 3.2 gives `a_u s ≤ μ_c ≤ C_u s`. With `(r+1)! ≥ ((r+1)/e)^{r+1}`:
`E[Q_r(H)|c] ≤ e^{−a_u s} + (2eC_u s/(r+1))^{r+1} ≤ e^{−a_u s} + e^{−(r+1)}`. Average over c. ∎

(Compared with MN Lemma 4.1, no selector `S_y` and no bad-fibre event `Z(c) > η` are needed:
in the reduced model every fibre is reduced. This is exactly the prime situation.)

**Lemma 1.2 (multiplicity of moduli; PROVED, Shiu).** Expand
`Q_r(H(n)) = Σ_{B ⊆ 𝒜, |B| ≤ r} (−1)^{|B|} 1[n ∈ ∩_{A∈B} E_A]`. Drop the B with
`∩ E_A = ∅` (identically zero). Each remaining B has *distinct* ℓ's (MN Lemma 1.3) and
`∩_B E_A` is one unit class `a_B mod q_B`, `q_B = lcm(k_A ℓ_A) = q'_B Π_{A∈B} ℓ_A`,
`q'_B = lcm(k_A) ≤ K^r`. Let `M(q) = #{B : q_B = q}`. Then, for fixed r and `X ≥ X_2(r)`,
`S_2 := Σ_q M(q)²/φ(q) ≤ C(r) t^{17r + 4^r}` (for `X ≥ X_1`; `C(r)` depends on r, κ only).

*Proof.* Since `k ≤ K < X^{1/2} < ℓ`, the ℓ's of B are exactly the prime factors of q above
`X^{1/2}`, each carrying one atom; given q and ℓ | q, that atom is fixed by `k | q' := q/Πℓ` and
`(u, v)` with `u, v | kℓ+1`. So `M(q) ≤ Π_{ℓ|q, ℓ>X^{1/2}} g_{q'}(ℓ)`,
`g_{q'}(ℓ) = Σ_{k|q', k≤K} τ(kℓ+1)²` (atoms have k ≤ K; R-self repair 3), and
`g_{q'}(ℓ)² ≤ τ(q') Σ_{k|q', k≤K} τ(kℓ+1)⁴` (Cauchy–Schwarz).
Shiu's theorem (Shiu 1980, Thm 1, F = τ⁴, progression `n ≡ 1 (mod k)`, `n ∈ (kx, 2kx]`,
`k ≤ X^κ ≤ x^{2κ}`, `x ≥ X^{1/2}`) gives `Σ_{x<ℓ≤2x} τ(kℓ+1)⁴ ≪ (k/φ(k)) x (log X)^{15}`;
summing dyadically and using `k/φ(k) ≪ log t`:
`Σ_{X^{1/2}<ℓ≤X} τ(kℓ+1)⁴/(ℓ−1) ≪ t^{17}`. Hence
`Σ_ℓ g_{q'}(ℓ)²/(ℓ−1) ≤ C τ(q')² t^{17}`, and, as φ is multiplicative over the coprime
factors `q'`, ℓ's,
`S_2 ≤ Σ_{q' ≤ K^r} (1/φ(q')) Σ_{j≤r} (Cτ(q')² t^{17})^j / j! ≤ (r+1) C^r t^{17r} Σ_{q'≤K^r} τ(q')^{2r}/φ(q')`.
Finally `Σ_{n≤x} τ(n)^{2r}/φ(n) ≤ Π_{p≤x}(1 + Σ_{ν≥1}(ν+1)^{2r}/φ(p^ν)) ≪_r (log x)^{4^r}`
with `log K^r ≤ rκt`. ∎

**Theorem 1.3 (PROVED rel. MN Cor 3.2, BV, Shiu).** There are absolute `a, C_1, s_0 > 0` and for
each `s ≥ s_0` an (ineffective) `N_0(s)` such that for all `m ≥ 4` and `N ≥ N_0(s)` with
`log N ≥ C_1 s^{4/3} m^{1/3}`:
`#{p ∈ (N/2, N] : p m-exceptional} ≤ 3 e^{−a s} π*(N)`.

*Proof.* Take `t = (sm)^{1/3}`, `X = e^t`, r the least even integer `≥ 2e²C_u s`; `t ≥ (4s)^{1/3} ≥ log X_1`
for `s ≥ s_0` (s_0 absolute); `m ≤ t³` as `s ≥ 1`. (Lemma 1.2 needs no size condition beyond
`X ≥ X_1`; its constant `C(r)` is absorbed into `N_0(s)`.) Moduli: `q_B ≤ (KX)^r = e^{(1+κ)rt}`, and `(1+κ) r t ≤ (1+κ)(2e²C_u s + 2)(sm)^{1/3}
≤ 0.45 L` once `C_1` is large: so `q_B ≤ N^{0.45}`.
Every m-exceptional prime p has `Q_r(H(p)) ≥ 1`, so
`#{exc. p} ≤ Σ_{p ∈ (N/2,N]} Q_r(H(p)) = Σ_B (−1)^{|B|} π*(N; q_B, a_B)`.
Write `π*(N; q, a) = π*(N)/φ(q) + Δ(q, a)`. The main terms sum to `π*(N) E[Q_r(H(ñ))]`
exactly (`P(ñ ≡ a_B mod q_B) = 1/φ(q_B)`, `a_B` a unit), which is `≤ π*(N)(e^{−a_u s} + e^{−(r+1)})`
by Lemma 1.1. For the error, by Brun–Titchmarsh `|Δ(q,a)| ≤ C N/(φ(q) L)` (q ≤ N^{0.45}), and by
BV (with `π*` = difference of two BV sums) `Σ_{q≤N^{0.45}} max_{(a,q)=1}|Δ(q,a)| ≪_{A'} N L^{−A'}`. Cauchy–Schwarz:
`Σ_B |Δ(q_B,a_B)| ≤ Σ_q M(q) max_a|Δ(q,a)| ≤ (Σ_q M(q)² C N/(φ(q)L))^{1/2} (C_{A'} N L^{−A'})^{1/2}`
`≤ C'(r) N (t^{17r+4^r} L^{−1−A'})^{1/2} ≤ C'(r) N/L^{3}` for `A' = 17r + 4^r + 5` (`t ≤ L`), which is
`≤ N/L²` for N ≥ N_0(s).
Since `π*(N) ≥ N/(3L)`, `N/L² ≤ e^{−a_u s} π*(N)` for `N ≥ N_0(s)`. Total `≤ 3e^{−a s}π*(N)`
with `a = a_u` (`e^{−(r+1)} ≤ e^{−a_u s}` as `r ≥ a_u s`). ∎

**Theorem U (PROVED rel. MN Cor 3.2, BV, Shiu).** For every ε > 0 there is `A_ε` such that for
all `m ≥ 4` and N with `log N ≥ A_ε m^{1/3}`:
`#{p ∈ (N/2,N] : m-exceptional} ≤ ε π*(N)`.

*Proof.* Fix `s ≥ s_0` with `3e^{−as} ≤ ε`, and `A_ε = max(C_1 s^{4/3}, log N_0(s))`; then
`log N ≥ A_ε m^{1/3} ≥ A_ε` gives both hypotheses of Theorem 1.3. ∎

*Remarks.* (i) Quantitatively, Theorem 1.3 gives proportion `≤ 3exp(−a (A/C_1)^{3/4})` whenever
N is large in terms of A (ineffective BV constant at level `L^{−A'(r)}`, `r ≍ A^{3/4}`); MN Cor D
covers `A ≥ C (log m)^{4/3}` effectively-in-form. (ii) The m-dependence enters only through
MN Cor 3.2 (`μ_c ≍ t³/m` on every reduced fibre, absolute constants) — the *same* scaling the
lower side must match. (iii) No GRH: BV level 1/2 is ample since the Bonferroni level is
`e^{O(rt)}` with r bounded.

## 2. Numerics: locating the transition for m ≤ 300 (EVIDENCE)

Tool: `scripts/emn2_scan.c` decides m-representability of a prime p exactly via PW Cor 2.4
(Type II: `e | a+b`, `mab | p+e`, `mab ≤ 2p`, e forced to be `−p mod mab`) and PW Cor 2.2 (Type I:
`f | ma²d+1`, `mad | p+f`, `mad ≤ 3p` by PW Lemma 7.4; divisors f and cofactors `g ≤ √(ma²d+1)`
enumerated in their forced classes `−p`, `−p^{−1} (mod mad)`). Validated against an independent
brute force (`scripts/emn2_brute.py`: smallest denominator `s ∈ (p/m, 3p/m]` plus the criterion
`A/B = 1/y+1/z ⟺ ∃ u, v | B, A | u+v`): 0 mismatches for all `4 ≤ m ≤ 40`, `p < 1500`
(e.g. 105 exceptional primes for m = 40). Primes are sampled (every k-th prime, ~600–800 per window).

**2.1 Half-point `L_{1/2}(m)`** (`scripts/emn2_half.py 800 …`, output `scripts/emn2_half.out.txt`):
L_q = log N at which the representable proportion in (N/2, N] reaches q.

| m | φ/m | L_.25 | L_.5 | L_.75 | L_.5/m^{1/3} |
|---|---|---|---|---|---|
| 60 | .267 | 5.68 | 7.64 | 9.41 | 1.95 |
| 64 | .500 | 5.81 | 7.72 | 9.21 | 1.93 |
| 100 | .400 | 7.26 | 9.21 | 10.73 | 1.98 |
| 128 | .500 | 7.16 | 9.65 | 11.42 | 1.91 |
| 150 | .267 | 7.93 | 10.54 | 12.60 | 1.98 |
| 200 | .400 | 8.57 | 11.21 | 13.40 | 1.92 |
| 240 | .267 | 9.89 | 12.50 | 14.88 | 2.01 |
| 256 | .500 | 9.84 | 12.22 | 14.71 | 1.92 |
| 300 | .267 | 10.48 | 13.06 | 15.82 | 1.95 |
| 101 (prime) | .990 | 5.29 | 7.59 | 9.73 | 1.63 |
| 127 (prime) | .992 | 5.87 | 8.84 | 11.05 | 1.76 |
| 199 (prime) | .995 | 8.31 | 10.38 | 12.63 | 1.78 |

**Odd m** (`scripts/emn2_half_odd.out.txt`, same command with
`61,63,75,81,99,105,135,151,165,189,225,251,255,273,293,297`): `L_{1/2}/m^{1/3}` = 1.79 (63), 1.79 (75),
1.77 (81), 1.78 (99), 1.83 (105), 1.83 (135), 1.85 (165), 1.84 (189), 1.92 (225), 1.81 (255), 1.87 (273);
primes 1.63 (61), 1.79 (151), 1.71 (251), 1.80 (293).

* **Even m ∈ [60, 300]** (all sampled composites in the table above are even; R-self MAJOR 5):
  `L_{1/2}/m^{1/3} = 1.95 ± 0.05` with no trend; local log-log slope 60 → 300: `0.333`. A
  `(log m)^{4/3}` (MN Cor D) or `(log m)^{−2/3}` (PW) correction would change the ratio by factors
  1.53 resp. 0.76 over this range; neither is visible.
* **Odd m** sit lower (odd composites 1.77–1.92, odd primes 1.63–1.80) and drift upward: local
  slopes 0.36 (odd composites 63 → 273) and 0.40 (primes 61 → 293). This is a **parity effect**, not a
  prime/composite effect. The data are consistent with a common limit near 1.95 approached from
  below for odd m, but cannot by themselves exclude a slowly varying factor for odd m. Within each
  parity class there is no visible dependence on φ(m)/m.
* **Width.** The window `L_.75 − L_.25 ≈ 0.4 L_.5` does not shrink over this range. In
  `A = L/m^{1/3}` the profile for even m ≥ 60 roughly collapses: `A_.25 ∈ [1.27, 1.59]`,
  `A_.5 ≈ 1.95`, `A_.75 ∈ [2.27, 2.41]`. The one-parameter Poisson-cube profile
  `F(A) = 1 − exp(−κA³)` fitted at A_.5 (κ = ln 2/1.95³ ≈ 0.094) predicts F(1.5) = 0.27,
  F(2.37) = 0.71, consistent with the data. This matches PW's heuristic `exp(−(log p)³/m)` with an
  effective constant κ ≈ 0.09. Finite data; a non-shrinking window is conjectural (C2).
* **Overdispersion** (`scripts/emn2_lambda.out.txt`, count mode): the mean number of Type I+II
  tuples per prime is far above `−log(1−F)`: e.g. m = 200, N = 2^20: mean 4.85 tuples, yet only
  74% of primes are representable (Poisson would give 99.2%). Solutions cluster (fibre effect:
  `p mod m` and p modulo small primes fix most of the mass, cf. MN §4). Type I solutions dominate
  (m = 200, N = 2^20: 72% of primes have a Type I solution, 24% a Type II solution, 75% either).

Assessment: the data (even m especially) support "transition at `log N ≍ m^{1/3}` with a
non-degenerate profile F(A)", i.e. g ≡ 1 and no sharp threshold constant (Conjecture C2). Odd m
show a slower approach. Proportions are over primes `p ∤ m` (the scanner skips p | m).

## 3. Lower side: re-deriving PW's first moment with smaller losses

PW (proof of Thm 3.1) bound the proportion `ρ_rep` of m-representable primes in (N/2, N] by
`≪ L³ log² m/φ(m)` (range `m^{1/4} ≪ L < m`). Their losses relative to the heuristic `L³/m`:
(a) Type II: Brun–Titchmarsh (BT) near modulus N (`log L`) and `φ(m)` instead of m (coprimality
of e to m unused); (b) Type I: ET Prop 1.4's `log(1+k)` (k = m·…) and BT near modulus N (`log L`).
Below: (a) is removed completely; in (b) the `log(1+k)` loss is confined to a lower-order region;
the BT loss in Type I is **not** removed — it is exactly the `log log N` gap in ET Thm 1.1
(`Σ_{p≤N} f_I(p) ≪ N log² N log log N`), which ET could not remove even for m = 4 (ET §9: "it does
not seem that a similar trick is available").

Standing: `m ≥ 4`, `log m ≤ L/10` (the complementary range is Lemma 3.5). Every bound
`≪` has an absolute constant. `S'_m(E) := Σ_{e≤E, (e,m)=1} 1/φ(e) ≤ Π_{p≤E, p∤m}(1 + p/(p−1)²) ≪
(φ(m)/m) log E` for `E ≥ log m` (as MN Lemma 2.1(d): `Π_{p|m, p>E}(1−1/p)^{−1} ≤ e^{2ω(m)/E} ≪ 1`).

**Lemma 3.1 (two harmonic sums; PROVED, elementary).** For `Y ≥ 2`:
(a) For `Y ≥ log m`: `Σ_{e ≤ Y, (e,m)=1} Σ_{a,b ≤ Y, (a,b)=1, e | a+b} 1/(φ(a)φ(b)) ≪ (φ(m)/m) log³ Y + log² Y`.
(b) For `U ≥ 2` with `log U ≥ (1/2) log(mU)`: `Σ_{u ≤ U} τ_3(u)/φ(mu − 1) ≪ (log³ U + m^{0.02})/m`.

*Proof.* (a) Since `(a,b)=1`, `(e,a) = 1`. Using `b/φ(b) = Σ_{g|b} μ²(g)/φ(g)`, for `(β,e) = 1`:
`Σ_{b≤Y, b≡β (e)} 1/φ(b) ≤ 1/φ(β_0) + Σ_g (μ²(g)/φ(g)) Σ_{β_0<b≤Y, b≡β (e), g|b} 1/b ≪ 1/φ(β_0) + (log Y)/e`
(β_0 ∈ [1, e] the least representative; for `(g,e) = 1` the inner sum is over one class mod ge with
`b > e`, so `≤ 1/e + 2 log Y/(ge)`; `(g,e) > 1` gives nothing; `Σ_{g≤Y} μ²(g)/φ(g) ≪ log Y`).
Summing over a in classes `a_0 (mod e)`: `≪ Σ_{a_0+β_0=e} 1/(φ(a_0)φ(β_0)) + (log Y)(log e)/e + (log² Y)/e`
(e = 1: just `log² Y`). The convolution `Σ_{a+β=e} 1/(φ(a)φ(β)) ≪ (log 2e)²/e` (same g-expansion).
Now sum over `e ≤ Y`, `(e,m) = 1`: `Σ (log² Y)/e ≤ log² Y · S'_m(Y) ≪ (φ(m)/m) log³ Y`, plus the e = 1 term.
(b) (Corrected; R-self FATAL 1: the earlier "Shiu after removing the least element" step was false.)
Put `n = mu − 1 ≤ mU`, `y = log(mU)`. Since `ω(n) ≤ 2y`, `Π_{p|n, p>y}(1−1/p)^{−1} ≤ e^4`, so
`n/φ(n) ≤ e^4 Σ_{s|n, s|P(y)} μ²(s)/φ(s)`. Rankin with σ = 1/log y:
`Σ_{s|P(y), s>S} 1/φ(s) ≤ S^{−σ} Π_{p≤y}(1 + p^σ/(p−1)) ≪ S^{−1/log y}(log y)^{2e}`, which for
`S = U^{1/2}` is `≪ y^{−10}` (as `log U ≥ y/2`). That part contributes `≪ y^{−10} Σ_u τ_3(u)/(mu) ≪ 1/m`.
For `s ≤ U^{1/2}`, `(s, m) = 1`, the u lie in one class `r_s ≡ m^{−1} (mod s)`. Split `u ≤ s^{1.1}` /
`u > s^{1.1}`. *Large u:* on dyadic `(x, 2x]` with `x ≥ s^{1.1}`, Shiu (modulus `s ≤ x^{1/1.1}`, F = τ_3)
gives `Σ τ_3(u) ≪ (x/φ(s)) (log x)² (s/φ(s))³`; summing `1/(mx)` over dyadic x and then
`μ²(s)(s/φ(s))³/φ(s)²` over s: `≪ log³ U/m`. *Small u:* swap the order:
`Σ_s (μ²(s)/φ(s)) Σ_{u ≤ s^{1.1}, s | mu−1} τ_3(u)/(mu−1) ≤ Σ_u (τ_3(u)/(mu−1)) τ(mu−1) max_{s ≥ u^{1/1.1}} 1/φ(s)
≪ m^{−1} Σ_u τ_3(u) τ(mu−1) log log(3u) u^{−1−0.909} ≪ m^{0.02}/m` (`τ_3(u) ≪ u^{0.01}`, `τ(mu−1) ≪ (mu)^{0.01}`). ∎

**Proposition 3.2 (Type II, sharp; PROVED rel. BT).** For `log m ≤ L/10`,
`#{p ∈ (N/2,N] : p has a Type II solution} ≪ (N/L)(L³ + m^{1/2})/m`.

*Proof.* PW Cor 2.4/Prop 2.3: `p + e = mabd`, `a + b = ce`, `(a,b) = 1`; by the a↔b symmetry
(y ↔ z) take `a ≤ b`, so `b < ce ≤ 2b`. As `(e, m) | p`, `(e, m) = 1`; likewise `(e, ad) = 1`.
ET §9 with m: `(made)(macd)(mab)^{1/2} ≤ m^{5/2} a²b·ce·d² ≤ 2m^{5/2}(abd)² ≤ 8 m^{1/2} N²`, so one of
the three moduli is `≤ 3 m^{1/5} N^{4/5} ≤ 3N^{0.82}`; in each case BT has `log(N/q) ≫ L`.
(i) `made ≤ 3N^{0.82}`: fix (a, d, e); `b ≡ −a (e)` puts p in one class mod made:
`≪ Σ N/(L φ(m)φ(a)φ(d)φ(e)) ≪ (N/(Lφ(m))) L² S'_m(N) ≪ N L²/m`.
(ii) `macd ≤ 3N^{0.82}`: fix (a, c, d); `p = (macd − 1)e − ma²d`, one class mod `macd − 1`:
`≪ (N/L) Σ_{u ≤ 3N^{0.82}/m} τ_3(u)/φ(mu−1) ≪ (N/L)(L³ + m^{0.02})/m` (Lemma 3.1(b); its size
hypothesis holds as `m ≤ N^{1/10}`).
(iii) `mab ≤ 3N^{0.82}`: fix (a, b, e), one class `−e (mod mab)`:
`≪ (N/(Lφ(m))) Σ 1/(φ(a)φ(b)) ≪ (N/(Lφ(m)))((φ(m)/m)L³ + L²) ≪ N L²/m + N L/φ(m)`, and
`L/φ(m) ≪ L² log log m/m ≪ L³/m` since `L ≥ log(m/3)`. ∎

**Lemma 3.3 (ET Prop 1.4 with Pólya–Vinogradov; PROVED rel. ET Thm 7.1 and ET's proof of Prop 1.4).**
Fix l. For `k ≥ 1`, `A, D ≥ 2`, `k ≤ (AD)^l`:
`Σ_{a≤A, d≤D} τ(k a² d + 1) ≪_l AD log(A+D) · (1 + 1[D < k log⁴(kAD)] log(1+k))`.

*Proof.* If `D ≥ A`: ET Cor 7.4 in the linear variable d for each a (coefficient `ka² ≤ D^{3l}`):
`≪ D log D` per a. If `D < A`: follow ET's proof of Prop 1.4, case "A ≤ B" (their linear variable a
= our d, their quadratic b = our a, their k = our k; ET pp. 30–32), keeping its **signed**
expression (7.11) `Σ_{q≤A, (q,2k)=1} Σ_{d≤D, (d,2q)=1} (−kd/q) log(A/q)/q`, after ET's reduction to
odd d (`d = 2^j d'`, `2^j` absorbed into k, D into `D/2^j`). ET split q into `q < D` (period 2q,
inner sum O(q): no loss), `q > kD` (reciprocity in q for each fixed d, partial summation over q:
`O(log A)` per d, no loss), and `D ≤ q ≤ kD`, where they bound `|(−kd/q)| ≤ 1` and lose `log(1+k)`.
Only the middle range is changed (absolute values are taken only there, which is legitimate):
for q non-square, `d ↦ (d/q)1_{d odd}` is a combination of two non-principal character sums, so
`|Σ_{d≤D'}| ≪ √q log q` (Pólya–Vinogradov); squares `q = r²` give `≤ D' Σ_r log A/r² ≪ D' log A`.
So the middle range costs `≪ D' log A + log A Σ_{q≤kD'} log q/√q ≪ D' log A (1 + √(k/D') log(kD'))`,
`≪ D' log A` when `D' ≥ k log²(kAD)`. Summing over j with weight `2^{−j}` (`d' ≤ D/2^j`, `k → 2^j k`): the middle range is lossy only for
the j with `4^j > D/(k log²(kAD))`, whose total contribution is `≪ Σ_{such j} 2^{−j} log(1+2^j k) ≪
(k log²(kAD)/D)^{1/2} log(kAD) ≤ 1` when `D ≥ k log⁴(kAD)`. ∎

**Proposition 3.4 (Type I; PROVED rel. Lemma 3.3, BT).** For `log m ≤ L/10` and `L ≤ m^{1/2}`:
`#{p ∈ (N/2,N] : Type I solution} ≪ (N/L)·[(L³ + L² log² m) log L/φ(m) + m^{−0.35}]`.

*Proof.* PW (3.2): `≪ Σ_{mad ≤ 3N} τ(ma²d+1) N/(φ(m)φ(ad) log(2+N/mad))`. ET (A.12)
`1/φ(ad) ≪ (ad)^{−1}Σ_{s|a, t|d} 1/(st)`; put `a = sa'`, `d = td'`, `k = ms²t`, and split the block
`ad ~ X` into `≪ log X` dyadic boxes `a' ~ A'`, `d' ~ D'`, `A'D' ≍ X/(st)`.
* Boxes with `A'D' ≥ k^{1/10}`: Lemma 3.3 (l = 10). Non-lossy boxes give `(X/st) log X` each; lossy
  ones (`D' < k log²(kN)`, at most `≪ log m + log(st) + log L` of them) give `(X/st) L log(1+k)` each.
  With the weight `(st)^{−1}` and `X^{−1}` this is `Σ_{s,t}(st)^{−2}[log² X + L log²(ms²t L)]
  ≪ log² X + L log² m` per block (`log L ≪ log m` as `L ≤ m^{1/2}`).
* Boxes with `A'D' < k^{1/10}`: `τ(n) ≪ n^{1/40}`, `n ≤ k·(A'D')² ≤ k^{1.2}`, so each gives
  `≪ (X/st)·k^{0.03}`; they exist only in blocks with `X ≤ st·k^{0.1}`, and in total contribute
  `≪ (N/φ(m)) m^{0.1} log² m ≪ N m^{−0.85}` to the count, i.e. `≪ (N/L) L m^{−0.85} ≤ (N/L) m^{−0.35}`.
Summing blocks `X = 3N2^{−j}/m` with BT weight `1/log(2 + 2^j/3) ≪ 1/j`, `j ≤ 2L`:
count `≪ (N/φ(m))(L² + L log² m) log L`, which is the claim. ∎

**Lemma 3.5 (very large m; PROVED, trivial).** For `log m > L/10`: `ρ_rep ≤ e^{C L/log L}/m`.
*Proof.* Count classes trivially: `#{n ≤ N : n ≡ r (q)} ≤ N/q + 1`, `τ(n) ≤ e^{CL/log L}` for
`n ≤ 9N²`; Type I: `Σ_{mad≤3N} τ(ma²d+1)(N/(mad)+1) ≪ e^{CL/log L}(N/m)L²`, Type II likewise. ∎

**Theorem L (lower side; PROVED rel. ET Thm 7.1 + ET's proof of Prop 1.4, BT, Shiu).** Let
`ρ_rep(m, N)` be the proportion of m-representable primes in (N/2, N]. For all `m ≥ 4`, `N ≥ 16`:
* if `log m ≤ L/10` and `L ≤ m^{1/2}`: `ρ_rep ≪ L³/m + (L³ + L² log² m) log L/φ(m) + m^{−0.35}`
  (Props 3.2, 3.4; `π*(N) ≫ N/L`);
* if `log m > L/10`: `ρ_rep ≤ e^{CL/log L}/m` (Lemma 3.5).
Consequently **`ρ_rep → 0` whenever `L³ log L/φ(m) → 0`**, e.g. when `L ≤ ε (φ(m)/log m)^{1/3}` with
ε → 0. (If `ρ_rep > 0` then `L ≥ log(m/3)`, so `A → 0` forces `m → ∞`; and
`L² log² m log L/φ(m) ≤ (L³ + log⁶ m) log L/φ(m) → 0`.)

## 4. Status and open points

* Theorem U, Thm 1.3: PROVED relative to MN Cor 3.2 (itself PROVED rel. the note), BV, Shiu.
  Ineffective (BV/Siegel at level `L^{−A'(r)}`, r ≍ s).
* Theorem L: PROVED relative to ET Thm 7.1 and the structure of ET's proof of Prop 1.4 (Lemma 3.3
  changes one range of q), BT, Shiu, Pólya–Vinogradov. Not machine-checked.
* §2: EVIDENCE. Conjecture C2: CONJECTURE.
* Open: (i) Type I prime count without the BT `log L` (= ET's open `log log N` for m = 4); a
  two-variable (c, w) Selberg sieve handles most of the bad range `c < N^δ`, `d < gN^δ` but not
  `c, w = O(1)` (scratch analysis, not written up); (ii) the `φ(m)/m` coprimality gain in ET
  Prop 1.4 (main terms come from square q, which lose the Euler factors at p | m in ET's upper
  bound `ρ ≤ 1 ∗ χ`); (iii) a quantitative, effective form of Theorem U for `1 ≪ A ≪ (log m)^{4/3}`.

## Replay

```
gcc -O2 -o /tmp/emn2_scan scripts/emn2_scan.c -lm
uv run --with sympy python scripts/emn2_brute.py 40 1500   # per-prime validation, exit 1 on mismatch, ~1 min
ulimit -v 8000000; timeout 3000 uv run python scripts/emn2_transition.py 600 8,16,32,64,128,200 6 22
                                                     # -> scripts/emn2_transition.out.txt, ~20 min
ulimit -v 8000000; timeout 3000 uv run python scripts/emn2_transition.py 300 16,64,128,200 8 20 1
                                                     # -> scripts/emn2_lambda.out.txt (tuple means)
ulimit -v 8000000; timeout 3500 uv run --with sympy python scripts/emn2_half.py 800 \
  6,8,10,12,16,20,24,30,36,48,60,64,72,90,100,101,120,127,128,150,180,199,200,210,240,256,300
                                                     # -> scripts/emn2_half.out.txt, ~40 min
```
ulimit -v 8000000; timeout 5000 uv run --with sympy python scripts/emn2_half.py 800 \
  61,63,75,81,99,105,135,151,165,189,225,251,255,273,293,297   # -> scripts/emn2_half_odd.out.txt
(Sampling is deterministic: every k-th prime; 2 worker processes.)

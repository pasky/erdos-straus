# EXCEPTIONAL_MN2 — the density transition for m/p (task O102)

Status labels as in DISCOVERIES.md. "MN" = `EXCEPTIONAL_MN.md` ((D)31; PROVED rel. the 3/4 note).
"The note" = `paper/es-threequarter-note.tex`. PW = Pomerance–Weingartner, arXiv:2511.16817v2
(`sources/pw.txt`). Notation: `m ≥ 4`, `L = log N`, `π*(N) = π(N) − π(N/2)`,
`π*(N; q, a)` the same in the class `a (mod q)`. A prime p is *m-exceptional* if
`m/p = 1/x+1/y+1/z` has no solution in positive integers. `A := L / m^{1/3}`.

## 0. Summary (filled in as the work proceeds)

* **Theorem U (upper side; PROVED rel. MN Cor 3.2 + Bombieri–Vinogradov).** For every ε > 0
  there is `A_ε` such that for all `m ≥ 4` and all N with `log N ≥ A_ε m^{1/3}`, at most
  `ε π*(N)` primes in `(N/2, N]` are m-exceptional. I.e. the `(log m)^{4/3}` in MN Cor D is
  removed: g ≡ 1 on the upper side (qualitatively; the dependence of `A_ε` on ε is ineffective).

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
`g_{q'}(ℓ) = Σ_{k|q'} τ(kℓ+1)²`, and `g_{q'}(ℓ)² ≤ τ(q') Σ_{k|q'} τ(kℓ+1)⁴` (Cauchy–Schwarz).
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
`≤ C(r) N (t^{17r+4^r} L^{−1−A'})^{1/2} ≤ N/L²` for `A' = 17r + 4^r + 3` (`t ≤ L`) and N ≥ N_0(s).
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

* For composite m in [60, 300], `L_{1/2}/m^{1/3} = 1.95 ± 0.05` with no trend; the local
  log-log slope from m = 60 to 300 is `log(13.06/7.64)/log 5 = 0.333`. A `(log m)^{4/3}` (MN Cor D)
  or `(log m)^{−2/3}` (PW) correction would change the ratio by factors 1.53 resp. 0.76 over this
  range; neither is visible. No visible φ(m)/m dependence among composites (φ/m from .23 to .5).
* Prime m sit lower (1.63–1.78) but drift upward (slope ≈ 0.46 from 101 to 199); finite-size.
* **The transition is not sharp:** the window `L_.75 − L_.25 ≈ 0.4 L_.5` does not shrink. In
  `A = L/m^{1/3}` the profile collapses (composite m): `A_.25 ≈ 1.45–1.57`, `A_.5 ≈ 1.95`,
  `A_.75 ≈ 2.36–2.40`. The one-parameter Poisson profile `F(A) = 1 − exp(−κA³)` with κ fitted
  at A_.5 (κ = ln 2/1.95³ ≈ 0.094) predicts F(1.5) = 0.27, F(2.37) = 0.71 — a good fit. This is
  PW's heuristic `exp(−(log p)³/m)` with an effective constant κ ≈ 0.09.
* **Overdispersion** (`scripts/emn2_lambda.out.txt`, count mode): the mean number of Type I+II
  tuples per prime is far above `−log(1−F)`: e.g. m = 200, N = 2^20: mean 4.85 tuples, yet only
  74% of primes are representable (Poisson would give 99.2%). Solutions cluster (fibre effect:
  `p mod m` and p modulo small primes fix most of the mass, cf. MN §4). Type I solutions dominate
  (e.g. m = 200, N = 2^20: Type II-only 2.3%... Type I alone covers 71%, Type II alone 23%).

Assessment: the data support "transition at `log N ≍ m^{1/3}` exactly, with a non-degenerate
profile F(A)", i.e. g ≡ 1 and **no sharp threshold constant** — the right theorem is two-sided
at the scale, not a 0–1 law at a constant. (Conjecture C2 below.)

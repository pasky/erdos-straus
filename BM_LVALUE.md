# BM_LVALUE — the Brauer–Manin correction T(p) is ¼·E(χ_p)·L(1,χ_p)² (depth lane Z2882, wave z52c)

Status: depth-lane draft (skeleton). **ES is OPEN; nothing here proves ES or any infinite case of it.** Labels: PROVED /
CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Scripts `scripts/z52c_bmL_*`, data `data/z52c/bmL/`.
Builds on `BM_CORRECTED_COUNT.md` (Prop 2.1, Thm 2.2, Prop 2.3), `FRONTIER.md` §2.2, Pass-1 record
`BRAINSTORM/z52b_pass1_H07.md` §Z2882.

## 0. Summary
(to be written last)

## 1. Statement and numerics

### 1.1 Definitions (exact; no truncation other than the sharp cutoff of 𝒫(p))

p ≥ 5 is a prime, χ = χ_p = (·/p), σ := χ(−1) = (−1)^{(p−1)/2}. As in `BM_CORRECTED_COUNT.md` §§1–2:
* 𝒫(p) := {(u, B) ∈ ℕ² : gcd(u, B) = 1, u + B odd, 4uB − u − B ≤ p} = {… : (4u − 1)(4B − 1) ≤ 4p + 1}.
* M₀(p) := Σ_{𝒫(p)} 1/φ(4uB), **T(p) := Σ_{𝒫(p)} (−uB/p)/φ(4uB) = σ·Σ_{𝒫(p)} χ(u)χ(B)/φ(4uB)**, M_BM(p) = M₀(p) − T(p)
  (`BM_CORRECTED_COUNT` Prop 2.1(d); Theorem 1.1 there is stated for every prime p, so T is defined for p ≡ 3 (4) too).
* Split 𝒫(p) = 𝒫_bulk ⊔ ℬ, 𝒫_bulk := {4uB ≤ p}, ℬ := {p/4 < uB ≤ (p + u + B)/4} (the *boundary*). On 𝒫_bulk the
  map (u, B) ↦ m = uB is 2^{ω(m)}-to-1 onto the even m ≤ p/4 (`BM_CORRECTED` Prop 2.1(e)).
* The local factor
  **E(χ) := (2χ(2) − 1) · ∏_{ℓ odd, ℓ ≠ p} e_ℓ(χ(ℓ)),  e_ℓ(+1) = 1 + 1/ℓ²,  e_ℓ(−1) = 1 − (3ℓ + 1)/(ℓ²(ℓ − 1))**
  (in general e_ℓ(c) = 1 + 2c/(ℓ(ℓ − 1)) − c²(ℓ + 1)/(ℓ²(ℓ − 1)); this equals the Pass-1 form
  (1 − c/ℓ)² + 2c(1 − c/ℓ)/(ℓ − 1), and 2χ(2) − 1 = 2χ(2)(1 − χ(2)/2)). E(χ) = H(1, χ) where
  Σ_{m even} χ(m)2^{ω(m)}m^{1−s}/φ(m) = L(s, χ)²·H(s, χ) (§2, Lemma 2.2). Every e_ℓ lies in (0, 1 + ℓ⁻²] (e₃(−1) = 4/9), so
  **sign E = χ(2)**; precisely 0 < E ≤ ∏_{ℓ odd}(1 + ℓ⁻²) = 12/π² if χ(2) = 1, and
  −36/π² ≤ E < 0 if χ(2) = −1.
* Class-number form: L(1, χ) = 2h(p) log ε_p/√p for p ≡ 1 (4) (ℚ(√p), ε_p the fundamental unit), L(1, χ) = πh(−p)/√p for
  p ≡ 3 (4), p > 3.

**The p mod 8 dependence** (σ and χ(2) = (−1)^{(p²−1)/8}):

| p mod 8 | σ | χ(2) | 2-factor 2χ(2) − 1 | sign of T ≈ σE·L²/4 | effect on M_BM = M₀ − T |
|---|---|---|---|---|---|
| 1 | + | + | +1 | T > 0 | deficit (M_BM < M₀) |
| 5 | + | − | −3 | T < 0 | surplus |
| 3 | − | − | −3 | T > 0 | deficit |
| 7 | − | + | +1 | T < 0 | surplus |

**Theorem A (PROVED, §2; unconditional, effective).** There is an absolute effective constant c such that for every prime
p ≥ 5
  **T(p) = (σ/4)·E(χ_p)·L(1, χ_p)² + θ·c·p^{−1/16} log p,  |θ| ≤ 1.**
Equivalently, p ≡ 1 (4): **T(p) = E(χ_p)·(h(p) log ε_p)²/p + O(p^{−1/16} log p)**; p ≡ 3 (4):
T(p) = −(π²/4)·E(χ_p)·h(−p)²/p + O(p^{−1/16} log p). The boundary ℬ contributes only O(p^{−1/4}(log p)² log log p)
(Pólya–Vinogradov suffices there); the p^{−1/16} comes from Burgess (r = 2) in the bulk. **CONDITIONAL on GRH** (via the
Lindelöf consequence Σ_{n≤t}χ(n) ≪_ε t^{1/2}p^ε) the error is O_ε(p^{−1/4+ε}). Neither bound is close to the observed size
(≈ p^{−1/2}(log p)^{3/2}, §1.3).

### 1.2 Data (EVIDENCE; `scripts/z52c_bmL_Tp.c`, driver `z52c_bmL_run.sh`, stats `z52c_bmL_stats.py` → `data/z52c/bmL/stats.txt`)

Engine: per prime, T, its bulk/boundary split, M₀, R(p) (the (★) count), M_gen (genus main term of SINGLE_P_COUNT Lemma 2.1,
cross-checked against `scripts/z30_rgen.c` at 6 primes), L(1, χ) **exactly** from the finite formulas
L(1, χ) = −p^{−1/2}Σ_{a<p} χ(a) log(2 sin(πa/p)) (σ = +1), πh(−p)/√p with h(−p) = −p⁻¹Σ aχ(a) (σ = −1), and E as the Euler
product over ℓ ≤ 2·10⁶ (relative truncation error < 10⁻⁶). Long-double accumulation. Samples (91 415 distinct primes):
* **census**: all 78 496 primes 5 ≤ p ≤ 10⁶ (both classes mod 4);
* **window**: all 12 314 primes in [9.8·10⁶, 10⁷];
* **strat**: 600 random p ≡ 1 (4) in (10⁶, 9.8·10⁶) (seed 52882) plus the five (★)-failures > 10⁶.
`scripts/z52c_bmL_identity_check.py` verifies the algebra of §2 (convolution identity exactly for m ≤ 3000; the bulk/boundary
decomposition, the d-expansion and the hyperbola identity in floating point at six primes) and reproduces the C values.
Pass-1 values (40 random primes, `data/z52b/pass1/H07/`) are reproduced exactly.

Error err := T − (σ/4)E·L(1, χ)² (from `stats.txt`; "[9.8e6, 1e7]" = window):

| range | p mod 8 | N | mean err | sd err | max \|err\| (at p) | max \|T_ℬ\| | range of T |
|---|---|---|---|---|---|---|---|
| [10³, 10⁴) | 1 / 5 / 3 / 7 | 258 / 271 / 267 / 265 | +0.145 / +0.001 / −0.022 / −0.042 | 0.098 / 0.044 / 0.045 / 0.049 | 0.54 (1129) / 0.21 / 0.15 / 0.20 | ≤ 0.153 | [−6.1, 4.9] |
| [10⁴, 10⁵) | 1 / 5 / 3 / 7 | ≈ 2090 each | +0.061 / 0.000 / −0.007 / −0.014 | 0.047 / 0.020 / 0.021 / 0.022 | 0.30 (13729) / 0.10 / 0.10 / 0.12 | ≤ 0.060 | [−8.8, 7.0] |
| [10⁵, 10⁶] | 1 / 5 / 3 / 7 | ≈ 17 200 each | +0.024 / −0.000 / −0.002 / −0.004 | 0.022 / 0.008 / 0.008 / 0.009 | 0.18 (130729) / 0.064 / 0.058 / 0.050 | ≤ 0.022 | [−10.8, 9.0] |
| (10⁶, 9.8·10⁶) | 1 / 5 | 306 / 299 | +0.010 / −0.000 | 0.010 / 0.003 | 0.068 (1726201) / 0.013 | ≤ 0.0052 | [−3.9, 10.3] |
| [9.8·10⁶, 10⁷] | 1 / 5 / 3 / 7 | ≈ 3080 each | +0.006 / −0.000 / −0.001 / −0.001 | 0.007 / 0.002 / 0.002 / 0.003 | 0.052 (9850801) / 0.017 / 0.017 / 0.010 | ≤ 0.0024 | [−12.1, 10.5] |

* **The identity holds to within 0.6 at every prime p ≥ 10³ (91 415 primes), within 0.18 for p ≥ 10⁵ and within 0.052 on
  the window at 10⁷, while T itself ranges over [−12.1, 10.5].** Relative to the typical spread of T the error is ≲ 1 %
  at 10⁷.
* The boundary ℬ is negligible (≤ 0.0024 at 10⁷); the bulk carries the whole error.
* Small primes (p < 10³, not in the table): the error is O(1) there (e.g. p = 7: T = −0.5, prediction −0.127).

### 1.3 Size of the error term (EVIDENCE / CONJECTURE)

* **Rate.** On dyadic bins 2¹⁰ … 2²⁴ (p ≡ 1 (4)), rms(err)·√p/(log p)^{3/2} = 0.32–0.34 (one bin of 75 primes: 0.39), flat
  over the whole range; a pure power fit gives rms ≈ 2.8·p^{−0.37} on this range, which is the same curve. So empirically
  **err ≍ p^{−1/2}(log p)^{3/2}**, far below the proved p^{−1/16} log p. (This is the size the random-multiplicative
  model predicts for the tail Σ_{m > p/4} χ(m)τ(m)/m: variance ≈ Σ_{m>x} τ(m)²/m² ≍ (log x)³/x.)
* **A secondary term at p ≡ 1 (8)** (`scripts/z52c_bmL_secondary.py` → `data/z52c/bmL/secondary.txt`). The error is
  biased only for p ≡ 1 (8) (mean ≈ +0.5 sd); there err·√p is strongly correlated with E·L(1, χ) (corr 0.78–0.86 in every
  range), with err ≈ b·E·L(1, χ)·(log p)/√p, b = 0.57–0.62 stable from 10³ to 10⁷; residual sd ≈ 0.13–0.20·(log p)^{3/2}/√p.
  For p ≡ 7 (8): b ≈ −0.12 … −0.16 (corr ≈ −0.6 … −0.7); p ≡ 3, 5 (8): |b| ≤ 0.05, corr ≤ 0.44 in absolute value.
  Assessment (not proved): partial sums Σ_{n ≤ θp} χ(n) at θ = 1/4, 1/8 are of size √p and depend on p mod 8 (Pólya's
  Fourier expansion; e.g. Σ_{n<p/4} χ(n) is a class number of ℚ(√−p) up to a factor for p ≡ 1 (4)), and the sharp cutoff at
  x = p/4 converts them into a cross term L(1, χ)×(√p-size sum)/p. **CONJECTURE (from the data):**
  T(p) = (σ/4)E L(1, χ)² + β_{p mod 8}·E·L(1, χ)·(log p)/√p + O(p^{−1/2}(log p)^{3/2}) with β₁ ≈ 0.6.
  Not needed anywhere below.

### 1.4 The (★)-failure primes and the hardest primes (EVIDENCE)

All 14 (★)-failures p ≡ 1 (4) ≤ 10¹⁰ (all ≤ 8 813 281, `B1_LINE.md` §3.6) and the 8 failures p ≡ 7 (8) ≤ 10⁶:

| p | p mod 8 | M₀ | T | (σ/4)E L² | err | L(1, χ) | E | M_BM | M_BM/L² | M_gen |
|---|---|---|---|---|---|---|---|---|---|---|
| 409 | 1 | 5.15 | 2.157 | 1.667 | +0.490 | 2.585 | 0.999 | 2.99 | 0.083 | 4.00 |
| 577 | 1 | 5.81 | 1.353 | 1.079 | +0.273 | 2.256 | 0.848 | 4.46 | 0.110 | 5.35 |
| 5569 | 1 | 10.93 | 4.305 | 3.949 | +0.356 | 3.737 | 1.131 | 6.63 | 0.089 | 6.24 |
| 9601 | 1 | 12.39 | 4.744 | 4.436 | +0.308 | 3.939 | 1.143 | 7.64 | 0.091 | 7.93 |
| 23929 | 1 | 15.04 | 3.612 | 3.478 | +0.134 | 3.624 | 1.060 | 11.43 | 0.113 | 11.41 |
| 83449 | 1 | 19.09 | 5.945 | 5.786 | +0.159 | 4.476 | 1.155 | 13.14 | 0.102 | 12.34 |
| 102001 | 1 | 19.78 | 6.682 | 6.511 | +0.171 | 4.707 | 1.176 | 13.10 | 0.099 | 13.41 |
| 329617 | 1 | 24.07 | 2.101 | 2.087 | +0.015 | 3.031 | 0.909 | 21.97 | 0.136 | 21.04 |
| 712321 | 1 | 27.12 | 7.920 | 7.828 | +0.093 | 5.143 | 1.184 | 19.20 | 0.106 | 18.80 |
| 1134241 | 1 | 29.05 | 4.397 | 4.370 | +0.028 | 4.037 | 1.072 | 24.66 | 0.127 | 25.22 |
| 1724209 | 1 | 30.85 | 6.890 | 6.842 | +0.048 | 4.861 | 1.158 | 23.96 | 0.116 | 22.79 |
| 1726201 | 1 | 30.85 | 8.096 | 8.028 | +0.068 | 5.220 | 1.178 | 22.76 | 0.110 | 22.13 |
| 5212561 | 1 | 35.84 | 7.599 | 7.561 | +0.039 | 5.119 | 1.154 | 28.24 | 0.118 | 27.50 |
| 8813281 | 1 | 38.34 | 7.832 | 7.805 | +0.027 | 5.155 | 1.175 | 30.51 | 0.119 | 29.08 |
| 7, 31, 79, 127 | 7 | 0.5–3.3 | −0.21 … −0.64 | −0.13 … −0.33 | −0.04 … −0.37 | 1.19–1.77 | 0.35–0.44 | 1.0–3.5 | — | 0–1.9 |
| 199, 2719, 8191, 861199 | 7 | 3.9–27.9 | −0.41 … −0.79 | −0.39 … −0.71 | −0.004 … −0.08 | 1.91–2.47 | 0.42–0.47 | 4.4–28.3 | — | 2.9–25.7 |

At the 14 failures ≡ 1 (4) the identity's error decreases with p (0.49 → 0.03), as in the random sample. The hardest primes
(smallest R/M_BM, p ≡ 1 (4), p ≥ 10⁴) are listed in `stats.txt`; their correlation with L(1, χ) is §3.3.

## 2. Proof of Theorem A (PROVED)

Notation: F(k) := χ(k)/k, G(t) := Σ_{k≤t} χ(k)/k, L := L(1, χ), S_χ(v) := Σ_{n≤v} χ(n), ν := max_{n≤p} n/φ(n) ≪ log log p.
We may take p ≥ 100 (for p < 100 every quantity is bounded and the constant c absorbs it). Two external inputs:
* **(PV)** For every interval, |Σ_{M<n≤M+N} χ(n)| ≤ P := √p log p (p ≥ 100). Explicit Pólya–Vinogradov
  (Frolenkov–Soundararajan; Lapkova): ≤ (2/π²)√p log p + 0.9467√p + 1.668 (χ even), (1/2π)√p log p + 0.8204√p + 1.0286 (odd), as
  quoted in Johnston–Ramaré–Trudgian, arXiv:2303.13785, Lemma 14; both are ≤ √p log p for p ≥ 100.
* **(Bu)** Burgess (Proc. LMS 12 (1962) 193–206, Thm 2; Iwaniec–Kowalski Thm 12.6) with r = 2, prime modulus:
  |Σ_{M<n≤M+N} χ(n)| ≤ C_B N^{1/2} p^{3/16} log p for all M, N ≥ 1, C_B absolute and effective (explicit versions:
  Treviño, IJNT 11 (2015); Francis, JNT 228 (2021)).

**Lemma 2.1 (decomposition).** T(p) = (σ/4)·(S(p/4) + S_ℬ), where
S(x) := Σ_{m≤x, 2|m} χ(m)2^{ω(m)}/φ(m) and S_ℬ := Σ_{(u,B)∈ℬ} χ(u)χ(B)/(φ(u)φ(B)).
*Proof.* On 𝒫(p) exactly one of u, B is even and gcd(u, B) = 1; if B = 2^k B′ (k ≥ 1, B′ odd) then
φ(4uB) = 2^{k+1}φ(u)φ(B′) = 4φ(u)φ(B) (symmetrically if u is even). Also (4u − 1)(4B − 1) ≤ 4p + 1 gives u, B ≤ (p + 1)/3 < p,
and (−uB/p) = σχ(u)χ(B). On 𝒫_bulk the coprime ordered factorisations m = uB of an even m ≤ p/4 are exactly its 2^{ω(m)}
splittings (each has u + B odd), with φ(u)φ(B) = φ(m), χ(u)χ(B) = χ(m); and every pair with 4uB ≤ p is in 𝒫(p). ∎

**Lemma 2.2 (the Dirichlet series; exact).** Let f(m) := 1[2|m]·2^{ω(m)}·m/φ(m). Then f = h ∗ τ (Dirichlet convolution), where
h(d) = h₂(v₂(d))·∏_{ℓ^k ‖ d, ℓ odd} h_ℓ(k) with h₂(0) = 0, h₂(1) = 4, h₂(2) = −4, h₂(k) = 0 (k ≥ 3); h_ℓ(0) = 1,
h_ℓ(1) = 2/(ℓ − 1), h_ℓ(2) = −(ℓ + 1)/(ℓ − 1), h_ℓ(k) = 0 (k ≥ 3). Consequently Σ_m χ(m)f(m)m^{−s} = L(s, χ)²H(s, χ) with
H(s, χ) = Σ_d h(d)χ(d)d^{−s} absolutely convergent for Re s > 1/2, and **H(1, χ) = Σ_d h(d)χ(d)/d = E(χ)** of §1.1.
*Proof.* f, τ and h are of product form F(m) = ∏_ℓ F_ℓ(v_ℓ(m)) (with f₂(0) = h₂(0) = 0 allowed), and the convolution of
product-form functions is of product form with local convolutions, so it suffices to compare local power series. At 2:
Σ_{k≥1} 4Y^k = 4Y/(1 − Y) = (4Y − 4Y²)(1 − Y)^{−2}. At odd ℓ: 1 + (2ℓ/(ℓ − 1))X/(1 − X) = (1 + 2X/(ℓ − 1) − ((ℓ + 1)/(ℓ − 1))X²)(1 − X)^{−2}
(multiply out). Twisting by the completely multiplicative χ preserves the convolution identity. At s = 1 the local factors are
4χ(2)/2 − 4χ(2)²/4 = 2χ(2) − 1 and 1 + 2χ(ℓ)/(ℓ(ℓ − 1)) − χ(ℓ)²(ℓ + 1)/(ℓ²(ℓ − 1)) = e_ℓ(χ(ℓ)). Absolute convergence: the moment
H_θ := Σ_d |h(d)| d^{θ−1} = (4·2^{θ−1} + 4·4^{θ−1})·∏_{ℓ odd}(1 + 2ℓ^{θ−1}/(ℓ − 1) + (ℓ + 1)ℓ^{2θ−2}/(ℓ − 1)) is finite for
θ < 1/2; numerically H_{1/4} = 13.97. Also Σ_{d≤x}|h(d)|d^{−1/2} ≤ (2 + 2√2)∏_{3≤ℓ≤x}(1 + 2/((ℓ−1)√ℓ) + (ℓ+1)/(ℓ(ℓ−1))) ≤ C₁ log x for
x ≥ 10, by Mertens (numerically C₁ = 12.6 suffices up to x = 10⁷ and the ratio converges, ≈ 12.51 there). ∎
(Checked exactly for m ≤ 3000 in `scripts/z52c_bmL_identity_check.py`.)

**Lemma 2.3 (tails of L(1, χ)).** For t ≥ 1: (a) |L − G(t)| ≤ 2P/t; (b) |L − G(t)| ≤ K t^{−1/2} with K := 3C_B p^{3/16} log p;
(c) |L| ≤ 2 + log p.
*Proof.* By periodicity and Σ_{n≤p} χ(n) = 0, S_χ(v) = S_χ(v − p⌊v/p⌋), so (PV) gives |S_χ(v)| ≤ P and (Bu) gives
|S_χ(v)| ≤ C_B v^{1/2}p^{3/16} log p for all v ≥ 0. Abel summation: L − G(t) = Σ_{n>t} χ(n)/n = −S_χ(t)/t + ∫_t^∞ S_χ(v)v^{−2}dv,
whence (a) and (b) (∫_t^∞ v^{−3/2}dv = 2t^{−1/2}). (c): |G(p)| ≤ 1 + log p and 2P/p = 2 log p/√p < 1 for p ≥ 100. ∎

**Lemma 2.4 (hyperbola; exact).** For y ≥ 1, z := √y, A(y) := Σ_{n≤y} χ(n)τ(n)/n = Σ_{ab≤y} F(a)F(b) satisfies
  A(y) = L² − (L − G(z))² + 2Σ_{a≤z} F(a)(G(y/a) − L),
hence, by Lemma 2.3(b) (y/a ≥ z ≥ 1 for a ≤ z) and Σ_{a≤z} a^{−1/2} ≤ 2z^{1/2}:
  **|A(y) − L²| ≤ K² y^{−1/2} + 4K y^{−1/4}.**
*Proof.* Dirichlet's hyperbola method gives Σ_{ab≤y} F(a)F(b) = 2Σ_{a≤z} F(a)G(y/a) − G(z)²; write G(y/a) = L + (G(y/a) − L)
and 2G(z)L − G(z)² = L² − (L − G(z))². ∎ (Checked numerically at six primes.)

**Proposition 2.5 (bulk).** For x ≥ 10:
  |S(x) − E(χ)L²| ≤ C₁K² x^{−1/2} log x + (4K + L²)·H_{1/4}·x^{−1/4}.
At x = p/4 this is **≤ 12√2·C_B·H_{1/4}·p^{−1/16} log p + O(p^{−1/8}(log p)³)**.
*Proof.* By Lemma 2.2, S(x) = Σ_{m≤x} χ(m)f(m)/m = Σ_{dn≤x} (h(d)χ(d)/d)(τ(n)χ(n)/n) = Σ_{d≤x} (h(d)χ(d)/d)·A(x/d). Subtract
E L² = Σ_d (h(d)χ(d)/d)L²:
  S(x) − EL² = Σ_{d≤x} (h(d)χ(d)/d)(A(x/d) − L²) − L²Σ_{d>x} h(d)χ(d)/d.
Lemma 2.4 with y = x/d bounds the first sum by K²x^{−1/2}Σ_{d≤x}|h(d)|d^{−1/2} + 4Kx^{−1/4}Σ_{d≤x}|h(d)|d^{−3/4}; the tail is
≤ L²x^{−1/4}Σ_{d>x}|h(d)|d^{−3/4}. Use Lemma 2.2's moment bounds. At x = p/4: 4K x^{−1/4} = 12√2 C_B p^{−1/16} log p;
K²x^{−1/2} = 18C_B² p^{−1/8}(log p)²; L²x^{−1/4} ≤ √2(2 + log p)²p^{−1/4} (Lemma 2.3(c)). ∎

**Proposition 2.6 (boundary; Pólya–Vinogradov suffices).** |S_ℬ| ≪ p^{−1/4}(log p)² log log p; explicitly, for every
1 ≤ U ≤ √p/2,
  |S_ℬ| ≤ 31.2·ν·(1 + log p)(log p)(1 + log U)·U/√p + 2ν²(1/(3U) + 3/√p),
and U = p^{1/4}/log p gives the stated order.
*Proof.* ℬ is invariant under (u, B) ↔ (B, u), the summand is symmetric and u ≠ B (u + B odd), so S_ℬ = 2S_ℬ^<, the sum over
u < B. For fixed u, (u, B) ∈ ℬ iff B ∈ J_u := (X_u, X_u + Y_u], X_u := p/(4u), X_u + Y_u := (p + u)/(4u − 1) [4uB > p, resp.
B(4u − 1) ≤ p + u], together with gcd(B, u) = 1 and B ≢ u (mod 2). Here Y_u = (p + 4u²)/(4u(4u − 1)) ≤ p/(12u²) + 1/3, and u < B
≤ (p + u)/(4u − 1) forces 4u² − 2u < p, i.e. u < u₀ := (1 + √(4p + 1))/4. For u ≤ U ≤ √p/2 one has X_u ≥ u, so u < B is automatic.
(i) *Small u ≤ U (cancellation).* For B coprime to u, B/φ(B) = Σ_{e|B} ν_u(e) with ν_u(e) := μ²(e)∏_{ℓ|e, ℓ|u}(−1)∏_{ℓ|e, ℓ∤u}(ℓ − 1)^{−1},
and Σ_{e|B} ν_u(e) = 0 if gcd(B, u) > 1 (a factor 1 − 1). Hence, with ε the required parity of B,
  I(u) := Σ_{B∈J_u, (B,u)=1, B≡ε (2)} χ(B)/φ(B) = Σ_e (ν_u(e)χ(e)/e)·Σ_{n∈J_u/e, en≡ε (2)} χ(n)/n.
The parity condition on n is: none, empty, or n ≡ 0 or 1 (mod 2); n = 2n′ gives (χ(2)/2)Σ_{n′∈J_u/(2e)} χ(n′)/n′ and "n odd" is
the difference of the full and the even sum. For any interval (a, b], Abel summation with |Σ_{a<n≤t} χ(n)| ≤ P gives
|Σ_{a<n≤b} χ(n)/n| ≤ P/b + P(1/a − 1/b) = P/a. So the inner sum is ≤ P e/X_u + ½·P·2e/X_u = 2Pe/X_u in absolute value, and
  |I(u)| ≤ (2P/X_u)·Σ_{e ≤ p} |ν_u(e)| ≤ (2P/X_u)·2^{ω(u)}·1.95(1 + log p) = 15.6·2^{ω(u)}(1 + log p)·u·P/p,
using Σ_{e≤Z} |ν_u(e)| ≤ 2^{ω(u)}Σ_{e₁≤Z} μ²(e₁)/φ(e₁) and Σ_{n≤Z} μ²(n)/φ(n) ≤ Σ_d μ²(d)/(dφ(d))·Σ_{m≤Z} 1/m ≤
(ζ(2)ζ(3)/ζ(6))(1 + log Z) (from n/φ(n) = Σ_{d|n} μ²(d)/φ(d)). Summing with weight 1/φ(u) ≤ ν/u and Σ_{u≤U} 2^{ω(u)} ≤ U(1 + log U):
Σ_{u≤U} |I(u)|/φ(u) ≤ 15.6ν(1 + log p)(log p)(1 + log U)U/√p.
(ii) *Large u ∈ (U, u₀) (trivial).* Every admissible B exceeds X_u, so 1/φ(B) ≤ ν/X_u = 4νu/p, and there are ≤ Y_u + 1 of them:
the u-term is ≤ (ν/u)(p/(12u²) + 4/3)(4νu/p) = ν²(1/(3u²) + 16/(3p)); summed over U < u < u₀ ≤ √p/2 + 1/2 this is
≤ ν²(1/(3U) + 3/√p). Double for S_ℬ = 2S_ℬ^<. ∎

**Proof of Theorem A.** T(p) − (σ/4)EL² = (σ/4)[(S(p/4) − EL²) + S_ℬ] (Lemma 2.1); Propositions 2.5 and 2.6 bound the brackets by
O(p^{−1/16} log p) and O(p^{−1/4}(log p)² log log p). Every constant is absolute and effective (C_B, H_{1/4}, C₁, ζ-values). ∎

**Conditional sharpening (CONDITIONAL on GRH for L(s, χ_p)).** GRH implies the Lindelöf bound for L(s, χ) and hence
S_χ(v) ≪_ε v^{1/2}p^ε for all v (standard: Perron's formula shifted to Re s = 1/2 + ε). Then Lemma 2.3(b) holds with K ≪_ε p^ε,
Proposition 2.5 gives O_ε(p^{−1/4+ε}), and the argument of 2.6(i) with |Σ_{a<n≤b}χ(n)| ≪ (b − a + 1)^{1/2}p^ε for all u ≤ u₀ gives
O_ε(p^{−1/2+ε}) for the boundary. So **under GRH, T(p) = (σ/4)E L² + O_ε(p^{−1/4+ε})**. (The observed size p^{−1/2}(log p)^{3/2},
§1.3, would need square-root cancellation in the bulk hyperbola terms beyond termwise bounds.)

**Where the Pass-1 sketch was imprecise (and what changed).** (1) No truncation d ≤ p^ε is needed: Lemma 2.4's bound is
uniform in y ≥ 1 and the d-sum converges against it (H_{1/4} < ∞). (2) The boundary does **not** need Burgess: Pólya–Vinogradov
with the cut at U ≈ p^{1/4} suffices (the sketch's cut at p^{3/8} with Burgess is also valid). Burgess is genuinely needed in
the bulk: with (PV) alone, Lemma 2.4's error is 2Σ_{a≤z}(1/a)(2Pa/y) ≈ 4P/√y ≈ 8 log p at y ≈ p/4 — not small, because the
hyperbola sums G(y/a) at lengths down to √y ≈ √p/2 < √p. (3) The sketch's "o(1)" is in fact a power saving p^{−1/16}
with an absolute effective constant (no Siegel-type ineffectivity: only upper bounds on character sums are used).

## 3. Consequences
(TODO)

## 4. Novelty
(TODO)

## 5. Review log
(TODO)

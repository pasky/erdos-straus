# Z56_K4BILIN — Type II / bilinear attack on K(4) = P(4,15)

**ES is OPEN.** Nothing here proves or disproves it. All results are internal (internally reviewed only).
Lane K4BILIN (wave z56). Scripts `scripts/z56_k4bilin_*`, data `data/z56/k4bilin/`. **Status: CHECKPOINT 1 (skeleton).**

Notation (as in `Z54_HCKILL.md`, `Z55_P415.md`): 𝒬 = {primes ≡ 3 (mod 4)}; S = {n ≥ 1 : every prime factor ≡ 1 (mod 4)};
χ = χ₋₄; r(N) = #{(a, b) ∈ ℤ² : a² + b² = N}; N₁ = n + 4, N₂ = 4n + 1 (so 4N₁ − N₂ = 15).

## 0. Statements attacked

* **P(4,15)** (OPEN; = K(4) by HCKILL Lemma 1.1): infinitely many primes p ≡ 1 (8) with p + 4, 4p + 1 ∈ S.
* **Route D (dense sequence, prime detection by Type I + Type II).** Put n₀ = 97, so n ≡ n₀ (mod 120) gives n ≡ 1 (8)
  and (N₁N₂, 30) = 1, and
    a_n := r(n + 4)·r(4n + 1)·1[n ≡ n₀ (mod 120)]   (n ≥ 1),   A_d(x) := Σ_{n ≤ x, d | n} a_n.
  a_n ≥ 0 has mean ≍ 1. P(4,15) follows from Σ_{p ≤ x} a_p ≫ x/log x plus a cheap 𝒬-square sieve (Lemma R, §1). Prime
  detection in (a_n) needs Type I (A_d) and Type II (Σ α_m β_n a_{mn}) information. **Attack:** prove the Type I side,
  identify the exact Type II estimate that is missing, and test whether it is plausible (falsifiers).
* **Route P (prime variable; bilinear = dispersion for primes in APs).** HCKILL Thm E / FI 2009 / P415 §2: the exact
  problem is a *level* problem (it is solved under EH(θ₀), θ₀ < 1). Bilinear (dispersion) technology is the only known
  source of level > 1/2. **Attack:** compute the level actually needed by the best architecture (FI's: one shift exact
  through r = 4(1 ∗ χ), the other by the semi-linear sieve + switching), and compare with what dispersion delivers for
  the residue structure p ≡ −4 (k), 4p ≡ −1 (d).

**Why not closed.** P415 proved Theorem U (one exact shift + bounded Ω_𝒬 in the other) and a level ledger for the
vector / product-linear sieves (≈ 1.22, ≈ 0.996); it did not treat (a) the dense-sequence formulation with its own
Type I/II information, (b) the FI architecture's threshold, (c) the actual bilinear inputs (Type II for a_n; dispersion
with factor-dependent residues). Nothing here is in FRONTIER §6 or the closed list.

## 1. First lemma (CHECKPOINT): Type I level x^{1/6} for (a_n)

**Lemma T (PROVED relative to FI 2009 Lemma 4.1 = Smith's theorem for r in APs).** For squarefree d with (d, 30) = 1,
  A_d(x) = g(d)·X + r_d(x),   X = c₀ x,   g(d) = d⁻¹ ∏_{ℓ | d} (ℓ − χ(ℓ))/(ℓ + χ(ℓ)),
  |r_d(x)| ≪_ε d^{−1/2} x^{11/12 + ε} + x^{1/2 + ε},
with an absolute c₀ > 0. Hence Σ_{d ≤ D} μ²(d)|r_d(x)| ≪ x^{1 − ε} for D = x^{1/6 − 3ε}: level of distribution x^{1/6−ε}.
(This is the det-15 analogue of FI 2009 Lemma 4.2, with the d^{−1/2} refinement also used by Sedunova arXiv:2609.28200
Lemma 2 for det 1.) Proof: §2.

**First falsifier (planned, §5):** the bilinear hypothesis (B) of Friedlander–Iwaniec's asymptotic sieve for (a_n)
(Möbius cancellation in Σ_m |Σ_{n∼N} μ(mn) a_{mn}|), tested numerically against Selberg's parity sequence (1 + λ(n))/2
(where (B) fails) and the odd-square control. A visible failure would kill Route D.

## 2–8. (to be written)

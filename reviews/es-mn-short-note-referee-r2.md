# Referee report R104 — density-transition section of `paper/es-mn-short-note.tex` (O104)

Hostile referee, round 2 (new §8 "The density transition", changed abstract / intro / open problems).
Source compared: `EXCEPTIONAL_MN2.md` + `reviews/exceptional-mn2-review-{A,B}.md`; ET = Elsholtz–Tao
arXiv:1107.1010 (`sources/elsholtz-tao-1107.1010.pdf`); PW = Pomerance–Weingartner arXiv:2511.16817v2.
From-scratch checks: `scripts/review_r104_*.py`.

(Work in progress — sections are added claim by claim.)

## 1. Upper side (Lemma 8.1 reduced model, Lemma 8.2 multiplicities, Thm 8.3, Thm U)

**Verdict: SOUND.** Statement and label of Theorem U match MN2 Thm U exactly (for every ε an
ineffective A_ε, all m ≥ 4, all N with log N ≥ A_ε m^{1/3}); no strengthening. Re-derived:

* Bonferroni: for even r, Q_r(h) = C(h−1, r) for h ≥ 1, so 1_{h=0} ≤ Q_r(h) ≤ 1_{h=0} + C(h, r+1)
  (C(h−1,r) ≤ C(h,r+1)·(r+1)/h, and C(h−1,r)=0 for h ≤ r). Checked numerically
  (`review_r104_bonf.py`).
* Reduced model: f_c(ℓ) ≤ ℓ−1 (distinct non-zero classes), Bernoulli product, elementary symmetric
  bound e_{r+1}(p) ≤ (Σp)^{r+1}/(r+1)!, Σ f/(ℓ−1) ≤ 2μ_c with μ_c = Σ f_c(ℓ)/ℓ exactly as in
  Cor 5.2; (2eC_u s/(r+1))^{r+1} ≤ e^{−(r+1)} iff r+1 ≥ 2e²C_u s. ✓.
  Cor 5.2's lower bound a_u t³/m is for (c, L_K)=1, which is exactly the reduced fibre. ✓
* Main term identity: q_B | 𝓜' (lcm k_A | L_K), a_B a unit, so P(ñ ≡ a_B (q_B)) = 1/φ(q_B). ✓
  Exceptional primes p ∈ (N/2, N]: p > X > K, so p is a unit mod 𝓜', and Lemma 3.3(1) has no
  hypothesis besides n ≥ 1. ✓
* Moduli: (1+κ)(2e²C_u s+2)(sm)^{1/3} ≤ 0.45 C_1^{-1}… uses s ≥ 1 (2 ≤ 2s) and s·(sm)^{1/3} =
  s^{4/3}m^{1/3}. ✓ t ≤ L. ✓
* Lemma 8.2: Shiu Thm 1 (F = τ⁴, F(p)=16, interval (kx,2kx] of length y = kx, modulus k ≤ y^{1−β})
  gives (kx/φ(k))·(log)^{−1}·exp(16 Σ1/p) ≍ (k/φ(k)) x t^{15}; the restriction to prime ℓ is by
  positivity. Dyadic sum: ≪ t · log t · t^{15} ≤ t^{17}. Euler product exponent 4^r. ✓
  (Needs κ ≤ 1/4 for "X^{1/2} ≥ k²"; κ = 1/480 in §2.1. ✓)
* Cauchy–Schwarz: N (C S_2 L^{−1−A'})^{1/2} = C'(r) N L^{−3} for A' = 17r+4^r+5 and t ≤ L. ✓

Minor points: see defects m1, m2 below.

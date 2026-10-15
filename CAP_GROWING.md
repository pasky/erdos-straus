# CAP_GROWING — bounded cap with a growing mute set (R200 M1), PM-II and SQ_± on average (task O229, wave Z-e)

Status: in progress (O229). **ES is not solved here, nor any infinite case of ES.** Labels as in DISCOVERIES.md.
Builds on EXPONENT_CAP (Def 1.1, Prop 1.2, Prop 3.1), GROWING_MUTE, CAP_TWO, PHASE_DIAGRAM, MARKOFF_ES §6,
BRIDGE_WORLDS §5 (PM-II), SYNTHESIS_SPARKS4 §2 (SQ_±), paper/vaughan-loglog-note.tex. Scripts `scripts/z5_*`,
outputs `data/z5/`.

## 0. Iteration log

(Z1) Goal 1 head-on (pointwise ES^{(y,e)}, e bounded, S growing). Every reformulation I tried (symmetric
divisibility 2ABD | nA² + B² + D; "m | nq² + 4, m ≡ −n mod 4 rad q"; polynomial families at fixed n via Capelli;
Pell unit of ℚ(√n)) lands on the known two layers: (i) a fibre/class-group layer (MARKOFF_ES §6, CAP_TWO §6) and
(ii) an (e+1)-free layer on a binary recurrence (Wieferich-type). Barrier hypotheses violated: B3 (no archimedean
wall ⇒ infinite main term) and B2 (no fixed slice set) — but neither violation supplies existence. Pointwise: no proof.
(Z2) Steering: the hypothesis B6 ("averages over n say nothing pointwise") is the one a growing-S argument CAN use
honestly — on average over n the cap e is a *dimension* parameter. Modification: ask how the exceptional set of
ES^{(y,e)} shrinks with e. Result (§1): Vaughan's exponent 2/3 becomes (e+1)/(e+2) — the cap is a sieve-dimension
knob, interpolating between Vaughan (e = 1) and the pointwise theorem ES^{(y)} (e = ∞).
(Z3) PM-II: Vaughan's classes are prime-modulus Type II certificates, so PM-II inherits Vaughan's bound (§2).
(Z4) SQ_±: its prime-modulus classes number only ≍ τ(ℓ²−1) per ℓ, so the same machinery gives exponent 1/2 —
the "easier" signed twin is *provably harder on average* by this method (§3).

## 1. Goal 1 on average: the cap e is a sieve-dimension knob

Setting (EXPONENT_CAP Def 1.1, Prop 1.2). For a prime ℓ ≡ 3 (mod 4) put K := (ℓ+1)/4; for odd Q put
Q^{(e)} := ∏_{s|Q} s^{max(1, v_s(Q) − e)}. A *cap-e shot at ℓ* is an odd Q with **Q^{(e)} | K** (⟺ rad Q | K and
v_s(Q) ≤ v_s(K) + e); by Prop 1.2, if n is odd, gcd(Q, n) = 1 and **n ≡ −4Q² (mod ℓ)**, the shot solution is an
ES^{(y,e)}(n) solution (den z = Q₁², v_s(Q₁) ≤ e, rad Q₁ | y). Let ω_e(ℓ) := #{cap-e shots Q < ℓ/2 at ℓ}; these
give ω_e(ℓ) *distinct* classes −4Q² mod ℓ (Q² ≡ Q'² with Q, Q' < ℓ/2 forces Q = Q'). The mute set S = rad Q₁ is
unrestricted (grows with n), the cap e is fixed: this is exactly R200 M1's regime.

**Lemma 1.1 (class mass; PROVED relative to Bombieri–Vinogradov).** For fixed e ≥ 0 and X ≥ X₀(e),
`  S_e(X) := Σ_{X^{1/2} < ℓ ≤ X, ℓ ≡ 3 (4)} ω_e(ℓ)/ℓ  ≥  c_e (log X)^{e+1},   c_e > 0.`
*Proof.* For ℓ > X^{1/2}, every odd Q ≤ X^{1/5} with Q^{(e)} | K is counted, so
S_e(X) ≥ Σ_{R odd ≤ X^{1/5}} h(R) Σ_{X^{1/2}<ℓ≤X, ℓ ≡ −1 (4R)} 1/ℓ, h(R) := #{Q odd ≤ X^{1/5} : Q^{(e)} = R}
(ℓ ≡ −1 mod 4R gives ℓ ≡ 3 mod 4). The moduli 4R ≤ 4X^{1/5} lie below y^{1/2}(log y)^{−B} for y ∈ [X^{1/2}, X], and
h(R) ≤ (e+1)^{ω(R)} ≤ τ(R)^{log₂(e+1)}; Bombieri–Vinogradov with divisor-bounded weights (Cauchy–Schwarz against the
Brun–Titchmarsh bound, as in paper/vaughan-loglog-note §4) and partial summation give
Σ_{ℓ ∈ (X^{1/2}, X], ℓ ≡ −1 (4R)} 1/ℓ = (log 2)/φ(4R) + E_R with Σ_R h(R)|E_R| ≪_e 1. Hence
S_e(X) ≥ (log 2)·½·Σ_{Q odd ≤ X^{1/5}} 1/φ(Q^{(e)}) − O_e(1). Restrict to Q = r₁r₂²⋯r_{e+1}^{e+1} with r_j odd,
squarefree, pairwise coprime, r_j ≤ Z := X^{2/(5(e+1)(e+2))}; then Q ≤ X^{1/5}, Q^{(e)} = r₁⋯r_{e+1} =: m and
1/φ(m) ≥ 1/m. Each odd squarefree m ≤ Z arises from (e+1)^{ω(m)} ordered splittings (all r_j ≤ m ≤ Z), so the sum is
≥ Σ_{m ≤ Z odd} μ²(m)(e+1)^{ω(m)}/m ≫_e (log Z)^{e+1} ≫_e (log X)^{e+1}. ∎
*Numerics (EVIDENCE, `scripts/z5_cap_classes.py 2000000 3 200`, all ℓ ≤ X, no X^{1/2} cut):*
`  X = 2^10: S0, S1, S2, S3 = 1.92, 2.33, 2.49, 2.56    X = 2^20: 4.10, 6.36, 7.85, 8.77    X = 2·10^6: 4.30, 6.82, 8.52, 9.59`
S₀/log X = 0.277 → 0.296 (flat); S₁ fits 0.018 L² + 0.21 L (L = log X) — the asymptotic order is reached slowly (the
constants c_e are small: the shots carry a (1/φ)-weight per prime of K). 140 random shots (e = 3) re-verified with exact
rationals and Def 1.1 prime by prime.

**Theorem 1.2 (ES^{(y,e)} with bounded cap and free mute set holds for almost all primes, with exponent
(e+1)/(e+2); PROVED relative to Bombieri–Vinogradov and Montgomery's large sieve).** For every e ≥ 0 there is
c_e > 0 such that
`  #{p ≤ N prime : ES^{(y,e)}(p) has no solution}  ≪_e  N·exp(−c_e (log N)^{(e+1)/(e+2)}).`
*Proof.* Let 𝒩 be the set of exceptional primes in (X, N], X := exp(C(log N)^{1/(e+2)}). A prime p ∈ 𝒩 avoids every
class −4Q² (mod ℓ) of Lemma 1.1 for X^{1/2} < ℓ ≤ X (gcd(Q, p) = 1 as Q < ℓ/2 < p, and the class is nonzero). Montgomery's
large sieve with sieving level N^{1/2}: |𝒩| ≤ 2N/L, L ≥ Σ_q μ²(q)∏_{ℓ|q} ω_e(ℓ)/ℓ over q = product of k distinct
primes of (X^{1/2}, X], k := ⌊log N/(2 log X)⌋. By the multinomial bound,
L ≥ (S^k − (k choose 2) S^{k−2} T)/k! with S = S_e(X), T = Σ_ℓ (ω_e(ℓ)/ℓ)² ≪ X^{−1/2+o(1)}, so L ≥ S^k/(2·k!) ≥ (eS/k)^k/(2e√k).
With S ≥ c_e(log X)^{e+1} = c_e C^{e+1}(log N)^{(e+1)/(e+2)} and k ≍ (log N)^{(e+1)/(e+2)}/(2C), choose C with
e·S/k ≥ e², giving L ≥ exp(k) and |𝒩| ≪ N exp(−c_e'(log N)^{(e+1)/(e+2)}); primes ≤ X are negligible. ∎
*Calibration.*
* e = 0 (ES itself, shot family only = the d = 1 slice of Type II): exponent 1/2. Vaughan's 2/3 uses the full
  Type II cube (classes −4c²d, cd | K, τ₃(K) of them); e = 1 already matches 2/3 **with the d = 1 slice alone**, and
  e ≥ 2 beats Vaughan (and the loglog note): ES^{(y,2)}: 3/4, ES^{(y,3)}: 4/5, …
* (Assessment, not proved.) Combining the cap with Vaughan's d-dimension should give (e+2)/(e+3). Uniformity in e is
  not tracked (c_e decays like ((e+1)(e+2))^{−e}), so letting e → ∞ with N is not covered; e = ∞ with FIXED S is the
  pointwise theorem ES^{(y)} (FROBENIUS_FIRING Thm 4.2), and PHASE_DIAGRAM Thm 5.1 is the pointwise sub-polynomial cap.
* T1: odd squares avoid every class (−4Q² is a non-residue mod ℓ ≡ 3 (4)); the exceptional set contains them, and the
  bound is consistent with √N squares.
* Barrier screen: this is a B6 statement (average over p) and makes no pointwise claim. What it shows is that R200 M1's
  regime (bounded e, unbounded S) differs from ES on average *quantitatively*: the cap raises the sieve dimension from
  log² to log^{e+1}. By the large sieve's own ceiling (Σ_{q≤N^{1/2}} ∏ω/ℓ with ω ≤ (log ℓ)^{O(1)} is
  exp(O((log N)^{1−δ}))) no fixed cap gives power saving by this method.

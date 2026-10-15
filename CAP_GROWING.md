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

## 2. PM-II on average (goal 2)

**Lemma 2.1 (Vaughan's classes are prime-modulus Type II certificates; PROVED, elementary).** Let ℓ ≡ 3 (mod 4) be
prime, (ℓ+1)/4 = uvw. If n ≡ −u v^{−1} (mod ℓ) then n ≡ −4u²w (mod ℓ), i.e. ℓ | n + 4c²d with (c, d) = (u, w) and
4cd = 4uw | ℓ + 1: a Type II certificate with PRIME modulus h = ℓ (BRIDGE_WORLDS §5 notation).
*Proof.* 4uvw ≡ 1 (mod ℓ) gives v^{−1} ≡ 4uw. ∎
**Corollary 2.2 (PM-II for almost all primes; PROVED relative to Vaughan 1970 / Pomerance–Weingartner Thm 1.3).**
`  #{p ≤ N prime : p has no prime-modulus Type II certificate} ≪ N exp(−c (log N)^{2/3}).`
*Proof.* Vaughan's large sieve (as described in paper/vaughan-loglog-note.tex §1: classes −uv^{−1} mod primes
ℓ ≡ 3 (4), multiplier k = 1) uses only the classes of Lemma 2.1; an exceptional prime p > X avoids all of them. ∎
*Remarks.* (i) The loglog improvement of the note does NOT transfer: it uses the composite moduli kℓ. (ii) PM-II is
trivial for p ≡ 3 (mod 4) and for p ≡ 2 (mod 3) (h = 3, c = d = 1); the classes at h = 7 ((c,d) ∈ {(1,1),(1,2),(2,1)},
classes 3, 6, 5) are exactly the non-residues mod 7, so **a PM-II failure is ≡ 1 (mod 12) and a QR mod 7** (3361 ≡ 1 mod 84
and 3361 ≡ 1 mod 5, 7 as well). Among primes h ≡ 3 (mod 4) ≤ 20 000 only h = 3, 7 have
covering class sets (`scripts/z5_pm_cover.py 20000`; CERTIFIED in that range), and for large h the τ₃((h+1)/4) = h^{o(1)}
classes cannot cover the (h−1)/2 non-residues — no further covering (B1). (iii) A pointwise PM-II would give Type II-ES at every p ≠ 3361: B2/B3 apply
verbatim (BRIDGE_WORLDS §5); nothing here addresses that.

## 3. SQ_± on average, its prime-modulus core, and a calibration (goal 3)

Notation of SYNTHESIS_SPARKS4 §2: words (t, u, v), tuv − u − v = n, A = tu − 1, χ = (−A/n); n ≡ 1 (mod 8) is the
content (Prop 2.1(c) there handles n ≢ 1 mod 8).

**Lemma 3.1 (prime-modulus words; PROVED, elementary).** Let n ≡ 1 (mod 4), ℓ an odd prime, u ∈ ℤ∖{0, −n}. There is
a word with A = ±ℓ and this u iff ℓ | n + u and u | ℓ + 1 (A = ℓ) or u | ℓ − 1 (A = −ℓ); then
**χ = (n/ℓ) = (−u/ℓ)**. Hence such a word with χ = −1 exists iff for some prime ℓ with **(n/ℓ) = −1**, the residue
n mod ℓ lies in R(ℓ) := {−u mod ℓ : u ∈ ±div(ℓ+1) ∪ ±div(ℓ−1)}.
*Proof.* v = (n + u)/A and t = (A + 1)/u must be nonzero integers; χ = (−A/n) = (±ℓ/n) = (ℓ/n) = (n/ℓ) by Jacobi
reciprocity (n ≡ 1 mod 4, (−1/n) = 1), and n ≡ −u (mod ℓ). ∎
So the prime-modulus layer of SQ_± fires at ℓ on ω_±(ℓ) := #{r ∈ R(ℓ) : (r/ℓ) = −1} ≤ 2(τ(ℓ+1) + τ(ℓ−1)) classes;
note the **free** genus filter: any prime with (n/ℓ) = −1 converts every hit n ≡ −u into a χ = −1 word.
For |u| ∈ {1, 2, 3, 4, 6} the condition u | ℓ ± 1 is automatic, giving additive-shift slots "n + u has a prime factor
ℓ with ψ_u(ℓ) := (−u/ℓ) = −1" (u = 1: ℓ ≡ 3 mod 4; ±2: (∓2/ℓ) = −1; u = −1, −4 never) — the shift-dual of the
|t|n ± 1 slot table.

**Proposition 3.2 (SQ_± almost always, exponent 1/2; PROVED relative to Montgomery's large sieve and the
Titchmarsh divisor bound).** #{n ≤ N : n ≡ 1 (8), no prime-modulus χ = −1 word} ≪ N exp(−c (log N)^{1/2}).
*Proof.* As Thm 1.2 with a = 1: Σ_{X^{1/2}<ℓ≤X} ω_±(ℓ)/ℓ ≫ log X (already the class u = 1 for ℓ ≡ 3 (4) together with
u = 2, ±3, 4, ±6 gives ≫ 1 per dyadic block of log ℓ; the class count of R(ℓ) is ≥ 1 for every ℓ ≥ 5), and
ω_±(ℓ) ≪ τ(ℓ²−1). ∎
*Calibration (Assessment).* SQ_± is "empirically far easier" than ES-five (SYNTHESIS_SPARKS4 §2.5), yet its
prime-modulus class mass is only Σω_±/ℓ ≍ log X (measured: 1.95·log N at N = 10⁵, 2.06·log N at 10⁶), against
(log X)² for Vaughan's ES classes. So **by the large-sieve method the signed twin is provably HARDER on average
(exponent 1/2 < 2/3)**: its ease is pointwise (many cheap genus slots with Landau-type failure probability), not a
richer class structure. A lottery-breaker tested on SQ_± (SPARKS4 steering rule) should therefore not be expected to
transfer its *average* strength to ES, nor conversely.

**CONJECTURE PM-SQ_± (EVIDENCE).** Every non-square n ≡ 1 (mod 8) has a word with A = ±(prime) and χ = −1.
* `scripts/z5_sqpm_prime.py 1000000`: **0 exceptions among all non-squares n ≡ 1 (8) ≤ 10⁶**; 0 odd squares marked (T1).
* `scripts/z5_sqpm_verify.py` (independent direct search + exact identity tuv − u − v = n, Jacobi symbol): 300 random
  n ≤ 10⁶ (max |u| needed 10), 100 random n ≤ 10¹¹ (max |u| 3).
* Adversarial (`scripts/z5_sqpm_adversarial.py Q 20 300`): n ≡ 1 (mod 8∏_{3≤q≤Q} q) — every small prime has
  (n/q) = +1 and cannot fire — Q = 13, 23, 31 (n up to ≈ 1.6·10¹³): min 10, 11, 21 tickets with |u| ≤ 300, least |u| ≤ 8.
  Contrast PM-II (exception 3361, stacked residues kill its small-h tickets): here the tickets come from LARGE prime
  factors of n + u with |u| tiny, which stacking cannot touch.
* Heuristic (Assessment): expected tickets ≈ 2 log n (Poisson failure ≈ n^{−2}, summable), so finitely many exceptions
  are expected; the slots |u| ≤ 6 alone fail with probability ≍ (log n)^{−9/2}. As for the t-slots (SPARKS4 §2.4), no
  finite u-set should suffice (Dickson-type construction; not carried out here).

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
ES^{(y,e)} shrinks with e. Result (§1): Vaughan's exponent 2/3 becomes (e+2)/(e+3) (overflow certificate cube, Prop 1.3/Thm 1.4;
shots alone give (e+1)/(e+2)) — the cap is a sieve-dimension knob, from Vaughan (e = 0) towards the pointwise
theorem ES^{(y)} (e = ∞, fixed S).
(Z3) PM-II: Vaughan's classes are prime-modulus Type II certificates, so PM-II inherits Vaughan's bound (§2).
(Z4) SQ_±: its prime-modulus classes number only ≍ τ(ℓ²−1) per ℓ, so the same machinery gives exponent 1/2 —
the "easier" signed twin gets a *weaker exponent* from this method (§3; (R230 repair D6): a statement about the method's
prime-modulus layer, not a proof that SQ_± is harder on average).

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
  e ≥ 2 beats Vaughan (and the loglog note): ES^{(y,2)}: 3/4, ES^{(y,3)}: 4/5, … ((R230 repair D1): the campaign's
  own ES record is already 3/4 — paper/es-threequarter-note, composite multiplier moduli — so the comparison with
  Vaughan is a comparison within the prime-modulus large-sieve architecture only.)
* Combining the cap with Vaughan's d-dimension gives (e+2)/(e+3): this is Thm 1.4 below ((R230 repair D9)). Uniformity in e is
  not tracked (c_e decays like ((e+1)(e+2))^{−e}), so letting e → ∞ with N is not covered; e = ∞ with FIXED S is the
  pointwise theorem ES^{(y)} (FROBENIUS_FIRING Thm 4.2), and PHASE_DIAGRAM Thm 5.1 is the pointwise sub-polynomial cap.
* T1: odd squares avoid every class (−4Q² is a non-residue mod ℓ ≡ 3 (4)); the exceptional set contains them, and the
  bound is consistent with √N squares.
* Barrier screen: this is a B6 statement (average over p) and makes no pointwise claim. What it shows is that R200 M1's
  regime (bounded e, unbounded S) differs from ES on average *quantitatively*: the cap raises the sieve dimension from
  log² to log^{e+1}. By the large sieve's own ceiling (Σ_{q≤N^{1/2}} ∏ω/ℓ with Σ_{ℓ≤y} ω(ℓ)/ℓ ≪ (log y)^A is
  exp(O((log N)^{A/(A+1)})) by Rankin's trick; (R230 repair D9): the hypothesis is on average, ω itself is not
  pointwise (log ℓ)^{O(1)}) no fixed cap gives power saving by this method.

## 2. PM-II on average (goal 2)

**Lemma 2.1 (Vaughan's classes are prime-modulus Type II certificates; PROVED, elementary).** Let ℓ ≡ 3 (mod 4) be
prime, (ℓ+1)/4 = uvw. If n ≡ −u v^{−1} (mod ℓ) then n ≡ −4u²w (mod ℓ), i.e. ℓ | n + 4c²d with (c, d) = (u, w) and
4cd = 4uw | ℓ + 1: a Type II certificate with PRIME modulus h = ℓ (BRIDGE_WORLDS §5 notation).
*Proof.* 4uvw ≡ 1 (mod ℓ) gives v^{−1} ≡ 4uw. ∎
**Corollary 2.2 (PM-II for almost all primes; PROVED relative to Bombieri–Vinogradov and Montgomery's large sieve, as the case e = 0 of Thm 1.4; (R230 repair D3)).**
`  #{p ≤ N prime : p has no prime-modulus Type II certificate} ≪ N exp(−c (log N)^{2/3}).`
*Proof.* (R230 repair D3.) Thm 1.4 with e = 0: R = 1, the classes −4c₀²d₀ mod ℓ come from Prop 1.3 with R = 1, i.e.
the cube lemma at the PRIME modulus ℓ — PM-II certificates; an exceptional prime p > X avoids all of them. Consistent
with Vaughan's large sieve (paper/vaughan-loglog-note.tex §1: classes −uv^{−1} mod primes ℓ ≡ 3 (4), multiplier k = 1,
which are PM-II by Lemma 2.1) and PW Thm 1.3 (m = 4); Vaughan 1970 itself was not accessible
(sources/vaughan-1970-access-log.md). ∎
*Remarks.* (i) The loglog improvement of the note does NOT transfer: it uses the composite moduli kℓ. (ii) PM-II is
trivial for p ≡ 3 (mod 4) and for p ≡ 2 (mod 3) (h = 3, c = d = 1); the classes at h = 7 ((c,d) ∈ {(1,1),(1,2),(2,1)},
classes 3, 6, 5) are exactly the non-residues mod 7, so **a PM-II failure is ≡ 1 (mod 12) and a QR mod 7** (3361 ≡ 1 mod 84
and 3361 ≡ 1 mod 5, 7 as well). Among primes h ≡ 3 (mod 4) ≤ 20 000 only h = 3, 7 have
covering class sets (`scripts/z5_pm_cover.py 20000`; CERTIFIED in that range), and for large h the τ₃((h+1)/4) = h^{o(1)}
classes cannot cover the (h−1)/2 non-residues — no further covering (B1). (R230 repair D4: PROVED for all h — the class
count is ≤ τ₃(K) ≤ τ(K)² ≤ (3.5273·K^{1/3})² < 2K − 1 for K > 241, and τ₃(K) ≥ 2K − 1 for K ≤ 242 only at K = 1, 2;
`scripts/review_r230_pmcover.py`.) (iii) A pointwise PM-II would give Type II-ES at every p ≠ 3361: B2/B3 apply
verbatim (BRIDGE_WORLDS §5); nothing here addresses that.

## 3. SQ_± on average, its prime-modulus core, and a calibration (goal 3)

Notation of SYNTHESIS_SPARKS4 §2: words (t, u, v), tuv − u − v = n, A = tu − 1, χ = (−A/n); n ≡ 1 (mod 8) is the
content (Prop 2.1(c) there handles n ≢ 1 mod 8).

**Lemma 3.1 (prime-modulus words; PROVED, elementary).** Let n ≡ 1 (mod 4), ℓ an odd prime, u ∈ ℤ∖{0, −n}. There is
a word with A = ±ℓ and this u iff ℓ | n + u and u | ℓ + 1 (A = ℓ) or u | ℓ − 1 (A = −ℓ); then
**χ = (n/ℓ) = (−u/ℓ)**. Hence such a word with χ = −1 exists iff for some prime ℓ with **(n/ℓ) = −1**, the residue
n mod ℓ lies in R(ℓ) := {−u mod ℓ : u ∈ ±div(ℓ+1) ∪ ±div(ℓ−1)}. ((R230 repair D7): the excluded u = −n never matters:
it would need ℓ ≡ ±1 (mod n), whence (n/ℓ) = (±1/n) = 1. The search is finite, |u| ≤ n + 1.)
*Proof.* v = (n + u)/A and t = (A + 1)/u must be nonzero integers; χ = (−A/n) = (±ℓ/n) = (ℓ/n) = (n/ℓ) by Jacobi
reciprocity (n ≡ 1 mod 4, (−1/n) = 1), and n ≡ −u (mod ℓ). ∎
So the prime-modulus layer of SQ_± fires at ℓ on ω_±(ℓ) := #{r ∈ R(ℓ) : (r/ℓ) = −1} ≤ 2(τ(ℓ+1) + τ(ℓ−1)) classes;
note the **free** genus filter: any prime with (n/ℓ) = −1 converts every hit n ≡ −u into a χ = −1 word.
For |u| ∈ {1, 2, 3, 4, 6} the condition u | ℓ ± 1 is automatic, giving additive-shift slots "n + u has a prime factor
ℓ with ψ_u(ℓ) := (−u/ℓ) = −1" (u = 1: ℓ ≡ 3 mod 4; ±2: (∓2/ℓ) = −1; u = −1, −4 never) — the shift-dual of the
|t|n ± 1 slot table.

**Proposition 3.2 (SQ_± almost always, exponent 1/2; PROVED relative to Montgomery's large sieve and the
divisor bound; (R230 repair D5)).** #{n ≤ N : n ≡ 1 (8), no prime-modulus χ = −1 word} ≪ N exp(−c (log N)^{1/2}).
*Proof.* As Thm 1.2 with a = 1: Σ_{X^{1/2}<ℓ≤X} ω_±(ℓ)/ℓ ≫ log X and ω_±(ℓ) ≪ τ(ℓ²−1) = ℓ^{o(1)}. (R230 repair D5: a
fixed set of u gives only ≫ 1 here, which is useless.) For ℓ ≡ 3 (4) and odd u | ℓ + 1 (⟺ ℓ ≡ −1 mod 4u) every odd
prime q | u has (q/ℓ) = (ℓ/q)(−1)^{(q−1)/2} = 1, so (−u/ℓ) = −1: each −u is a firing class, and these are distinct for
u < ℓ. Bombieri–Vinogradov as in Lemma 1.1 gives Σ_{u ≤ X^{1/5} odd} (log 2)/φ(4u) − O(1) ≫ log X. ∎
*Calibration (Assessment).* SQ_± is "empirically far easier" than ES-five (SYNTHESIS_SPARKS4 §2.5), yet its
prime-modulus class mass is only Σω_±/ℓ ≍ log X (measured: 1.95·log N at N = 10⁵, 2.06·log N at 10⁶), against
(log X)² for Vaughan's ES classes. So **the prime-modulus large sieve gives the signed twin a weaker exponent
(1/2 < 2/3)** ((R230 repair D6): this compares what one method yields on one layer — A = ±prime; it does not prove
SQ_± harder on average, composite-A words were not sieved, and ES's own record 3/4 uses composite moduli): its ease is pointwise (many cheap genus slots with Landau-type failure probability), not a
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

### 1.2 Upgrade: the certificate cube with overflow — exponent (e+2)/(e+3)

**Proposition 1.3 (overflow cube; PROVED, elementary).** Let ℓ ≡ 3 (mod 4) be prime, K = (ℓ+1)/4 = c₀d₀j, and R odd
with rad R | c₀ and, for every s | R, v_s(c₀) = v_s(K) (so s ∤ d₀j). If p is a prime, p ∤ R and
**p ≡ −4c₀²d₀R² (mod ℓ)**, put E := (p + 4c₀²d₀R²)/ℓ, x := (p + E)/4, y := p·c₀d₀j, z := p·x·j/(c₀R²). Then
4/p = 1/x + 1/y + 1/z with x, y ∈ ℤ_{>0}, **den z = R²**, rad R | y; so it is an ES^{(y,e)}(p) solution as soon as
v_s(R) ≤ e for all s. (R = 1 is FIXED_MODULUS_SHOTS Lemma 1.1, i.e. Vaughan's classes; d₀ = 1, c₀ = Q₀, R = Q₁ is the
shot family — the cube point (c₀R², d₀/R², j) of EXPONENT_CAP Cor 1.4 with d₀ free.)
*Proof.* Lemma 1.1 of FIXED_MODULUS_SHOTS with the rational point (c, d) = (c₀R², d₀/R²): cd = c₀d₀ and c²d = c₀²d₀R²
are integers, ℓ = 4cdj − 1, and its computation (4(x + c²d) = E(ℓ + 1), so x + c₀²d₀R² = E·K; ℓ ≡ −1 and
p + 4c₀²d₀R² ≡ p mod 4c₀d₀ give 4c₀d₀ | p + E) is formal: x ∈ ℤ, c₀ | x, and 1/y + 1/z = (x + c²d)/(p·cdj·x) = E/(px)
= 4/p − 1/x. Valuations: for s ∤ R, v_s(z) ≥ 0 (c₀ | x). For s | R put σ = v_s(K) = v_s(c₀) ≥ 1, ρ = v_s(R) ≥ 1:
s ∤ p and ℓ ≡ −1 (mod s) give v_s(E) = 0, so in x = EK − c₀²d₀R², v_s(EK) = σ < 2σ + 2ρ, hence v_s(x) = σ and
v_s(z) = σ + v_s(j) − v_s(c₀) − 2ρ = −2ρ. So den z = R². ∎
*Check (`scripts/z5_cube_overflow.py 20000 2 0 1`, `… 5000 3 0 2`):* 2 441 (e = 2, ℓ < 2·10⁴) and 753 (e = 3,
ℓ < 5000) random overflow-cube solutions at large primes p re-verified with exact rationals and Def 1.1 prime by prime.

**Theorem 1.4 (supersedes Thm 1.2; PROVED relative to Bombieri–Vinogradov and Montgomery's large sieve).**
`  #{p ≤ N prime : ES^{(y,e)}(p) has no solution}  ≪_e  N·exp(−c_e (log N)^{(e+2)/(e+3)}).`
e = 0 is Vaughan's 2/3; e = 1 gives 3/4, e = 2 gives 4/5. ((R230 repair D1): e = 1 only ties the campaign's internally
proved ES exponent 3/4 (paper/es-threequarter-note); the relaxation exceeds what is known for ES only for e ≥ 2. No
conflict with the 3/4 cap of EXCEPTIONAL_KARY3 Thm 4.1/Cor 4.2: that cap concerns ES-certificate classes, while the
overflow classes with R > 1 certify only ES^{(y,e)}; their mass (log)^{e+2} exceeding the cubic ES mass for e ≥ 2 is the
signature of the relaxation. Overflow + the 3/4 note's multipliers should give (e+3)/(e+4) — Assessment.)
*Proof.* As Thm 1.2, with ω'_e(ℓ) := number of triples (c₀, d₀, R): c₀, d₀ odd squarefree coprime, c₀d₀ | K,
rad R | c₀, v_s(R) ≤ e, s² ∤ K for s | R, and 4c₀²d₀R² < ℓ. The map (c₀, d₀, R) ↦ c₀²d₀R² is injective (d₀ is the
squarefree kernel, c₀R its square root, c₀ = rad(c₀R)), so these give ω'_e(ℓ) distinct classes −4c₀²d₀R² mod ℓ
(Prop 1.3). Class mass: for c₀²d₀R² ≤ X^{1/5}, the primes ℓ ∈ (X^{1/2}, X] with ℓ ≡ −1 (mod 4c₀d₀) and
ℓ ≢ −1 (mod 4s²) for s | R have, by BV with divisor-bounded weights as in Lemma 1.1, reciprocal sum
(log 2)·∏_{s|R}(1 − 1/s)/φ(4c₀d₀) + error (summably small). The Euler factor of Σ ∏_{s|R}(1−1/s)/φ(c₀d₀) at a prime s
is 1 + 1/(s−1) [s | d₀] + 1/(s−1) [s | c₀, s ∤ R] + e(1 − 1/s)/(s−1) [s | c₀, 1 ≤ v_s(R) ≤ e] = 1 + (e+2)/s + O(1/s²), and
the restriction c₀²d₀R² ≤ X^{1/5} keeps a fixed power of log X ((R230 repair D2): restrict to m := c₀d₀ ≤ W := X^{1/(10(e+1))}; then R ≤ c₀^e gives c₀²d₀R² ≤ m^{2e+2} ≤ X^{1/5}, and the
sum is ≥ ½Σ_{m≤W odd} μ²(m)∏_{s|m}(2/(s−1) + e/s) ≥ ½Σ μ²(m)(e+2)^{ω(m)}/m), so
S'_e(X) ≫_e (log X)^{e+2}; the large-sieve step is unchanged with a = e + 2. ∎
*T1.* (−4c₀²d₀R²/ℓ) = −(d₀/ℓ) = −1, since every odd prime q | d₀ divides ℓ + 1 and ℓ ≡ 3 (4) give (q/ℓ) = 1 by
reciprocity (and 2 | d₀ forces ℓ ≡ 7 mod 8): the classes are non-residues, odd squares are never hit.
*Reading.* The cap e adds e dimensions to Vaughan's two (c and d of the Type II cube). ES^{(y,e)} with free mute set
is therefore on average a sieve problem of dimension ≍ (log)^{e+2}; ES itself is the case e = 0 (within the prime-modulus large sieve; (R230 repair D1)). Pointwise nothing
changes (B6).

## 4. Construction attempts for the pointwise e = 2 layer (goal 1; negative, see memos)
* Fixed-field x-orbits (BRAINSTORM/z5_fixed_field_orbits): Δ_x = D₀m_k² along (x₀ + √D₀)ε^k keeps one field, but the
  only elements forced into O_{m_k} have norms ±(16n)^i r² (never −E, E ≡ 3 mod 4: T1 shape), and the ring class
  group ≍ m_k makes the expected hits along an orbit converge. The Cohen–Lenstra luck of MARKOFF_ES §6 lives *across*
  fields; fixing the field destroys it.
* Pell unit of ℚ(√n) (BRAINSTORM/z5_pell_unit_T1): T1-shaped (exists ⟺ n non-square) but acts on an ES^{[2]} fibre
  only if n | λ, which reciprocity forbids; it is a sign-blind (real) tool.
* Polynomial families at fixed n (log Z1): λ constant needs 4λ²nA(s)⁴ + 1 reducible (Capelli), i.e. A(s) − θ reducible
  over ℚ(θ), θ⁴ = −1/(4λ²n); for quadratic A this is a rational point on an n-dependent plane cubic — an n-specific
  lottery, not a mechanism (not pursued).
* The (e+1)-free layer: an ES^{[2]} Pell orbit gives ES^{(y,e)} iff some orbit B is (e+1)-free — k-free values of
  binary recurrences are open for every fixed k (Wieferich-type; Assessment, uncited — and what is needed is ONE
  (e+1)-free orbit element; (R230 repair D8)); abc controls the powerful part, not every exponent.

## 5. Verdict (O229 checkpoint 1)
1. **R200 M1 on average (PROVED rel. BV + large sieve):** ES^{(y,e)} with bounded cap and free mute set fails for
   ≪ N exp(−c_e (log N)^{(e+2)/(e+3)}) primes (Thm 1.4, via the overflow cube Prop 1.3; shots alone: (e+1)/(e+2)).
   The cap is a sieve-dimension knob; e = 0 is Vaughan (prime-modulus large sieve; ES's record is 3/4, so only e ≥ 2
   exceeds it; (R230 repair D1)). Pointwise R200 M1 remains OPEN (two layers: class group
   across fields + (e+1)-free values on Pell orbits; §4).
2. **PM-II (PROVED rel. BV + large sieve, = Thm 1.4 at e = 0; (R230 repair D3)):** fails for ≪ N exp(−c (log N)^{2/3}) primes; failures are ≡ 1 (mod 12) and QR mod 7
   (the only covering moduli, for all h: h = 3, 7; (R230 repair D4)). No structural reason for p > 3361 (would be pointwise Type II-ES).
3. **SQ_± (PROVED + CONJECTURE):** the prime-modulus layer has χ = (n/ℓ) (free genus filter), exponent 1/2 on average
   (weaker exponent than ES's 2/3 by the prime-modulus method — not a hardness statement; (R230 repair D6)); CONJECTURE PM-SQ_± (0 exceptions ≤ 10⁶, adversarial-robust). Power saving
   is beyond the large sieve for all three (class masses Σ_{ℓ≤y} ω(ℓ)/ℓ = (log y)^{O(1)}). No pointwise strengthening found.
ES untouched.

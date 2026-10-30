# EXSET_DEPTH_BREAK — a depth-breaking bound for the prime-modulus U family? (wave z51, lane 1a, slug `dbreak`)

ES is OPEN. Nothing here proves or disproves it.
Labels: PROVED / CONDITIONAL (on what) / CERTIFIED / EVIDENCE / CONJECTURE / Assessment.
Scripts: `scripts/z51_dbreak_*`. Data: `data/z51_dbreak/`. Brief: `../z51briefs/1a_opus_dbreak.md`. Reviews:
`reviews/z51-dbreak-review-1.md`, `reviews/z51-dbreak-review-2.md` (Astra).

## 0. Summary table

**Status: three rounds complete; two Astra hostile reviews folded in (§7). No target is reached: there is no
depth-breaking bound here.** What the lane produced:
* an exact reformulation, and a reduction of T1-min, and of a power saving for E_U off the squares and for ES₅/U at
  primes, to one large-prime layer, the *top band* ℓ > √(2N) (Cor 3.3);
* EVIDENCE that the top band is Poisson at a fixed scale (n ∈ [N/2, N], N = 10⁸…10¹¹) with mean ≈ 0.32 log N, so that
  layer alone would give N^{−0.3} (§3.3);
* an abstract barrier for prime-detection information that is two-sided only at first order, with scoped arithmetic
  meaning (Thm 2.3), and a model-level statement for two-sided information below the level cap (Thm 2.6);
* a product-form obstruction for shift arguments (Prop 3.1) and scoped assessments for the other approaches.

| # | statement | label | § | review |
|---|---|---|---|---|
| 1 | target on the 4ℤ line (A_N ⊇ Av(𝓕_N)); three views (e/t/m) of one event; the non-CRT inputs named and why they escape Thm 2.2(c)(ii)'s hypotheses | PROVED (elementary) + Assessment | §1 | R1 MAJOR → R2 SOUND-WITH-MINOR (N1 identity fixed in R3) |
| 2a | exchange rate: PD events with modulus 4em ≤ e^λ carry first-moment mass ≪ λ²/(log N − λ), against ≍ λ for CRT events | PROVED (Brun–Titchmarsh); depth reading heuristic | §2.2 | R2 SOUND |
| 2b | **one-sided PD barrier (abstract, with scoped arithmetic meaning):** CRT data at level λ + PD first moments on modulus-bounded tests (exact, with candidate roughness to the horizon) + PD k-point upper bounds with K_k ≥ C^{k−1} + support cannot prove #A_N < (1 − 1/C)β_λ#I, β_λ ≥ (10/21)e^{−C₁√λ−C₂log²(2+λ)}; with C = 2 for bounds of that form with K_k ≥ 2^{k−1} | PROVED for arguments using only the stated axioms; not a theorem about prime detection in general | §2.3 | R1 FATAL (arithmetic) → R2 MAJOR (test family) → repaired in R3: tests now have modulus ≤ e^λ |
| 2c | sharpness (existence): Cauchy–Schwarz with pair constant K₂ and the mixture with constant densities have the same limit 1 − 1/K₂ | PROVED | §2.3 | R2 SOUND-WITH-MINOR (finite-size factor fixed) |
| 2d | the k-th factorial moment of the CRT events visible at level L is ≤ (Ce²L/k²)^k for k ≤ L/log 3 | PROVED | §2.4 | R2 SOUND |
| 2e | in the class-constant Cramér–Haar model, all mixed CRT/PD statistics of (all-prime) level ≤ λ, two-sided and of every order, are consistent with avoidance ≥ ½e^{−C√λ} | PROVED for that model, given the KARY/EK framework (EXSET_SIEVE_MASS Thm 3.2 proviso); arithmetic version OPEN | §2.4 | R2 SOUND-WITH-MINOR (repairs folded in) |
| 3a | cost profile of shifts; product-form bounds with a common loss C > 1 per factor save ≪_C (log log N)² log log log N; a common loss 1 + ε needs log(1/ε) ≳ M/log log N to save M ≫ (log log N)² log log log N | PROVED for the defined product format | §3.1 | R2 SOUND-WITH-MINOR |
| 3b | one layer suffices for upper bounds; T1-min ⟸ (TB_δ); (TB_pow) ⟹ E_U = odd squares + O(N^{1−c}) and #{p ≤ N : ES₅(p) fails} ≪ N^{1−c}; polynomial-level CRT majorants are linear (λ ≤ log N) or of degree ≤ 3 (λ ≤ 2 log N) in the top-band hits and save O(log log N) there | PROVED (inclusions; band bound via THETA) | §3.2 | R2 SOUND-WITH-MINOR |
| 3c | over all n ≤ N: P(X_top = 0) ≈ 1.3–1.5·e^{−E X_top}, slope −0.30 in log N over 10⁷–4·10⁹; the excess over Poisson is a mixture over the scale of n | CERTIFIED counts / EVIDENCE | §3.3 | R2 SOUND-WITH-MINOR |
| 3d | at a fixed scale (n ∈ [N/2, N]) X_top is Poisson within sampling error (ratio P(X_top=0)/e^{−E X_top} = 1.05, 1.02, 0.88, 1.12 at N = 10⁸, 10⁹, 10¹⁰, 10¹¹; standard errors 3–17%), E X_top ≈ 0.32 ln N; ≈ 0.08 (log N)² candidates per n | EVIDENCE (sampled; cross-checked against brute force) | §3.3 | added in R3 |
| 3e | literature: two-shift laws of P⁺ are *size* laws (logarithmic density; power-of-log error outside exceptional scales; unrefereed natural-density claim); nothing on P⁺(n+4e) mod 4e over many e. TB has a precise sufficient hypothesis (§3.2), not shown necessary | Assessment | §3.2 | R2 SOUND-WITH-MINOR |
| 4 | raw Chebyshev on X stops at ≫ N/μ (Haar Var X ≥ E X/2); anatomy split is a research plan, not a barrier | PROVED (constant centering, Haar) / Assessment | §4 | R2 SOUND-WITH-MINOR |
| 5 | a direct comparison with additive error η certifies ≤ log(1/η); the cited averaging/entropy results have bounded k and o(1) or power-of-log errors | PROVED (trivial) + Assessment | §5 | R2 SOUND-WITH-MINOR |
| 6 | census of the 4ℤ-line family to 4·10⁹ (complete histograms), independent cross-checks, controls | CERTIFIED / EVIDENCE | §6 | R2 SOUND |

## 1. Target, reformulations, and the non-CRT inputs

### 1.1 The target, on the 4ℤ line

I = I_N = {n ≤ N : n ≡ 1 (mod 8)}. An *event* is a pair (ℓ, e) with ℓ ≤ N prime, e ≥ 1 and ℓ ≡ −1 (mod 4e); its
class is E_{ℓ,e} = {n : ℓ | n + 4e}. The *4ℤ-line avoider set* is

    A_N = {n ∈ I : n ∉ E_{ℓ,e} for every event (ℓ, e)}.

The z50 prime-modulus U family 𝓕_N (classes −v mod ℓ, v | ℓ+1, v ≡ 0 (4) or 7 (8), ℓ < n + v) contains the classes
E_{ℓ,e} as its v = 4e part, and on the 4ℤ line the proper-divisor condition ℓ < n + 4e is automatic (Lemma 1.1(d)). So
Av(𝓕_N) ∩ I ⊆ A_N, and

> **T1-min(4ℤ).** #(A_N ∖ □) ≤ N exp(−(log N)^{1/2+δ}) for some δ > 0

implies T1-min of the brief. A_N is a *larger* set than Av(𝓕_N): upper bounds for A_N transfer to 𝓕_N; the barrier
statements are made for A_N (§8 on extensions).

**Lemma 1.1 (three views of one event; PROVED, elementary).** Let n ≡ 1 (mod 8), e, t ≥ 1, and ℓ = 4et − 1 prime.
(a) ℓ | n + 4e ⟺ ℓ | tn + 1.
(b) If ℓ | n + 4e and m := (n + 4e)/ℓ, then n = 4etm − 4e − m (the word (t, u, v) = (t, 4e, m)), n + m = 4e(tm − 1),
    and tn + 1 = ℓ(tm − 1).
(c) The map (ℓ, e) ↦ (ℓ, t = (ℓ+1)/(4e)) is a bijection between events and pairs (ℓ, t) with ℓ ≡ −1 (mod 4t). Hence
    n ∈ A_N ⟺ for every e ≥ 1, n + 4e has no prime factor ℓ ≤ N with ℓ ≡ −1 (mod 4e)
           ⟺ for every t ≥ 1, tn + 1 has no prime factor ℓ ≤ N with ℓ ≡ −1 (mod 4t).
(d) In (b), m ≡ 3 (mod 4); in particular m ≥ 3, so ℓ < n + 4e. Every event meeting n has e ≤ (n + 3)/8 and
    ℓ ≤ (n + 4e)/3 ≤ (n + 1)/2, so the cutoff ℓ ≤ N is automatic for n ≤ N.
(e) For fixed n and m, the events with cofactor m are exactly the divisors e of (n + m)/4 with (n + m)/(4e) ≡ −1 (mod m)
    for which (n + 4e)/m is prime; writing k = (n + m)/(4e) = tm − 1, the candidate is (n + 4e)/m = (tn + 1)/k = 4et − 1.

*Proof.* (a) tn + 1 = t(n + 4e) − ℓ, and ℓ ∤ t since ℓ > t. (b) n = mℓ − 4e = m(4et − 1) − 4e; the other two are
expansions. (c) Immediate from (a). (d) mℓ = n + 4e ≡ 1 (mod 4) and ℓ ≡ 3 (mod 4); then n + 4e = mℓ ≥ 3(4e − 1).
(e) n + 4e = mℓ with ℓ ≡ −1 (mod 4e) ⟺ n + 4e ≡ −m (mod 4em) ⟺ 4e | n + m and m | (n + m)/(4e) + 1 (since
n + m + 4e = 4e((n+m)/(4e) + 1)). ∎

**Lemma 1.2 (squares; Theorem E, recorded for the control).** No odd square x² lies in any E_{ℓ,e}. *Proof.* For an
odd prime q | e, ℓ ≡ −1 (mod q) and ℓ ≡ 3 (mod 4) give (q/ℓ) = (ℓ/q)(−1)^{(q−1)/2} = (−1/q)(−1)^{(q−1)/2} = 1; if 2 | e
then ℓ ≡ 7 (mod 8) and (2/ℓ) = 1. Since e < ℓ, (−4e/ℓ) = (−1/ℓ) = −1. ∎ Every forbidden class is a quadratic non-residue.

*Convention.* The scripts exclude n = 1 (an odd square in I). "Squares" in counts below are odd squares > 1; non-square
counts are unaffected.

**Baseline (PROVED, z50).** #A_N ≪ N exp(−c√(log N)): EXSET_SIEVE_MASS Prop 2.3's lower-bound mass already uses only
u ∈ 4ℤ, so Thm 2.2(a) applies to A_N. By Thm 2.2(c)(ii) (EXCEPTIONAL_THETA Thm 2.5 with slice primes ℓ ≡ 3 (4), ℓ ≥ 11,
and ℓ = 3, 7 moved into the small modulus Q₀ = 168), every level-λ nonnegative CRT majorant for A_N saves at most
C√λ + O(log²(2 + λ)). The local hypothesis holds: for ℓ ≥ 11, a = (ℓ+1)/4 ≥ 3 and w(ℓ) = τ(a) ≤ a − 1 < ℓ/4, and the
classes −4e (e | a) are distinct mod ℓ; in the fibre x ≡ 1 (8) the factor from 3 and 7 is (1 − 1/3)(1 − 2/7) = 10/21.
T1-min(4ℤ) asks for exponent 1/2 + δ.

**Mass profile (CERTIFIED counts, `scripts/z51_dbreak_sieve4.c`, `data/z51_dbreak/sieve4_*`).** The local density at
ℓ ≡ 3 (4) is w(ℓ)/ℓ with w(ℓ) = τ((ℓ+1)/4). The Haar mass grows with empirical slope C₄ ≈ 0.59 in log ℓ (3.23 at
ℓ = 1695, 7.14 at ℓ = 1.37·10⁶; EVIDENCE, no closed form derived); compare C_V ≈ 0.74 for the full prime family. Events
with ℓ > (N + 4e)/3 never meet I (Lemma 1.1(d)). At N = 10⁹: |I| = 1.25·10⁸, 15 810 odd squares > 1, and
#(A_N ∖ □) = 17 886 (the full z50 prime family leaves 4 932 non-squares). The Haar prediction for the non-squares is
3.0·10³, so the non-square excess is e^{1.8}, the 4ℤ-line analogue of z50's D_ns.

### 1.2 Where the mass sits, and what "depth" means here

Each dyadic block ℓ ∈ (L, 2L] carries mass ≈ C₄ log 2 = O(1) (EVIDENCE), spread over the divisors e of (ℓ+1)/4. The
optimal saving of a level-λ CRT method is Θ(√λ) (G1): the dimension κ(ℓ) ≍ log ℓ makes the Rankin truncation stop at
blocks with log ℓ ≍ √λ. (Individual primes up to e^λ are visible; it is their collective saving that stops.) T1-min
needs ≥ (log N)^{1/2+δ} units of mass certified jointly. Per n, R(n) := #{events containing n} has mean ≍ log N; its
large-prime layers are close to Poisson on the integers tested (EVIDENCE, §§3.3, 6.2), so the target is a lower-tail
statement.

### 1.3 The non-CRT inputs, named, and why they escape Thm 2.2(c)(ii)'s hypotheses

Thm 2.2 (and THETA Thm 2.5) caps bounds of the form N·Eν + (nonnegative rounding term), ν a nonnegative *periodic*
majorant of level ≤ λ evaluated by its CRT mean. Its engine is (b′)/Step 0 plus the Rankin functional. A function on
the finite interval [1, N] can always be written with classes of modulus > N; what the inputs below escape is the
global periodic-majorant-plus-CRT-mean architecture, not representability.

* **(N1) Prime detection in the cofactor (PD).** By Lemma 1.1(b),(e), ⋃_ℓ E_{ℓ,e} ∩ I = ⋃_m E^{PD}_{e,m}, where
  E^{PD}_{e,m} = {n ∈ I : n ≡ −4e − m (mod 4em), (n + 4e)/m is prime} (the union on the left is over the pivot primes
  ℓ ≡ −1 (mod 4e)). The first moment of E^{PD}_{e,m} is a count of primes ≤ (N + 4e)/m in a class mod lcm(4e, 8), evaluated by
  Siegel–Walfisz/BV/Brun–Titchmarsh in the candidate variable (BV ranges are governed by x = N/m), whereas as a CRT
  event its modulus is ℓ ≈ N/m.
* **(N2) Mean values of multiplicative functions over all primes.** E.g. Σ_{x≤X} z^{ω_e(x)}, ω_e(x) = #{ℓ | x : ℓ ≡ −1
  (4e)}, evaluated by Selberg–Delange (a Dirichlet series in all primes ≤ X): one shift, all primes, no dimension cost.
  Multi-shift versions (Shiu, Nair–Tenenbaum, Henriot) are discussed in §3.
* **(N3) Quadratic large sieve / Linnik duality.** Heath-Brown: Σ*_{n≤N} |Σ*_{m≤M} a_m (n/m)|² ≪ (NM)^ε(N + M)Σ|a_m|²,
  the sums over odd squarefree n, m. Non-squarefree n must be treated separately (on n ≡ 1 (8), n = 17b² repeats
  characters), so this input controls the quadratic profile (n/ℓ)_ℓ of squarefree n only. The profile is a *suggested*
  dependence mechanism between shifts (EXSET_SHIFT_DIVISORS Remark 3.1(3), a heuristic there). Squares fail it
  completely.

Escaping the hypotheses is necessary, not sufficient. Sections 2–5 examine what each input yields.

*Where squares must fail (control).* For n = x² every event indicator vanishes identically (Lemma 1.2). A statement of
T1-min strength is not contradicted by squares (density N^{−1/2}), but any *universal* inequality behind it must fail
on sets made of squares (G5).

## 2. Approach 1: prime detection in the cofactor

Verdict. PD is a genuine non-CRT input. (i) Per unit of level its first-moment mass is smaller than that of the CRT
events (Prop 2.2), so it is not a cheap layer for depth arguments. (ii) Arguments whose PD information consists of
exact first moments on modulus-bounded tests, one-sided correlation bounds of a stated form, and support, gain at most
log(C/(C − 1)) over the CRT cap (Theorem 2.3, a theorem about those axioms), and the constant is attained in a model
(Prop 2.4). (iii) In the class-constant Cramér–Haar model, two-sided mixed statistics below the level cap add nothing
to the exponent (Theorem 2.6). Not excluded: true (roughness-aware) two-sided PD correlations below or above the cap,
signed interval sums, archimedean relations, nonlinear Type II structure, and other deterministic relations.

### 2.1 PD events and their first moments

Fix a horizon λ with λ₀ ≤ λ ≤ c log N and put z = e^λ. For e ≥ 1 and m ≡ 3 (mod 4) let

    E^{PD}_{e,m} = {n ∈ I : n ≡ −4e − m (mod 4em), (n + 4e)/m is a prime > z}.

By Lemma 1.1(b),(e), ⋃_{e,m} E^{PD}_{e,m} = ⋃_{ℓ>z} E_{ℓ,e} ∩ I. Write B_λ ⊆ 1 + 8Ẑ for the clopen set of x avoiding the
(finitely many) event classes with ℓ ≤ z, and A^{CRT}_λ = B_λ ∩ I. Then A_N = A^{CRT}_λ ∖ ⋃ E^{PD}_{e,m}.
#E^{PD}_{e,m} counts primes p ∈ (z, (N + 4e)/m] with p ≡ −1 (mod 4e) and mp − 4e ≡ 1 (mod 8). Siegel–Walfisz gives its
asymptotic for 4e ≤ (log N)^A; BV gives it on average over 4e ≤ (N/m)^{1/2}(log N)^{−B}; Brun–Titchmarsh gives an upper
bound always.

### 2.2 The exchange rate between PD level and mass

**Proposition 2.2 (PROVED, Brun–Titchmarsh).** For λ₀ ≤ λ ≤ log N − 1,

    M_PD(λ) := Σ_{4em ≤ e^λ} #E^{PD}_{e,m}/#I ≤ C(1 + λ)²/(log N − λ),

whereas the CRT mass at level λ is Σ_{ℓ≤e^λ} w(ℓ)/ℓ ≫ λ for λ ≥ λ₀ (EXSET_SIEVE_MASS Prop 2.3). So for λ₀ ≤ λ ≤ (log N)/2,
M_PD(λ) ≤ C′(λ/log N)·mass_CRT(λ).

*Proof.* Brun–Titchmarsh: π(x; q, a) ≤ 2x/(φ(q) log(x/q)) for q < x. With x = (N + 4e)/m ≤ 2N/m, q = 4e < x and
log(x/q) ≥ log(N/(4em)) ≥ log N − λ, we get #E^{PD}_{e,m} ≤ 4N/(m φ(4e)(log N − λ)). Divide by #I ≥ N/8 − 1 and sum
1/(mφ(4e)) over 4em ≤ e^λ, which is O((1 + λ)²). ∎

*Heuristic reading (Assessment).* A PD event lumps all t (all primes ℓ = 4et − 1) at one cofactor, which is why its
modulus is small, but it pays 1/log N for primality. *If* compatible PD k-tuples had product-law main terms and the
weighted profile Σ P(E^{PD})(4em)^{−α} were ≪ 1/(α² log N), Rankin would bound the level-N part of the PD k-th factorial
moment by (C log N/k³)^k, against (C log N/k²)^k for CRT events (Lemma 2.5): the PD representation would reach
k ≍ (log N)^{1/3}, the CRT one k ≍ (log N)^{1/2}. Prop 2.2 bounds only the first-moment mass.

### 2.3 An abstract barrier for one-sided PD information

**Setting.** Fix λ, z = e^λ as in §2.1 and a finite family 𝒥 of PD events j = (e_j, m_j) with 4e_jm_j ≤ z, so m_j is
z-smooth. A *model* is a probability space carrying x ∈ 1 + 8Ẑ (Ẑ the profinite completion; x plays n) and bits
π_j ∈ {0, 1}, j ∈ 𝒥. Put

    r_j(x) = c_j·1[x ∈ class_j]·1[(x + 4e_j)/m_j has no prime factor ≤ z],

class_j the class −4e_j − m_j (mod 4e_jm_j) inside 1 + 8Ẑ, with c_j ≥ 0 chosen so that E_ℋ r_j = #E^{PD}_j/#I (ℋ = Haar
on 1 + 8Ẑ; r_j := 0 if the class or the event is empty). PD events with cofactor m > z are not represented; their bits
can be adjoined identically zero, and nothing is asserted about them.

*Facts about r_j (PROVED).* (α) On the support of r_{e,m}, v_q(x + 4e) = v_q(m) for every prime q ≤ z, so m is the full
z-smooth part of x + 4e; for fixed (x, e) at most one m has r_{e,m}(x) > 0. Thus the true exclusivity "n + 4e has at
most one cofactor m ≤ z with (n + 4e)/m a prime > z" holds in every model satisfying (I4) below. (β) If r_j(x) > 0 and a
CRT event (ℓ′, e_j) with ℓ′ ≤ z meets x, then ℓ′ | m_j, as for integers. (γ) r_j ≤ C₁λ/(log N − λ): with Q = lcm(8, 4e),
ℋ(class_j) = 8/(m_jQ), the roughness probability on the class is ∏_{p≤z, p∤Q}(1 − 1/p) ≍ Q/(φ(Q) log z), and
Brun–Titchmarsh gives #E^{PD}_j/#I ≪ 1/(m_jφ(Q)(log N − λ)); divide. So r_j ≤ 1/C once λ ≤ c_C log N.
(δ) *Arithmetic meaning on modulus-bounded tests.* Let S be a class b (mod d) with d ≤ z (so all prime factors of d,
and all prime powers in d, are ≤ z). Under ℋ conditioned on class_j ∩ S the candidate (x + 4e_j)/m_j is uniform on the
residue classes it can occupy modulo lcm(Q, d), and the roughness factor kills exactly the classes sharing a prime ≤ z
with it. Hence E_ℋ[1_S r_j] = (#E^{PD}_j/#I)·ϖ_j(S), where ϖ_j(S) is the proportion of admissible *reduced* candidate
classes that S selects: the Siegel–Walfisz/BV equidistribution main term, normalised by the true global count. It
vanishes exactly when S is locally inadmissible. (Positive main term does not mean positive finite count; BV is an
averaged statement.)

An argument of **type (λ; K₂, K₃, …)** uses the integers only through statements implied by the following axioms.

* (I1) *CRT data at level λ:* E f(x) = E_ℋ f for every f of level ≤ λ (finite combinations of class indicators b mod d
  with Σ_{slice ℓ | d} log ℓ ≤ λ, THETA §1).
* (I2) *PD first moments on modulus-bounded tests, exact:* P(π_j = 1, x ∈ S) = E_ℋ[1_S r_j] for every j and every class S
  of modulus ≤ z.
* (I3) *PD correlations, one-sided:* P(π_J ≡ 1, x ∈ S) ≤ K_k E_ℋ[1_S ∏_{j∈J} r_j] for every k ≥ 2, J ⊆ 𝒥 with |J| = k,
  and every clopen S.
* (I4) *Support:* π_j = 0 wherever r_j = 0.

By (δ), (I2) is the statement "primes in the candidate variable are equidistributed among the admissible reduced
classes of every modulus d ≤ z, with the true total"; the integers satisfy it up to the Siegel–Walfisz/BV error terms,
and an exact axiom implies every inequality |count − main term| ≤ error *with the same main term*. So arguments that use
SW/BV/BT-type equidistribution of the PD candidates on such tests, sieve upper bounds of I3 form, CRT data at level λ,
and the support facts (α)–(β), are covered. Not covered: first-moment tests outside the modulus-bounded family (e.g.
classes with a large uncharged prime or a large prime power), two-sided correlations of order ≥ 2 (even averaged),
signed interval sums at moduli > N, archimedean relations between candidates, Type I/II identities used beyond first
moments, and exact zero correlations not implied by congruences and roughness.

**Theorem 2.3 (one-sided PD information is worth a constant; PROVED for arguments of type (λ; K)).** Let C > 1,
K_k ≥ C^{k−1} for every k ≥ 2, and r_j ≤ 1/C for every j (by (γ), true for λ ≤ c_C log N). Then some model satisfies
(I1)–(I4) and

    P(x ∈ B_λ, π ≡ 0) ≥ (1 − 1/C)·β_λ,   β_λ := inf{E_ℋ ν : ν a level-λ majorant of B_λ} ≥ (10/21)e^{−C₁√λ − C₂ log²(2+λ)}.

Hence no argument of type (λ; K) proves #A_N < (1 − 1/C)β_λ·#I. With λ ≤ A log N such arguments gain at most
log(C/(C − 1)) over the CRT cap of G1.

*Proof.* (i) *A fake CRT law.* Conditional averaging onto the finite quotient generated by Q₀ and the slice primes
≤ z preserves majorisation, nonnegativity, the mean and the allowed slice supports, so the infimum is a finite LP. For a
finite set 𝒞 of level-λ classes containing the trivial class, LP duality (ν = 1 is primal feasible, ℋ dual feasible)
gives a probability ρ_𝒞 with ρ_𝒞 = ℋ on every class of 𝒞 and ρ_𝒞(B_λ) ≥ β_λ. The sets {ρ : ρ = ℋ on 𝒞, ρ(B_λ) ≥ β_λ} are
weak-* closed (class indicators and the clopen B_λ are continuous), nonempty, and have the finite-intersection
property; by compactness some ρ lies in all of them. The bound on β_λ is THETA Thm 2.5 for the 4ℤ-line system (§1.1):
Σ_ℓ w(ℓ)ℓ^{−1−α} ≪ 1/α by Brun–Titchmarsh and divisor pairing, the truncated mass is O(λ), s_* = log 11; optimise
19αλ + C/α (λ₀ large enough to absorb the bounded factors).
(ii) *The mixture.* Let ξ be an independent coin with P(ξ = 1) = 1/C. On {ξ = 0}: x ~ ρ and π ≡ 0. On {ξ = 1}: x ~ ℋ
and, given x, the π_j are independent Bernoulli(C r_j(x)).
(iii) *Checks.* (I1): the law of x is (1 − 1/C)ρ + (1/C)ℋ, equal to ℋ on level-λ functions. (I2), and in fact for every
clopen S: P(π_j = 1, x ∈ S) = (1/C)E_ℋ[1_S C r_j] = E_ℋ[1_S r_j]. (I3): P(π_J ≡ 1, x ∈ S) = C^{k−1}E_ℋ[1_S ∏_J r_j]
≤ K_k E_ℋ[1_S ∏_J r_j]. (I4): C r_j vanishes where r_j does; (α) and (β) hold on the support. Finally
P(x ∈ B_λ, π ≡ 0) ≥ P(ξ = 0)ρ(B_λ) ≥ (1 − 1/C)β_λ. ∎

The model event B_λ ∩ {π ≡ 0} contains the image of A_N; the strict inequality in the conclusion is the correct
endpoint.

**Corollary 2.3′ (sieve-type correlation constants).** If the correlation inputs are exactly upper bounds of the I3
form with K_k ≥ 2^{k−1} for all k ≥ 2 (and r_j ≤ 1/2), take C = 2: the gain over the CRT cap is ≤ log 2. The following
classical constants satisfy K_k ≥ 2^{k−1}: Selberg's tuple bound 2^k k!(1 + o(1)) and the variant 4^{k−1}(k−1)!, and the
twin-prime pair constants of Selberg (8), Bombieri–Davenport (4), Chen (3.9171), Wu (3.3996) and Lichtman (3.2290,
arXiv:2309.08522, Thm 1.1), all relative to the full Hardy–Littlewood main term. A global tuple estimate is not
automatically localised to every S as I3 requires, and a pair constant says nothing about the higher K_k.

**Proposition 2.4 (sharpness, existence; PROVED).** (a) If R = Σ_j π_j has E R = μ and E[R(R − 1)] ≤ K₂μ², then
P(R = 0) ≤ 1 − μ²/(μ + K₂μ²) (Cauchy–Schwarz). (b) For J = |𝒥| constant densities r_j ≡ r ≤ 1/K₂ with Jr → ∞, the
mixture with C = K₂ satisfies every I3 bound with K_k = K₂^{k−1}, has E R(R − 1) = K₂μ²(1 − 1/J), and
P(R = 0) = 1 − 1/K₂ + (1/K₂)(1 − K₂r)^J → 1 − 1/K₂, the limit of (a). With variable densities the last term is
(1/K₂)∫∏_j(1 − K₂r_j)dℋ, which need not vanish. ∎ This is an abstract example, not one of the roughness-supported
arithmetic densities.

*What lies outside Theorem 2.3.* (a) Upper bounds with K_k < C^{k−1} at some order k with a positive product integral
(they exclude this mixture; such constants would be of Hardy–Littlewood quality). (b) A *lower* bound for a union,
P(∃ j ∈ B : π_j = 1) ≥ 1/C + ε on a block of large mass; in the mixture the union has probability ≤ 1/C. That is a
T1-type statement itself. (c) Relative statements inside sets that already avoid PD events (RLD (R1) for PD steps).
(d) Everything listed after (I4) as not covered.

*Novelty (Assessment).* G1/THETA supply the fake CRT law and EXSET_ARITH_JANSON_OPUS §3 the LP-duality viewpoint; (D)22
concerns prime-supported CRT majorants. The zero-inflated mixture over added, roughness-supported PD bits is a
distinct elementary extension. It is a barrier for arguments built from the stated axioms, not for prime detection in
general.

### 2.4 Two-sided PD information below the level cap

**Lemma 2.5 (level-L content of CRT factorial moments; PROVED).** For 1 ≤ k ≤ L/log 3 and every α ∈ (0, 1],

    F_k(L) := Σ_{k-sets of events at distinct primes with Σ log ℓ_i ≤ L} ∏_i 1/ℓ_i ≤ e^{αL}(Σ_ℓ w(ℓ)ℓ^{−1−α})^k/k! ≤ e^{αL}(C/α)^k/k!,

so F_k(L) ≤ (Ce²L/k²)^k (take α = k/L ≤ 1); for k > L/log 3 the sum is empty. *Proof.* The degree-k coefficient of
∏_ℓ(1 + w(ℓ)ℓ^{−1−α}z) is at most (Σ w(ℓ)ℓ^{−1−α})^k/k!; Rankin gives 1[Σ log ℓ_i ≤ L] ≤ e^{α(L − Σ log ℓ_i)}; and
Σ_ℓ w(ℓ)ℓ^{−1−α} ≪ 1/α by Brun–Titchmarsh. Use k! ≥ (k/e)^k. ∎
The Haar factorial moment is e_k(p_ℓ : ℓ ≤ N) (elementary symmetric polynomial of p_ℓ = w(ℓ)/ℓ), ≈ μ_N^k/k! only for
k = o(μ_N). So for √(log N) ≪ k ≪ log N the part of the k-th factorial moment visible at level log N is exponentially
small. This limits Bonferroni/moment arguments that evaluate intersections by their CRT main terms; it does not
classify other uses of moment information.

**Theorem 2.6 (model-level; PROVED for the class-constant Cramér–Haar model, given the KARY/EK framework of
EXSET_SIEVE_MASS Thm 3.2 run with supply exponent 1).** Let W be the absolute constant of that theorem and, in this
theorem only, let the level of a class b (mod d) be Σ_{p | d, p > W} log p (all primes above W are charged). Let
λ₀ ≤ λ ≤ (log N)/2 and 𝒥 a finite family of PD events with s_j := Σ_{p | 4e_jm_j, p > W} log p ≤ λ. The
*class-constant Cramér–Haar model* CH draws x ~ ℋ and independent coins κ_j ~ Bernoulli(ρ_j) and sets
π_j = 1[x ∈ class_j]κ_j, where 0 ≤ ρ_j ≤ min{1, C₀(4e_j/φ(4e_j))/(log N − λ)}, C₀ absolute. A *mixed monomial*
1_S(x)∏_{j∈J}π_j (S a class) has level (level of S) + Σ_J s_j. Then some joint law of (x, π) agrees with CH on every
mixed monomial of level ≤ λ and has P(x ∈ B_λ, π ≡ 0) ≥ ½ exp(−C√λ), C absolute.

*Proof.* (1) *Random subfamily.* Let 𝒥′ ⊆ 𝒥 contain each j independently with probability ρ_j.
(2) *Linear supply.* With Γ, G, 𝔐 as in EXSET_BEYOND_CRT §2 and EXSET_SIEVE_MASS §3, let 𝔐_{𝒥′}(y) be the sum of
Γ(G)/G over the refined classes (step (3)) of j ∈ 𝒥′ with W < P(G) ≤ y. Dropping m ≡ 3 (4) and other restrictions,
Σ_{P(em)≤y} Γ(4em)(4e/φ(4e))/(4em) has odd-prime Euler factors 1 + γ′(p)[1/(p−1) + p²/(p−1)³] = 1 + 2/p + O(p^{−3/2})
for p > W (the first term from v_p(e) = 0 < v_p(m), the second from v_p(e) > 0, including 4e/φ(4e)), and bounded
factors at 2 and at p ≤ W; so it is ≪_W (log y)². Hence E𝔐_{𝒥′}(y) ≪ (log y)²/(log N − λ) ≪ log y for y ≤ e^λ, and the
supply is constant beyond e^λ (every prime > W of an indexed modulus is ≤ e^λ; λ₀ ≥ log W). The weights Γ(G)/G are
uniformly bounded (W large), so with t = log y the variance is O(t); Bernstein gives P(𝔐_{𝒥′}(e^t) > Kt) ≤ e^{−cKt}, and
summing over t = 2^i, with monotonicity in between (another factor 2 in K), gives with probability ≥ ½:
𝔐_{𝒥′}(y) ≤ K log y for all y ≥ y₀, K and y₀ absolute. The prime-local classes −4e (mod ℓ), ℓ ≤ e^λ, have supply
≤ K log y (Brun–Titchmarsh).
(3) *The cap for the realised family.* Refine: class_j ∩ (1 + 8Ẑ) is a union of refined W2 classes of the U-family 𝔘 of
EXSET_SIEVE_MASS §1.1 (split by the compatible t mod 4 and intersect with n ≡ 1 (8); e.g. (e, m) = (1, 3) gives
5 mod 12 → 17 mod 24 = (17 mod 48) ∪ (41 mod 48), refined W2 classes for (u, v) = (4, 3)), and the prime-local W1
classes refine by the other endpoint mod 8; all refinements of one j share j's selection coin, and their total weight
does not exceed the unrefined one. Let 𝔊(𝒥′) be these refined classes for ℓ ≤ e^λ and j ∈ 𝒥′, together with the
classes n ≢ 1 (mod 8). It has the square base of EXSET_SIEVE_MASS Thm 3.2 (word classes of 𝔘 contain no unit square;
the excluded residues mod 8 contain no unit square), and the cofactor sums (iii) are inherited by subfamilies. Rerun
Thm 3.2's assembly with first moment K log y: s₁ = √λ; singletons cost ≤ (8/3)K√λ; block i (s = 2^i s₁,
d_i = ⌊λ/s⌋) has E M_{V_i} ≤ 2Ks and (E M_{V_i} + 4d_i)/d_i ≤ 4K·4^i + 4, so the blocks cost O(√λ Σ_i 2^{−i}(1 + i)) = O(√λ);
keep the linear block, base term, leak bound and O(log²λ) remainder of the cited proof. So on the event of (2), every
level-λ majorant of 𝒜(𝔊(𝒥′)) has Eν ≥ e^{−C√λ} (constants absorbed for λ ≥ λ₀).
(4) *Fake laws.* As in Thm 2.3(i), there is a probability ρ_{𝒥′} with Haar marginals on every class of level ≤ λ and
ρ_{𝒥′}(𝒜(𝔊(𝒥′))) ≥ e^{−C√λ}; off the event of (2), put ρ_{𝒥′} = ℋ.
(5) *The model.* Draw 𝒥′, then x ~ ρ_{𝒥′}, and set π_j = 1[j ∈ 𝒥′, x ∈ class_j]. For a mixed monomial of level ≤ λ,
T = S ∩ ⋂_J class_j is a class (or empty) of level ≤ level(S) + Σ_J s_j ≤ λ, so E[1_S ∏_J π_j | 𝒥′] = 1[J ⊆ 𝒥′]ℋ(T) for
every 𝒥′, and averaging over the independent coins gives ∏_J ρ_j·ℋ(T), the CH value. On the good event, x ∈ 𝒜(𝔊(𝒥′))
forces x ∈ B_λ and π ≡ 0. ∎

*Arithmetic scope (Assessment).* CH ignores the roughness of candidates at primes q ∈ (W, e^λ]: for S forcing
q | (x + 4e_j)/m_j the true PD count is 0 while CH gives a positive value. So Theorem 2.6 shows that "PD events as coins
attached to W2 classes" add nothing to the exponent below the level cap; it is not a barrier for arguments using the
true level-λ PD statistics. An arithmetic version needs a fake law that also matches Haar on roughness-refined sets
S ∩ ⋂_J(class_j ∩ Rough_j), i.e. a sieve-limit theorem for roughness-refined (prime-law) majorants; EXSET_BEYOND_CRT §2
expects such a "prime-law version" by a unit-group rerun but has not checked it. OPEN.

**Scoped conclusion for approach 1.** Within the axioms of Thm 2.3, PD gains a constant; in the class-constant model
below the level cap (Thm 2.6) it gains nothing in the exponent. A depth-breaking PD argument must use information
outside these: true two-sided PD correlations (below or above the cap), union lower bounds (the target itself),
first-moment tests outside the modulus-bounded family, archimedean relations, or signed interval sums. *Step that fails
at squares:* none at the level of first moments (squares are a null set); the universal form of a union lower bound
fails on planted squares (G5).

## 3. Approach 2: exponential moments over shifts; the top band

Write X(n) = R(n) = Σ_e ω_e(n + 4e) (the number of events containing n), with ω_e(x) = #{ℓ | x prime, ℓ ≡ −1 (4e)}
(Lemma 1.1(c),(d)). For 0 ≤ z < 1, P(X = 0) ≤ E z^X = #I^{−1} Σ_{n∈I} ∏_e z^{ω_e(n+4e)}, a correlation of multiplicative
functions at many shifts. Verdict: bounds of product form over shifts with a common loss per factor are useless for
this family (Prop 3.1); for upper bounds one layer suffices (Lemma 3.2), which reduces T1-min, and a power saving, to
the top band (Cor 3.3); there the numerics are Poisson at fixed scale (§3.3). No proof of the top-band statement is
offered.

### 3.1 Product forms over shifts: the cost profile of the prime family

For a shift e let F_e = {n ∈ I : ω_e(n + 4e) = 0}, hit(e) = 1 − #F_e/#I, cost(e) = log(#I/#F_e). A *product-form* bound
over a shift set S is

    #A_N/#I ≤ ∏_{e∈S} min{1, C_e π_e} + R,   π_e ≥ #F_e/#I,  C_e ≥ 1,  R ≥ 0.

Its saving is ≤ Σ_{e∈S}(cost(e) − log C_e)^+, since min{1, C_e π_e} ≥ exp(−(cost(e) − log C_e)^+).

**Lemma 3.0 (cost profile; PROVED, Brun–Titchmarsh and PNT mod 8).** Uniformly for 4e ≤ N/2, N ≥ N₀:
(a) cost(e) ≤ log log N + O(1);
(b) hit(e) ≤ C₀(1 + log 4e + log log N)/φ(4e);
(c) Σ_{e≤E} hit(e) ≤ C₀(1 + log log N) log 2E for 1 ≤ E ≤ N^{1/3};
(d) Σ_{e≥1} hit(e) ≤ C₀ log N.
(Every relevant shift has 4e ≤ (N − 1)/2 by Lemma 1.1(d).)
*Proof.* (a) If n + 4e is prime then n ∈ F_e: its only prime factor is ≡ n (mod 4e), and n ≢ −1 (mod 4) on I. Primes in
(N/2, N] in the class 1 + 4e (mod 8) number ≫ N/log N. (b) For n uniform on I, P(ℓ | n + 4e) ≤ 1/ℓ + 9/N. Over
ℓ ≡ −1 (mod q), q = 4e: the ℓ ≤ q² contribute ≤ Σ_{j≤q} 1/(jq − 1) ≤ 2(1 + log q)/q; the ℓ ∈ (q², 2N] contribute
≤ (4/φ(q))(1 + log log 2N) by partial summation with π(t; q, −1) ≤ 4t/(φ(q) log t) (Brun–Titchmarsh, t ≥ q²), the range
being empty if q² > 2N; the 9/N terms add ≤ 9π(2N; q, −1)/N ≪ 1/φ(q). (c) Split at 16E², so that ℓ > (4e)² for every
e ≤ E in the upper range. Lower range: Σ_{ℓ≤16E²} #{e : 4e | ℓ + 1}/ℓ ≤ Σ_{ℓ≤16E²} τ((ℓ+1)/4)/ℓ ≪ log 2E (divisor pairing
and Brun–Titchmarsh). Upper range: the second part of (b) for each e ≤ E, and Σ_{e≤E} 1/φ(4e) ≪ log 2E. Rounding terms
add O(log 2E). (d) Σ_e hit(e) ≤ Σ_{ℓ≤N} w(ℓ)(1/ℓ + 9/N) ≪ log N. ∎

**Proposition 3.1 (product forms over shifts; PROVED for the format above).** Write L_j for the j-fold iterated
logarithm of N.
(a) If C_e ≥ C > 1 for every e ∈ S, the saving is ≪_C L₂² L₃.
(b) If C_e = 1 + ε for every e ∈ S (0 < ε ≤ 1, a = log(1/ε)), the saving is ≤ C₁L₂(a + log(2 + a + L₂)) + C₁L₂²L₃. So a
    saving M ≫ L₂²L₃ with a common factor 1 + ε requires a ≳ M/L₂.
*Proof.* (a) (cost(e) − log C)^+ > 0 forces hit(e) > 1 − 1/C, so by Lemma 3.0(b) and φ(q) ≫ q/log log 3q, e ≤ E₁ with
E₁ = O_C(L₂L₃). Each such shift contributes ≤ L₂ + O(1) (Lemma 3.0(a)).
(b) Fix an absolute E₁′ with hit(e) ≤ ½ for e > E₁′ (Lemma 3.0(b)). Shifts e ≤ max(E₁, E₁′) contribute O(L₂²L₃) as in (a).
A larger shift has cost(e) ≤ 2hit(e) and contributes only if ε/2 < cost(e) ≤ 2hit(e), which by Lemma 3.0(b) forces
e ≤ E₀ with log E₀ ≤ a + O(log(2 + a + L₂)). If E₀ ≤ N^{1/3}, Lemma 3.0(c) bounds their contribution by
C₀(1 + L₂) log 2E₀. If E₀ > N^{1/3}, then (log N)/3 < a + O(log(2 + a + L₂)) forces a ≫ log N, and Lemma 3.0(d) bounds
their contribution by C₀ log N ≪ a. Add the small-shift term. ∎

*Reading.* This concerns the displayed format with a common loss; it says nothing about exact factors (C_e = 1),
heterogeneous losses, or non-product estimates. Heuristically the per-shift cost is ≈ log(log N/log 4e)/φ(4e), much
smaller than for the full U family (lane D, EXSET_SHIFT_DIVISORS Thm 5.1, 5.3: (log N)^{log 2+o(1)} costly shifts); the
proposition proves only the upper bounds used. Whether a particular Nair–Tenenbaum/Henriot/Shiu application falls
under the format, or under G1 as a periodic CRT majorant, has to be checked case by case (its constants and local
factors must translate into factors C_e on the true marginals, or its majorant must be shown periodic, nonnegative
and CRT-evaluated); the common implementation, which bounds the y-rough part of each n + 4e by f ≤ 1 and sieves the
y-smooth parts, is of the latter kind.

### 3.2 One layer suffices for upper bounds; the top band

**Lemma 3.2 (decoupling; PROVED, trivial).** For any subfamily B of events, A_N ⊆ Av(B). For subfamilies B₁, …, B_k and
z ∈ [0, 1), E z^{X_{B₁}+⋯+X_{B_k}} ≤ ∏_i (E z^{k X_{B_i}})^{1/k} (Hölder). So if one layer B satisfies
#Av(B) ∩ (I ∖ □) ≤ N e^{−M}, so does A_N.

One sufficiently strong layer is *sufficient*; it is not shown necessary (combined information can beat every single
layer). RLD-U is a statement at the level of the full Mertens product, and Hölder loses a factor k in the exponent when
layers are combined this way.

*Which layer.* Small primes ℓ ≤ e^{c√(log N)} are where CRT works and stops (G1). For the top band ℓ > √(2N), a level-λ
majorant with λ ≤ log N contains at most one band prime per term, so it is *linear* in the band hits; after conditional
averaging its saving on the band is ≤ log(1/(1 − max p_ℓ)) = o(1) (EXSET_SIEVE_MASS Thm 2.2(c)(iii), linear case). At
λ = 2 log N up to three band primes fit in a term (four do not); for a band of fixed logarithmic width THETA Prop 2.4
with s_* ≍ log N has O(1) groups and gives saving O(log(2 + μ)). So polynomial-level CRT majorants cannot supply an
exponential-in-mass saving from the top band (they save O(log log N) there; smaller primes add their own saving). The
top band is also the cleanest large layer: each n + 4e ≤ 2N has at most one prime factor > √(2N), namely P⁺(n + 4e).

**Corollary 3.3 (reduction to the top band; PROVED).** Put X_top(n) = #{e ≥ 1 : P⁺(n + 4e) > √(2N),
P⁺(n + 4e) ≡ −1 (mod 4e)} (by Lemma 1.1(d) only e ≤ (n + 3)/8 contribute, and every such prime is ≤ (n + 1)/2 ≤ N, so
each counted hit is an event). Then A_N ⊆ {X_top = 0}, and
* (TB_δ) #{n ∈ I ∖ □ : X_top(n) = 0} ≤ N exp(−(log N)^{1/2+δ}) implies T1-min(4ℤ) and T1-min;
* (TB_pow) #{n ∈ I ∖ □ : X_top(n) = 0} ≤ N^{1−c} implies
  #{n ≤ N, n ≡ 1 (4) : U(n) fails} = #{odd squares ≤ N} + O(N^{1−c}) (a power saving for E_U off the squares), and
  #{p ≤ N prime : ES₅(p) fails} ≤ #{p ≤ N : U(p) fails} ≪ N^{1−c} (EXSET_SIEVE_MASS Thm 3.5(a) for the first
  inequality), i.e. z50 Target 1 for ES₅ and U.
*Proof.* A U failure at n ≡ 1 (8) lies in no prime-pivot U certificate class, so it lies in A_N ⊆ {X_top = 0}; U holds at
every n ≡ 5 (mod 8), n > 5 (z50 Obs. 6.0); primes are not squares. ∎

By Lemma 1.1(e), X_top(n) = #{(m, e) : m ≡ 3 (4), e | (n + m)/4, (n + m)/(4e) ≡ −1 (mod m), (n + 4e)/m a prime > √(2N)}:
for each cofactor m ≤ (3n + 3)/(2√(2N)), the divisors of the single integer (n + m)/4 in one class mod m produce
candidates, and one candidate must be prime (§3.3 counts them).

**A precise sufficient hypothesis, and the literature (Assessment).** TB_δ (resp. TB_pow) follows from: *there are a
selected set 𝔈 of shifts and a reference law Q for the top-band hit indicators (Y_e)_{e∈𝔈} of a random n ∈ I ∖ □ such
that Q(all Y_e = 0) ≪ e^{−M} and |P(all Y_e = 0) − Q(all Y_e = 0)| ≪ e^{−M}*, with M = (log N)^{1/2+δ} (resp. c log N). A
direct bound for the zero event, an exponential moment or a weighted witness count could suffice with less; this is a
sufficient hypothesis, not a characterisation. What is known is far from it, and of a different kind: two-shift laws
of the *sizes* of largest prime factors. Teräväinen (arXiv:1710.01195, Thms 1.11, 1.14) proves the joint law of
log P⁺(n)/log n and log P⁺(n+1)/log n in logarithmic density; Tao–Teräväinen (arXiv:2512.01739, Thm 1.8) give the
consecutive smooth-number law with error O((log x)^{−c}) for x outside a set of logarithmic measure O((log X)^{−c}),
uniformly in u, v ≥ 1; the OpenAI release (item 012, *The joint Dickman law for consecutive integers*, unrefereed)
claims natural-density independence for fixed parameters, with no rate. None concerns P⁺(n + 4e) modulo a growing
4e, and size thresholds do not determine those residues. Short-interval analogy: under a uniform Hardy–Littlewood
hypothesis Gallagher obtains Poisson statistics for primes in [x, x + λ log x] with λ fixed; uniformity for λ → ∞ at
exponentially small zero probabilities is additional. Under RH, Selberg's bound #{x ∈ [X, 2X] : no prime in
[x, x + H]} ≪ X(log X)²/H (1 ≤ H ≤ X) is a power saving for H = X^θ, trivial for H = λ log X with λ fixed, and polylogarithmic
for polylogarithmic H. TB_δ asks for a super-√ Poisson tail among ≍ (log N)² structured candidates (EVIDENCE for the
count in §3.3); no reduction to a prime-gap theorem is claimed.

### 3.3 Numerics for the top band

**Over all n ≤ N (CERTIFIED counts, `data/z51_dbreak/sieve4_top_N*.txt`; histograms complete).** Non-squares n ∈ I,
top band ℓ > √(2N):

| N | E X_top | P(X_top = 0) | e^{−E X_top} | ratio | P(X_top = 0 \| small layer avoided) |
|---:|---:|---:|---:|---:|---:|
| 10⁷ | 3.534 | 0.03844 | 0.02919 | 1.32 | 0.0841 |
| 10⁸ | 4.251 | 0.01975 | 0.01425 | 1.39 | 0.0461 |
| 10⁹ | 4.989 | 0.00981 | 0.00681 | 1.44 | 0.0236 |
| 2·10⁹ | 5.209 | 0.00795 | 0.00547 | 1.45 | 0.0193 |
| 4·10⁹ | 5.429 | 0.00644 | 0.00439 | 1.47 | 0.0158 |

log P(X_top = 0) falls with slope −0.30 in log N (−0.297 over 10⁷–10⁹, −0.304 over 10⁹–4·10⁹). Conditioning on the
small layer (ℓ ≤ √(2N)) lowers E X_top (4.99 → 4.20 at N = 10⁹) and raises P(X_top = 0) by a factor 2.4, which is why
Lemma 3.2 (no conditioning) is the way to use the layers. The largest X_top seen is 41 (five n ≤ 4·10⁹ have X_top ≥ 40,
e.g. n = 2 895 235 193).

*Where the excess over Poisson comes from (EVIDENCE).* Stratifying the non-squares at N = 10⁹ by their quadratic profile
at 3, …, 29 (512 profiles; `PROFILE=1`, `data/z51_dbreak/profile_top_N1e9.txt`) changes the Poisson prediction for the
number of zeros only from 851 611 to 906 959 (actual 1 225 894): the small-prime profile explains little. Stratifying
instead by the dyadic range of n (`SCALE=1`, `data/z51_dbreak/scale_top_N1e9.txt`) gives a mixture-Poisson prediction
of 1 156 446, i.e. actual/prediction 1.06 instead of 1.44: the excess is mostly a mixture over the *scale* of n (the
threshold √(2N) is fixed, so n ≪ N have fewer top-band candidates; E X_top = 3.34, 3.76, 4.18, 4.61, 5.03, 5.43 on
[2^b, 2^{b+1}), b = 24…29). Within the top dyadic range [2²⁹, 10⁹] the ratio is 1.021; it is 1.04–1.10 in the lower ranges,
which still mix scales by a factor 2. At a fixed scale the top band is Poisson (next table).

**At a fixed scale, n uniform in [N/2, N] (EVIDENCE; `scripts/z51_dbreak_candidates.c`, random samples,
`data/z51_dbreak/cand_N*.txt`).** The program enumerates, for each sampled n, all top-band candidates by the m-view of
Lemma 1.1(e) (segmented factorisation of n + m, m ≤ (3n + 3)/(2√(2N))) and tests them with a deterministic
Miller–Rabin; it agrees with a brute-force e-view count of X_top on 150 random n at N = 10⁶ (`scripts/z51_dbreak_xcheck_top.py`).

| N | samples | E C_top (candidates) | E X_top | var/mean | P(X_top = 0) ± s.e. | e^{−E X_top} | ratio |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 10⁸ | 100 000 | 25.8 | 4.668 | 1.036 | 0.00985 ± 0.00031 | 0.00939 | 1.05 |
| 10⁹ | 100 000 | 33.5 | 5.418 | 1.048 | 0.00454 ± 0.00021 | 0.00444 | 1.02 |
| 10¹⁰ | 100 000 | 42.1 | 6.155 | 1.053 | 0.00187 ± 0.00014 | 0.00212 | 0.88 |
| 10¹¹ | 30 000 | 51.9 | 6.870 | 1.085 | 0.00117 ± 0.00020 | 0.00104 | 1.12 |

At a fixed scale the zero probability agrees with the Poisson value within one to two standard errors, the mean grows
by ≈ 0.74 per decade (≈ 0.32 ln N), and log P(X_top = 0) falls by ≈ 0.83 per decade between 10⁸ and 10¹⁰. The candidate
count C_top is ≈ 0.08 (log N)² on average (0.076, 0.078, 0.080, 0.081 times (ln N)²), and its lower tail thins quickly
(P(C_top ≤ 20) = 0.29, 0.097, 0.021, 0.003). A candidate is prime with probability ≈ 2.46/log p (local factors), and
weighting candidates by 1/log p predicts the zero probability badly in both directions: the primality events are not
a simple function of the candidate count. Reading (Assessment): at fixed scale the top band behaves like independent
events with total mean ≈ 0.32 log N, which under TB_pow would give c ≈ 0.3; these are finite-range samples, not an
asymptotic.

## 4. Approach 3: anatomy and the bilinear (e, m) incidence

Verdict: the bilinear (e, m) form is the PD system of §2 summed over n. Raw Chebyshev on X stops at N/μ. Anatomy
controls the *candidates* (divisors of one integer (n + m)/4 per cofactor m), not their primality or joint law. Neither
observation is a barrier for weighted or nonlinear uses of the incidence.

### 4.1 The incidence form and the raw L² ceiling

By Lemma 1.1(b),(e), X(n) = #{words (t, 4e, m) of n with 4et − 1 prime}: n has C(n) := #{4ℤ-line words of n} candidates
(C(x²) = 0 by Theorem E), and X(n) counts those whose pivot tu − 1 is prime. Double counting (over all PD events, i.e.
without the horizon of §2.1): Σ_n X(n) = Σ_{e,m} #{PD events}, Σ_n X(n)² = Σ over pairs, each pair being the binary
problem m p − m′p′ = 4(e − e′), p ≡ −1 (4e), p′ ≡ −1 (4e′): twin-prime type for fixed coefficients; averaged over
(e, m, e′, m′), the setting where circle-method or dispersion asymptotics are plausible.

**Proposition 4.1 (raw Chebyshev ceiling; PROVED for Haar with constant centering).** With μ = E_ℋ X,
Var_ℋ X = Σ_ℓ p_ℓ(1 − p_ℓ) ≥ μ/2 (at each prime at most one forbidden class is hit, p_ℓ = w(ℓ)/ℓ ≤ 1/2, and distinct
primes are independent under ℋ), so the Chebyshev bound N·Var X/μ² is ≫ N/μ. ∎ On the integers the large-prime layers
have variance/mean 1.04–1.13 (§§3.3, 6.2; the full count X was not tabulated). This limits the direct second-moment
bound for the raw count, even with an exact asymptotic for the averaged binary problem: exact second moments give 1/μ.
It does not limit L² arguments applied to weighted counts, sieve weights, nonlinear transforms or bilinear error terms;
for a general predictor μ(n) no such ceiling holds (μ(n) = max(1, X(n)) makes the numerator count the zeros exactly).

### 4.2 Anatomy: candidates versus primes

The m-view (Lemma 1.1(e)) makes the candidates of cofactor m the divisors e of the single integer (n + m)/4 in one class
mod m. Hall–Tenenbaum/Ford anatomy and Erdős–Hall (divisors in residue classes) control such divisor sets one integer
at a time; they bear on C(n), not on X(n). One can split

    P(X = 0) ≤ P(C(n) ≤ K) + P(X = 0, C(n) > K),

with K = (log N)^{3/2+δ}, so that "K candidates, each prime with probability ≍ 1/log N" would give e^{−(log N)^{1/2+δ}} in a
Poisson model. This split is a research plan; failure of a crude implementation is not a barrier. Two observations
(Assessment): the first term is a lower tail for the full (composite-pivot) word count, beyond what the CRT architecture
certifies (its optimal collective saving corresponds to words of moduli ≤ T with log T ≍ (log N)^{1/3}, lane E's 2/3
exponent); the second is the PD problem restricted to {C > K}, which falls under the axioms of Thm 2.3 only after the
selection {C > K} is itself represented in the model. The fixed-scale data of §3.3 (top band only) show C_top ≈ 0.08 (log N)²
with a thin lower tail.

## 5. Approach 4: entropy decrement and averaged independence

**Lemma 5.1 (additive-error floor; PROVED, trivial).** A direct comparison P(X_B = 0) ≤ P_model(X_B = 0) + η certifies a
saving of at most log(1/η).

The quantitative errors of the available results are, as far as checked: powers of log h or log X for
Matomäki–Radziwiłł-type short-interval and averaged-correlation theorems; a power of log outside an exceptional set of
scales for Tao–Teräväinen arXiv:2512.01739; no explicit rate for entropy-decrement arguments (Tao; Tao–Teräväinen odd-order
Chowla; OpenAI item 012). Substituted into Lemma 5.1, a power-of-log error gives O(log log N); a qualitative o(1) gives
no explicit saving. The cited correlation theorems concern a bounded number of shifts (or an average over one shift). By
Lemma 3.2 the target is the lower tail of one sum X_B; pairwise independence on average is second-moment information
(§4.1). If one uses the Poisson-scale central-moment bound (Ck/μ)^{k/2} with μ ≍ log N, a saving M = (log N)^{1/2+δ}
(0 < δ < 1/2) needs order k ≍ M/log(μ/M) > √(log N); this is the order needed for that particular bound, not for all
moment arguments.

**Scoped assessment for approach 4.** The cited averaging/entropy theorems, used through Lemma 5.1 or through moments of
bounded order, cannot reach T1-min. Amplifications that combine bounded-order information nonlinearly (as the
growing-dimensional sieve in Tao–Teräväinen does for another problem) are not excluded here.

## 6. Numerics and controls

All runs with `ulimit -v 8000000` and timeouts. C sources `scripts/z51_dbreak_sieve4.c` (usage `sieve4 N Y`; prints the
complete histogram, its total, every non-square n with ≥ 40 large events; options `DUMP=file`, `PROFILE=1`) and
`scripts/z51_dbreak_candidates.c` (usage `candidates N samples seed [n…]`); Python `scripts/z51_dbreak_controls.py`,
`scripts/z51_dbreak_xcheck.py`, `scripts/z51_dbreak_xcheck_top.py`, `scripts/z51_dbreak_cand_analyze.py`.

### 6.1 Census of the 4ℤ-line prime family (CERTIFIED)

* Cross-checks: the brute-force e-view enumeration (factor n + 4e for e ≤ (n + 3)/8, justified by Lemma 1.1(d)) and the
  sieve agree exactly on A_N at N = 2·10⁴ (160 avoiders > 1, 70 of them squares; with n = 1, 161 and 71;
  `data/z51_dbreak/xcheck_alive_N20000.txt`). The t-view (ℓ | tn + 1, ℓ ≡ −1 (4t)) agrees with the e-view on every
  control below 3000. The candidates program agrees with the e-view on X_top for 150 random n at N = 10⁶. The round-1
  reviewer reran N = 10⁷ (top band) byte-for-byte and an independent brute force at 2·10⁴ including the top-band
  histogram; the round-2 reviewer recomputed the 2·10⁹ and 4·10⁹ rows from the stored histograms.
* The sieve checks every odd square ≤ N against every class it marks and reports any hit on stderr; none occurred at
  N = 10⁷, 10⁸, 10⁹, 2·10⁹, 4·10⁹. No histogram bin saturated (bin 255 empty in every run).
* #(A_N ∖ □) = 2 457, 6 836, 17 886, 23 727, 31 612 at N = 10⁷, 10⁸, 10⁹, 2·10⁹, 4·10⁹ (squares > 1: 1 580, 4 999,
  15 810, 22 360, 31 622); density in I 1.97·10⁻³, 5.47·10⁻⁴, 1.43·10⁻⁴, 9.49·10⁻⁵, 6.32·10⁻⁵. At 4·10⁹ the non-square
  avoiders are as many as the squares.

### 6.2 Poisson behaviour of the large layers (EVIDENCE)

Variance/mean of the number of events with ℓ > Y, over non-squares n ≤ N (complete histograms):

| N | Y | mean | var/mean (all) | mean, var/mean (small layer avoided) |
|---:|---:|---:|---:|---:|
| 10⁹ | 10³ | 7.17 | 1.05 | 6.48, 1.19 |
| 10⁸ | √(2N) | 4.25 | 1.12 | 3.47, 1.20 |
| 10⁹ | √(2N) | 4.99 | 1.12 | 4.20, 1.20 |
| 4·10⁹ | √(2N) | 5.43 | 1.13 | — |

These are finite-range observations over all n ≤ N (mixing scales); the fixed-scale data are in §3.3. (At N = 10⁹,
Y = 10³ one non-square, n = 833 975 993, has 42 large events.)

### 6.3 Controls (`data/z51_dbreak/controls.json`)

For a single control n, "top band" means ℓ > √(2n) (not the fixed √(2N) of the census).

| n | events R(n) | top-band events | least event prime | n ∈ A_N |
|---|---:|---:|---:|---|
| odd squares 9 … 998001 | 0 | 0 | — | yes (Lemma 1.2) |
| 105, 2961, 3985, 25305, 111969, 978145 (the U failures) | 0 | 0 | — | yes |
| 193, 2521, 3361, 9601, 66529 (hard primes) | 0 | 0 | — | yes |
| 409, 577, 5569, 8813281 (hard primes) | 2, 3, 2, 5 | 1, 2, 0, 2 | 7, 7, 47, 191 | no |
| R-zeros 23929, 83449, 102001, 329617, 712321, 1134241, 1724209, 1726201, 5212561 | 4, 2, 3, 2, 2, 7, 2, 1, 4 | 1, 2, 2, 1, 1, 3, 2, 1, 3 | 7, 7591, 23, 71, 23, 7, 5147, 5279, 503 | no |
| 17, 241 (numerator 8) | 2, 3 | 1, 1 | 3, 7 | no |

Readings. Five of the nine hard primes avoid the whole 4ℤ-line prime family; an exceptional-set statement must allow
such survivors, and nothing here is pointwise. Three R-zeros are hit only in their top band (83449, 1724209, 1726201).
Numerator 8: no statement here is pointwise or transfers to 8/n; the barrier statements are about axioms and models,
and Cor 3.3 is an inclusion of avoider sets, so there is nothing to falsify at 17 or 241 (both are in fact hit by
4ℤ-line prime events for 4/n).

## 7. Hostile reviews

Both reviews were run with `openai-codex/gpt-6-astra:high` through the `pi` CLI (the `subagent` tool's codex provider
crashed with a module error), prompted to break every claim, with independent numerical checks.

**R1 (`reviews/z51-dbreak-review-1.md`).** On §§1–6 as first written: rows 1, 2c, 2d, 3a, 3b (packaging), 3d, 4, 5
MAJOR; 2b FATAL as an arithmetic barrier but SOUND-WITH-MINOR as an abstract mixture lemma; 2a, 3c, 6
SOUND-WITH-MINOR. Reruns: N = 10⁷ top band byte-identical; independent brute force at 2·10⁴ matches. Repairs (round 2):
candidate roughness to the horizon in Thm 2.3 (the earlier w-rough density contradicted true zero counts); PD family
restricted to 4em ≤ e^λ (automatic within-shift exclusivity); B_λ vs A^{CRT}_λ; inf/finite quotient; "<"; R-term
10/21; Cor 2.3′ literature corrected (Lichtman 3.2290; Wu 3.3996); Prop 2.4 integral; Lemma 2.5 ranges; Prop 3.1(b) proof;
band language; sufficient-not-necessary; literature on P⁺ (sizes, not residues; Tao–Teräväinen 2512.01739); Prop 4.1
restricted to constant centering; §5 necessity language; quadratic large sieve with squarefree condition; n = 1
convention; complete histograms.

**R2 (`reviews/z51-dbreak-review-2.md`).** Rows 2a, 2d, 6 SOUND; 1, 2c, 2e, 3a, 3b, 3c, 3d, 4, 5 SOUND-WITH-MINOR; 2b
MAJOR: THETA's slice level does not bound the test modulus, and an explicit level-zero test (modulus 2424 = 8·3·101,
101 a non-slice prime, horizon 100) has true PD count identically 0 but positive model value, so "(I2) matches the true
SW/BV main terms at level ≤ λ" was false. Thm 2.6 SOUND as a model theorem after: an explicit all-prime level convention,
refinement of the W1/W2 classes with a common selection coin, constant 4K·4^i + 4, expanded supply/concentration
argument. Stored 2·10⁹ and 4·10⁹ rows reproduced. Repairs (round 3): (I2) now ranges over classes of modulus ≤ e^λ, with
the arithmetic meaning (δ) proved (proportion of admissible reduced candidate classes, true global count, zero exactly
on locally inadmissible tests) and the uncovered first-moment tests listed; (γ) proof of r_j ≤ 1/C; Cor 2.3′ limited to
the listed constants; Prop 2.4 factor (1 − 1/J); "what lies outside" softened; Thm 2.6 repairs as listed; Prop 3.1
O(L₂L₃) and the small-shift term; Reading heuristics labelled; Cor 3.3 ES₅ at primes explicit (Thm 3.5(a)); precise
sufficient hypothesis; Selberg's range; N1 identity with ⋃_ℓ; variance ratios labelled as large-layer statistics; §5
moment order restricted to the displayed bound; §8 wording. Not accepted: none.

The fixed-scale Poisson data (§3.3, row 3d) were added after R2 and have not been reviewed.

## 8. Exact remaining gap

* **No depth-breaking bound is proved.** T1-min(4ℤ) would follow from TB_δ, and a power saving for E_U off the squares
  and for ES₅/U at primes from TB_pow (Cor 3.3). Polynomial-level CRT majorants cannot supply an exponential-in-mass
  saving from the top band (they save O(log log N) there). At a fixed scale the top band is Poisson within sampling
  error with mean ≈ 0.32 ln N at N = 10⁸–10¹¹ (EVIDENCE), so TB_pow with c ≈ 0.3 is consistent with all data.
* **What is excluded, and only in this scope.** Arguments using CRT data at level λ, exact PD first moments on
  modulus-bounded tests, one-sided PD correlation bounds with K_k ≥ C^{k−1} and the support facts gain a constant
  (Thm 2.3). In the class-constant Cramér model, two-sided mixed statistics below the level cap gain nothing in the
  exponent (Thm 2.6); the arithmetic version needs a sieve-limit theorem for roughness-refined (prime-law) majorants.
  Product-form shift bounds with a common loss C > 1 save ≪ (log log N)² log log log N, and with a common loss 1 + ε
  need log(1/ε) ≳ M/log log N (Prop 3.1). Raw Chebyshev stops at N/μ (Prop 4.1).
* **What is not excluded.** True (roughness-aware) two-sided PD correlations below or above the level cap; union lower
  bounds for a block of mass ≫ √(log N) (that is the target in another form); weighted or nonlinear uses of the
  incidence; signed interval sums at moduli above N; archimedean relations; heterogeneous or exact shift factors.
* **The cleanest open statement this lane isolates:** TB_pow (or TB_δ) for the single layer ℓ > √(2N), i.e. a Poisson
  lower tail for the residues of the largest prime factors P⁺(n + 4e) modulo 4e over the shifts e, beyond any two-shift
  technology.
* **Transfer to the full prime family 𝓕_N.** Upper bounds transfer (A_N ⊇ Av(𝓕_N)). Theorems 2.3 and 2.6 are proved
  for the 4ℤ-line classes. The CRT fake law and the CH construction plausibly extend to the full refined U family with
  adjusted supply constants (Assessment); the exact roughness/cofactor parametrisation and the first-moment transfer
  for the 8ℤ+7 line need their own proof.

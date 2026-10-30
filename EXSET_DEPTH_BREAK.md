# EXSET_DEPTH_BREAK — a depth-breaking bound for the prime-modulus U family? (wave z51, lane 1a, slug `dbreak`)

ES is OPEN. Nothing here proves or disproves it.
Labels: PROVED / CONDITIONAL (on what) / CERTIFIED / EVIDENCE / CONJECTURE / Assessment.
Scripts: `scripts/z51_dbreak_*`. Data: `data/z51_dbreak/`. Brief: `../z51briefs/1a_opus_dbreak.md`. Reviews:
`reviews/z51-dbreak-review-1.md`, `reviews/z51-dbreak-review-2.md` (Astra).

## 0. Summary table

**Status: three rounds complete; three Astra hostile reviews folded in (§7). No target is reached: there is no
depth-breaking bound here.** What the lane produced:
* an exact reformulation, and a reduction of T1-min, and of a power saving for E_U off the squares and for ES₅/U at
  primes, to one large-prime layer, the *top band* ℓ > √(2N) (Cor 3.3);
* EVIDENCE that at a fixed scale (n ∈ [N/2, N], N = 10⁸…10¹¹) the top band's zero probability matches e^{−mean}
  within two standard errors (despite significant over-dispersion), with the mean growing ≈ 0.32 per unit of ln N,
  consistent with that layer alone giving a power saving (§3.3);
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
| 3c | over all n ≤ N: P(X_top = 0) ≈ 1.3–1.5·e^{−E X_top}, slope −0.30 in log N over 10⁷–4·10⁹; at N = 10⁹ dyadic stratification by the size of n accounts for 81% of the excess zeros over a homogeneous Poisson prediction | CERTIFIED counts / EVIDENCE | §3.3 | R3 SOUND-WITH-MINOR |
| 3d | at a fixed scale (n ∈ [N/2, N]) the zero probability of X_top is compatible with e^{−E X_top} (ratios 1.05, 1.02, 0.88, 1.12 at N = 10⁸…10¹¹, within ≈ 2 s.e.), although X_top is significantly over-dispersed (var/mean 1.04–1.09, 7–10 s.e.); E X_top ≈ 0.319 ln N − 1.20 over this range; ≈ 0.08 (log N)² candidates per n | EVIDENCE (sampled; cross-checked against brute force) | §3.3 | R3: counts SOUND; Poisson wording corrected |
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
on 1 + 8Ẑ; r_j := 0 if the class or the event is empty). All PD events outside 𝒥 (cofactor m > z, or 4em > z) are not
represented: the stated information set constrains none of them, so their bits can be adjoined identically zero. Nothing
is asserted about them, and B_λ ∩ {π ≡ 0} is a model event, not a lower bound for the arithmetic A_N.

*Facts about r_j (PROVED).* (α) On the support of r_{e,m}, v_q(x + 4e) = v_q(m) for every prime q ≤ z, so m is the full
z-smooth part of x + 4e; for fixed (x, e) at most one m has r_{e,m}(x) > 0. Thus the true exclusivity "n + 4e has at
most one cofactor m ≤ z with (n + 4e)/m a prime > z" holds in every model satisfying (I4) below. (β) If r_j(x) > 0 and a
CRT event (ℓ′, e_j) with ℓ′ ≤ z meets x, then ℓ′ | m_j, as for integers. (γ) r_j ≤ C₁λ/(log N − λ): with Q = lcm(8, 4e),
ℋ(class_j) = 8/(m_jQ), the roughness probability on the class is ∏_{p≤z, p∤Q}(1 − 1/p) ≍ Q/(φ(Q) log z), and
Brun–Titchmarsh gives #E^{PD}_j/#I ≪ 1/(m_jφ(Q)(log N − λ)); divide. So r_j ≤ 1/C once λ ≤ c_C log N.
(δ) *Arithmetic meaning on modulus-bounded tests.* Let S be a class b (mod d) with d ≤ z. Under x = m_jp − 4e_j, class_j is
one reduced candidate class p ≡ a (mod Q) (a ≡ −1 (mod 4e_j), m_ja − 4e_j ≡ 1 (mod 8); incompatible pairs are the
empty classes), and S becomes p ≡ c (mod d/g), g = gcd(m_j, d), or is empty if g ∤ b + 4e_j. Put L = lcm(Q, d) (all its
prime factors are ≤ z), R = {a′ mod L : a′ ≡ a (mod Q), gcd(a′, L) = 1}, R_S = {a′ ∈ R : m_ja′ − 4e_j ≡ b (mod d)} and
ϖ_j(S) = |R_S|/|R|. Haar gives equal mass to the extensions of the base class modulo L, the roughness factor kills
exactly the non-reduced ones and multiplies each reduced one by the same ∏_{q≤z, q∤L}(1 − 1/q); hence
E_ℋ[1_S r_j] = (#E^{PD}_j/#I)·ϖ_j(S): the Siegel–Walfisz/BV equidistribution proportion, normalised by the true global
count. ϖ_j(S) vanishes exactly when S is locally inadmissible (E_ℋ[1_S r_j] also vanishes when the global count is 0).
Positive main term does not mean positive finite count; BV is an averaged statement.

An argument of **type (λ; K₂, K₃, …)** uses the integers only through statements implied by the following axioms.

* (I1) *CRT data at level λ:* E f(x) = E_ℋ f for every f of level ≤ λ (finite combinations of class indicators b mod d
  with Σ_{slice ℓ | d} log ℓ ≤ λ, THETA §1).
* (I2) *PD first moments on modulus-bounded tests, exact:* P(π_j = 1, x ∈ S) = E_ℋ[1_S r_j] for every j and every class S
  of modulus ≤ z.
* (I3) *PD correlations, one-sided:* P(π_J ≡ 1, x ∈ S) ≤ K_k E_ℋ[1_S ∏_{j∈J} r_j] for every k ≥ 2, J ⊆ 𝒥 with |J| = k,
  and every clopen S.
* (I4) *Support:* π_j = 0 wherever r_j = 0.

By (δ), (I2) says that primes in the candidate variable are equidistributed among the admissible reduced classes
modulo the induced moduli L₀ = lcm(Q, d/gcd(m_j, d)), normalised by the true total. Write A_j = #E^{PD}_j,
A_j(S) = #(E^{PD}_j ∩ S), and let M_j be the conventional main term (Li(X_j) − Li(z))/φ(Q), X_j = (N + 4e_j)/m_j. If
A_j = M_j + R_j and A_j(S) = ϖ_j(S)M_j + R_j(S), then A_j(S) − ϖ_j(S)A_j = R_j(S) − ϖ_j(S)R_j, so an available error bound
transfers as |A_j(S) − ϖ_j(S)A_j| ≤ |R_j(S)| + ϖ_j(S)|R_j| (for averaged bounds, summed with the actual weights). The
distribution theorem must be applied at modulus L₀ ≤ 2z²/m_j in the candidate variable X_j: Siegel–Walfisz in its
logarithmic range, BV only on average in its X_j-dependent range. With this ledger, an exact axiom implies every
inequality |count − main term| ≤ error centred at the same normalised main term. So arguments that use SW/BV/BT-type
equidistribution of the PD candidates on such tests (within those ranges), sieve upper bounds of I3 form, CRT data at
level λ, and the support facts (α)–(β), are covered. Not covered: first-moment tests outside the modulus-bounded family
(e.g. classes with a large uncharged prime or a large prime power), two-sided correlations of order ≥ 2 (even averaged),
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
(4) *Fake laws.* As in Thm 2.3(i), but on a finite quotient that retains the full relevant prime-power digits (the
realised W2 avoider may depend on them) and with the dual run directly on the fibre 1 + 8Ẑ, there is a probability
ρ_{𝒥′} with Haar marginals on every class of level ≤ λ and ρ_{𝒥′}(𝒜(𝔊(𝒥′))) ≥ e^{−C√λ}; off the event of (2), put
ρ_{𝒥′} = ℋ.
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
functions at many shifts. Verdict: product-form bounds over shifts with a common loss C > 1 per factor save only
≪ (log log N)² log log log N (Prop 3.1); for upper bounds one layer suffices (Lemma 3.2), which reduces T1-min, and a power saving, to
the top band (Cor 3.3); there the fixed-scale zero probabilities match e^{−mean} (§3.3). No proof of the top-band statement is
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
(b) Choose E₁′(N) = O(L₂L₃) with hit(e) ≤ ½ for e > E₁′(N) (Lemma 3.0(b); no absolute cutoff exists, since for each fixed
e, hit(e) → 1 as N → ∞). Shifts e ≤ max(E₁, E₁′(N)) contribute O(L₂²L₃) as in (a).
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
  #{n ≤ N, n ≡ 1 (4) : U(n) fails} = #{odd squares ≤ N} + O(N^{1−c}) (a power saving for E_U off the squares), and,
  with ES₅ defined globally by a positive word with a slot ≡ 0 (mod 4) (EXSET_BEYOND_CRT §1.3; automatic at p = 2 via
  (t, u, v) = (1, 2, 4) and at p ≡ 3 (4) via (2, 1, p + 1)),
  #{p ≤ N : ES₅(p) fails} = #{p ≤ N, p ≡ 1 (4) : ES₅(p) fails} ≤ #{p ≤ N, p ≡ 1 (4) : U(p) fails} ≪ N^{1−c}
  (EXSET_SIEVE_MASS Thm 3.5(a) for the inequality), i.e. z50 Target 1 for ES₅ and U.
*Proof.* A U failure at n ≡ 1 (8) lies in no prime-pivot U certificate class, so it lies in A_N ⊆ {X_top = 0}; U holds at
every n ≡ 5 (mod 8), n > 5 (v = 3, A = 8; z50 Obs. 6.0); odd squares fail U (Theorem E), which gives the main term;
primes are not squares. ∎

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
which still mix scales by a factor 2. So at N = 10⁹ the stratification accounts for about 81% of the excess zeros
(69 448 zeros remain above the stratified prediction; narrower bins or other arithmetic features may explain them; this
is a finite-scale decomposition, not an identification of the cause). Fixed-scale samples follow.

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

At a fixed scale the zero probability agrees with e^{−E X_top} within about two standard errors (standardised
differences 1.5, 0.5, −1.9, 0.65, accounting for the fitted mean), but the full law is not Poisson: Var X_top − E X_top is
7–10 standard errors above zero at every scale (R3 §6.1), and 20-bin stratification in n removes only a small part of
it. The mean grows by ≈ 0.74 per decade, i.e. slope ≈ 0.32 against ln N (mean ≈ 0.319 ln N − 1.20 over this range; the
ratio mean/ln N is 0.253–0.271), and log P(X_top = 0) falls by ≈ 0.83 per decade between 10⁸ and 10¹⁰. The candidate
count C_top is ≈ 0.08 (log N)² on average (0.076, 0.078, 0.080, 0.081 times (ln N)²), and its lower tail thins quickly
(P(C_top ≤ 20) = 0.29, 0.097, 0.021, 0.003). The aggregate fit E X_top/E Σ_cand 1/log p is ≈ 2.46 (a fitted weighting, not a calibrated primality
probability per candidate); the mixed-Poisson prediction E e^{−2.46 Σ 1/log p} fails in both directions across deciles,
so the primality events are not a simple function of the candidate count. Reading (Assessment): the zero probability
at fixed scale tracks e^{−mean}, and the mean grows like ≈ 0.32 ln N over these scales; if this persisted, TB_pow would
hold with c ≈ 0.3. These are finite-range samples; no asymptotic, no independence statement and no exponent is proved.

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

**R3 (`reviews/z51-dbreak-review-3.md`).** Rows 1, 2a, 2c, 2d, 3e, 4, 5 SOUND; 2b, 2e, 3a, 3b, 3c, 6 SOUND-WITH-MINOR;
3d MAJOR for wording (counts SOUND). The modulus-bounded test family cures the round-2 counterexample: the local
identity (δ) was rederived in the candidate variable (induced modulus, mod-8 condition, prime powers) and no
replacement counterexample was found; Thm 2.6 repairs pass. The reviewer regenerated 12 sampled rows and checked 40 n
by an independent e-view implementation (all agree), recomputed both numerical tables, and found the fixed-scale X_top
significantly over-dispersed (Var − mean 7–10 s.e. above 0) although its zero probability matches e^{−mean} within
≈ 2 s.e. Repairs (final): "Poisson within sampling error" replaced by the zero-probability statement everywhere; the
mean described by its fitted slope (≈ 0.32 per unit ln N) and intercept; the scale stratification described as
accounting for 81% of the excess at N = 10⁹; the false absolute cutoff in Prop 3.1(b) replaced by E₁′(N) = O(L₂L₃) (for
fixed e, hit(e) → 1); ϖ_j defined explicitly with the induced modulus and the normalised error ledger stated; omitted
events = all events outside 𝒥; Cor 3.3's ES₅ conclusion written on its domain with the global word/slot definition;
Thm 2.6's quotient and fibre stated; §8 wording; the cross-check harness hardened. Not accepted: none.

## 8. Exact remaining gap

* **No depth-breaking bound is proved.** T1-min(4ℤ) would follow from TB_δ, and a power saving for E_U off the squares
  and for ES₅ at primes from TB_pow (Cor 3.3). Polynomial-level CRT majorants cannot supply an exponential-in-mass
  saving from the top band (they save O(log log N) there). At a fixed scale the top band's zero probability matches
  e^{−mean} within about two standard errors at N = 10⁸–10¹¹, with the mean growing ≈ 0.32 per unit of ln N
  (EVIDENCE; the full law is over-dispersed). This is consistent with TB_pow for some c ≈ 0.3; nothing asymptotic is
  established.
* **What is excluded, and only in this scope.** Arguments using CRT data at level λ, exact PD first moments on
  modulus-bounded tests, one-sided PD correlation bounds with K_k ≥ C^{k−1} and the support facts gain a constant
  (Thm 2.3). In the class-constant Cramér model, two-sided mixed statistics below the level cap gain nothing in the
  exponent (Thm 2.6); the arithmetic version needs a sieve-limit theorem for roughness-refined (prime-law) majorants.
  Product-form shift bounds with a common loss C > 1 save ≪ (log log N)² log log log N, and with a common loss 1 + ε
  need log(1/ε) ≳ M/log log N (Prop 3.1). The raw Chebyshev bound with constant centering stops at ≫ N/μ in the Haar
  model (Prop 4.1).
* **What is not excluded.** True (roughness-aware) two-sided PD correlations below or above the level cap; union lower
  bounds for a block of mass ≫ √(log N) (that is the target in another form); weighted or nonlinear uses of the
  incidence; signed interval sums at moduli above N; archimedean relations; heterogeneous, exact or sufficiently
  accurate shift factors; amplifications of bounded-order correlation inputs.
* **The cleanest open statement this lane isolates:** TB_pow (or TB_δ) for the single layer ℓ > √(2N): a zero-event
  upper bound for the hits "P⁺(n + 4e) ≡ −1 (mod 4e), P⁺(n + 4e) > √(2N)" over the shifts e. It is not supplied by the
  cited two-shift theorems on largest prime factors, which concern sizes, not residues.
* **Transfer to the full prime family 𝓕_N.** Upper bounds transfer (A_N ⊇ Av(𝓕_N)). Theorems 2.3 and 2.6 are proved
  for the 4ℤ-line classes. The CRT fake law and the CH construction plausibly extend to the full refined U family with
  adjusted supply constants (Assessment); the exact roughness/cofactor parametrisation and the first-moment transfer
  for the 8ℤ+7 line need their own proof.

## 9. Round 4: the board's astra-5 programme (quadratic-orthogonal residual) — drop-screen and cumulants

*Requested after the board memo `/home/pasky/.pi/boards/20261029-depth-break/memo.md` (finalist 3: astra-5 ⊕ fable-3).*

### 9.0 Summary (round 4)

**Status: round 4 written; Astra review pending. No target reached.** The drop-screen does not drop the route: the
normalised log-mgf of the residual tracks the independent model within 0.02, with no growth in μ, at β = 0.6, 0.75, 0.9
(N ≤ 10¹⁰) and on the top band (N ≤ 10¹¹). The cumulant lemma is proved exactly in the CRT range j ≤ (log N)^{1−β}; the
lemma needs j up to (log N)^{1/2+δ}, and that window is depth.

| # | statement | label | § | review |
|---|---|---|---|---|
| 9a | algebra of R (zero on residues, orthogonal to 1 and to (·/ℓ)); avoiders have R = −μ + Q + o(1); T1-min ⟸ (L_C) for β > 1/2 | PROVED (elementary; quadratic-piece rarity as on the board) | §9.1 | — |
| 9b | drop-screen: (1/(μt²))log E e^{−t(R−ER)} within 0.02 of the independent model, excess decreasing in N (β = 0.6, 0.75) or negative (β = 0.9; Var R 4–5% below model); no growth with μ | CERTIFIED (exact rows) / EVIDENCE | §9.2 | — |
| 9c | negative tail follows the exact independent law (slightly below it); most negative n have typical profile and no kernel enrichment: no coherent residual component found | EVIDENCE | §9.3 | — |
| 9d | top band: the quadratic piece is negligible off N^{3/4+ε} integers, so the top-band (L_C) ⟹ TB_pow (power saving off squares, ES₅ at primes); its normalised mgf is flat and near Poisson (N ≤ 10¹¹); band and disjoint large layers nearly independent (corr −0.02, −0.04) | PROVED (Heath-Brown QLS) / EVIDENCE | §9.4 | — |
| 9e | κ₂(R) = Σσ² + O(N^{−1+o(1)}) in the subexponential band; E_I R² ≤ (1 + 8z²/N)Σσ² for every z (large sieve); beyond √N the excess is fable-3's Kloosterman-fraction sum, numerically negative for the residual | PROVED / EVIDENCE | §9.5 | — |
| 9f | |κ_j(R)| ≤ 1.44 j!Σσ² + j!(6W_B)^j/|I| for all j, so |κ_j| ≤ 3j!Σσ² for j ≤ (1−o(1))(log N)^{1−β}; via moments, (L_C)'s conclusion needs j up to (log N)^{1/2+δ}; the gap (log N)^{1−β} < j ≤ (log N)^{1/2+δ} is exactly the beyond-level window (cumulant form of G1) | PROVED | §9.6 | — |

### 9.1 Setup and the algebra of the residual

Band: B = {ℓ prime, ℓ ≡ 3 (mod 4), y < ℓ ≤ z}, z = exp((log N)^β), y = √z. (On the 4ℤ line only ℓ ≡ 3 (4) carry
classes.) F_ℓ(n) = 1[n ≡ −4e (mod ℓ) for some e with 4e | ℓ + 1], w(ℓ) = τ((ℓ+1)/4), c_ℓ = w(ℓ)/(ℓ − 1), μ = Σ_B c_ℓ,
and, as in the board's astra-5,

    R_ℓ(n) = F_ℓ(n) − c_ℓ[1_{ℓ∤n} − (n/ℓ)],    R(n) = Σ_{ℓ∈B} R_ℓ(n),    Q(n) = Σ_{ℓ∈B} c_ℓ (n/ℓ).

**Lemma 9.1 (PROVED, elementary).**
(a) R_ℓ(n) = 0 if ℓ | n or (n/ℓ) = 1; R_ℓ(n) = F_ℓ(n) − 2c_ℓ if (n/ℓ) = −1. In particular |R_ℓ| ≤ 1 and R(x²) = 0.
(b) Σ_{a mod ℓ} R_ℓ(a) = 0 and Σ_{a mod ℓ} R_ℓ(a)(a/ℓ) = 0.
(c) If n avoids every class of B, then R(n) = −μ + Q(n) + Σ_{ℓ∈B, ℓ|n} c_ℓ.
(d) In the independent (Haar) model, R_ℓ has mean 0, variance σ_ℓ² = (w/ℓ)(1 − 2c_ℓ)² + ((ℓ−1)/(2ℓ) − w/ℓ)·4c_ℓ², and
    E e^{−tR_ℓ} = (ℓ+1)/(2ℓ) + (w/ℓ)e^{−t(1−2c_ℓ)} + ((ℓ−1)/(2ℓ) − w/ℓ)e^{2tc_ℓ}.
(e) #{n ∈ I : n avoids B} ≤ #{n ∈ I : Q(n) ≥ μ/2 − Σ_{ℓ|n}c_ℓ} + #{n ∈ I : R(n) ≤ −μ/2}.
*Proof.* (a) Every forbidden class is a non-residue (Lemma 1.2); on non-residues 1_{ℓ∤n} − (n/ℓ) = 2. (b) Σ_a F_ℓ = w =
c_ℓ(ℓ − 1) = Σ_a c_ℓ(1_{a≠0} − (a/ℓ)); Σ_a F_ℓ(a)(a/ℓ) = −w = Σ_a c_ℓ(1_{a≠0} − (a/ℓ))(a/ℓ). (c) Sum (a) with F ≡ 0.
(d) Direct. (e) From (c). ∎

The quadratic piece is rare (board, PROVED there; recorded): Σ_{n∈I} Q(n)² ≤ |I|Σ_B c_ℓ² + Σ_{ℓ≠ℓ′} c_ℓc_ℓ′·O(√(ℓℓ′) log ℓℓ′)
(Pólya–Vinogradov for the character (·/ℓℓ′) on an AP mod 8), so #{n ∈ I : Q(n) ≥ μ/4} ≪ μ^{−2}(N y^{−1+o(1)} + z(log z)^{O(1)}),
which is ≤ N exp(−(½ − o(1))(log N)^β). And Σ_{ℓ|n} c_ℓ ≤ ω(n) max_B c_ℓ ≤ (log N)y^{−1+o(1)} = o(1). So T1-min(4ℤ) for
β > 1/2 follows from #{R ≤ −μ/2} ≤ N exp(−(log N)^{1/2+δ}), in particular from the board's lemma

> **(L_C)** E_{n∈I} exp(−tR(n)) ≤ exp(Ct²μ) for some fixed C and all 0 < t ≤ t₀,

via Markov at t = min(t₀, 1/(4C)): P(R ≤ −μ/2) ≤ exp(−tμ/4).

The independent model satisfies (L_C) with C ≈ ½: (1/(μt²)) log E e^{−tR} = (e^{−t} − 1 + t)/t² + O(max c_ℓ) (by (d)).

### 9.2 Drop-screen along z = exp((log N)^β)

**Method (CERTIFIED for exact rows, EVIDENCE for sampled rows).** `scripts/z51_dbreak_resid.c`: `exact` mode computes R(n)
for every n ∈ I ∖ □ (table of R_ℓ per prime, accumulated along the progression); `sample` mode computes R(n) by
Jacobi symbols for random n ∈ I ∖ □. Both print the independent-model value Σ_ℓ log E e^{−tR_ℓ} (Lemma 9.1(d)).
`scripts/z51_dbreak_resid_analyze.py` reports, for the *centred* residual (the first cumulant E_I R is a rounding
artefact of size ≤ 2W_B/|I| by Prop 9.3(a); it is 10⁻²–10⁻⁸ here),

    A(t) = (1/(μt²))·log E_{I∖□} e^{−t(R − E R)},     A_mod(t) = (1/(μt²))·Σ_ℓ log E e^{−tR_ℓ},     excess = A − A_mod.

Checks: the sampler reproduces the exact β = 0.9, N = 10⁸ row (excess −0.0170 ± 0.009 vs −0.0173); an earlier version of
the hit test missed the class n ≡ −1 (4e = ℓ + 1) and gave a spurious mean −0.32, found because the mean must vanish
(Lemma 9.1(b)) and fixed before any row below was produced.

| β | N | z | primes in B | μ | Var_I R/Σσ² | A(0.25) (model) | excess(0.25) | A(1) (model) | excess(1) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.6 | 10⁷ | 201 | 21 | 1.303 | 1.0015 | 0.3797 (0.3791) | +0.0006 | 0.3251 (0.3247) | +0.0004 |
| 0.6 | 10⁸ | 312 | 31 | 1.540 | 1.0004 | 0.3879 (0.3877) | +0.0002 | 0.3296 (0.3295) | +0.0002 |
| 0.6 | 10⁹ | 475 | 42 | 1.638 | 1.0001 | 0.3973 (0.3972) | +0.00006 | 0.3349 (0.3348) | +0.00006 |
| 0.6 | 10¹⁰ | 711 | 60 | 1.662 | 1.0000 | 0.4144 (0.4143) | +0.00002 | 0.3445 (0.3445) | +0.00003 |
| 0.75 | 10⁷ | 3 116 | 216 | 2.190 | 1.020 | 0.4473 (0.4380) | +0.0093 | 0.3637 (0.3569) | +0.0068 |
| 0.75 | 10⁸ | 7 271 | 459 | 2.374 | 1.007 | 0.4510 (0.4471) | +0.0039 | 0.3647 (0.3615) | +0.0032 |
| 0.75 | 10⁹ | 16 528 | 948 | 2.718 | 1.002 | 0.4522 (0.4503) | +0.0018 | 0.3650 (0.3630) | +0.0020 |
| 0.75 | 10¹⁰ (80 000 samples) | 36 733 | 1 937 | 2.946 | 1.004 | 0.4555 (0.4536) | +0.0019 ± 0.0075 | 0.3660 (0.3646) | +0.0014 ± 0.0018 |
| 0.9 | 10⁷ | 2.0·10⁵ | 8 964 | 3.500 | 0.950 | 0.4380 (0.4576) | −0.0196 | 0.3565 (0.3664) | −0.0100 |
| 0.9 | 10⁸ | 9.5·10⁵ | 37 456 | 4.025 | 0.956 | 0.4419 (0.4593) | −0.0173 | 0.3582 (0.3672) | −0.0090 |
| 0.9 | 10⁹ (120 000 samples) | 4.4·10⁶ | 155 593 | 4.508 | 0.959 | 0.4442 (0.4601) | −0.0158 ± 0.0050 | 0.3598 (0.3675) | −0.0077 ± 0.0015 |
| 0.9 | 10¹⁰ (120 000 samples) | 2.0·10⁷ | 644 321 | 5.018 | 0.964 | 0.4468 (0.4604) | −0.0137 ± 0.0048 | 0.3609 (0.3677) | −0.0068 ± 0.0015 |

(t = 0.1 and 0.5 behave the same way; all values in `data/z51_dbreak/resid_exact_*`, `samp_*`.)

**Verdict of the screen (EVIDENCE).** The board's drop condition, "the normalised quantity grows with μ along fixed β",
is **not met** at any β. A(t) stays within 0.02 of the independent-model value A_mod(t) ≈ (e^{−t} − 1 + t)/t² (≈ 0.46 at
t = 0.25, 0.37 at t = 1), and the excess decreases in |·| as N grows: to 2·10⁻⁵ at β = 0.6, to 0.002 at β = 0.75. At
β = 0.9, where z² > N and pairs of band primes are already beyond level, the excess is **negative** (the residual is
4–5% less dispersed than independent) and drifts towards 0. The range of μ is small (1.3–5.0); the screen can falsify,
not confirm, and it cannot see the cumulant orders j ≍ (log N)^{1/2+δ} that the lemma needs (§9.6).

### 9.3 The negative tail

`scripts/z51_dbreak_resid_tail.py` compares the empirical histogram of an exact run with the exact independent-model law
(R = H − D: dynamic programme in the hit count H with the conditional mean and variance of the drift D = 2Σ_{nonres}c_ℓ;
a grid convolution is useless here because it rounds the drifts −2c_ℓ ~ 10⁻⁵ to 0), and inspects the 200 most negative n.

| β, N | P(R ≤ −μ/2): emp / model | P(R ≤ −3μ/4): emp / model | P(R ≤ −μ): emp / model |
|---|---|---|---|
| 0.6, 10¹⁰ | 0.2535 / 0.2547 | 0.1575 / 0.1609 | 0.0604 / 0.0647 |
| 0.75, 10⁹ | 0.2396 / 0.2380 | 0.0717 / 0.0705 | 0.0272 / 0.0271 |
| 0.9, 10⁷ | 0.1324 / 0.1380 | 0.0379 / 0.0428 | 0.0140 / 0.0135 |
| 0.9, 10⁸ | 0.1599 / 0.1673 | 0.0520 / 0.0537 | 0.0068 / 0.0082 |

(thresholds rounded to the 0.02 histogram bins; at β = 0.75 the far tail R ≤ −1.25μ has 1.9·10⁻⁶ emp. vs 3.2·10⁻⁶ model.)
The lower tail follows the independent law, slightly *below* it where the screen sees a difference. The most negative
n: at β = 0.75, 0.9 they are band avoiders (H = 0) with a typical quadratic profile (non-residue fraction 0.50–0.53, as for
random n) and no small-kernel enrichment (squarefree kernel ≤ 10⁴: 0–1.5%, random 0–3%; 6.5% vs 3% at the smallest run);
at β = 0.6 (μ = 1.7) they are profile-driven (non-residue fraction 0.74), which the independent law also predicts at that μ.
**No coherent residual component was found**, in contrast with the raw count, where the squares and the quadratic
profile are coherent (squares have R = 0 by Lemma 9.1(a)).

### 9.4 The top band

**Proposition 9.2 (the top-band quadratic piece is negligible; PROVED given Heath-Brown's quadratic large sieve).** Let
B_top = {ℓ ≡ 3 (4) prime : √(2N) < ℓ ≤ N} and Q_top(n) = Σ_{B_top} c_ℓ(n/ℓ). For every ε > 0 and η > 0,

    #{n ≤ N odd : |Q_top(n)| ≥ η} ≪_ε N^{3/4+ε}η^{−2}.

*Proof.* Σ_{B_top} c_ℓ² ≪ Σ_{ℓ>√N} ℓ^{−2+ε} ≪ N^{−1/2+ε} (w(ℓ) ≤ ℓ^{o(1)}). Write n = n₁n₂², n₁ squarefree. Since every
ℓ ∈ B_top exceeds n₂ ≤ √N, (n/ℓ) = (n₁/ℓ), and by reciprocity (n₁/ℓ) = ±(ℓ/n₁) with a sign depending only on n₁ mod 4.
Heath-Brown's bound Σ*_{m≤M}|Σ*_{ℓ≤L} a_ℓ(ℓ/m)|² ≪ (ML)^ε(M + L)Σ|a_ℓ|² (odd squarefree m, ℓ), with M = N/n₂², L = N, gives
Σ_{n₁}|Q_top(n₁n₂²)|² ≪ N^{1/2+2ε} for each n₂. So the count is ≤ #{n : n₂ > Z} + Σ_{n₂≤Z} N^{1/2+2ε}η^{−2} ≪ N/Z + ZN^{1/2+2ε}η^{−2};
take Z = N^{1/4}. ∎

So on the top band the board's projection costs nothing: off a set of N^{3/4+ε} integers R_top = X_top − μ_top + o(1) in
the regime that matters (if X_top(n) = 0 then R_top(n) = −μ_top + Q_top(n) + O(N^{−1/2+ε})), with μ_top = Σ_{B_top}c_ℓ ≍ log N.
Hence **the top-band version of (L_C) — E_I e^{−t(R_top − E R_top)} ≤ e^{Ct²μ_top} for small fixed t — implies TB_pow
(Cor 3.3), i.e. a power saving for E_U off the squares and for ES₅ at primes**, stronger than T1-min. (E_I R_top is a
bounded negative constant: the Haar densities w/ℓ overstate the hit rate for ℓ > (n + 4e)/3, Lemma 1.1(d).) In the top
band no cumulant is CRT-accessible (all band primes exceed √N), so Theorem 9.4 gives nothing there; it is the band where
the depth problem is purest.

*Numerics (EVIDENCE, fixed scale n ∈ [N/2, N], data of §3.3; Q_top neglected per Prop 9.2):*
(1/(μt²))·log E e^{−t(X_top − E X_top)} with μ = E X_top:

| N | μ | t = 0.25 (Poisson 0.4608) | t = 1 (Poisson 0.3679) |
|---:|---:|---:|---:|
| 10⁸ | 4.67 | 0.4710 ± 0.0055 | 0.3713 ± 0.0016 |
| 10⁹ | 5.42 | 0.4747 ± 0.0052 | 0.3716 ± 0.0016 |
| 10¹⁰ | 6.16 | 0.4743 ± 0.0049 | 0.3697 ± 0.0016 |
| 10¹¹ | 6.87 | 0.4853 ± 0.0086 | 0.3760 ± 0.0032 |

Flat in μ, within 0.025 of the Poisson value: the drop condition is not met on the top band either.

*Joint behaviour of the two layers (EVIDENCE; `scripts/z51_dbreak_joint.py`, `data/z51_dbreak/joint_*`).* Is the band
residual's lower tail governed by the top band? No. With disjoint layers, the band residual R and the large-prime layer X
are nearly independent and slightly negatively correlated:

| layers | corr(R, X) | P(X = 0) | P(X = 0 \| R ≤ −μ/2) | P(both)/product |
|---|---:|---:|---:|---:|
| β = 0.75, N = 10¹⁰: band (192, 3.7·10⁴] vs top ℓ > √(2N) | −0.022 ± 0.007 | 0.00515 | 0.00533 | 1.03 |
| β = 0.9, N = 10⁹: band (2.1·10³, 4.4·10⁶] vs layer ℓ > 4.5·10⁶ | −0.044 ± 0.007 | 0.158 | 0.141 | 0.89 |

(20 000 sampled n each.) The naive comparison at β = 0.9 with the top band ℓ > √(2N) gives corr +0.50, but there the two
bands overlap on (√(2N), z]; that is an artefact, recorded in `joint_Xtop_overlap_b0.9_N1e9.txt.gz`. The negative sign
for disjoint layers has the same archimedean source as in §9.5: one shifted integer n + 4e cannot carry two large
event primes whose product exceeds it. So the layers can be combined (Lemma 3.2 does not even need this), and neither
explains the other's tail.

### 9.5 The second cumulant

Write Σσ² := Σ_B σ_ℓ² (≈ μ: σ_ℓ² = c_ℓ(1 + O(c_ℓ)) by Lemma 9.1(d)) and W_B := Σ_B w(ℓ) ≤ C_T z (divisor pairing and
Brun–Titchmarsh). E_I is the average over I = {n ≤ N : n ≡ 1 (8)}; removing the √N squares (where R = 0) multiplies all
moments by 1 + O(N^{−1/2}).

**Proposition 9.3 (PROVED).**
(a) |E_I R| ≤ 2W_B/|I| ≪ z/N.
(b) (CRT range) |E_I R² − Σσ²| ≤ 2(6W_B)²/|I| + (2W_B/|I|)² (the case j = 2 of Theorem 9.4); in the subexponential band
    this is N^{−1+o(1)}, so κ₂(R) = Σσ² + O(N^{−1+o(1)}): the j = 2 cumulant is *exactly* the independent-model value.
(c) (all z, large sieve) E_I R² ≤ (1 + 8z²/N + O(N^{−1}))·Σσ². So κ₂(R) ≤ (1 + o(1))Σσ² for z = o(√N), and κ₂ = O(μ) for
    z ≤ C√N, with no arithmetic input beyond Lemma 9.1(b).
*Proof.* (a) For a function g periodic mod q (q odd), each class mod q contains |I|/q + θ elements of I, |θ| ≤ 1, so
|E_I g − E g| ≤ |I|^{−1}Σ_{a mod q}|g(a)|; and Σ_a|R_ℓ(a)| = w|1 − 2c| + ((ℓ−1)/2 − w)·2c ≤ 2w. (c) As a function of
k (n = 8k + 1), R_ℓ has period ℓ and mean 0, so R(8k+1) = Σ_ℓ Σ_{h≢0 (ℓ)} b_ℓ(h)e(hk/ℓ) with Σ_h|b_ℓ(h)|² = σ_ℓ²
(Parseval). The frequencies h/ℓ (ℓ ∈ B prime) are 1/z²-spaced, and the Montgomery–Vaughan large sieve gives
Σ_{k≤|I|} R(8k+1)² ≤ (|I| + z²)Σσ². ∎

*Beyond √N (fable-3).* For z > √N, E_I R² − Σσ² = Σ_{ℓ≠ℓ′} Cov_I(R_ℓ, R_ℓ′) + O(W_B/|I|), and the pairs with ℓℓ′ ≤ N^{1−ε}
contribute O(N^{−ε}(log)^{O(1)}) by (a) applied to g = R_ℓR_ℓ′. The pairs with ℓℓ′ > N are fable-3's Kloosterman-fraction
sum; (c) bounds them by 8z²/N·Σσ², which is not O(μ) once z ≫ √N. No better unconditional bound is proved here.
Numerically (§9.2) the beyond-level covariance of the *residual* is **negative**: Var_I R/Σσ² = 0.95–0.96 at β = 0.9
(z = N^{0.76…0.68}, N = 10⁷–10⁹). A mechanism (Assessment): two hits ℓ, ℓ′ on the same shift e need ℓℓ′ | n + 4e, which
is impossible when ℓℓ′ > n + 4e; the independent model counts such pairs, the integers do not (an archimedean exact zero,
§2.3(d)). This sign is the favourable one for (L_C), and it is the opposite of the raw count X, whose excess variance
(fable-3, positive) comes from the quadratic profile that R removes.

### 9.6 Higher cumulants: the range proved and the range needed

**Theorem 9.4 (PROVED).** For every j ≥ 2,

    |κ_j(R)| ≤ 1.44·j!·Σσ² + j!·(6W_B)^j/|I|,

where κ_j is the j-th cumulant of R(n), n uniform on I. Consequently |κ_j(R)| ≤ 3·j!·Σσ² for all
2 ≤ j ≤ J₀ := log(|I|Σσ²)/log(6C_T z) = (1 + o(1))(log N)^{1−β}.

*Proof.* (Model.) The R_ℓ are independent, mean 0, |R_ℓ| ≤ 1, σ_ℓ² ≤ 0.69. For complex |s| ≤ 1,
|E e^{sR_ℓ} − 1| = |E(e^{sR_ℓ} − 1 − sR_ℓ)| ≤ σ_ℓ²(e − 2) ≤ ½, so |log E e^{sR_ℓ}| ≤ 1.44σ_ℓ², and Cauchy's estimate on |s| = 1
gives |κ_j(R_ℓ)| ≤ 1.44·j!·σ_ℓ²; sum over ℓ. (Integers.) By multilinearity κ_j(R) = Σ_{(ℓ₁,…,ℓ_j)∈B^j} κ(R_{ℓ₁}, …, R_{ℓ_j}),
and in the model the joint cumulant vanishes unless ℓ₁ = ⋯ = ℓ_j. A joint cumulant is Σ_π (−1)^{|π|−1}(|π| − 1)!∏_{b∈π} m_b
over set partitions π of [j], m_b the joint moment of the block. Each block function ∏_{i∈b}R_{ℓ_i} is periodic modulo the
product q_b of its distinct primes, so by the argument of Prop 9.3(a) its I-moment differs from the model moment by
δ_b ≤ |I|^{−1}∏_{distinct ℓ ∈ b}(ℓ E|R_ℓ|) ≤ |I|^{−1}∏_{i∈b}2w(ℓ_i), while |m_b^{mod}| ≤ 1. Hence the product over blocks changes by
≤ Σ_{∅≠S⊆π}∏_{b∈S}δ_b ≤ 2^{|π|}|I|^{−1}∏_i 2w(ℓ_i), and the joint cumulant by ≤ |I|^{−1}∏_i 2w(ℓ_i)·Σ_π(|π| − 1)!2^{|π|}
≤ j!3^j|I|^{−1}∏_i 2w(ℓ_i) (Σ_k S(j, k)(k − 1)!2^k ≤ j!3^j, checked to j = 40 and asymptotically ≈ j!·2.47^j). Sum over
B^j. ∎

**What (L_C) needs.** Let μ′ = Σσ² ≤ μ(1 + o(1)).
*Lemma 9.5 (PROVED, standard).* If |κ₁| ≤ 1 and |κ_j(R)| ≤ j!C^jμ′ for 2 ≤ j ≤ 2k, with k ≤ μ′/4, then
E R^{2k} ≤ O(√k)(4eC²kμ′)^k, hence P(R ≤ −μ/2) ≤ O(√k)(16eC²kμ′/μ²)^k ≤ O(√k)(C′k/μ)^k.
*Proof.* E R^{2k} depends only on κ₁, …, κ_{2k}, and E R^{2k} = (2k)![s^{2k}]exp(Σ_{j≤2k}κ_j s^j/j!) ≤ (2k)! r^{−2k}
exp(r + μ′C²r²/(1 − Cr)) for 0 < r < 1/C. Take r² = k/(C²μ′) (so Cr ≤ ½) and (2k)! ≤ O(√k)(2k/e)^{2k}. Markov. ∎
So, with μ ≍ (log N)^β: cumulant control up to order 2k = 2(log N)^γ gives P(R ≤ −μ/2) ≤ exp(−(β − γ − o(1))(log N)^γ log log N).
* **Needed** for T1-min (saving (log N)^{1/2+δ}, with β > 1/2 + δ so that the quadratic piece and μ are large enough):
  cumulant bounds |κ_j| ≤ j!C^jμ for **2 ≤ j ≤ (log N)^{1/2+δ}** (any γ ≥ 1/2 + δ); the full mgf form (L_C) asks for every j,
  but beyond j ≍ μ the moment route needs nothing more.
* **Proved** (Theorem 9.4): **2 ≤ j ≤ (1 − o(1))(log N)^{1−β}**, i.e. γ ≤ 1 − β < 1/2 − δ.
* The missing window (log N)^{1−β} < j ≤ (log N)^{1/2+δ} is nonempty exactly because β > 1/2: it consists of the cumulants
  whose prime tuples have product > N, i.e. depth. With the proved range alone, Lemma 9.5 gives
  P(R ≤ −μ/2) ≤ exp(−c(2β − 1)(log N)^{1−β}log log N), and the overall bound is optimised near β = ½, where it is the CRT
  exponent ½ (G1) again. So Theorem 9.4 is the cumulant form of G1, and (L_C) beyond it is equivalent in strength to
  depth breaking.
* At polynomial z = N^{1/s} (s < 2) the proved range is only j ≤ s: already κ₂ is beyond level (§9.5).

### 9.7 Review and remaining gap

**Review.** Pending (Astra, round 4).

**Remaining gap after round 4.**
* astra-5's lemma (L_C) is consistent with all data: no growth of the normalised log-mgf with μ, no coherent residual
  component, beyond-level correlations of the residual negative. The data cover μ ≤ 5 (band) and μ ≤ 6.9 (top band); they
  cannot reach the cumulant orders that matter.
* Proved: every cumulant of order j ≤ (1 − o(1))(log N)^{1−β} equals its independent-model value up to j!(6W_B)^j/|I|,
  and satisfies |κ_j| ≤ 3j!Σσ². Needed for T1-min: the same bound for (log N)^{1−β} < j ≤ (log N)^{1/2+δ}, i.e. for joint
  cumulants of prime tuples with product above N. That is depth in cumulant form; nothing here reaches it.
* On the top band, astra-5 and TB coincide: the projection is free (Prop 9.2), and (L_C) there would give a power saving.
  There no cumulant at all is CRT-accessible; even κ₂ is fable-3's Kloosterman-fraction problem, for which only the large
  sieve bound (1 + 8z²/N)Σσ² is proved.

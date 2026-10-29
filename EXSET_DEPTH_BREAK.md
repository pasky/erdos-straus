# EXSET_DEPTH_BREAK — a depth-breaking bound for the prime-modulus U family? (wave z51, lane 1a, slug `dbreak`)

ES is OPEN. Nothing here proves or disproves it.
Labels: PROVED / CONDITIONAL (on what) / CERTIFIED / EVIDENCE / CONJECTURE / Assessment.
Scripts: `scripts/z51_dbreak_*`. Data: `data/z51_dbreak/`. Brief: `../z51briefs/1a_opus_dbreak.md`. Reviews: `reviews/z51-dbreak-review-*.md`.

## 0. Summary table

**Status: round 2 (repairs after the round-1 Astra review folded in; round-2 review pending). No target reached:
there is no depth-breaking bound here.** What the lane produced: an exact reformulation and a reduction of T1-min to a
single large-prime layer (the top band), with evidence that the top band alone saves N^{0.30}; one abstract barrier
theorem for prime-detection information that is two-sided only at first order (scoped to explicit axioms); a
model-level statement for two-sided information below the level cap; a product-form obstruction for shift
arguments; and scoped assessments for the other three approaches.

| # | statement | label | § | review |
|---|---|---|---|---|
| 1 | target on the 4ℤ line (A_N ⊇ Av(𝓕_N)); three views (e/t/m) of one event; non-CRT inputs named and why they escape Thm 2.2(c)(ii)'s hypotheses | PROVED (elementary) + Assessment | §1 | R1 MAJOR (N3 statement, dependence claim) → repaired |
| 2a | exchange rate: PD events with modulus 4em ≤ e^λ carry first-moment mass ≪ λ²/(log N − λ), against ≍ λ for CRT events | PROVED (Brun–Titchmarsh); the depth reading is heuristic | §2.2 | R1 SOUND-WITH-MINOR → repaired |
| 2b | **one-sided PD barrier (abstract):** CRT data at level λ + PD first moments at level ≤ λ (exact, with candidate roughness to the horizon) + PD k-point upper bounds with constants K_k ≥ C^{k−1} + support cannot prove #A_N < (1 − 1/C)β_λ#I, β_λ ≥ e^{−C₁√λ−C₂log²λ}. For bounds of this form with K_k ≥ 2^{k−1} (Selberg-type constants; all pair constants in the literature, down to Lichtman's 3.2290) the gain over the CRT cap is ≤ log 2 | PROVED for arguments using only the stated axioms; NOT a theorem about all prime-detection methods | §2.3 | R1: FATAL as arithmetic barrier, SOUND-WITH-MINOR as abstract lemma → re-scoped, density repaired |
| 2c | sharpness (existence): with constant small densities and K_k = K₂^{k−1}, Cauchy–Schwarz and the mixture give the same limit 1 − 1/K₂ | PROVED | §2.3 | R1 MAJOR → restated |
| 2d | the k-th factorial moment of the CRT events visible at level L is ≤ (Ce²L/k²)^k for k ≤ L/log 3 | PROVED | §2.4 | R1 MAJOR → ranges added, necessity language removed |
| 2e | in the class-constant Cramér–Haar model, all mixed CRT/PD statistics of level ≤ λ (two-sided, every order) are consistent with avoidance ≥ ½e^{−C√λ} | PROVED for that model (random subfamily + LP duality + Thm 3.2 sieve limit with supply exponent 1); arithmetic version OPEN (candidate roughness not encoded) | §2.4 | added after R1; R2 pending |
| 3a | cost profile of shifts; product-form shift bounds with a common loss C > 1 per factor save ≪_C (log log N)² log log log N; a common loss 1 + ε needs log(1/ε) ≳ M/log log N to save M | PROVED for the defined product format | §3.1 | R1 MAJOR → proof of (b) repaired |
| 3b | one layer suffices: T1-min ⟸ (TB_δ) and a power saving for E_U off squares ⟸ (TB_pow), for the top band ℓ > √(2N) (linear for CRT majorants at level ≤ log N) | PROVED (inclusions) | §3.2 | R1: implications SOUND-WITH-MINOR; band language repaired |
| 3c | top band: P(X_top = 0) ≈ 1.4–1.5·e^{−E X_top}; log P falls with slope −0.30 in log N over 10⁷–4·10⁹ | CERTIFIED counts / EVIDENCE | §3.2 | R1 SOUND-WITH-MINOR (10⁷ rerun identical) |
| 3d | literature: the two-shift laws of P⁺ are size laws with o(1) or power-of-log errors at most scales; nothing on residues of P⁺(n+4e) mod 4e over many e. TB is a sufficient hypothesis, not shown necessary | Assessment | §3.2 | R1 MAJOR → corrected |
| 4 | raw Chebyshev on X stops at ≫ N/μ (Haar Var X ≥ E X/2; integers 1.05–1.12); anatomy split is a research plan, not a barrier | PROVED (constant centering, Haar) / EVIDENCE / Assessment | §4 | R1 MAJOR → restricted |
| 5 | a direct comparison with additive error η certifies ≤ log(1/η); listed results have bounded k and o(1) or power-of-log errors | PROVED (trivial) + Assessment | §5 | R1 MAJOR → necessity language removed |
| 6 | census of the 4ℤ-line family to 4·10⁹, independent cross-check at 2·10⁴, full histograms, controls | CERTIFIED / EVIDENCE | §6 | R1 SOUND-WITH-MINOR → conventions fixed |
| 7–8 | review record; remaining gap | — | §§7–8 | — |

## 1. Target, reformulations, and the non-CRT inputs

### 1.1 The target, on the 4ℤ line

I = I_N = {n ≤ N : n ≡ 1 (mod 8)}. An *event* is a pair (ℓ, e) with ℓ ≤ N prime, e ≥ 1 and ℓ ≡ −1 (mod 4e); its
class is E_{ℓ,e} = {n : ℓ | n + 4e}. The *4ℤ-line avoider set* is

    A_N = {n ∈ I : n ∉ E_{ℓ,e} for every event (ℓ, e)}.

The z50 prime-modulus U family 𝓕_N (classes −v mod ℓ, v | ℓ+1, v ≡ 0 (4) or 7 (8), ℓ < n + v) contains the classes
E_{ℓ,e} as its v = 4e part, and on the 4ℤ line the proper-divisor condition ℓ < n + 4e is automatic (Lemma 1.1(d)). So
Av(𝓕_N) ∩ I ⊆ A_N, and

> **T1-min(4ℤ).** #(A_N ∖ □) ≤ N exp(−(log N)^{1/2+δ}) for some δ > 0

implies T1-min of the brief. Everything below is about A_N, a *larger* set than Av(𝓕_N): upper bounds for A_N transfer
to 𝓕_N; the barrier statements are made for A_N (§8 says how they extend).

**Lemma 1.1 (three views of one event; PROVED, elementary).** Let n ≡ 1 (mod 8), e, t ≥ 1, and ℓ = 4et − 1 prime.
(a) ℓ | n + 4e ⟺ ℓ | tn + 1.
(b) If ℓ | n + 4e and m := (n + 4e)/ℓ, then n = 4etm − 4e − m (the word (t, u, v) = (t, 4e, m)), n + m = 4e(tm − 1),
    and tn + 1 = ℓ(tm − 1).
(c) The map (ℓ, e) ↦ (ℓ, t = (ℓ+1)/(4e)) is a bijection between events and pairs (ℓ, t) with ℓ ≡ −1 (mod 4t). Hence
    n ∈ A_N ⟺ for every e ≥ 1, n + 4e has no prime factor ℓ ≤ N with ℓ ≡ −1 (mod 4e)
           ⟺ for every t ≥ 1, tn + 1 has no prime factor ℓ ≤ N with ℓ ≡ −1 (mod 4t).
(d) In (b), m ≡ 3 (mod 4); in particular m ≥ 3, so ℓ < n + 4e. Consequently every event meeting n has
    e ≤ (n + 3)/8 and ℓ ≤ (n + 4e)/3 ≤ (n + 1)/2; the cutoff ℓ ≤ N is automatic for n ≤ N.
(e) For fixed n and m, the events with cofactor m are exactly the divisors e of (n + m)/4 with (n + m)/(4e) ≡ −1 (mod m)
    for which (n + 4e)/m is a prime.

*Proof.* (a) tn + 1 = t(n + 4e) − ℓ, and ℓ ∤ t since ℓ > t. (b) n = mℓ − 4e = m(4et − 1) − 4e; the other two are
expansions. (c) Immediate from (a). (d) mℓ = n + 4e ≡ 1 (mod 4) and ℓ ≡ 3 (mod 4); then n + 4e = mℓ ≥ 3(4e − 1).
(e) n + 4e = mℓ with ℓ ≡ −1 (mod 4e) ⟺ n + 4e ≡ −m (mod 4em) ⟺ 4e | n + m and m | (n + m)/(4e) + 1 (since
n + m + 4e = 4e((n+m)/(4e) + 1)). ∎

**Lemma 1.2 (squares; Theorem E, recorded for the control).** No odd square x² lies in any E_{ℓ,e}. *Proof.* For an
odd prime q | e, ℓ ≡ −1 (mod q) and ℓ ≡ 3 (mod 4) give (q/ℓ) = (ℓ/q)(−1)^{(q−1)/2} = (−1/q)(−1)^{(q−1)/2} = 1; if 2 | e
then ℓ ≡ 7 (mod 8) and (2/ℓ) = 1. Since e < ℓ, (−4e/ℓ) = (−1/ℓ) = −1. ∎ Every forbidden class is a quadratic non-residue.

*Convention.* The scripts exclude n = 1 (an odd square in I). Counts of "squares" below are odd squares > 1; non-square
counts are unaffected.

**Baseline (PROVED, z50).** #A_N ≪ N exp(−c√(log N)): EXSET_SIEVE_MASS Prop 2.3's lower-bound mass already uses only
u ∈ 4ℤ, so Thm 2.2(a) applies to A_N. By Thm 2.2(c)(ii) (EXCEPTIONAL_THETA Thm 2.5 with slice primes ℓ ≡ 3 (4), ℓ ≥ 11,
and ℓ = 3, 7 moved into the small modulus Q₀ = 168), every level-λ nonnegative CRT majorant for A_N saves at most
C√λ + O(log²(2 + λ)). The local hypothesis holds: for ℓ ≥ 11, a = (ℓ+1)/4 ≥ 3 and w(ℓ) = τ(a) ≤ a − 1 < ℓ/4, the classes
−4e (e | a) are distinct mod ℓ; in the fibre x ≡ 1 (8) the R-term is log(21/10). T1-min(4ℤ) asks for exponent 1/2 + δ.

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
needs ≥ (log N)^{1/2+δ} units of mass certified jointly. Per n, R(n) := #{events containing n} has mean ≍ log N and is
close to Poisson on the integers tested (EVIDENCE, §6.2), so the target is a lower-tail statement for R.

### 1.3 The non-CRT inputs, named, and why they escape Thm 2.2(c)(ii)'s hypotheses

Thm 2.2 (and THETA Thm 2.5) caps bounds of the form N·Eν + (nonnegative rounding term), ν a nonnegative *periodic*
majorant of level ≤ λ, evaluated by its CRT mean. Its engine is (b′)/Step 0 plus the Rankin functional. A function on
the finite interval [1, N] can always be written with classes of modulus > N; what the inputs below escape is the
global periodic-majorant-plus-CRT-mean architecture, not representability.

* **(N1) Prime detection in the cofactor (PD).** By Lemma 1.1(b),(e), E_{ℓ,e} ∩ I = ⋃_m E^{PD}_{e,m}, where
  E^{PD}_{e,m} = {n ∈ I : n ≡ −4e − m (mod 4em), (n + 4e)/m is prime}. Its first moment is evaluated by
  Siegel–Walfisz/BV/Brun–Titchmarsh for primes ≤ (N + 4e)/m in a class mod 4e (BV ranges are governed by x = N/m),
  while as a CRT event its modulus is ℓ ≈ N/m. For 4em < ℓ the PD modulus is the smaller one.
* **(N2) Mean values of multiplicative functions over all primes.** E.g. Σ_{x≤X} z^{ω_e(x)}, ω_e(x) = #{ℓ | x : ℓ ≡ −1
  (4e)}, evaluated by Selberg–Delange (a Dirichlet series in all primes ≤ X): one shift, all primes, no dimension cost.
  Multi-shift versions (Shiu, Nair–Tenenbaum, Henriot) are discussed in §3.
* **(N3) Quadratic large sieve / Linnik duality.** Heath-Brown: Σ*_{n≤N} |Σ*_{m≤M} a_m (n/m)|² ≪ (NM)^ε(N + M)Σ|a_m|²,
  the sums over odd squarefree n, m. Non-squarefree n must be treated separately (square parts lose; on n ≡ 1 (8),
  n = 17b² repeats characters), so the input controls the quadratic profile (n/ℓ)_ℓ of squarefree n only. The profile
  is the *suggested* dependence mechanism between shifts (EXSET_SHIFT_DIVISORS Remark 3.1(3): a heuristic; their
  Thm 3.1 proves negative dependence only given the full small-prime-power fibre, and the integer behaviour is
  EVIDENCE). Squares fail the profile completely.

Escaping the hypotheses is necessary, not sufficient. Sections 2–5 examine what each input yields.

*Where squares must fail (control).* For n = x² every event indicator vanishes identically (Lemma 1.2). A statement of
T1-min strength is not contradicted by squares (density N^{−1/2}), but any *universal* inequality behind it must fail
on sets made of squares (G5). Each section names the step that would fail at squares.

## 2. Approach 1: prime detection in the cofactor

Verdict. PD is a genuine non-CRT input. (i) Per unit of level its first-moment mass is smaller than that of the CRT
events (Prop 2.2), so it is not a cheap layer for depth arguments. (ii) An argument whose PD information is two-sided
only at first order (BV-type statistics at level ≤ λ, idealised as exact) and one-sided at higher orders (sieve upper
bounds of the I3 form below) gains at most log(C/(C − 1)) over the CRT cap (Theorem 2.3, an abstract theorem about
those axioms), and the constant is attained in a model (Prop 2.4). (iii) Two-sided information at total level ≤ λ adds
nothing to the exponent in the class-constant Cramér model (Theorem 2.6, model-level). What remains open is PD (or
other) information outside these axioms: two-sided correlations at total level above log N, signed interval sums,
archimedean relations, nonlinear Type II structure.

### 2.1 PD events and their first moments

Fix a CRT horizon λ with λ₀ ≤ λ ≤ c log N. For e ≥ 1 and m ≡ 3 (mod 4) put

    E^{PD}_{e,m} = {n ∈ I : n ≡ −4e − m (mod 4em), (n + 4e)/m is a prime > e^λ}.

By Lemma 1.1(b),(e), ⋃_{e,m} E^{PD}_{e,m} = ⋃_{ℓ>e^λ} E_{ℓ,e} ∩ I. Write B_λ ⊆ 1 + 8Ẑ for the clopen set of x avoiding
the (finitely many) event classes with ℓ ≤ e^λ, and A^{CRT}_λ = B_λ ∩ I. Then A_N = A^{CRT}_λ ∖ ⋃ E^{PD}_{e,m}.
#E^{PD}_{e,m} counts primes p ∈ (e^λ, (N + 4e)/m] with p ≡ −1 (mod 4e) and mp − 4e ≡ 1 (mod 8). Siegel–Walfisz gives its
asymptotic for 4e ≤ (log N)^A; BV gives it on average over 4e ≤ (N/m)^{1/2}(log N)^{−B}; Brun–Titchmarsh gives an
upper bound always.

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
moment by (C log N/k³)^k, against (C log N/k²)^k for CRT events (Lemma 2.5): the PD representation reaches k ≍ (log N)^{1/3},
the CRT one k ≍ (log N)^{1/2}. Prop 2.2 bounds only the first-moment mass; the premises of this reading are not proved.

### 2.3 An abstract barrier for one-sided PD information

**Setting.** Fix λ as in §2.1 and the finite family 𝒥 of PD events j = (e_j, m_j) with 4e_jm_j ≤ e^λ. For such j the
cofactor m_j is e^λ-smooth. A *model* is a probability space carrying x ∈ 1 + 8Ẑ (Ẑ the profinite completion; x plays
n) and bits π_j ∈ {0, 1}, j ∈ 𝒥. Put

    r_j(x) = c_j·1[x ∈ class_j]·1[(x + 4e_j)/m_j has no prime factor ≤ e^λ],

class_j the class −4e_j − m_j (mod 4e_jm_j), with c_j chosen so that E_ℋ r_j = #E^{PD}_j/#I (ℋ = Haar on 1 + 8Ẑ).
(The roughness factor runs to the horizon e^λ. A true PD candidate is a prime > e^λ, so for every class S of level
≤ λ the Haar quantity E_ℋ[1_S r_j] vanishes exactly when the true count does, and otherwise has the
Siegel–Walfisz/BV main term: uniform over reduced classes of each modulus q ≤ e^λ, zero on the others.)
Two consequences of the roughness factor are used below. (α) If r_{e,m}(x) > 0 then m is the full e^λ-smooth part of
x + 4e, so for fixed (x, e) at most one m has r_{e,m}(x) > 0: the true exclusivity "n + 4e has at most one cofactor
m ≤ e^λ with (n + 4e)/m a prime > e^λ" holds in every model satisfying (I4). (β) If r_j(x) > 0 and a CRT event
(ℓ′, e_j) with ℓ′ ≤ e^λ meets x, then ℓ′ | m_j, as for integers.

An argument of **type (λ; K₂, K₃, …)** uses the integers only through statements implied by the following axioms.

* (I1) *CRT data at level λ:* E f(x) = E_ℋ f for every f of level ≤ λ (finite combinations of class indicators b mod d
  with Σ_{slice ℓ | d} log ℓ ≤ λ, as in THETA §1).
* (I2) *PD first moments at level ≤ λ, exact:* P(π_j = 1, x ∈ S) = E_ℋ[1_S r_j] for every j and every clopen S of
  level ≤ λ.
* (I3) *PD correlations, one-sided:* P(π_J ≡ 1, x ∈ S) ≤ K_k E_ℋ[1_S ∏_{j∈J} r_j] for every k ≥ 2, J ⊆ 𝒥 with |J| = k,
  and every clopen S.
* (I4) *Support:* π_j = 0 wherever r_j = 0.

The integers satisfy (I1) up to rounding, (I2) up to the BV/SW error terms, (I4) exactly, and (I3) wherever a sieve
upper bound of that shape is available. An exact axiom implies every statement of the form "|count − main term| ≤ error"
about the same statistic, so arguments that use BV-type first moments with error terms are covered. Arguments that use
anything else are not: two-sided PD correlations of order ≥ 2 (even averaged), signed interval sums at moduli > N,
archimedean (size) relations between candidates, Type I/II identities used beyond first moments, and exact zero
correlations not implied by congruences and roughness.

**Theorem 2.3 (one-sided PD information is worth a constant; PROVED for arguments of type (λ; K)).** Let C > 1,
K_k ≥ C^{k−1} for every k ≥ 2, and r_j ≤ 1/C for every j (true for λ ≤ c_C log N). Then some model satisfies (I1)–(I4) and

    P(x ∈ B_λ, π ≡ 0) ≥ (1 − 1/C)·β_λ,   β_λ := inf{E_ℋ ν : ν a level-λ majorant of B_λ} ≥ (10/21)e^{−C₁√λ − C₂ log²(2+λ)}.

Hence no argument of type (λ; K) proves #A_N < (1 − 1/C)β_λ·#I. With λ ≤ A log N such arguments gain at most
log(C/(C − 1)) over the CRT cap of G1.

*Proof.* (i) *A fake CRT law.* Conditional averaging onto the finite quotient generated by Q₀ and the slice primes
≤ e^λ reduces the infimum to a finite LP (finer digits and other primes are uncharged and irrelevant to B_λ). For a
finite set 𝒞 of level-λ classes containing the trivial class, finite LP duality (ν = 1 is primal feasible, ℋ is dual
feasible) gives a probability ρ_𝒞 with ρ_𝒞 = ℋ on every class of 𝒞 and ρ_𝒞(B_λ) ≥ β_λ. The sets
{ρ : ρ = ℋ on 𝒞, ρ(B_λ) ≥ β_λ} are weak-* closed (class indicators and the clopen B_λ are continuous), nonempty, and have
the finite-intersection property; by compactness some ρ lies in all of them. The lower bound on β_λ is THETA Thm 2.5
for the 4ℤ-line system (§1.1): Σ_ℓ w(ℓ)ℓ^{−1−α} ≪ 1/α by Brun–Titchmarsh and divisor pairing; optimise 19αλ + C/α.
(ii) *The mixture.* Let ξ be an independent coin with P(ξ = 1) = 1/C. On {ξ = 0}: x ~ ρ and π ≡ 0. On {ξ = 1}: x ~ ℋ
and, given x, the π_j are independent Bernoulli(C r_j(x)).
(iii) *Checks.* (I1): the law of x is (1 − 1/C)ρ + (1/C)ℋ, equal to ℋ on level-λ functions. (I2) and more, for every
clopen S: P(π_j = 1, x ∈ S) = (1/C)E_ℋ[1_S C r_j] = E_ℋ[1_S r_j]. (I3): P(π_J ≡ 1, x ∈ S) = C^{k−1}E_ℋ[1_S ∏_J r_j]
≤ K_k E_ℋ[1_S ∏_J r_j]. (I4): C r_j vanishes where r_j does. Finally P(x ∈ B_λ, π ≡ 0) ≥ P(ξ = 0)ρ(B_λ). ∎

*Endpoint.* The model has probability ≥ (1 − 1/C)β_λ, so it refutes bounds strictly below that value.

**Corollary 2.3′ (sieve-type correlation constants).** If the correlation inputs are upper bounds of the I3 form with
K_k ≥ 2^{k−1} for all k ≥ 2, take C = 2: the gain over the CRT cap is ≤ log 2. Selberg's tuple bound (K_k = 2^k k!(1+o(1));
also 4^{k−1}(k−1)!) and every pair constant in the literature (Selberg 8, Bombieri–Davenport 4, Chen 3.9171, Wu 3.3996,
Lichtman 3.2290 [arXiv:2309.08522, Thm 1.1], all relative to the full Hardy–Littlewood main term) satisfy K_k ≥ 2^{k−1}.
This is a statement about bounds *of that form*; inadmissible configurations (exact zeros), averaged tuple estimates and
the localisation of a global bound to every S are separate inputs, not claimed to be of I3 form.

**Proposition 2.4 (sharpness, existence; PROVED).** (a) Cauchy–Schwarz: if R = Σ_j π_j has E R = μ and
E[R(R − 1)] ≤ K₂μ², then P(R = 0) ≤ 1 − μ²/(μ + K₂μ²). (b) For constant densities r_j ≡ r ≤ 1/K₂ with |𝒥|r → ∞, the
mixture with C = K₂ satisfies every I3 bound with K_k = K₂^{k−1}, has E R(R − 1) = K₂μ², and
P(R = 0) = 1 − 1/K₂ + (1/K₂)(1 − K₂r)^{|𝒥|} → 1 − 1/K₂, the limit of (a). With general densities the last term is
(1/K₂)∫∏_j(1 − K₂r_j)dℋ, which need not vanish. ∎ So within these axioms the pair constant determines the gain
exactly, when K_k = K₂^{k−1}; in general the activation parameter is limited by all orders.

*What escapes Theorem 2.3 (each item excludes the mixture).* (a) Upper bounds with K_k < C^{k−1} at some order, i.e.
two-sided, Hardy–Littlewood-quality information. (b) A lower bound for a union, P(∃ j ∈ B : π_j = 1) ≥ 1/C + ε on a block
of large mass; in the mixture the union has probability ≤ 1/C. Such a bound is itself a T1-type statement. (c) Relative
statements inside sets that already avoid PD events (RLD (R1) for PD steps). (d) Deterministic relations not implied by
(I4): within one shift, (α) above already encodes the exclusivity of cofactors ≤ e^λ; relations involving sizes of the
candidates (e.g. n + 4e = mm′ when two cofactors both work) are archimedean and outside these axioms.

*Novelty (Assessment, after R1).* G1/THETA supply the fake CRT law and EXSET_ARITH_JANSON_OPUS §3 the LP-duality
viewpoint; (D)22 concerns prime-supported CRT majorants. The zero-inflated mixture over added PD bits is a distinct,
elementary extension. It is a barrier for arguments built from the stated axioms, not for prime-detection methods in
general.

### 2.4 Two-sided PD information below the level cap

**Lemma 2.5 (level-L content of CRT factorial moments; PROVED).** For 1 ≤ k ≤ L/log 3 and every α ∈ (0, 1],

    F_k(L) := Σ_{k-sets of events at distinct primes with Σ log ℓ_i ≤ L} ∏_i 1/ℓ_i ≤ e^{αL}(Σ_ℓ w(ℓ)ℓ^{−1−α})^k/k! ≤ e^{αL}(C/α)^k/k!,

so F_k(L) ≤ (Ce²L/k²)^k (take α = k/L ≤ 1); for k > L/log 3 the sum is empty. *Proof.* The degree-k coefficient of
∏_ℓ(1 + w(ℓ)ℓ^{−1−α}z) is at most (Σ w(ℓ)ℓ^{−1−α})^k/k!; Rankin gives 1[Σ log ℓ_i ≤ L] ≤ e^{α(L − Σ log ℓ_i)}; and
Σ_ℓ w(ℓ)ℓ^{−1−α} ≪ 1/α by Brun–Titchmarsh. Use k! ≥ (k/e)^k. ∎
For comparison, the Haar factorial moment is e_k(p_ℓ : ℓ ≤ N) (elementary symmetric polynomial of p_ℓ = w(ℓ)/ℓ), which is
≈ μ_N^k/k! only for k = o(μ_N). So for √(log N) ≪ k ≪ log N the part of the k-th factorial moment visible at level
log N is exponentially small. This limits Bonferroni/moment arguments that evaluate intersections by their CRT main
terms; it does not classify other uses of moment information.

**Theorem 2.6 (model-level: two-sided PD statistics below the level cap; PROVED for the class-constant Cramér–Haar
model, given the KARY/EK framework of EXSET_SIEVE_MASS Thm 3.2 run with supply exponent 1).** Let W be the absolute
constant of that theorem, λ₀ ≤ λ ≤ (log N)/2, and 𝒥 a finite family of PD events with level s_j := Σ_{ℓ | 4e_jm_j, ℓ > W}
log ℓ ≤ λ. The *class-constant Cramér–Haar model* CH draws x ~ ℋ and independent coins κ_j ~ Bernoulli(ρ_j) and sets
π_j = 1[x ∈ class_j]κ_j, with 0 ≤ ρ_j ≤ C₀(4e_j/φ(4e_j))/(log N − λ). A *mixed monomial* 1_S(x)∏_{j∈J}π_j has level
(level of S) + Σ_J s_j. Then some joint law of (x, π) agrees with CH on every mixed monomial of level ≤ λ and has
P(x ∈ B_λ, π ≡ 0) ≥ ½ exp(−C√λ), C absolute.

*Proof.* (1) Let 𝒥′ ⊆ 𝒥 contain each j independently with probability ρ_j. (2) With Γ, G, 𝔐 as in EXSET_BEYOND_CRT §2 and
EXSET_SIEVE_MASS §3, 𝔐_{𝒥′}(y) = Σ_{j∈𝒥′, W<P(G_j)≤y} Γ(G_j)/G_j has E𝔐_{𝒥′}(y) ≤ (C/(log N − λ))Σ_{P(em)≤y} Γ(4em)(4e/φ(4e))/(4em)
≤ C′(log y)²/(log N − λ) ≤ C′ log y for y ≤ e^λ, and is constant for y > e^λ. Summands are bounded, so Bernstein and a
union bound over y = e^{2^i} give, with probability ≥ ½, 𝔐_{𝒥′}(y) ≤ K log y for all y ≥ y₀ (K, y₀ absolute). The
prime-local classes −4e (mod ℓ) have supply ≤ K log y (Brun–Titchmarsh). (3) The family 𝔊(𝒥′) = {prime-local classes
at ℓ ≤ e^λ} ∪ {class_j : j ∈ 𝒥′} ∪ {n ≢ 1 (mod 8)} consists of classes of the U-family 𝔘 of EXSET_SIEVE_MASS §1.1
(word classes with endpoint u = 4e ∈ S; class_j is a W2 class) and excluded residues mod 8, so it has the square base;
the cofactor sums (iii) hold for subfamilies of 𝔘. Rerun Thm 3.2's assembly with first moment K log y: s₁ = √λ,
singletons ≤ (8/3)K√λ, block i (s = 2^i s₁, d_i = ⌊λ/s⌋) has (E M_{V_i} + 4d_i)/d_i ≤ 2K·4^i + 4, total C√λ + O(log²λ).
So on the event of (2), every level-λ majorant of 𝒜(𝔊(𝒥′)) has Eν ≥ e^{−2W−log 2−C√λ}. (4) As in Thm 2.3(i), a fake
law ρ_{𝒥′} with Haar marginals on level-λ classes and ρ_{𝒥′}(𝒜(𝔊(𝒥′))) ≥ e^{−2W−log 2−C√λ}; off the event, ρ_{𝒥′} = ℋ.
(5) Draw 𝒥′, x ~ ρ_{𝒥′}, π_j = 1[j ∈ 𝒥′, x ∈ class_j]. For a mixed monomial of level ≤ λ, 1_S∏_J 1_{class_j} is a class
indicator of level ≤ λ, so E[1_S∏_J π_j] = ∏_J ρ_j·ℋ(S ∩ ⋂_J class_j), the CH value; and x ∈ 𝒜(𝔊(𝒥′)) forces
x ∈ B_λ and π ≡ 0. ∎

*Arithmetic scope (Assessment).* CH ignores the roughness of candidates at primes q ∈ (W, e^λ]: for S forcing q | (x + 4e_j)/m_j
the true PD count is 0 while CH gives a positive value. So Theorem 2.6 shows that "PD events as coins attached to W2
classes" add nothing to the exponent below the level cap; it is not a barrier for arguments using the true level-λ PD
statistics. The arithmetic version needs a fake law that also matches Haar on roughness-refined classes
S ∩ ⋂_J(class_j ∩ Rough_j), i.e. a sieve-limit theorem for rough-refined (prime-law) majorants; EXSET_BEYOND_CRT §2 expects
such a "prime-law version" by a unit-group rerun but has not checked it. OPEN.

**Blocking statement for approach 1 (scoped).** Within the axioms of Thm 2.3, PD gains a constant; below the level cap
in the CH model it gains nothing in the exponent. A depth-breaking PD argument must use information outside these
axioms: two-sided correlations at total level above log N, union lower bounds (the target), archimedean relations, or
signed interval sums. *Step that fails at squares:* none at the level of first moments (squares are a null set); the
universal form of a union lower bound fails on planted squares (G5).

## 3. Approach 2: exponential moments over shifts

Write X(n) = R(n) = Σ_e ω_e(n + 4e) (the number of events containing n), with ω_e(x) = #{ℓ | x prime, ℓ ≡ −1 (4e)}
(Lemma 1.1(c),(d)). For 0 ≤ z < 1, P(X = 0) ≤ E z^X = #I^{−1} Σ_{n∈I} ∏_e z^{ω_e(n+4e)}, a correlation of multiplicative
functions at many shifts. Verdict: bounds of product form over shifts are useless for this family (Prop 3.1); for upper
bounds one layer suffices (Lemma 3.2), which reduces T1-min to the top band (Cor 3.3), where the numerics show N^{−0.30}.
No proof of the top-band statement is offered.

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
*Proof.* (a) If n + 4e is prime then n ∈ F_e: its only prime factor is ≡ n (mod 4e), and n ≢ −1 (mod 4) on I. Primes in
(N/2, N] in the class 1 + 4e (mod 8) number ≫ N/log N. (b) For n uniform on I, P(ℓ | n + 4e) ≤ 1/ℓ + 9/N. Over
ℓ ≡ −1 (mod q), q = 4e: the ℓ ≤ q² contribute ≤ Σ_{j≤q} 1/(jq − 1) ≤ 2(1 + log q)/q; the ℓ ∈ (q², 2N] contribute
≤ (4/φ(q))(1 + log log 2N) by partial summation with π(t; q, −1) ≤ 4t/(φ(q) log t) (Brun–Titchmarsh, t ≥ q²), the
range being empty if q² > 2N; the 9/N terms add ≤ 9π(2N; q, −1)/N ≪ 1/φ(q). (c) Split at 16E², so that ℓ > (4e)² for
every e ≤ E in the upper range. Lower range: Σ_{ℓ≤16E²} #{e : 4e | ℓ + 1}/ℓ ≤ Σ_{ℓ≤16E²} τ((ℓ+1)/4)/ℓ ≪ log 2E (divisor
pairing and Brun–Titchmarsh). Upper range: the second part of (b) for each e ≤ E, and Σ_{e≤E} 1/φ(4e) ≪ log 2E. The
rounding terms add O(log 2E). (d) Σ_e hit(e) ≤ Σ_{ℓ≤N} w(ℓ)(1/ℓ + 9/N) ≪ log N. ∎

**Proposition 3.1 (product forms over shifts; PROVED for the format above).**
(a) If C_e ≥ C > 1 for every e ∈ S, the saving is ≪_C (log log N)² log log log N.
(b) If C_e = 1 + ε for every e ∈ S (0 < ε ≤ 1, a = log(1/ε)), the saving is ≤ C₁ log log N·(a + log(2 + a + log log N))
    + C₁(log log N)² log log log N. So a saving M ≫ (log log N)² log log log N with a common factor 1 + ε requires
    a ≳ M/log log N.
*Proof.* Write L_j for the j-fold iterated logarithm of N. (a) (cost(e) − log C)^+ > 0 forces hit(e) > 1 − 1/C, so by
Lemma 3.0(b) and φ(q) ≫ q/log log 3q, e ≤ E₁ ≍_C L₂L₃. Each such shift contributes ≤ L₂ + O(1) (Lemma 3.0(a)).
(b) Shifts with e ≤ E₁ contribute ≤ E₁(L₂ + O(1)) as in (a). For e > E₁, hit(e) ≤ ½ and cost(e) ≤ 2hit(e), and the shift
contributes only if cost(e) > log(1 + ε) ≥ ε/2, which by Lemma 3.0(b) forces e ≤ E₀ with
log E₀ ≤ a + O(log(2 + a + L₂)). If E₀ ≤ N^{1/3}, Lemma 3.0(c) bounds the contribution by C₀(1 + L₂) log 2E₀. If
E₀ > N^{1/3}, then a ≫ log N, and Lemma 3.0(d) bounds the whole contribution by C₀ log N ≪ a. ∎

*Reading.* For the full U family, lane D (EXSET_SHIFT_DIVISORS Thm 5.1, 5.3) found (log N)^{log 2+o(1)} costly shifts.
For the prime family the per-shift cost is ≈ log(log N/log 4e)/φ(4e), the costly shifts number ≍ L₂L₃, and product forms
collapse to (log log N)^{2+o(1)}. This concerns the displayed format. No theorem is claimed that every
Nair–Tenenbaum/Henriot/Shiu application has that format (their constants and local factors would have to be
translated into factors C_e multiplying the true marginals); the standard implementation, which bounds the y-rough part
of each n + 4e by f ≤ 1 and sieves the y-smooth parts, is a CRT majorant to which G1 applies.

### 3.2 One layer suffices for upper bounds; the top band

**Lemma 3.2 (decoupling; PROVED, trivial).** For any subfamily B of events, A_N ⊆ Av(B). For subfamilies B₁, …, B_k and
z ∈ [0, 1), E z^{X_{B₁}+⋯+X_{B_k}} ≤ ∏_i (E z^{k X_{B_i}})^{1/k} (Hölder). So if one layer B satisfies
#Av(B) ∩ (I ∖ □) ≤ N e^{−M}, so does A_N.

One sufficiently strong layer is *sufficient*; it is not shown necessary (combined information can beat every single
layer). RLD-U is a statement at the level of the full Mertens product, and Hölder loses a factor k in the exponent when
layers are combined this way.

*Which layer.* Small primes ℓ ≤ e^{c√(log N)} are where CRT works and stops (G1). For large primes CRT is weaker
still. For the top band ℓ > √(2N), a level-λ majorant with λ ≤ log N contains at most one band prime per term, so it is
*linear* in the band hits and its saving is ≤ log(1/(1 − max p_ℓ)) = o(1) (EXSET_SIEVE_MASS Thm 2.2(c)(iii), linear case).
At λ = 2 log N up to three band primes fit in a term; for a band of fixed logarithmic width THETA's Boolean argument
with s_* ≍ log N gives O(1) groups and saving O(log(2 + μ)). In words: polynomial-level CRT majorants save only
O(log log N) on the top band. The top band is also the cleanest large layer: each n + 4e ≤ 2N has at most one prime
factor > √(2N), namely P⁺(n + 4e).

**Corollary 3.3 (reduction to the top band; PROVED).** Put X_top(n) = #{e ≥ 1 : P⁺(n + 4e) > √(2N),
P⁺(n + 4e) ≡ −1 (mod 4e)} (by Lemma 1.1(d) only e ≤ (n + 3)/8 contribute, and every such prime is ≤ (n + 1)/2 ≤ N, so
each counted hit is an event). Then A_N ⊆ {X_top = 0}, and
* (TB_δ) #{n ∈ I ∖ □ : X_top(n) = 0} ≤ N exp(−(log N)^{1/2+δ}) implies T1-min(4ℤ) and T1-min;
* (TB_pow) #{n ∈ I ∖ □ : X_top(n) = 0} ≤ N^{1−c} implies #{n ≤ N, n ≡ 1 (4) : U(n) fails} = #{odd squares ≤ N} + O(N^{1−c}),
  a power saving for E_U off the squares, and the same bound for the ES₅ exceptional count on the domain where
  E_{ES₅} ≤ E_U holds (z50).
*Proof.* A U failure at n ≡ 1 (8) lies in no prime-pivot U certificate class, so it lies in A_N ⊆ {X_top = 0}; U holds at
every n ≡ 5 (mod 8), n > 5 (z50 Obs. 6.0). ∎

By Lemma 1.1(e), X_top(n) = #{(m, e) : m ≡ 3 (4), e | (n + m)/4, (n + m)/(4e) ≡ −1 (mod m), (n + 4e)/m a prime > √(2N)}:
for each cofactor m < √(2N)(1 + o(1)), the divisors of the single integer (n + m)/4 in one class mod m produce candidates,
and one candidate must be prime.

**A sufficient hypothesis and the literature (Assessment).** TB_δ would follow from joint control of the residues
P⁺(n + 4e) mod 4e over exp((log N)^{1/2+δ}) shifts e at precision exp(−(log N)^{1/2+δ}); a direct bound for the zero event,
an exponential moment or a weighted witness count could suffice with less, so this is a sufficient hypothesis, not a
characterisation. What is known is far from it, and of a different kind: two-shift laws of the *sizes* of largest
prime factors. Teräväinen (arXiv:1710.01195, Thms 1.11, 1.14) proves the joint law of log P⁺(n)/log n and
log P⁺(n+1)/log n in logarithmic density; Tao–Teräväinen (arXiv:2512.01739, Thm 1.8) give the consecutive smooth-number
law with a power-of-log error outside a small exceptional set of scales; the OpenAI release (item 012, *The joint
Dickman law for consecutive integers*, unrefereed) claims natural-density independence by an iterated-limit argument
with no rate. None of these concerns P⁺(n + 4e) modulo a growing 4e, and size thresholds do not determine those residues.
The short-interval analogy: under a uniform Hardy–Littlewood hypothesis Gallagher obtains Poisson statistics for
primes in [x, x + λ log x] with λ fixed; uniformity for λ → ∞ at exponentially small zero probabilities is additional.
Under RH, Selberg's bound #{x ≤ X : no prime in [x, x + H]} ≪ X(log X)²/H is a power saving for H = X^θ but only
polylogarithmic for polylogarithmic H. TB_δ asks for a super-√ Poisson tail among ≍ (log N)² structured candidates;
no reduction to a prime-gap theorem is claimed.

**Numerics for the top band (CERTIFIED counts, EVIDENCE for the trend; `data/z51_dbreak/sieve4_top_N*.txt`).**
Non-squares n ∈ I, top band ℓ > √(2N); histograms complete (they sum to the number of non-squares):

| N | E X_top | P(X_top = 0) | e^{−E X_top} | ratio | P(X_top = 0 \| small layer avoided) |
|---:|---:|---:|---:|---:|---:|
| 10⁷ | 3.534 | 0.03844 | 0.02919 | 1.32 | 0.0841 |
| 10⁸ | 4.251 | 0.01975 | 0.01425 | 1.39 | 0.0461 |
| 10⁹ | 4.989 | 0.00981 | 0.00681 | 1.44 | 0.0236 |
| 2·10⁹ | 5.209 | 0.00795 | 0.00547 | 1.45 | 0.0193 |
| 4·10⁹ | 5.429 | 0.00644 | 0.00439 | 1.47 | 0.0158 |

log P(X_top = 0) falls with slope −0.30 in log N (−0.297 over 10⁷–10⁹, −0.304 over 10⁹–4·10⁹): the top band alone shows
N^{−0.30} at five scales over 2.6 decades (EVIDENCE for TB_pow, not an asymptotic). The ratio to the Poisson value grows
slowly and decelerates (log ratio 0.28, 0.33, 0.36, 0.37, 0.38; increments per decade 0.051, 0.038, 0.032): mild positive
dependence. Conditioning on the small layer (ℓ ≤ √(2N)) lowers E X_top (4.99 → 4.20 at N = 10⁹) and raises
P(X_top = 0) by a factor 2.4, which is why Lemma 3.2 (no conditioning) is the way to use the layers. The whole 4ℤ-line
family leaves 23 727 and 31 612 non-squares at N = 2·10⁹ and 4·10⁹ (squares > 1: 22 360 and 31 622). The largest X_top
seen is 41 (five n ≤ 4·10⁹ have X_top ≥ 40, e.g. n = 2 895 235 193).

## 4. Approach 3: anatomy and the bilinear (e, m) incidence

Verdict: the bilinear (e, m) form is the PD system of §2 summed over n. Raw Chebyshev on X stops at N/μ. Anatomy
controls the *candidates* (divisors of one integer (n + m)/4 per cofactor m), not their primality or joint law. Neither
observation is a barrier for weighted or nonlinear uses of the incidence.

### 4.1 The incidence form and the raw L² ceiling

By Lemma 1.1(b),(e), X(n) = #{words (t, 4e, m) of n with 4et − 1 prime}: n has C(n) := #{4ℤ-line words of n} candidates
(C(x²) = 0 by Theorem E), and X(n) counts those whose pivot tu − 1 is prime. Double counting (summing over all PD
events, i.e. without the horizon of §2.1): Σ_n X(n) = Σ_{e,m} #{PD events}, Σ_n X(n)² = Σ over pairs, each pair being the
binary problem m p − m′p′ = 4(e − e′), p ≡ −1 (4e), p′ ≡ −1 (4e′): twin-prime type for fixed coefficients; averaged over
(e, m, e′, m′), the setting where circle-method or dispersion asymptotics are plausible.

**Proposition 4.1 (raw Chebyshev ceiling; PROVED for Haar with constant centering).** With μ = E_ℋ X,
Var_ℋ X = Σ_ℓ p_ℓ(1 − p_ℓ) ≥ μ/2 (at each prime at most one forbidden class is hit, p_ℓ = w(ℓ)/ℓ ≤ 1/2, and distinct
primes are independent under ℋ), so the Chebyshev bound N·Var X/μ² is ≫ N/μ. On the integers Var X/E X = 1.05–1.12
(§6.2). ∎ This limits the direct second-moment bound for the raw count, even with an exact asymptotic for the averaged
binary problem: exact second moments give 1/μ. It does not limit L² arguments applied to weighted counts, sieve
weights, nonlinear transforms or bilinear error terms; for a general predictor μ(n) no such ceiling holds (μ(n) =
max(1, X(n)) makes the numerator count the zeros exactly).

### 4.2 Anatomy: candidates versus primes

The m-view (Lemma 1.1(e)) makes the candidates of cofactor m the divisors e of the single integer (n + m)/4 in one class
mod m. Hall–Tenenbaum/Ford anatomy and Erdős–Hall (divisors in residue classes) control such divisor sets one integer
at a time; they bear on C(n), not on X(n). One can split

    P(X = 0) ≤ P(C(n) ≤ K) + P(X = 0, C(n) > K),

with K = (log N)^{3/2+δ}, so that "K candidates, each prime with probability ≍ 1/log N" would give e^{−(log N)^{1/2+δ}} in a
Poisson model. This split is a research plan, and its failure in a crude implementation is not a barrier. Two
observations (Assessment): the first term is a lower tail for the full (composite-pivot) word count, beyond what the
CRT architecture certifies (its optimal collective saving corresponds to words of moduli ≤ T with log T ≍ (log N)^{1/3},
lane E's 2/3 exponent); the second is the PD problem restricted to {C > K}, whose one-sided version falls under the
axioms of Thm 2.3 only after the selection {C > K} is itself represented in the model.

## 5. Approach 4: entropy decrement and averaged independence

**Lemma 5.1 (additive-error floor; PROVED, trivial).** A direct comparison P(X_B = 0) ≤ P_model(X_B = 0) + η certifies a
saving of at most log(1/η).

The quantitative errors of the available results are, as far as checked: powers of log h or log X for
Matomäki–Radziwiłł-type short-interval and averaged-correlation theorems; a power of log outside an exceptional set of
scales for Tao–Teräväinen arXiv:2512.01739; no explicit rate for entropy-decrement arguments (Tao; Tao–Teräväinen odd-order
Chowla; OpenAI item 012). Substituted into Lemma 5.1, a power-of-log error gives O(log log N); a qualitative o(1) gives
no explicit saving at all. The cited correlation theorems concern a bounded number of shifts (or an average over one
shift). By Lemma 3.2 the target is the lower tail of one sum X_B; pairwise independence on average is second-moment
information (§4.1). For moment-based use, a central-moment bound (Ck/μ)^{k/2} saves M with k ≍ M/log(μ/M), so for
M = (log N)^{1/2+δ} the order k must exceed √(log N); this is a requirement of moment arguments, not of all arguments.

**Scoped assessment for approach 4.** The cited averaging/entropy theorems, used through Lemma 5.1 or through moments of
bounded order, cannot reach T1-min. Amplifications that combine bounded-order information nonlinearly (as the
growing-dimensional sieve in Tao–Teräväinen does for another problem) are not excluded here.

## 6. Numerics and controls

All runs with `ulimit -v 8000000` and timeouts; C source `scripts/z51_dbreak_sieve4.c` (usage `sieve4 N Y`, optional
`DUMP=file`; it now prints the complete histogram, its total, and every non-square n with ≥ 40 large events), Python
`scripts/z51_dbreak_controls.py`, `scripts/z51_dbreak_xcheck.py`.

### 6.1 Census of the 4ℤ-line prime family (CERTIFIED)

* Independent cross-check: the brute-force e-view enumeration (factor n + 4e for e ≤ (n + 3)/8, justified by Lemma 1.1(d))
  and the sieve agree exactly on A_N at N = 2·10⁴ (160 avoiders > 1, 70 of them squares; with n = 1 included, 161 and
  71; `data/z51_dbreak/xcheck_alive_N20000.txt`). The t-view (ℓ | tn + 1, ℓ ≡ −1 (4t)) agrees with the e-view on every
  control below 3000 (Lemma 1.1(c)). The round-1 reviewer reran N = 10⁷ (top band) byte-for-byte and an independent
  brute force at 2·10⁴ including the top-band histogram (R1 §9).
* The sieve checks every odd square ≤ N against every class it marks and reports any hit on stderr; none occurred at
  N = 10⁷, 10⁸, 10⁹, 2·10⁹, 4·10⁹. The control script checks the listed squares only.
* #(A_N ∖ □) = 2 457, 6 836, 17 886, 23 727, 31 612 at N = 10⁷, 10⁸, 10⁹, 2·10⁹, 4·10⁹ (squares > 1: 1 580, 4 999,
  15 810, 22 360, 31 622); density in I 1.97·10⁻³, 5.47·10⁻⁴, 1.43·10⁻⁴, 9.49·10⁻⁵, 6.32·10⁻⁵.

### 6.2 Poisson behaviour of the large layers (EVIDENCE)

Variance/mean of the number of events with ℓ > Y, over non-squares (complete histograms):

| N | Y | mean | var/mean (all) | mean, var/mean (small layer avoided) |
|---:|---:|---:|---:|---:|
| 10⁹ | 10³ | 7.17 | 1.05 | 6.48, 1.19 |
| 10⁸ | √(2N) | 4.25 | 1.12 | 3.47, 1.20 |
| 10⁹ | √(2N) | 4.99 | 1.12 | 4.20, 1.20 |

The large layers are close to Poisson and mildly over-dispersed; conditioning on the small layer lowers the mean and
raises the dispersion. These are finite-range observations; they do not certify an exponentially small lower tail.
(At N = 10⁹, Y = 10³ one non-square, n = 833 975 993, has 42 large events.)

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

**R1 (Astra, `openai-codex/gpt-6-astra:high`, run through the `pi` CLI because the subagent tool's codex provider
crashed; `reviews/z51-dbreak-review-1.md`).** Verdicts on §§1–6 as first written: rows 1, 2c, 2d, 3a, 3b (packaging),
3d, 4, 5 MAJOR; 2b FATAL as an arithmetic barrier but SOUND-WITH-MINOR as an abstract mixture lemma; 2a, 3c, 6
SOUND-WITH-MINOR. Independent reruns: N = 10⁷ top band byte-identical; independent brute force at 2·10⁴ matches,
including the top-band histogram. Repairs made:
* Thm 2.3: PD densities now carry candidate roughness to the horizon e^λ (the earlier w-rough density contradicted true
  zero counts for S forcing q | candidate, q ∈ (w, e^λ]); PD family restricted to 4em ≤ e^λ, which makes the
  within-shift exclusivity automatic (§2.3(α)); (I2) restricted to level ≤ λ; B_λ (profinite) separated from the finite
  A^{CRT}_λ; "≤" → "<"; inf instead of min with the finite-quotient reduction; R-term log(21/10). The theorem is now
  stated as a barrier for arguments using the listed axioms only, with the excluded kinds of input listed.
* Cor 2.3′: "every published K₂ ≥ 3.39" was false (Lichtman 3.2290; Wu's constant is 3.3996); rewritten as a statement
  about bounds of I3 form.
* Prop 2.4: unintegrated product corrected; restated as an existence statement.
* Lemma 2.5: range k ≤ L/log 3, Haar factorial moment only for k = o(μ); "the needed objects are the full factorial
  moments" and the "≍ M" moment order removed (k ≍ M/log(μ/M) suffices for central moments).
* Prop 3.1(b): Lemma 3.0(c) split at 16E²; the cutoff inversion and the range E₀ > N^{1/3} handled (Lemma 3.0(d));
  "every shift factor must be exact" → common-loss statement; NT/Henriot claims confined to the defined format.
* §3.2: "CRT-invisible" → linear at λ ≤ log N (≤ 3 band primes per term at 2 log N); one layer is sufficient, not shown
  necessary; "what TB needs" → a sufficient hypothesis; literature corrected (size laws vs residues; Tao–Teräväinen
  arXiv:2512.01739 quantitative; Gallagher fixed λ; Selberg's bound with its range).
* §4: Prop 4.1 restricted to constant centering (the arbitrary-μ(n) form was false); anatomy split relabelled as a plan.
* §5: o(1) is not a rate; necessity language removed.
* §1.3: quadratic large sieve stated with the squarefree condition; "carries all positive dependence" → suggested
  mechanism (heuristic in the source).
* §6: n = 1 convention; complete histograms (one observation at 10⁹ and five at 4·10⁹ were outside the printed bins);
  controls' top threshold √(2n) labelled.
Not accepted as stated: none. Theorem 2.6 was written after R1 started and is reviewed in R2.

**R2.** Pending.

## 8. Exact remaining gap

(to be finalised after R2)

* No depth-breaking bound is proved. T1-min(4ℤ) would follow from TB_δ for the top band, which polynomial-level CRT
  majorants cannot touch (§3.2) and which shows N^{−0.30} numerically.
* Within explicit axioms, one-sided PD information gains a constant (Thm 2.3); in the class-constant Cramér model,
  two-sided level-≤λ information gains nothing in the exponent (Thm 2.6). The arithmetic version of Thm 2.6 needs a
  sieve-limit theorem for roughness-refined (prime-law) majorants.
* Product forms over shifts are useless here (Prop 3.1); raw Chebyshev stops at N/μ (Prop 4.1).
* What would be new: any two-sided information about the top-band events (or the full event family) at total level
  above log N, a union lower bound for a block of mass ≫ √(log N), or a non-moment argument for the lower tail of X_top.
* Transfer to the full prime family 𝓕_N: upper bounds transfer (A_N ⊇ Av(𝓕_N)). Theorems 2.3 and 2.6 are stated for
  the 4ℤ-line classes; the same constructions apply to 𝓕_N with w(ℓ) the full count (the 8ℤ+7 line adds classes of the
  same type, still with no unit square), which changes only constants (Assessment).

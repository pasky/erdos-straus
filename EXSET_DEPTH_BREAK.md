# EXSET_DEPTH_BREAK — the first depth-breaking bound for the prime-modulus U family? (wave z51, lane 1a, slug `dbreak`)

ES is OPEN. Nothing here proves or disproves it.
Labels: PROVED / CONDITIONAL (on what) / CERTIFIED / EVIDENCE / CONJECTURE / Assessment.
Scripts: `scripts/z51_dbreak_*`. Data: `data/z51_dbreak/`. Brief: `../z51briefs/1a_opus_dbreak.md`.

## 0. Summary table

**Status: round 1 in progress (§1 written).**

| # | statement | label | § | review |
|---|---|---|---|---|
| 1 | target, three views (e/t/m) of one event, and the named non-CRT inputs; why each is outside EXSET_SIEVE_MASS Thm 2.2(c)(ii) | — | §1 | — |
| 2 | approach 1 (prime detection in the cofactor) | — | §2 | — |
| 3 | approach 2 (exponential moments over shifts) | — | §3 | — |
| 4 | approach 3 (anatomy / bilinear (e,m) incidence) | — | §4 | — |
| 5 | approach 4 (entropy decrement / averaged independence) | — | §5 | — |
| 6 | numerics and controls | — | §6 | — |
| 7 | reviews | — | §7 | — |
| 8 | exact remaining gap | — | §8 | — |

## 1. Target, reformulations, and the non-CRT inputs

### 1.1 The target, on the 4ℤ line

I = I_N = {n ≤ N : n ≡ 1 (mod 8)}. An *event* is a pair (ℓ, e) with ℓ ≤ N prime, e ≥ 1 and ℓ ≡ −1 (mod 4e); its
class is E_{ℓ,e} = {n : ℓ | n + 4e}. The *4ℤ-line avoider set* is

    A_N = {n ∈ I : n ∉ E_{ℓ,e} for every event (ℓ, e)}.

The z50 prime-modulus U family 𝓕_N (classes −v mod ℓ, v | ℓ+1, v ≡ 0 (4) or 7 (8), ℓ < n + v) contains the classes
E_{ℓ,e} as its v = 4e part, and on the 4ℤ line the proper-divisor condition ℓ < n + 4e is automatic (Lemma 1.1(d)). So
Av(𝓕_N) ∩ I ⊆ A_N, and

> **T1-min(4ℤ).** #(A_N ∖ □) ≤ N exp(−(log N)^{1/2+δ}) for some δ > 0

implies T1-min of the brief. Everything below is about A_N (a *larger* set than Av(𝓕_N), so bounds are harder, barriers
for it are barriers for nothing else; §8 records which statements transfer to 𝓕_N).

**Lemma 1.1 (three views of one event; PROVED, elementary).** Let n ≡ 1 (mod 8), e, t ≥ 1, and ℓ = 4et − 1 prime.
(a) ℓ | n + 4e ⟺ ℓ | tn + 1.
(b) If ℓ | n + 4e and m := (n + 4e)/ℓ, then n = 4etm − 4e − m (the word (t, u, v) = (t, 4e, m)), n + m = 4e(tm − 1),
    and tn + 1 = ℓ(tm − 1).
(c) The map (ℓ, e) ↦ (ℓ, t = (ℓ+1)/(4e)) is a bijection between events and pairs (ℓ, t) with ℓ ≡ −1 (mod 4t). Hence
    n ∈ A_N ⟺ for every e ≥ 1, n + 4e has no prime factor ℓ ≤ N with ℓ ≡ −1 (mod 4e)
           ⟺ for every t ≥ 1, tn + 1 has no prime factor ℓ ≤ N with ℓ ≡ −1 (mod 4t).
(d) In (b), m ≡ 3 (mod 4); in particular m ≥ 3, so ℓ < n + 4e.
(e) For fixed n and m, the events with cofactor m are exactly the divisors e of (n + m)/4 with (n + m)/(4e) ≡ −1 (mod m)
    for which (n + 4e)/m is a prime ≤ N.

*Proof.* (a) tn + 1 = t(n + 4e) − ℓ, and ℓ ∤ t since ℓ > t. (b) n = mℓ − 4e = m(4et − 1) − 4e; the other two are
expansions. (c) Immediate from (a). (d) mℓ = n + 4e ≡ 1 (mod 4) and ℓ ≡ 3 (mod 4). (e) n + 4e = mℓ with
ℓ ≡ −1 (mod 4e) ⟺ n + 4e ≡ −m (mod 4em) ⟺ 4e | n + m and m | (n + m)/(4e) + 1 (since n + m + 4e = 4e((n+m)/(4e) + 1)). ∎

**Lemma 1.2 (squares; Theorem E, recorded for the control).** No odd square x² lies in any E_{ℓ,e}. *Proof.* For an
odd prime q | e, ℓ ≡ −1 (mod q) and ℓ ≡ 3 (mod 4) give (q/ℓ) = (ℓ/q)(−1)^{(q−1)/2} = (−1/q)(−1)^{(q−1)/2} = 1; if 2 | e
then ℓ ≡ 7 (mod 8) and (2/ℓ) = 1. So (−4e/ℓ) = (−1/ℓ) = −1. ∎ Every forbidden class is a quadratic non-residue.

**Baseline (PROVED, z50).** #A_N ≪ N exp(−c√(log N)): EXSET_SIEVE_MASS Prop 2.3's lower-bound mass already uses only
u ∈ 4ℤ, so Thm 2.2(a) applies to A_N. And by Thm 2.2(c)(ii) (EXCEPTIONAL_THETA Thm 2.5 with slice primes ℓ ≡ 3 (4),
ℓ ≥ 11, and ℓ = 3, 7 moved into the small modulus Q₀ = 168, where |F_ℓ| ≤ ℓ/4 fails), every level-λ nonnegative CRT
majorant for A_N saves at most C√λ + O(log²λ). T1-min(4ℤ) asks for exponent 1/2 + δ.

**Mass profile (CERTIFIED counts, `scripts/z51_dbreak_sieve4.c`, `data/z51_dbreak/sieve4_*`).** The local density at
ℓ ≡ 3 (4) is w(ℓ)/ℓ with w(ℓ) = τ((ℓ+1)/4). The Haar mass grows with slope C₄ ≈ 0.59 in log ℓ (mass 3.23 at
ℓ = 1695, 7.14 at ℓ = 1.37·10⁶); compare C_V ≈ 0.74 for the full prime family. Events with ℓ > (N + 4e)/3 never meet I
(m ≥ 3 by Lemma 1.1(d)), so the effective mass at scale N is ≈ C₄ log(N/3). At N = 10⁹: |I| = 1.25·10⁸, 15 810 odd
squares, and #(A_N ∖ □) = 17 886 (the full z50 prime family leaves 4 932 non-squares). The Haar prediction for the
non-squares is 3.0·10³, so the non-square excess is e^{1.8}, the 4ℤ-line analogue of z50's D_ns.

### 1.2 Where the mass sits, and what "depth" means here

Each dyadic block ℓ ∈ (L, 2L] carries mass ≈ C₄ log 2 = O(1), spread uniformly in log e/log ℓ ∈ [0, 1] (each
divisor of (ℓ+1)/4 is one event). A level-λ CRT method can only certify the blocks with ℓ ≤ e^{c√λ} (dimension
κ(ℓ) ≍ log ℓ, so Σ_{ℓ ≤ y} w(ℓ) log ℓ/ℓ ≍ (log y)² must stay ≤ λ). T1-min therefore needs ≥ (log N)^{1/2+δ} units of mass
certified *jointly*. Taking the cheapest blocks first, these sit at primes up to exp((log N)^{1/2+δ}), whose product is
far above N. That is the depth problem of G1. Per n, R(n) := #{events containing n} has mean ≈ C₄ log N and is close to
Poisson (EVIDENCE, §6.2), so the target is a lower-tail (Poisson large-deviation) statement for R.

### 1.3 The non-CRT inputs, named, and why they are outside Thm 2.2(c)(ii)

Thm 2.2 (and its source, THETA Thm 2.5) caps bounds of the form N·Eν + (nonnegative rounding term), ν a nonnegative
finite combination of class indicators of level ≤ λ. Its engine is (b′)/Step 0: such a ν does not depend on n mod ℓ for
ℓ > e^λ, and inside the visible range the Rankin functional is ≍ √λ. The inputs tested here are not of that form.

* **(N1) Prime detection in the cofactor (PD).** By Lemma 1.1(b),(e), E_{ℓ,e} ∩ I = ⋃_m E^{PD}_{e,m}, where
  E^{PD}_{e,m} = {n ∈ I : n ≡ −4e − m (mod 4em), (n + 4e)/m is a prime ≤ N}. The indicator of E^{PD}_{e,m} is not a
  combination of class indicators of modulus ≤ N^{A}; its first moment is evaluated by Siegel–Walfisz/BV/Brun–Titchmarsh
  at modulus 4em, while as a CRT event its modulus is ℓ ≈ N/m. For m ≤ N^{1/2}/(4e) the PD modulus is smaller than ℓ:
  PD sees primes ℓ above every CRT horizon. (Outside (b′).)
* **(N2) Mean values of multiplicative functions over all primes.** E.g. Σ_{x≤X} z^{ω_e(x)}, ω_e(x) = #{ℓ | x : ℓ ≡ −1
  (4e)}, evaluated by Selberg–Delange (Dirichlet series in all primes up to X); more generally Shiu/Halász/Nair–Tenenbaum
  products over shifts. The single-shift evaluation sees all ℓ ≤ X with no dimension cost. (Outside (b′); see §3 for
  which part of the multi-shift technology is nevertheless a CRT majorant.)
* **(N3) Quadratic large sieve / Linnik duality.** Σ_{n}|Σ_{ℓ≤L} a_ℓ (n/ℓ)|² ≪ (NL)^ε(N + L)Σ|a_ℓ|² (Heath-Brown), with
  L up to N^{O(1)}: as a function of n the inner sum has period ∏ℓ ≫ N, and the proof is Poisson summation plus
  reciprocity (a character sum in ℓ of conductor ≍ n). It controls the *quadratic profile* (n/ℓ)_ℓ, which carries all
  positive dependence between shifts (EXSET_SHIFT_DIVISORS Remark 3.1(3)) and which squares fail completely.

Being outside the cap's hypotheses is necessary, not sufficient. Sections 2–5 test, input by input, whether it carries
the missing depth; each ends in a theorem or an exact blocking statement.

*Where squares must fail (control).* For n = x² every event indicator vanishes identically (Lemma 1.2). A statement of
T1-min strength is not contradicted by squares (their density N^{−1/2} is far below the target), but any *universal*
inequality behind it must fail on sets made of squares (G5). In each approach below the step that fails at squares is
named.


## 2. Approach 1: prime detection in the cofactor

Verdict first. PD is a genuine non-CRT input, and it does see primes above every CRT horizon. But (i) per unit of
level it carries *less* mass than the CRT representation (Prop 2.2), so it cannot relieve the depth accounting; and
(ii) whatever its level, PD information that is two-sided only at first order (BV, BFI, Type I/II, EH: all of these are
first moments) and one-sided at higher orders (every sieve upper bound for prime tuples) is worth at most a factor
C/(C − 1) in the avoider count, C the pair constant (Theorem 2.3), and this is sharp (Prop 2.4). Escaping needs
two-sided correlations of order ≳ √(log N) at total modulus above N (Lemma 2.5), which is the problem itself.

### 2.1 PD events and their first moments

Fix a CRT horizon λ (1 ≤ λ ≤ log N). For e ≥ 1 and m ≡ 3 (mod 4) put

    E^{PD}_{e,m} = {n ∈ I : n ≡ −4e − m (mod 4em), (n + 4e)/m is a prime in (e^λ, N]}.

By Lemma 1.1(b),(e), ⋃_{e,m} E^{PD}_{e,m} = ⋃_{e^λ<ℓ≤N} E_{ℓ,e} ∩ I, so A_N = A^{CRT}_λ ∖ ⋃ E^{PD}_{e,m}, where
A^{CRT}_λ ⊆ I avoids the events with ℓ ≤ e^λ. First moments are standard: #E^{PD}_{e,m} counts primes p ≤ (N + 4e)/m,
p > e^λ, with p ≡ −1 (mod 4e) and mp − 4e ≡ 1 (mod 8). Siegel–Walfisz/BV give its asymptotic on average over
4e ≤ N^{1/2−ε}, uniformly in m; Brun–Titchmarsh gives an upper bound always. Type I/II information and BFI-type levels
beyond 1/2 refine the same first moments.

### 2.2 The exchange rate between PD level and mass

**Proposition 2.2 (PROVED, Brun–Titchmarsh).** For 1 ≤ λ ≤ log N − 1,

    M_PD(λ) := Σ_{4em ≤ e^λ} #E^{PD}_{e,m}/#I ≤ C λ²/(log N − λ),

whereas the CRT mass at the same level is Σ_{ℓ≤e^λ} w(ℓ)/ℓ ≫ λ (EXSET_SIEVE_MASS Prop 2.3). So for λ ≤ (log N)/2,
M_PD(λ) ≤ C′(λ/log N)·mass_CRT(λ): per unit of level, PD buys a factor λ/log N *less* mass.

*Proof.* Brun–Titchmarsh: π(x; q, a) ≤ 2x/(φ(q) log(x/q)) for q < x. With x = (N + 4e)/m ≤ 2N/m, q = 4e, and
log(x/q) ≥ log(N/(4em)) ≥ log N − λ, we get #E^{PD}_{e,m} ≤ 4N/(m φ(4e)(log N − λ)). Divide by #I ≥ N/8 − 1 and use
Σ_{e≤x} 1/φ(4e) ≤ C(1 + log x) and Σ_{m≤x} 1/m ≤ 1 + log x. ∎

*Reading.* A PD event lumps all t (all primes ℓ = 4et − 1) at one cofactor, which is why its modulus is small; but it
pays the factor 1/log N for primality. A k-fold Bonferroni or moment term needs total modulus ≤ N. With CRT events this
allows k ≍ √(log N) (G1). With PD events the same accounting (level cost per unit mass ≈ log N/λ) allows only
k ≍ (log N)^{1/3}. So PD events cannot be the cheap layer of a depth argument.

### 2.3 The one-sided barrier (main result of this section)

**Setting.** A *model* is a probability space carrying x ∈ 1 + 8Ẑ (Ẑ the profinite completion; x plays n) and bits
π_j ∈ {0, 1} for j in a finite family 𝒥 of PD events (horizon λ as in §2.1). Fix measurable *PD densities*
r_j : 1 + 8Ẑ → [0, 1]. For instance, the Cramér–Granville densities
r_j(x) = 1[x ∈ class_j]·1[(x + 4e_j)/m_j has no prime factor ≤ w]·∏_{p≤w}(1 − 1/p)^{−1}/log(N/m_j) reproduce the
Hardy–Littlewood main terms of the true integers up to factors 1 + o(1). Let ℋ be Haar measure on 1 + 8Ẑ. An argument
of **type (λ; K₂, K₃, …)** uses only the following inputs; the true integers satisfy them up to their error terms.

* (I1) *CRT data at level λ:* E f(x) = E_ℋ f for every f of level ≤ λ (finite combinations of class indicators b mod d
  with Σ_{slice ℓ | d} log ℓ ≤ λ, as in THETA §1).
* (I2) *PD first moments, exact, at every level:* P(π_j = 1, x ∈ S) = E_ℋ[1_S r_j] for every j and every clopen S.
* (I3) *PD correlations, one-sided, every order:* P(π_J ≡ 1, x ∈ S) ≤ K_k E_ℋ[1_S ∏_{j∈J} r_j] for every k ≥ 2,
  every J ⊆ 𝒥 with |J| = k, and every clopen S.
* (I4) *Deterministic support:* π_j = 0 wherever r_j = 0. So π_j = 1 forces the class of j and the roughness of its
  candidate prime.

Such an argument *proves* "P(x ∈ A^{CRT}_λ, π ≡ 0) ≤ β" only if this holds in every model satisfying (I1)–(I4).

**Theorem 2.3 (one-sided PD information is worth a constant; PROVED).** Let C > 1. Suppose K_k ≥ C^{k−1} for every
k ≥ 2 and r_j ≤ 1/C for every j. Then some model satisfying (I1)–(I4) has

    P(x ∈ A^{CRT}_λ, π ≡ 0) ≥ (1 − 1/C)·β_λ,   β_λ := min{E_ℋ ν : ν a level-λ majorant of A^{CRT}_λ} ≥ e^{−C₁√λ − C₂ log²λ}.

Hence no argument of type (λ; K) with K_k ≥ C^{k−1} proves #A_N ≤ (1 − 1/C)β_λ·#I. With λ ≤ A log N it gains at most
log(C/(C − 1)) over the CRT cap of G1, and T1-min(4ℤ) is out of its reach.

*Proof.* (i) *A fake CRT law.* Let 𝒞 be a finite set of level-λ classes containing the trivial class. On a finite
quotient ℤ/Q (Q a common period of 𝒞 and of A^{CRT}_λ), the LP min{E_ℋ ν : ν ∈ span 1_𝒞, ν ≥ 1_{A^{CRT}_λ}} has the dual
max{ρ(A^{CRT}_λ) : ρ ≥ 0, ρ = ℋ on every class of 𝒞}, and ρ is a probability because the trivial class is in 𝒞. Finite
LP duality gives ρ_𝒞 with ρ_𝒞(A^{CRT}_λ) ≥ β_λ. The sets {ρ : ρ = ℋ on 𝒞, ρ(A^{CRT}_λ) ≥ β_λ} are weak-* closed (class
indicators and the clopen A^{CRT}_λ are continuous on 1 + 8Ẑ), nonempty and decreasing in 𝒞. By compactness some
probability ρ lies in all of them: ρ has Haar marginals on every level-λ class and ρ(A^{CRT}_λ) ≥ β_λ. The lower bound
for β_λ is THETA Thm 2.5 applied to the 4ℤ-line system of §1.1: Σ_ℓ w(ℓ)ℓ^{−1−α} ≪ 1/α by Brun–Titchmarsh, and one
optimises 19αλ + C/α.
(ii) *The mixture.* Let ξ be an independent coin with P(ξ = 1) = 1/C. On {ξ = 0}: x ~ ρ and π ≡ 0. On {ξ = 1}: x ~ ℋ
and, given x, the π_j are independent Bernoulli(C r_j(x)); this is allowed since C r_j ≤ 1.
(iii) *Checks.* (I1): the law of x is (1 − 1/C)ρ + (1/C)ℋ, which equals ℋ on level-λ functions. (I2):
P(π_j = 1, x ∈ S) = (1/C)E_ℋ[1_S C r_j] = E_ℋ[1_S r_j]. (I3): P(π_J ≡ 1, x ∈ S) = (1/C)C^k E_ℋ[1_S ∏ r_j]
= C^{k−1}E_ℋ[1_S ∏ r_j] ≤ K_k E_ℋ[1_S ∏ r_j]. (I4): C r_j = 0 wherever r_j = 0. Finally
P(x ∈ A^{CRT}_λ, π ≡ 0) ≥ P(ξ = 0)·ρ(A^{CRT}_λ) ≥ (1 − 1/C)β_λ. ∎

**Corollary 2.3′ (the known prime-tuple upper bounds).** Every published upper bound for correlations of primes in
linear forms has K₂ ≥ 3.39 for two forms (Selberg 8, Bombieri–Davenport 4, Chen 3.92, Wu 3.39 for twin primes) and
Selberg-type constants K_k = 2^k k!(1 + o(1)) for k ≥ 3, all ≥ 2^{k−1}. Taking C = 2: all sieve upper-bound information
on PD tuples, added to exact first moments at every level, gains at most a factor 2 over the CRT cap. (Selberg's parity
example makes 2 the natural floor for sieve-only pair constants; this folklore is not used.)

**Proposition 2.4 (sharpness; PROVED, Cauchy–Schwarz).** Without a CRT layer the constant is attained. If
R = Σ_{j∈𝒥} π_j has E R = μ and E[R(R − 1)] ≤ K₂μ², then P(R = 0) ≤ 1 − μ²/(μ + K₂μ²), which tends to 1 − 1/K₂ as
μ → ∞. The mixture with C = K₂ has P(R = 0) = 1 − 1/K₂ + (1/K₂)∏_j(1 − K₂r_j), which tends to 1 − 1/K₂. So one-sided
PD information is worth exactly log(K₂/(K₂ − 1)) in this regime. *Proof.* P(R > 0) ≥ (E R)²/E R². ∎

*What escapes Theorem 2.3 (each item excludes the mixture).*
(a) An upper bound for some k-point PD correlation with K_k < C^{k−1}, i.e. a two-sided, Hardy–Littlewood-quality
asymptotic. To gain M one needs K_k ≤ (1 + e^{−M})^{k−1} at some order, and the classical moment problem then asks for
two-sided control up to order ≍ M.
(b) A *lower* bound for a union, P(∃ j ∈ B : π_j = 1) ≥ 1/C + ε on a block of large mass. In the mixture the union has
probability ≤ 1/C. Such a bound is a T1-type statement itself.
(c) Relative statements inside sets that already avoid PD events (RLD (R1) for PD steps); the mixture concentrates such
sets on {ξ = 0}.
(d) Deterministic relations between PD bits and CRT data beyond (I4). None is known that is not already a congruence
on the candidate prime, which (I4) allows.

### 2.4 Two-sided PD information still meets the depth wall

**Lemma 2.5 (level-N content of the k-th factorial moment; PROVED for the CRT representation).** For k ≥ 1 and
L ≤ log N, and every α ∈ (0, 1],

    F_k(L) := Σ_{k-sets of events at distinct primes with Σ log ℓ_i ≤ L} ∏_i 1/ℓ_i ≤ e^{αL}(C/α)^k/k!.

So F_k(log N) ≤ (Ce² log N/k²)^k, while the Haar factorial moment E_ℋ C(R, k) is (C₄ log N)^k/k! up to (1 + o(1))^k.
For k ≥ C′√(log N) the part of the k-th moment visible at level N is ≤ e^{−k}.

*Proof.* Rankin: 1[Σ log ℓ_i ≤ L] ≤ e^{α(L − Σ log ℓ_i)}, and Σ_ℓ w(ℓ)ℓ^{−1−α} ≤ C/α (Brun–Titchmarsh). Take α = k/L
and use k! ≥ (k/e)^k. ∎

With PD representations (cost log(4em) instead of log ℓ) the Rankin sum gains Σ_{e,m} P(E^{PD}_{e,m})(4em)^{−α}
≪ 1/(α² log N) by Prop 2.2, i.e. ≪ log N/k² at α = k/log N. That is below the CRT term C log N/k. (Assessment: rigorous
in the Cramér–Haar model with HL main terms; for integers it presupposes the HL evaluation.) So even an exact
Hardy–Littlewood oracle for PD tuples *at total modulus ≤ N* leaves the exponent at 1/2. The needed objects are the full
factorial moments, i.e. k-point correlations Σ_n ∏_i ω_{e_i}(n + 4e_i) of restricted prime-factor counts at k ≳ √(log N)
shifts with total modulus above N. Already k = 3 of this type (Σ τ(n)τ(n+h₁)τ(n+h₂)) has no proved asymptotic.

**Blocking statement for approach 1 (exact).** PD helps only through (a) or (b) of §2.3. Beyond level N, (a) is the
k-point correlation problem for k ≳ √(log N), and (b) is the target. *Step that fails at squares:* none at the level of
first moments, since squares are a null set for (I2). The universal form of (b) ("every set with these PD first moments
contains a hit") fails on planted squares (G5).

## 3. Approach 2: exponential moments over shifts

(to be written)

## 4. Approach 3: anatomy and the bilinear (e, m) incidence

(to be written)

## 5. Approach 4: entropy decrement and averaged independence

(to be written)

## 6. Numerics and controls

(to be written)

## 7. Hostile reviews

(to be written)

## 8. Exact remaining gap

(to be written)

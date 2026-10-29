# EXSET_DEPTH_BREAK — the first depth-breaking bound for the prime-modulus U family? (wave z51, lane 1a, slug `dbreak`)

ES is OPEN. Nothing here proves or disproves it.
Labels: PROVED / CONDITIONAL (on what) / CERTIFIED / EVIDENCE / CONJECTURE / Assessment.
Scripts: `scripts/z51_dbreak_*`. Data: `data/z51_dbreak/`. Brief: `../z51briefs/1a_opus_dbreak.md`.

## 0. Summary table

**Status: rounds 1–2 written; round-1 hostile review pending.**

| # | statement | label | § | review |
|---|---|---|---|---|
| 1 | target, three views (e/t/m) of one event, and the named non-CRT inputs; why each is outside EXSET_SIEVE_MASS Thm 2.2(c)(ii) | — | §1 | — |
| 2a | exchange rate: PD events with modulus 4em ≤ e^λ carry mass ≪ λ²/log N, against ≍ λ for CRT events | PROVED (Brun–Titchmarsh) | §2.2 | — |
| 2b | **one-sided PD barrier:** CRT data at level λ + exact PD first moments at every level + PD k-point upper bounds with constants K_k ≥ C^{k−1} cannot prove #A_N ≤ (1 − 1/C)e^{−C₁√λ−C₂log²λ}#I; with all known sieve constants (C = 2) PD adds at most a factor 2 | PROVED (mixture + LP duality + THETA Thm 2.5) | §2.3 | — |
| 2c | sharpness: without CRT, Cauchy–Schwarz with pair constant K₂ gives P(no PD event) → 1 − 1/K₂, attained by the mixture | PROVED | §2.3 | — |
| 2d | the k-th factorial moment visible at level N is ≤ (C log N/k²)^k, ≤ e^{−k} for k ≳ √log N; PD representations add a lower-order Rankin term | PROVED (CRT part) | §2.4 | — |
| 2e | **two-sided PD barrier below the level cap:** CRT data at level λ + exact (Cramér–Haar) PD correlations of every order at total level ≤ λ cannot prove #A_N ≤ ½e^{−C√λ}#I (random subfamily + LP duality + the Thm 3.2 sieve-limit run with supply exponent 1) | PROVED given the KARY/EK framework (EXSET_SIEVE_MASS Thm 3.2 proviso) | §2.4 | — |
| 3a | cost profile of shifts; product-form shift bounds (Nair–Tenenbaum/Henriot/Shiu shape) with loss C > 1 per shift save ≪ (log log N)² log log log N; loss 1 + ε needs ε ≤ exp(−M/(C log log N)) to save M | PROVED (BT, PNT mod 8) | §3.1 | — |
| 3b | decoupling: upper bounds need one layer only (no RLD between layers); T1-min ⟸ (TB_δ), and a power saving for E_U off squares ⟸ (TB_pow), for the CRT-invisible top band ℓ > √(2N) | PROVED (trivial) | §3.2 | — |
| 3c | top band: P(X_top = 0) ≈ 1.4·e^{−E X_top}, slope −0.30 in log N over 10⁷–10⁹ | CERTIFIED counts / EVIDENCE | §3.2 | — |
| 3d | what TB needs: joint law of P⁺(n+4e) mod 4e at exp((log N)^{1/2+δ}) shifts with precision exp(−(log N)^{1/2+δ}); known only for 2 shifts with o(1) errors | Assessment (literature) | §3.2 | — |
| 4 | bilinear (e,m) incidence = PD system; L² methods stop at N/μ (Var X ≥ E X/2 in the Haar model; 1.05–1.12 on integers); anatomy moves depth between candidate count and primality | PROVED (model) / EVIDENCE / Assessment | §4 | — |
| 5 | entropy decrement / averaged independence: additive o(1) errors certify ≤ O(log log N); bounded k | PROVED (trivial) + Assessment | §5 | — |
| 6 | census of the 4ℤ-line family to 10⁹, independent cross-check at 2·10⁴, Poisson dispersion, controls (squares, U failures, hard primes, R-zeros, 17, 241) | CERTIFIED / EVIDENCE | §6 | — |
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

implies T1-min of the brief. Everything below is about A_N, a *larger* set than Av(𝓕_N): upper bounds for A_N transfer
to 𝓕_N, while the barriers proved here are for A_N (§8 records how they extend to the full prime family).

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
≪ 1/(α² log N) by Prop 2.2, i.e. ≪ log N/k² at α = k/log N, below the CRT term C log N/k. The following theorem makes
this rigorous at the level of what any argument can extract from such data.

**Theorem 2.6 (two-sided PD information below the level cap adds nothing to the exponent; PROVED given the KARY/EK
framework of EXSET_SIEVE_MASS Thm 3.2, run with supply exponent 1).** Let W be the absolute constant of that theorem,
1 ≤ λ ≤ (log N)/2, and let 𝒥 be a finite family of PD events j = (e_j, m_j). Give j the level
s_j = Σ_{ℓ | 4e_jm_j, ℓ > W} log ℓ and assume s_j ≤ λ. The *Cramér–Haar model* CH draws x ~ ℋ and independent coins
κ_j ~ Bernoulli(ρ_j), and sets π_j = 1[x ∈ class_j]κ_j, where class_j is the class −4e_j − m_j (mod 4e_jm_j) (refined
mod 8 to lie in 1 + 8Ẑ) and 0 ≤ ρ_j ≤ C₀(4e_j/φ(4e_j))/(log N − λ) (the Brun–Titchmarsh size of the true conditional
prime density). A *mixed monomial* 1_S(x)∏_{j∈J}π_j has level (level of S) + Σ_{j∈J} s_j. Then there is a joint law of
(x, π) that agrees with CH on every mixed monomial of level ≤ λ (so every two-sided Hardy–Littlewood-type statistic
of PD tuples and every CRT statistic at level λ is reproduced exactly), and in which

    P(x ∈ A^{CRT}_λ, π ≡ 0) ≥ ½ exp(−C√λ),   C absolute.

So an argument whose inputs are CRT data at level λ plus *exact* PD correlations of every order at total level ≤ λ
cannot prove #A_N ≤ ½e^{−C√λ}#I. With λ ≍ log N this is the exponent 1/2 again.

*Proof.* (1) *Random subfamily.* Let 𝒥′ ⊆ 𝒥 contain each j independently with probability ρ_j.
(2) *Its supply is linear.* With Γ, G and 𝔐 as in EXSET_BEYOND_CRT §2 / EXSET_SIEVE_MASS §3, let
𝔐_{𝒥′}(y) = Σ_{j∈𝒥′, W<P(G_j)≤y} Γ(G_j)/G_j, G_j ≍ 4e_jm_j the modulus of class_j. Then
E𝔐_{𝒥′}(y) ≤ (C/(log N − λ)) Σ_{P(em)≤y} Γ(4em)(4e/φ(4e))/(4em) ≤ C′(log y)²/(log N − λ), which is ≤ C′ log y for
y ≤ e^λ (as log y ≤ λ ≤ log N − λ); for y > e^λ, 𝔐_{𝒥′}(y) = 𝔐_{𝒥′}(e^λ). Each summand is ≤ Γ(G)/G ≤ C″, so Bernstein's
inequality and a union bound over y = e^{2^i} give, with probability ≥ ½, 𝔐_{𝒥′}(y) ≤ K log y for all y ≥ y₀, with K,
y₀ absolute (monotonicity in y covers intermediate y). The prime-local classes −4e (mod ℓ), ℓ ≤ e^λ, have supply
≤ K log y by Brun–Titchmarsh (EXSET_SIEVE_MASS Prop 2.3).
(3) *The cap for the realised family.* Let 𝔊(𝒥′) be the prime-local classes at ℓ ≤ e^λ, the classes of 𝒥′, and the
classes n ≢ 1 (mod 8). All are classes of the U-family 𝔘 of EXSET_SIEVE_MASS §1.1 (word classes with an endpoint
u = 4e ∈ S, or the excluded residues mod 8), so they contain no unit square (base), and the cofactor sums (iii) hold
because they hold for 𝔘 and only decrease for subfamilies. Run the proof of EXSET_SIEVE_MASS Thm 3.2 with the first
moment K log y in place of K(log y)²(log log y)²: take s₁ = √λ; singletons cost ≤ (8/3)K√λ; block i (s = 2^i s₁,
d_i = ⌊λ/s⌋) has (E M_{V_i} + 4d_i)/d_i ≤ 2K·4^i + 4, so Σ_i EΦ_i ≤ Cλ/s₁ + O(log²λ). Hence, on the event of (2), every
level-λ majorant ν ≥ 0 of 𝒜(𝔊(𝒥′)) has Eν ≥ e^{−2W−log 2−C√λ}.
(4) *Fake laws.* As in Thm 2.3(i) (finite LP duality plus weak-* compactness), on the event of (2) there is a
probability ρ_{𝒥′} on Ẑ with Haar marginals on every level-λ class and ρ_{𝒥′}(𝒜(𝔊(𝒥′))) ≥ e^{−2W−log 2−C√λ}. Off that
event put ρ_{𝒥′} = ℋ.
(5) *The model.* Draw 𝒥′, then x ~ ρ_{𝒥′}, and set π_j = 1[j ∈ 𝒥′, x ∈ class_j]. For a mixed monomial of level ≤ λ,
1_S ∏_{j∈J} 1_{class_j} is a class indicator of level ≤ λ, so E[1_S ∏_J π_j | 𝒥′] = 1[J ⊆ 𝒥′]·ℋ(S ∩ ⋂_J class_j) for every
𝒥′, and averaging over 𝒥′ gives ∏_J ρ_j·ℋ(S ∩ ⋂_J class_j), the CH value. If x ∈ 𝒜(𝔊(𝒥′)) then x ∈ A^{CRT}_λ and every
π_j = 0. So P(x ∈ A^{CRT}_λ, π ≡ 0) ≥ ½e^{−2W−log 2−C√λ}. ∎

*Scope.* Theorem 2.6 covers two-sided PD information whose total level is ≤ λ; Theorem 2.3 covers one-sided PD
information at every level. Neither covers two-sided PD correlations at total level above log N, i.e. the full factorial
moments of R: the k-point correlations Σ_n ∏_i ω_{e_i}(n + 4e_i) of restricted prime-factor counts at k ≳ √(log N) shifts
with total modulus above N. Already k = 3 of this type (Σ τ(n)τ(n+h₁)τ(n+h₂)) has no proved asymptotic. Local
(Cramér–Granville) factors in ρ_j can be included by refining class_j modulo a fixed W-smooth modulus; this changes only
the constants (Assessment).

**Blocking statement for approach 1 (exact).** PD helps only through (a) or (b) of §2.3. Beyond level N, (a) is the
k-point correlation problem for k ≳ √(log N), and (b) is the target. *Step that fails at squares:* none at the level of
first moments, since squares are a null set for (I2). The universal form of (b) ("every set with these PD first moments
contains a hit") fails on planted squares (G5).

## 3. Approach 2: exponential moments over shifts

Write X(n) = R(n) = Σ_e ω_e(n + 4e) (the number of events containing n), with ω_e(x) = #{ℓ | x prime, ℓ ≤ N, ℓ ≡ −1 (4e)}
(Lemma 1.1(c)). For 0 ≤ z < 1, P(X = 0) ≤ E z^X = #I^{−1} Σ_{n∈I} ∏_e z^{ω_e(n+4e)}, a correlation of multiplicative functions
at many shifts. Verdict: product-form bounds over shifts are useless for this family even with O(1) loss per shift
(Prop 3.1); the exponential moment needs no joint control *between* layers (Lemma 3.2), which reduces T1-min to a
single CRT-invisible layer, the top band (Cor 3.3); there the needed input is a joint law of largest prime factors at
exp((log N)^{1/2+δ}) shifts, known today only for two shifts with o(1) errors.

### 3.1 Product forms over shifts: the cost profile of the prime family

For a shift e let F_e = {n ∈ I : ω_e(n + 4e) = 0} and cost(e) = log(#I/#F_e). A *product-form* bound is one of the shape

    #A_N/#I ≤ ∏_{e∈S} min{1, C_e π_e} + R,   π_e ≥ #F_e/#I,  C_e ≥ 1,  R ≥ 0,

which is what Nair–Tenenbaum/Henriot/Shiu-type arguments over a set S of shifts deliver (their constants C_e absorb the
truncation and the local factors). Its saving is at most Σ_{e∈S}(cost(e) − log C_e)^+, since
min{1, C_e π_e} ≥ exp(−(cost(e) − log C_e)^+).

**Lemma 3.0 (cost profile; PROVED, Brun–Titchmarsh and PNT mod 8).** Uniformly for 4e ≤ N/2 and N ≥ N₀:
(a) cost(e) ≤ log log N + O(1);
(b) 1 − #F_e/#I ≤ C₀(1 + log 4e + log log N)/φ(4e);
(c) Σ_{e≤E}(1 − #F_e/#I) ≤ C₀(1 + log log N) log E for 2 ≤ E ≤ N^{1/3}.
*Proof.* (a) If n + 4e is prime then n ∈ F_e: its only prime factor is ≡ n (mod 4e), and n ≢ −1 (mod 4) for n ∈ I. The
primes in (4e, N + 4e] in the class 1 + 4e (mod 8) number ≫ N/log N. (b) P(ℓ | n + 4e) ≤ 1/ℓ + 9/N for n uniform on I.
Sum over ℓ ≡ −1 (mod q), q = 4e: the ℓ ≤ q² contribute ≤ Σ_{j≤q} 1/(jq − 1) ≤ 2(1 + log q)/q; the ℓ ∈ (q², 2N] contribute
≤ (4/φ(q))(log log 2N − log log q² + 1) by partial summation with π(t; q, −1) ≤ 4t/(φ(q) log t) (Brun–Titchmarsh, t ≥ q²);
the 9/N terms add ≤ 9π(2N; q, −1)/N ≪ 1/φ(q). (c) Swap sums: for ℓ ≤ E², Σ_{ℓ≤E²} #{e : 4e | ℓ+1}/ℓ ≤
Σ_{ℓ≤E²} τ((ℓ+1)/4)/ℓ ≪ log E (Titchmarsh-type upper bound by Brun–Titchmarsh); for ℓ > E² ≥ (4e)²/16 use the second
part of (b) for each e ≤ E, and Σ_{e≤E} 1/φ(4e) ≪ log E. ∎

**Proposition 3.1 (product forms over shifts are useless here; PROVED from Lemma 3.0).**
(a) If C_e ≥ C > 1 for every e ∈ S, the saving of a product-form bound is ≪_C (log log N)² log log log N.
(b) If C_e = 1 + ε for every e ∈ S, the saving is ≤ C₁ log log N·(log(1/ε) + log log log N) + C₁(log log N)²·log log log N.
    So saving M = (log N)^{1/2+δ} needs ε ≤ exp(−M/(C₂ log log N)): every shift factor must be exact to within
    exp(−(log N)^{1/2+δ−o(1)}).
*Proof.* (a) (cost(e) − log C)^+ > 0 forces 1 − #F_e/#I > 1 − 1/C, hence by Lemma 3.0(b) φ(4e) < C₀(1 + log 4e + L₂)/(1 − 1/C),
i.e. e ≤ E₁ ≍_C L₂L₃ (L_j the j-fold iterated log of N). Each such shift contributes ≤ cost(e) ≤ L₂ + O(1) (Lemma 3.0(a)).
(b) A shift contributes only if cost(e) > log(1 + ε) ≥ ε/2. For e > E₁ we have cost(e) ≤ 2(1 − #F_e/#I), so by Lemma 3.0(b)
contributing shifts satisfy e ≤ E₀ with log E₀ ≤ log(1/ε) + O(L₃ + log L₂). Their total is ≤ E₁(L₂ + O(1)) +
2Σ_{e≤E₀}(1 − #F_e/#I), and Lemma 3.0(c) bounds the last sum by C₀(1 + L₂) log E₀. ∎

*Reading.* For the full U family, lane D (EXSET_SHIFT_DIVISORS Thm 5.1, 5.3) found (log N)^{log 2+o(1)} costly shifts and
precision (log N)^{−0.0037}. For the prime family the per-shift cost is only ≈ log(log N/log 4e)/φ(4e), so the useful
shifts number ≍ L₂L₃ and the product form collapses to (log log N)^{2+o(1)}: worse than the CRT sieve itself. A
Shiu-type argument with O(1) loss per shift (the brief's question) is therefore not enough by a wide margin; it would
need per-shift precision exp(−(log N)^{1/2+δ−o(1)}). The Nair–Tenenbaum/Henriot proofs are in addition CRT majorants after
their first step (they bound the z-rough part of each n + 4e by f ≤ 1 and sieve the z-smooth parts), so G1 applies to
them regardless of constants.

### 3.2 Layers decouple for upper bounds

**Lemma 3.2 (decoupling; PROVED, trivial).** For any subfamily B of events, A_N ⊆ Av(B). For subfamilies B₁, …, B_k and
z ∈ [0, 1), E z^{X_{B₁}+⋯+X_{B_k}} ≤ ∏_i (E z^{k X_{B_i}})^{1/k} (Hölder). In particular, if one layer B satisfies
#Av(B) ∩ (I ∖ □) ≤ N e^{−M}, so does A_N.

So T1-min (and any power saving) needs *one* subfamily with a super-√(log N) lower tail; no relative statement between
layers (no RLD step) is needed. RLD-U is different: it asks for the full Mertens product, for which Hölder loses a factor
k in the exponent; it genuinely needs near-independence of all layers.

Which layer? The small primes ℓ ≤ e^{c√(log N)} are exactly where CRT works and stops (G1). For a band of large primes
(N^{a}, N^{b}] with a ≥ 1/4 the CRT is worse still: by EXSET_SIEVE_MASS Thm 2.2(c)(iii) a level-λ majorant with
λ ≤ 2 log N saves only O(log(2 + μ)) on the band (linear in the hits for λ ≤ log N, quadratic for λ ≤ 2 log N). The
cleanest large layer is the *top band* ℓ > √(2N): each n + 4e ≤ 2N has at most one prime factor there, namely P⁺(n + 4e).

**Corollary 3.3 (reduction to the top band; PROVED, trivial).** Put X_top(n) = #{e ≥ 1 : P⁺(n + 4e) > √(2N),
P⁺(n + 4e) ≡ −1 (mod 4e)}. Then A_N ⊆ {X_top = 0}. Hence
* (TB_δ) #{n ∈ I ∖ □ : X_top(n) = 0} ≤ N exp(−(log N)^{1/2+δ}) implies T1-min(4ℤ) and T1-min;
* (TB_pow) #{n ∈ I ∖ □ : X_top(n) = 0} ≤ N^{1−c} implies #{n ≤ N, n ≡ 1 (4) : U(n) fails} = #{odd squares ≤ N} + O(N^{1−c}),
  a power saving for E_U off the squares, hence also for E_{ES₅} (E_{ES₅} ≤ E_U, z50).
*Proof.* The events of the top band are events; U failure at non-squares n ≡ 1 (8) implies n ∈ Av(𝓕_N) ⊆ A_N, and U
holds at every n ≡ 5 (mod 8), n > 5 (z50 Obs. 6.0). ∎

By Lemma 1.1(e), X_top(n) = #{(m, e) : m < √(2N)·(1 + o(1)), m ≡ 3 (4), e | (n + m)/4, (n + m)/(4e) ≡ −1 (mod m),
(n + 4e)/m prime > √(2N)}: for each small cofactor m, the divisors of the single integer (n + m)/4 in one class mod m
produce candidates, and one of the ≈ (log N)²·c candidates must be prime. Its mean is ≈ (C₄/2) log N·(1 + o(1)) minus the
unreachable part ℓ > (N + 4e)/3.

**What TB needs (Assessment, with literature).** The top band is invisible to CRT (above), to one-sided PD (Thm 2.3,
whose proof never used the band), and to PD with HL at total modulus ≤ N (Lemma 2.5 with all PD moduli 4em ≤ e^λ; the
Rankin term is ≪ log N/k², which reaches only k ≍ (log N)^{1/3}). It is a statement about the joint law of the residues
P⁺(n + 4e) mod 4e over exp((log N)^{1/2+δ}) shifts e, at precision exp(−(log N)^{1/2+δ}). The joint law of P⁺ at *two*
consecutive integers is known only with o(1) errors: Teräväinen (2018) in logarithmic density, and the OpenAI release
(item 012, *The joint Dickman law for consecutive integers*, unrefereed) in natural density, by a qualitative
iterated-limit argument; Tao–Teräväinen's quantitative version holds outside an exceptional set of scales. The analogous
Poisson tail for primes in short sets (no prime in [x, x + H], H = λ log x, probability e^{−λ}) is known only under uniform
Hardy–Littlewood (Gallagher); under RH Selberg's bound gives only #{x ≤ X : no prime in [x, x + H]} ≪ X(log X)²/H, a
polylogarithmic saving. TB_δ asks for a super-√ Poisson tail in a structured set of ≍ (log N)² candidates: by analogy,
beyond RH-type technology (Assessment; no implication is claimed).

**Numerics for the top band (CERTIFIED counts, EVIDENCE for the trend; `data/z51_dbreak/sieve4_top_N*.txt`).**
Non-squares n ∈ I, top band ℓ > √(2N):

| N | E X_top | P(X_top = 0) | e^{−E X_top} | ratio | P(X_top = 0 \| small layer avoided) |
|---:|---:|---:|---:|---:|---:|
| 10⁷ | 3.534 | 0.03844 | 0.02919 | 1.32 | 0.0841 |
| 10⁸ | 4.251 | 0.01975 | 0.01425 | 1.39 | 0.0461 |
| 10⁹ | 4.989 | 0.00981 | 0.00681 | 1.44 | 0.0236 |
| 2·10⁹ | 5.209 | 0.00795 | 0.00547 | 1.45 | 0.0193 |
| 4·10⁹ | 5.429 | 0.00644 | 0.00439 | 1.47 | 0.0158 |

log P(X_top = 0) falls with slope −0.30 in log N (−0.297 over 10⁷–10⁹, −0.304 over 10⁹–4·10⁹), so the top band alone
already shows N^{−0.30} (EVIDENCE for TB_pow, 2.6 decades). The ratio to the Poisson value grows slowly and
decelerates (log ratio 0.28, 0.33, 0.36, 0.37, 0.38; increments per decade 0.051, 0.038, 0.032): mild positive
dependence, consistent with the quadratic-profile mechanism (squares and near-squares are QR-rich; z50 lane D). The
histogram of X_top is close to Poisson at every N (§6). Conditioning on the small layer (ℓ ≤ √(2N)) lowers E X_top
(4.99 → 4.20 at N = 10⁹) and raises P(X_top = 0) by a factor 2.4: the layers are positively dependent, which is why
Lemma 3.2 (no conditioning) is the right way to use them. For the record, the whole 4ℤ-line family leaves 23 727 and
31 612 non-squares at N = 2·10⁹ and 4·10⁹ (squares: 22 360 and 31 622), so at 4·10⁹ the non-square avoiders are as
many as the squares.

## 4. Approach 3: anatomy and the bilinear (e, m) incidence

Verdict: the bilinear (e, m) form is the PD system of §2 summed over n; every L² method on it (dispersion, large sieve
in (e, m), Cauchy–Schwarz) is a second-moment method and stops at N/μ; anatomy controls the *candidates* (divisors of
one integer (n + m)/4 per cofactor m), not their primality or their joint law.

### 4.1 The incidence form and its L² ceiling

By Lemma 1.1(b),(e), X(n) = #{words (t, 4e, m) of n with 4et − 1 prime ≤ N}: each n has C(n) := #{4ℤ-line words of n}
candidates (mean ≍ c(log N)²; C(x²) = 0 by Theorem E), and X(n) counts those whose pivot tu − 1 is prime. Double counting,
Σ_n X(n) = Σ_{e,m} #E^{PD}_{e,m}, and Σ_n X(n)² = Σ_{(e,m),(e′,m′)} #(E^{PD}_{e,m} ∩ E^{PD}_{e′,m′}), where each pair is the binary
prime problem m p − m′p′ = 4(e − e′), p ≡ −1 (4e), p′ ≡ −1 (4e′). For fixed coefficients this is of twin-prime type; averaged
over (e, m, e′, m′) it is the setting where circle-method or dispersion asymptotics are plausible.

**Proposition 4.1 (L² ceiling; PROVED for the Haar model, EVIDENCE for integers).** Any bound of the form
#{X = 0} ≤ Σ_n (X(n) − μ(n))²/min_n μ(n)² (dispersion; large sieve in (e, m); Turán–Kubilius) is at best ≍ N·Var X/(E X)².
In the Haar model Var X = Σ_ℓ (w(ℓ)/ℓ)(1 − w(ℓ)/ℓ) ≥ E X/2 (classes at one prime are disjoint, classes at distinct primes
are independent), so these bounds are ≫ N/log N. On the integers Var X/E X = 1.05–1.12 (§6.2). *Proof.* Variance of a sum
of indicators with the stated covariance structure. ∎
So L² information on the incidence (exact, even with an asymptotic for the averaged binary problem) gives a
polylogarithmic saving only. Combined with one-sided higher correlations it gains at most log(K₂/(K₂ − 1)) more (Thm 2.3,
Prop 2.4).

### 4.2 Anatomy: candidates versus primes

The m-view (Lemma 1.1(e)) makes the candidates of cofactor m the divisors e of the single integer (n + m)/4 in one class
mod m. Hall–Tenenbaum/Ford anatomy and Erdős–Hall (divisors in residue classes) control these divisor sets for one
integer at a time; they are the right tools for C(n), not for X(n). One can split

    P(X = 0) ≤ P(C(n) ≤ K) + P(X = 0, C(n) > K),

with K = (log N)^{3/2+δ}, so that "K candidates, each prime with probability ≍ 1/log N" would give e^{−(log N)^{1/2+δ}} in a
Poisson model. *Blocking (Assessment, with a PROVED count).* (i) The first term is a lower-tail statement for the full
(composite-pivot) word count. CRT methods see only words with all moduli ≤ T, log T ≤ (log N)^{1/3} (the 2/3 exponent of
lane E), i.e. ≪ (log T)² ≤ (log N)^{2/3} visible words per n, far below K; so (i) also needs depth beyond CRT. (ii) The
second term is the PD problem with K candidates and falls under Thm 2.3 for one-sided inputs. Anatomy therefore moves
the difficulty between the two factors without removing it.

**Blocking statement for approach 3 (exact).** The bilinear incidence is the PD system; L² methods stop at N/μ
(Prop 4.1), one-sided higher information at a constant (Thm 2.3), two-sided information below the level cap at
exponent 1/2 (Thm 2.6). *Step that fails at squares:* none in the L² bound (squares are a null set). In the anatomy
split, squares sit in the first term (C(x²) = 0), which is why that term, unlike the second, must use non-residue
information.

## 5. Approach 4: entropy decrement and averaged independence

**Lemma 5.1 (additive-error floor; PROVED, trivial).** If an argument shows |P(X_B = 0) − P_model(X_B = 0)| ≤ η for some layer
B, it certifies a saving of at most log(1/η).

The averaged-independence technology produces additive errors that are o(1), not exponentially small: the
Matomäki–Radziwiłł short-interval theorem and the Matomäki–Radziwiłł–Tao averaged Elliott bound have errors that are
powers of log h or log X (or worse), Tao's entropy decrement and Tao–Teräväinen's odd-order Chowla are qualitative or
doubly logarithmic, and all treat a bounded number k of shifts (or averages over one shift). By Lemma 5.1 they certify at
most O(log log N) here. Averaging over e is not a substitute for joint control either: by Lemma 3.2 the target is the lower
tail of one sum X_B, and "independence on average over pairs (e, e′)" is second-moment information (Prop 4.1, N/μ);
averaged k-wise independence gives the k-th moment, and the moment problem needs k ≳ M with relative precision e^{−M}
(§2.3(a)).

**Blocking statement for approach 4 (exact).** Entropy/averaging methods would need (i) a number of simultaneous shifts
exp((log N)^{1/2+δ}) (the shifts e carrying the top-band mass (log N)^{1/2+δ} in §3.2) and (ii) additive precision
exp(−(log N)^{1/2+δ}). Present results give k = 2 (or bounded k) and o(1). Nothing in this route is specific to squares;
the square step is the same as in §2.

## 6. Numerics and controls

All runs with `ulimit -v 8000000` and timeouts; C source `scripts/z51_dbreak_sieve4.c` (usage `sieve4 N Y`, optional
`DUMP=file`), Python `scripts/z51_dbreak_controls.py`, `scripts/z51_dbreak_xcheck.py`.

### 6.1 Census of the 4ℤ-line prime family (CERTIFIED)

* Independent cross-check: the brute-force e-view enumeration (factor n + 4e for e ≤ (n + 3)/8) and the sieve agree
  exactly on A_N at N = 2·10⁴ (160 avoiders, 70 of them squares; `data/z51_dbreak/xcheck_alive_N20000.txt`). The
  t-view (ℓ | tn + 1, ℓ ≡ −1 (4t)) agrees with the e-view on every control below 3000 (Lemma 1.1(c)).
* No square was ever hit (the sieve reports any square hit on stderr; none occurred at N = 10⁷, 10⁸, 10⁹).
* #(A_N ∖ □) = 2 457, 6 836, 17 886 at N = 10⁷, 10⁸, 10⁹ (squares 1 580, 4 999, 15 810), i.e. density
  1.97·10⁻³, 5.47·10⁻⁴, 1.43·10⁻⁴ of I: slope −0.57 in log N.

### 6.2 Poisson behaviour of the large layers (EVIDENCE)

Variance/mean of the number of events with ℓ > Y, over non-squares:

| N | Y | mean | var/mean (all) | mean, var/mean (small layer avoided) |
|---:|---:|---:|---:|---:|
| 10⁹ | 10³ | 7.17 | 1.05 | 6.48, 1.19 |
| 10⁸ | √(2N) | 4.25 | 1.12 | 3.47, 1.20 |
| 10⁹ | √(2N) | 4.99 | 1.12 | 4.20, 1.20 |

The large layers are close to Poisson, mildly over-dispersed; conditioning on the small layer lowers the mean and raises
the dispersion (positive dependence through the quadratic profile). The top-band lower tail is tabulated in §3.2.

### 6.3 Controls (`data/z51_dbreak/controls.json`)

| n | events R(n) | top-band events | least event prime | n ∈ A_N |
|---|---:|---:|---:|---|
| odd squares 9 … 998001 | 0 | 0 | — | yes (Lemma 1.2) |
| 105, 2961, 3985, 25305, 111969, 978145 (the U failures) | 0 | 0 | — | yes |
| 193, 2521, 3361, 9601, 66529 (hard primes) | 0 | 0 | — | yes |
| 409, 577, 5569, 8813281 (hard primes) | 2, 3, 2, 5 | 1, 2, 0, 2 | 7, 7, 47, 191 | no |
| R-zeros 23929, 83449, 102001, 329617, 712321, 1134241, 1724209, 1726201, 5212561 | 4, 2, 3, 2, 2, 7, 2, 1, 4 | 1, 2, 2, 1, 1, 3, 2, 1, 3 | 7, 7591, 23, 71, 23, 7, 5147, 5279, 503 | no |
| 17, 241 (numerator 8) | 2, 3 | 1, 1 | 3, 7 | no |

Readings. Five of the nine hard primes avoid the whole 4ℤ-line prime family; an exceptional-set statement must allow
such survivors, and nothing here is pointwise. Several R-zeros are hit only in the top band (83449, 1724209, 1726201),
which is the layer of Cor 3.3. Numerator 8: none of the statements here is pointwise or transfers to 8/n; the barrier
theorems are family-agnostic upper-bound statements, and Cor 3.3 is an inclusion of avoider sets, so there is nothing to
falsify at 17 or 241 (both are in fact hit by 4ℤ-line prime events for 4/n).

## 7. Hostile reviews

(to be written)

## 8. Exact remaining gap

(to be written)

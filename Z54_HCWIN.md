# Z54_HCWIN — the growing-window target HC(p) ≤ (log p)^A, A > 2 log 2: anatomy layer vs class layer (wave z54, lane HCWIN)

**ES is OPEN. Nothing here proves or disproves ES.** Labels: PROVED / CONDITIONAL (on what) / CERTIFIED / EVIDENCE /
CONJECTURE / Assessment. Internal results, internally reviewed only. Scripts `scripts/z54_hcwin_*`, data `data/z54/hcwin/`.
Kickoff: `z52bbriefs/z54_lanes.md` §HCWIN (FRONTIER §7.2).

## 0. Verdict first

**Verdict: NARROWED, with one small conditional strengthening.** S_A is not proved. The lane gives a *sufficient* route
to S_A through an anatomy layer, a genus layer and a class layer. It proves what is provable about the anatomy layer and
calibrates the class layer in the model and on data. S_A does not imply the anatomy statement; the route is sufficient,
not a factorisation.

1. **Where 2 log 2 comes from (Theorem B; PROVED relative to Henriot's uniform Nair–Tenenbaum bound and
   Bombieri–Vinogradov).** The relevant quantity is the *truncated divisor mass* of the window integers,
     Λ(p, X) := Σ_{x∈𝒞, x≤X} [min(1, τ(p+x)/φ(x)) + min(1, τ(xp+1)/φ(x))],
   averaged over primes p. Put X = (log T)^θ and κ = θ/log 2.
   * For 1 < κ < 2, the average of Λ over p ∈ (T, 2T] is ≤ (log T)^{g(κ)+o(1)} = o(log T), where
     g(κ) = κ log 2 − κ log κ + κ − 1 < 1. This is an upper bound; for κ ≤ 1 the bound o(log T) is trivial.
   * For κ > 2, the average is ≫_θ log T · log log T.
   So 2 log 2 separates two proved regimes of an arithmetic quantity. The boundary itself is not decided.
   * Mechanism (Rankin): E_p τ(p+x)^s ≪ (log p)^{2^s−1} (with ≍ at s = 1), so the mean of τ is carried by
     ω ≈ 2 log log p. The exponents match the model's g(κ) (HCSHIFTS §3.2).
   * It is an average over p (B6), so it only *calibrates* the threshold.
2. **What is provable at a single p (Theorem A; PROVED, elementary).**
   * Turán–Kubilius over the window variable x is exact, but only for primes ≤ X^{1/2}. The provable single-p anatomy is
     therefore: outside O(|𝒳|/t²) exceptional x ≤ X, |ω_{≤√X}(N_x) − log log X| ≤ t√(1 + log log X) + O(1). Letting
     t → ∞ slowly gives density one. That is ≍ log log log p prime factors at polylogarithmic X, against the
     ≈ 2 log log p the model uses.
   * Pointwise, Λ(p, X) ≥ (1/8) log²X − O(log X) for every prime (indeed every odd integer) p > X, from the "outer
     layer" (divisors d ≤ x/2 of p + x; congruence data). At polylogarithmic X this is only O((log log p)²).
   * Beyond that the question is a pointwise short-interval divisor-type problem with no known approach (Assessment,
     §3.3).
3. **Per-line class hypotheses are model-false (Theorem C; PROVED in the HCHYP model 𝔐).**
   * The conjunction "(ii) every large p has a line with τ ≥ Kφ(x)" ∧ "(i) every such big line succeeds" has
     𝔐-probability 0, for every fixed K and every K = K(p) → ∞, at every window size.
   * Assessment: a model-compatible class statement must be a joint lottery over ≍ log p·log log p lines with small
     individual success probabilities. This is not a theorem about all arguments at actual primes.
4. **The conditioned lottery Lot(C) and two conditional theorems (PROVED implications; hypotheses OPEN).**
   * Lot_Λ(C): "Λ(p, X) ≥ C log p ⟹ HC(p) ≤ X", for all large p and X up to a cap. Lot_Γ(C) is the same with the
     genus mass Γ (§1). In 𝔐 they hold a.s. for C > 4, resp. C > 2 (Prop L).
   * **Thm S:** Anat(A, C) ∧ Lot(C) ⟹ S_A. In 𝔐, with those C, both conjuncts hold a.s. for A ≥ 2 log 2, and Anat
     fails i.o. for A < 2 log 2. The exponent lives in the anatomy conjunct.
   * **Thm D:** Lot_Λ(C) *alone* ⟹ HC(p) ≤ exp(√(8C log p) + O(1)) = p^{o(1)} for all large p. The anatomy at windows
     exp(O(√log p)) is supplied unconditionally by Theorem A2. This beats the open HC ≪ p^θ, but only conditionally on
     a pure class-layer hypothesis.
   * Byproduct (Prop M′, PROVED in 𝔐 only): the boundary case A = 2 log 2, left undecided in HCHYP Thm M, holds in 𝔐.
5. **Numerics (EVIDENCE; CERTIFIED controls).** About 1.7·10⁵ primes with all lines x ≤ 1024, plus 6.5·10⁶ primes with
   lines x ≤ 64, at heights 10⁹–4·10¹⁵.
   * *Per-line law.* For genus mass m ≥ ½, pooled over x ∈ [64, 1024), an endpoint line succeeds with probability within
     about four percentage points of 1 − e^{−m}, and a level line within about four points of 1 − e^{−m/2} (pairing
     d ↔ N/d), in these pooled bins (largest deviations 2.4 points for E and 3.9 points for L).
     This holds at every height. At small m both fall short of the law (factors 0.5–0.85).
   * *Joint failures.* Given the genus masses, the class failures at x ≤ 64 show no clear systematic excess over the
     two marginal lottery surrogates. Observed/predicted is 0.31–0.94 (cL = ½) and 0.67–1.71 (cL = 1) in the 10⁹
     scan, and 0.75–1.16 and 1.47–4.15 at 10¹². The counts are low (≤ 25 at 10¹²), and independence is not
     established.
   * *Where failures happen.* In the samples of consecutive primes p ≡ 1 (8) at 10¹¹–4·10¹⁵ every failure occurs while Γ = 0. Of the 145 listed
     hard primes with HC ≥ 20, 95 have Γ(p, 16) = 0. The one high-mass failure is p = 21841 (Γ = 1.02 log p at
     X = 60–63).
   * *Odd squares.* Λ is prime-like, while Γ = 0 on all 3.84·10⁶ lines (CERTIFIED).

**What it buys.** FRONTIER §7.2 can record a sufficient route with three named parts:
* (a) a pointwise anatomy statement for the window integers p + x, xp + 1. It is not ES-specific and is OPEN; its
  threshold 2 log 2 is PROVED on average;
* (b) the genus layer, where T1 lives;
* (c) a conditioned joint class lottery (OPEN, B2-type; model-true).
Per-line versions of (c) are model-false, and (c) alone would give p^{o(1)}.

## 1. Statements attacked; the three layers

Notation as in `Z53_HCHYP.md` §1.
* p ≡ 1 (8) is prime (for p ≡ 5 (8), HC(p) = 3). 𝒞 = {x ≥ 4 : 4 | x or x ≡ 7 (8)}.
* For x ∈ 𝒞 the two *lines* ι = (x, E), (x, L) have window integers N_ι = p + x and N_ι = xp + 1, both coprime to x.
* G_x = (ℤ/x)^×. Line ι *succeeds* iff N_ι has a divisor d ≡ −1 (mod x), and HC(p) = min{x : a line at x succeeds}
  (LOWERTAIL_ROUND2_FABLE Cor 1.1; Z53_UPPER Lemma 1.1).

**Target S_A (FRONTIER §7.2).** ∃ p₀ ∀ prime p > p₀, p ≡ 1 (8): HC(p) ≤ (log p)^A, with A > 2 log 2.

**Per-line quantities.** For a line ι at x, with N = N_ι:
* τ(N) (anatomy);
* the **genus count** g_ι := #{d | N : d ∈ −G_x²} (quadratic layer);
* the **class count** c_ι := #{d | N : d ≡ −1 (mod x)}; success iff c_ι ≥ 1.

Let r_x be the 2-rank of G_x, so G_x/G_x² ≅ (ℤ/2)^{r_x} and |G_x²| = φ(x)/2^{r_x}.

**Window masses.**
* Λ(p, X) := Σ_{ι : x ≤ X} min(1, τ(N_ι)/φ(x)) (anatomy mass);
* Γ(p, X) := Σ_{ι : x ≤ X} min(1, g_ι/|G_x²|) (genus mass);
* Λ_E, Γ_E denote the same sums over endpoint lines only.

**Lemma 1.1 (PROVED).** Let x ∈ 𝒞 and N ≥ 1 coprime to x.
(a) c ≥ 1 ⟹ g ≥ 1. So g = 0 (genus confinement) forces failure.
(b) If G_x has exponent 2 (equivalently x | 24, i.e. x ∈ {4, 8, 12, 24}), then G_x² = {1} and c = g: the line is
    *deterministic* given its genus data.
(c) Let v : G_x → G_x/G_x² be the projection, and W the span of v(ℓ) over the primes ℓ | N. If N is squarefree, then
    g = τ(N)/|W| when v(−1) ∈ W, and g = 0 otherwise. In particular g/|G_x²| ≥ τ(N)/φ(x) whenever g > 0.
(d) (T1) If N_ι is formed at n = m² with m odd and gcd(m, x) = 1, then g_ι = 0 for every line.

*Proof.*
* (a) A divisor ≡ −1 lies in −G_x².
* (b) Immediate. The exponent of (ℤ/x)^× is 2 iff x | 24.
* (c) The map {0,1}^{ω(N)} → G_x/G_x², ε ↦ Σ ε_i v(ℓ_i), is a group homomorphism with image W. Its fibres all have size
  2^{ω}/|W| = τ(N)/|W|. The divisors in −G_x² form the fibre over v(−1), which is empty unless v(−1) ∈ W. Then
  g/|G_x²| = τ 2^{r_x}/(|W| φ(x)) ≥ τ/φ(x), since |W| ≤ 2^{r_x}.
* (d) This is HCSHIFTS Lemma C(d): the odd real character χ_{−x} (Kronecker symbol, a character mod x) is +1 on every
  prime factor of N_ι, and χ_{−x}(−1) = −1. Every d | N_ι therefore has χ_{−x}(d) = 1, while every element of −G_x² has
  χ_{−x} = −1. ∎

There is no general pointwise ordering between the line masses min(1, τ/φ) and min(1, g/|G_x²|). For example x = 12,
N = 11 gives 1/2 and 1, while x = 12, N = 13 gives 1/2 and 0. By (c), on a squarefree, genus-live line (g > 0) the genus
mass is the larger. Γ = 0 at odd squares by (d); the same argument applies to the unit divisors when gcd(m, x) > 1. So
Lemma 1.1(d) is where primality enters: Γ is the T1-aware mass, Λ is class- and genus-blind.

**Lemma 1.2 (two more deterministic coordinates; PROVED).** Let p ≡ 1 (8) and x ∈ {7, 15}. Then 8 | N_ι for both lines,
G_x² ⊆ ⟨2⟩ and ord_x(2) ≤ 4. Hence c ≥ 1 ⟺ g ≥ 1, so these lines are deterministic given their genus data, like the
lines x | 24 of Lemma 1.1(b).
*Proof.*
* p + x ≡ 1 + 7 ≡ 0 and xp + 1 ≡ 7 + 1 ≡ 0 (mod 8).
* G_7² = {1, 2, 4} = ⟨2⟩, and G_15² = {1, 4} ⊂ ⟨2⟩ = {1, 2, 4, 8}.
* Let d | N lie in −G_x² and write d = 2^a d_o with d_o odd. Then the 2^j d_o, 0 ≤ j ≤ 3, all divide N and fill
  d_o⟨2⟩ ⊇ d·G_x² = −G_x² ∋ −1. ∎

**Statements attacked.**
* **(Q1)** The arithmetic origin of 2 log 2. Target form: Anat(A, C): Λ(p, (log p)^A) ≥ C log p for all large p.
* **(Q2)** The part of Anat provable at one p.
* **(Q3)** The weakest clean class hypothesis, and S_A conditional on it plus anatomy. Can it be per-line?
* **(Q4)** Numerics to 10¹³ and beyond, at hard primes (the HCSHIFTS list, which contains the 14 (★)-zero primes of
  §4 item 14 and 2521, 3361, 66529, 21841), with odd squares and near-squares as controls.

## 2. Why this is not already closed

* HCSHIFTS §3.2 and HCHYP Thm M derive 2 log 2 *inside a model*. Neither identifies an arithmetic statement with that
  threshold, and neither separates the anatomy layer from the class layer at one p.
* HCHYP's LT (§5.2 there) is a joint lower-tail hypothesis on the *model* mass 𝓜, which is a function of x only. It fuses
  anatomy and class into one far-tail assumption.
* HCHYP Cor M3/M4 block hypotheses that 𝔐 satisfies with positive probability (θ < 2 log 2), and block-robust ones. They
  do not address:
  * (i) the "anatomy + per-line class" decomposition;
  * (ii) which part of the anatomy is provable at a single p;
  * (iii) a class hypothesis conditioned on the *actual* anatomy, which is pointwise and numerically falsifiable.
* `git grep` finds no Turán–Kubilius-over-the-window statement and no conditioned-lottery hypothesis in the repository.
  (Remark 3.1 of HCSHIFTS counts small divisors in the window; Theorem A below extends that count.)

## 3. Theorem A — what is provable at one p

Throughout this section p is a prime, 8 < X < p, and 𝒳 := 𝒞 ∩ [4, X]. Note |𝒳| = 3X/8 + O(1).

### 3.1 Exact local layer and Turán–Kubilius over the window (PROVED)

**Lemma A1.** Let q ≥ 1 be any odd integer coprime to p, and F ∈ {E, L}. Then
  #{x ∈ 𝒳 : q | N_x^F} = |𝒳|/q + O(1), with |O(1)| ≤ 4.

*Proof.*
* q | p + x ⟺ x ≡ −p (mod q).
* q | xp + 1 ⟺ x ≡ −p̄ (mod q), where p̄ is the inverse of p mod q.
* 𝒞 is the union of the classes 0, 4, 7 mod 8 (minus x < 4), and (q, 8) = 1. By the Chinese remainder theorem each
  class mod 8 meets the condition in exactly one class mod 8q. Each class mod 8q has X/(8q) + O(1) members in [1, X]. ∎

**Theorem A1 (Turán–Kubilius over the window; PROVED).** Let 3 ≤ z ≤ X^{1/2} and
ω_z(n) := #{ℓ ≤ z odd prime, ℓ ≠ p : ℓ | n}. Put μ_z := Σ_{3≤ℓ≤z} 1/ℓ = log log z + O(1). Then
  Σ_{x∈𝒳} (ω_z(N_x^F) − μ_z)² ≪ |𝒳| (1 + log log z),
so #{x ∈ 𝒳 : |ω_z(N_x^F) − μ_z| > t√(1 + log log z)} ≪ |𝒳|/t². (The same proof works for strongly additive sums
F(n) = Σ_{ℓ≤z odd prime, ℓ∣n} f(ℓ), centred at Σ_{ℓ≤z} f(ℓ)/ℓ, with variance ≪ |𝒳| Σ_{ℓ≤z}|f(ℓ)|²/ℓ + (Σ_{ℓ≤z}|f(ℓ)|)². It
does not extend to general additive functions with prime-power values, which this right-hand side does not see.)

*Proof.* Expand ω_z = Σ_ℓ 1[ℓ | N] and use Lemma A1 with q = ℓ and q = ℓℓ′.
* Σ_x ω_z = |𝒳| μ_z + O(π(z)).
* Σ_x ω_z² = Σ_{ℓ≠ℓ′} (|𝒳|/(ℓℓ′) + O(1)) + Σ_ℓ (|𝒳|/ℓ + O(1)) ≤ |𝒳|(μ_z² + μ_z) + O(π(z)²).
* Hence Σ_x (ω_z − μ_z)² = Σ ω_z² − 2μ_z Σ ω_z + |𝒳| μ_z² ≤ |𝒳| μ_z + O(π(z)² + μ_z π(z)).
* Finally π(z)² ≤ z² ≤ X ≪ |𝒳|. ∎

*Reading.* At a single p the window variable x is a free variable, and its local statistics are exact. But only primes
≤ X^{1/2} are seen. With X = (log p)^A, log log z = log log log p + O_A(1), whereas the anatomy relevant to S_A
(ω ≈ 2 log log p, HCSHIFTS §3.2) lives on primes up to p.

### 3.2 The outer layer gives (log X)² pointwise (PROVED)

**Theorem A2.** For every prime p (indeed every odd integer p) and 6 ≤ X < p,
  Λ_E(p, X) ≥ ½ Σ_{d odd ≤ X/6} (1/d) log(X/(6d)) = (1/8) log²X − O(log X).

*Proof.*
* For x ∈ 𝒞 with 4 | x, let a_x := #{d odd : d | p + x, d ≤ x/2}. Then τ(p + x) ≥ a_x, and φ(x) ≤ x/2 since x is even,
  so τ/φ ≥ 2a_x/x.
* Also a_x ≤ x/4 + 1 ≤ x/2, so min(1, τ/φ(x)) ≥ 2a_x/x.
* Hence Λ_E(p, X) ≥ 2 Σ_{d odd} Σ_{x : 4|x, 2d ≤ x ≤ X, x ≡ −p (d)} 1/x.
* For odd d ≤ X/6 the inner x run over one class mod 4d, starting at some x₀ < 6d. For decreasing f, an arithmetic
  progression of step h starting at x₀ satisfies Σ f(x₀ + jh) ≥ h^{−1} ∫_{x₀}^{X} f. So the inner sum is
  ≥ (1/(4d)) log(X/(6d)).
* Finally Σ_{d odd ≤ u} 1/d = ½ log u + O(1), and partial summation gives
  Σ_{d odd ≤ Y} (1/d) log(Y/d) = ¼ log²Y + O(log Y). ∎

*Remarks.*
* Primality is not used. The A2 bound holds at odd squares, where every line is genus-confined (Lemma 1.1(d)). The
  anatomy layer is class-blind and cannot by itself see T1. At X = (log p)^A the bound is only
  (A²/8)(log log p)² = o(log p), so it does **not** give Anat(A, C) at squares or anywhere else.
* The certificates the outer layer can supply are congruence data. A small divisor d ≤ x/2 is never ≡ −1 (mod x). Its
  cofactor (p + x)/d is ≡ −1 iff d ≡ −p (mod x), i.e. iff p ≡ −(x + d) (mod xd). This is the word (t, x, d) with two
  small coordinates, a forest edge {x, d}. Such certificates can all be absent up to exp((log p)^κ) at infinitely many
  primes (H4_NOT_POLYLOG Thm 1: κ < 1/12 unconditionally, κ < 1/6 relative to Gallagher's (G) or GRH). At that window
  the bound of Theorem A2 is only (1/8)(log p)^{2κ}.

### 3.3 Beyond the outer layer: a pointwise short-interval divisor problem (Assessment, with checked literature)

The remaining mass comes from divisors d ∈ (X, √p] of p + x, i.e. from lattice points (m, d) with p < md ≤ p + X.
* The best pointwise asymptotic Σ_{p<n≤p+X} τ(n) ~ X log p follows, by subtracting two values of Δ, for
  X ≥ p^{θ*+ε}, with θ* = 0.31448… (Li–Yang, arXiv:2308.14859, Thm 1.2; this improves Huxley's 131/416). That is a
  sufficient range for an unweighted asymptotic. It is not a theorem that every lower-bound or weighted/truncated
  approach needs it. Λ also involves the level integers xp + 1, the weights 1/φ(x) and the truncation. Do not cite
  Bourgain–Watt 517/1648: its arXiv comment withdraws Thms 1–3.
* Jutila's mean square, ∫_T^{2T}(Δ(x+U) − Δ(x))² dx ≪ TU log³(√T/U) + T log⁴T for 1 ≤ U ≤ T^{1/2}/2 (as quoted in
  Ivić–Zhai, arXiv:1209.0872, Thm B and (2.3)), gives Σ_{x<n≤x+U} τ(n) ~ U log x for almost all starting points
  x ∈ [T, 2T] (real or integer) once U/log T → ∞. Passing to almost all *primes* needs more:
  Chebyshev's inequality gives an exceptional measure ≪ T(log T/U + log²T/U²), which is o(T/log T) only when
  U/(log T)² → ∞ (and then only with a suitable tolerance). Either way this is an average (B6), not a single p.
* For polylogarithmic X the literature search (`data/z54/hcwin/lit_notes.md` Q3) found nothing pointwise beyond the
  trivial bounds Σ τ ≫ X log X and max ω ≳ log X/log log X (CRT).
* Even "every [N, N + (log N)^A] contains an n with ω(n) ≥ c log log N", or with τ(n) ≥ (log N)^c, appears to be open.
  Tao (MathOverflow 275191) notes that no technique rules out conspiracies of medium-sized primes in such intervals.

*Assessment.* Pointwise Anat(A, C) at polylogarithmic X is beyond current methods. It is a class-blind, ES-independent
statement about divisors of integers in a polylogarithmic window at a prime. It is part of a *sufficient* route to S_A
(Theorem S), not a proved necessary condition: S_A needs only one successful line, and no implication S_A ⟹ Anat is
claimed. Sieve methods meet the parity obstruction here. Consider a window in which every integer free of prime
factors ≤ √X is prime. Upper-bound sieve information cannot exclude it: the Selberg upper bound for those integers and the
Brun–Titchmarsh bound for the primes of the window are the same (2 + o(1))X/log X. In such a window the √X-rough integers
all have τ = 2.

## 4. Theorem B — the anatomy threshold 2 log 2, on average over primes

Write π*(T) := #{p ∈ (T, 2T] prime, p ≡ 1 (8)}, g(κ) := κ log 2 − Q(κ), and Q(κ) := κ log κ − κ + 1. On [1, 2], g
increases from log 2 to 1, since g′(κ) = log 2 − log κ.

**Theorem B (PROVED relative to (H) and (BV) below).** Fix θ > 0, put κ = θ/log 2 and X = (log T)^θ.
(i) If 1 < κ < 2, then Σ_{T<p≤2T, p≡1(8)} Λ(p, X) ≤ π*(T)·(log T)^{g(κ)+o(1)}.
(ii) If κ > 2, then Σ_{T<p≤2T, p≡1(8)} Λ(p, X) ≥ c(θ)·π*(T)·log T·log log T for T ≥ T₀(θ), with c(θ) > 0.

*Inputs.*
* (H) Henriot, *Math. Proc. Camb. Phil. Soc.* 152 (2012), arXiv:1102.1643, Thm 7 (the prime-variable Nair–Tenenbaum
  bound). For f(n) = τ(n)^s with fixed s ∈ [0, 2] (Shiu class, f(ℓ^k) ≤ 2^{sk}), uniformly for 1 ≤ a ≤ (log T)^C:
    Σ_{T<p≤2T} τ(p + a)^s ≪_{s,C} (a/φ(a))·(T/log T)(log T)^{2^s−1},
    Σ_{T<p≤2T} τ(ap + 1)^s ≪_{s,C} (T/log T)(log T)^{2^s−1}.
  Henriot's theorem applies with Q(X) = X + a (Q(0) = a, giving the factor a/φ(a)) and with Q(X) = aX + 1 (Q(0) = 1).
  Both are linear and ‖Q‖ ≤ a + 1 ≤ T^δ. Henriot's 2014 erratum replaces the bad-prime quantity D* by a*D* (a* the
  leading coefficient); for aX + 1 the primes ℓ | a are not roots, so the bound is unaffected (checked in review). The constant depends only on the degree, α, δ and the Shiu
  parameters. This specialisation is ours, not stated in the source. Pollack (*Glasgow Math. J.* 62 (2020), Thm 1.1)
  gives the first bound independently. (Statements VERIFIED from the sources; `lit_notes.md` Q1.)
* (BV) Bombieri–Vinogradov, used for the Titchmarsh-type lower bound below. It is uniform in the residue class, hence
  in a.

*Proof of (i).*
* For u ≥ 0 and s ∈ [0, 1], min(1, u) ≤ u^s. Hence
    Σ_p Λ(p, X) ≤ Σ_{x∈𝒞, x≤X} φ(x)^{−s} Σ_p [τ(p+x)^s + τ(xp+1)^s]
               ≪ (T/log T)(log T)^{2^s−1} Σ_{x≤X} (x/φ(x)) φ(x)^{−s}.
* Since x/φ(x) ≪ log log x, the last sum is ≪ (log log X)² X^{1−s}/(1 − s).
* Take s = s* := log₂ κ ∈ (0, 1). The exponent of log T is then
    2^{s*} − 1 + θ(1 − s*) = κ − 1 + κ log 2 − κ log κ = g(κ),
  using θ s* = κ log 2 · log κ/log 2 = κ log κ.
* π*(T) ≍ T/log T, and the (log log)² factor is (log T)^{o(1)}. ∎

*Proof of (ii).*
* Fix θ₀ with 2 log 2 < θ₀ < θ, and put Y = (log T)^{θ₀}. Restrict to E-lines with Y < x ≤ X, 4 | x. Then N = p + x
  is odd.
* For η > 0, τ·1[τ ≤ φ] ≥ τ − τ^{1+η}φ^{−η}, so
    min(1, τ/φ(x)) ≥ φ(x)^{−1}[τ − τ^{1+η}φ(x)^{−η}].
* *Lower bound for Στ (BV).* Put D := T^{1/2}(log T)^{−B} < √(p + x). Each divisor d ≤ D of n = p + x pairs with a
  distinct divisor n/d > D, so τ(n) ≥ 2#{d | n : d ≤ D}. With BV for the moduli 8d ≤ 8D:
    Σ_{p∈(T,2T], p≡1(8)} τ(p+x) ≥ 2 Σ_{d≤D odd, (d,x)=1} #{p ∈ (T,2T] : p ≡ 1 (8), p ≡ −x (d)}
                               ≥ 2π*(T) Σ_{d≤D odd, (d,x)=1} 1/φ(d) − O(T/log²T)
                               ≥ c₁ (φ(x)/x) π*(T) log T,
  with c₁ > 0 absolute, uniformly in x ≤ (log T)^C. Here Σ_{d≤D, (d,2x)=1} 1/d ≥ (φ(2x)/(2x))(log D − O(log log x)).
* *Upper bound for Στ^{1+η} (H).*
    Σ_p τ(p+x)^{1+η} ≤ C_η (x/φ(x)) π*(T) (log T)^{2^{1+η}−1}.
* Hence the bracket summed over p is
    ≥ π*(T)(φ(x)/x) log T·[c₁ − C_η (x/φ(x))² φ(x)^{−η} (log T)^{2^{1+η}−2}].
* For x > Y we have φ(x) ≥ x/(C log log x), so the subtracted term is ≤ (log T)^{2(2^η−1) − ηθ₀ + o(1)}.
  Now 2(2^η − 1) − ηθ₀ = η(2 log 2 − θ₀) + O(η²) < 0 for small η > 0. So the square bracket is ≥ c₁/2 for T ≥ T₀,
  and the whole expression is ≥ (c₁/2)·π*(T)(φ(x)/x) log T.
* Dividing by φ(x) leaves (c₁/2) π*(T) log T/x. Summing over x ∈ (Y, X] with 4 | x gives ≥ (c₁/8) π*(T) log T·(θ − θ₀)
  log log T·(1 − o(1)). ∎

*Range remarks.* For 0 < θ ≤ log 2 the trivial bound Λ ≤ 2#𝒳 ≪ (log T)^θ = o(log T) replaces (i). (i) is an upper
bound only. Neither part decides the arithmetic boundary θ = 2 log 2: "the threshold is 2 log 2" means that 2 log 2
separates the two proved regimes.

*Reading.*
* On average, the window's truncated divisor mass passes from o(log p) to ≫ log p log log p as θ crosses 2 log 2.
  Below, the upper bound (log p)^{g(κ)} has the same exponent as the model's per-block cost (HCSHIFTS §3.2, item 4).
* The mechanism is Rankin's: E_p τ(p + x)^s ≪ (log p)^{2^s − 1}. The minimiser s* = log₂ κ is the tilt at which τ's
  mass sits at ω ≈ κ log log p.
* So 2 log 2 is an arithmetic property of τ on shifted primes, not an artefact of 𝔐. Part (i) is an upper bound only:
  no lower bound of the form (log T)^{g(κ)−o(1)} is claimed (it would need lower-bound large deviations for ω(p + a),
  which Ford, *Lith. Math. J.* 61 (2021), reports as unknown for every k).
* Thm B is an average over p (screen 5). It calibrates; it does not reach one p.

## 5. The model: per-line class is model-false, the conditioned lottery is model-true

𝔐 is HCHYP §3.1. Write λ = log log p. For each line, k_ι ~ Poisson(λ) and g_{ι,i} are i.i.d. uniform in G_x. Everything
is independent across lines and primes. Line ι succeeds iff −1 ∈ Σ_ι (subproducts). In 𝔐, τ(N_ι) ↔ 2^{k_ι}.

**Theorem C (PROVED in 𝔐).** Call a line *K-big* if 2^{k_ι} ≥ K φ(x).
(a) Let K = K(p) ≥ 1 with K(p) → ∞. Then 𝔐-a.s., for infinitely many p *no* line ι (any x ∈ 𝒞) is
    K(p)-big.
(b) Let K ≥ 1 and y ≥ 1 be fixed. Then 𝔐-a.s., for infinitely many p some K-big line with φ(x) ≥ y fails.
Consequently, for every fixed K and every K(p) as in (a), the conjunction
  [for all large p, some line is K-big] ∧ [for all large p, every K-big line succeeds]
has 𝔐-probability 0, whatever the window.

*Proof.* (a)
* Let N(t) := #{x ∈ 𝒞 : φ(x) ≤ t}. Then N(t) ≤ c₂t with c₂ absolute. For n ∈ (y, 2y], φ(n) ≤ t forces n/φ(n) ≥ y/t, and
  Σ_{n≤2y}(n/φ(n))² ≤ C·2y (Σ_{n≤u} n/φ(n) ≪ u and its square analogue are standard). So
  #{n ∈ (y, 2y] : φ(n) ≤ t} ≤ (t/y)²·2Cy. Summing over dyadic y ≥ t gives O(t), and n ≤ t gives ≤ t.
* Hence Σ_ι P(ι is K-big) = 2E[N(2^k/K)] ≤ 2c₂ e^λ/K = 2c₂ log p/K, using E 2^k = e^λ for k ~ Poi(λ).
* Split the lines. Where q_ι := P(big) ≤ ½, use 1 − q ≥ e^{−2q}; these contribute ≥ exp(−4c₂ log p/K).
* Where q_ι > ½, the median of 2^k must be ≥ Kφ(x), so φ(x) ≤ 2^{λ+O(1)} = O((log p)^{log 2}) and there are
  O((log p)^{0.7}) such lines. For each, 1 − q_ι ≥ P(k = 0) = 1/log p.
* By independence,
    P(no big line at p) ≥ exp(−4c₂ log p/K(p) − O((log p)^{0.7} log log p)) = p^{−o(1)}.
* Σ_p p^{−o(1)} = ∞ over primes p ≡ 1 (8), and the events are independent across p. The second Borel–Cantelli lemma
  gives (a).
(b)
* Fix a prime q ≡ 3 (mod 4) with 2(q − 1) ≥ y and take x = 4q ∈ 𝒞, so φ(x) = 2(q − 1). Then H := ker χ_{−4} is an
  index-2 subgroup of G_x with −1 ∉ H.
* Put k₀ := ⌈log₂(Kφ(x))⌉. If k_ι = k₀ and all g_{ι,i} ∈ H, the line is K-big and fails, since all subproducts lie in H.
* So P(K-big and fails) ≥ e^{−λ}λ^{k₀}/k₀! · 2^{−k₀} ≫_{K,q} (log log p)^{k₀}/log p.
* Σ_p (log log p)^{k₀}/log p = ∞, and the second Borel–Cantelli lemma gives (b). ∎

*Reading.* A per-line "class from anatomy" hypothesis must either fix K, and then single lines fail infinitely often, or
let K grow, and then big lines are absent infinitely often. The second alternative holds at *every* window, even
X = ∞: Σ_ι P(big) ≍ log p/K is too small to be summably sure. In 𝔐 the bulk of the success comes from lines with
τ/φ(x) ≪ 1 (cf. HCSHIFTS §3.2: at the critical scale the share of hits with τ ≳ φ decays like λ^{−1/2}).

*Scope.* Theorem C is a statement about 𝔐. It shows that this anatomy-plus-universal-per-line conjunction is
incompatible with the model, so a model-compatible class hypothesis must avoid that formulation. It is not a theorem
about actual primes: an arithmetic mechanism may violate 𝔐 (cf. HCHYP Cor M3's scope). It also does not classify other
non-lottery arguments, such as adaptive choices of K or restricted families of candidate lines. That the class layer
should be stated as a joint lottery is an Assessment.

**Proposition M′ (PROVED in 𝔐; decides HCHYP's boundary case in 𝔐).** 𝔐-a.s., HC(p) ≤ (log p)^{2 log 2} for all large p.

*Proof.* Put X := (log p)^{2 log 2}, so log₂ X = 2λ.
* By HCHYP Lemma M1, P(line succeeds | k) ≥ ½ min(1, (2^k − 1)/φ(x)) ≥ ½ min(1, 2^{k−1}/x) for k ≥ 1.
* For 2^k ≤ x, the minimum is 2^{k−1}/x. Also Σ_{x∈𝒞, U<x≤X} 1/x ≥ (3/8) log(X/U) − 3 for U ≥ 8.
* Using E-lines only, and only k ≥ 3 (so that U = 2^k ≥ 8),
    S := Σ_{x∈𝒞, x≤X} P(E-line at x succeeds) ≥ ½ E[1(k≥3) 2^{k−1} ((3/8) log 2·(2λ − k) − 3)_+].
* With E[2^k F(k)] = e^λ E F(V), V ~ Poi(2λ), this is ≥ ¼ e^λ E[1(V≥3) ((3/8) log 2·(2λ − V) − 3)_+].
* By the Poisson CLT, P(3 ≤ V ≤ 2λ − √(2λ)) → Φ(−1) = 0.1587 > 0.15. On that event the bracket is
  ≥ (3/8) log 2·√(2λ) − 3. So S ≥ c·log p·√(log log p) for large p (c = 0.01 is eventually valid).
* Lines are independent, so P(HC(p) > X) ≤ exp(−S) ≤ p^{−2} eventually, which is summable over p. The first
  Borel–Cantelli lemma gives the claim; no independence across primes is needed. ∎

*Remark.* HCHYP Thm M(b) used only the lines with φ(x) ≥ (log p)^{2 log 2 + δ}, which is why its boundary was left open.
The sum above is carried by the partially truncated regime 2λ − V ≍ √λ. This matches HCSHIFTS §3.2 item 6 (in its own
miss-probability model). The model statement says nothing about actual primes.

**The conditioned lottery.** For C > 0 and a window cap X_max(p) ≤ exp((log p)^{3/4}), define:
* **Lot_Λ(C):** ∃p₀ ∀p > p₀ (prime, ≡ 1 (8)) ∀X ≤ X_max(p): Λ(p, X) ≥ C log p ⟹ HC(p) ≤ X.
* **Lot_Γ(C):** the same with Γ in place of Λ.
* **Anat_Λ(A, C):** Λ(p, (log p)^A) ≥ C log p for all large p. **Anat_Γ(A, C):** the same with Γ.

**Proposition L (PROVED in 𝔐).**
(a) Lot_Γ(C) holds 𝔐-a.s. for every C > 2, and Lot_Λ(C) for every C > 4.
(b) For A ≥ 2 log 2 and every C, Anat_Λ(A, C) and Anat_Γ(A, C) hold 𝔐-a.s. For A < 2 log 2 and every C > 0, both fail
    𝔐-a.s. (at infinitely many p; indeed P(Λ(p,(log p)^A) ≥ C log p) → 0).

*Proof.* (a) Condition on all line data at p: the k_ι, and for Γ also the genus images v(g_{ι,i}).
* Then X*(p) := min{X ≤ X_max : Γ(p, X) ≥ C log p} is determined. If no X ≤ X_max reaches the threshold, the
  implication holds vacuously at p. Given the data, the lines succeed independently.
* *Γ version.* Write g_{ι,i} = c_{ι,i}h_{ι,i}, with c fixed coset representatives and h_{ι,i} i.i.d. uniform in G_x².
  For nonempty I in the genus fibre of −1, g_I is uniform on −G_x². For distinct such I, J the events {g_I = −1},
  {g_J = −1} are independent: pick j ∈ J∖I (or I∖J) and use the uniformity of h_j.
* Lemma M1's Paley–Zygmund argument therefore gives P(success | data) ≥ ½ min(1, g_ι/|G_x²|). The empty product is not
  in the fibre, since −1 ∉ G_x² for x ∈ 𝒞 (4 | x, or x has a prime factor ≡ 3 (4)).
* So P(all lines ≤ X* fail | data) ≤ exp(−½Γ(p, X*)) ≤ p^{−C/2}, which is summable for C > 2.
* *Λ version.* Use M1 directly: ½ min(1, (2^k−1)/φ) ≥ ¼ min(1, 2^k/φ) for k ≥ 1. Lines with k = 0 contribute
  ≤ 2Σ_{x≤X} 1/φ(x) = O(log X) = o(log p) to Λ (two line types; X ≤ exp((log p)^{3/4})). This gives p^{−C/4+o(1)},
  summable for C > 4. No union bound over X is needed.
(b) *Upper range.*
* By Lemma 1.1(c) (in 𝔐 the "primes" are distinct), Γ_ι ≥ min(1, 2^{k_ι}/φ(x))·1[v(−1) ∈ W_ι].
* Given k, P(v(−1) ∉ W_ι) ≤ 2^{r_x}·2^{−k}: a nonzero character of G/G² is trivial on k uniform elements with
  probability 2^{−k}.
* So EΓ ≥ EΛ − Σ_{x≤X} 2^{r_x+1}/φ(x). Here 2^{r_x} ≤ 4·2^{ω(x)}, and the Euler product gives
  Σ_{x≤X} 2^{ω(x)}/φ(x) = O((log X)²). The loss is O((log log p)²) at polylogarithmic X.
* The proof of M′ (the same sum, with min(1, 2^k/φ) ≥ min(1, 2^{k−1}/x)) gives EΛ ≥ c log p √(log log p) at
  A = 2 log 2, and Λ is monotone in A.
* Different lines are independent (also after the genus-failure events), so Λ and Γ are sums of independent [0, 1]
  variables. The Chernoff bound P(Γ ≤ EΓ/2) ≤ exp(−EΓ/8), and likewise for Λ, is summable.
*Lower range.*
* For 0 < A ≤ log 2: EΛ ≤ 2#𝒳 ≪ (log p)^A = o(log p).
* For A = κ log 2 with 1 < κ < 2, the Rankin computation of Theorem B(i) inside 𝔐 (E 2^{sk} = (log p)^{2^s−1},
  s = log₂ κ ∈ (0, 1)) gives EΛ ≤ (log p)^{g(κ)+o(1)} = o(log p).
* For Γ: in 𝔐, E[g_ι | k] = (2^k − 1)/2^{r_x}, since each nonempty subset has a uniform genus image. By Jensen for the
  concave min(1, ·), E[min(1, g_ι/|G_x²|) | k] ≤ min(1, (2^k − 1)/φ(x)) ≤ min(1, 2^k/φ(x)). Hence EΓ ≤ EΛ.
* Markov's inequality gives P(Λ ≥ C log p) → 0 and P(Γ ≥ C log p) → 0. The second Borel–Cantelli lemma (independence
  across p) gives failure of both at infinitely many p. ∎

## 6. Conditional theorems

**Theorem S (PROVED implication).** Anat_Γ(A, C) ∧ Lot_Γ(C) ⟹ S_A, and Anat_Λ(A, C) ∧ Lot_Λ(C) ⟹ S_A (window cap
X_max ≥ (log p)^A).
*Proof.* Take X = (log p)^A in Lot. ∎

In 𝔐, with C > 2 (Γ form) or C > 4 (Λ form), both conjuncts are almost sure when A ≥ 2 log 2, and the anatomy conjunct
fails infinitely often when A < 2 log 2 (Prop L). These are sufficient constants, not optimal ones. The exponent lives
in the anatomy conjunct, which is class-blind (Λ) or genus-level (Γ). The class conjunct Lot is exponent-free. Theorem S
is a sufficient route only; S_A does not imply Anat.

**Theorem D (CONDITIONAL on Lot_Λ(C) with X_max(p) = exp(3√(C log p))).** Every sufficiently large prime p ≡ 1 (8)
satisfies
  HC(p) ≤ exp(√(8C log p) + O(1)) = p^{o(1)}.
*Proof.* Λ ≥ Λ_E ≥ (1/8) log²X − c₀ log X by Theorem A2, which is ≥ C log p once log X ≥ √(8C log p) + 8c₀. That X is
≤ X_max, so Lot_Λ(C) gives HC(p) ≤ X. ∎

*Remarks.*
* Pointwise HC(p) ≪ p^θ is open for every fixed θ < 1 (FRONTIER §7.2). Theorem D obtains p^{o(1)} from a hypothesis that
  says nothing about anatomy: the anatomy at windows exp(O(√log p)) is supplied unconditionally by the outer layer.
  Reaching polylog windows additionally needs pointwise Anat (§3.3, open).
* With Γ instead of Λ there is no unconditional analogue of Theorem A2. Outer-layer genus mass needs non-residue small
  primes mod p, because for ℓ | N_ι reciprocity gives χ_{−x}(ℓ) = (ℓ/p) (Z53_UPPER L3.1 proof). Their count below
  X ≤ exp(O(√log p)) is a least-non-residue/character-sum problem, out of unconditional reach. Burgess gives a
  non-residue only below p^{1/(4√e)+ε} ≈ p^{0.1516}, and nontrivial short character sums need length p^{1/4+ε}.
* *Relation to the known kills (Assessment).* None of the scoped barriers in the repository supplies a refutation of
  eventual Lot(C):
  * Thm W bounds the certified window of fixed polynomial families (products and powers of prime-valued factors are
    allowed). Its displayed Prop W2 family (CONDITIONAL on UBH) has window integers of the form (forced small part)·prime,
    so their τ, and hence Λ, stay at the smooth-layer size.
  * Prop 3.3/W3 kill only small-prime (congruence) certificates; they do not bound HC (their instances have HC = 4).
  * H4 kills outer certificates only, at windows where the A2 bound is (1/8)(log p)^{2κ} with 2κ < 1/3. It does not
    bound the full Λ at those windows.
  * T1 gives Γ = 0 on every line. Alignment (HCHYP Lemma N) confines the aligned lines only away from the exceptional
    primes dividing 2·lead·Δ, and those can let a line escape. Example (from the internal review): f(m) = m² − 3, m = 10,
    p = 97, x = 15. The composed quadratic m² + 12 is aligned through χ₋₃, yet p + 15 = 112 has the divisor
    14 ≡ −1 (mod 15), via the prime 2.
  These are scoped barriers; that none of them produces high mass with an unlucky class draw is an observation, not a
  theorem excluding such constructions.
* Lot is ES-specific (it speaks about divisor classes of the ES lines). It is weaker than HCHYP's LT in one respect (it
  is conditioned on the actual mass, so anatomy deficits are not charged to it) and stronger in another (pointwise rather
  than a frequency bound). It is B2 restated for a joint family. It is *not* a mechanism.

## 7. Numerics (EVIDENCE unless marked CERTIFIED)

Program `scripts/z54_hcwin_lines.c` (C; trial division + Pollard–Brent + deterministic Miller–Rabin; explicit divisor
enumeration). For every line with x ∈ 𝒞, x ≤ 1024 (and x < n), it computes:
* τ(N) of the full N, used in Λ;
* the genus count g (DP over G_x/G_x² ≅ (ℤ/2)^{r_x}), the class count c and the outer data, all on the part of N
  coprime to x (identical at primes p > x);
* per prime, the masses Λ, Γ and S (defined in §7.4) over all lines with x < HC(p). These are the largest masses at
  which p still fails, *over every window*, not only the dyadic grid.
HC values at 193, 409, 577, 2521, 3361, 5569, 9601, 21841, 66529, 83449 and 8813281 reproduce Fable's 7, 4, 4, 15, 7, 7,
7, 64, 8, 39, 8 (CERTIFIED; independently re-checked in review).

**7.1 Controls.**
* *Odd squares* m², m odd from 100 001 (5 000 values): all 3 840 000 lines (x ≤ 1024) are genus-confined, Γ = 0, and
  there are 0 successes (CERTIFIED; Lemma 1.1(d), with the unit-divisor remark after Lemma 1.1).
* At the same squares the mean Λ(·, 1024)/log n is 5.20, against 4.53–5.85 at primes. **The anatomy layer does not see
  T1; the genus layer does.**

**7.2 Window masses** (means over the sample of Λ/log p and Γ/log p, at X = 64 and X = 1024):

| sample | N | P(HC>8) | P(HC>16) | Λ (64) | Γ (64) | Λ (1024) | Γ (1024) | min Γ (1024) |
|---|---|---|---|---|---|---|---|---|
| primes from 10⁹ | 50 000 | 1.6e−3 | 1.0e−4 | 1.69 | 1.23 | 5.85 | 4.56 | 2.52 |
| primes from 10¹¹ | 50 000 | 9.8e−4 | 4.0e−5 | 1.44 | 1.08 | 5.34 | 4.31 | 2.46 |
| primes from 10¹³ | 50 000 | 6.4e−4 | 2.0e−5 | 1.25 | 0.96 | 4.95 | 4.08 | 2.44 |
| primes from 4·10¹⁵ | 20 000 | 4.0e−4 | 5.0e−5 | 1.07 | 0.84 | 4.53 | 3.83 | 2.62 |
| non-square n ≡ 1 (8) from 10¹¹ | 20 000 | 2.6e−3 | 5.0e−5 | 1.40 | 0.99 | 5.07 | 3.70 | 1.62 |
| primes m²+24, m ≥ 10⁵ | 5 000 | 2.0e−3 | 8.0e−4 | 1.48 | 0.94 | 5.42 | 3.98 | 2.62 |
| primes m²+120, m ≥ 10⁵ | 5 000 | 2.5e−2 | 1.6e−3 | 1.50 | 0.85 | 5.45 | 3.76 | 2.38 |
| odd squares | 5 000 | 1 | 1 | 1.49 | 0 | 5.20 | 0 | 0 |
| hard primes (HCSHIFTS list)* | 166 | 0.91 | 0.87 | 1.73 | 0.68 | 5.88 | 3.31 | 2.55 |

\*For the two listed primes below 1024 (409 and 577) the "1024" columns stop at x < p.

* Genus-confined lines are common at primes: 47 % (10⁹), 41 % (10¹³) and 39 % (4·10¹⁵) of all lines x ≤ 1024, and 48 %
  at m² + 24.
* Ratio of mean Γ to mean Λ at X = 64:
  * 0.73–0.78 at the consecutive-prime samples (all four heights);
  * 0.63 at m² + 24 and 0.56 at m² + 120;
  * 0.40 at the hard primes.
  Near-squares and hard primes keep their Λ but lose Γ.

**7.3 Per-line law: given the genus mass, a line is close to a lottery.** The `.lines` tables store, per bin of
m = g/|G_x²| (bins of width √2), the count, the successes, and the bin sums of 1 − e^{−m} and 1 − e^{−m/2} over the
actual lines (`z54_hcwin_perline.py`). Pooled over x ∈ [64, 1024), observed rate against the bin-averaged prediction:

| m-bin (lower edge) | E: 10⁹ | E: 10¹³ | E: 4·10¹⁵ | pred. 1 − e^{−m} | L: 10⁹ | L: 10¹³ | L: 4·10¹⁵ | pred. 1 − e^{−m/2} |
|---|---|---|---|---|---|---|---|---|
| 2^{−5} | 0.027 | 0.029 | 0.029 | 0.037 | 0.008 | 0.009 | 0.010 | 0.019 |
| 2^{−3} | 0.116 | 0.121 | 0.123 | 0.136–0.137 | 0.046 | 0.051 | 0.053 | 0.071 |
| 2^{−1} | 0.434 | 0.439 | 0.438 | 0.436–0.439 | 0.223 | 0.231 | 0.233 | 0.252–0.253 |
| 1 | 0.700 | 0.695 | 0.697 | 0.677–0.681 | 0.431 | 0.435 | 0.439 | 0.435–0.437 |
| 2 | 0.916 | 0.904 | 0.898 | 0.893–0.895 | 0.709 | 0.702 | 0.700 | 0.677–0.680 |
| 4 | 0.991 | 0.984 | 0.979 | 0.988 | 0.925 | 0.914 | 0.911 | 0.894–0.895 |

(Each cell has between 2 500 and 1.4·10⁶ lines.)
* For m ≥ ½ the observed rate is within about four percentage points of the law in these pooled bins, at every height,
  for both line types. The largest deviations over all pooled bins with m ≥ ½ are 2.4 points (E) and 3.9 points (L, at
  10⁹, m-bin 2^{1.5}, 13 921 lines; that bin is not displayed in the table).
* For small m the observed rate is systematically *below* the law: by a factor of about 0.75–0.85 (E) and 0.5–0.75 (L)
  at m ≈ 2^{−5}–2^{−3}.
* Individual dyadic blocks scatter more (e.g. 0.947 on 432 lines at 10⁹, E, x ∈ [256, 512), m-bin 2). At small x
  (x < 64) the law also fails in both directions, because |G_x²| is small and the lottery is coarse. The law is a pooled
  approximate shape, not a calibrated conditional probability.
* Level lines follow the half-rate law because N ≡ 1 (mod x): certificates come in pairs d ↔ N/d.
* Genus-confined lines (m = 0) never succeed (PROVED, Lemma 1.1(a)).

**7.4 Joint failure given the masses (the Lot falsifier).** Mode `scan` (`z54_hcwin_joint.py`) covers all primes
p ≡ 1 (8) from 10⁹ (4·10⁶ primes) and from 10¹² (2.5·10⁶ primes), with lines x ≤ 64.
* Lines with x | 24 (Lemma 1.1(b)) and x ∈ {7, 15} (Lemma 1.2) are deterministic: a positive genus count forces success.
* On the primes where no deterministic line succeeds, the independent-lottery surrogate is P(HC > X | data) ≈ exp(−S),
  with S := Σ_E m + cL·Σ_L m over the lottery lines x ≤ X. Here cL = ½ (the large-x level law of §7.3) or cL = 1.

| 10⁹, X | 8 | 12 | 16 | 20 | 24 | 28 | 32 | 40 |
|---|---|---|---|---|---|---|---|---|
| observed HC > X | 6558 | 2307 | 339 | 123 | 17 | 9 | 1 | 0 |
| of which genus-dead (S = 0) | 6558 | 2307 | 206 | 49 | 8 | 2 | 0 | 0 |
| class failures: obs / pred (cL = ½) | 0/0 | 0/0 | 133/156 | 74/78 | 9/14 | 7/12 | 1/3.3 | 0/0.6 |
| class failures: obs / pred (cL = 1) | — | — | 133/101 | 74/43 | 9/7.4 | 7/6.2 | 1/1.5 | 0/0.1 |
| largest S at a class failure (cL = ½) | — | — | 4.0 | 4.0 | 3.5 | 3.8 | 4.8 | — |

| 10¹², X | 8 | 12 | 16 | 20 | 24 | 28 |
|---|---|---|---|---|---|---|
| observed HC > X | 1804 | 535 | 58 | 14 | 1 | 0 |
| of which genus-dead | 1804 | 535 | 33 | 7 | 0 | 0 |
| class failures: obs / pred (cL = ½) | 0/0 | 0/0 | 25/27 | 7/9.3 | 1/0.9 | 0/0.4 |
| class failures: obs / pred (cL = 1) | — | — | 25/17 | 7/4.7 | 1/0.2 | 0/0.1 |

**7.5 The largest masses at which a prime still fails** (max over the sample of the masses over x < HC(p); over all
windows, not only the dyadic grid):

| sample | max Λ/log p | max Γ/log p | max S (cL = ½) |
|---|---|---|---|
| primes 10⁹ (50 000) | 0.83 | 0.13 | 3.2 |
| primes 10¹¹, 10¹³, 4·10¹⁵ | 0.47, 0.43, 0.29 | 0, 0, 0 | 0, 0, 0 |
| m² + 24, m² + 120 | 0.56, 0.77 | 0.084, 0.086 | 2.5, 2.9 |
| hard list, p > 10⁸ (139 primes) | — | 0.14 | 4.0 |
| hard list, all (166) | 2.91 (21841) | 1.02 (21841, log p = 10.0) | 9.7 (21841) |
| scans, x ≤ 64 (6.5·10⁶ primes) | — | — | 4.8 (10⁹), 3.0 (10¹²), on the dyadic grid |

Reading (EVIDENCE):
* (i) Below X = 16 every failure is genus-dead: all lines ≤ X have g = 0. With x | 24, 7, 15 deterministic, there is no
  lottery line below 16 at all.
* (ii) Where lotteries occur, the class failures are compared with the two surrogates (not every row lies between them):
  * observed/predicted is 0.31–0.94 with cL = ½ and 0.67–1.71 with cL = 1 (10⁹);
  * it is 0.75–1.16 and 1.47–4.2 respectively (10¹², counts ≤ 25).
  At these small x the marginal laws are not calibrated (§7.3), and the counts are low. The data show **no clear
  systematic joint-failure excess given the genus masses**. This contrasts with the raw ×3–×80 of HCSHIFTS (L2), which conditioned on nothing; HCSHIFTS'
  stratification by p mod 15015 removed most of it too. They do not establish independence or negative dependence.
* (iii) In the samples of consecutive primes at 10¹¹–4·10¹⁵ *every* failure occurs at Γ = 0: the prime fails exactly while all its
  lines are genus-dead. At 10⁹ and at near-squares, failures occur with Γ ≤ 0.14 log p.
* (iv) The hard primes of the HCSHIFTS list are mostly genus-starved: of the 145 with HC ≥ 20, 95 have Γ(p, 16) = 0. The
  exception is 21841 (HC = 64, the record below 10⁸). It still fails at Γ = 10.2 = 1.02 log p and S = 9.7 (windows
  60 ≤ X ≤ 63). Given its masses, the surrogate gives this event probability e^{−9.7} ≈ 6·10⁻⁵. 21841 is the HC
  record among the ≈ 1.4·10⁶ primes p ≡ 1 (8) below 10⁸.
* So at accessible heights failure is overwhelmingly a genus/anatomy deficit. The one high-mass failure seen is at a
  tiny prime and is compatible with a lottery tail. Finite data cannot test the eventual statement Lot(C), whose p₀ is
  unspecified. These numbers bound nothing at the heights where S_A's logarithmic mass matters.

## 8. FRONTIER §4 hard screens (for the conditional route Anat + Lot ⟹ S_A)

1. *T1 squares.*
   * The anatomy layer is class-blind: the A2 bound holds at odd squares (PROVED). Numerically, Λ at squares is
     comparable to Λ at primes (§7.2). Anat itself is not proved at squares or anywhere.
   * Γ = 0 at squares (Lemma 1.1(d), PROVED; CERTIFIED on 5 000 squares × all lines ≤ 1024).
   * So the step that must fail at squares is the genus layer (Γ comparable to Λ). Lot_Γ is vacuous there, and Lot_Λ is
     stated for primes only. **Passes** as bookkeeping. The primality input sits in the genus layer, which no
     unconditional theorem here controls pointwise.
2. *8/131.* Lot is an ES-specific lottery statement with a threshold p₀. A numerator-8 analogue is not formulated.
   **Not established.**
3. *Tied modulus.* **FAILS as a mechanism.** Lot postulates the lottery outcome. It does not force a divisor in a class.
4. *Fixed p.* Theorems A, C, D and S are pointwise or model statements. Theorem B is an average over p, used only as
   calibration. Lot and Anat are pointwise hypotheses. **Passes formally.**

## 9. Proposed FRONTIER §7.2 text (for the curator; not edited here)

> *(z54, `Z54_HCWIN.md`.)* **A sufficient three-layer route.** S_A (HC(p) ≤ (log p)^A) follows from (a) a pointwise
> anatomy statement for the window integers p + x, xp + 1 (x ≤ X), namely Anat: Λ(p, X) = Σ min(1, τ(N)/φ(x)) ≥ C log p,
> or its genus form with Γ (Γ = 0 at odd squares), together with (c) a conditioned class lottery Lot(C):
> "mass ≥ C log p ⟹ HC(p) ≤ X" (Thm S, a PROVED implication). Neither Anat nor Lot is proved, and S_A does not imply Anat.
> * 2 log 2 separates two *anatomy* regimes, on average over primes (Thm B, PROVED rel. Henriot + BV). For
>   log 2 < θ < 2 log 2 the average of Λ(p, (log p)^θ) is ≤ (log p)^{g(θ/log 2)+o(1)} = o(log p) (upper bound only;
>   for θ ≤ log 2 it is trivially o(log p)). For θ > 2 log 2 it is ≫ log p log log p. The boundary is not decided.
> * At one p only the outer layer is provable. Turán–Kubilius over the window variable sees primes ≤ √X only, and
>   Λ(p, X) ≥ (1/8) log²X − O(log X) pointwise, at every odd integer including squares (Thm A, PROVED). Pointwise Anat
>   at polylogarithmic X is a short-interval divisor-type problem with no known approach (Assessment; the cited Δ-bound
>   supplies a sufficient range X ≥ p^{θ*+ε}, θ* = 0.31448…, for the unweighted divisor asymptotic).
> * In the Kubilius model, the conjunction "some line has τ ≥ Kφ(x)" ∧ "every such line fires" has probability 0 for
>   every K (Thm C, model-only). A model-compatible class hypothesis must therefore be joint (Assessment).
> * Lot_Λ(C) alone implies HC(p) ≤ exp(√(8C log p) + O(1)) = p^{o(1)} (Thm D, CONDITIONAL). In the model Lot holds a.s.
>   for C > 4 (C > 2 for Γ), and S_{2 log 2} holds a.s. (Prop M′, deciding HCHYP's boundary in the model only).
> * EVIDENCE (10⁹–4·10¹⁵): for genus mass m ≥ ½ a line fires with probability within ≈ 4 points of 1 − e^{−m}
>   (endpoint) or 1 − e^{−m/2} (level), pooled over x ∈ [64, 1024). Small m falls short. Joint class failures at x ≤ 64
>   show no clear systematic excess over the lottery surrogates (low counts). In consecutive-prime samples at
>   10¹¹–4·10¹⁵ all failures occur at Γ = 0.
>   Odd squares have prime-like Λ and Γ ≡ 0 (CERTIFIED).

## 10. Bottom line

The model exponent 2 log 2 is an **anatomy** exponent, and on average over primes it is arithmetic. The truncated divisor
mass of the window {p + x, xp + 1 : x ≤ (log p)^θ} is o(log p) on average for θ < 2 log 2 and ≫ log p log log p for
θ > 2 log 2 (Theorem B, PROVED relative to Henriot and BV; the boundary is not decided). At a single p only the outer,
congruence-data layer of that anatomy is provable. Turán–Kubilius over the window variable is exact but sees only
primes ≤ √X, and the pointwise mass bound is (1/8) log²X − O(log X) (Theorem A). Pointwise anatomy at polylogarithmic X
is a short-interval divisor-type problem with no known method (Assessment).

On the class side, the per-line hypotheses examined are false in the Kubilius model at every K (Theorem C, model-only).
The natural replacement is a conditioned joint lottery Lot(C), which is exponent-free and holds in the model for C > 4
(C > 2 in its genus form).
* Combined with pointwise anatomy, Lot gives S_A (Theorem S, a sufficient route).
* Alone, Lot_Λ gives HC(p) ≤ exp(√(8C log p) + O(1)) = p^{o(1)} (Theorem D, CONDITIONAL).
* As a byproduct, the boundary case A = 2 log 2 holds in the model (Prop M′).

At accessible heights, for m ≥ ½ a line behaves like a lottery with the genus mass as its parameter, to within a few
percentage points; small masses do worse than the law. Joint class failures show no gross excess over the lottery
surrogates. Almost every observed failure happens while the genus mass is zero. The one high-mass failure (21841,
Γ ≈ 1.02 log p) is at a tiny prime. None of this tests an eventual statement.

So §7.2 can record a **sufficient route: anatomy (open pointwise; its threshold PROVED on average) + genus layer (where
T1 lives) + a joint conditioned lottery (B2-type; open; model-true; consistent with the data)**. Nothing here forces a
single tied divisor event. B2 has not moved.

## 11. Reproduction

```sh
gcc -O2 -o /tmp/hcwinZ54run scripts/z54_hcwin_lines.c -lm     # compile WITHOUT a vmem ulimit (ld fails under it)
ulimit -v 6000000; mkdir -p /tmp/z54e
timeout 120 /tmp/hcwinZ54run list 128 /tmp/t.txt 193 409 577 2521 3361 5569 9601 21841 66529 83449 8813281   # HC check
for a in "1000000000 1e9" "100000000000 1e11" "10000000000000 1e13"; do set -- $a
  timeout 1800 /tmp/hcwinZ54run stat $1 50000 1024 /tmp/z54e/stat_$2.txt; done           # ~2-4 min each
timeout 1800 /tmp/hcwinZ54run stat 4000000000000000 20000 1024 /tmp/z54e/stat_4e15.txt
timeout 1800 /tmp/hcwinZ54run list 1024 /tmp/z54e/hard.txt $(cat data/z53/hcshifts/hard_primes_list.txt)
timeout 1800 /tmp/hcwinZ54run sq 100001 5000 1024 /tmp/z54e/sq_1e10.txt                  # T1 control
timeout 1800 /tmp/hcwinZ54run near 24 100000 5000 1024 /tmp/z54e/near24_1e10.txt         # also k = 120
timeout 1800 /tmp/hcwinZ54run int 100000000000 20000 1024 /tmp/z54e/int_1e11.txt
timeout 1800 /tmp/hcwinZ54run scan 1000000000 4000000 /tmp/z54e/scan_1e9.txt             # ~10 min, 0.45 GB
timeout 1800 /tmp/hcwinZ54run scan 1000000000000 2500000 /tmp/z54e/scan_1e12.txt
uv run --with numpy python scripts/z54_hcwin_analyze.py /tmp/z54e/stat_1e9.txt                     # masses, failures
python3 scripts/z54_hcwin_perline.py /tmp/z54e/stat_1e9.txt.lines 5                                 # per-line law
uv run --with numpy --with pandas python scripts/z54_hcwin_joint.py /tmp/z54e/scan_1e9.txt 0.5 1.0  # joint test
```
Committed data (`data/z54/hcwin/`): all `.lines` tables, the first 5 000 rows of every per-prime file (gzip), `hard.txt`,
the joint outputs, `analyze_all.out`, `perline_all.out`, `lit_notes.md` and the internal review. The full per-prime files
are regenerated by the commands above; they are deterministic. (The first draft's files, in an older column format with
the composite-control τ bug, are superseded.)

## 12. Review log

* **Internal hostile review** (deep-mode subagent; `data/z54/hcwin/REVIEW_internal.md`, 33 items). Fixes applied:
  * the false Γ ≤ Λ remark (item 1);
  * A1 restated for ω_z with a direct proof and Lemma A1 for all odd moduli (items 3–4);
  * "Anat at squares" and the necessity reading of the decomposition removed: the route is sufficient only (6);
  * the Henriot erratum checked for aX + 1 (8);
  * B(ii) wording and the range/boundary remarks (10, 12);
  * Jutila restricted to almost all starting points (13);
  * the Li–Yang scope and the Burgess exponent corrected (14);
  * Theorem C relabelled as model-only, with the joint-lottery reading as Assessment (16);
  * M′ restricted to k ≥ 3 (17);
  * L(a) given the factor 2 and the empty-crossing convention (19);
  * L(b) given its Γ part (conditional Jensen) and its κ ≤ 1 range (20);
  * S's C-ranges stated (22);
  * the known-kills paragraph rescoped, with the alignment escape example (24);
  * the composite-control τ bug fixed in code and all data regenerated (25);
  * the hard-prime rows for p < 1024 labelled (26);
  * the ranges corrected (28);
  * the per-line law re-measured with bin-averaged predictions, the low-mass shortfall reported, and the claim
    weakened to a pooled approximate shape (29);
  * x = 7, 15 classified deterministic (Lemma 1.2) and the joint tables regenerated; the earlier "joint failures rarer
    than independence" claim withdrawn (31);
  * the failure masses now taken over *all* windows (per-prime pre-HC masses), with the 21841 counterexample to the
    first draft's "max 0.49" reported (32).
  Items 2, 5, 7, 9, 11, 15, 18, 21, 23, 27, 30 and 33 were confirmed by the reviewer.
* **Cross-model review** (`data/z54/xreview/REVIEW_HCWIN.md`; helpers `scripts/z54_xrev_hcwin_check.py`,
  `scripts/z54_xrev_hcwin_joint.py`): ACCEPT-WITH-FIXES. The reviewer re-derived all numbered results, regenerated the
  squares, the 10⁹ sample, the hard list and the 10¹² scan (byte-identical or count-identical), and checked Henriot
  (with its erratum), Li–Yang and Ivić–Zhai from the sources. Fixes applied:
  * A1's parenthesis restricted to strongly additive sums, and the §0 summary quantifier corrected (Chebyshev
    exceptions; density one only with t → ∞);
  * the per-line precision restated as "about four percentage points" (a 3.9-point level bin);
  * the joint summary restated with both heights, low counts and "no clear systematic excess";
  * §9 "needs X ≥ p^{0.3145}" replaced by a sufficient-range statement;
  * the "random samples" are now called consecutive-prime samples.

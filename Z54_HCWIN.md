# Z54_HCWIN — the growing-window target HC(p) ≤ (log p)^A, A > 2 log 2: anatomy layer vs class layer (wave z54, lane HCWIN)

**ES is OPEN. Nothing here proves or disproves ES.** Labels: PROVED / CONDITIONAL (on what) / CERTIFIED / EVIDENCE /
CONJECTURE / Assessment. Internal results, internally reviewed only. Scripts `scripts/z54_hcwin_*`, data `data/z54/hcwin/`.
Kickoff: `z52bbriefs/z54_lanes.md` §HCWIN (FRONTIER §7.2).

## 0. Verdict first

**Verdict: NARROWED, with one small strengthening.** S_A is not proved. The lane splits S_A into an anatomy layer and a
class layer, proves what is provable about the anatomy layer, and calibrates the class layer in the model and on data.

1. **Where 2 log 2 comes from (Theorem B; PROVED relative to Henriot's uniform Nair–Tenenbaum bound and
   Bombieri–Vinogradov).** The threshold is a fact about the *truncated divisor mass* of the window integers,
     Λ(p, X) := Σ_{x∈𝒞, x≤X} [min(1, τ(p+x)/φ(x)) + min(1, τ(xp+1)/φ(x))],
   on average over primes p. Put X = (log T)^θ and κ = θ/log 2.
   * For 1 < κ < 2, the average of Λ over p ∈ (T, 2T] is ≤ (log T)^{g(κ)+o(1)}, where g(κ) = κ log 2 − κ log κ + κ − 1 < 1.
   * For κ > 2, the average is ≫_θ log T · log log T.
   The mean of τ(p+x) is carried by integers with ω ≈ 2 log log p, so the window must reach τ ≈ (log p)^{2 log 2} before the
   untruncated mass Σ τ/φ stops being cut off by the min(1, ·). The exponents match the model's g(κ) of HCSHIFTS §3.2.
   No model is used in the proof; it is an average over p (B6), so it only *calibrates* the threshold.
2. **What is provable at a single p (Theorem A; PROVED, elementary).**
   * Turán–Kubilius over the window variable x is exact, but only for primes ≤ X^{1/2}. The provable single-p anatomy is
     therefore ω_{≤√X}(N_x) = (1+o(1)) log log X for almost all x ≤ X, which is ≍ log log log p prime factors at
     polylogarithmic X. The model needs ≈ 2 log log p.
   * Pointwise, Λ(p, X) ≥ (1/8) log²X − O(log X) for every prime (indeed every odd integer) p > X. This comes from the
     "outer layer", the divisors d ≤ x/2 of p + x, which are congruence data.
   * Everything beyond is a pointwise short-interval divisor problem. Known pointwise methods need windows ≥ p^{0.3145}
     (Li–Yang); Jutila's mean square gives almost all p only (Assessment, §3.3).
3. **The class hypothesis cannot be per-line (Theorem C; PROVED in the HCHYP model 𝔐).**
   Take the two-layer decomposition "(ii) every large p has a line with τ ≥ Kφ(x)" plus "(i) every such big line
   succeeds". This conjunction has 𝔐-probability 0 for every fixed K, and also for every K = K(p) → ∞, at every
   window size.
   So any correct class statement must be a **joint lottery**: it must assert that at least one of ≍ log p·log log p lines,
   each with a small success probability, fires.
4. **The conditioned lottery Lot(C) and two conditional theorems (PROVED implications; hypotheses OPEN).**
   * Lot_Λ(C): "Λ(p, X) ≥ C log p ⟹ HC(p) ≤ X". Lot_Γ(C) is the same with the genus mass Γ (§1). Both hold 𝔐-a.s. for
     C > 4, resp. C > 2 (Prop L).
   * **Thm S:** Anat(A, C) ∧ Lot(C) ⟹ S_A. In 𝔐, Anat(A, C) holds a.s. iff A ≥ 2 log 2, so the whole exponent lives
     in the anatomy conjunct.
   * **Thm D:** Lot_Λ(C) *alone* ⟹ HC(p) ≤ exp((1+o(1))√(8C log p)) = p^{o(1)} for all large p. This beats the open
     target HC ≪ p^θ, conditionally on a pure class-layer statement.
   * Byproduct (Prop M′, PROVED in 𝔐): the boundary case A = 2 log 2, left undecided in HCHYP Thm M, holds in 𝔐.
5. **Numerics (EVIDENCE; CERTIFIED controls).** About 1.7·10⁵ primes with all lines x ≤ 1024, plus 6.6·10⁶ primes with
   lines x ≤ 64, at heights 10⁹–4·10¹⁵.
   * *Per-line law.* Given the genus mass m = g/|G_x²|, an endpoint line succeeds with probability 1 − e^{−m} to within
     a few per cent, in every dyadic block and at every height. Level lines follow 1 − e^{−m/2} (pairing d ↔ N/d).
   * *Joint failures.* Given the genus masses, joint failures are *rarer* than independence predicts (observed/predicted
     0.25–0.6). Every failure below X = 16 is genus-dead.
   * *Hard primes are genus-starved, not unlucky.* 95 of the 145 listed primes with HC ≥ 20 have Γ(p, 16) = 0.
   * *Odd squares:* Λ is as large as at primes, while Γ = 0 on all 3.84·10⁶ lines (CERTIFIED).

**What it buys.** FRONTIER §7.2 can be sharpened from "B2 with a growing window" to three named layers:
* (a) a pointwise anatomy statement for the window integers p + x, xp + 1. It is not ES-specific and is OPEN (a polylog
  short-interval divisor problem); its threshold 2 log 2 is PROVED on average;
* (b) the genus layer;
* (c) a conditioned class lottery (OPEN, B2).
Per-line forms of (c) are model-false; (c) alone already gives p^{o(1)}.

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

So Γ ≤ Λ fails only through non-squarefree parts, and Γ = 0 at odd squares. Lemma 1.1(d) is where primality enters: Γ
is the T1-aware mass, Λ is class- and genus-blind.

**Statements attacked.**
* **(Q1)** The arithmetic origin of 2 log 2. Target form: Anat(A, C): Λ(p, (log p)^A) ≥ C log p for all large p.
* **(Q2)** The part of Anat provable at one p.
* **(Q3)** The weakest clean class hypothesis, and S_A conditional on it plus anatomy. Can it be per-line?
* **(Q4)** Numerics to 10¹³, at hard primes, with odd squares, near-squares and the §4 item-14 primes as controls.

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

**Lemma A1.** Let q = ℓ^k ≤ X be an odd prime power, ℓ ≠ p, and F ∈ {E, L}. Then
  #{x ∈ 𝒳 : q | N_x^F} = |𝒳|/q + O(1), with |O(1)| ≤ 4.
The same holds for squarefree odd q ≤ X coprime to p, with ν(q) = 1/q.

*Proof.*
* q | p + x ⟺ x ≡ −p (mod q).
* q | xp + 1 ⟺ x ≡ −p̄ (mod q), where p̄ is the inverse of p mod q.
* 𝒞 is the union of the classes 0, 4, 7 mod 8 (minus x < 4), and (q, 8) = 1. By the Chinese remainder theorem each
  class mod 8 meets the condition in exactly one class mod 8q. Each class mod 8q has X/(8q) + O(1) members in [1, X]. ∎

**Theorem A1 (Turán–Kubilius over the window; PROVED).** Let 2 ≤ z ≤ X^{1/2}, and let f be a complex additive function
supported on odd prime powers ≤ z (f(n) = Σ_{q ∥ n, q ≤ z} f(q)). Put μ_f := Σ_{q≤z} f(q)(1 − 1/ℓ)/q. Then
  Σ_{x∈𝒳} |f(N_x^F) − μ_f|² ≤ C |𝒳| Σ_{q≤z} |f(q)|²/q
with an absolute C. In particular, for ω_z(n) := #{ℓ ≤ z odd prime : ℓ | n},
  #{x ∈ 𝒳 : |ω_z(N_x^F) − log log z| > t√(log log z)} ≪ |𝒳|/t².

*Proof.* The standard Turán–Kubilius proof (Tenenbaum, *Introduction to analytic and probabilistic number theory*,
III.3, Thm 3.1, in its "sieve" form) uses only the counts #{x : q | N_x} and #{x : q₁q₂ | N_x} for coprime q₁, q₂ ≤ z.
Lemma A1 gives them with densities 1/q, 1/(q₁q₂) and O(1) errors. The accumulated error is
  O((Σ_{q≤z}|f(q)|)²) ≤ O(Σ_{q≤z} q · Σ_{q≤z} |f(q)|²/q) ≤ O(z² Σ |f(q)|²/q) ≤ O(X Σ |f(q)|²/q),
by Cauchy–Schwarz and z² ≤ X. Mertens gives μ_{ω_z} = log log z + O(1). ∎

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
* Primality is not used. The bound holds at odd squares, where every line is genus-confined (Lemma 1.1(d)). So the
  anatomy layer cannot see T1; primality must enter through the genus or class layer.
* The certificates the outer layer can supply are congruence data. A small divisor d ≤ x/2 is never ≡ −1 (mod x). Its
  cofactor (p + x)/d is ≡ −1 iff d ≡ −p (mod x), i.e. iff p ≡ −(x + d) (mod xd). This is the word (t, x, d) with two
  small coordinates, a forest edge {x, d}. Such certificates can all be absent up to exp((log p)^κ), κ < 1/6, at
  infinitely many primes (H4_NOT_POLYLOG Thm 1). There the outer mass is only (log p)^{2κ}.

### 3.3 Beyond the outer layer: a pointwise short-interval divisor problem (Assessment, with checked literature)

The remaining mass comes from divisors d ∈ (X, √p] of p + x, i.e. from lattice points (m, d) with p < md ≤ p + X.
* Pointwise control of Σ_{p<n≤p+X} τ(n) is known only for X ≥ p^{θ*+ε}, with θ* = 0.31448… (Li–Yang, arXiv:2308.14859,
  Thm 1.2; this improves Huxley's 131/416). Do not cite Bourgain–Watt 517/1648: its arXiv comment withdraws Thms 1–3.
* Jutila's mean square, ∫_T^{2T}(Δ(x+U) − Δ(x))² dx ≪ TU log³(√T/U) + T log⁴T for 1 ≤ U ≤ T^{1/2}/2 (as quoted in
  Ivić–Zhai, arXiv:1209.0872, Thm B and (2.3)), gives Σ_{x<n≤x+U} τ(n) ~ U log x for *almost all* x once
  U/log T → ∞. That is an average over p (B6).
* For polylogarithmic X the literature search (`data/z54/hcwin/lit_notes.md` Q3) found nothing pointwise beyond the
  trivial bounds Σ τ ≫ X log X and max ω ≳ log X/log log X (CRT).
* Even "every [N, N + (log N)^A] contains an n with ω(n) ≥ c log log N", or with τ(n) ≥ (log N)^c, appears to be open.
  Tao (MathOverflow 275191) notes that no technique rules out conspiracies of medium-sized primes in such intervals.

*Assessment.* Pointwise Anat(A, C) at polylogarithmic X is beyond current methods. It is a class-blind, ES-independent
statement about divisors of integers in a polylogarithmic window at a prime, so the HC target contains at least this
open problem. Its sieve-theoretic part is blocked by parity: a window in which every integer coprime to the small primes
is (X-smooth)·(prime) is consistent with all upper-bound sieve information (Selberg-type upper bounds give
≤ (2 + o(1))X log log X/log X such integers, against ≍ X/log X rough integers in the window).

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
  Both are linear, so D* = 1, and ‖Q‖ ≤ a + 1 ≤ T^δ. The constant depends only on the degree, α, δ and the Shiu
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
* *Lower bound for Στ (BV).* Every n has τ(n) ≥ 2#{d | n : d ≤ √n}. With D := T^{1/2}(log T)^{−B} and BV for the moduli
  8d ≤ 8D:
    Σ_{p∈(T,2T], p≡1(8)} τ(p+x) ≥ 2 Σ_{d≤D odd, (d,x)=1} #{p ∈ (T,2T] : p ≡ 1 (8), p ≡ −x (d)}
                               ≥ 2π*(T) Σ_{d≤D odd, (d,x)=1} 1/φ(d) − O(T/log²T)
                               ≥ c₁ (φ(x)/x) π*(T) log T,
  with c₁ > 0 absolute, uniformly in x ≤ (log T)^C. Here Σ_{d≤D, (d,2x)=1} 1/d ≥ (φ(2x)/(2x))(log D − O(log log x)).
* *Upper bound for Στ^{1+η} (H).*
    Σ_p τ(p+x)^{1+η} ≤ C_η (x/φ(x)) π*(T) (log T)^{2^{1+η}−1}.
* Hence the bracket summed over p is
    ≥ π*(T)(φ(x)/x) log T·[c₁ − C_η (x/φ(x))² φ(x)^{−η} (log T)^{2^{1+η}−2}].
* For x > Y we have φ(x) ≥ x/(C log log x), so the subtracted term is ≤ (log T)^{2(2^η−1) − ηθ₀ + o(1)}.
  Now 2(2^η − 1) − ηθ₀ = η(2 log 2 − θ₀) + O(η²) < 0 for small η > 0. So the bracket is ≥ (c₁/2)·π*(T)(φ(x)/x) log T
  for T ≥ T₀.
* Dividing by φ(x) leaves (c₁/2) π*(T) log T/x. Summing over x ∈ (Y, X] with 4 | x gives ≥ (c₁/8) π*(T) log T·(θ − θ₀)
  log log T·(1 − o(1)). ∎

*Reading.*
* The window's truncated divisor mass reaches log p *on average* exactly at (log p)^{2 log 2}. Below it, it is
  (log p)^{g(κ)} = o(log p), the same exponent as the model's per-block cost (HCSHIFTS §3.2, item 4).
* The mechanism is Rankin's: E_p τ(p + x)^s ≍ (log p)^{2^s − 1}. The minimiser s* = log₂ κ is the tilt at which τ's
  mass sits at ω ≈ κ log log p.
* So 2 log 2 is an arithmetic property of τ on shifted primes, not an artefact of 𝔐. Part (i) is an upper bound only:
  no lower bound of the form (log T)^{g(κ)−o(1)} is claimed (it would need lower-bound large deviations for ω(p + a),
  which Ford, *Lith. Math. J.* 61 (2021), reports as unknown for every k).
* Thm B is an average over p (screen 5). It calibrates; it does not reach one p.

## 5. The model: per-line class is false, the conditioned lottery is not

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
τ/φ(x) ≪ 1 (cf. HCSHIFTS §3.2: at the critical scale the share of hits with τ ≳ φ decays like λ^{−1/2}). **Any correct
class statement must be a joint lottery.**

**Proposition M′ (PROVED in 𝔐; decides HCHYP's boundary case in 𝔐).** 𝔐-a.s., HC(p) ≤ (log p)^{2 log 2} for all large p.

*Proof.* Put X := (log p)^{2 log 2}, so log₂ X = 2λ.
* By HCHYP Lemma M1, P(line succeeds | k) ≥ ½ min(1, (2^k − 1)/φ(x)) ≥ ½ min(1, 2^{k−1}/x) for k ≥ 1.
* For 2^k ≤ x, the minimum is 2^{k−1}/x. Also Σ_{x∈𝒞, U<x≤X} 1/x ≥ (3/8) log(X/U) − 3 for U ≥ 8.
* Using E-lines only,
    S := Σ_{x∈𝒞, x≤X} P(E-line at x succeeds) ≥ ½ E[2^{k−1} ((3/8) log 2·(2λ − k) − 3)_+].
* With E[2^k F(k)] = e^λ E F(V), V ~ Poi(2λ), this is ≥ ¼ e^λ E[((3/8) log 2·(2λ − V) − 3)_+].
* By the Poisson CLT, P(V ≤ 2λ − √(2λ)) → Φ(−1) > 0.15, so S ≥ c·log p·√(log log p) for large p.
* Lines are independent, so P(HC(p) > X) ≤ exp(−S), which is summable over p. The first Borel–Cantelli lemma gives the
  claim. ∎

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
* Then X*(p) := min{X : Γ(p, X) ≥ C log p} is determined. Given the data, the lines succeed independently.
* *Γ version.* Write g_{ι,i} = c_{ι,i}h_{ι,i}, with c fixed coset representatives and h_{ι,i} i.i.d. uniform in G_x².
  For nonempty I in the genus fibre of −1, g_I is uniform on −G_x². For distinct such I, J the events {g_I = −1},
  {g_J = −1} are independent: pick j ∈ J∖I (or I∖J) and use the uniformity of h_j.
* Lemma M1's Paley–Zygmund argument therefore gives P(success | data) ≥ ½ min(1, g_ι/|G_x²|). The empty product is not
  in the fibre, since −1 ∉ G_x² for x ∈ 𝒞 (4 | x, or x has a prime factor ≡ 3 (4)).
* So P(all lines ≤ X* fail | data) ≤ exp(−½Γ(p, X*)) ≤ p^{−C/2}, which is summable for C > 2.
* *Λ version.* Use M1 directly: ½ min(1, (2^k−1)/φ) ≥ ¼ min(1, 2^k/φ) for k ≥ 1. Lines with k = 0 contribute
  ≤ Σ_{x≤X} 1/φ(x) = O(log X) = o(log p) to Λ. This gives p^{−C/4+o(1)}, summable for C > 4.
(b) *Upper range.*
* By Lemma 1.1(c) (in 𝔐 the "primes" are distinct), Γ_ι ≥ min(1, 2^{k_ι}/φ(x))·1[v(−1) ∈ W_ι].
* Given k, P(v(−1) ∉ W_ι) ≤ 2^{r_x}·2^{−k}: a nonzero character of G/G² is trivial on k uniform elements with
  probability 2^{−k}.
* So EΓ ≥ EΛ − Σ_{x≤X} 2^{r_x+1}/φ(x) = EΛ − O((log X)^{O(1)}).
* The proof of M′ gives EΛ ≥ c log p √(log log p) at A = 2 log 2, and larger for larger A.
* Λ and Γ are sums of independent [0, 1] variables, so the Chernoff bound P(Γ ≤ EΓ/2) ≤ exp(−EΓ/8) is summable.
*Lower range.*
* For A = κ log 2 with κ < 2, the Rankin computation of Theorem B(i) inside 𝔐 (E 2^{sk} = (log p)^{2^s−1}) gives
  EΛ ≤ (log p)^{g(κ)+o(1)} = o(log p).
* Markov's inequality gives P(Λ ≥ C log p) → 0, and the second Borel–Cantelli lemma (independence across p) gives
  failure at infinitely many p. ∎

## 6. Conditional theorems

**Theorem S (PROVED implication).** Anat_Γ(A, C) ∧ Lot_Γ(C) ⟹ S_A, and Anat_Λ(A, C) ∧ Lot_Λ(C) ⟹ S_A (window cap
X_max ≥ (log p)^A).
*Proof.* Take X = (log p)^A in Lot. ∎

In 𝔐 both conjuncts are almost sure exactly when A ≥ 2 log 2 (Prop L). The exponent lives entirely in the anatomy
conjunct, which is class-blind (Λ) or genus-level (Γ). The class conjunct Lot is exponent-free.

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
  X ≤ exp(√log p) is a least-non-residue problem, out of unconditional reach (Burgess needs p^{1/4}).
* *Consistency with every known kill (Assessment).* Each infinitely-often kill in the repository depletes the anatomy,
  genus or outer layer rather than producing an unlucky class draw at high mass:
  * Thm W/W2 (Dickson-type): window integers are (forced small part)·prime, so Λ ≍ smooth mass;
  * Prop 3.3/W3: small-prime certificates only;
  * H4: outer certificates, outer mass (log p)^{2κ}, 2κ < 1/3;
  * T1 and alignment (Lemma N): Γ = 0 on the affected lines.
  None of them refutes Lot(C) with C log p mass. Whether some construction does is open.
* Lot is ES-specific (it speaks about divisor classes of the ES lines). It is weaker than HCHYP's LT in one respect (it
  is conditioned on the actual mass, so anatomy deficits are not charged to it) and stronger in another (pointwise rather
  than a frequency bound). It is B2 restated for a joint family. It is *not* a mechanism.

## 7. Numerics (EVIDENCE unless marked CERTIFIED)

Program `scripts/z54_hcwin_lines.c` (C; trial division + Pollard–Brent + deterministic Miller–Rabin; explicit divisor
enumeration). For every line with x ∈ 𝒞, x ≤ 1024, it computes τ(N), the genus count g (DP over G_x/G_x² ≅ (ℤ/2)^{r_x}),
the class count c, and the outer data. HC values at 193, 409, 577, 2521, 3361, 5569, 9601, 21841, 66529, 83449 and
8813281 reproduce Fable's 7, 4, 4, 15, 7, 7, 7, 64, 8, 39, 8 (CERTIFIED).

**7.1 Controls.**
* *Odd squares* m², m odd from 100 001 (5 000 values): all 3 840 000 lines (x ≤ 1024) are genus-confined, Γ = 0, and
  there are 0 successes (CERTIFIED; Lemma 1.1(d)).
* At the same squares, mean Λ(·, 1024)/log n = 4.82, against 4.95–5.85 at primes. **The anatomy layer does not see T1;
  the genus layer does.**

**7.2 Window masses** (means over the sample; X = 64 and X = 1024):

| sample | N | P(HC>8) | P(HC>16) | Λ/log p (64) | Γ/log p (64) | Λ/log p (1024) | Γ/log p (1024) | min Γ/log p (1024) |
|---|---|---|---|---|---|---|---|---|
| primes from 10⁹ | 50 000 | 1.6e−3 | 1.0e−4 | 1.69 | 1.23 | 5.85 | 4.56 | 2.52 |
| primes from 10¹¹ | 50 000 | 9.8e−4 | 4.0e−5 | 1.44 | 1.08 | 5.34 | 4.31 | 2.46 |
| primes from 10¹³ | 50 000 | 6.4e−4 | 2.0e−5 | 1.25 | 0.96 | 4.95 | 4.08 | 2.44 |
| primes from 4·10¹⁵ | 20 000 | 4.0e−4 | 5.0e−5 | 1.07 | 0.84 | 4.53 | 3.83 | 2.62 |
| non-square n ≡ 1 (8) from 10¹¹ | 20 000 | 2.6e−3 | 5.0e−5 | 1.37 | 0.99 | 4.70 | 3.70 | 1.62 |
| primes m²+24, m ≥ 10⁵ | 5 000 | 2.0e−3 | 8.0e−4 | 1.48 | 0.94 | 5.42 | 3.98 | 2.62 |
| primes m²+120, m ≥ 10⁵ | 5 000 | 2.5e−2 | 1.6e−3 | 1.50 | 0.85 | 5.45 | 3.76 | 2.38 |
| odd squares | 5 000 | 1 | 1 | 1.45 | 0 | 4.82 | 0 | 0 |
| hard primes (HCSHIFTS list) | 166 | 0.91 | 0.87 | 1.73 | 0.68 | 5.88 | 3.31 | 2.55 |

* Genus-confined lines are common at primes: 47 % (10⁹), 41 % (10¹³) and 39 % (4·10¹⁵) of all lines x ≤ 1024, and 48 %
  at m² + 24.
* The near-squares and the hard primes keep their Λ but lose Γ. At X = 64, Γ/Λ ≈ 0.57–0.64 at near-squares and 0.39 at
  the hard primes, against 0.73–0.77 for random primes.

**7.3 Per-line law: given the genus mass, a line is a fair lottery.** From the `.lines` tables
(`z54_hcwin_perline.py`), the success rate of lines with m = g/|G_x²| in a bin, against 1 − e^{−m}:
* *Endpoint lines*, x ∈ [64, 1024), at 10⁹, 10¹³ and 4·10¹⁵:
  * m ≈ 0.15: 0.12 vs 0.14;
  * m ≈ 1.2: 0.69–0.70 vs 0.70;
  * m ≈ 1.7: 0.81–0.84 vs 0.81;
  * m ≈ 2.4: 0.90–0.92 vs 0.91.
  (Bin centres m = 2^{b+1/4}.) The law is the same in every dyadic block and at both heights.
* *Level lines* follow 1 − e^{−m/2} closely (m ≈ 1.2: 0.42–0.44; m ≈ 2.4: 0.69–0.73). This is the pairing d ↔ N/d: N ≡ 1
  (mod x), so certificates come in pairs.
* Genus-confined lines (m = 0) never succeed (PROVED, Lemma 1.1(a)).
* Against τ/φ instead of m, the endpoint rate is lower and drifts with x (τ/φ ≈ 1.2: 0.60 at x ∈ [32, 64), rising to
  0.70 at x ∈ [512, 1024)). The genus normalisation is the stable one.

**7.4 Joint failure given the masses (the Lot falsifier).** Mode `scan` (`z54_hcwin_joint.py`): all primes p ≡ 1 (8)
from 10⁹ (4·10⁶ primes) and from 10¹² (2 572 700 primes; the run was cut short), lines x ≤ 64.
* Lines with x | 24 have G_x of exponent 2 and are deterministic (Lemma 1.1(b)); a prime with such a line of positive
  genus count succeeds. On the remaining primes the independent-lottery prediction is
  P(HC > X | data) = exp(−S), S := Σ_E m + ½ Σ_L m over lottery lines x ≤ X (§7.3).

| 10⁹, X | 8 | 12 | 16 | 20 | 24 | 28 | 32 | 40 |
|---|---|---|---|---|---|---|---|---|
| observed HC > X | 6558 | 2307 | 339 | 123 | 17 | 9 | 1 | 0 |
| of which genus-dead (S = 0) | 6558 | 2307 | 206 | 49 | 8 | 2 | 0 | 0 |
| class failures (S > 0): observed / predicted | 0/964 | 0/338 | 133/278 | 74/122 | 9/21 | 7/17 | 1/3.9 | 0/0.7 |
| largest S at a class failure | — | — | 4.0 | 4.0 | 3.5 | 3.8 | 4.8 | — |

| 10¹², X | 8 | 12 | 16 | 20 | 24 | 28 | 32 |
|---|---|---|---|---|---|---|---|
| observed HC > X | 1840 | 545 | 59 | 15 | 1 | 0 | 0 |
| of which genus-dead | 1840 | 545 | 33 | 7 | 0 | 0 | 0 |
| class failures: observed / predicted | 0/263 | 0/70 | 26/47 | 8/15 | 1/1.8 | 0/0.9 | 0/0.1 |
| largest S at a class failure | — | — | 3.0 | 3.5 | 1.5 | — | — |

With the cruder constant cL = 1 for level lines the observed/predicted class ratios are 0.64–1.34 (10⁹) and 1.10–2.2
(10¹², counts ≤ 26). Full outputs: `data/z54/hcwin/joint_1e9.out`, `joint_1e12.out`.

Reading (EVIDENCE):
* (i) Below X = 16 every failure is genus-dead: all lines ≤ X have g = 0. At X ≤ 12 the only lottery lines are x = 7.
  There N ≡ 0 (mod 8) and ⟨2⟩ = G_7², so the powers of 2 sweep the genus coset and the line is in fact deterministic
  (HCSHIFTS Lemma C(e) mechanism). This is why 0 of the predicted 964 class failures occur.
* (ii) Where genuine lotteries occur (X ≥ 16), class failures are *fewer* than independence with the calibrated
  constants predicts (ratio 0.25–0.61 at 10⁹, 0.54–0.56 at 10¹²).
  Conditioning on the actual genus masses removes the raw ×3–×80 joint-failure excess of HCSHIFTS (L2) and overshoots
  it. Forced small-prime structure (powers of 2 and 3 in N) makes classes *more* successful than uniform.
* (iii) No class failure has S > 4.8 in 6.6·10⁶ primes (S ≤ 0.24 log p).
* (iv) The hard primes of the HCSHIFTS list are genus-starved: of the 145 with HC ≥ 20, 95 have Γ(p, 16) = 0 and all
  have Γ(p, 16) ≤ 0.09 log p. The largest Γ/log p at a failure in that list is 0.49 (p = 21841 at X = 32, S = 5.1).
* At accessible heights, hardness is a *genus/anatomy deficit*, not bad luck in the class lottery at high mass. This is
  consistent with Lot(C) for every C ≥ 0.5. It cannot test Lot at the heights where S_A's logarithmic mass matters.

## 8. FRONTIER §4 hard screens (for the conditional route Anat + Lot ⟹ S_A)

1. *T1 squares.*
   * Anat_Λ holds at odd squares: Theorem A2 is class-blind (PROVED).
   * Γ = 0 at squares (Lemma 1.1(d), PROVED; CERTIFIED on 5 000 squares × all lines ≤ 1024).
   * So the step false at squares is the genus layer "Γ ≍ Λ". Lot_Γ is vacuous there, and Lot_Λ is stated for primes
     only. **Passes** as bookkeeping. The primality input is located in the genus layer, which no unconditional theorem
     here controls pointwise.
2. *8/131.* Lot is an ES-specific lottery statement with a threshold p₀. A numerator-8 analogue is not formulated.
   **Not established.**
3. *Tied modulus.* **FAILS as a mechanism.** Lot postulates the lottery outcome. It does not force a divisor in a class.
4. *Fixed p.* Theorems A, C, D and S are pointwise or model statements. Theorem B is an average over p, used only as
   calibration. Lot and Anat are pointwise hypotheses. **Passes formally.**

## 9. Proposed FRONTIER §7.2 text (for the curator; not edited here)

> *(z54, `Z54_HCWIN.md`.)* **Three layers.** S_A = HC(p) ≤ (log p)^A splits as (a) anatomy of the window integers
> p + x, xp + 1 (x ≤ X): the truncated divisor mass Λ(p, X) = Σ min(1, τ(N)/φ(x)); (b) genus layer (Γ; zero at odd
> squares); (c) a conditioned class lottery Lot(C): "mass ≥ C log p ⟹ HC ≤ X".
> * The threshold 2 log 2 is an *anatomy* threshold (Thm B, PROVED rel. Henriot + BV): on average over primes,
>   Λ(p, (log p)^θ) is (log p)^{g(θ/log 2)+o(1)} = o(log p) for θ < 2 log 2 and ≫ log p log log p for θ > 2 log 2.
> * At one p, only the outer layer is provable: Turán–Kubilius over the window variable sees primes ≤ √X only, and
>   Λ(p, X) ≥ (1/8) log²X pointwise (Thm A, PROVED, valid at squares). Pointwise Anat at polylog X is a short-interval
>   divisor problem with no known approach (known pointwise methods need X ≥ p^{0.3145}).
> * Per-line class hypotheses ("τ ≥ Kφ ⟹ the line fires", with anatomy supplying a big line) are false in the Kubilius
>   model for every K (Thm C). The class statement must be a joint lottery.
> * Lot_Λ(C) alone implies HC(p) ≤ exp(√(8C log p) + O(1)) = p^{o(1)} (Thm D, CONDITIONAL); in the model Lot holds a.s.
>   for C > 4, and S_{2 log 2} holds a.s. (Prop M′, deciding HCHYP's boundary in the model).
> * EVIDENCE (10⁹–4·10¹⁵): given the genus mass m, a line fires with probability ≈ 1 − e^{−m} (endpoint) or
>   1 − e^{−m/2} (level), uniformly in x and p. Joint failures given the masses are rarer than independence predicts.
>   Hard primes are genus-starved (Γ ≈ 0), not unlucky. Odd squares have prime-like Λ and Γ ≡ 0.

## 10. Bottom line

The model exponent 2 log 2 is an **anatomy** exponent, and it is arithmetic. On average over primes, the truncated
divisor mass of the window {p + x, xp + 1 : x ≤ (log p)^θ} reaches log p exactly when θ crosses 2 log 2 (Theorem B,
PROVED relative to Henriot and BV). At a single p only the outer, congruence-data layer of that anatomy is provable:
Turán–Kubilius over the window variable is exact but sees only primes ≤ √X, and the pointwise mass bound is
(1/8) log²X (Theorem A). Pointwise anatomy at polylogarithmic X is a short-interval divisor problem for which no method is
known (Assessment).

On the class side, per-line hypotheses are false in the Kubilius model at every K (Theorem C). The right object is a
conditioned joint lottery Lot(C). It is exponent-free and holds in the model for C > 4 (C > 2 in its genus form).
* Combined with pointwise anatomy, Lot gives S_A (Theorem S).
* Alone, Lot_Λ gives HC(p) ≤ exp(√(8C log p) + O(1)) = p^{o(1)} (Theorem D, CONDITIONAL).
* As a byproduct, the boundary case A = 2 log 2 holds in the model (Prop M′).

At accessible heights the data say the class layer behaves like a fair lottery given the genus mass, and jointly it does
slightly *better* than independent. Every hard prime seen is hard because its genus mass is near zero, not because the
lottery was unlucky at high mass.

So §7.2 becomes: **anatomy (open pointwise, threshold PROVED on average) + genus layer (where T1 lives) + a joint
conditioned lottery (B2, open, model-true, data-consistent)**. Nothing here forces a single tied divisor event. B2 has
not moved.

## 11. Reproduction

```sh
gcc -O2 -o /tmp/z54hcwin scripts/z54_hcwin_lines.c -lm        # compile WITHOUT a vmem ulimit (ld fails under it)
ulimit -v 6000000
timeout 120 /tmp/z54hcwin list 128 /tmp/t.txt 193 409 577 2521 3361 5569 9601 21841 66529 83449 8813281   # HC check
for a in "1000000000 1e9" "100000000000 1e11" "10000000000000 1e13"; do set -- $a
  timeout 1800 /tmp/z54hcwin stat $1 50000 1024 /tmp/z54d/stat_$2.txt; done              # ~2-4 min each
timeout 1800 /tmp/z54hcwin stat 4000000000000000 20000 1024 /tmp/z54d/stat_4e15.txt
timeout 1800 /tmp/z54hcwin list 1024 /tmp/z54d/hard.txt $(cat data/z53/hcshifts/hard_primes_list.txt)
timeout 1800 /tmp/z54hcwin sq 100001 5000 1024 /tmp/z54d/sq_1e10.txt                     # T1 control
timeout 1800 /tmp/z54hcwin near 24 100000 5000 1024 /tmp/z54d/near24_1e10.txt            # also k = 120
timeout 1800 /tmp/z54hcwin int 100000000000 20000 1024 /tmp/z54d/int_1e11.txt
timeout 1800 /tmp/z54hcwin scan 1000000000 4000000 /tmp/z54d/scan_1e9.txt                # ~10 min, 0.5 GB
timeout 1800 /tmp/z54hcwin scan 1000000000000 3000000 /tmp/z54d/scan_1e12.txt
uv run --with numpy python scripts/z54_hcwin_analyze.py /tmp/z54d/stat_1e9.txt                     # masses, failures
python3 scripts/z54_hcwin_perline.py /tmp/z54d/stat_1e9.txt.lines 5                                 # per-line law
uv run --with numpy --with pandas python scripts/z54_hcwin_joint.py /tmp/z54d/scan_1e9.txt 0.5 1.0  # joint test
```
Committed data (`data/z54/hcwin/`, 3.7 MB): all `.lines` tables, the first 5 000 rows of every per-prime file (gzip),
`hard.txt`, the joint outputs, `analyze_all.out`, `perline_all.out`, `lit_notes.md`. The full per-prime files are
regenerated by the commands above; they are deterministic.

## 12. Review log

[TBD]

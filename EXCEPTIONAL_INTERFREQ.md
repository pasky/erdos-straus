# EXCEPTIONAL_INTERFREQ — the inter-frequency cancellation door (task O18)

Status: **checkpoint 2 (O18), after the hostile review
`reviews/exceptional-interfreq-review.md` (SOUND-WITH-REPAIRS; D1–D7
applied).** Labels follow `DISCOVERIES.md`. PROVED
means proved in this file, internal checks only, not refereed. No θ > 3/4.

## 0. Summary

| item | statement | label |
|---|---|---|
| Obs 1.1 | unrestricted exact interval evaluation is the problem itself (ν = 1_𝒜); any cap must restrict spectrum, structure or evaluation | PROVED (trivial) |
| Thm 2.2 | Selberg minorant: ν ≥ 0 on ℤ, all nonzero frequencies of denominator ≤ D < N ⇒ `Σ_{n≤N}ν ≥ (N−D)Eν`, whatever the cancellation | PROVED (classical tool) |
| Cor 2.3 | majorants built from classes of modulus ≤ N/2 (any coefficients, any evaluation: exact, dispersion/BFI, Kloosterman, Vaaler, floor/ceiling, smooth windows, any Q₀) save `≤ C(log N)^{3/4}(log log N)^{3/4}` for every K2 forced-class mixture | PROVED (K2 proviso: Case A via ElT Prop 1.4) |
| Thm 2.5, Rem 2.6 | **coefficient-budget cap**: any bound B ≥ Σ_{n≤N}ν with `T_> := Σ_{d_i>N/2}|a_i| ≤ cB` saves `≤ log(2+12c) + C(log N)^{3/4}(log log N)^{3/4}`; the same order holds whenever `T_> ≤ (N/24)exp(−C(log N)^{3/4}(log log N)^{3/4})`, whatever B is. Contains K2 Cor 6.1 (c = 1). It contains Cor 2.3 for families with primes ≤ N^A. It does **not** by itself cover hybrid methods that charge large classes their trivial count (D1 of the review) | PROVED (same proviso; family primes ≤ N^A) |
| Prop 3.1 | exact-interval LP value of level-λ hit-pattern majorants depends only on the interval correlation counts `#{n≤N: n ∈ ∩_{ℓ∈T}F_ℓ}`, s(T) ≤ λ (dual: σ ≥ 0 matching moments) | PROVED |
| Prop 3.2 | averaged over shifts, the exact-interval LP value is ≤ the CRT value (Jensen; an average inequality only) | PROVED |
| §3.2 | toy full hit-pattern LPs: interval within 0.005 of CRT up to Q = N; above N the deviations are larger and of either sign, mostly gains; [1,N] is not systematically better than shifted windows | EVIDENCE |
| §3.3 | reading of Thm 2.5's contrapositive: a method escaping it must save on the large-modulus coefficient mass `T_>^*`, which for hit-pattern majorants means counting n ≤ N with prescribed witness sets of combined modulus > N/2 better than termwise (the non-CRT tuple-count door) | Assessment |
| Lemma 4.1, 4.2 | (H_eq) may lose a factor N^{−A}; a window-correlation lower bound for patterns of modulus > N is a *sufficient* condition for it; not needed for majorants built from classes of modulus ≤ N/2 | PROVED; (H_eq) itself CONJECTURE |
| §5 | BV/BFI/DI/Zhang-type inputs, used as remainder estimates for majorants with all moduli ≤ N/2, are capped *whatever their strength* (Cor 2.3, integer avoider count). With large classes present they are capped only when the bound dominates `T_>^*/c` (Thm 2.5). The input that would be needed (high-order ES witness correlations above modulus N) is not known | PROVED (Cor 2.3 / Thm 2.5 parts, integer count only) / Assessment |

**Verdict.** For the integer avoider count, two statements are proved.
In both, ν is a nonnegative majorant of the *whole* avoider set of a K2
forced-class mixture.
* (Cor 2.3) If every class of ν has modulus ≤ N/2, no evaluation of
  Σ_{n≤N}ν beats 3/4. It may be exact, use dispersion or smoothing, and
  the coefficients may be of any size.
* (Thm 2.5, Rem 2.6) Large classes may be present, with family primes
  ≤ N^{O(1)}, provided the method's bound dominates `T_>^*/c`, where
  `T_>^*` is the least coefficient mass on moduli > N/2 over
  representations of ν. Here c may be as large as
  `exp(O((log N)^{3/4}(log log N)^{3/4}))`. Alternatively it suffices that
  `T_>^*` itself is that much below N.

Not covered: methods that save on the large-modulus coefficient mass.
**In particular, a "hybrid" method is not proved to be capped.** By a
hybrid method we mean: any evaluation below N/2, with each class above N/2
charged its trivial count `N/d_i + O(1)`. Its bound is
`Σ_{n≤N}ν + Σ_{d_i>N/2}(|a_i| − a_i r_i)`, which can be ≪ T_> when positive
coefficients sit on large classes that meet [1,N]. No counterexample is
known; this is a proof gap. Also not covered: smooth per-frequency bounds
with large classes (§4, open), prime-only counts beyond NC's prime-slice
results, and majorants that are ≥ 0 only on [1,N]. §3.3 (Assessment)
reads what remains as counting integers ≤ N with prescribed large-modulus
ES witness sets, better than termwise. That is a reformulation, not a
proof that it is hard.

Notation as in `EXCEPTIONAL_NONCRT.md` (NC below), `EXCEPTIONAL_KARY2.md`
(K2) and `EXCEPTIONAL_THETA.md` (ET). A *majorant* of an avoider set 𝒜 is a
finite real combination `ν(n) = Σ_i a_i 1[n ≡ b_i (mod d_i)]` with `ν ≥ 0` on
ℤ and `ν ≥ 1` on 𝒜 (the whole avoider set in ℤ). Its period is `Q`,
`Eν = ν̂(0)` its mean, `ν̂(θ) = E_{n mod Q} ν(n)e(−nθ)`, and every frequency
θ ∈ (1/Q)ℤ/ℤ has a *denominator* `den(θ)` (the order of θ in ℚ/ℤ). The
*level* of ν is K2's: `max_i Σ_{ℓ | d_i, ℓ > W} log ℓ ≤ max_i log d_i`.

## 1. What "inter-frequency cancellation" can mean

Exactly (NC (1.2), (8.1)),

    Σ_{n≤N} ν(n) = N·Eν + Σ_{θ≠0} ν̂(θ) S_N(θ),    S_N(θ) = Σ_{n≤N} e(nθ).   (1.1)

NC Thm 2.3 caps every bound that charges each nonzero frequency separately
with a weight `w(θ) ≥ 1`. A method "exploits cancellation between
frequencies" if it controls the sum in (1.1) better than termwise. We
distinguish four classes.

* **𝓘_exact(𝒞).** For a class 𝒞 of majorants, the bound is the exact value
  `Σ_{n≤N} ν(n)`, ν ∈ 𝒞, however obtained. All inter-frequency
  cancellation is included.
* **𝓘_spec(D).** 𝓘_exact for the majorants whose every nonzero frequency
  has `den(θ) ≤ D`. Equivalently (Lemma 2.1(a)): ν is a combination of
  classes of moduli ≤ D, with coefficients of any size. This is the
  "sieve of level D" with arbitrary remainder evaluation: Selberg Λ²
  `(Σ_{d≤√D}λ_d 1_d)²`, β-sieves of level D, Bombieri–Friedlander–Iwaniec /
  Deshouillers–Iwaniec dispersion over moduli `d ≤ D`, Erdős–Turán/Vaaler
  and per-class floor/ceiling rounding.
* **𝓘_smooth(Φ).** The bound `Σ_n Φ(n/N)ν(n)` with a window
  `Φ ≥ 1_{[1/N,1]}`, evaluated through Poisson, `N Φ̂(0)Eν +
  Σ_{θ≠0} ν̂(θ)W_N(θ)`, either exactly or per frequency (`Σ|ν̂||W_N|`, NC
  §2.5, weights < 1).
* **𝓘_split(D, w).** Exact cancellation among frequencies with
  `den(θ) ≤ D`, and per-frequency weights `w ≥ 1` above D.

**Observation 1.1 (PROVED, trivial).** Without a restriction on 𝒞 the
class 𝓘_exact is not a method but the problem itself. Let the family
be finite with period Q. Then `ν = 1_𝒜` is a majorant in the sense
above, and `Σ_{n≤N} 1_𝒜(n) = #(𝒜 ∩ [1,N])`. So no cap on 𝓘_exact(all)
can exceed the truth. Any theorem about this door must restrict the
spectrum or the structure of ν, or the evaluation. ∎

## 2. Spectrum below N: inter-frequency cancellation is worthless

**Lemma 2.1 (PROVED, routine).**
(a) A Q-periodic function has all nonzero frequencies of denominator ≤ D
iff it is a finite combination of indicators of classes of moduli ≤ D.
(b) If every `d_i ≤ D`, then ν has level ≤ log D.

*Proof.* (a) `1[n ≡ b (d)] = d^{−1}Σ_{h mod d} e(h(n−b)/d)` has frequencies
`h/d`, of denominator dividing d. Conversely,
`e(na/q) = Σ_{b mod q} e(ab/q)1[n ≡ b (q)]`. (b) Each term's level is at most
`Σ_{ℓ|d_i} log ℓ ≤ log d_i`. ∎

**Theorem 2.2 (Selberg-minorant lower bound; PROVED).** Let ν ≥ 0 on ℤ be
periodic, and let every nonzero frequency θ of ν satisfy `den(θ) ≤ D`.
Then for every N ≥ 1,

    Σ_{n=1}^{N} ν(n) ≥ (N − D)·Eν.                                   (2.1)

*Proof.* Let `I = [1/2, N + 1/2]`, so `I ∩ ℤ = {1,…,N}` and |I| = N. Put
δ = 1/D. Selberg's minorant (Vaaler, *Some extremal functions in Fourier
analysis*, Bull. AMS 12 (1985), the section on Selberg's functions;
Montgomery, *Ten lectures on the interface between analytic number theory
and harmonic analysis*, Ch. 1) is an integrable F: ℝ → ℝ with
* `F(x) ≤ 1_I(x)` for all real x;
* `F̂(ξ) = ∫F(x)e(−xξ)dx` continuous and supported in `[−δ, δ]`;
* `F̂(0) = |I| − 1/δ = N − D`.

F is entire of exponential type 2πδ and in L¹(ℝ), so `Σ_n |F(n)| < ∞`
(Plancherel–Pólya). The periodisation `P(θ) = Σ_k F̂(k − θ)` is a finite sum
of continuous functions, with Fourier coefficients `F(n)`; these are
absolutely summable, so `Σ_{n∈ℤ} F(n)e(nθ) = P(θ)` for every θ (Poisson). If θ ∉ ℤ has
`den(θ) = q ≤ D`, then `‖θ‖ ≥ 1/q ≥ δ`, so every `|k − θ| ≥ δ` and the sum
is 0 (F̂ is continuous and vanishes outside (−δ, δ), hence also at ±δ).
For θ ∈ ℤ it is `F̂(0)`. Since ν is a finite trigonometric sum,

    Σ_n F(n)ν(n) = Σ_θ ν̂(θ) Σ_n F(n)e(nθ) = (N − D)·Eν.

Finally `F(n) ≤ 1_{[1,N]}(n)` and `ν(n) ≥ 0` for every n ∈ ℤ, so
`Σ_{n≤N} ν(n) ≥ Σ_n F(n)ν(n)`. ∎

*Remarks.* (i) The hypothesis ν ≥ 0 is used at every integer, including
those outside [1,N]: this is where "majorant on ℤ" enters (K2 §6 item 3
excludes majorants that are ≥ 0 only on [1,N]). (ii) (2.1) is the
minorant counterpart of the Selberg extremal functions behind the large
sieve. The large-sieve constant `N − 1 + δ^{−1}` comes from the *majorant*;
the minorant used here has `F̂(0) = |I| − δ^{−1}` with `|I| = N`.
It is classical in spirit; the point here is its consequence for the
sieve-limit programme. (iii) For periodic ν with period Q ≤ D the
elementary bound `Σ_{n≤N}ν ≥ ⌊N/Q⌋·Q·Eν` gives the same thing. Theorem 2.2
needs only the denominators, not the period, which can be `e^{cD}`.

**Corollary 2.3 (𝓘_spec(N/2) is capped at 3/4; PROVED, the Case-A part
via K2 Thm 5.1's use of ElT Prop 1.4).** Let 𝔊 be any finite family of
ℛ(M)-, (a,D)-, Case-A and selector classes (K2 Def 2.0, arbitrary moduli,
any primes), 𝒜 = 𝒜(𝔊), and let ν be a majorant of 𝒜 that is a
combination of classes of moduli ≤ D with `D ≤ N/2`. Then, for N large,

    Σ_{n≤N} ν(n) ≥ (N/2)·exp(−C(log N)^{3/4}(log log N)^{3/4}),

and if all moduli of 𝔊 satisfy `G ≤ P(G)^{1+B}`, the exponent is
`C_B(log N)^{3/4}`. Coefficient sizes, the number of classes, and the way
the interval sum is evaluated are unrestricted.

*Proof.* By Lemma 2.1, ν has level ≤ log D ≤ log N, and its spectrum has
denominators ≤ D. K2 Thm 5.1 (resp. 5.2) gives
`Eν ≥ exp(−C λ^{3/4}(log λ)^{3/4})` with λ = max(log N, λ₀). Theorem 2.2
gives `Σ_{n≤N}ν ≥ (N − D)Eν ≥ (N/2)Eν`. ∎

**What this closes.** Every sieve whose majorant has level `D ≤ N/2`
(after expanding products of classes into lcm-moduli), with *any*
evaluation of the remainder terms. In particular:
* Selberg Λ² `(Σ_{d ≤ √D} λ_d 1_{d})²` and β-sieves of level D < N/2,
  with remainders evaluated by any cancellation over d;
* BFI/Deshouillers–Iwaniec dispersion and Kloosterman-sum cancellation over
  moduli `d < N/2`;
* Erdős–Turán/Vaaler ψ-rounding and per-class floor/ceiling rounding, at
  level < N/2 (NC review N2 left these open at all levels);
* smooth windows `Φ(n/N) ≥ 1_{[1,N]}(n)` (Φ ≥ 0) with all moduli ≤ N/2, since
  `Σ Φ(n/N)ν(n) ≥ Σ_{n≤N}ν(n)`. This includes non-hit-pattern majorants and
  Q₀ > 1, so NC §2.5 (H_eq) is not needed below level N/2.

So in the integer problem *level of distribution below N is free*: any
inter-frequency gain must come from frequencies of denominator ≳ N, i.e.
from products of classes whose combined modulus exceeds N. On such a
class an n ≤ N is unique if it exists, and the "remainder" is the 0/1
question whether that n is ≤ N. Combined with NC Lemma 8.2 (Case-B classes
of modulus > M₀ ≍ N² are empty on [1,N]), the door for single Case-B
classes is the modulus window `(N/2, M₀]`; for products it is combined
moduli above N/2.

### 2.1 Large classes under a coefficient budget

Theorem 2.2 allows an extension: classes of modulus > N/2 may be present,
provided the method's bound dominates a multiple of their total coefficient
mass (hypothesis (2.2); paying the trivial count per class is *not*
enough, Rem 2.6).

**Lemma 2.4 (PROVED).** Let F be the minorant of Theorem 2.2 (for N and
D < N). For every class `b mod d`,

    | Σ_{n ≡ b (d)} F(n) − (N − D)/d | ≤ 2(N + D)/D,

and the left side is 0 if d ≤ D.

*Proof.* Poisson along the progression:
`Σ_m F(b + md) = d^{−1} Σ_{k∈ℤ} F̂(k/d) e(kb/d)`. The k = 0 term is
`(N−D)/d`. F̂ vanishes outside (−1/D, 1/D), so at most `2d/D` nonzero k
contribute; none if d ≤ D. Each `|F̂(k/d)| ≤ ‖F‖₁`. Write `F = 1_I − g`
with `g ≥ 0`, `∫g = |I| − F̂(0) = D`; then `|F| ≤ 1_I + g` and
`‖F‖₁ ≤ N + D`. ∎

**Theorem 2.5 (coefficient-budget cap with free small moduli; PROVED, Case-A
part via K2 Thm 5.1).** Let 𝔊 be any finite family of ℛ(M)-, (a,D)-,
Case-A and selector classes with every prime of every modulus `≤ N^A`.
Let `ν = Σ_i a_i 1[n ≡ b_i (d_i)]` be a majorant of 𝒜(𝔊). Put
`T_> = Σ_{i: d_i > N/2} |a_i|` (coefficients as written, no merging
needed). Suppose a method produces a bound B with

    B ≥ Σ_{n≤N} ν(n)   and   T_> ≤ c·B   (c ≥ 0),                   (2.2)

and `B = N e^{−s}`. Then, for N ≥ N₀(A) (N₀ and C_A independent of c),

    s ≤ log(2 + 12c) + C_A (log N)^{3/4} (log log N)^{3/4},

and with `G ≤ P(G)^{1+B₀}` for all moduli of 𝔊, `s ≤ log(2+12c) + C_{A,B₀}(log N)^{3/4}`.

*Proof.* *Interval side.* ν ≥ 0 on ℤ and `F ≤ 1_{[1,N]}` on ℤ give
`Σ_{n≤N}ν ≥ Σ_n F(n)ν(n)`. Take F with D = N/2. By Lemma 2.4,
term by term (classes of modulus ≤ N/2 contribute no error),
`Σ_n F(n)ν(n) ≥ (N/2)Eν − 6T_>`. With (2.2),
`B ≥ (N/2)Eν − 6cB`, so `Eν ≤ (2+12c)B/N = (2+12c)e^{−s}`.

*Mean side.* If `s ≤ log(2+12c)` there is nothing to prove. Otherwise
`B < N/(2+12c)`, so `T_> ≤ cB < N/12`, and `Eν < 1`. Put `S = log(1/Eν) > 0`;
so `s ≤ S + log(2+12c)`. Follow K2
Cor 6.1's proof, with one change. The projection `ν̄` to the family modulus
does not raise moduli or coefficient sizes, so the terms of ν̄ of level
`> log(N/2)` have coefficient sum ≤ T_>. ET Lemma 2.9's proof alters only
terms of level > λ, so its conclusion holds with T replaced by the
coefficient sum of those terms. For `λ ≥ log N` this is ≤ T_>.
With `Λ₀ = A log N` and
`λ = max{λ₀, log N, Λ₀ + log(max(T_>,1)) + S} ≤ (A+1)log N + S + λ₀`, we get
a majorant of level λ with mean `≤ 2Eν`. K2 Thm 5.1 (resp. 5.2) bounds S
exactly as in K2 Cor 6.1's case analysis. ∎

**Remark 2.6 (strength and scope; PROVED).**
* *Representations.* T_> depends on how ν is written. A class of modulus
  ≤ N/2 splits into k classes of modulus kd > N/2, which inflates T_>
  without changing ν. Theorem 2.5 holds for every representation, so it
  applies with `T_>^* = inf_{repr} Σ_{d_i>N/2}|a_i|`.
* *T_>/N, not T_>/B, is binding.* Put
  `S_max = C_A(log N)^{3/4}(log log N)^{3/4}`. The mean side caps
  `S = log(1/Eν) ≤ S_max` whenever `T_> ≤ N`, whatever B is. Then
  `B ≥ (N/2)e^{−S} − 6T_>`. So if `T_>^* ≤ (N/24)e^{−S_max}`, then
  `B ≥ (N/4)e^{−S_max}` and the saving is ≤ `S_max + log 4`. Equivalently,
  c in (2.2) may be as large as `exp(O(S_max))` without changing the
  order of the cap.
* *Contains:* K2 Cor 6.1 (`B ≥ N·Eν + Σ_i|a_i| ≥ Σ_{n≤N}ν` and `B ≥ T_>`,
  c = 1). It also contains Cor 2.3, but only for families with primes
  ≤ N^A. That hypothesis serves only Λ₀ in ET Lemma 2.9, which is idle when
  `T_> = 0`; Cor 2.3 itself needs no prime bound.
* *Does not contain (proof gap, not a refutation):* hybrid methods that
  evaluate the classes of modulus ≤ N/2 in any way and charge each class of
  modulus > N/2 its trivial count. With `r_i = #{n≤N: n≡b_i (d_i)} − N/d_i`,
  their bound is `B_hyb = Σ_{n≤N}ν + Σ_{d_i>N/2}(|a_i| − a_i r_i)`. The last
  sum is ≈ `a_i N/d_i` for a positive coefficient on a class with `d_i ≫ N`
  that meets [1,N], so B_hyb can be ≪ T_>. Then (2.2) fails for every
  useful c. The mean side also needs `log T_> = O(log N)`, which is not
  automatic for such methods. In natural sieves positive large-modulus
  terms typically miss [1,N] and are charged ≈ |a_i|. A route to closing
  the gap (review numerics only) is to show
  `Σ_{n≡b (d)}(1_{[1,N]} − F)(n) ≤ 1 + N/(2d)` for d > N, together with
  `F ≥ 0` on [1,N]. Not attempted here.
* Smooth windows `Φ(n/N) ≥ 1_{[1,N]}(n)`: covered when the bound
  dominates `T_>^*/c` (Rem 2.6 bullet 2), or when all moduli are ≤ N/2
  (Cor 2.3).

**What is left of the door (Assessment).** A method escapes Theorem 2.5
only if its bound B is much smaller than `T_>^*` (and `T_>^*` is not tiny
compared with N, Rem 2.6). How Σ_{n≤N}ν splits between small and large
classes depends on the representation. Such a class `b mod d` has `N/d + r` elements in
[1,N], with `r ∈ (−1, 1)`. For d > N its count is `1[b̃ ≤ N]` (b̃ the least
positive residue). So the method must evaluate

    Σ_{i: d_i > N/2} a_i · ( #{n ≤ N : n ≡ b_i (d_i)} − N/d_i )       (2.3)

with cancellation between the classes, to accuracy `≪ B ≪ T_>^*`. For
d_i > N this is a statement about *which* classes of large modulus meet
[1,N]. For hit-pattern majorants those classes are intersections of
forced classes, and (2.3) is a weighted count of integers n ≤ N with
prescribed witness patterns. §3 develops this.

## 3. Above N/2: what an exact interval count actually needs

### 3.1 LP duality for hit-pattern majorants

Take a finite family of classes `F_ℓ mod ℓ` (distinct primes ℓ ∈ 𝒫,
`0 < |F_ℓ| < ℓ`, Q₀ = 1 for simplicity), hit pattern
`x(n) = (1[n mod ℓ ∈ F_ℓ])_ℓ`, and level `s(T) = Σ_{ℓ∈T} log ℓ`. A
*hit-pattern majorant of level λ* is `ν(n) = G(x(n))` with G multilinear,
`G = Σ_{s(T)≤λ} c_T x^T`. By CRT every pattern occurs in ℤ, so

    ν ≥ 0 on ℤ  ⟺  G ≥ 0 on the whole cube {0,1}^𝒫.                (3.1)

This is the decisive constraint: G may not exploit patterns that are
absent from [1,N], since they occur elsewhere in ℤ. Write π_N for the law
of x(n), n uniform in [1,N], and `m_T(π) = E_π x^T`.

**Proposition 3.1 (PROVED; finite LP duality).** Put
`V_N(λ) = min{ E_{π_N} G : G of level ≤ λ, G ≥ 0 on the cube, G(0) ≥ 1 }`,
so `N·V_N(λ)` is the best exact interval count over level-λ hit-pattern
majorants. Then

    V_N(λ) = max{ σ(0) : σ ≥ 0 on the cube, m_T(σ) = m_T(π_N) ∀ s(T) ≤ λ }.

In particular, `V_N(λ)` depends on [1,N] only through the correlation
counts `N·m_T(π_N) = #{n ≤ N : n ∈ F_ℓ (mod ℓ) ∀ℓ ∈ T}`, s(T) ≤ λ. The
same holds with π_N replaced by the CRT law (product Bern(|F_ℓ|/ℓ)),
giving `V_CRT(λ)`. *For the ES families* of NC Cor 2.5 / K2 Thm 5.1
(not for arbitrary F_ℓ: one prime with `|F_ℓ| = ℓ − 1` already gives
`V_CRT ≤ 1/ℓ`), `V_CRT(λ) ≥ e^{−Cλ^{3/4}}` up to the stated log factors.

*Proof.* G ≥ 0 together with G(0) ≥ 1 is G ≥ 1_{x=0}. The primal
`min ⟨π_N, G⟩, G ∈ span{x^T}, G ≥ 1_{0}` is feasible (G ≡ 1) and bounded
(by 0). LP duality gives `max ⟨σ, 1_0⟩` over σ ≥ 0 with `⟨σ − π_N, x^T⟩ = 0`
for every admissible T. ∎

**Proposition 3.2 (exact counts beat CRT on average over shifts; PROVED).**
Let `π_N^{(t)}` be the law of x(n) for n uniform in `[t+1, t+N]`. Then
`V(π) := min_G E_π G` is concave in π, and `avg_{t mod Q} π_N^{(t)}` is the
CRT law (Q = Πℓ). Hence

    avg_t V_N^{(t)}(λ) ≤ V_CRT(λ)    for every λ.

*Proof.* A minimum of linear functionals is concave; Jensen. ∎

So *on average over shifts* an exact interval count at level λ does at
least as well as the CRT sieve. This is a generic effect of fixing one
window, not an arithmetic feature of [1,N]. (Jensen gives an average
inequality only, not a gain at every shift.) For `λ = ∞` the value is the
void `π_N^{(t)}(0)`, whose average is the CRT density `Π(1 − p_ℓ)` (prime
moduli). *Heuristically*, for the full ES family up to N^{O(1)} the CRT
avoider density is `e^{−c(log N)^3}`-small (mean witness mass ≍ (log N)³;
composite-modulus classes are not a product `Π(1−p_ℓ)`, so this is not
proved here), far below `e^{−(log N)^{3/4}}`. So in the LP
sense exact counts at high level face no barrier from (3.1) alone: this is
Observation 1.1 seen through the LP. The barrier is evaluation: knowing
the interval counts `N·m_T(π_N)` for T of combined modulus `Π_T ℓ > N/2`.
Theorem 2.5 covers every method that charges those terms at coefficient
cost. (Lemma 2.4 gives exact CRT values for *minorant-weighted*
progression sums, not for the sharp counts `N·m_T`.)

### 3.2 Numerics (EVIDENCE; toy family)

`scripts/interfreq_hitpattern_lp.py` solves V for *all* hit-pattern
majorants (the full monomial basis up to level Q, G ≥ 0 on all 2^m
patterns: HiGHS, < 5 s). Family: the 12 primes `3 ≤ ℓ ≤ 79`, ℓ ≡ 3 (4),
`F_ℓ = ℛ(ℓ)`. N = 3000, all n in `[t+1, t+N]`. The table gives savings
`−log V` (data: `data/interfreq/hitpattern_lp_N3000_m12.txt`).

| Q | CRT | [1,N] | t = 10⁹+7 | t = 5·10⁹ |
|---|---|---|---|---|
| N^{1/2} | 0.965 | 0.965 | 0.965 | 0.966 |
| N | 1.668 | 1.671 | 1.669 | 1.664 |
| N^{3/2} | 2.324 | 2.306 | 2.343 | 2.346 |
| N² | 2.675 | 2.808 | 2.916 | 3.015 |
| ∞ (void) | 3.152 | 2.976 | 3.178 | 3.270 |

* Up to Q = N the interval LP is within 0.005 of the CRT LP, at every
  shift. Theorem 2.2 constrains this only for Q < N; at Q = N it is
  vacuous (N − D = 0), and at Q = N^{1/2} it allows an excess ≤ 0.018.
* Above N the deviations grow and have either sign. At Q = N^{3/2}, [1,N]
  saves less than CRT (2.306 < 2.324) and the shifts save more. At Q = N²
  all three save more (Prop 3.2 predicts this only on average). At full
  level [1,N] saves less than CRT (void 0.051 versus CRT 0.043). The squares
  are avoiders, which is a plausible but unverified explanation: there are
  54 squares ≤ 3000 against an excess of about 25 voids. [1,N] saves the
  most at Q = N (1.6713 vs 1.6690, 1.6642) and ties at Q = N^{3/4}. It is
  not the best at Q ≥ N^{5/4}. There is no systematic advantage of [1,N].
* Prime samples (`mode=prime`, about 200–400 points) deviate more, already
  near Q = N. The relevant scale is the sample size N/log N, and
  small-sample overfitting at high level grows.

The toy savings are tiny (m = 12). The table illustrates the mechanism.
It is no evidence about the asymptotic exponent.

### 3.3 The door, reduced (Assessment)

This subsection is a reading, not a theorem. It interprets the
contrapositive of Theorem 2.5 (with D1/D2 of the review: only methods
whose bound is ≪ T_>^* escape) and combines it with NC Thm 8.1/Cor 8.3.
Those two hold only for prime-slice / Case-B hit-pattern families, a
narrower scope than K2 mixtures. Read this way, a method that beats
θ = 3/4 through inter-frequency cancellation must, for some majorant and
representation, evaluate

    Σ_{i: d_i > N/2} a_i ( #{n ≤ N : n ≡ b_i (d_i)} − N/d_i )         (3.2)

with an error far below `T_>^*`. For hit-pattern
majorants the classes are intersections ∩_{ℓ∈T} F_ℓ with `Π_T ℓ > N/2`.
Then (3.2) is a signed count of integers n ≤ N carrying a prescribed set of
ES witnesses, i.e. correlations of the Elsholtz–Tao witness function f(n),
non-trivially in the coefficients c_T. NC Thm 8.1 adds a quantitative
requirement. Either Fourier mass sits above level `c s^{4/3}`; for
hit-pattern majorants on [1,N] with moduli ≤ M₀ ≍ N² (NC Cor 8.3) that
means correlations of order `|T| ≥ c(log N)^{4θ/3−1}`. Or the interval
count is ≤ ½ of the CRT mean. In both cases the input is a count of
multi-witness integers ≤ N, done better than termwise. This is the
"non-CRT tuple count" door (c′) of NC §6. **Assessment: the inter-frequency door is not a
separate door. Below N/2 it is closed (Cor 2.3). With large classes it is
closed for methods paying ≳ T_>^*/c (Thm 2.5). What remains is the
tuple-count door.**

## 4. Smooth per-frequency rounding and (H_eq)

Setting of NC §2.5: Q₀ = 1, hit-pattern majorant ν with Walsh coefficients
`d_S`, smooth window Φ ≥ 0 (Schwartz, or compactly supported), bound
`B_Φ = N Φ̂(0) Eν + Σ_S |d_S| M_S` (with `Φ(n/N) ≥ 1_{[1,N]}(n)`), where
`M_S = Σ_{θ∈Θ_S} m_S(θ)|W_N(θ)|`, `m_S(Σ h_ℓ/ℓ) = Π_S |1̂_{F_ℓ}(h_ℓ)|`,
and `W_N(θ) = Σ_n Φ(n/N) e(nθ)`.

**Status after §2.** By Cor 2.3, if `Φ(n/N) ≥ 1_{[1,N]}(n)` on ℤ and ν is
built from classes of modulus ≤ N/2 (a denominator condition; a level
bound alone does not control the Q₀ part), smooth windows give nothing,
without (H_eq), for every Q₀. In NC §2.5's setting (Q₀ = 1) (H_eq) is
needed only for S of large Walsh level s(S); since `s_ℓ ≤ log ℓ` these
have `Π_S ℓ ≥ e^{s(S)}`.

**Lemma 4.1 (polynomial loss suffices; PROVED).** In NC §2.5, (2.6) may be
replaced by

    (H_eq^A)   M_S ≥ N^{−A} Π_{ℓ∈S}(1 − p_ℓ)   for all S with s(S) > λ_A := (A+2) log N,

for any fixed A ≥ 0. Then, for the Cor 2.5 families, every bound `B_Φ < N`
saves `≤ C(A)(log N)^{3/4} + log(P/φ(P))`.

*Proof.* Use weights `s_ℓ = log(3/(8p_ℓ⁺))`. Then `2p_ℓ ≤ (3/4)e^{−s_ℓ}`,
so `Π_S 2p_ℓ(1−p_ℓ) ≤ e^{−s(S)}Π_S(1−p_ℓ) ≤ e^{−s(S)}N^A M_S`, and also
`Π_S (4/3)p_ℓ ≤ Π_S 2p_ℓ(1−p_ℓ)` because p_ℓ ≤ 1/4. Hence the tails of NC
Prop 2.1 at level λ ≥ λ_A satisfy
`r₀, r₁ ≤ e^{−λ}N^A Σ_S|d_S|M_S ≤ e^{−λ}N^{A+1}`. Choose `λ = λ_A`. Then
`r₀, r₁ ≤ 1/N`, and `Φ̄(λ_A) ≤ C(A)(log N)^{3/4} = o(log N)` by NC Cor 2.5,
so `r₀, r₁ ≤ e^{−Φ̄(λ_A)}/4` for N ≥ N₀(A). Conclude as in NC Cor 2.4. ∎

**Lemma 4.2 (a sufficient condition for H_eq; PROVED).** For
every S and every shift t ∈ ℤ,

    M_S ≥ | Σ_n Φ(n/N) y^S(n − t) |,   y^S(n) = Π_{ℓ∈S}(1[n mod ℓ ∈ F_ℓ] − p_ℓ).

*Proof.* `y^S` has Fourier transform `Π_S 1̂_{F_ℓ}(h_ℓ)` on Θ_S and 0
elsewhere. With `c(θ) = e(−tθ)·Π 1̂_{F_ℓ}(h_ℓ)/|1̂_{F_ℓ}(h_ℓ)|` (any unimodular
value where 1̂ = 0), `|c| ≤ 1` and
`Σ_θ c(θ)m_S(θ)W_N(θ) = Σ_n Φ(n/N)y^S(n − t)`. Bound by `Σ m_S|W_N| = M_S`. ∎

So (H_eq^A) follows if, for each S of level > (A+2)log N, *some* window
of length ≍ N carries a centred S-pattern correlation of size
`≥ N^{−A}Π(1−p)`. Placing a point of ∩_S F_ℓ (it exists by CRT) inside the
window gives a main term `Φ(n₀/N)Π_S(1−p_ℓ)`. The other points of the
window contribute `±Π_T(1−p)Π_{S∖T}p` according to their hit sets T ⊂ S.
To control them one needs the distribution of hit sets of combined modulus
> N in short windows: the §3 data again. Neither a proof nor a
counterexample was found.

**Assessment (heuristic).** Lemma 4.2 has no converse: a large ℓ¹
quantity M_S need not give a large correlation at any shift. So (H_eq) is
not shown to be equivalent to a §3.3-type statement, only implied by
one. Both concern patterns of combined modulus > N in windows of length
N. **Status: (H_eq) remains CONJECTURE.** It is
superseded below level N/2 (Cor 2.3), and the polynomial-loss form
(H_eq^A) suffices (Lemma 4.1).

## 5. Which arithmetic input would be needed, and is any known?

**(i) Level-of-distribution / dispersion inputs at moduli ≤ N/2.**
Bombieri–Vinogradov, BFI, Deshouillers–Iwaniec, Zhang/Polymath and
Maynard-type well-factorable estimates control remainders
`Σ_{d≤D} λ_d r_d` for moduli `d ≤ D < N` (for the integers, or level
`N^{1/2+δ}`, `N^{4/7}` for primes). For the integer avoider count, Cor 2.3 shows
that if every class of the majorant has modulus ≤ N/2, then *any*
evaluation, however strong (even exact), is capped at
`(log N)^{3/4}(log log N)^{3/4}`. With classes above N/2 present,
Theorem 2.5 gives the same cap provided the bound dominates `T_>^*/c`
(Rem 2.6). That is not proved for hybrid methods that charge large
classes only their trivial count (Rem 2.6, last bullet). So no estimate
of this type helps when used on majorants of modulus ≤ N/2, or inside a
method whose bound dominates T_>^*/c. It could matter only inside a method
that also saves on the large-modulus mass. For prime-only majorants, NC Thm 3.2/Rem 3.4 already
showed level `N^{O(1)}` equidistribution is capped. Theorem 2.5 does not
extend this to prime counts (Lemma 2.4 is a statement about integers).

**(ii) What would be needed.** A non-trivial evaluation of (3.2): signed
counts of n ≤ N lying in intersections of forced classes with combined
modulus > N/2. For Case-B classes on [1,N] a hit by `ℛ(M)`, M > N/2, means
`n + 4D = aM` with a small cofactor `a ≤ (N+4D)/M`. Switching to the
complementary divisor turns it into the (a,D)-class
`n ≡ −(4D + a) (mod 4a·g(D))` (NC Lemma 8.2; ET Lemma 3.2). Its modulus is
`≤ 8⌊(N+1)/3⌋² ≍ N²`, and it is < N/2 only when `a·g(D) < N/8`. Caveat: the
unrestricted (a,D)-class has *more* hits than the original classes, even
inside [1,N]. Example: N = 10, class `3 mod 7` (M = 7, D = 1) hits n = 3
with a = 1, and the switched class `3 mod 4` also hits n = 7. So switching
enlarges the family unless the original restrictions on M are kept, and
then the moduli are no longer small. A method may of course use the
(a,D)-classes from the start; those of modulus ≤ N/2 are capped by
Theorem 2.5 (K2 covers (a,D)-classes). Also, a large *combined* modulus
does not force each individual witness modulus to be large. What
remains is to count integers n ≤ N with **k simultaneous witnesses of
large modulus**. By NC Thm 8.1(H) this needs `k ≳ (log N)^{4θ/3−1}`
(prime-slice setting), or else, at bounded k, an interval deficit
≥ ½ against the CRT mean.

**(iii) Known results.** For k = 1 (first moments of f(n)) Elsholtz–Tao
give asymptotics of the right order, and ET Thm 1.8 the typical size. Their
Remark 1.3 calls second and higher moments out of reach. We know no
estimate for correlations of the ES witness function of growing order, nor
any Type I/II decomposition of the forced-class indicator above modulus N.
The interval deficit is not seen numerically: NC §8.3, and §3.2 here,
where [1,N] saves no more than shifted intervals. **Assessment: no known
technique supplies the input; the door stays open only formally.**

## Replay

```
PYTHONPATH=scripts uv run --with scipy python scripts/interfreq_selberg_check.py > data/interfreq/selberg_check.txt   # Thm 2.2 LP check, ~1 min, <1 GB
for off in 0 1000000007 5000000000; do uv run --with scipy python scripts/interfreq_hitpattern_lp.py 3000 12 all 3 $off; done > data/interfreq/hitpattern_lp_N3000_m12.txt
for off in 0 1000000 2000000; do uv run --with scipy python scripts/interfreq_hitpattern_lp.py 3000 12 prime 3 $off; done >> data/interfreq/hitpattern_lp_N3000_m12.txt   # §3.2, seconds each, <2 GB
```

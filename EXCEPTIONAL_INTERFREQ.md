# EXCEPTIONAL_INTERFREQ — the inter-frequency cancellation door (task O18)

Status: **in progress (O18).** Labels follow `DISCOVERIES.md`. PROVED means
proved in this file, internal checks only, not refereed.

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
analysis*, Bull. AMS 12 (1985), Thm 9 and §5; Montgomery, *Ten lectures*,
Ch. 1) is an integrable F: ℝ → ℝ with
* `F(x) ≤ 1_I(x)` for all real x;
* `F̂(ξ) = ∫F(x)e(−xξ)dx` continuous and supported in `[−δ, δ]`;
* `F̂(0) = |I| − 1/δ = N − D`.

F is of exponential type 2πδ and `F(x) = O(1/(1+x²))`, so Poisson summation
holds: `Σ_{n∈ℤ} F(n)e(nθ) = Σ_{k∈ℤ} F̂(k − θ)`. If θ ∉ ℤ has
`den(θ) = q ≤ D`, then `‖θ‖ ≥ 1/q ≥ δ`, so every `|k − θ| ≥ δ` and the sum
is 0 (F̂ is continuous and vanishes outside (−δ, δ), hence also at ±δ).
For θ ∈ ℤ it is `F̂(0)`. Since ν is a finite trigonometric sum,

    Σ_n F(n)ν(n) = Σ_θ ν̂(θ) Σ_n F(n)e(nθ) = (N − D)·Eν.

Finally `F(n) ≤ 1_{[1,N]}(n)` and `ν(n) ≥ 0` for every n ∈ ℤ, so
`Σ_{n≤N} ν(n) ≥ Σ_n F(n)ν(n)`. ∎

*Remarks.* (i) The hypothesis ν ≥ 0 is used at every integer, including
those outside [1,N]: this is where "majorant on ℤ" enters (K2 §6 item 3
excludes majorants that are ≥ 0 only on [1,N]). (ii) (2.1) is the
minorant half of the Selberg/Montgomery–Vaughan large sieve (`N − 1 + δ^{−1}`).
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
* smooth windows Φ ≥ 1_{[1,N]} at level < N/2, since
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

# EXCEPTIONAL_LARGESIEVE2 — the remaining large-sieve and prime-law escapes (task O27)

Status: **in progress (checkpoint 1 being written).** Labels as in
`DISCOVERIES.md`. Notation: LS = `EXCEPTIONAL_LARGESIEVE.md`, K2 =
`EXCEPTIONAL_KARY2.md`, EK = `EXCEPTIONAL_KARY.md`, PL =
`EXCEPTIONAL_PRIMELAW.md`, ET = `EXCEPTIONAL_THETA.md`.

Throughout, 𝔊 is a finite mixture of ℛ(M)-, (a,D)-, Case-A and selector
classes with arbitrary moduli (K2 Def. 2.0), `𝒜 = 𝒜(𝔊) ⊂ ℤ` its avoider
set, `M₀` the lcm of its moduli. "Level" means W-rough level,
`λ(d) = Σ_{ℓ | d, ℓ > W} log ℓ`, with W the absolute constant of K2
Thm 5.1. `S(λ) := C λ^{3/4}(log λ)^{3/4}` denotes the right side of K2
Thm 5.1 (`λ ≥ λ₀`), and `S_B(λ) = C(B)λ^{3/4}` that of K2 Thm 5.2.

## 1. The comparison measure (LP dual of K2 Thm 5.1)

Fix a finite set 𝒟 of moduli, all of level `≤ λ` and containing 1, and
let `M'` be a common multiple of `M₀` and of all `d ∈ 𝒟`. Write `V_𝒟` for
the real span of the class indicators `1[n ≡ b (mod d)]`, `d ∈ 𝒟`, viewed
as functions on `ℤ/M'`; `E_U` is the uniform mean on `ℤ/M'`.

**Lemma 1.1 (comparison measure; PROVED, conditional on K2 Thm 5.1 —
i.e. with its Case-A proviso).** For `λ ≥ λ₀` there is a probability
measure `π = π_𝒟` on `ℤ/M'`, supported on `𝒜 mod M'`, such that

    E_π f ≤ e^{S(λ)} E_U f     for every f ∈ V_𝒟 with f ≥ 0 on ℤ/M'.      (1.1)

Under bounded B (`G ≤ P(G)^{1+B}` for every modulus of 𝔊), `S` may be
replaced by `S_B`.

*Proof.* Consider the LP

    m* = min { E_U ν : ν ∈ V_𝒟,  ν(x) ≥ 1_𝒜(x) for all x ∈ ℤ/M',  ν ≥ 0 }.

It is feasible (`ν ≡ 1`, as `1 ∈ 𝒟`) and bounded below by 0, so finite;
every feasible ν is a majorant of level `≤ λ` of 𝒜 in the sense of K2
Thm 5.1, so `m* ≥ e^{−S(λ)}`. Write the constraints as `ν(x) ≥ b(x)`
with `b = 1_𝒜 ≥ 0` (the constraints `ν ≥ 0` off 𝒜 are the same family
with `b(x) = 0`). LP duality (finite dimension, primal feasible and
bounded) gives multipliers `μ(x) ≥ 0` with

    Σ_x μ(x) ν(x) = E_U ν  for every ν ∈ V_𝒟,     and    Σ_x μ(x) b(x) = μ(𝒜) = m*.

(Stationarity of the Lagrangian `E_Uν − Σ_x μ(x)(ν(x) − b(x))` in the free
variable `ν ∈ V_𝒟` is the first identity.) Put `π = μ|_𝒜 / μ(𝒜)`. For
`f ∈ V_𝒟` with `f ≥ 0` everywhere,
`E_π f = Σ_{x∈𝒜} μ(x)f(x)/m* ≤ Σ_x μ(x)f(x)/m* = E_U f/m* ≤ e^{S(λ)}E_U f`. ∎

*Remarks.* (i) Lemma 1.1 is **equivalent** to K2 Thm 5.1 on `V_𝒟`
(conversely, (1.1) with `f = ν` gives `1 ≤ E_πν ≤ e^S E_Uν`). Its use
is that one measure serves every nonnegative test function at once,
including test functions that are not majorants. (ii) Only the
existence of π is used below, not its construction; the explicit KARY
law (EK Thm 4.1: the sequential law `Q'` reweighted by `e^{−ΣΦ}` and
restricted to 𝒜) is one admissible choice, used in §6. (iii) Fibres:
for `Q₀ | M'` and a class `c mod Q₀` with `π(c) > 0`, the conditional
law of `m = (n − c)/Q₀` given `n ≡ c (Q₀)` is supported on
`𝒜_c = {m : c + Q₀m ∈ 𝒜}`, and for every `f ≥ 0` in the span of classes
in m whose moduli d have `Q₀d` ∈ 𝒟-span (level `λ(Q₀) + λ(d) ≤ λ`),

    E_{π_c} f ≤ e^{S(λ)} E_U f / (Q₀ π(c)),                              (1.2)

since `n ↦ f((n−c)/Q₀)1[n ≡ c (Q₀)]` is `≥ 0`, lies in `V_𝒟` (a class
`m ≡ b (d)` becomes `n ≡ c + Q₀b (Q₀d)`), and has U-mean `E_U f/Q₀`.
Also `π(c) ≤ e^{S(λ)}/Q₀` by (1.1) with `f = 1[n ≡ c (Q₀)]`.

**Lemma 1.2 (unit-measure version; PROVED, conditional on PL Thm 3.1).**
Let `E*` be uniform on `(ℤ/M')^×`. For `λ ≥ λ₀` there is a probability π*
on `(ℤ/M')^× ∩ 𝒜` with `E_{π*} f ≤ e^{S(λ)} E* f` for every `f ∈ V_𝒟`
with `f ≥ 0` on `(ℤ/M')^×`.

*Proof.* Identical, with the LP of PL (1.1) (constraints on units only)
and PL Thm 3.1 in place of K2 Thm 5.1. ∎

## 2. Periodic Bessel systems: twisted, multiplicative, hybrid (escape 3)

**Definition 2.1.** A *periodic Bessel system of length N* is a finite
family `Φ = (φ_j)_{j∈J}` of functions `ℤ → ℂ`, `φ_j` periodic with
period `d_j`, and a constant `Δ > 0` such that, for every interval I of
N consecutive integers and all `a ∈ ℂ^I`,

    Σ_j | Σ_{n∈I} a_n conj(φ_j(n)) |² ≤ Δ Σ_{n∈I} |a_n|².               (2.1)

Its level is `λ_Φ = max_j λ(d_j)`. Examples (all with Δ explicit):
* LS §1 systems: `φ_θ = √w_θ e(nθ)`, θ rational, `Δ = 1`
  (Montgomery–Vaughan, Farey with any moduli, weighted forms);
* multiplicative: `φ_χ = (q/φ(q))^{1/2} χ`, χ primitive mod `q ≤ Q`,
  `Δ = N + Q²`;
* any *hybrid* rows `φ = χ(n)e(nθ)`, Gauss-sum or Kloosterman-twisted
  rows, or any other periodic rows, with whatever Δ a proof of (2.1)
  provides.

**Lemma 2.2 (generalised Fact 1.1; PROVED).** For every `c ∈ ℂ^J`,
`N · E_U |Σ_j c_j φ_j|² ≤ Δ ‖c‖²` (U uniform on `ℤ/M''`, `M''` a common
period).

*Proof.* (2.1) says the map `a ↦ (⟨a, φ_j⟩_I)_j` has norm `≤ √Δ`; so
does its adjoint, `Σ_{n∈I}|Σ_j c_jφ_j(n)|² ≤ Δ‖c‖²`. Average over the
translates `I + t`, `t mod M''`: each residue mod `M''` lies in exactly
N of them, so the average of the left side is `N·E_U|Σ c_jφ_j|²`. ∎

**Twisted sequences and admissibility.** Let ψ be periodic with `|ψ| ≥ 1`
on 𝒜 (ψ ≡ 1 is the untwisted case; unimodular characters, Gauss sums,
weights `≥ 1`). Apply (2.1) to `a_n = ψ(n)1_A(n)`, `A ⊂ 𝒜 ∩ I`, `Z = |A|`,
`π_A` the law of A mod a common period. With
`R̃(π) = Σ_j |E_π[ψ φ̄_j]|²` this reads `Z² R̃(π_A) ≤ Δ Z E_{π_A}|ψ|²`.
A bound `Z ≤ Δ/L` is *CRT-admissible* if
`L ≤ R̃(π)/E_π|ψ|²` for **every** probability π on 𝒜 (mod the common
period); `E_π|ψ|² ≥ 1` there. This is LS §1's definition with the twist
added (LS review D1 listed twisted sequences as not covered).

**Fibrewise hybrids.** Fix `Q₀ ≤ N/2`. In fibre `c mod Q₀`
(`n = c + Q₀m`, m in an interval of `N_c ≥ ⌊N/Q₀⌋` integers, avoiding
`𝒜_c`) a method uses one of:
* (i) a periodic Bessel system `(Φ_c, Δ_c)` of length `N_c`, a twist
  `ψ_c` with `|ψ_c| ≥ 1` on `𝒜_c`, and a CRT-admissible `L_c`:
  `B_c = Δ_c/L_c`;
* (ii) a majorant with coefficient-sum rounding: `ν_c ≥ 0` on ℤ,
  `ν_c ≥ 1` on `𝒜_c`, `ν_c = Σ_i a_i 1[m ≡ b_i (d_i)]`,
  `B_c = N_c E ν_c + T_c`, `T_c = Σ|a_i|`;
* (iii) the trivial bound `B_c = N_c`.

The total bound is `B = Σ_c B_c`. This is the "hybrid" of LS §1 (sketch
only there) and contains LS Thm 3.1 (all fibres of type (i), ψ ≡ 1) and
K2 Cor 6.1 (`Q₀ = 1`, type (ii)).

**Lemma 2.3 (coarsening with fibre budget; PROVED; ET Lemma 2.9 / K2
Cor 6.1).** If every prime of 𝔊 is `≤ e^{Λ₀}`, a type-(ii) fibre has a
majorant `ν'_c` of `𝒜_c` (`≥ 0` on ℤ, `≥ 1` on `𝒜_c`) of level
`≤ Λ₀ + log N_c` with `N_c E ν'_c ≤ B_c`.

*Proof.* Project `ν_c` onto moduli dividing the period of `𝒜_c` (K2
Cor 6.1, "Projection": mean kept, `T` not increased, still a majorant);
all its primes are now primes of 𝔊. For a term of level `> λ_c :=
Λ₀ + log N_c`, keep the W-smooth part and the longest prefix (increasing
primes `> W`, with full exponents) of level `≤ λ_c`; that prefix has
level `> λ_c − Λ₀`, so the kept modulus `d' > e^{λ_c−Λ₀} = N_c`. Positive
terms move to modulus `d'` (pointwise larger), negative terms are
dropped; the mean rises by at most `Σ|a_i|/d' ≤ T_c/N_c`. ∎

**Theorem 2.4 (hybrid cap; PROVED, conditional on K2 Thm 5.1).** Let all
type-(i) systems have level `≤ λ_Φ`, all primes of 𝔊 be `≤ e^{Λ₀}`, and
put `λ = max(λ₀, λ(Q₀) + max(2λ_Φ, Λ₀ + log N))`. Then

    B ≥ (N/2) e^{−S(λ)}       (and `≥ (N/2)e^{−S_B(λ)}` under bounded B).

*Proof.* Let 𝒟 consist of 1, `Q₀`, all lifted moduli `Q₀·lcm(d_j, d_k)`
(j, k rows of one fibre system) and `Q₀·d` (d a modulus of some `ν'_c`);
all have level `≤ λ`. Take π from Lemma 1.1 and the fibre laws `π_c`
(Remark (iii)). Fibres with `π(c) = 0` contribute `B_c ≥ 0`.
* Type (i): for `‖c‖ ≤ 1`, Cauchy–Schwarz and (1.2), Lemma 2.2 give
  `|E_{π_c}[ψ_c Σ_j c_jφ̄_j]|² ≤ E_{π_c}|ψ_c|² · E_{π_c}|Σ_j c̄_jφ_j|²
  ≤ E_{π_c}|ψ_c|² · e^{S}Δ_c/(N_cQ₀π(c))`. (`|Σ c̄_jφ_j|² ≥ 0` is a real
  combination of classes mod `lcm(d_j,d_k)`.) Taking the sup over c,
  `R̃_c(π_c)/E_{π_c}|ψ_c|² ≤ e^SΔ_c/(N_cQ₀π(c))`, so admissibility gives
  `B_c = Δ_c/L_c ≥ N_c Q₀ π(c) e^{−S}`.
* Type (ii): with `ν'_c` of Lemma 2.3, `1 ≤ E_{π_c}ν'_c ≤
  e^S E_Uν'_c/(Q₀π(c))`, so `B_c ≥ N_cE ν'_c ≥ N_cQ₀π(c)e^{−S}`.
* Type (iii): `π(c) ≤ e^S/Q₀`, so `B_c = N_c ≥ N_cQ₀π(c)e^{−S}`.

Summing, `B ≥ e^{−S}Q₀⌊N/Q₀⌋Σ_cπ(c) ≥ (N/2)e^{−S}`. ∎

**Corollary 2.5 (exceptional-set reading; PROVED, same proviso).** If
`Q₀ ≤ min(N^A, N/2)`, all row periods are `≤ N^A` and all primes of 𝔊
are `≤ N^A` (A ≥ 1), then `λ ≤ 4A log N` and every such hybrid bound
saves at most `C_A(log N)^{3/4}(log log N)^{3/4}` (`C_{A,B}(log N)^{3/4}`
under bounded B). In particular twisted large sieves (any periodic twist
ψ with `|ψ| ≥ 1` on 𝒜, of **any** period and level), the multiplicative
large sieve and its hybrids with additive frequencies, Gauss-sum
twisted rows, and fibrewise mixtures of large-sieve and
majorant-with-rounding fibres give no θ > 3/4.

*Remarks.* (a) The twist ψ never enters the level: Cauchy–Schwarz
removes it. Only the rows' periods do. (b) Translating π by multiples of
`M₀` (which preserves 𝒜 and every `V_𝒟`-inequality) makes π uniform on
the fibres of `ℤ/M' → ℤ/M₀`. If ψ is `M₀`-periodic, `E_π[ψφ̄_j]` then
depends only on the projection `E_U[φ_j | n mod M₀]`, so (LS Rem 3.3)
only the parts of the rows of period dividing `M₀` count toward λ_Φ.
(c) Not covered: rows that are not periodic (Archimedean twists
`n^{it}`, smooth weights in n); these use the position of n in I, i.e.
non-CRT information (LS (E3)).

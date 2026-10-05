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

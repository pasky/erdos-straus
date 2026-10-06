# EXCEPTIONAL_WEIGHTS — per-frequency weights below 1 (task O81)

Status: **work in progress (O81), not reviewed.** Labels follow `DISCOVERIES.md`.
PROVED means proved in this file, internal checks only. No θ > 3/4 is claimed.

Notation as in `EXCEPTIONAL_NONCRT.md` (NC), `EXCEPTIONAL_INTERFREQ.md` (IF),
`EXCEPTIONAL_KARY2.md`/`KARY3.md` (K2/K3). 𝒜 = 𝒜(𝔊) ⊂ ℤ is the avoider set of a
finite family 𝔊 of residue classes, periodic with period Q. A *majorant* is a
Q-periodic ν: ℤ → ℝ with ν ≥ 0 on ℤ and ν ≥ 1 on 𝒜 (on all of ℤ; for finite
combinations of classes the period is a multiple of Q, and we take Q to be a
common period). Fourier coefficients `ν̂(θ) = E_{n mod Q} ν(n) e(−nθ)`,
θ ∈ (1/Q)ℤ/ℤ, so `ν(n) = Σ_θ ν̂(θ) e(nθ)` and `ν̂(0) = Eν`.

## 0. Summary

(filled in at the checkpoint)

## 1. Per-frequency bounds are translation invariant

A **per-frequency bound** with weight `w: (1/Q)ℤ/ℤ → [0,∞)` is

    R_w(ν) = Σ_θ w(θ) |ν̂(θ)|            (the θ = 0 term is w(0)·Eν).        (1.1)

It is used through an identity `Σ_n Ψ(n) ν(n) = Σ_θ ν̂(θ) Ψ̌(θ)` for a test
function Ψ ≥ 1_{[1,N]} on ℤ, with `Ψ̌(θ) = Σ_{n∈ℤ} Ψ(n) e(nθ)` and `w ≥ |Ψ̌|`.
The two cases of NC §2.5:

* *sharp:* `Ψ = 1_{[1,N]}`, `Ψ̌ = S_N(θ) = Σ_{n≤N} e(nθ)`, `|S_N(θ)| = |sin πNθ / sin πθ|`;
* *smooth window:* `Ψ(n) = Φ(n/N)`, Φ ≥ 0 integrable on ℝ, Φ ≥ 1 on [1/N, 1],
  `Σ_n Φ(n/N) < ∞`; `Ψ̌ = W_N(θ) = Σ_n Φ(n/N) e(nθ)`.

The weights `|S_N|` and `|W_N|` are < 1 on large sets of frequencies
(`|W_N(θ)| = O_A(N(N‖θ‖)^{−A})` for smooth Φ). NC Thm 2.3 needs `w ≥ 1` at
every θ ≠ 0 and does not apply.

**Lemma 1.1 (translation invariance; PROVED, trivial).** Let `w ≥ |Ψ̌|` with Ψ
as above. For every majorant ν and every t ∈ ℤ,

    R_w(ν) ≥ Σ_{n=t+1}^{t+N} ν(n) ≥ #(𝒜 ∩ (t, t+N]).

Hence `R_w(ν) ≥ M(N)` for every majorant ν, where

    M(N) = M_𝒜(N) := max_{t∈ℤ} #(𝒜 ∩ (t, t+N])                               (1.2)

is the **shift-uniform avoider count**.

*Proof.* `ν_t(n) = ν(n+t)` is a majorant of 𝒜 − t, and `|ν̂_t(θ)| = |ν̂(θ)|`, so
`R_w(ν) = R_w(ν_t) ≥ |Σ_θ ν̂_t(θ)Ψ̌(θ)| = Σ_n Ψ(n)ν(n+t) ≥ Σ_{n≤N} ν(n+t)`, using
Ψ ≥ 1_{[1,N]} and ν ≥ 0 on ℤ. Finally ν ≥ 1 on 𝒜. ∎

So no per-frequency bound — any weights, any coefficients, any majorant — can
beat the maximal number of avoiders in a window of length N anywhere in ℤ.
The same holds for every bound of the form `N·Eν + Σ_i|a_i|` (each class meets
any window in ≤ N/d + 1 points), so M(N) is a common floor of all
shift-uniform methods. `M(N) ≥ #(𝒜∩[1,N])`, and M(N) is in general much larger
than the true count on [1,N] (it is a maximum over all of ℤ, i.e. over all CRT
translates of the family).

**Lemma 1.2 (LP duality for per-frequency bounds; PROVED).** For every weight
`w ≥ 0` with `w(−θ) = w(θ)`,

    min { R_w(ν) : ν majorant of 𝒜 }
      = max { Σ_{n mod Q} g(n) 1_𝒜(n) : g: ℤ/Q → [0,∞), |Q ĝ(θ)| ≤ w(θ) ∀θ }.   (1.3)

*Proof.* Let `G = {g real: |Qĝ(θ)| ≤ w(θ) ∀θ}`, a compact convex set (ĝ = 0
where w = 0). For real ν, `Σ_n g(n)ν(n) = Q Σ_θ ĝ(θ) conj(ν̂(θ)) ≤ R_w(ν)`, with
equality for `Qĝ(θ) = w(θ) ν̂(θ)/|ν̂(θ)|` (any unimodular value where ν̂ = 0,
chosen conjugate-symmetric, so g is real). Hence `R_w(ν) = max_{g∈G} ⟨g, ν⟩`.
The constraint "ν majorant" is `ν ≥ 1_𝒜` pointwise on ℤ/Q (since 1_𝒜 ≥ 0). By
Sion's minimax theorem (bilinear form, G compact convex, feasible set convex),
`min_{ν ≥ 1_𝒜} max_{g∈G} ⟨g,ν⟩ = max_{g∈G} inf_{ν ≥ 1_𝒜} ⟨g,ν⟩`. The inner
infimum is −∞ unless g ≥ 0, and then it is `⟨g, 1_𝒜⟩` (attained at ν = 1_𝒜). ∎

*Remark.* `g(n) = Ψ(n − t)` periodised is in G (its `Qĝ` is `Ψ̌(θ)e(−tθ)`), which
is the dual form of Lemma 1.1. The KARY/NC caps are the statement that, for
`w ≥ 1` at θ ≠ 0 (and the prime-slice/forced structure), G contains a g with
value `≥ N e^{−C(log N)^{3/4}}`; such g may be very rough. For weights below 1,
G consists of functions whose spectrum is (essentially) confined where w is
large, and §2 shows this confines g to be smooth at scale N.

## 2. Band-limited windows: the general-majorant door is exactly M(N)

Let K ≥ 1 and let Φ = Φ_K be Selberg's majorant of `1_{[0,1]}` with
`Φ̂` supported in `[−K, K]` and `∫Φ = Φ̂(0) = 1 + 1/K` (Vaaler, Bull. AMS 12
(1985); Montgomery, *Ten lectures*, Ch. 1). Φ ≥ 0, Φ ≥ 1 on [0,1], Φ is entire of
exponential type and `Φ(x) = O(x^{−2})`, so `Σ_n Φ(n/N)` converges absolutely.

**Lemma 2.0 (PROVED, routine).** For N ≥ 4K: `W_N(θ) = 0` unless `‖θ‖ ≤ K/N`,
and `W_N(0) = N(1 + 1/K)`.

*Proof.* Poisson (valid: Φ ∈ L¹, Φ̂ continuous with compact support, Φ = O(x^{−2})):
`W_N(θ) = Σ_k N Φ̂(N(k − θ))`. A term is nonzero only if `|k − θ| ≤ K/N ≤ 1/4`. ∎

**Theorem 2.1 (per-frequency rounding with a band-limited window ≍ the
shift-uniform count; PROVED).** For every finite family (any classes, any
moduli) and N ≥ 4K,

    M(N) ≤ min_{ν majorant} Σ_θ |ν̂(θ)| |W_N(θ)| ≤ 12(K+1)·M(⌈N/K⌉) ≤ 12(K+1)·M(N).   (2.1)

*Proof.* Lower bound: Lemma 1.1 (Φ ≥ 1 on [1/N, 1]). Upper bound: by Lemma 1.2 it
suffices to bound `⟨g, 1_𝒜⟩` for g ≥ 0 with `|Qĝ| ≤ |W_N|`. By Lemma 2.0 the
spectrum of g lies in `‖θ‖ ≤ δ := K/N ≤ 1/4`.

*Reproducing kernel.* Put `k_δ(x) = δ(sin πδx / πδx)²`, whose Fourier transform
is the triangle `(1 − |ξ|/δ)_+`, and `v = 2k_{2δ} − k_δ`. Then `v̂ = 1` on
`|ξ| ≤ δ` and `v̂ = 0` for `|ξ| ≥ 2δ`, and `|v(x)| ≤ 5δ min(1, (πδx)^{−2})`. By
Poisson, `Σ_{m∈ℤ} v(m) e(−mθ) = Σ_k v̂(θ + k)`, which equals 1 for `‖θ‖ ≤ δ`
(2δ ≤ 1/2). Since g is a trigonometric polynomial with spectrum in `‖θ‖ ≤ δ`,

    g(n) = Σ_{m∈ℤ} v(m) g(n − m)      for every n (absolutely convergent).

*Bound.* Summing over n mod Q and substituting r = n − m,

    ⟨g, 1_𝒜⟩ = Σ_{r mod Q} g(r) Σ_{m∈ℤ} v(m) 1_𝒜(r + m)
             ≤ Σ_{r mod Q} g(r) · Σ_{m∈ℤ} |v(m)| 1_𝒜(r + m),

using g ≥ 0. Cut ℤ into blocks `I_j = [jL, (j+1)L)`, `L = ⌈1/δ⌉`. Each block
meets `𝒜 − r` in at most `M(L)` points. On `I_j` we have `|v| ≤ 5δ` for
j ∈ {−1, 0}, and `|v| ≤ 5δ/(π² j'²)` with `j' = j` (j ≥ 1) or `j' = |j| − 1`
(j ≤ −2). So the inner sum is ≤ `5δ M(L)(2 + 2·π^{−2}·π²/6) ≤ 12 δ M(L)`.
Finally `Σ_r g(r) = Qĝ(0) ≤ W_N(0) = N(1+1/K)`, and `12δ·N(1+1/K) = 12(K+1)`.
M is nondecreasing, and `⌈N/K⌉ ≤ N`. ∎

**Corollary 2.2 (PROVED).** (a) For the window Φ_K there is a majorant ν of 𝒜
(a general Q-periodic function, not a hit-pattern or level-restricted one)
whose per-frequency bound is `≤ 12(K+1)M(N)`. (b) Hence, for per-frequency
smooth rounding over general majorants, a cap of the form
`saving ≤ C(log N)^{3/4}` holds **if and only if**
`M(N) ≥ N exp(−C′(log N)^{3/4})` (with C, C′ related by `log(12(K+1))`).
(c) By Lemma 1.1, a lower bound `M(N) ≥ N e^{−C(log N)^{3/4}}` would cap **every**
per-frequency bound with `w ≥ |W_N|` or `w ≥ |S_N|`, for every majorant class,
every window, and every family.

So the "weights below 1" door for general majorants is not a door about
Fourier analysis at all: it is the shift-uniform version of the counting
problem. It is the analogue of IF Obs 1.1 (exact interval evaluation over
unrestricted majorants is the problem itself), with [1,N] replaced by the
worst window. In particular no arithmetic-free argument (Walsh tails,
comparison measures, LP caps built from level/mass hypotheses) can cap this
class unless it proves a lower bound for M(N) — a statement about the
avoider set itself.

*What M(N) is.* By CRT, t ranges over all residue vectors. In a prime-slice
system (Q₀ = 1, one prime ℓ per class set F_ℓ) M(N) is the **translate sieve**

    M(N) = max_{(c_ℓ)} #{ j ∈ [1,N] : j + c_ℓ ∉ F_ℓ (mod ℓ) for all ℓ }.     (2.2)

A class set with `N·|F_ℓ| < ℓ` has a gap of length N mod ℓ and is avoided at no
cost. For forced classes `|ℛ(M)| = M^{o(1)}`, so only moduli `≤ N^{1+o(1)}`
matter for M(N). The upper bound `M(N) ≤ N exp(−c(log N)^{3/4})` holds (the 3/4
note's bound is shift-uniform). Whether M(N) is that large is §5.

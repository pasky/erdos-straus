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

## 3. Sharp weights for hit-pattern majorants: capped unconditionally

Setting of NC §2.5: a prime-slice system with Q₀ = 1 (distinct primes ℓ ∈ 𝒫,
class sets `F_ℓ ⊂ ℤ/ℓ`, `p_ℓ = |F_ℓ|/ℓ ≤ 1/4`), and a **hit-pattern majorant**
`ν(n) = f(x(n))`, `x_ℓ(n) = 1[n mod ℓ ∈ F_ℓ]`, with biased Walsh expansion
`ν = Σ_S d_S y^S`. As in NC §2.5, `ν̂` on `Θ_S` equals `d_S·Π_{ℓ∈S} 1̂_{F_ℓ}(h_ℓ)`,
so for any weight w

    R_w(ν) = Σ_S |d_S| M_S^w,   M_S^w = Σ_{θ∈Θ_S} m_S(θ) w(θ),
    m_S(Σ h_ℓ/ℓ) = Π_{ℓ∈S} |1̂_{F_ℓ}(h_ℓ)|,   A_S := Σ_θ m_S(θ) = Π_{ℓ∈S} a_ℓ,       (3.1)

`a_ℓ = Σ_{h≠0} |1̂_{F_ℓ}(h)| ≥ Σ|1̂|²/max|1̂| = 1 − p_ℓ`. Put
`g_ℓ(n) = Σ_{h≢0} |1̂_{F_ℓ}(h)| e(nh/ℓ)` (real, since `|1̂_F(−h)| = |1̂_F(h)|`) and
`φ_ℓ(n) = g_ℓ(n)/a_ℓ ∈ [−1, 1]`.

**Lemma 3.1 (sin² lower bound; PROVED).** If `w(θ) ≥ c₀|sin πNθ|` for all θ ≠ 0,
then for every S ≠ ∅

    M_S^w ≥ (c₀/2) · A_S · (1 − |Π_{ℓ∈S} φ_ℓ(N)|).

This applies to the sharp weight `|S_N(θ)| = |sin πNθ|/|sin πθ| ≥ |sin πNθ|`
(c₀ = 1).

*Proof.* `|sin x| ≥ sin² x = (1 − cos 2x)/2`. So
`M_S^w ≥ (c₀/2) Σ_θ m_S(θ)(1 − cos 2πNθ) = (c₀/2)(A_S − Re Σ_θ m_S(θ)e(Nθ))`.
Since `m_S` is a product measure in the CRT coordinates and
`e(Nθ) = Π_ℓ e(Nh_ℓ/ℓ)`, `Σ_θ m_S(θ)e(Nθ) = Π_ℓ g_ℓ(N) = A_S Π_ℓ φ_ℓ(N)`. ∎

**Lemma 3.2 (one-prime anti-concentration; PROVED).** Let ℓ be an odd prime,
ℓ ∤ N, `F ⊂ ℤ/ℓ` with `|F| = k ≥ 1`, `p = k/ℓ ≤ 1/4`. Then
`1 − |φ_ℓ(N)| ≥ 9/(256 k²)`.

*Proof.* Let μ be the probability measure `|1̂_F(h)|/a_ℓ` on h ≢ 0. Then
`1 − |φ(N)| ≥ Σ_h μ(h)(1 − |cos(2πNh/ℓ)|)`. For `η ∈ (0,1/2]`, put
`B = {h ≢ 0 : ‖2Nh/ℓ‖ < η}`. As `h ↦ 2Nh` is a bijection of ℤ/ℓ (ℓ odd, ℓ ∤ N),
`#B ≤ 2ηℓ`. Each `|1̂_F(h)| ≤ p` and `a_ℓ ≥ 1 − p ≥ 3/4`, so
`μ(B) ≤ 2ηℓp/(3/4) = (8/3)ηk`. Off B, `1 − |cos(2πNh/ℓ)| = 1 − cos(π‖2Nh/ℓ‖) ≥ 2η²`
(`1 − cos y ≥ 2y²/π²` on [0,π]). With `η = 3/(16k)`: `μ(B) ≤ 1/2` and
`1 − |φ| ≥ (1/2)·2η² = 9/(256k²)`. ∎

**Theorem 3.3 (sharp and sin-dominated weights are capped for hit-pattern
majorants; PROVED).** Take a prime-slice system with Q₀ = 1 and `p_ℓ ≤ 1/4`.
Fix γ < 1/3 and `s_* ∈ (0, log 2]`; call ℓ *good* if `|F_ℓ|³ ≤ ℓ e^{−s_*}/2`,
*bad* otherwise (bad primes are `< (2e^{s_*})^{1/(1−3γ)}` if `|F_ℓ| ≤ ℓ^γ`; we only
assume their number and size are bounded, `B₁ := Σ_{ℓ bad} log ℓ < ∞`). Weights:

    s_ℓ = log(ℓ/(2|F_ℓ|³)) = log(1/(2p_ℓ)) − 2log|F_ℓ|   (ℓ good),
    s_ℓ = log(1/(2p_ℓ))                                    (ℓ bad);

all `s_ℓ ≥ s_*`. Let ν be a hit-pattern majorant of arbitrary level and w any
weight with `w(0) = N` and `w(θ) ≥ c₀|sin πNθ|` for θ ≠ 0. Then for every
`λ ≥ log N + B₁` NC Thm 2.3 holds with ε replaced by
`ε^w := (512/(9c₀))·e^{−λ}·R_w(ν)`:

    Eν ≥ (1 − ε^w) e^{−Φ̄(λ,α)} − 2ε^w,

Φ̄ computed with these s_ℓ. Consequently, if the system satisfies the mass
hypothesis
(M) `|F_ℓ| ≤ ℓ^γ` for good ℓ, and `Σ_ℓ p_ℓ ℓ^{−β} ≤ C_M β^{−3}` for β ∈ (0,1]
(true for ℛ(ℓ)-slices, `|ℛ(ℓ)| = ℓ^{o(1)}`, by ET Lemmas 3.1, 3.2, 3.7 as used in
NC Cor 2.5), then every bound `N·Eν + Σ_{θ≠0}|ν̂(θ)|w(θ) = N e^{−s}` with ν a
hit-pattern majorant has

    s ≤ C₉(γ, C_M, B₁, c₀) (log N)^{3/4}      (N ≥ N₀).

*Proof.* Only NC's tail estimate (2.3) changes. Let `s(S) > λ`. Bad primes
contribute at most B₁ to s(S), and `s_ℓ < log ℓ` for good ℓ, so the good primes
of S have product `> e^{λ−B₁} ≥ N`; hence some good `ℓ₀ ∈ S` does not divide N
(and ℓ₀ ≥ 5 since p ≤ 1/4). Lemmas 3.1–3.2 with ℓ₀ give
`M_S^w ≥ (9c₀/512)·A_S/|F_{ℓ₀}|² ≥ (9c₀/512)·Π_S(1−p_ℓ)/|F_{ℓ₀}|²`. By the
choice of weights, `Π_S 2p_ℓ·|F_{ℓ₀}|² ≤ e^{−s(S)}`. Hence

    |d_S| Π_S 2p_ℓ(1−p_ℓ) ≤ (512/(9c₀)) |d_S| M_S^w e^{−s(S)},

and `Π_S p_ℓ ≤ Π_S (4/3)p_ℓ(1−p_ℓ) ≤ Π_S 2p_ℓ(1−p_ℓ)`. Summing over `s(S) > λ`,
`r₀, r₁ ≤ (512/(9c₀)) e^{−λ} Σ_S |d_S| M_S^w ≤ ε^w`. The rest of NC Prop 2.1 /
Thm 2.3 uses only `s_ℓ ≥ s_*`. For the consequence: `R_w(ν) ≤ N e^{−s} ≤ N`;
take `λ = 2 log(4N) + log(512/(9c₀)) + B₁`, so `ε^w ≤ e^{−Φ̄}/4` once
`Φ̄(λ) = o(log N)`, and conclude as in NC Cor 2.4. For Φ̄: on good primes
`e^{−αs_ℓ} ≤ 2^α ℓ^{−α(1−3γ)}`, so `Σ p_ℓ e^{−αs_ℓ} ≤ 2C_M(α(1−3γ))^{−3} + O_{B₁}(1)`;
and `s_ℓ ≤ λ` forces `ℓ ≤ (2e^{λ+s_*})^{1/(1−3γ)}` (good) =: X, so the truncated mass is
`Σ_{ℓ≤X} p_ℓ ≤ e·Σ_ℓ p_ℓ ℓ^{−1/log X} ≤ e·C_M (log X)³ + O_{B₁}(1) ≪ λ³` (β = 1/log X in (M)). With α = λ^{−1/4}
this is NC Cor 2.5's computation: `Φ̄ ≤ Cλ^{3/4} + O(log²λ)`. ∎

*What this closes.* In NC §2.5's list: the exact sharp weight `|S_N(θ)|` and
ψ-based Erdős–Turán/Vaaler rounding whose weights carry the factor
`|sin πNθ|` (with a lower bound `w ≥ c₀|sin πNθ|`), for hit-pattern
majorants with Q₀ = 1, are capped at `(log N)^{3/4}` without (H_eq). The
mechanism: a weight below 1 only near `‖Nθ‖ = 0` is harmless because the
product measure m_S cannot concentrate near `{‖Nθ‖ = 0}` — its N-th
"characteristic function" `Πφ_ℓ(N)` is bounded away from 1 by a single
coordinate.

*Not closed by §3:* smooth windows (weights tiny on all of `‖θ‖ ≫ 1/N`, so
anti-concentration is not enough; one needs equidistribution, (H_eq)); and
general (non-hit-pattern) majorants with sharp weights (they may reshape ν̂
inside Θ_S towards `‖Nθ‖ ≈ 0`; whether positivity forbids this is open).

## 4. Smooth windows for hit-pattern majorants: what (H_eq) really asks

Same setting as §3 (Q₀ = 1, hit-pattern ν), now `w = |W_N|` for a fixed window Φ
(Φ ≥ 0, Φ ≥ 1 on [0,1], Φ̂ continuous and integrable decay so that Poisson
applies). Then `W_N(θ) = Σ_k NΦ̂(N(k−θ))`, and there are `c_Φ > 0`, `N_Φ` with
`|W_N(θ)| ≥ N/3` for `‖θ‖ ≤ c_Φ/N`, N ≥ N_Φ (continuity of Φ̂ at 0, Φ̂(0) ≥ 1).
NC (2.6) / IF Lemma 4.1 need `M_S^{|W|} ≳ e^{−o(λ)} A_S` (or `N^{−A}Π(1−p)`) for
`s(S) > λ`. Write `X_S = Σ_{ℓ∈S} X_ℓ mod 1` with independent `X_ℓ = h_ℓ/ℓ`,
`P(X_ℓ = h/ℓ) = |1̂_{F_ℓ}(h)|/a_ℓ` (h ≢ 0). Then `M_S^{|W|} = A_S·E|W_N(X_S)|`, and the
"characteristic function" of X_S is `E e(kX_S) = Π_ℓ φ_ℓ(k)`.

**Lemma 4.1 (a sufficient condition; PROVED).** If

    Σ_{0<|k|≤N/c_Φ} |Π_{ℓ∈S} φ_ℓ(k)| ≤ 1/6,                                     (4.1)

then `M_S^{|W|} ≥ (c_Φ/6) A_S`.

*Proof.* Let T be Selberg's minorant of the arc `‖θ‖ ≤ c/N` (c = c_Φ) on ℝ/ℤ, a
trigonometric polynomial of degree `H = ⌊N/c⌋ − 1` with `T ≤ 1_{‖θ‖≤c/N}`,
`T̂(0) = 2c/N − 1/(H+1) ≥ c/N`, `|T̂(k)| ≤ |1̂_arc(k)| + (2c/N − T̂(0)) ≤ 3c/N`. Then
`M_S ≥ (N/3) A_S P(‖X_S‖ ≤ c/N) ≥ (N/3) A_S E T(X_S)` and
`E T(X_S) = Σ_{|k|≤H} T̂(k) Πφ_ℓ(k) ≥ (c/N)(1 − 3·(1/6))`. ∎

**Lemma 4.2 (one large prime; PROVED).** If S = {ℓ} with `ℓ ≥ 2|F_ℓ|N/c_Φ`, then
`M_S^{|W|} ≥ c_Φ/6 ≥ (c_Φ/(6√|F_ℓ|))·A_S`.

*Proof.* Fejér at a point `x₀ ∈ F` (`H' = ⌊cℓ/N⌋ ≥ 2|F|`): the Fejér kernel is
nonnegative, so `Σ_{|h|<H'}(1−|h|/H')1̂_F(h)e(hx₀/ℓ) = ℓ^{−1}Σ_{y∈F}F_{H'}((x₀−y)/ℓ)
≥ H'/ℓ`; removing h = 0 (value p) gives `Σ_{0<|h|<H'}|1̂_F(h)| ≥ (H' − |F|)/ℓ ≥ c/(2N)`,
and these h have `‖h/ℓ‖ ≤ c/N`. Finally `a_ℓ ≤ (ℓ Σ|1̂_F|²)^{1/2} ≤ √|F|`. ∎

So for a single high prime (H_eq) holds with an affordable loss `√|F_ℓ|` (absorbed
by weights exactly as in Thm 3.3). The single-prime proof uses that the scale
`1/N` is coarse compared with `1/ℓ`. With **several** primes the target is the
density of a *sum* `X_S` near 0. A product box (all `‖X_ℓ‖ ≤ c/(N|S|)`) loses a
factor `≈ (N|S|)^{|S|−1}`, and near an arbitrary point β the one-coordinate
mass can be very small (F = {−2,−1} ⊂ ℛ(ℓ) for ℓ ≡ 7 (8): `|1̂_F(h)| = (2/ℓ)|cos πh/ℓ|`
vanishes to first order at θ = 1/2). Lemma 4.1 needs the characteristic function
`Πφ_ℓ(k)` to be `o(1/N)` on average over `0 < |k| ≲ N`. For ℛ(ℓ)-slices this is a
statement about `Σ_h |1̂_{ℛ(ℓ)}(h)| e(kh/ℓ)` for small k; the absolute value
destroys the multiplicative structure of the classes `−u/v`, and small-height
labels give **positive** correlations at small k (e.g. `{−2,−1} ⊂ ℛ(ℓ)` gives
`φ_ℓ(1) ≈ 1/3` for that pair alone), which help (H_eq) but are not summable to
≤ 1/6 in general. **Status: (H_eq) for several primes ≤ N^{O(1)} remains
CONJECTURE.** Neither a proof nor an abstract counterexample (a family whose
`X_S` avoids the `1/N`-neighbourhood of 0 for all high S) was found; depletion
would need every `|1̂_{F_ℓ}|` to avoid low frequencies, while Lemma 4.2's Fejér
argument shows that a sparse F always carries spectral mass `≥ c/N` within `c/N`
of 0.

**Relation to §2.** For hit-pattern majorants the smooth per-frequency LP value
is ≥ M(N) (Lemma 1.1). So the hit-pattern smooth door is closed if *either*
(H_eq) holds (NC §2.5, IF Lemma 4.1) *or* `M(N) ≥ N e^{−C(log N)^{3/4}}` (§5).

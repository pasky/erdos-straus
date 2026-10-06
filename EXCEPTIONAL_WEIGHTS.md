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

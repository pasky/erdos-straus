# EXCEPTIONAL_LARGESIEVE — the large sieve over forced-class mixtures (task O17)

Status: **in progress (checkpoint 1 being written).** Labels follow
`DISCOVERIES.md`. Notation: ET = `EXCEPTIONAL_THETA.md`, KARY2 =
`EXCEPTIONAL_KARY2.md`, NONCRT = `EXCEPTIONAL_NONCRT.md`.

## 0. Summary

(written at the end)

## 1. Setting

**Families.** 𝔊 is a finite family of classes `b (mod G)` of the four
KARY2 types (ℛ(M), (a,D), Case A, selector `0 mod p`), mixed arbitrarily,
arbitrary moduli (KARY2 Def. 2.0). `𝒜 = 𝒜(𝔊) ⊂ ℤ` is the set of all
integers in none of its classes. It is `M₀`-periodic, `M₀ = lcm` of the
moduli. Every exceptional prime `p ≤ N` with `p > y` lies in `𝒜` when 𝔊
consists of forced classes and selector classes `0 mod ℓ`, `ℓ ≤ y`.

**Large-sieve inequalities.** Let `Θ ⊂ ℝ/ℤ` be finite (distinct points)
and `w : Θ → (0,∞)`. Say `(Θ,w)` is an *N-large-sieve system* if

    Σ_{θ∈Θ} w_θ |Σ_{n∈I} a_n e(nθ)|² ≤ Σ_{n∈I} |a_n|²            (LS)

for every interval `I` of `N` consecutive integers and all `a_n ∈ ℂ`.
Examples:
* Montgomery–Vaughan: Θ δ-spaced, `w ≡ (N−1+δ^{−1})^{−1}`;
* Farey (Montgomery's arithmetic form): `Θ = {a/q : q ∈ 𝒬, (a,q)=1}`
  for any set `𝒬 ⊆ [1,Q]` of moduli (prime, prime power or composite),
  `w ≡ (N+Q²)^{−1}`; any subset of the `a` is allowed;
* weighted (Montgomery–Vaughan): `w_θ = (N + (3/2)δ_θ^{−1})^{−1}`, `δ_θ`
  the distance to the nearest other point.

**Fact 1.1.** In every N-large-sieve system, `w_θ ≤ 1/N` for each θ.
*Proof.* Take `a_n = e(−nθ)` on I in (LS): `w_θ N² ≤ N`. ∎

**CRT-admissible large-sieve bounds.** Let `A ⊂ 𝒜 ∩ I` be the sifted set,
`Z = |A|`, `S_A(θ) = Σ_{n∈A} e(nθ)`. Applying (LS) with `a_n = 1_A(n)`
gives `Σ_θ w_θ|S_A(θ)|² ≤ Z`. A large-sieve argument turns this into
`Z ≤ 1/L` by proving a lower bound `Σ_θ w_θ|S_A(θ)|² ≥ L·Z²`.

Fix a modulus `M'` that is a multiple of `M₀` and of every denominator of
the rational points of Θ. Write `Θ_ℚ = Θ ∩ (M'^{−1}ℤ/ℤ)`, `P(𝒜)` for the
probability measures on `ℤ/M'` supported on `𝒜 mod M'`,
`π̂(θ) = Σ_n π(n) e(nθ)` and

    F_w(π) = Σ_{θ∈Θ_ℚ} w_θ |π̂(θ)|²,      F*_w = min_{π∈P(𝒜)} F_w(π).

For the empirical law `π_A` of `A mod M'` one has `S_A(θ) = Z·π̂_A(θ)` on
`Θ_ℚ`. We call the bound *CRT-admissible* if its `L` satisfies
`L ≤ F_w(π)` for **every** `π ∈ P(𝒜)`; that is, the lower bound uses only
the fact that the residues of A lie in `𝒜`, not that A sits in a short
interval or that `π_A` is an empirical law of a small set. Every
arithmetic large sieve in use is of this kind: the lower bound comes from
Cauchy–Schwarz over residue classes, `Σ_{a mod q}|S(a/q)|² =
q Σ_b Z(q,b)²`, and multiplicativity. This includes
* prime moduli with `ω(ℓ)` excluded classes (Montgomery; the 2/3 note
  (LS); Vaughan 1970; Pomerance–Weingartner §4);
* prime powers and composite moduli (sieving by `q` via
  `Σ*_{a mod q}`);
* forced classes of composite moduli, used through any of their
  prime-power components or directly through `D_q(π)` below.

Write `D_q(π) = Σ*_{a mod q}|π̂(a/q)|²`. By Parseval mod q,
`q Σ_b π(n≡b (q))² = Σ_{d|q} D_d(π)`.

Irrational θ are not seen by a CRT-admissible bound: `S_A(θ)` is not a
function of `π_A`, and dropping these terms only weakens (LS)'s left side.
So the best CRT-admissible bound is `Z ≤ 1/F*_w`.

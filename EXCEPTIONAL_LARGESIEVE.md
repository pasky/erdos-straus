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

## 2. Exact duality: the optimal large sieve is a Λ²-majorant

**Theorem 2.1 (duality; PROVED).** Let `(Θ,w)` be any finite set of
points with positive weights, and `M'`, `Θ_ℚ`, `P(𝒜)` as in §1. Put

    m_w = inf { Σ_{θ∈Θ_ℚ} |γ_θ|²/w_θ :  g(n) = Σ_{θ∈Θ_ℚ} γ_θ e(−nθ),
                                        Re g(n) ≥ 1 for all n ∈ 𝒜 }

(`inf ∅ = ∞`). Then `F*_w = 1/m_w`, and the infimum is attained when
finite.

*Proof.* `P(𝒜)` is a simplex in `ℝ^{M'}`. The map
`T π = (√w_θ π̂(θ))_θ ∈ ℂ^{Θ_ℚ}` is ℝ-linear and `F_w(π) = ‖Tπ‖²`.

(≥) Let g be feasible and `π ∈ P(𝒜)`. Since π is real,
`Σ_n π(n) g(n) = Σ_θ γ_θ conj(π̂(θ))`, and its real part is
`Σ_n π(n) Re g(n) ≥ 1`. Cauchy–Schwarz gives
`1 ≤ (Σ_θ|γ_θ|²/w_θ)(Σ_θ w_θ|π̂(θ)|²)`. Hence `F_w(π) ≥ 1/m_w` for all π.

(≤) Write `‖Tπ‖ = max_{c∈ℂ^{Θ_ℚ}, ‖c‖≤1} φ(π,c)` with
`φ(π,c) = Re⟨Tπ,c⟩ = Σ_n π(n) Re h_c(n)`, where
`h_c(n) = Σ_θ √w_θ conj(c_θ) e(nθ)`. φ is ℝ-bilinear and both sets are
compact and convex. Von Neumann's minimax theorem gives

    √F*_w = min_π max_c φ = max_c min_π φ = max_{‖c‖≤1} min_{n∈𝒜} Re h_c(n).

If `F*_w = 0` there is no feasible g, by (≥). If `F*_w > 0`, take a
maximiser `c*` and put `g = conj(h_{c*})/√F*_w`, i.e.
`g(n) = Σ_θ γ_θ e(−nθ)` with `γ_θ = √w_θ c*_θ/√F*_w`. Then
`Re g = Re h_{c*}/√F*_w ≥ 1` on 𝒜 and
`Σ|γ_θ|²/w_θ = ‖c*‖²/F*_w ≤ 1/F*_w`. So `m_w ≤ 1/F*_w`, attained by g. ∎

**Corollary 2.2 (the large sieve is bounded below by a CRT majorant;
PROVED).** Let `(Θ,w)` be an N-large-sieve system and `A ⊂ 𝒜 ∩ I`. Every
CRT-admissible large-sieve bound `Z ≤ 1/L` satisfies

    1/L ≥ 1/F*_w = m_w ≥ N · Eν*,      ν* := |g*|²,

where `g*` attains `m_w` (if `m_w = ∞` there is no bound at all). `ν*`
is a CRT majorant of 𝒜 in the sense of ET §1 and KARY2 Thm 5.1:
* `ν* ≥ 0` on ℤ, and `ν* ≥ (Re g*)² ≥ 1` on all of 𝒜;
* `ν*(n) = Σ_{θ,θ'} γ_θ conj(γ_{θ'}) e(n(θ'−θ))`, and
  `e(na/d) = Σ_{b mod d} e(ab/d)·1[n ≡ b (d)]`. Taking real parts,
  `ν* = Σ_i a_i 1[n ≡ b_i (d_i)]` with real `a_i`, every `d_i` dividing
  `lcm(den θ, den θ')` for some `θ, θ' ∈ Θ_ℚ`.

*Proof.* `L ≤ F*_w` by admissibility; then Theorem 2.1; then Fact 1.1:
`Σ|γ_θ|²/w_θ ≥ N Σ|γ_θ|² = N·E_{n mod M'}|g*(n)|²` (Parseval on `ℤ/M'`;
the θ are distinct mod 1). ∎

**Remark 2.3 (what this says).** The best bound any CRT-admissible large
sieve can give, with any frequencies, any composite moduli and any
weights, is at least `N` times the mean of a Selberg-square majorant
`|g|²`, nonnegative on ℤ, built from the characters the large sieve
uses. This is the classical large-sieve/Selberg duality, made exact and
extended to arbitrary class systems. Unlike KARY2 Cor 6.1 there is no
rounding term: the factor `N + δ^{−1} ≥ N` of the large sieve already
contains N. So the cap needs only the **level** of `ν*`, not its
coefficient sum.

## 3. The cap for frequencies of polynomial level

**Fibrewise large sieves.** Fix a modulus `Q₀` (the small modulus). For
each `c mod Q₀`, the sifted numbers `n ≡ c` are written `n = c + Q₀m`,
with m in an interval of `N_c ≥ ⌊N/Q₀⌋` consecutive integers, and they
avoid `𝒜_c = {m : c + Q₀m ∈ 𝒜}`. In each fibre one applies its own
`N_c`-large-sieve system `(Θ_c, w_c)` (or the trivial bound), with its own
CRT-admissible lower bound. The total bound is `B = Σ_c 1/L_c`. This
covers the 2/3 note (`Q₀ = L_K ≤ N^{2δ}`, prime moduli `ℓ ≤ X`,
`ω_c(ℓ)` classes per fibre), Vaughan 1970 and Pomerance–Weingartner §4,
and every "excluded classes chosen fibrewise over a small modulus"
variant, including composite moduli inside the fibre.

The **W-rough level** of a rational θ = a/d is `λ(θ) = Σ_{ℓ | d, ℓ > W} log ℓ`
(W the absolute constant of KARY2 Thm 5.1). Put
`λ_Θ = max_c max_{θ∈Θ_{c,ℚ}} λ(θ)` and `λ(Q₀) = Σ_{ℓ|Q₀, ℓ>W} log ℓ`.

**Theorem 3.1 (large-sieve cap for forced-class mixtures; PROVED; the
Case-A part uses ElT Prop 1.4, as KARY2 does).** Let 𝔊 be any finite
mixture of ℛ(M)-, (a,D)-, Case-A and selector classes with arbitrary
moduli, `𝒜 = 𝒜(𝔊)`, `Q₀ ≤ N/2`, and let B be any fibrewise CRT-admissible
large-sieve bound for `A ⊂ 𝒜 ∩ I`, `|I| = N`. Put
`λ = max(λ₀, λ(Q₀) + 2λ_Θ)`. Then

    log(N/B) ≤ log 2 + C λ^{3/4}(log λ)^{3/4}.

If every modulus G of 𝔊 has `G ≤ P(G)^{1+B'}` (B' fixed), then
`log(N/B) ≤ log 2 + C(B')λ^{3/4}`.

*Proof.* In fibre c, Corollary 2.2 (applied to `𝒜_c`, which is
`M₀`-periodic) gives `1/L_c ≥ N_c·E ν_c` with `ν_c = |g*_c|² ≥ 0` on ℤ,
`≥ 1` on `𝒜_c`, and moduli `d | lcm(den θ, den θ')`, `θ,θ' ∈ Θ_{c,ℚ}`.
Put `ν_c ≡ 1` in fibres with the trivial bound, and `ν_c ≡ 0` if
`𝒜_c = ∅`. Define

    ν(n) = ν_c((n − c)/Q₀)   for n ≡ c (mod Q₀).

A term `a·1[m ≡ b (d)]` of `ν_c` becomes `a·1[n ≡ c + Q₀b (mod Q₀d)]`.
So ν is a real combination of class indicators, `ν ≥ 0` on ℤ, `ν ≥ 1` on
𝒜, and every modulus has W-rough level `≤ λ(Q₀) + 2λ_Θ ≤ λ`. Its mean is
`Eν = Q₀^{−1} Σ_c Eν_c`. Hence

    B = Σ_c 1/L_c ≥ ⌊N/Q₀⌋ Σ_c Eν_c = ⌊N/Q₀⌋ Q₀ Eν ≥ (N/2)·Eν.

KARY2 Thm 5.1 (resp. 5.2) gives `log(1/Eν) ≤ Cλ^{3/4}(log λ)^{3/4}`
(resp. `C(B')λ^{3/4}`). ∎

**Corollary 3.2 (the exceptional-set reading; PROVED, same proviso).** If
`Q₀ ≤ N^A` and every frequency used has denominator `≤ N^A` (for example
Montgomery's arithmetic large sieve with `Q ≤ N^{1/2}`, any set of moduli
`q ≤ Q` — prime, prime-power or composite — and any forced classes,
used fibrewise or not), then every such large-sieve bound for
`#(𝒜(𝔊) ∩ [1,N])` saves at most

    C_A (log N)^{3/4}(log log N)^{3/4},   and C_{A,B'}(log N)^{3/4} under bounded B'.

In particular **no CRT-admissible large sieve with polynomially bounded
frequency denominators proves `E(N) ≪ N exp(−(log N)^θ)` with θ > 3/4.**

*Proof.* `λ ≤ 3A log N`. ∎

**Remark 3.3 (what changed relative to ET Remark 2.6).** ET covered the
large sieve only for prime-slice systems, fibre by fibre, through
Rankin's bound on `S_c(Q)`. Theorem 3.1 needs no slice structure: the
classes may have any number of large primes, the moduli `q` of the large
sieve may be composite, and the lower bound may use the forced classes in
any CRT-admissible way (Cauchy–Schwarz over classes mod q, prime-power
components, or the exact `D_q(π)`). The price is the
`(log log N)^{3/4}` factor of KARY2 for unbounded B'. Note that
frequencies whose denominators contain primes not dividing `M₀` can be
discarded: averaging g* over the residue mod such a prime keeps
`Re g* ≥ 1` on 𝒜 (𝒜 does not see that prime) and does not increase
`Σ|γ|²/w`; so only primes of 𝔊 enter `λ_Θ`.

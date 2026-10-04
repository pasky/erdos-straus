# EXCEPTIONAL_LARGESIEVE — the large sieve over forced-class mixtures (task O17)

Status: **checkpoint 1 (unreviewed).** Labels follow
`DISCOVERIES.md`. Notation: ET = `EXCEPTIONAL_THETA.md`, KARY2 =
`EXCEPTIONAL_KARY2.md`, NONCRT = `EXCEPTIONAL_NONCRT.md`.

## 0. Summary

| item | statement | label |
|---|---|---|
| Thm 2.1, Cor 2.2 | **Exact duality.** For any frequency set Θ and weights w, the best CRT-admissible large-sieve denominator is `F*_w = 1/m_w`, `m_w = min{Σ|γ_θ|²/w_θ : Re Σγ_θe(−nθ) ≥ 1 on 𝒜}`. Since every N-large-sieve system has `w_θ ≤ 1/N`, every such bound is `≥ N·E|g*|²`, and `|g*|²` is a nonnegative CRT majorant whose moduli are lcm's of two frequency denominators | PROVED |
| Thm 3.1, Cor 3.2 | **Large-sieve cap for every forced-class mixture.** With KARY2 Thm 5.1: any CRT-admissible large sieve (Montgomery, weighted, Farey with prime, prime-power or composite moduli, forced classes used in any form, fibrewise over `Q₀`, weighted sequences) saves `≤ Cλ^{3/4}(log λ)^{3/4}`, `λ = λ(Q₀) + 2λ_Θ`. With denominators `≤ N^{O(1)}` and `Q₀ ≤ min(N^{O(1)}, N/2)`: `≤ C(log N)^{3/4}(log log N)^{3/4}`, and `C_B(log N)^{3/4}` under bounded B. No rounding term is needed | PROVED (Case A via ElT Prop 1.4, as in KARY2) |
| Thm 4.1, Cor 4.2, Rem 4.4 | **Prime-slice systems, any frequencies** (any denominators, sparse sets, any weights): Fourier–Rankin bound `saving ≤ α log N/(2(1−κ)) + log(2Q₀/|R|) + 8Σ p̄_ℓ ℓ^{−α}`; for ET Cor 3.4 families (also fibrewise, `Q₀ ≤ N/2`) `≤ C(log N)^{3/4} + log(P/φ(P))` | PROVED |
| Prop 5.1, Ex 5.2 | **Key question.** For prime moduli, `S_c(Q)` ≤ exp(Rankin functional of the prime-local system used), tautologically. For composite moduli the small-prime-conditioned Euler product does **not** dominate (twin classes are invisible to it but seen by the composite large sieve); the dominating functional is the top-prime sequential one (Thm 3.1) | PROVED |
| Thm 6.2, Cor 6.3 | **Larger-sieve kernels** `K = Σ_q w(q)1[q|m]` (composite q allowed) save `≤ log(1 + N·X(π)/(W−h))`, `X(π) = Σ_q (w(q)/q)χ²_q(π)` (χ² of the mod-q marginals, q as in the kernel) for any `π` on 𝒜. For **Gallagher's** weights (Λ on prime powers) this is `≤ X(π) + O(1)`, and `O(1)` on ET Cor 3.4 prime slices | PROVED |
| §7 | **Exact escape.** (E1) frequencies of super-polynomial level (`λ_Θ ≥ (log N)^{1+ε}`) against multi-large-prime classes, needing (H_LS); (E2) the larger sieve over mixtures, needing (H_Gal); (E3) non-CRT interval information; (E4) KARY2's inherited exclusions | (H_LS), (H_Gal): CONJECTURE/open |
| §8 | duality, `F* = S(Q)` for product systems, Ex 5.2, Thm 4.1 bound: checked on small systems | EVIDENCE |

**Bottom line.** The large-sieve door is closed for every form used in
the literature on this problem (Vaughan 1970, Pomerance–Weingartner §4,
the 2/3 note) and for all their composite-moduli/fibrewise variants: by
duality, the optimal large sieve *is* a Selberg-square CRT majorant of
level `≤ 2 log Q + log Q₀`, so KARY2's 3/4 cap applies with no rounding
term. The only remaining large-sieve escape is (E1): rational
frequencies with super-polynomially large denominators, which are
provably useless on prime slices and conjecturally useless in general.

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

Irrational θ are excluded **by definition**, not by proof: `S_A(θ)` is
not a function of `π_A`, so a residue-only lower bound cannot use them,
and dropping them only weakens (LS)'s left side. So the best
CRT-admissible bound is `Z ≤ 1/F*_w`. Throughout, "any frequencies"
means **any rational frequencies**.

**Scope of the definition (review D1).** The class is (LS) applied to
`a_n = 1_A(n)` (or to comparable weights, Remark 2.4), with residue-only
lower bounds. Not covered as stated:
* (LS) applied to *twisted* sequences `a_n = 1_A(n)ψ(n)` with ψ periodic
  but not constant on the fibres used;
* *hybrids*: the large sieve in some fibres and a majorant with
  coefficient-sum rounding (KARY2 Cor 6.1) in others. These should follow
  by the assembly of Theorem 3.1, after coarsening the majorant fibres
  with ET Lemma 2.9 as in KARY2 Cor 6.1, but this is not written out here
  (sketch only).

Neither form occurs in the literature on this problem.

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

**Remark 2.3 (what this says; framing).** Theorem 2.1 is standard
convex/Hilbert-space duality (the classical large-sieve/Selberg duality;
the projection theorem would do as well as minimax). It is **not**
claimed as new. The new content is the combination of Fact 1.1 with the
level count of Theorem 3.1, which feeds the large sieve into KARY2
Thm 5.1. The best bound any CRT-admissible large
sieve can give, with any rational frequencies, any composite moduli and any
weights, is at least `N` times the mean of a Selberg-square majorant
`|g|²`, nonnegative on ℤ, built from the characters the large sieve
uses. This is the classical large-sieve/Selberg duality, made exact and
extended to arbitrary class systems. Unlike KARY2 Cor 6.1 there is no
rounding term: the factor `N + δ^{−1} ≥ N` of the large sieve already
contains N. So the cap needs only the **level** of `ν*`, not its
coefficient sum.

**Remark 2.4 (weighted sifted sequences; PROVED).** If the large sieve
is applied to weights `a_n ≥ 0` supported on `𝒜 ∩ I`, (LS) gives
`(Σa)²·F_w(π_a) ≤ Σa²` with `π_a = a/Σa ∈ P(𝒜)` (after reduction mod
`M'`). The CRT-admissible optimum is `Σa ≤ (Σa²/Σa)·m_w`. To use it a
method needs a known upper bound `U ≥ Σa²/Σa`; its final bound is
`U·m_w ≥ U·N·Eν*`. So, relative to the trivial bound `N·U`, the saving is
at most `log(1/Eν*)`. For example, for indicators `U = 1`. For `Λ` on
primes in `(N/2, N]` one may take `U = log N`; the final bound is
`≥ N log N·Eν* ≥ (N/2)·Eν*`, so even relative to the Chebyshev value
`N/2` the saving is at most `log(1/Eν*)`. Some such U is needed. If a method could use
`Σa²/Σa` itself, no ceiling holds: take one weight 1 and the others
`N^{−1/2}`. In the results below, "weighted sequences" always carries
this proviso.

**Remark 2.5 (the multiplicative large sieve is covered; PROVED).** For
primitive χ mod q, `τ(χ̄)χ(n) = Σ_{a mod q} χ̄(a)e(an/q)` with
`|τ(χ̄)|² = q`. Hence, for every finite measure π on `ℤ/M'` (q | M'),

    q Σ_{χ prim mod q} |Σ_n π(n)χ(n)|² ≤ Σ_{χ mod q} |Σ*_a χ̄(a)π̂(a/q)|² = φ(q)·D_q(π).

So the character functional `Σ_{q≤Q}(q/φ(q))Σ*_χ|π̂(χ)|²` is at most the
Farey functional `F_1(π) = Σ_{q≤Q}D_q(π)`, **pointwise in π**. Every
CRT-admissible lower bound `L` in character form is therefore also one
for the additive Farey system with the same `N + Q²`. Theorem 3.1 applies
with `λ_Θ ≤ log Q`.

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
(resp. `C(B')λ^{3/4}`). The W-smooth parts of ν's moduli are unbounded
here (e.g. Farey `q = 2^k`, or the smooth part of Q₀). KARY2 Thm 5.1
allows this as stated: its level charges only primes `ℓ > W`.
Mechanically, either project ν onto moduli `gcd(·, M₀)` as in KARY2
Cor 6.1 (mean unchanged, still a majorant), or lift the base `R_W^□` to
the higher prime powers. Unit squares mod `p^e` have density
`(p−1)/(2p)` (p odd) or `1/8` (`p = 2`, `e ≥ 3`) at every exponent, so
the R-term stays `≤ 2W`. ∎

**Corollary 3.2 (the exceptional-set reading; PROVED, same proviso).** If
`Q₀ ≤ min(N^A, N/2)` and every frequency used has denominator `≤ N^A` (for example
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
`(log log N)^{3/4}` factor of KARY2 for unbounded B'.

*Sharpening (review D4).* Replace g* by its conditional average
`E[g*(n') | n' ≡ n (mod M₀)]` (in a fibre: modulo the period of `𝒜_c`).
This keeps `Re g ≥ 1` on 𝒜, since 𝒜 is a union of classes mod `M₀`. It
does not increase `Σ|γ|²/w`, and it kills **every** frequency whose
denominator does not divide `M₀`. So `m_w(Θ) = m_w(Θ ∩ M₀^{−1}ℤ)`, and in
Theorem 3.1 `λ_Θ` may be taken over the frequencies with
`den θ | M₀` only. Frequencies whose denominators involve anything not
seen by the family are useless.

**Remark 3.4 (the campaign's and the literature's large sieves are
instances; review D3).**
* *The 2/3 note* (`paper/vaughan-loglog-note.tex` §5, re-read for this
  check):
  * small modulus `Q₀ = M = L_K ≤ N^{2δ}`, `δ < 1/4`, so `Q₀ ≤ N/2`,
    with `λ(Q₀) ≤ 2δ log N`;
  * in fibre c it applies Montgomery's (LS) with `Q = Y^{1/2}`,
    `Y = N/M`, over squarefree `s ≤ Q`, so `λ_Θ ≤ ½ log N`;
  * the excluded classes `Ω_c(ℓ)`, `ℓ ∈ (X^{1/2}, X]`, `ℓ ≡ 3 (4)`, come
    from its Lemma "identity": `n ≡ −uv^{−1} (mod kℓ)` with
    `kℓ ≡ −1 (4)` and `(kℓ+1)/4 = uvw`. These are ℛ(kℓ)-classes, the
    same atoms as the 3/4 note's (KARY2 Remark 5.4);
  * `k | L_K` with `k ≤ K = δ log N = ℓ^{o(1)}`, so the moduli satisfy
    `kℓ ≤ ℓ^{1+B'}` with B' small: Theorem 5.2 of KARY2 applies with no
    loglog loss.

  Take 𝔊 = these classes plus the selector classes `0 mod p`, `p ≤ K`.
  Then the non-reduced fibres are empty (`ν_c = 0`). The note's added
  `K` (primes `≤ K`) and its semigroup transfer `E_pr → E` only enlarge
  or post-process the bound. Its large-sieve part is therefore `≥ (N/2)Eν`
  with ν of level `≤ (½ + 2δ) log N`, and Theorem 3.1 caps it at
  `C(log N)^{3/4}`. The note's actual saving `(log N)^{2/3}(log log N)^{1/3}`
  is consistent with this.
* *Vaughan 1970 and Pomerance–Weingartner §4* are described in the 2/3
  note's introduction as the same architecture: prime moduli,
  `ω_c(ℓ)` classes, and Montgomery's (LS) in reduced fibres. They are
  covered by the same check **on that description**. Neither paper was
  re-read for this remark.
* *The 3/4 note* uses a majorant with coefficient-sum rounding, not the
  large sieve (KARY2 Remark 5.4).

## 4. Arbitrary frequencies over prime-slice systems: a Fourier–Rankin bound

Theorem 3.1 needs the frequencies to have bounded level. For prime-slice
systems (ET §1) no level condition is needed at all: one product measure
on 𝒜 has small Fourier transform in an `ℓ^{2+2β}` sense, and Hölder
does the rest.

**Fact 4.0 (trace bound; PROVED).** In every N-large-sieve system,
`Σ_θ w_θ ≤ 1`. *Proof.* Average (LS) over independent random signs
`a_n = ±1`: `E|Σ_n a_n e(nθ)|² = N`, so `N Σ_θ w_θ ≤ N`. ∎

**Theorem 4.1 (large-sieve cap for prime-slice systems, any frequencies;
PROVED).** Take a prime-slice system `(Q₀, R, 𝒫, F_ℓ(c))` as in ET §1
(classes mod `q₀ℓ`, `q₀ | Q₀`, `ℓ ∈ 𝒫` prime, `ℓ ∤ Q₀`). Assume, for some
`0 ≤ κ < 1` and all `c ∈ R`, `ℓ ∈ 𝒫`:

    f_ℓ(c) := |F_ℓ(c)| ≤ min(ℓ/2, ℓ^κ).

Put `p̄_ℓ = E_{c∈R} f_ℓ(c)/ℓ` (no truncation). Then every CRT-admissible
bound B from any N-large-sieve system `(Θ,w)` — any frequencies, any
denominators, any weights — for `A ⊂ 𝒜 ∩ I` satisfies, for every
`0 < α ≤ 1−κ`,

    log(N/B) ≤ α log N/(2(1−κ)) + log(2Q₀/|R|) + 8 Σ_{ℓ∈𝒫} p̄_ℓ ℓ^{−α}.   (4.1)

*Proof.* Put `β = α/(2(1−κ)) ≤ 1/2` and `p' = 2+2β`.

*Good fibres.* Let `Σ(c) = Σ_ℓ 4 f_ℓ(c)/ℓ · ℓ^{−α}` and
`R' = {c ∈ R : Σ(c) ≤ 2 E_R Σ}`; by Markov `|R'| ≥ |R|/2`.

*The measure.* Let `M'` be as in §1, and let π be the law of n mod `M'`
for which: `n mod Q₀ = c` is uniform on `R'`; given c, the residues
`n mod ℓ` (ℓ ∈ 𝒫) are independent and uniform on `ℤ/ℓ ∖ F_ℓ(c)`; all
remaining CRT digits (higher powers of primes of `Q₀` and of ℓ ∈ 𝒫,
and other primes) are uniform given these. Then π is supported on 𝒜
(`f_ℓ(c) < ℓ`).

*Its Fourier transform.* Let θ ∈ `M'^{−1}ℤ/ℤ`. If its denominator has a
prime-power factor that is not resolved by the coordinates above (a
prime outside `Q₀𝒫`, `ℓ²` with ℓ ∈ 𝒫, or a power of a prime of Q₀
beyond its exponent in Q₀), then `π̂(θ) = 0`, since that digit is uniform
given the rest. Otherwise `θ = θ₀ + Σ_{ℓ∈S} a_ℓ/ℓ` with `den θ₀ | Q₀`,
S ⊂ 𝒫 finite, `ℓ ∤ a_ℓ`, and

    π̂(θ) = E_{c∈R'} [ e(θ₀c) Π_{ℓ∈S} φ_{ℓ,c}(a_ℓ) ],
    φ_{ℓ,c}(a) = E[e(a n/ℓ) | c] = −(ℓ−f_ℓ(c))^{−1} Σ_{b∈F_ℓ(c)} e(ab/ℓ).

Put `g_ℓ(c) = f_ℓ(c)/(ℓ−f_ℓ(c)) ≤ 2f_ℓ(c)/ℓ`. Then
`|φ_{ℓ,c}(a)| ≤ g_ℓ(c)` and, by Parseval mod ℓ,
`Σ_{a≢0}|φ_{ℓ,c}(a)|² = (ℓf − f²)/(ℓ−f)² = g_ℓ(c)`. Hence

    Σ_{a≢0} |φ_{ℓ,c}(a)|^{p'} ≤ g_ℓ(c)^{1+2β} ≤ 2^{2β}·(2f/ℓ)·ℓ^{−2β(1−κ)} ≤ 4 (f_ℓ(c)/ℓ) ℓ^{−α},

using `g ≤ 2f/ℓ ≤ 2ℓ^{κ−1}` and `2^{2β} ≤ 2`.

*Hausdorff–Young in the small coordinate.* Fix S and `(a_ℓ)`, and put
`X(c) = Π_{ℓ∈S} φ_{ℓ,c}(a_ℓ)`, `|X| ≤ 1`, and
`f(c) = (Q₀/|R'|) 1_{R'}(c) X(c)` on `ℤ/Q₀`. Then
`π̂(θ₀ + Σ a_ℓ/ℓ) = E_{c∈ℤ/Q₀} f(c) e(θ₀c) = f̂(θ₀)`. Hausdorff–Young on
the finite abelian group `ℤ/Q₀` (uniform probability on the group,
counting measure on the dual), with `p = p'/(p'−1) ∈ [1,2]`, gives

    Σ_{θ₀} |f̂(θ₀)|^{p'} ≤ ‖f‖_p^{p'} = (Q₀/|R'|) (E_{R'}|X|^p)^{p'/p}
                        ≤ (Q₀/|R'|) E_{R'} |X|^{p'}

(the last step is Jensen, `p'/p ≥ 1`). Summing over all S and `(a_ℓ)`,

    𝓡 := Σ_θ |π̂(θ)|^{p'} ≤ (Q₀/|R'|) E_{c∈R'} Π_{ℓ∈𝒫} (1 + Σ_{a≢0}|φ_{ℓ,c}(a)|^{p'})
       ≤ (2Q₀/|R|) E_{R'} e^{Σ(c)} ≤ (2Q₀/|R|) exp(8 Σ_ℓ p̄_ℓ ℓ^{−α}).

*Hölder.* With Fact 4.0 and Fact 1.1,

    F_w(π) = Σ_θ w_θ|π̂(θ)|² ≤ (Σ_θ w_θ)^{β/(1+β)} (Σ_θ w_θ|π̂(θ)|^{p'})^{1/(1+β)}
           ≤ (𝓡/N)^{1/(1+β)}.

So `B ≥ 1/F*_w ≥ 1/F_w(π) ≥ (N/𝓡)^{1/(1+β)}`, i.e.
`log(N/B) ≤ (β log N + log 𝓡)/(1+β) ≤ β log N + log⁺ 𝓡`. ∎

**Corollary 4.2 (ET Cor 3.4 families, any large sieve; PROVED).** For
the families of ET Cor 3.4 (forced classes of Lemma 16.1/3.2, and Case A
via ET Lemma 3.7; moduli `q₀ℓ` with `q₀ ≤ ℓ^C`, C < 1; selector R),
every CRT-admissible large-sieve bound — any frequency set, including
sparse sets of rationals with huge denominators — saves at most

    C'(C)(log N)^{3/4} + log(P/φ(P)) + log 2.

*Proof.* ET Cor 3.4's proof gives `f_ℓ(c) ≤ ℓ^{C+o(1)} ≤ min(ℓ/2, ℓ^κ)`
with `κ = (1+C)/2` for `ℓ ≥ ℓ₀(C)`, and
`Σ_ℓ p̄_ℓ ℓ^{−α} ≪ α^{−3}` (untruncated; Lemmas 3.1, 3.2, 3.7); and
`Q₀/|R| = P/φ(P)`. Take `α = (log N)^{−1/4}` in (4.1). ∎

**Remark 4.3.** Theorem 4.1 closes the ET Remark 2.6 case completely:
there the large sieve was covered only through `S_c(Q)` (Farey
frequencies, prime moduli). Here any `(Θ,w)` is allowed, and the
exponent of `N` enters only through `β log N`, a Rankin term in
frequency space. The mechanism is the product structure in each fibre:
`|π̂(θ)|` decays by a factor `g_ℓ(c)` for **every** slice prime in the
denominator. For mixtures with several large primes per modulus there is
no such product measure; see §7.

**Remark 4.4 (fibrewise over Q₀; PROVED).** ET Remark 2.6's large sieve
runs fibre by fibre over `c mod Q₀`. In fibre `c ∈ R`, `n = c + Q₀m`,
the set `𝒜_c` is a pure product system in m (the slice classes become
`m ∉ Q₀^{−1}(F_ℓ(c) − c) mod ℓ`), so Theorem 4.1 applies with small
modulus 1 and no Markov step:
`log(N_c/B_c) ≤ β log N_c + 4Σ_ℓ (f_ℓ(c)/ℓ)ℓ^{−α}`, any frequencies in
each fibre. Fibres `c ∉ R` are empty. Jensen over `c ∈ R` and
`N_c ≥ ⌊N/Q₀⌋` (assume `Q₀ ≤ N/2`, so `Q₀⌊N/Q₀⌋ ≥ N/2`) give the total saving
`≤ log 2 + log(Q₀/|R|) + β log N + 4Σ_ℓ p̄_ℓ ℓ^{−α}`.

## 5. The key question: is `S(Q)` dominated by a Rankin functional?

**5.1 Prime moduli: yes, tautologically.** The arithmetic large sieve
with prime moduli, in fibre c over a small modulus Q₀, uses sets
`Ω_c(ℓ) ⊂ ℤ/ℓ` (ℓ ∤ Q₀) of classes that `𝒜_c` avoids. The largest
admissible choice is the *induced prime-local system*
`Ω_c(ℓ) = ℤ/ℓ ∖ (𝒜_c mod ℓ)`. It contains, for each class `b (mod q₀ℓ)` of
𝔊 with `q₀ | Q₀` and `b ≡ c (q₀)`, the class `b mod ℓ`, and possibly more
(fibres mod ℓ covered by classes with other primes). With
`g_ℓ = ω_c(ℓ)/(ℓ−ω_c(ℓ))` and any `α > 0`, Rankin gives

    S_c(Q) = Σ_{s≤Q} μ²(s) Π_{ℓ|s} g_ℓ ≤ Q^α Π_ℓ (1 + g_ℓ ℓ^{−α}),        (5.1)

and by Jensen over fibres, `Σ_c Y/S_c(Q) ≥ |R|·Y·exp(−avg_c log S_c(Q))`.
So the saving of any prime-modulus large sieve is at most the averaged
Rankin functional of whatever prime-local system it uses (ET Remark 2.6).
For Farey frequencies this is also a special case of Theorem 3.1, so no
mass estimate for `Ω_c(ℓ)` (including covered fibres) is needed.

**5.2 Composite moduli: no; the small-prime-conditioned Euler product
does not dominate.** Once the large sieve uses composite moduli, its
denominator is `F*_w` (Theorem 2.1), not a truncated Euler product, and
it can see classes with two or more large primes that are invisible to
every prime-local system obtained by conditioning on small primes.

**Example 5.2 (PROVED).** Let `{(ℓ_j, ℓ'_j)}` be disjoint pairs of
primes `> W`, with `m_j = ℓ_jℓ'_j ≡ 3 (mod 4)` (e.g. `ℓ_j ≡ 1`,
`ℓ'_j ≡ 3 (mod 4)`), and let 𝔊 consist of the ℛ(m_j)-classes, `ω_j`
of them mod `m_j`. Take `ℓ_j < ℓ'_j < ℓ_j²` with `ℓ_j` large, so that
`1 ≤ ω_j ≤ τ(A_{m_j}²) ≤ m_j^{o(1)} < ℓ_j`. Let Q₀ be coprime to all `m_j`. Then:
1. the induced prime-local system is empty: `Ω_c(ℓ) = ∅` for every c and
   every prime ℓ, so `S_c(Q) = 1` for every Q and the prime-modulus
   arithmetic large sieve saves nothing;
2. the large sieve with the composite modulus `m_j` (frequencies `a/d`,
   `d | m_j`, weight `w = (N+m_j²)^{−1}`) has
   `F*_w ≥ w·(1 + g_j)`, `g_j = ω_j/(m_j − ω_j) > 0`.

*Proof.* By CRT, 𝒜 is a product over the pairs of
`(ℤ/m_j ∖ F_j)` times free coordinates. 1. Given `n ≡ b (mod ℓ_j)`, the
classes of `F_j` exclude at most `ω_j < ℓ'_j` residues mod `ℓ'_j`, and the
other coordinates are unconstrained; so every residue mod ℓ (ℓ a pair
prime) and every residue mod any other prime occurs in `𝒜_c`. 2. For
π ∈ P(𝒜), `π mod m_j` is supported on the `m_j − ω_j` residues outside
`F_j`. By Parseval mod `m_j` and Cauchy–Schwarz,
`Σ_{d|m_j} D_d(π) = m_j Σ_b π(n≡b (m_j))² ≥ m_j/(m_j − ω_j)`. ∎

So "S(Q) ≤ exp(Rankin functional of the prime-local system induced by
conditioning on small primes)" fails as soon as composite moduli are
allowed. The saving in Example 5.2 is tiny, but by ET Lemma 3.8 the
balanced moduli (no dominant prime) carry `≫ (log x)³` of the ES supply,
so the mass that the small-prime-conditioned system misses is not lower
order. **The functional that does dominate is the sequential one:**
condition at each prime ℓ on the residues at *all* smaller primes and
count the classes decided at ℓ (their top prime). That is the KARY
construction, and Theorem 3.1 transfers its cap to the large sieve
through duality. The answer to the key question is therefore:
dominated by the top-prime sequential functional (Theorem 3.1, for
polynomial-level frequencies), not by the small-prime-conditioned Euler
product (Example 5.2); for prime-slice systems the two coincide
(Theorem 4.1).

## 6. Gallagher's larger sieve and its kernel variants

**Setting.** Take moduli `𝒮` with weights `w(q) ≥ 0`, the kernel
`K(m) = Σ_{q∈𝒮} w(q) 1[q | m]`, `W = K(0) = Σ_q w(q)`, and any
`h ≥ max_{0<|m|<N} K(m)`. For `A ⊂ I`, `|I| = N`,

    Z² Σ_q w(q) coll_q(π_A) = Σ_{n,n'∈A} K(n−n') ≤ Z·W + (Z² − Z)·h,

with `coll_q(π) = Σ_b π(n ≡ b (q))²`. Hence `Z ≤ (W−h)/(D(π_A) − h)`
whenever `D(π) := Σ_q w(q) coll_q(π) > h`. Gallagher's larger sieve is
`𝒮` = prime powers `≤ Q`, `w = Λ`, `h = log N`, with Cauchy–Schwarz
`coll_q ≥ 1/ν(q)`. The CRT-admissible optimum is `Z ≤ (W−h)/(D* − h)`,
`D* = min_{π∈P(𝒜)} D(π)`; composite moduli and the forced classes in any
form are allowed in `𝒮`.

Write `χ²_q(π) = q·coll_q(π) − 1` (the χ²-distance of `π mod q` from
uniform) and

    X(π) = Σ_{q∈𝒮} (w(q)/q) χ²_q(π).

**Lemma 6.1 (PROVED).** `D_u := Σ_q w(q)/q ≤ h + (W − h)/N`.
*Proof.* Count pairs in I: `Σ_{n,n'∈I} K(n−n') ≤ NW + (N²−N)h`, while by
Cauchy–Schwarz over residues mod q it is `≥ Σ_q w(q) N²/q`. ∎

**Theorem 6.2 (larger-sieve cap by a χ² functional; PROVED).** For every
π ∈ P(𝒜), every CRT-admissible kernel bound B satisfies

    log(N/B) ≤ log(1 + N·X(π)/(W − h)).

For Gallagher's sieve (`w = Λ`, prime powers `≤ Q`, `h = log N`) this
gives `log(N/B) ≤ X(π) + c₁` with an absolute `c₁`, unless
`X(π) ≥ (log N)/3`.

*Proof.* Since `coll_q ≤ 1`, `D ≤ W`; so a bound exists only if `W > h`.
`D* ≤ D(π) = D_u + X(π)`, so by Lemma 6.1
`D* − h ≤ (W−h)/N + X(π)` and `B ≥ (W−h)/((W−h)/N + X(π))`.
Gallagher: `D_u ≤ log Q + c₀` (Mertens), so `D* > h` forces
`Q ≥ N e^{−c₀−X}`. If `X < (log N)/3` and N is large, then `ψ(Q) ≥ Q/2 ≥
2 log N`, so `W − h ≥ Q/4`, and with `u = D(π) − h ∈ (0, log(Q/N)+c₀+X]`,
`B ≥ (Q/4)/u ≥ (N/4)e^{u−c₀−X}/u ≥ (N/4)e^{1−c₀−X}`. ∎

**Corollary 6.3 (prime-slice systems; PROVED).** For a prime-slice system
with `f_ℓ(c) ≤ ℓ/2`, a selector `R = {(c,P)=1}` (`P | Q₀`), and `Σ_ℓ p̄_ℓ ℓ^{−1/2} ≤ K₀`, Gallagher's larger sieve (any
Q) saves at most `C(1 + K₀)`. For ET Cor 3.4 families this is `O(1)`.

*Proof.* Take the product measure of Theorem 4.1 with `R' = R`. For
`ℓ ∈ 𝒫`: `π mod ℓ^v` is `π mod ℓ` lifted uniformly, and by convexity of
χ² in its first argument `χ²_{ℓ^v}(π) ≤ E_R χ²(Unif(ℤ/ℓ∖F_ℓ(c))) =
E_R g_ℓ(c) ≤ 2p̄_ℓ`. For `p | P`: `π mod p^v` is uniform on units mod `p^v` (for
`p^v | Q₀`) or that lifted uniformly, so `χ² = 1/(p−1)`. Other primes
(including `p | Q₀`, `p ∤ P`): χ² = 0. Hence
`X(π) ≤ Σ_ℓ 4p̄_ℓ log ℓ/ℓ + Σ_p 2 log p/(p(p−1)) ≤ C(1+K₀)`. Theorem 6.2. ∎

For general kernels with composite q, `X` involves the mod-q marginals
for those composite q, and Cor 6.3 does not apply: e.g. the single
kernel `𝒮 = {P}` (`h = 0`, `N ≤ P`) with the selector `R = {(c,P)=1}`
saves `log(P/φ(P))` — exactly the R-term, as for majorants.

So on prime slices Gallagher's larger sieve does not even reach the
`(log N)^{3/4}` scale: it is designed for sets occupying few classes,
and forced-class avoiders occupy almost all classes.

**Mixtures (open, precisely).** For a general mixture, Theorem 6.2
reduces the cap to the existence of `π ∈ P(𝒜)` whose prime-power
marginals are near uniform:

> **(H_Gal)** there is `π ∈ P(𝒜(𝔊))` with
> `Σ_{ℓ^v≤Q} (log ℓ/ℓ^v) χ²_{ℓ^v}(π) ≤ C(log N)^{3/4}` (Q ≤ N^{O(1)}).

The square base gives this for `ℓ ≤ W` (cost `O(W)`). For `ℓ > W` the
natural candidate is the KARY sequential law conditioned on no leak;
before conditioning its marginals satisfy `χ²_ℓ ≤ E g_ℓ`, but the
conditioning on the leak event may correlate with `n mod ℓ`, and that
correlation is not controlled here. Note also that the Cauchy–Schwarz
form `coll_q ≥ 1/ν(q)` only needs `|𝒜 mod ℓ^v|` close to `ℓ^v`; the
squares give `𝒜 mod ℓ ⊇` the quadratic residues (KARY2 Lemmas 2.1–2.2),
which is too weak by a factor 2. (H_Gal) is **open**; the larger sieve
over mixtures is not covered.

## 7. Where the large sieve can still escape (exact form)

Combining §§3–6, a CRT-admissible large-sieve-type bound for a
forced-class mixture can save more than `C(log N)^{3/4}(log log N)^{3/4}`
only in the following forms (all with `Q₀ ≤ min(N^{O(1)}, N/2)`).

**(E1) Frequencies of super-polynomial level against multi-large-prime
classes.** By Theorem 3.1 the saving is `≤ Cλ^{3/4}(log λ)^{3/4}` with
`λ = λ(Q₀) + 2λ_Θ` **for every level**. So a saving
`≥ (log N)^{3/4+ε}` needs, for N large, `λ_Θ ≥ (log N)^{1+ε}`:
frequencies `a/d` whose W-rough part of `d` exceeds `N^{(log N)^ε}`. Such
points are allowed in Montgomery's inequality (it only needs δ-spacing
with `δ^{−1} ≲ N`, and by Fact 4.0 the total weight is ≤ 1), but they
are useful only if `𝒜` has non-product structure across many large
primes: for prime-slice systems Theorem 4.1 shows they are useless. The
missing input is a measure on 𝒜 with Fourier decay at every large prime
of the denominator:

> **(H_LS)** there is `π ∈ P(𝒜(𝔊))` and `β ≍ (log N)^{−1/4}` with
> `log Σ_θ |π̂(θ)|^{2+2β} ≤ C(log N)^{3/4}·polylog`.

By the Hölder step of Theorem 4.1, (H_LS) caps **every** N-large-sieve
system, any frequencies. For KARY's sequential law the transform decays
at the top prime of the denominator only (`|E[e(a n/ℓ) | history]| ≤
g_ℓ`); products over several large primes would need conditional
independence that classes such as ℛ(ℓ₁ℓ₂) destroy. (H_LS) is
**CONJECTURE**; heuristically the Fourier coefficients of 𝒜 at
high-level frequencies behave like those of a random set of the same
local densities, and no escape is expected.

**(E2) The larger sieve over mixtures.** Theorem 6.2 caps it by the
χ²-functional `X(π)`; the cap for mixtures needs (H_Gal) (§6), open.

**(E3) Non-CRT information.** Bounds that use that `π_A` is the
empirical law of a set in a short interval (not just a law on 𝒜) are
outside the definition of CRT-admissible; this is the "direct interval
count" exclusion of NONCRT §2.4 and KARY2 §6. The large sieve inequality
itself uses the interval (through `N + δ^{−1}`), but only through the
factor N, which the theorems keep.

**(E4) Inherited exclusions.** The `(log log N)^{3/4}` factor for
unbounded-B mixtures, other class types, and the Case-A dependence on ElT
Prop 1.4 are inherited from KARY2 Thm 5.1 through Theorem 3.1.

Everything else is closed: Montgomery's inequality and its weighted
forms, any Farey-type frequency set with denominators `≤ N^{O(1)}`,
prime, prime-power and composite moduli, forced classes of composite
moduli used through prime-power components or directly, excluded
classes chosen fibrewise over any modulus `Q₀ ≤ min(N^{O(1)}, N/2)`,
weighted sequences with comparable weights (Theorem 3.1, Remark 2.4);
and, for the ET Cor 3.4 prime-slice families, every large sieve system
whatsoever (Cor 4.2, Remark 4.4) and Gallagher's larger sieve (Corollary
6.3, saving O(1)). Theorem 4.1 itself is a bound, not a cap: it keeps
the R-term `log(Q₀/|R|)` and the supply functional `Σp̄_ℓℓ^{−α}`, which
must be bounded for the family at hand.

## 8. Numerics (EVIDENCE only)

`scripts/ls_duality_check.py` (~10 s, cvxpy):
1. Theorem 2.1 on 12 random class systems (moduli products of 1–2 primes
   from {3,…,13}, random weights; 6 Farey sets and 6 sparse sets of
   5 random nonzero frequencies plus 0, not closed under conjugation):
   the two QPs give `F*_w·m_w = 1` to `1.2·10⁻¹⁴`. Degenerate case (no
   classes, Θ without 0): `F* = 0` and the dual is infeasible, as the
   theorem says. Solver status and all tolerances are asserted.
2. Prime-only systems with Farey frequencies: `F*_1 = S(Q)` to `5·10⁻¹⁴`
   in 8 cases. So for product systems the arithmetic large sieve
   (Montgomery's lemma) is already the CRT-optimal large sieve; the
   uniform measure on 𝒜 attains `F*`.
3. Analogues of Example 5.2 with `m = 35 = 5·7` and `143 = 11·13`
   (these violate its crude sufficient condition `ω_j < ℓ_j`: ω = 5, 22;
   emptiness is checked directly): all residues mod 5, 7, 11, 13 occur
   in 𝒜 (prime-local system empty), while
   `F*` over the divisors of m equals `m/(m−ω)` = 1.1667, 1.1818.
4. Theorem 4.1's bound `𝓡(π) ≤ (Q₀/|R|)E_R Π(1+Σ|φ|^{p'})` on 6 random
   prime-slice systems (`Q₀ = 4`, slice primes 5, 7, 11): holds, with
   ratios 0.89–0.97.

## Replay

```
PYTHONPATH=scripts uv run --with cvxpy --with numpy python scripts/ls_duality_check.py   # ~10 s
```

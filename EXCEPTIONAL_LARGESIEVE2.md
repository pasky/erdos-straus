# EXCEPTIONAL_LARGESIEVE2 — the remaining large-sieve and prime-law escapes (task O27)

Status: **checkpoint 2.** Hostile review R27
(`reviews/exceptional-largesieve2-review.md`, branch
`side-agent/review-largesieve2`): all claims SOUND, no FATAL/MAJOR; minor
m1–m6 applied. Labels as in
`DISCOVERIES.md`. Notation: LS = `EXCEPTIONAL_LARGESIEVE.md`, K2 =
`EXCEPTIONAL_KARY2.md`, EK = `EXCEPTIONAL_KARY.md`, PL =
`EXCEPTIONAL_PRIMELAW.md`, ET = `EXCEPTIONAL_THETA.md`.

Throughout, 𝔊 is a finite mixture of ℛ(M)-, (a,D)-, Case-A and selector
classes with arbitrary moduli (K2 Def. 2.0), `𝒜 = 𝒜(𝔊) ⊂ ℤ` its avoider
set, `M₀` the lcm of its moduli. "Level" means W-rough level,
`λ(d) = Σ_{ℓ | d, ℓ > W} log ℓ`, with W the absolute constant of K2
Thm 5.1. `S(λ) := C λ^{3/4}(log λ)^{3/4}` denotes the right side of K2
Thm 5.1 (`λ ≥ λ₀`), and `S_B(λ) = C(B)λ^{3/4}` that of K2 Thm 5.2.

**Update (KARY3, ledger (D)24).** `EXCEPTIONAL_KARY3.md` Thm 4.1 removes the
`(log λ)^{3/4}` loss from K2 Thm 5.1 for every mixture (no B): one may take
`S(λ) = Cλ^{3/4}` throughout, with KARY3's dependencies (K2/EK as reviewed;
Case A via ElT §7, published, not re-proved). Every result below that cites
K2 Thm 5.1 (Lemma 1.1, Thms 2.4, 4.2, Cor 2.5, Prop 5.1) therefore holds
with `S(λ) = Cλ^{3/4}`, and its exceptional-set reading becomes
`C_A(log N)^{3/4}` — the `(log log N)^{3/4}` factor drops. For the
unit-measure results (Lemma 1.2, Thm 3.1) the same holds via KARY3 §4.3's
transfer to PL Thm 3.1, which is stated there at pointer level only.
Theorem 4.3 does not use K2 Thm 5.1 and is unaffected.

## 0. Summary

| item | statement | label |
|---|---|---|
| Lemma 1.1, 1.2 | **comparison measure**: K2 Thm 5.1 (resp. PL Thm 3.1) is equivalent, by LP duality, to the existence of one π on 𝒜 (resp. on 𝒜 ∩ units) with `E_π f ≤ e^{S(λ)}E_U f` (resp. `E*f`) for **every** nonnegative f of level ≤ λ | PROVED, conditional on K2 Thm 5.1 / PL Thm 3.1 |
| Thm 2.4, Cor 2.5 | **periodic Bessel systems, twisted, hybrid**: any inequality `Σ_j|Σ a_n φ̄_j(n)|² ≤ ΔΣ|a_n|²` with periodic rows of level ≤ λ_Φ, applied to `a_n = ψ(n)1_A(n)` with any periodic twist `|ψ| ≥ 1` on 𝒜 (any period), fibrewise over `Q₀`, mixed with majorant-with-rounding fibres: `B ≥ (N/2)e^{−S(λ)}`; saving `≤ C_A(log N)^{3/4}(log log N)^{3/4}` for polynomial periods (`C_A(log N)^{3/4}` with KARY3 Thm 4.1). Covers multiplicative × additive, Gauss-sum twisted and hybrid forms (escape 3) | PROVED, conditional on K2 Thm 5.1 (internal) |
| Thm 3.1 | **large sieve applied to the primes** of the sifted set (PL §6 item 5): same cap relative to `π(N)`, when all primes of `M'` (family, rows, twists, `Q₀`) are `≤ N^A` | PROVED, conditional on PL Thm 3.1 |
| Lemma 4.1, Thm 4.2 | **larger sieve, any kernel** = a Bessel functional minus the zero frequency; CRT-optimal kernel bounds are `≥ (N/2)e^{−S(2λ_𝒮)}/(1 + Nh/(W_K−h))`; a cap only where the factor `1+Nh/(W_K−h)` is controlled (composite kernels with `W_K − h ≪ Nh` stay open) | PROVED, conditional on K2 Thm 5.1 |
| **Thm 4.3** | **(H_Gal) holds**: for every mixture there is π on 𝒜 with `Σ_{ℓ^v≤Q}(log ℓ/ℓ^v)χ²_{ℓ^v}(π) ≤ 24 log log 3Q + C`; Gallagher's larger sieve (CRT-optimal and Cauchy–Schwarz forms, any Q) saves `≤ 26 log log N + C` over **any** forced-class mixture (LS (E2a), (E2b) closed) | PROVED, **unconditional** (K2 Lemmas 2.3, 3.1, 4.1–4.3, EK Lemma 2.1; Shiu and Mertens, no ElT Prop 1.4) |
| Prop 5.1, 5.2 | (E1) sharpened: a saving `≥ (log N)^{3/4+ε}` needs frequencies whose denominators have `≥ (log N)^{4ε/3−o(1)}` distinct family primes; a different sufficient criterion: (a) Lemma 1.1 at level `2λ'` plus (b) a **sup** bound `|π̂(θ)|² ≤ e^{S}/N` at level `> λ'` for the same π (no cross terms) | PROVED (reduction); (H_LS∞) CONJECTURE |
| Prop 6.1 | the finite-range prime relaxation ("ν ≥ 1 only at primes of 𝒜 ∩ [1,N]") has LP value equal to the exact count, at level `log 2N`, so **no cap of any kind** holds for it; the gap is certification (non-CRT), not majorant design. It does **not** cover the other relaxation (`ν ≥ 0` only at primes `≤ N`, `ν ≥ 1` on all primes of 𝒜), which stays open (Assessment, §6.2) | PROVED |
| §6.3 | unconditional signed errors: Assessment (unchanged from PL) | Assessment |
| §7 | LP/QP/exact-law sanity checks of Lemma 1.1, Lemma 2.2/Thm 2.4, Lemma 4.1/Thm 4.2, Thm 4.3's steps | EVIDENCE |

**Bottom line.** Of the four escape groups of O27: escape 2 (Gallagher
over mixtures) is closed for prime-power kernels, unconditionally and far
below the 3/4 scale (Thm 4.3); composite kernels are capped by Thm 4.2 only
where `Nh/(W_K−h)` is controlled; escape 3 (twisted, multiplicative
× additive, Gauss-sum, hybrid fibrewise forms) is closed (Thm 2.4); the
prime large sieve (escape 4, third item) is closed (Thm 3.1); the
relaxation "`ν ≥ 1` only on the primes of `𝒜 ∩ [1,N]`" is vacuous as a
sieve limit (Prop 6.1), while the relaxation "`ν ≥ 0` only at primes
`≤ N`" (with `ν ≥ 1` on all primes of 𝒜) stays open (Assessment). Open: (E1)/(H_LS) — now reduced to frequencies with
many-prime denominators and to a sup-decay statement (H_LS∞) — and
unconditional signed error accounting (Assessment only). The tool behind
all of it is Lemma 1.1: K2's cap, read through LP duality, is one
measure that tests every nonnegative low-level function at once, so
Cauchy–Schwarz can strip twists and fibres away.

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
`E_π f = Σ_{x∈𝒜} μ(x)f(x)/m* ≤ Σ_x μ(x)f(x)/m* = E_U f/m* ≤ e^{S(λ)}E_U f`.
(Since `1 ∈ V_𝒟`, the first identity with `ν ≡ 1` gives `Σ_x μ(x) = 1`: μ is
a probability, `μ(𝒜) = m* ≤ 1`, and π is μ conditioned on 𝒜; review m6.) ∎

*Remarks.* (i) Lemma 1.1 is **equivalent** to K2 Thm 5.1 on `V_𝒟`
(conversely, (1.1) with `f = ν` gives `1 ≤ E_πν ≤ e^S E_Uν`). Its use
is that one measure serves every nonnegative test function at once,
including test functions that are not majorants. (ii) Only the
existence of π is used below, not its construction; the explicit KARY
law (EK Thm 4.1: the sequential law `Q'` reweighted by `e^{−ΣΦ}` and
restricted to 𝒜) is one admissible choice (discussed in §5). (iii) Fibres:
for `Q₀ | M'` and a class `c mod Q₀` with `π(c) > 0`, the conditional
law of `m = (n − c)/Q₀` given `n ≡ c (Q₀)` is supported on
`𝒜_c = {m : c + Q₀m ∈ 𝒜}`, and for every `f ≥ 0` in the span of classes
in m whose moduli d have `Q₀d` ∈ 𝒟-span (level `λ(Q₀) + λ(d) ≤ λ`),

    E_{π_c} f ≤ e^{S(λ)} E_U f / (Q₀ π(c)),                              (1.2)

since `n ↦ f((n−c)/Q₀)1[n ≡ c (Q₀)]` is `≥ 0`, lies in `V_𝒟` (a class
`m ≡ b (d)` becomes `n ≡ c + Q₀b (Q₀d)`), and has U-mean `E_U f/Q₀`.
If moreover `Q₀ ∈ 𝒟`, then `π(c) ≤ e^{S(λ)}/Q₀` by (1.1) with `f = 1[n ≡ c (Q₀)]` (review: this needs `1[n≡c (Q₀)] ∈ V_𝒟`; Theorem 2.4 puts `Q₀` into 𝒟).

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
all have level `≤ λ`. Take `M'` a common multiple of `M₀`, of 𝒟 and of
`Q₀·`(every row period and every twist period), so that every
`E_{π_c}[ψ_cφ̄_j]` is defined; Lemma 1.1 holds for every such `M'` with 𝒟
unchanged, which is why the twists' periods never enter the level
(review m1). Take π from Lemma 1.1 and the fibre laws `π_c`
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
under bounded B), and `C_A(log N)^{3/4}` for every mixture with KARY3
Thm 4.1. In particular twisted large sieves (any periodic twist
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

## 3. The large sieve applied to the primes (PL §6 item 5)

Let `A ⊂ {p ≤ N prime : p ∈ 𝒜, p ∤ M'} ∩ I`. (Primes dividing `M'` are
at most `ω(M')` and are added by the method separately; that only
enlarges its bound, as in PL Cor 4.2 / review D3.) Now `π_A` lives on
`𝒜 ∩ (ℤ/M')^×`. Call a bound *CRT-admissible for primes* if, in the
definitions of §2, "every probability on 𝒜" is replaced by "every
probability on `𝒜 ∩ (ℤ/M')^×`" (a lower bound may use primality through
the residues: all moduli at once, Dirichlet/Siegel–Walfisz-type
reduced-class information included).

**Theorem 3.1 (prime large sieve cap; PROVED, conditional on PL Thm 3.1,
i.e. with its Case-A proviso).** In the setting of Theorem 2.4 with
admissibility for primes, every fibre of type (i) or (iii), and fibre
classes `c ∈ (ℤ/Q₀)^×`,

    B ≥ (N/2) e^{−S(λ)} φ(M')/M',      λ = max(λ₀, λ(Q₀) + 2λ_Φ).

If all primes of `M'` — the family's, the rows', the twists' and `Q₀`'s — are `≤ N^A`, and `λ ≤ 3A log N`, then
`B ≥ π(N)·exp(−C_A(log N)^{3/4}(log log N)^{3/4})`: relative to the
trivial bound `π(N)` the saving is `≤ C_A(log N)^{3/4}(log log N)^{3/4}`
(`≤ C_A(log N)^{3/4}` with KARY3 §4.3, pointer-level).

*Proof.* As Theorem 2.4, with π* of Lemma 1.2. For `f ≥ 0` on all of
`ℤ/M'`, `E*f = (M'/φ(M'))E_U[f·1_{units}] ≤ (M'/φ(M'))E_U f`. Hence for
the lifted fibre function `F(n) = |H((n−c)/Q₀)|²1[n ≡ c (Q₀)] ≥ 0`,
`E_{π*}F ≤ e^S(M'/φ(M'))E_U|H|²/Q₀`, and the type-(i) estimate becomes
`B_c ≥ N_cQ₀π*(c)e^{−S}φ(M')/M'`. For type (iii),
`π*(c) ≤ e^S E*1[n≡c] = e^S/φ(Q₀) ≤ e^S(M'/φ(M'))/Q₀`. Sum over c. For
the reading, Mertens gives `M'/φ(M') ≤ Π_{p≤N^A}(1−1/p)^{−1} ≤ 2A log N`
for N large, and `N/(4A log N) ≥ π(N)/(5A)`. ∎

So Montgomery's large sieve for the primes of the sifted set (any
periodic rows and twists `|ψ| ≥ 1` whose periods have all prime factors
`≤ N^A`, fibrewise; unlike Theorem 2.4, the twist's period enters here
through `M'/φ(M')`)
gains nothing beyond the integer cap: the factor `φ(M')/M'` is exactly
the prime density already in `π(N)`. *Sketch only (not claimed):* type-
(ii) fibres carrying prime majorants with `Err ≥ 0` (PL Cor 4.2) can be
mixed in the same way under PL's hypothesis (H1); this needs PL Lemma
1.3's fibre bookkeeping under E*, which is not written out here.

## 4. Gallagher's larger sieve over mixtures (escape 2, LS (E2a), (E2b))

Setting and notation as in LS §6: moduli 𝒮 with weights `w(q) ≥ 0`,
`K(m) = Σ_q w(q)1[q | m]`, `W_K = K(0)`, `h ≥ max_{0<|m|<N}K(m)`,
`D(π) = Σ_q w(q) coll_q(π)`, `D_u = Σ_q w(q)/q`, a CRT-admissible kernel
bound is `B = (W_K−h)/(L−h)` with `h < L ≤ D(π)` for all `π ∈ P(𝒜)`, and
`X(π) = Σ_q (w(q)/q)χ²_q(π)`, so `D = D_u + X` (LS Thm 6.2). (`W_K` is
written for LS's W to avoid a clash with K2's W.)

### 4.1 Any kernel: the larger sieve is a Bessel inequality minus the zero frequency

Expanding `1[q | m] = q^{−1}Σ_{a mod q}e(am/q)`,

    K(m) = Σ_θ w̃_θ e(mθ),   w̃_θ = Σ_{q∈𝒮, den θ | q} w(q)/q ≥ 0,   D(π) = Σ_θ w̃_θ |π̂(θ)|²,

with `w̃_0 = D_u`.

**Lemma 4.1 (PROVED).** `w̃_θ ≤ h + (W_K − h)/N` for every θ.

*Proof.* With `a_n = e(−nθ)` on I, `K ≥ 0` and the pair count of LS
Lemma 6.1: `w̃_θN² ≤ Σ_φ w̃_φ|Σ_{n∈I}e(n(φ−θ))|² = Σ_{n,n'∈I}
e(−(n−n')θ)K(n−n') ≤ Σ_{n,n'∈I}K(n−n') ≤ NW_K + (N²−N)h`. ∎

**Theorem 4.2 (kernel cap by level; PROVED, conditional on K2 Thm 5.1).**
Let every `q ∈ 𝒮` (with `w(q) > 0`) have level `≤ λ_𝒮`, and
`λ = max(λ₀, 2λ_𝒮)`. Every CRT-admissible kernel bound satisfies

    B ≥ (N/2) e^{−S(λ)} / (1 + N h/(W_K − h)).

*Proof.* Take π from Lemma 1.1 with 𝒟 = `{1} ∪ {lcm(q,q') : q,q' ∈ 𝒮}`
(1 is needed by Lemma 1.1; review m2). For
`‖c‖ ≤ 1` put `H_c = Σ_{θ≠0} (w̃_θ)^{1/2} c_θ e(nθ)`; `|H_c|² ≥ 0` lies in
`V_𝒟`. Then
`D(π) − D_u = Σ_{θ≠0}w̃_θ|π̂(θ)|² = sup_c |E_π H_c|² ≤ sup_c E_π|H_c|²
≤ e^S sup_c Σ_{θ≠0} w̃_θ|c_θ|² ≤ e^S(h + (W_K−h)/N)` (Lemma 4.1). With
`D_u − h ≤ (W_K−h)/N` (LS Lemma 6.1),
`L − h ≤ D(π) − h ≤ 2e^S(h + (W_K−h)/N)`, and
`B = (W_K−h)/(L−h)` gives the claim. ∎

So the larger sieve with composite moduli of polynomial level is capped
like the large sieve **up to the factor `1 + Nh/(W_K − h)`, which is not
controlled in general** (review: adding weight T at modulus 1 leaves the
kernel bound unchanged but inflates h by T; more generally kernels with
`W_K − h ≪ Nh` are not covered). Composite kernels are therefore capped
only when `log(1 + Nh/(W_K−h)) ≪ (log N)^{3/4}` (after deleting the
modulus 1, which cancels). For
Gallagher's kernel (`h = log N`, `W_K = ψ(Q)`) that factor is
`≤ 1 + 4 log N` once `Q ≥ N`; the next theorem does much better.

### 4.2 Prime-power kernels: an O(log log N) cap, unconditionally

**Theorem 4.3 (H_Gal holds; PROVED, unconditional — no ElT Prop 1.4 and
nothing conditional; it uses Shiu's theorem and Mertens through K2 Lemmas
3.1, 4.2).** There are
absolute constants `C, N₀` such that for every finite mixture 𝔊 of the
four types (arbitrary moduli, Case A included) and every `Q ≥ 2` there is
`π ∈ P(𝒜(𝔊))` with

    Σ_{q = ℓ^v ≤ Q} (Λ(q)/q) χ²_q(π) ≤ 24 log log(3Q) + C.               (4.1)

Consequently, for `N ≥ N₀`, Gallagher's larger sieve (`w = Λ` on the
prime powers `≤ Q`, `h = log N`, any Q), in its CRT-optimal form `D*`
and a fortiori in the Cauchy–Schwarz form `Σ Λ(q)/ν(q)`, saves at most
`log(N/B) ≤ 26 log log N + C`.

*Proof.* *The law.* Take `W = max(W₀, (log 3Q)^8)` and let σ be the
plain sequential law of EK §1 for 𝔊: base uniform on K2's `R_W^□`
(K2 Lemma 2.3, any `W ≥ 3`), then every prime `ℓ > W` of `M₀` as a
singleton in increasing order, caps `δ_ℓ = ℓ^{−1/2}` (light: `y_ℓ`
uniform on `Ω_ℓ ∖ F_ℓ`; heavy: uniform on `Ω_ℓ = ℤ/ℓ^{E_ℓ}`), all other
CRT digits uniform and independent. By EK Lemma 2.1(2) and K2 (R2), σ
satisfies the chain-rule inflation `σ(n ≡ b (m)) ≤ Γ(m)/m` used in K2
Lemmas 4.1–4.3, so K2 Lemma 4.3 holds for σ:
`E_σ p_ℓ² ≤ C(log W)^c ℓ^{−7/4}(log ℓ)^c`. Every class is decided at its
top prime (W-smooth classes by the base, K2 Lemma 2.3(1)), so by EK
Lemma 2.1(1) and Markov,
`𝔏 := σ(𝒜^c) ≤ Σ_{ℓ>W} ℓ^{1/2}E p_ℓ² ≤ C'(log W)^{c'}W^{−1/4} ≤ 1/4`.
The load-bearing input when `W = (log 3Q)^8` grows is the W-uniformity
`C(W) ≤ C(log W)^c` of K2 Lemma 4.3 ("W-dependence", via K2 Lemma 3.1's
Euler factors); c is huge but absolute. `𝔏 ≤ 1/4` (used for
`χ² ≤ (4/3)p` and `(1−𝔏)^{−2} ≤ 1 + 4𝔏`) needs a `W₀` larger than K2's
(which only gives `𝔏 ≤ 1/2`); `W₀` is enlarged accordingly (review m3).
Put `π = σ(· | 𝒜)`.

*Conditioning.* For every q and residue b, `π(b mod q) ≤ σ(b mod q)/(1−𝔏)`,
so `1 + χ²_q(π) ≤ (1 + χ²_q(σ))(1−𝔏)^{−2}` and
`χ²_q(π) ≤ χ²_q(σ) + 4𝔏(1 + χ²_q(σ))`.

*Marginals of σ.* χ²(·‖uniform) is convex and contracts under
projection `ℤ/ℓ^{E} → ℤ/ℓ^v`; above `ℓ^{E_ℓ}` the law is a uniform lift.
* `ℓ > W`, `ℓ | M₀`: given the past, `y_ℓ` is uniform on `Ω∖F`
  (χ² `= p/(1−p) ≤ (4/3)p` as `p ≤ 1/4`) or uniform (χ² = 0). Hence
  `χ²_{ℓ^v}(σ) ≤ (4/3)E p_ℓ ≤ (4/3)(E p_ℓ²)^{1/2} ≤ C(log W)^cℓ^{−7/8}(log ℓ)^c`.
* `ℓ ∤ M₀`: χ² = 0.
* `p ≤ W`: the base is uniform on the unit squares mod `p^{e_p}`;
  reduction is a group homomorphism of the unit-square group onto the
  unit squares mod `p^v`, so the marginal is uniform there:
  `χ² = (p+1)/(p−1) ≤ 2` (p odd), `≤ 7` (p = 2).

*Sum.* The W-smooth prime powers give
`≤ Σ_{p≤W}(log p/(p−1))(2+12𝔏) + log 2·Σ_v 2^{−v}(7+32𝔏) = 2 log W + 12𝔏 log W + O(1)`
(Mertens), which is `≤ 3 log W + C` because `𝔏 log W = o(1)` (not merely
`𝔏 ≤ 1/4`, which would give `5 log W`; review m3(d)). The rough ones give
`≤ Σ_{ℓ>W}(2log ℓ/ℓ)·2C(log W)^cℓ^{−7/8}(log ℓ)^c + 4𝔏Σ_{q≤Q}Λ(q)/q
≤ C + 4C'(log W)^{c'}W^{−1/4}(log Q + 2) ≤ C`, by the choice of W (for
`Q ≥ Q₁(c')`; smaller Q are absorbed into C). Since
`3 log W ≤ 24 log log(3Q) + C`, (4.1) follows.

*Consequence.* LS Thm 6.2's proof gives `log(N/B) ≤ log(1 + NX/(ψ(Q) −
log N))` whenever a bound exists, i.e. `D* > log N`. As
`D* ≤ D(π) ≤ log Q + c₀ + X`, a bound needs `Q ≥ N e^{−c₀−X}`, hence
`Q ≥ N(log N)^{−25}` for `N ≥ N₀`; then `ψ(Q) − log N ≥ Q/4`. If
`Q ≤ N²`, `NX/(ψ(Q)−log N) ≤ 4(log N)^{25}(25 log log N)`, and the
saving is `≤ 26 log log N + C`. If `Q > N²`, `4NX/Q ≤ 1` and the saving
is `≤ log 2`. The Cauchy–Schwarz form has `L = Σ Λ/ν(q) ≤ D*`, so its
bound is larger. ∎

*Remarks.* (a) Theorem 4.3 uses only K2 Lemmas 2.3, 3.1, 4.1–4.3 and EK
Lemma 2.1 (published inputs: Shiu, Mertens; no ElT Prop 1.4); it does **not** need K2 Thm 5.1.
It is far below the 3/4 scale: on forced-class avoiders, which occupy
almost every residue class modulo every prime power, Gallagher's sieve is
essentially powerless, as on the prime slices of LS Cor 6.3. (b) Any
other weights `w ≥ 0` on prime powers: the same π (with `W = W₀`) has
`χ²_q(π) ≤ 7(1+4𝔏) + 4𝔏 ≤ 15` for every prime power q, so
`X(π) ≤ 15D_u ≤ 15(h + (W_K−h)/N)` and the saving is
`≤ log(16 + 15Nh/(W_K − h))`. (c) Composite kernels are covered by Theorem 4.2
when their moduli have polynomial level **and** `Nh/(W_K−h)` is at most
`exp(O((log N)^{3/4}))`; otherwise they remain open, and kernels whose
moduli have super-polynomial level belong with (E1) (§5).

## 5. Escape (E1): super-polynomial levels — sharpened, not closed

Throughout this section the system is LS's: rational frequencies Θ,
weights `w_θ ≤ 1/N` (LS Fact 1.1), `Σ_θ w_θ ≤ 1` (LS Fact 4.0).

**Proposition 5.1 (what (E1) really requires; PROVED, conditional on K2
Thm 5.1).** Let all primes of 𝔊 be `≤ N^A`. If every frequency θ used
(after LS Rem 3.3's projection, `den θ | M₀`) has at most r distinct
prime factors `> W` in its denominator, the saving is
`≤ log 2 + S(max(λ₀, 2rA log N + λ(Q₀)))`. Hence a saving `≥ (log N)^{3/4+ε}`
needs frequencies with `≥ (log N)^{4ε/3 − o(1)}` distinct family primes
`> W` in the denominator.

*Proof.* Such θ have level `≤ rA log N`; LS Thm 3.1 (or Theorem 2.4).
Solve `S(2rA log N) ≥ (log N)^{3/4+ε}` for r. ∎

So (E1) is not about large denominators but about denominators with
**many** prime factors (each `≤ N^A`). Such frequencies probe correlations
of the residues of 𝒜 at many primes simultaneously.

**Proposition 5.2 (diagonal reduction; PROVED).** Fix `λ' ≥ λ₀/2`.
Suppose there is `π ∈ P(𝒜)` with
* (a) `E_π f ≤ e^{S₁} E_U f` for all `f ≥ 0` of level `≤ 2λ'`, and
* (b) `|π̂(θ)|² ≤ e^{S₂}/N` for every θ of level `> λ'`.

Then every CRT-admissible large-sieve bound (any rational frequencies,
any weights) is `≥ N/(e^{S₁} + e^{S₂})`.

*Proof.* `F_w(π) = Σ_{level θ ≤ λ'} w_θ|π̂(θ)|² + Σ_{level θ > λ'} w_θ|π̂(θ)|²`.
The first sum is `sup_{‖c‖≤1}|E_π Σ_{low} √w_θ c_θ e(nθ)|² ≤ e^{S₁}·max w ≤
e^{S₁}/N` (as in Theorem 2.4); the second is `≤ max_{high}|π̂|²·Σw ≤
e^{S₂}/N`. Admissibility gives `B ≥ 1/F_w(π)`. ∎

There are no cross terms: `F_w` is diagonal in θ. This is a sufficient
criterion **different** from LS's (H_LS) (which asked for `ℓ^{2+2β}`
smallness of π̂ over all frequencies). Neither implies the other: an
`ℓ^{2+2β}` bound tolerates isolated large high-level coefficients (e.g.
density `1 + cos(2πn/d)`), which (b) forbids (review). Its advantage is
that the low levels are already handled by K2 (Lemma 1.1 supplies (a)),
so only high-level coefficients need control. Since λ'
may be any fixed multiple of `log N` (cost `S(2λ') ≍ (log N)^{3/4}·polylog`),
it suffices that (a) at level `2λ' = (2/η)log N` and

    (H_LS∞)   |π̂(θ)| ≤ e^{S(λ')} exp(−η·level(θ))   for level(θ) > λ'

hold for one π and some fixed `η > 0` (any exponential rate in the level).

*Status.* (H_LS∞) is **CONJECTURE**. What is missing is a measure that
satisfies (a) **and** has Fourier decay at many primes simultaneously:
* Lemma 1.1's π is an abstract LP dual (no Fourier information);
* EK's explicit law (sequential `Q'` reweighted by `e^{−ΣΦ}1_𝒜`)
  satisfies (a), but the reweighting depends on the whole path;
* the unweighted sequential law `Q'` decays at the **top** prime of the
  denominator only, `|Q̂'(θ)| ≤ E g_{ℓ_top}` (LS §7). Product decay over
  several primes fails for the naive Schur-type induction: each step
  sums `|·|` over all cofactors of the classes decided at the current
  prime, and with first moments `≍ (log ℓ)²/ℓ` per prime the losses
  compound (`Σ_q Π_{p|q}(log p)²/q` diverges); real cancellation in the
  phases would have to be used;
* a product sub-law (forbid every class at its top prime regardless of
  the lower residues) has exact product decay but loses density
  `Π_ℓ(1 − f̃_ℓ/ℓ)` with `f̃_ℓ` the number of all classes with top ℓ,
  `≍ ℓ^{B+o(1)}`; this works only for slice-type families (LS Thm 4.1).

*Heuristic (Assessment).* For the uniform law on 𝒜 a polymer (cluster)
expansion over connected covers of the primes of `den θ` by family moduli
predicts `|π̂(θ)| ≲ Π_{ℓ | den θ}(c(log ℓ)^c/ℓ)` times a combinatorial
factor `≤ ω^{ω/2}`; distinct primes force `ω ≲ ℓ_typ/log ℓ_typ`, so the
product still decays like `exp(−(1/2 − o(1))·level)`. So (H_LS∞) is
expected with `η = 1/2 − o(1)`, and no escape is expected. No method in
the literature uses such frequencies.

## 6. The remaining prime-law opens (PL §6 items 2, 3)

**6.1 The large sieve for primes** is closed by Theorem 3.1.

**6.2 Finite-range positivity.** PL §6 item 2 lists majorants with
`ν(p) ≥ 0` only for primes `p ≤ N` (and/or `ν ≥ 1` only at the primes of
`𝒜 ∩ [1,N]`), the gap living at period `L > N^c`.

**Proposition 6.1 (the finite-range LP is the exact count; PROVED).**
For every family 𝔊 and every N there is ν with
* `ν ≥ 0` on all of ℤ, `ν ≥ 1` at every prime `p ≤ N` with `p ∈ 𝒜`;
* every modulus a single prime `q ∈ (N, 2N]` (level `≤ log 2N`), and
  coefficient sum `T = #(𝒜 ∩ primes ≤ N) ≤ N`;
* `Σ_{p≤N} ν(p) = #(𝒜 ∩ primes ≤ N)` exactly.

*Proof.* `ν = Σ_{p ≤ N, p ∈ 𝒜} 1[n ≡ p (mod q)]`; for primes `p' ≤ N`,
`p' ≡ p (mod q)` with `p, p' ≤ N < q` forces `p' = p`. ∎

*Scope (review m4).* Prop 6.1 settles only PL §6 item 2's second bullet.
The first bullet — `ν(p) ≥ 0` only for `p ≤ N` but `ν ≥ 1` on **all**
primes of 𝒜 — is not covered: there the construction fails, since by
Dirichlet every reduced class mod q contains primes of 𝒜 above N. It stays
open (the "mixed variant" below, Assessment).

So with "`ν ≥ 1` only at the primes of `𝒜 ∩ [1,N]`" the relaxed LP has
value equal to the truth, already at level `≍ log N`, polynomial budget
and nonnegative ν: **no cap of any kind can hold for that relaxation.**
What a real method lacks is not a better majorant but the knowledge of
*which* primes `≤ N` lie in 𝒜 — that is, the ES verification itself
(non-CRT input, LS (E3)). Methods that certify `ν ≥ 1` through the
family alone are in PL Def 1.1 and capped by PL Cor 4.2. The mixed variant
(`ν ≥ 1` on every unit of 𝒜, `ν ≥ 0` only at primes `≤ N`) lets ν be
negative only on reduced classes containing no prime `≤ N`; at period
`L > N` these are almost all classes, and certifying the sign condition
again needs the location of the primes `≤ N` (Assessment; not a theorem).

**6.3 Unconditional signed errors.** Unchanged from PL §4.3/§6 item 3
(Assessment): unconditional error terms for `π(N; d, b)` with
`d ≥ (log N)^{O(1)}` are at best `N(log N)^{−A}` on average (BV), far
above the main terms `π(N)e^{−(log N)^{3/4}}` at stake; for
`d ≤ (log N)^{O(1)}` the uniform unconditional error is Siegel–Walfisz's
`N exp(−c(log N)^{1/2})` (ineffective); the Vinogradov–Korobov exponent
`3/5 − o(1)` applies only for fixed small d / away from a possible
exceptional zero (review m5). Both exceed those main terms, since
`1/2 < 3/5 < 3/4`. So no unconditional signed accounting can even resolve
the main term at the 3/4 scale. Under GRH, PL Prop 4.3 caps it.

## 7. Numerics (EVIDENCE / sanity checks only)

`scripts/largesieve2_checks.py` (~7 s, 2 threads, < 1 GB), output
`data/largesieve2/checks.txt`. Toy family: all ℛ(M)-, (a,D)-, Case-A
classes with modulus dividing `L = 24·5·7·11` plus the selectors
`0 mod p`, `p | L` (W = 3); "arity" k = number of primes 5, 7, 11 per
modulus of `V_𝒟` (stand-in for the level).
1. Lemma 1.1: the LP's dual multipliers satisfy stationarity to
   `1.4·10⁻¹⁵`; for the extracted π, a second LP gives
   `max{E_πf : f ∈ V_𝒟, f ≥ 0, E_Uf = 1} = 1/m*` exactly (24 at k = 0,
   140 at k = 2), as the proof predicts.
2. Lemma 2.2 and the type-(i) estimate of Theorem 2.4: 504 weighted Farey
   rows (denominators of arity ≤ 1), `N = 60`; `N·E_U|H|²/(Δ‖c‖²) ≤ 0.094`
   and `[R̃(π)/E_π|ψ|²]/[Δ/(Nm*)] ≤ 0.029` over random c and random
   twists `|ψ| ∈ [1,3]`.
3. Lemma 4.1 holds exactly for 6 random kernels (`N = 40`); the QP optimum
   `D*` gives kernel bounds `B ∈ [3.0, 12.7]`, all above Theorem 4.2's
   lower bound (which is far from sharp at this size).
4. Theorem 4.3's proof steps on the exact plain sequential law σ: base
   marginals `χ² = 7` (q = 8) and 2 (q = 3); `χ²_ℓ(σ) ≤ E[p/(1−p); light]`
   at ℓ = 5, 7, 11; and `1 + χ²_q(π) ≤ (1+χ²_q(σ))(1−𝔏)^{−2}` for all q,
   on the full toy family (every rough prime heavy, leak 0.91: degenerate)
   and on three random thinnings (leak 0, 0, 0.32).

## Replay

```
OMP_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2 PYTHONPATH=scripts uv run --with cvxpy --with scipy \
  --with numpy --with sympy python scripts/largesieve2_checks.py > data/largesieve2/checks.txt   # ~7 s
```

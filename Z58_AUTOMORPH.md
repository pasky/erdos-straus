# Z58_AUTOMORPH — modular / mock-modular generating functions for (MS): T1 at p², p⁴, … kills every effective Hecke-finite support proxy; where the escape lies

Status: z58 lane AUTOMORPH (brief `z52bbriefs/z58_lanes.md` §AUTOMORPH, common rules `z52bbriefs/z53_depth.md`).
Internal; internally reviewed only. **ES is OPEN; nothing here proves or disproves ES, (★), or (MS).**
Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment.
Scripts `scripts/z58_automorph_*`, data `data/z58/automorph/`.
Read: `paper/es-automorphic-barrier-note.tex` (§§1, 4.1, 6, 7), `METAPLECTIC_ES.md` (Thm K, Cor K1, Prop S, §§3–5),
`SIGN_IDENTITY.md` (Thm 2.2, Prop 2.3, Prop 2.4), `STRONG_APPROX_ES.md` Thm 9.1, `GROWING_IDENTITIES` (Eichler–Selberg
item in DISCOVERIES #10), `BRAINSTORM/z39_square_discriminant_shadow.md`, `Z57_SYNTH.md` §§0–2, the falsifier data.

History: checkpoint 1 = §§0–2; final = §§3–7. A hostile deep review (§7) found 2 FATAL + 10 MAJOR + 2 MINOR issues.
All are repaired in this version; repaired places are marked "(R1-n)".

---

## 0. MANDATORY FALSIFIER TABLE

The *mechanism* examined: "write Σ R(n)qⁿ, or a proxy a(n) with a(n) ≠ 0 ⟹ R(n) ≥ 1, as an automorphic object;
split it into Eisenstein (main term) + cusp/shadow part; bound the cusp part pointwise (Deligne/Duke) below the main
term at a single prime."

| screen | behaviour of the mechanism |
|---|---|
| **F1 odd squares** | A support proxy must vanish at 1, p², p⁴, … (all odd squares). **Theorem A (PROVED):** for every *Hecke-finite* proxy in the arithmetic class 𝓗 (§2: eigenvalue systems of holomorphic integral-weight forms, any level/character, Eisenstein or cuspidal; their n^j-twists = quasi-modular forms; real-parameter divisor sums Σ d^a(n/d)^b and their parameter derivatives), vanishing *at the powers of p alone* forces a(p) = 0, unless the Satake multiset at p contains a pair γ, −γ. On a positive-density set of 𝔐-primes (all ≡ 1 mod 840) no such pair exists, so every such proxy vanishes there. Typical collisions come from twists f, f⊗ψ with ψ(p) = −1, i.e. congruence data. CM forms and weight-one forms give further collisions (R1-4). Squares and primes lie in different Shimura square classes in half-integral weight, so F1 does not bind the same way there; see §4 (escape E1). |
| **F2 C-even sub-line** | Theorem A applies verbatim to R₈ (R₈ ≤ R, so R₈(m²) = 0): the no-go is line-blind and proves nothing false. For the escape E1 any proxy has to tell the C-odd line from the C-even line. No candidate examined does (§4). |
| **F3 composites** | Theorem A uses only T1 at the powers of p, not the 285 composite zeros. The composite zeros constrain the half-integral-weight escape. Under an explicit Eisenstein lower-bound hypothesis they force the weight-3/2 Eisenstein part to vanish on local classes that carry infinitely many zeros (§4, Prop C, CONDITIONAL). |
| **F4 known zeros** | The no-go proves no positivity, so nothing to check. Any proxy must vanish at the 14 (★)-zeros (three of them ≡ 1 mod 840: 712 321, 1 726 201, 8 813 281) and, if it is meant for 𝔊*, at the 38 𝔊*-zeros. |

Verdict: the mechanism is **dead for every Hecke-finite object in 𝓗**, in the sense that no support proxy in 𝓗 is
both valid and effective (Thm A, Cor A1). Valid but ineffective proxies exist, e.g. τ(n)·1[n ≡ 5 mod 12] (R1-5). The
escapes it leaves are
* (E1) half-integral weight, where a proper rational p-power series exists but has unavoidable ± poles (XR-1);
* (E2) constructions whose resulting coefficients lie outside 𝓗, e.g. level sums Σ_C over the variable 4Cn + 1.
  A Poincaré, Rademacher or Fourier–Jacobi *presentation* does not by itself put an object outside 𝓗 (XR-2);
* (E3) higher-depth objects without GL₂ Hecke theory.

---

## 1. Precise statements attacked

Notation: R(n) = #{(u,B,C) ∈ ℕ³ : 4uBC − u − B = n}, so Σ_n R(n)qⁿ = Σ_{C≥1} Σ_{u,B≥1} q^{4CuB−u−B}. Also
R(n) = Σ_C D⁻_{4C}(4Cn + 1) with D⁻_t(N) = #{d | N : d ≡ −1 (mod t)} (`METAPLECTIC_ES` Thm K, with u, B ≥ 1).

**Q1 (exact identity).** Is n ↦ R(n) (on n ≡ 1 mod 4, or on primes) the coefficient sequence of a modular,
quasi-modular, mock-modular or higher-depth object in a finite-dimensional space?

**Q2 (positive proxy, support form).** Is there an automorphic a(n) with a(n) ≠ 0 ⟹ R(n) ≥ 1 for all n ≡ 1 (4) (*valid*)
and a(p) ≠ 0 for all large p ∈ 𝔐 (*effective*)? Here "large" may mean p > 10¹⁰ or p > 10¹⁷.

**Q2′ (minorant / sign form).** The same with a(n) > 0 ⟹ R(n) ≥ 1, which at odd squares gives a(m²) ≤ 0.

**Q3 (decomposition template).** If a = E + c (Eisenstein + cusp), can |c(p)| < E(p) be shown at a single prime with
explicit constants?

**Prior closures (not redone).**
* SIGN_IDENTITY Thm 2.2: no finite sum of holomorphic forms equals N₋, by size, since the average is X log²X.
* SIGN_IDENTITY Prop 2.3 and STRONG_APPROX Thm 9.1: T1 kills finite *Eisenstein* (divisor-rank) combinations on
  p ≡ 1 (mod L).
* METAPLECTIC Thm K: each level is a Kronecker theta quotient plus weight-0 data, with no cusp forms.
* METAPLECTIC Prop S: holomorphic weight ½ is Serre–Stark.
* Paper Thm 4.1 ("ternary", `thm:ternary`). For positive-definite Q and fixed-complexity embeddings, a representation
  *theorem* producing sets of generic size p^{(k−2)/2−ε₀} proves ES only on the Mordell-type union U. The paper notes
  that an embedding supported on a *thin* set can still work outside U (R1-11).
* DISCOVERIES item (J)10 (GROWING_IDENTITIES Prop 2.1/2.2): ES is the sign-odd part of the split-hyperbolic
  Eichler–Selberg term.

**What is new here.**
* Theorem A extends the T1 kill (support form) from Eisenstein combinations to the class 𝓗 of GL₂ Hecke-finite
  arithmetic functions. That class includes cusp forms (where Deligne bounds live), quasi-modular forms, and
  real-parameter divisor sums with their derivatives (log-power sizes, which Thm 2.2's size argument does not reach).
  The identification of 𝓗 with a class of mock-modular objects is *not* claimed: full non-holomorphic coefficients
  carry Whittaker factors, and a prescribed shadow allows further additions (R1-9).
* It needs only T1 at the powers of the single prime p.
* It shows that such an object can be non-zero at p only through a ± collision of Satake parameters at p.

---

## 2. Lemma S and Theorem A

**Lemma S (sign lemma; PROVED, elementary).** Let K be a field of characteristic 0 and let a: {p^m : m ≥ 0} → K.
Suppose A(T) := Σ_{m≥0} a(p^m) T^m is a rational function that is *proper* (it tends to 0 as T → ∞) and whose poles
all lie in {1/γ : γ ∈ Γ} for a finite set Γ ⊂ K^×. Suppose further that Γ ∩ (−Γ) = ∅. If a(p^{2j}) = 0 for all
j ≥ 0, then a(p^m) = 0 for all m ≥ 0. In particular a(p) = 0.

*Proof.* The even part ½(A(T) + A(−T)) has Taylor coefficients a(p^{2j}) = 0, so A(T) = −A(−T) as rational
functions. The poles of A(T) lie in P := {1/γ}, and those of −A(−T) lie in −P. By hypothesis P ∩ (−P) = ∅, so the
two functions, being equal, have no poles at all. Hence A is a polynomial. It is also proper, so A = 0. ∎

**The class 𝓗_M (definition; XR-4).** Fix a level M. 𝓗_M is the set of functions a on {n : (n, M) = 1} of the form
a(n) = Σ_{i=1}^r c_i λ_i(n), with r finite, c_i ∈ ℂ, finitely many derivative orders, and each λ_i one of the
following. 𝓗 := ∪_M 𝓗_M is a union of fixed-level arithmetic classes. We call its elements "Hecke-finite" for short,
but 𝓗 is *not* claimed to contain every Hecke-finite automorphic object.
* (i) The normalised Hecke eigenvalue system λ_f(n) of a holomorphic newform or Eisenstein eigenform f of integral
  weight k ≥ 1, level | M, any nebentypus.
* (ii) n^j λ_f(n), j ∈ ℤ_{≥0}. This covers D^j f and the quasi-modular forms, since QM = ⊕ D^j M ⊕ ℂ D^j E₂ by
  Kaneko–Zagier, and E₂ has λ = σ₁.
* (iii) ∂_a^r ∂_b^s Σ_{d|n} ψ₁(d)ψ₂(n/d) d^a (n/d)^b evaluated at a real point (a, b) = (a₀, b₀), with r, s ≥ 0
  and ψ₁, ψ₂ characters mod M. This is equivalent to the earlier one-parameter description
  d^{s+u}(n/d)^{−s+v}. These are the
  arithmetic parts of the coefficients (times powers of n) of holomorphic or non-holomorphic Eisenstein series and of
  their s-derivatives. Examples: σ_a(n), n^bτ(n), τ(n), Σ_{d|n} χ(d) log(n/d²), Σ_{d|n} log d·log(n/d). The modular
  packaging is standard; the theorem below concerns only the arithmetic functions.

Every element of M_k(Γ₁(N)) restricted to (n, N) = 1 lies in 𝓗_N. Reason: for (n, N) = 1 the operators T_n act
semisimply, and a_f(n) = a_{T_n f}(1) = λ(n) a_f(1) on each eigencomponent. Old forms f(dz), d > 1, contribute 0 at
(n, d) = 1. Finite sums over different weights are allowed.

**Satake data.** For λ_i of type (i), at p ∤ M:
Σ_m λ_i(p^m) T^m = 1/((1 − α_i T)(1 − β_i T)), with α_i + β_i = λ_i(p) and α_iβ_i = ψ_i(p)p^{k_i−1}.
Type (ii) replaces (α, β) by (p^jα, p^jβ). Type (iii) gives ∂^e of 1/((1 − x(s)T)(1 − y(s)T)) with
x = ψ₁(p)p^{s+u}, y = ψ₂(p)p^{−s+v}; this is proper, with poles only at 1/x(s₀), 1/y(s₀). So for every a ∈ 𝓗_M and
p ∤ M, A_p(T) satisfies the rationality and properness hypotheses of Lemma S with Γ_p := ∪_i {α_i(p), β_i(p)}
(resp. {x_i(s₀), y_i(s₀)}). Collision-freeness still has to be established (R1-14).

**Theorem A (T1 kills every 𝓗-proxy at collision-free primes; PROVED, relative to the following inputs, XR-4).**
* λ-adic Galois representations attached to holomorphic eigenforms with Frobenius polynomial X² − λ(p)X + ψ(p)p^{k−1}
  (Deligne; Deligne–Serre for k = 1; e.g. T. Saito, *Galois representations and modular forms*, Def. 1.2,
  Thm 1.3).
* **Purity:** both roots have absolute value p^{(k−1)/2} (Deligne, Ramanujan–Petersson; Saito, Cor. 4.5). For k = 1,
  finite image gives roots of unity (G. Wiese, *Galois Representations*, Thms 1.3.4–1.3.6).
* The Chebotarev density theorem (Wiese, Thm 1.2.8).

The cross-model reviewer checked these sources. Purity is used separately from existence, in the mixed-collision step
of A.2(b).

Let a ∈ 𝓗_M and let p ∤ M be an odd prime with a(1) = a(p²) = a(p⁴) = … = 0.
1. If Γ_p ∩ (−Γ_p) = ∅, then a(p) = 0 (indeed a(p^m) = 0 for all m).
2. Γ_p ∩ (−Γ_p) = ∅ holds in the following cases:
   * (a) all λ_i are of Eisenstein type (i)/(ii)/(iii) and p ≡ 1 (mod L), where L is the lcm of the conductors of the
     characters involved and the s-parameters are real. Then Γ_p ⊂ ℝ_{>0}.
   * (b) In general (types (i), (ii), (iii) mixed), for every p ∤ Mℓ that splits completely in an explicit number
     field F = F(λ_1, …, λ_r; ℓ) ⊇ ℚ(ζ_{840LM}), for any fixed odd prime ℓ. The primes in (b) have positive density,
     and all of them are ≡ 1 (mod 840), hence lie in 𝔐.

*Proof of 2(b).* Fix an odd prime ℓ. Let E_λ be a finite extension of ℚ_ℓ containing all Hecke fields and the
characters' values, with ring of integers O and maximal ideal 𝔪. For each cuspidal λ_i, Deligne (k ≥ 2) and
Deligne–Serre (k = 1) give a continuous ρ_i: G_ℚ → GL₂(O), unramified outside Mℓ, with
det(X − ρ_i(Frob_p)) = X² − λ_i(p)X + ψ_i(p)p^{k_i−1}. For Eisenstein λ_i take ρ_i = ψ₁ ⊕ ψ₂ε^{k−1}, with ε the
ℓ-adic cyclotomic character. Type (ii) twists by ε^j.

Let F be the compositum of the following finite Galois extensions of ℚ:
* the fixed field of the kernel of ⊕_i ρ̄_i (mod 𝔪);
* ℚ(ζ_ℓ), which makes ε^j ≡ 1 at split primes, needed for type (ii);
* ℚ(ζ_{840LM});
* the normal closures of the Hecke fields of the cuspidal λ_i (R1-3).

Let p ∤ Mℓ split completely in F. Three kinds of pairs γ, γ′ have to be checked.
* *(i)/(ii) against (i)/(ii).* Every ρ_i(Frob_p) ≡ I (mod 𝔪). Its eigenvalues are α_i(p), β_i(p), embedded in Ō, and
  they are ≡ 1 modulo the maximal ideal of Ō. So γ + γ′ ≡ 2 ≢ 0, since ℓ is odd.
* *(iii) against (iii), and (iii) against Eisenstein (i)/(ii).* All characters are 1 at p (ζ_{LM} ⊂ F), so these
  parameters are positive reals and γ + γ′ > 0.
* *(iii) against cuspidal (i)/(ii) (R1-3).* A collision forces a cuspidal parameter γ = −t with t > 0 real. Since
  ψ_i(p) = 1, the parameters satisfy αβ = p^w with w = k_i − 1 + 2j, and |α| = |β| = p^{w/2} (Deligne; for k = 1
  Deligne–Serre gives roots of unity). Hence α = β = −p^{w/2} and λ_i(p)·p^j = −2p^{w/2}.
  * If w is even, this is a rational integer. But it is ≡ tr ρ_i(Frob_p) ≡ 2 (mod 𝔪), while −2p^{w/2} ≡ −2
    (p ≡ 1 mod ℓ). So 4 ≡ 0 (mod ℓ), a contradiction.
  * If w is odd, √p lies in the Hecke field. Then ℚ(√p) ⊆ F, and since p ≡ 1 (mod 4), p ramifies in ℚ(√p). But p
    splits completely in F, a contradiction.

So Γ_p ∩ −Γ_p = ∅. Chebotarev gives density 1/[F : ℚ] > 0. ∎

**Corollary A1 (answers Q1 and Q2 for 𝓗; PROVED, same inputs).**
* (a) *(Q2, support form.)* No a ∈ 𝓗_M is both valid and effective. The field F, and hence the density, depends on
  the chosen a; no universal positive-density set for all of 𝓗 is claimed. Validity gives a(m²) = 0 for all odd m
  coprime to M, and then
  a(p) = 0 for the positive-density set of 𝔐-primes in Thm A.2(b). In case (a) this holds for every p ≡ 1 (mod lcm(L, 840)).
* (b) *(Q1.)* There is no a ∈ 𝓗_M with a = R on all n ≡ 1 (mod 4) coprime to M. Equality on primes alone is not
  enough; one needs equality at 1 and at odd squares too (R1-1). If a = R on those n, then a(1) = R(1) = 0 and
  a(p^{2j}) = R(p^{2j}) = 0, so R(p) = 0 for every p ∤ M splitting completely in F. But there are such p with R(p) ≥ 1. Pick a prime q ≡ 3 (mod 4)
  unramified in F and q ∤ M. Chebotarev in F(ζ_q), with F ∩ ℚ(ζ_q) = ℚ, gives p split in F with 4p + 1 ≡ 0 (mod q).
  Then d = q, C = 1 is a (★) witness, since q | 4p + 1, q ≡ −1 (mod 4) and q ≤ (4p + 1)/3.
  * This complements SIGN_IDENTITY Thm 2.2 (a size argument) with a T1 argument. It covers quasi-modular forms and
    log-power-size divisor sums (τ(n), Σ_{d|n} log d·log(n/d), …), which the size argument does not reach.
* (c) *(Q3; elementary observation, R1-6.)*
  * A *support* proxy E + c ∈ 𝓗 that is valid cannot be effective, by (a).
  * More generally, if a main term E ∈ 𝓗 is T1-compatible (E(1) = E(p^{2j}) = 0), then E(p) = 0 on the Thm A.2 set.
  * If E is not T1-compatible, the error R − E equals −E(m²) at odd squares, as large as the main term there. So any
    error bound has to use non-squareness of p.
  * This is *not* an impossibility theorem for a prime-only "E + error" argument when the error is not itself in 𝓗.

**What an 𝓗-proxy can see at p (PROVED core + Assessment, R1-4).** PROVED (Lemma S): a T1-compatible a ∈ 𝓗 can be
non-zero at p only if some γ, −γ ∈ Γ_p.
* The main source of collisions is twist pairs f, f ⊗ ψ at primes with ψ(p) = −1, where ψ is any character with
  ψ(p) = −1, not necessarily quadratic. Example: a = f − f ⊗ χ_{−4} vanishes at every square and equals 2λ_f(p) at
  p ≡ 3 (mod 4).
* Other collisions exist on sets of positive density. A CM form has α = −β at the inert primes (density ½), and two
  CM forms for the same field can collide there. Weight-one forms with finite image can have positive-density
  trace-zero sets.
* No classification is claimed. Assessment: in the examples examined, the set where a T1-compatible proxy can be
  non-zero is cut out by Frobenius conditions in a fixed finite extension, i.e. congruence-type data.

The PROVED consequence is Thm A.2(b): the proxy vanishes on a positive-density Chebotarev set of 𝔐-primes.

**Numerical sanity check (CERTIFIED arithmetic, small range; `scripts/z58_automorph_lemmaS.py`, output
`data/z58/automorph/lemmaS_out.txt`).**
* Span{τ, τχ₋₄, σ₁₁, σ₁₁χ₋₄, σ₃, σ₃χ₋₄, nσ₁, r, n·r}, where r(n) = Σ_{d|n} χ₋₄(d) and nσ₁ is the D E₂-type
  quasi-modular piece. For each prime 3 ≤ p < 40 we solved a(p^{2j}) = 0, j = 0..12. At every p ≡ 1 (4) the solution
  space forces a(p) = 0. At every p ≡ 3 (4) it allows a(p) ≠ 0, through f − f ⊗ χ₋₄.
* Generic Satake data: the T1 equations force a(p) = 0, including a non-trivial "3-cycle" solution
  (pairs {2,3}, {3,5}, {5,2}). With a twist collision (γ, −γ) a(p) ≠ 0 occurs.

**The sign form Q2′ is not covered by a single-prime argument (PROVED by example).** Take
a(n) = 5σ₁(n) − (2n + 3)·r(n): σ₁ is the weight-2 Eisenstein (E₂) piece, n·r(n) is D of the weight-one Eisenstein
series Σ r(n)qⁿ, and r is weight one (R1-13). For every
prime p ≡ 1 (4):
* a(1) = 5 − 5 = 0;
* a(p) = 5(p + 1) − 2(2p + 3) = p − 1 > 0;
* a(p^{2j}) < 0 for j ≥ 1. For p ≥ 7: 5σ₁(p^{2j}) < 5p^{2j}·p/(p−1) ≤ (35/6)p^{2j} < 6p^{2j} ≤ (2j+1)(2p^{2j}+3). For p = 5,
  a(25) = −4, and for j ≥ 2 the factor 2j + 1 ≥ 5 wins. Checked for p < 60, j ≤ 3.

So T1 at the powers of p alone does not force a(p) ≤ 0 in the minorant form. The example fails globally: a(q²) > 0 for
q ≡ 3 (4) (`lemmaS_out.txt`). Globally the sign form is not killed by T1 either (§3, Prop B1).

---

## 3. The sign / minorant form Q2′: T1 alone does not kill it, and validity is (MS) again

**Prop B1 (T1-sign is satisfiable globally inside 𝓗; PROVED for all odd m; also checked numerically).** Let
a(n) := 5σ₂(n) − (2n² + 3)τ(n). It is in 𝓗 via type (iii) with e = 0: σ₂(n) = Σ d², n²τ(n) = Σ d²(n/d)², τ(n) = Σ 1.
σ₂(n)/n is the arithmetic part of the n-th coefficient of the weight-0 Eisenstein series E(z, 3/2); τ(n) is that of
∂_sE(z, s) at s = ½. Then:
* a(1) = 0 and a(p) = 5(1 + p²) − 2(2p² + 3) = p² − 1 > 0 at every prime p;
* a(m²) ≤ 0 for every odd m.

*Proof of the second item.* For m = 1, a(1) = 5 − 5 = 0. For odd m > 1 write m² = Π p^{2e_p}. Then
σ₂(m²)/m⁴ = Π_p (1 + p^{−2} + … + p^{−4e_p}) < Π_{p odd}(1 − p^{−2})^{−1} = (3/4)ζ(2) < 1.234, and a(m²) < m⁴(5σ₂(m²)/m⁴ − 2τ(m²)).
* If ω(m) = 1, m = p^e: σ₂(p^{2e})/p^{4e} < p²/(p² − 1) ≤ 9/8, so 5σ₂/m⁴ < 5.625 < 6 ≤ 2(2e + 1) = 2τ(m²).
* If ω(m) ≥ 2: τ(m²) ≥ 9, so 5·1.234 < 18 ≤ 2τ(m²).

In both cases a(m²) < 0. ∎
CERTIFIED for all odd m ≤ 20 001: max a(m²)/m⁴ = 0, attained at m = 1 (`classes_out.txt`).

So, unlike the support form (Thm A), the minorant form is **not** killed by T1, even globally and even with all odd
squares. The example is invalid as a proxy, as it must be: a(p) = p² − 1 > 0 at the 14 (★)-zero primes (F4), and
a(p) ≫ R(p).

**Prop B2 (single-prime T1-sign at log scale; PROVED).** Even at log size (exponent-0 Eisenstein derivatives, the size
class of R) the constraint at one prime is satisfiable. Take
a(n) = Σ_{d|n} [½(log²d + log²(n/d)) − 5 log d·log(n/d)],
a type-(iii) combination of second derivatives. On p^m:
a(p^m) = log²p·Σ_{j=0}^m [½(j² + (m−j)²) − 5j(m−j)] = log²p·[m(m+1)(2m+1)/6 − 5m(m+1)(m−1)/6] = log²p·m(m+1)(2 − m)/2.
This is 0 at m = 0 and m = 2, log²p at m = 1, and negative for m ≥ 3. (R1-2: the first version omitted the factor ½
and was wrong.)

**Reading (Assessment, scoped to the examined constructions; XR-3).**
* A minorant a with a(n) > 0 ⟹ R(n) ≥ 1 is *valid* only if that implication holds at every n. Suppose a(p) > 0 has
  been established at every target prime, with matching thresholds. Then checking validity there is equivalent to
  (MS). Without effectiveness this is no longer so: the zero minorant is trivially valid and implies nothing.
* Among the constructions examined, the proxies with a structural reason for validity are those built from
  certificates (a(n) = Σ_{solutions} w, w > 0). These are support proxies, and Theorem A kills them in 𝓗.
* B1–B2 do *not* exclude a structurally justified, effective, signed minorant. That remains open.
* Pointwise minorants a ≤ R obtained by sieve inequalities are typically fixed-conductor divisor-sum weights. That is
  the B6 world; STRONG_APPROX Thm 9.1(b) covers the exponent-0 holomorphic Eisenstein case. B1–B2 show T1 does not by
  itself kill such weights.

## 4. The escapes Theorem A leaves, and what each runs into

Theorem A uses two structural facts about a proxy (XR-1):
* (H1) a(p^m) at the powers of the *same* prime p has a proper rational generating function with poles at reciprocal
  Satake-type parameters (a Hecke recursion).
* (H2) collision-freeness, Γ_p ∩ −Γ_p = ∅, on a positive-density set of primes. Its source depends on the parameters:
  * for the algebraic parameters of types (i)/(ii), residual Galois control: reduction mod 𝔪 in a finite extension;
  * for the real type-(iii) parameters, positivity at primes where the characters are trivial; non-integral real powers
    need not even be algebraic and have no mod-𝔪 reduction;
  * for mixed pairs, Deligne purity plus the Hecke-field ramification argument.

The escapes are the objects that violate (H1) or (H2). The assessments below concern the specific constructions
examined; none is a classification (R1-12).

### E1. Half-integral weight (satisfies H1, violates H2: unavoidable ± poles; Assessment + Prop C; XR-1)

For g ∈ M_{3/2}(Γ₀(4N), ψ), Hecke theory (T_{ℓ²}, Shimura) relates only a(tm²) for a fixed squarefree t. The odd
squares (t = 1) and each prime p (t = p) lie in **different** Shimura orbits, so T1 imposes nothing on a(p) through
Hecke structure.

Precisely: let g be a T(p²)-eigenform with eigenvalue λ, p ∤ 2N. For m ≥ 1 the recursion
a(p^{m+2}) = λa(p^m) − ψ(p)²p·a(p^{m−2}) decouples odd and even exponents. If the even p-power coefficients vanish,
then Σ_m a(p^m)T^m = a(p)T/(1 − λT² + ψ(p)²pT⁴).
* This is proper rational, so (H1) holds.
* Its poles come in ± pairs, so (H2) fails unavoidably.
* a(p) ≠ 0 is allowed.

So E1 escapes collision-freeness, not (H1). This is the one place where the Deligne-type template exists *pointwise at primes*:
* the Eisenstein part is E(p) ≍ p^{1/2}L(1, χ_{−4p})·δ(p) ≫ p^{1/2−ε} (Siegel, ineffective) when the local density
  δ(p) ≠ 0;
* cusp forms orthogonal to unary theta series have |c(p)| ≪ p^{1/2−1/28+ε} (Iwaniec 1987, Duke 1988; cited, not
  re-checked);
* unary theta series vanish at large primes.

This is how Duke–Schulze-Pillot prove representation of large integers by ternary forms.

**Prop C (what the falsifiers force on a weight-3/2 support proxy; CONDITIONAL, R1-7).** Let
g = E + U + c ∈ M_{3/2}(Γ₀(4N), ψ): Eisenstein part, unary-theta part, and cusp part orthogonal to unary theta series.
Suppose g is a support proxy: g(n) ≠ 0 ⟹ R(n) ≥ 1 for n ≡ 1 (4). A *joint local class* 𝒞 means a choice of classes in
ℚ_ℓ^×/ℚ_ℓ^{×2} for every ℓ | 2N, with n ≡ 1 (mod 4).

Hypotheses:
* (I) Iwaniec–Duke: |c(n)| ≪ n^{1/2−1/28+ε} for squarefree n (cited, not re-checked).
* (H_E) For each joint local class 𝒞, E is either ≡ 0 on the squarefree n ∈ 𝒞, or |E(n)| ≫_{𝒞,ε} n^{1/2−ε} on all
  squarefree n ∈ 𝒞. This is an explicit *additional hypothesis*. It is expected from the Siegel–Weil / Cohen–Shimura
  shape of Eisenstein coefficients (local densities times L(1, χ_{−4n}) times n^{1/2}, plus Siegel's bound), but it is
  not proved here for arbitrary Eisenstein combinations, where cancellation and character restrictions need care.

Then:
* (a) If 𝒞 contains infinitely many squarefree R-zeros, E ≡ 0 on the squarefree n ∈ 𝒞. Proof: unary-theta
  coefficients vanish on squarefree n outside finitely many square classes. At the zeros, 0 = E(n) + c(n). Take
  ε < 1/56 and compare (I) with (H_E).
* (b) Consequently, if the joint class 𝒞₁ of 1 (n ≡ 1 mod 8, n a unit square at each odd ℓ | N) contains infinitely
  many squarefree R-zeros, then g(p) = c(p) is a pure cusp coefficient at every large prime p ∈ 𝒞₁. That includes the
  positive-density set p ≡ 1 (mod 8N·840) of 𝔐-primes. There g has no main term, so the Duke template has nothing to
  bound.

**Falsifier data for the hypothesis of (b) (EVIDENCE; `scripts/z58_automorph_classes.py`, `classes_out.txt`).**
These scripts use the supplied zero lists; they do not re-certify them.

*Table 1.* Counts of known zeros with n ≡ 1 (8) that are unit squares mod **every** odd ℓ ≤ P. This is the class 𝒞₁
for levels N divisible by all odd primes ≤ P:

| P | composite (285) | composite, squarefree | sqf, n > 10⁶ | (★)-primes (14) | 𝔊*-primes (38) | R₈-primes (12, ~10¹⁰) |
|---|---|---|---|---|---|---|
| 3 | 71 | 58 | 9 | 14 | 30 | 6 |
| 7 | 15 | 15 | 2 | 9 | 20 | 4 |
| 13 | 6 | 6 | 2 | 4 | 8 | 3 |
| 19 | 1 | 1 | 1 | 2 | 3 | 2 |
| 23 | 1 | 1 | 1 | 0 | 1 | 1 |

Per decade, the composite zeros that are locally square at {3, 5, 7} number 0, 0, 3, 3, 7, 2 (decades
10¹…10⁶⁺, the last one truncated at 8·10⁶).

*Table 2 (R1-8).* Single odd prime level N = ℓ: counts of known zeros with n ≡ 1 (8) and (n/ℓ) = 1.

| ℓ | composite | composite sqf, n > 10⁶ | (★)-primes | 𝔊*-primes | R₈-primes |
|---|---|---|---|---|---|
| 3 | 71 | 9 | 14 | 30 | 6 |
| 7 | 141 | 26 | 10 | 22 | 7 |
| 13 | 147 | 26 | 7 | 19 | 7 |
| 23 | 147 | 37 | 7 | 15 | 8 |
| 101 | 139 | 27 | 8 | 16 | 4 |

Reading (Assessment):
* For levels with few prime factors, zeros in 𝒞₁ are plentiful and keep appearing up to 8·10⁶ (Table 2). This is
  consistent with (b)'s hypothesis. It is EVIDENCE, not proof; (b) needs infinitely many squarefree zeros there.
* Only for levels divisible by *all* odd primes up to ~20 is the known data nearly exhausted (Table 1). So E1 is not
  closed by the falsifier data for such levels. It stays a formal escape, conditional anyway on (H_E).
* F2: the R₈-zeros near 10¹⁰ include locally-square ones (Tables 1–2). A C-even weight-3/2 proxy is constrained exactly
  like the full one, and an E1 argument would have to see C-parity.

**What E1 runs into when instantiated with CM/Heegner objects (Assessment, scoped to that instantiation).**
* Support alone does not force a size. But a proxy whose positivity at p comes from a non-zero Eisenstein part has
  g(p) ≍ p^{1/2±ε} at good primes, while R(p) ≍ log²p on average. If it is a weighted certificate count, the weights
  are ≍ p^{1/2}/log²p.
* The natural weight-3/2 objects of that size examined here are class numbers / CM-point counts of h(−4p) type
  (Zagier ℋ, Gross–Kohnen–Zagier, Duke's theorem).
* By the paper's dictionary (`es-automorphic-barrier-note.tex`, Prop "wedge" in §2.2 and §6 "What ES needs"),
  certificates correspond to Heegner points lying in *shrinking* targets of width ≍ |D|^{−1/2} (Planck scale). Duke-type
  pointwise theorems control only targets of fixed or slowly shrinking size, ≥ |D|^{−1/24} (Young) or |D|^{−1/8}
  under Lindelöf.
* So this instantiation of E1 lands on the known Planck-scale wall (paper Assessment `ass:verdict`, §6). E1 is a
  formal escape from Theorem A; no open road through it was found.

### E2. Constructions whose coefficients lie outside 𝓗, e.g. level sums (Assessment with one PROVED remark; XR-2)

A representation format is not an exclusion criterion. A holomorphic fixed-weight Poincaré series lies in a
finite-dimensional space of modular forms, so away from its level it *is* covered by 𝓗 and by Theorem A. What escapes
is a construction whose *resulting coefficients* are not in 𝓗. The level-sum route below is such an escape, not a new
no-go.

R itself is Σ_C D⁻_{4C}(4Cn + 1). Each level is Hecke-finite in N = 4Cn + 1 (Thm K: Dirichlet-character divisor sums
mod 4C), but not in n: the shift n ↦ 4Cn + 1 destroys the Hecke recursion at p-powers, which is exactly what Lemma S
needs.
* *C-direction (PROVED, trivial; R1-10).* For fixed p, C ↦ R_C(p) = D⁻_{4C}(4Cp + 1) has finite support:
  4Cp + 1 = de with d, e ≡ −1 (mod 4C) forces (4C − 1)² ≤ 4Cp + 1, so C ≤ (p + 2)/4.
  * A non-zero holomorphic modular form of any weight (integral or half-integral) with finitely many non-zero
    coefficients is a constant. So when R(p) > 0, the non-zero polynomial Σ_C R_C(p) q^C (no constant term) is not
    modular in C.
  * Modularity in the level variable would therefore need added completion terms. One specific mechanism is the
    partner quadrant Q_t of Thm K (D⁺); positivity then becomes D⁻ vs D⁺, METAPLECTIC's sign-odd part 𝔒. Cor K1 reads
    its mean ≈ 0 as numerical bookkeeping after a non-modular renormalisation; that qualification stands.
  * Other completions are not excluded.
* *n-direction.* Objects whose n-th coefficient is a sum over unboundedly many moduli c of level-c data at cn + const,
  when the resulting coefficients are not in 𝓗. Infinite-level sums, Kloosterman–Kuznetsov sums over all moduli and
  Rademacher-type expansions of non-holomorphic or weakly holomorphic objects are of this kind. R(n) counts the matrices [[a, n],[4C, e]] ∈ SL₂(ℤ) with
  a ≡ e ≡ −1 (mod 4C) and a, e > 0: one Bruhat cell per modulus, positive part (METAPLECTIC §3). Summing such
  cell-restricted counts over all moduli is the H-A hatch (paper Problem H-A). The Eichler–Selberg version is in
  DISCOVERIES item (J)10: ES is the sign-odd part of the split-hyperbolic term and the smallest term in the identity.
* Weakly holomorphic and mock forms with principal parts also live here: their coefficients are Rademacher sums over
  all c, with exponential growth. They are not excluded by Theorem A. No such form with support in {R ≥ 1} is known
  (Assessment). Exponential size alone does not rule them out as support proxies (R1-12).

### E3. Higher depth / objects without GL₂ Hecke theory (violates H2 or H1; Assessment, scoped)

* Indefinite theta series of signature (r, 2) and higher-depth mock forms (Zwegers; Alexandrov–Banerjee–Manschot–Pioline)
  are attached to *quadratic* forms on cones.
* The (★) exponent 4uBC − u − B is cubic. Every slice obtained by fixing one variable is split binary (C fixed: Thm K;
  u or B fixed: the same shape).
* So the indefinite-theta packaging examined here is Σ_C (split signature-(1,1) theta at level C), which is E2. Split
  binary forms give Eisenstein data in that identity (`z39_square_discriminant_shadow`). This is not a classification
  of all possible packagings (R1-12).
* GL(n) Hecke eigen-systems satisfy a degree-n recursion at p. Lemma S applies verbatim, since A_p(T) is proper
  rational with poles at the n Satake parameters. So *at primes where the Satake parameters have no sign collision*,
  T1-compatibility at p-powers again forces a(p) = 0.
* The global Chebotarev step (Thm A.2(b)) needs Galois representations with a mod-𝔪 reduction, available only for
  suitable (e.g. regular algebraic, essentially self-dual) GL(n) forms. It is literature-dependent and not checked
  here. Whether H-D is open beyond non-Hecke-finite objects is therefore left open.

## 5. Verdict, screens, proposed FRONTIER text, bottom line

**Verdict: narrowed.** This is a scoped no-go, stronger than the prior ones, plus a map of the escapes.
* *Answer to the brief's question (R1-5, R1-9).* No support proxy in the Hecke-finite arithmetic class 𝓗 is both valid
  and effective. R is not an element of 𝓗 on n ≡ 1 (mod 4) coprime to the level.
  * 𝓗 covers eigenvalue systems of all holomorphic integral-weight forms (Eisenstein + cusp, any level, character),
    their n^j-twists (quasi-modular forms), and real-parameter divisor sums with parameter derivatives (log-power size).
  * This is **Theorem A / Corollary A1, PROVED** relative to Deligne / Deligne–Serre and Chebotarev.
  * The mechanism is T1 at the powers of p alone, through Lemma S. A T1-compatible a ∈ 𝓗 can be non-zero at p only
    through a sign collision of Satake parameters. Collision-free primes include a positive-density Chebotarev set
    inside p ≡ 1 (mod 840).
  * In the examples examined, the collision sets are Frobenius conditions in a fixed finite extension, i.e.
    congruence-type data (Assessment, not a classification).
  * Valid but ineffective proxies exist (e.g. τ(n)·1[n ≡ 5 mod 12]).
* *Q3 (Eisenstein + cusp with Deligne pointwise).* A *support* proxy E + c ∈ 𝓗 cannot be effective (Cor A1(a)). For a
  prime-only "main term + error" argument, Cor A1(c) is only an elementary observation: the error must use
  non-squareness. It is not an impossibility theorem when the error is outside 𝓗.
* *Q2′ (minorant form).* Not killed by T1 (Props B1, B2, PROVED). For an effective minorant (a(p) > 0 at all target
  primes) validity at those primes is equivalent to (MS). No structural reason for validity was found among the
  constructions examined, but an effective signed minorant with such a reason is not excluded (Assessment, XR-3).
* *Escapes.*
  * E1, half-integral weight, is the only place found where a pointwise Deligne/Duke template coexists with T1. Prop C
    (CONDITIONAL on (H_E) and Iwaniec–Duke) shows that the falsifiers force the Eisenstein part to vanish on every joint
    local class carrying infinitely many squarefree zeros. Instantiated with CM/Heegner objects, it is the Planck-scale
    wall.
  * E2 (constructions whose coefficients lie outside 𝓗, e.g. level sums) is H-A/B2.
  * E3: the examined packagings reduce to E2. GL(n) Hecke-finite objects fall under Lemma S at collision-free primes.

**Falsifier table, final.**
* F1: the mechanism uses non-squareness only via Lemma S. What remains is the Satake sign-collision set at p. On the
  Thm A.2(b) set it is empty.
* F2: line-blind, so no false theorem.
* F3: not used by Thm A; used by Prop C.
* F4: nothing is proved positive. The sign example B1 is correctly invalid at the 14 (★)-zero primes.
* No HOT LEAD.

**FRONTIER §4 hard screens for the best idea (Thm A as a screen).**
* T1: it *is* T1, at p-powers.
* 8/131: line-blind.
* Tied modulus: not addressed; Hecke-finite objects have fixed level.
* Fixed p: the proof is pointwise at one p (Lemma S), which is why it kills proxies prime by prime.

**Proposed FRONTIER §6/§7 text (do not edit FRONTIER here).**
> *Automorphic proxies (z58 AUTOMORPH, Thm A, PROVED rel. Deligne/Deligne–Serre + Chebotarev).*
> * Let a be a finite combination of GL₂ Hecke eigen-systems: holomorphic integral weight, Eisenstein or cusp, any
>   level/character; their n^j-twists (quasi-modular forms); real-parameter divisor sums Σ d^a(n/d)^b and their
>   parameter derivatives. If a(1) = a(p²) = a(p⁴) = … = 0, then a(p) = 0 unless two Satake parameters at p are
>   negatives of each other.
> * Hence a support proxy of this kind (a(n) ≠ 0 ⟹ R(n) ≥ 1) vanishes on a positive-density set of primes
>   ≡ 1 (mod 840): it cannot be valid and effective. R is not such an a on n ≡ 1 (mod 4).
> * The minorant form is not killed by T1 (explicit examples). For an effective minorant, validity at the target
>   primes is equivalent to (MS).
> * Escapes:
>   * half-integral weight, which has proper rational p-power series but unavoidable ± poles; the CM/Heegner
>     instantiation is the Planck-scale wall;
>   * constructions whose coefficients lie outside 𝓗, such as level sums (H-A/B2);
>   * higher-depth / non-GL₂ objects.
>
>   Prop C stays CONDITIONAL. The verdict is "narrowed".
> * Add to §6: "support proxies with an Eisenstein + cusp decomposition and Deligne bounds, for any fixed-level
>   integral-weight object, quasi-modular form or real-parameter Eisenstein derivative".

**Bottom line.** The brief asked whether a modular, mock or higher-depth object with a Deligne-strength pointwise
cusp bound could carry (MS). For support proxies built from GL₂ Hecke eigen-systems (where Deligne bounds live) the
answer is a clean **no**.
* Odd-square vanishing at p², p⁴, … alone forces the coefficient at p to vanish unless two Satake parameters at p are
  negatives of each other. On a positive-density set of 𝔐-primes that never happens.
* This kills, in that class, the "valid and effective support proxy" question, the exact-identity question, and the
  Eisenstein-plus-cusp template for support proxies.
* It extends the prior size-based (Thm 2.2) and Eisenstein-only (Thm 9.1, Prop 2.3) no-gos to cusp forms,
  quasi-modular forms and log-sized divisor-sum derivatives.
* The minorant form survives T1. Among the constructions examined, automorphy gave no reason for validity.

The escape hatches it leaves:
* half-integral weight, which has ± poles that cannot be avoided; a pointwise template exists there but needs
  Planck-scale equidistribution when instantiated by CM objects;
* constructions whose coefficients lie outside 𝓗 (level sums), which is the old H-A/B2 wall.

Nothing here moves (MS) toward a proof.

## 6. Commands and files
All runs: `ulimit -v 4000000`, `timeout` as shown.
* `timeout 1200 uv run --with sympy python scripts/z58_automorph_lemmaS.py` (ulimit -v 4000000) → `data/z58/automorph/lemmaS_out.txt` (Lemma S / Thm A sanity checks, local sign example).
* `timeout 900 uv run --with sympy python scripts/z58_automorph_classes.py 20001` → `data/z58/automorph/classes_out.txt`
  (local square classes of the known zeros; global check of Prop B1 for odd m ≤ 20 001).

## 7. Review log
* **R1 (hostile deep-mode subagent review of the full memo):** 2 FATAL, 10 MAJOR, 2 MINOR. All repaired; places marked
  (R1-n).
  * FATAL 1: Cor A1(b) claimed R ∉ 𝓗 "on primes". Equality on primes does not give vanishing at squares. Now stated for
    equality on all n ≡ 1 (4) coprime to M.
  * FATAL 2: the Prop B2 polynomial was wrong. The ½ factor is restored; recomputed to m(m+1)(2 − m)/2.
  * MAJOR:
    * Thm A.2(b) lacked the cross-collision argument between type-(iii) and cuspidal parameters. It is added, using
      Deligne purity, F ⊇ ℚ(ζ_{LM}) and the normal closures of the Hecke fields.
    * The density-0 "quadratic characters only" classification was false as stated (CM forms, weight one). It is
      deleted and replaced by the PROVED collision statement plus a scoped Assessment.
    * Headline wording now says "valid and effective", with the counterexample τ(n)·1[n ≡ 5 mod 12].
    * Cor A1(c) is softened to an observation.
    * Prop C now has an explicit Eisenstein lower-bound hypothesis (H_E) and joint local classes.
    * The Table 1 reading is corrected, and Table 2 (single-prime levels) added.
    * The mock-class identification is removed.
    * The E2 finite-support remark is restricted to R(p) > 0; other completions are not excluded.
    * The paper `thm:ternary` citation is corrected (thin-set caveat).
    * E1/E3 exclusivity claims are scoped.
  * MINOR: nr(n) is D of weight one. The Σ log(n/d²) ≡ 0 example is removed. B1 is relabelled PROVED globally. The
    Lemma S hypothesis wording is fixed and the stale checkpoint text removed.
  * The reviewer reran both scripts under the memory limit; outputs matched the committed files.
* **Cross-model review** (`data/z58/xreview/REVIEW_AUTOMORPH.md`, ACCEPT-WITH-FIXES). Thm A / Cor A1 were
  independently re-derived and both scripts reproduced byte-identically. Required fixes applied:
  * XR-1: E1 corrected. A T(p²)-eigenform with vanishing even p-power coefficients has the proper rational series
    a(p)T/(1 − λT² + ψ(p)²pT⁴), so E1 escapes collision-freeness (± poles), not H1. H2 is rewritten to separate
    residual Galois control (algebraic parameters), positivity (real type-(iii) parameters, possibly non-algebraic)
    and purity (mixed pairs).
  * XR-2: representation formats are no longer exclusion criteria. Fixed-weight holomorphic Poincaré series are in
    𝓗; E2 now reads "constructions whose resulting coefficients lie outside 𝓗".
  * XR-3: the sign-form assessment is made conditional on effectiveness (the zero minorant is valid). "Automorphy buys
    nothing" and "the only automorphic-native proxies" are scoped to the examined constructions. B1–B2 do not exclude
    an effective, structurally justified signed minorant.
  * XR-4: the definition is made explicit (c_i ∈ ℂ, finite r, fixed M, finite derivative orders, type (iii) as
    ∂_a^r∂_b^s at real points). 𝓗 is no longer used as a synonym for "Hecke-finite". F depends on the chosen proxy.
    "Coprime odd m" is written where needed. Explicit purity, Galois and Chebotarev references are added (Saito
    Def 1.2 / Thm 1.3 / Cor 4.5; Wiese Thms 1.2.8, 1.3.4–1.3.6).

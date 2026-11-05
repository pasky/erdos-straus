# Z58_AUTOMORPH — modular / mock-modular generating functions for (MS): a T1 no-go for every Hecke-finite proxy, and where the escape lies

Status: z58 lane AUTOMORPH (brief `z52bbriefs/z58_lanes.md` §AUTOMORPH, common rules `z52bbriefs/z53_depth.md`).
Internal; internally reviewed only. **ES is OPEN; nothing here proves or disproves ES, (★), or (MS).**
Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment.
Scripts `scripts/z58_automorph_*`, data `data/z58/automorph/`.
Read: `paper/es-automorphic-barrier-note.tex` (§§1, 4.1, 6, 7), `METAPLECTIC_ES.md` (Thm K, Cor K1, Prop S, §§3–5),
`SIGN_IDENTITY.md` (Thm 2.2, Prop 2.3, Prop 2.4), `STRONG_APPROX_ES.md` Thm 9.1, `GROWING_IDENTITIES` (Eichler–Selberg
item in DISCOVERIES #10), `BRAINSTORM/z39_square_discriminant_shadow.md`, `Z57_SYNTH.md` §§0–2, the falsifier data.

**Checkpoint 1 (this version): §0 falsifier table, §1 precise statements, §2 Lemma S and Theorem A (PROVED) with a
numerical sanity check.** Later sections are placeholders.

---

## 0. MANDATORY FALSIFIER TABLE

The *mechanism* examined: "write Σ R(n)qⁿ, or a proxy a(n) with a(n) ≠ 0 ⟹ R(n) ≥ 1, as an automorphic object;
split it into Eisenstein (main term) + cusp/shadow part; bound the cusp part pointwise (Deligne/Duke) below the main
term at a single prime."

| screen | behaviour of the mechanism |
|---|---|
| **F1 odd squares** | The proxy must vanish at 1, p², p⁴, … (all odd squares). **Theorem A (PROVED):** for every *Hecke-finite* proxy (holomorphic forms of integral weight, any level/character, Eisenstein or cuspidal, quasi-modular forms, real-parameter s-derivatives of Eisenstein series) this vanishing *at the powers of p alone* forces a(p) = 0, unless the Satake multiset at p contains a pair γ, −γ. Such ± collisions are twist characters ψ(p) = −1 (plus accidental collisions). So the only place primality (non-squareness) enters is through *quadratic characters of p of bounded conductor*, i.e. through congruence data. On a positive-density set of 𝔐-primes (all ≡ 1 mod 840), every such proxy vanishes. In half-integral weight, squares and primes lie in different Shimura square classes, so F1 does not bind the same way; see §4 (escape E1). |
| **F2 C-even sub-line** | Theorem A applies verbatim to R₈ (R₈ ≤ R, so R₈(m²) = 0): the no-go is line-blind and proves nothing false. For the escape E1 any proxy has to tell the C-odd line from the C-even line. No candidate does (§4). |
| **F3 composites** | Theorem A uses only T1 at the powers of p, not the 285 composite zeros. The composite zeros constrain the half-integral-weight escape: they force the weight-3/2 Eisenstein density to vanish on square classes where infinitely many zeros live. That step is CONDITIONAL (§4, Prop C). |
| **F4 known zeros** | The no-go proves no positivity, so nothing to check. Any proxy must vanish at the 14 (★)-zeros (three of them ≡ 1 mod 840: 712 321, 1 726 201, 8 813 281) and, if it is meant for 𝔊*, at the 38 𝔊*-zeros. |

Verdict at checkpoint 1: the mechanism is **dead for every Hecke-finite object** (Thm A). The escapes it leaves are
(E1) half-integral weight, (E2) objects that are not Hecke-finite in n (level sums Σ_C over the variable 4Cn + 1,
Poincaré/Rademacher series, Fourier–Jacobi expansions), and (E3) higher-depth objects without Hecke theory.

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
* Paper Thm 4.1 ("ternary"): fixed-complexity theta-series embeddings are covered by Mordell classes only.
* DISCOVERIES #10 (GROWING_IDENTITIES Prop 2.1/2.2): ES is the sign-odd part of the split-hyperbolic Eichler–Selberg
  term.

**What is new here.**
* Theorem A extends the T1 kill from Eisenstein to *all* GL₂ Hecke-finite objects, including cusp forms (where Deligne
  bounds live), quasi-modular forms and real-parameter Eisenstein derivatives (the "mock with Eisenstein shadow" class,
  which has the right log² size and so escapes Thm 2.2).
* It needs only T1 at the powers of the single prime p.
* It identifies exactly what such an object can see at p: ± collisions of Satake parameters, i.e. quadratic
  characters.

---

## 2. Lemma S and Theorem A

**Lemma S (sign lemma; PROVED, elementary).** Let K be a field of characteristic 0 and let a: {p^m : m ≥ 0} → K.
Suppose A(T) := Σ_{m≥0} a(p^m) T^m is a rational function that is *proper* (it tends to 0 as T → ∞) and whose poles
all lie in {1/γ : γ ∈ Γ} for a finite set Γ ⊂ K^×. Suppose further that Γ ∩ (−Γ) = ∅. If a(p^{2j}) = 0 for all
j ≥ 0, then a(p^m) = 0 for all m ≥ 0. In particular a(p) = 0.

*Proof.* The even part ½(A(T) + A(−T)) has Taylor coefficients a(p^{2j}) = 0, so A(T) = −A(−T) as rational
functions. The poles of A(T) lie in P := {1/γ}, and those of −A(−T) lie in −P. By hypothesis P ∩ (−P) = ∅, so the
two functions, being equal, have no poles at all. Hence A is a polynomial. It is also proper, so A = 0. ∎

**Hecke-finite class 𝓗_M (definition).** 𝓗_M is the set of functions a on {n : (n, M) = 1} of the form
a(n) = Σ_{i=1}^r c_i λ_i(n), with each λ_i one of the following.
* (i) The normalised Hecke eigenvalue system λ_f(n) of a holomorphic newform or Eisenstein eigenform f of integral
  weight k ≥ 1, level | M, any nebentypus.
* (ii) n^j λ_f(n), j ∈ ℤ_{≥0}. This covers D^j f and the quasi-modular forms, since QM = ⊕ D^j M ⊕ ℂ D^j E₂ by
  Kaneko–Zagier, and E₂ has λ = σ₁.
* (iii) Σ_{d|n} ψ₁(d)ψ₂(n/d) d^{s+u}(n/d)^{−s+v} or a real-parameter derivative ∂_s^e|_{s=s₀} of it (e ≥ 0), with
  u, v, s₀ real and ψ₁, ψ₂ characters mod M; also mixed partial derivatives in two such parameters. These are the
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
p ∤ M, A_p(T) satisfies the hypotheses of Lemma S with Γ_p := ∪_i {α_i(p), β_i(p)} (resp. {x_i(s₀), y_i(s₀)}).

**Theorem A (T1 kills every Hecke-finite proxy at collision-free primes; PROVED, relative to the existence of
λ-adic Galois representations attached to holomorphic eigenforms (Deligne; Deligne–Serre for k = 1) and the
Chebotarev density theorem).** Let a ∈ 𝓗_M and let p ∤ M be an odd prime with a(1) = a(p²) = a(p⁴) = … = 0.
1. If Γ_p ∩ (−Γ_p) = ∅, then a(p) = 0 (indeed a(p^m) = 0 for all m).
2. Γ_p ∩ (−Γ_p) = ∅ holds in the following cases:
   * (a) all λ_i are of Eisenstein type (i)/(ii)/(iii) and p ≡ 1 (mod L), where L is the lcm of the conductors of the
     characters involved and the s-parameters are real. Then Γ_p ⊂ ℝ_{>0}.
   * (b) In general, for every p that splits completely in an explicit number field F = F(λ_1, …, λ_r; ℓ) containing
     ℚ(ζ_{840}), for any fixed odd prime ℓ. The primes in (b) have positive density, and all of them are ≡ 1 (mod 840),
     hence lie in 𝔐.

*Proof of 2(b).* Fix an odd prime ℓ. Let E_λ be a finite extension of ℚ_ℓ containing all Hecke fields and the
characters' values, with ring of integers O and maximal ideal 𝔪. For each cuspidal λ_i, Deligne (k ≥ 2) and
Deligne–Serre (k = 1) give a continuous ρ_i: G_ℚ → GL₂(O), unramified outside Mℓ, with
det(X − ρ_i(Frob_p)) = X² − λ_i(p)X + ψ_i(p)p^{k_i−1}. For Eisenstein λ_i take ρ_i = ψ₁ ⊕ ψ₂ε^{k−1}, with ε the
ℓ-adic cyclotomic character. Type (ii) twists by ε^j.

Let F be the fixed field of the kernel of ⊕_i ρ̄_i (mod 𝔪) ⊕ (mod-ℓ cyclotomic) ⊕ (mod-840L cyclotomic), a finite
Galois extension of ℚ (the mod-ℓ cyclotomic factor makes ε^j ≡ 1 at split primes, needed for type (ii)).
If p ∤ Mℓ splits completely in F, then every ρ_i(Frob_p) ≡ I (mod 𝔪). Its eigenvalues are α_i(p), β_i(p), embedded
in Ō, and they are ≡ 1 modulo the maximal ideal of Ō. So γ + γ′ ≡ 2 ≢ 0 for all γ, γ′ ∈ Γ_p, since ℓ is odd. Hence
Γ_p ∩ −Γ_p = ∅. Chebotarev gives density 1/[F : ℚ] > 0.

For type (iii) only Dirichlet characters and real powers of p occur. At p ≡ 1 (mod L), with L | [F-conductor] (take
F ⊇ ℚ(ζ_L)), all values are positive reals. ∎

**Corollary A1 (answers Q1 and Q2 for 𝓗; PROVED, same inputs).**
* (a) *(Q2, support form.)* No a ∈ 𝓗_M is both valid and effective. Validity gives a(m²) = 0 for all odd m, and then
  a(p) = 0 for the positive-density set of 𝔐-primes in Thm A.2(b). In case (a) this holds for every p ≡ 1 (mod lcm(L, 840)).
* (b) *(Q1.)* R ∉ 𝓗_M on primes. If R = a on primes coprime to M, then a(1) = R(1) = 0 and a(p^{2j}) = R(p^{2j}) = 0,
  so R(p) = 0 for every p splitting completely in F. But there are such p with R(p) ≥ 1. Pick a prime q ≡ 3 (mod 4)
  unramified in F and q ∤ M. Chebotarev in F(ζ_q), with F ∩ ℚ(ζ_q) = ℚ, gives p split in F with 4p + 1 ≡ 0 (mod q).
  Then d = q, C = 1 is a (★) witness, since q | 4p + 1, q ≡ −1 (mod 4) and q ≤ (4p + 1)/3.
  * This extends SIGN_IDENTITY Thm 2.2 from a size argument to a T1 argument. It now covers quasi-modular forms and
    real-parameter Eisenstein derivatives, which have the right log-power sizes (τ(n) ~ log, Σ log(n/d²)-type ~ log², …).
* (c) *(Q3.)* If a main term E ∈ 𝓗 is T1-compatible, then E(p) = 0 on the Thm A.2 set. If it is not T1-compatible,
  then the error R − E equals −E(m²) at odd squares and is as large as the main term there. So the error bound must use
  non-squareness of p at a step where, by Thm A, a Hecke-finite object only sees quadratic characters of p.

**What an 𝓗-proxy can see at p (Assessment, with a PROVED core).** By Lemma S, a T1-compatible a ∈ 𝓗 can be non-zero
only at primes where some γ, −γ ∈ Γ_p. Pairs of twist-equivalent forms f, f ⊗ ψ give exactly the primes with
ψ(p) = −1. Example: a = f − f ⊗ χ_{−4} vanishes at every square and equals 2λ_f(p) at p ≡ 3 (mod 4). The other
collisions are λ_i(p) = 0 and accidental α_i(p) = −α_j(p) between non-twist-equivalent forms; by Serre / Ramakrishnan
(cited, not checked here) they have density 0. So, **up to density 0, a T1-compatible Hecke-finite proxy is
non-zero only where a quadratic character of bounded conductor takes the value −1 at p. It is a congruence menu in
automorphic disguise**, subject to B1 and to the infinitely many 𝔐-primes that are squares modulo any fixed modulus.

**Numerical sanity check (CERTIFIED arithmetic, small range; `scripts/z58_automorph_lemmaS.py`, output
`data/z58/automorph/lemmaS_out.txt`).**
* Span{τ, τχ₋₄, σ₁₁, σ₁₁χ₋₄, σ₃, σ₃χ₋₄, nσ₁, r, n·r}, where r(n) = Σ_{d|n} χ₋₄(d) and nσ₁ is the D E₂-type
  quasi-modular piece. For each prime 3 ≤ p < 40 we solved a(p^{2j}) = 0, j = 0..12. At every p ≡ 1 (4) the solution
  space forces a(p) = 0. At every p ≡ 3 (4) it allows a(p) ≠ 0, through f − f ⊗ χ₋₄.
* Generic Satake data: the T1 equations force a(p) = 0, including a non-trivial "3-cycle" solution
  (pairs {2,3}, {3,5}, {5,2}). With a twist collision (γ, −γ) a(p) ≠ 0 occurs.

**The sign form Q2′ is not covered by a single-prime argument (PROVED by example).** Take
a(n) = 5σ₁(n) − (2n + 3)·r(n), a holomorphic quasi-modular combination (weight 2, nσ₁ type, and weight 1). For every
prime p ≡ 1 (4):
* a(1) = 5 − 5 = 0;
* a(p) = 5(p + 1) − 2(2p + 3) = p − 1 > 0;
* a(p^{2j}) < 0 for j ≥ 1. For p ≥ 7: 5σ₁(p^{2j}) < 5p^{2j}·p/(p−1) ≤ (35/6)p^{2j} < 6p^{2j} ≤ (2j+1)(2p^{2j}+3). For p = 5,
  a(25) = −4, and for j ≥ 2 the factor 2j + 1 ≥ 5 wins. Checked for p < 60, j ≤ 3.

So T1 at the powers of p alone does not force a(p) ≤ 0 in the minorant form. The example fails globally: a(q²) > 0 for
q ≡ 3 (4) (`lemmaS_out.txt`). A global sign theorem would need T1 at products and is left open (§3, to do).

---

## 3. The sign / minorant form Q2′: T1 alone does not kill it, and validity is (MS) again

**Prop B1 (T1-sign is satisfiable globally inside 𝓗; PROVED for the stated range, CERTIFIED numerically).** Let
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
a(n) = Σ_{d|n} [log²d + log²(n/d) − 5 log d·log(n/d)],
a type-(iii) second derivative. On p^m:
a(p^m) = log²p·Σ_{j=0}^m [j² + (m−j)² − 5j(m−j)] = log²p·m(m+1)(2 − m)/2.
This is 0 at m = 0 and m = 2, log²p at m = 1, and negative for m ≥ 3.

**Reading (Assessment).**
* In Q2′ the automorphic structure does no work. A minorant a with a(n) > 0 ⟹ R(n) ≥ 1 is *valid* only if that
  implication holds at every n. For an abstractly given modular a, checking this at all large primes is (MS) itself.
* The only automorphic-native proxies are those built from certificates (a(n) = Σ_{solutions} w, w > 0). These are
  support proxies, and Theorem A kills them in 𝓗.
* Pointwise minorants a ≤ R obtained by sieve inequalities are fixed-conductor divisor-sum weights. That is the B6
  world (SIGN_IDENTITY Prop 2.3 / STRONG_APPROX Thm 9.1(b) for the exponent-0 holomorphic Eisenstein case). B1–B2 show
  T1 does not by itself kill them prime-by-prime.

## 4. The escapes Theorem A leaves, and what each runs into

Theorem A uses exactly two structural facts about a proxy:
* (H1) a(p^m) at the powers of the *same* prime p has a proper rational generating function with poles at Satake
  parameters (a Hecke recursion);
* (H2) the Satake parameters at p, reduced mod 𝔪, are controlled by a finite Galois extension.

The escapes are the objects that violate (H1) or (H2).

### E1. Half-integral weight (violates H1 across square classes; Assessment + Prop C)

For g ∈ M_{3/2}(Γ₀(4N), ψ), Hecke theory (T_{ℓ²}, Shimura) relates only a(tm²) for a fixed squarefree t. The odd
squares (t = 1) and each prime p (t = p) lie in **different** Shimura orbits, so T1 imposes nothing on a(p) through
Hecke structure. This is the one place where the Deligne-type template exists *pointwise at primes*:
* the Eisenstein part is E(p) ≍ p^{1/2}L(1, χ_{−4p})·δ(p) ≫ p^{1/2−ε} (Siegel, ineffective) when the local density
  δ(p) ≠ 0;
* cusp forms orthogonal to unary theta series have |c(p)| ≪ p^{1/2−1/28+ε} (Iwaniec 1987, Duke 1988; cited, not
  re-checked);
* unary theta series vanish at large primes.

This is how Duke–Schulze-Pillot prove representation of large integers by ternary forms.

**Prop C (what the falsifiers force on a weight-3/2 support proxy; CONDITIONAL on the cited weight-3/2 inputs above
and on the standard shape of weight-3/2 Eisenstein coefficients, E(t f²) = δ(t f²)·(t f²)^{1/2}L(1, χ_{−4t}ψ′)·
Π_{ℓ|f}(positive factor), with δ depending only on the classes of n in ℚ_ℓ^×/ℚ_ℓ^{×2}, ℓ | 2N — Cohen / Shimura,
not re-derived here).** Let g = E + U + c be a weight-3/2 support proxy of level 4N:
g(n) ≠ 0 ⟹ R(n) ≥ 1 for n ≡ 1 (4).
* (a) If an ℓ-adic square class 𝒞 (ℓ | 2N) contains infinitely many squarefree R-zeros, then δ(𝒞) = 0. Proof: at such
  n, 0 = E(n) + c(n) with |c(n)| ≪ n^{1/2−1/28+ε} and |E(n)| ≫ |δ(𝒞)|n^{1/2−ε}.
* (b) Consequently, if the class 𝒞₁ of 1 (n ≡ 1 mod 8, n a unit square at each odd ℓ | N) contains infinitely many
  squarefree R-zeros, then g(p) = c(p) is a pure cusp coefficient at every prime p ∈ 𝒞₁ with p ≡ 1 (mod 840).
  This is a positive-density set of 𝔐-primes. There it has no main term, so the Duke template has nothing to bound.

**Falsifier data for the hypothesis of (b) (EVIDENCE; `scripts/z58_automorph_classes.py`, `classes_out.txt`).**
Among the known zeros, these are the counts of n ≡ 1 (8) that are unit squares mod every odd ℓ ≤ P:

| P | composite (285) | composite, squarefree | sqf, n > 10⁶ | (★)-primes (14) | 𝔊*-primes (38) | R₈-primes (12, ~10¹⁰) |
|---|---|---|---|---|---|---|
| 3 | 71 | 58 | 9 | 14 | 30 | 6 |
| 7 | 15 | 15 | 2 | 9 | 20 | 4 |
| 13 | 6 | 6 | 2 | 4 | 8 | 3 |
| 19 | 1 | 1 | 1 | 2 | 3 | 2 |
| 23 | 1 | 1 | 1 | 0 | 1 | 1 |

Per decade, the composite zeros that are locally square at {3, 5, 7} number 0, 0, 3, 3, 7, 2 (decades
10¹…10⁶⁺, the last one truncated at 8·10⁶).

Reading (Assessment):
* For small levels (N supported on {2, 3, 5, 7}) zeros in 𝒞₁ keep appearing up to 8·10⁶, consistent with (b)'s
  hypothesis. That is EVIDENCE, not proof; it would need infinitely many composite zeros there.
* For large levels (N with a prime ≥ 23) the known zero sets are already nearly exhausted. So E1 cannot be closed by
  the falsifier data. It stays a genuine formal escape.
* F2: the R₈-zeros near 10¹⁰ include locally-square ones up to P = 23. A C-even weight-3/2 proxy is therefore
  constrained exactly like the full one, and an E1 argument would have to see C-parity.

**What E1 runs into when instantiated (Assessment).**
* A weight-3/2 support proxy has a(p) ≍ p^{1/2−ε} at good primes, but R(p) ≍ log²p on average. So it must weight
  each certificate by ≍ p^{1/2}/log²p.
* The natural weight-3/2 objects of that size are class numbers / CM-point counts h(−4p)-type (Zagier ℋ, Gross–Kohnen–
  Zagier, Duke's theorem).
* By the paper's dictionary (`es-automorphic-barrier-note.tex`, Prop "wedge" in §2.2 and §6 "What ES needs"),
  certificates correspond to Heegner points lying in *shrinking* targets of width ≍ |D|^{−1/2} (Planck scale). Duke-type
  pointwise theorems control only targets of fixed or slowly shrinking size, ≥ |D|^{−1/24} (Young) or |D|^{−1/8}
  under Lindelöf.
* So the instantiated E1 lands on the known Planck-scale wall (paper Assessment 6.1). E1 is a formal escape from
  Theorem A, not an open road.

### E2. Level sums: objects not Hecke-finite in n (violates H1; Assessment with one PROVED remark)

R itself is Σ_C D⁻_{4C}(4Cn + 1). Each level is Hecke-finite in N = 4Cn + 1 (Thm K: Dirichlet-character divisor sums
mod 4C), but not in n: the shift n ↦ 4Cn + 1 destroys the Hecke recursion at p-powers, which is exactly what Lemma S
needs.
* *C-direction (PROVED, trivial).* For fixed p, C ↦ R_C(p) = D⁻_{4C}(4Cp + 1) has finite support:
  4Cp + 1 = de with d, e ≡ −1 (mod 4C) forces (4C − 1)² ≤ 4Cp + 1. A non-constant holomorphic modular form of any
  weight (integral or half-integral) has infinitely many non-zero coefficients. So Σ_C R_C(p) q^C is not modular in C.
  Any Kudla-type or theta-lift modularity in the level variable needs *completion terms* of the same size: the partner
  quadrant Q_t of Thm K, i.e. D⁺. Positivity then becomes D⁻ vs D⁺, which is METAPLECTIC's sign-odd part 𝔒 (mean ≈ 0,
  Cor K1) — B2.
* *n-direction.* Objects whose n-th coefficient is a sum over moduli c of level-c data at cn + const: Poincaré series,
  Rademacher expansions, Kloosterman–Kuznetsov sums. R(n) counts the matrices [[a, n],[4C, e]] ∈ SL₂(ℤ) with
  a ≡ e ≡ −1 (mod 4C) and a, e > 0: one Bruhat cell per modulus, positive part (METAPLECTIC §3). Summing such
  cell-restricted counts over all moduli is the H-A hatch (paper Problem H-A). The Eichler–Selberg version is in
  DISCOVERIES #10: ES is the sign-odd part of the split-hyperbolic term and the smallest term in the identity.
* Weakly holomorphic and mock forms with principal parts also live here: their coefficients are exactly Rademacher
  sums over all c, with exponential growth. They are not excluded by Theorem A. They are also not known to have any
  support in {R ≥ 1}, and their coefficient size e^{c√n} makes them useless as weights (Assessment).

### E3. Higher depth / objects without GL₂ Hecke theory (violates H2 or H1; Assessment)

* Indefinite theta series of signature (r, 2) and higher-depth mock forms (Zwegers; Alexandrov–Banerjee–Manschot–Pioline)
  are attached to *quadratic* forms on cones.
* The (★) exponent 4uBC − u − B is cubic. Every linear slice is split binary (C fixed: Thm K; u or B fixed: the same).
* So the only indefinite-theta packaging of R is Σ_C (split signature-(1,1) theta at level C) = E2. Split binary forms
  give Eisenstein data, not mock data (`z39_square_discriminant_shadow`).
* GL(3)-cuspidal coefficients (H-D) violate H1 for GL₂ but satisfy a GL₃ Hecke recursion. Lemma S generalises
  verbatim: A_p(T) is proper rational with poles at the three Satake parameters. So Theorem A extends to finite
  combinations of GL(n) eigen-systems with Galois representations (regular algebraic, essentially self-dual) at
  collision-free primes (Assessment; the Galois input is literature-dependent and not checked here). H-D is therefore
  open only through objects that are *not* Hecke-finite in n.

## 5. Verdict, screens, proposed FRONTIER text, bottom line

**Verdict: narrowed** (a scoped no-go that is stronger and cleaner than the prior ones, plus a map of the escapes).
* *Answer to the brief's question.* Σ R(n)qⁿ is not, and has no support proxy that is, in the Hecke-finite class 𝓗.
  𝓗 includes all holomorphic integral-weight forms (Eisenstein + cusp, any level, character), quasi-modular forms and
  real-parameter s-derivatives of Eisenstein series, i.e. the mock objects with Eisenstein shadow that have the right
  log² size. This is **Theorem A / Corollary A1, PROVED** relative to Deligne / Deligne–Serre and Chebotarev.
  * The mechanism is T1 at the powers of p alone, through Lemma S.
  * What survives is "a(p) can be non-zero only where Satake parameters collide in sign", which is quadratic-character
    (congruence) data up to density 0. So automorphic proxies in 𝓗 are congruence menus in disguise.
* *Q3 (Eisenstein + cusp with Deligne pointwise).* In 𝓗 any T1-compatible main term is 0 on a positive-density set of
  𝔐-primes. A T1-incompatible one has error = main term at squares. Dead in 𝓗 (Cor A1(c)).
* *Q2′ (minorant form).* Not killed by T1 (Props B1, B2, PROVED). But validity of an abstract modular minorant at
  primes is (MS) itself, so automorphy buys nothing there (Assessment).
* *Escapes.*
  * E1, half-integral weight, is the only place where a pointwise Deligne/Duke template coexists with T1. Prop C
    (CONDITIONAL) shows the falsifiers force its Eisenstein density to vanish on every square class carrying infinitely
    many zeros. Instantiated with CM/Heegner objects it is the Planck-scale wall.
  * E2 (level sums) is H-A/B2.
  * E3 reduces to E2, or to GL(n) Hecke-finite objects where Lemma S applies again.

**Falsifier table, final.**
* F1: the mechanism uses non-squareness only via Lemma S; the residual primality information is quadratic characters
  of p (Thm A).
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
> * If a is a finite combination of GL₂ Hecke eigen-systems (holomorphic integral weight, Eisenstein or cusp, any
>   level/character; quasi-modular; real-parameter Eisenstein s-derivatives) and a(1) = a(p²) = a(p⁴) = … = 0, then
>   a(p) = 0 unless two Satake parameters at p are negatives of each other.
> * Hence every such "support proxy" (a(n) ≠ 0 ⟹ R(n) ≥ 1) vanishes on a positive-density set of primes ≡ 1 (mod 840),
>   and R is not such an a on primes.
> * T1-compatible Hecke-finite objects see p only through quadratic characters of bounded conductor: congruence menus
>   in disguise (B1).
> * The minorant form is not killed by T1 (explicit examples), but its validity at primes is (MS) itself.
> * Escapes: half-integral weight (squares and primes in different Shimura classes; instantiated, it is the Planck-scale
>   wall), level sums (H-A/B2), non-Hecke-finite objects.
> * Add to §6: "Eisenstein + cusp decomposition with Deligne bounds for any fixed-level integral-weight object or
>   Eisenstein derivative".

**Bottom line.** The brief asked whether a modular, mock or higher-depth object with a Deligne-strength pointwise
cusp bound could carry (MS). For every object with a GL₂ Hecke recursion, which is where Deligne bounds live, the answer
is a clean **no**. Odd-square vanishing at p², p⁴, … alone forces the coefficient at p to vanish unless Satake
parameters collide in sign, i.e. unless a quadratic character of bounded conductor is −1 at p. That is congruence
information, and it is blind on a positive-density set of 𝔐-primes. This kills the support form of the proxy question,
the exact-identity question, and the Eisenstein-plus-cusp template in that class. It extends the prior size-based
(Thm 2.2) and Eisenstein-only (Thm 9.1, Prop 2.3) no-gos to cusp forms, quasi-modular forms and log-sized Eisenstein
derivatives. The escape hatches it leaves are precise:
* half-integral weight, where a pointwise template exists but, when instantiated by CM objects, needs Planck-scale
  equidistribution;
* objects with no Hecke recursion in n (level sums), which is the old H-A/B2 wall.

Nothing here moves (MS) toward a proof.

## 6. Commands and files
All runs: `ulimit -v 4000000`, `timeout` as shown.
* `timeout 1200 uv run --with sympy python scripts/z58_automorph_lemmaS.py` (ulimit -v 4000000) → `data/z58/automorph/lemmaS_out.txt` (Lemma S / Thm A sanity checks, local sign example).
* `timeout 900 uv run --with sympy python scripts/z58_automorph_classes.py 20001` → `data/z58/automorph/classes_out.txt`
  (local square classes of the known zeros; global check of Prop B1 for odd m ≤ 20 001).

## 7. Review log
(to be filled)

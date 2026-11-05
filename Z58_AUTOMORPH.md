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
* (iii) A real-parameter derivative ∂_s^e|_{s=s₀} of Σ_{d|n} ψ₁(d)ψ₂(n/d) d^{s+u}(n/d)^{−s+v}, with u, v, s₀ real and
  ψ₁, ψ₂ characters mod M. These are the coefficients of s-derivatives of holomorphic or non-holomorphic Eisenstein
  series, including τ(n) and Σ_{d|n} χ(d) log(n/d²).

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

Let F be the fixed field of the kernel of ⊕_i ρ̄_i (mod 𝔪) ⊕ (mod-840 cyclotomic), a finite Galois extension of ℚ.
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
prime p ≡ 1 (4) with p ≥ 7:
* a(1) = 0;
* a(p) = p + 5 − 6 = p − 1 > 0;
* a(p^{2j}) < 0 for j ≥ 1. Checked for p < 60, j ≤ 3; in general 5σ₁(p^{2j}) < 5p^{2j}·p/(p−1) < (2j + 1)·2p^{2j}.

So T1 at the powers of p alone does not force a(p) ≤ 0 in the minorant form. The example fails globally: a(q²) > 0 for
q ≡ 3 (4) (`lemmaS_out.txt`). A global sign theorem would need T1 at products and is left open (§3, to do).

---

## 3. (to do) Sign form Q2′ globally; Eisenstein-dominant minorants (Thm 9.1(b) analogue with cusp forms)
## 4. (to do) Escapes: E1 half-integral weight (Prop C, composite-zero falsifier), E2 level sums, E3 higher depth
## 5. (to do) Verdict, screens, proposed FRONTIER text, bottom line
## 6. Commands and files
* `timeout 1200 uv run --with sympy python scripts/z58_automorph_lemmaS.py` (ulimit -v 4000000) → `data/z58/automorph/lemmaS_out.txt`.
## 7. Review log

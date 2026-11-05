# Z58_TERNARY — the half-integral-weight escape E1: odd squares kill the genus main term of every ternary-theta proxy exactly on the local class of the squares (= 𝔐 at level 840); what is left is a pure cusp / Waldspurger problem

Status: z58 follow-up lane TERNARY (brief `z52bbriefs/z58_lanes.md` §TERNARY; common rules `z52bbriefs/z53_depth.md`).
Internal; internally reviewed only (§8). **ES is OPEN; nothing here proves or disproves ES, (★), or (MS).**
Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment.
Scripts `scripts/z58_ternary_*`, data `data/z58/ternary/` (< 100 kB). Read: `Z58_AUTOMORPH.md` (Thm A, §4 E1, Prop C),
`POINTWISE_TERNARY.md` (Thm 4.1, Cor 3.2, (Q_d)), `Z57_SYNTH.md` §§0–2, `Z58_LADDER.md` (L2^𝔐 census to 10¹¹),
`Z58_LOGIC.md` (zero census to 10¹⁰), `Z58_WILDCARD.md`, `METAPLECTIC_ES.md` Thm K, `Z53_WILDCARD.md` row 6,
`BRAINSTORM/bsB_theta_multiplier.md`; `git grep` Duke / spinor / ternary / Hurwitz. Literature checks:
`data/z58/ternary/lit_verify.md`.

**Verdict: narrowed** (a scoped no-go, unconditional where AUTOMORPH's was conditional, plus a named escape). No HOT LEAD.

---

## 0. MANDATORY FALSIFIER TABLE

Mechanism examined: a *quadratic-form / half-integral-weight proxy* — g = Σ cᵢ θ_{Lᵢ} + (cusp form) with Lᵢ positive
ternary lattices, or a class-group / Heegner count — whose non-vanishing at p is to force a (★) or Type II
certificate, made pointwise by the Duke–Iwaniec template (Eisenstein part ≫ p^{1/2−ε} beats cusp part
≪ p^{1/2−1/28+ε}).

| screen | behaviour |
|---|---|
| **F1 odd squares** | AUTOMORPH noted that squares and primes decouple through Hecke structure in half-integral weight, so F1 "does not bind the same way". **Theorem F (§3, PROVED rel. cited inputs) refines this: F1 binds through the genus (Eisenstein) part.** If g(ℓ²) = 0 for all large primes ℓ (which T1 forces on a valid proxy), the genus part of g vanishes identically on the joint *unit* local class 𝒞₁(2N) of the squares. At level 4N = 840 this class is, mod 840, *exactly* 𝔐 (Cor F1: 𝔐 = the squares of (ℤ/840)^×). So non-squareness is used at the Siegel local-density step; after it, the genus main term can survive (at primes p ∤ 2N) only on unit non-square classes — classes not excluded by the Mordell–Schinzel square obstruction (which is not the same as having a known identity). |
| **F2 C-even sub-line** | The proxies see C only through discriminants −4Cp and 2-adic data; nothing examined separates C odd from C even. Theorem F is negative and line-blind, so it proves nothing false; no positive statement is made. |
| **F3 composites** | Not needed by Theorem F (which, in the ternary-theta class, replaces AUTOMORPH Prop C's conclusion on the square class without (H_E) or composite data). Finite data (§5, n ≡ 1 (4), n ≤ 10¹⁰): 17 Shimura-orbit zeros t·m² (t prime), only one with m coprime to 105, none with m coprime to 1155; *non-square* composite zeros coprime to 105 end at 29 210 401; in 𝔐 at 17 401 609 (LADDER, to 10¹¹). Every non-square composite zero in (3·10⁷, 10¹⁰] has a factor 3, 5 or 7 (EVIDENCE, finite range). In this range composites constrain an E1 proxy only through 3, 5, 7; no asymptotic claim. |
| **F4 known zeros** | Nothing is proved positive. In the pure-cusp regime left by Thm F, a valid single-eigenform proxy whose Waldspurger local factor is non-zero on the class must vanish at the in-𝔐 (★)-zeros, i.e. L(½, F ⊗ ψ̄χ_{−4p}) = 0 there. Screen (§4.2, ψ = 1, EVIDENCE): for 15 distinct L-functions of conductor supported on {2,3,5,7}, the twists either have root number −1 on the class (proxy ineffective) or numerically non-vanishing central value at ≥ 2 of the 4 smallest in-𝔐 zeros (proxy invalid or, if its local factor vanishes, ineffective). |

---

## 1. Precise statements attacked

R(n) = #{(u,B,C) ∈ ℕ³ : 4uBC − u − B = n}; N_II(n) = #{(a,b,c,d) ∈ ℕ⁴ : 4abcd = a + b + nc} (Type II; (★) is c = 1).
𝔐 = {1, 121, 169, 289, 361, 529} ⊂ ℤ/840.

**Q-T (construction).** Is there a lattice family / class-group or Heegner count G(p) of power size such that
G(p) ≠ 0 ⟹ R(p) ≥ 1 (or N_II(p) ≥ 1) for primes p ∈ 𝔐, and G(p) ≠ 0 follows (even ineffectively) from
Duke–Schulze-Pillot / Iwaniec / Siegel?

**Q-N (scoped no-go).** Show in a precise class that representation by forms cannot force the tied divisor event
d ≡ −1 (mod 4C), and name the escape.

**Prior closures (not redone).** `POINTWISE_TERNARY` Thm 4.1 / paper `thm:ternary`: *bounded-complexity recipes*
v ↦ ES solution from a fixed lattice use ≪ f(p)p^{(k−2)/2−1/4+ε} representations outside Mordell-type classes.
`Z58_AUTOMORPH` Thm A: integral-weight proxies killed by T1 at p, p², p⁴; E1 left open; Prop C CONDITIONAL on (H_E)
and on infinitely many composite zeros per local class. `bsB_theta_multiplier`: the T1 sign is the weight-½ theta
multiplier; zeros of a Type I count do not propagate along Shimura orbits.

**New here.** (i) Theorem F: F1 alone (no (H_E), no composite data) kills the genus main term of any ternary-theta
proxy (one scalar nebentypus) on the unit local class of the squares; Cor F1 identifies that class with 𝔐 at level
840. This refines AUTOMORPH's E1 discussion (Hecke decoupling of squares and primes stays true; the genus part does not
decouple). (ii) The regime split of E1 (§4): the genus part survives only on unit non-square classes; the pure-cusp
regime is a Waldspurger / Goldfeld-type non-vanishing problem; prime-only validity needs a recipe of a kind not
covered by representation theorems (thin sets, growing families, other encodings). (iii) Dictionary (§2) with the
explicit Planck-scale hypercycle. (iv) Orbit/coprime zero data (§5).

## 2. Dictionary (PROVED, elementary; brute-force CERTIFIED for n ≤ 150)

**Lemma D.** Let n ≥ 1.
(a) Type II solutions (a,b,c,d) are in bijection with triples (C, a, f) of positive integers with
    f ≡ −1 (mod 4aC) and f | n + 4Ca², via C = d, f = 4acd − 1, c = (f+1)/(4aC), b = (nc + a)/f.
    (★) is the sub-case f = 4aC − 1 (c = 1).
(b) Equivalently, with β := 2aC: integral binary forms [f, 2β, g] = fx² + 2βxy + gy² with C ≥ 1, β > 0, f > 0,
    fg − β² = Cn, 2C | β, 2β | f + 1 (then a = β/(2C), c = (f+1)/(2β)). (★) ⟺ 2β = f + 1. (The sign conditions
    matter: C = 1, n = 2, β = −2, f = 3, g = 2 satisfies the rest with a = c = −1; internal review.)
(c) (Heegner reading.) Put z = (−β + i√(Cn))/f, the root of the form. The condition f + 1 = 2βc is equivalent to
    Re z + 1/(2c) = −Im z/(2c√(Cn)), i.e. z lies on the Euclidean ray from −1/(2c) making angle θ with the vertical,
    tan θ = 1/(2c√(Cn)): a hypercycle of the geodesic Re z = −1/(2c) at hyperbolic distance arsinh(1/(2c√(Cn)))
    ~ 1/(c√|disc|) (disc = −4Cn); Planck scale |disc|^{−1/2} for bounded c, smaller for growing c. Certificates are
    *exact incidences* of this specific representative z ∈ ℍ (not of its SL₂(ℤ)-class) with an explicit
    hypercycle — a measure-zero condition.
(d) (Norm form of T1.) For n = m²: 4Cm² + 1 = N_{ℚ(√−C)/ℚ}(1 + 2m√−C). Every prime q | 4Cm²+1 has q ∤ 4C and
    (−C/q) = 1, hence χ_{−4C}(q) = 1; so every divisor lies in ker χ_{−4C} ∌ −1 (χ_{−4C} is odd), and no divisor is
    ≡ −1 (mod 4C). For n = p prime, p ≡ 1 (4): 4Cp + 1 = N(1 + 2√(−Cp)) is a norm from ℚ(√−Cp) only; a certificate
    divisor d satisfies (p/d) = −1 = (d/p), i.e. the form [d, 2, (4Cp+1)/d] — of discriminant −16Cp, not the −4Cp of
    (b)–(c) — lies in the genus with χ_p = −1.

*Proof.* (a) 4abcd = a + b + nc ⟺ b(4acd − 1) = a + nc. Put f = 4acd − 1. Since 4ad·c ≡ 1 (mod f), multiplying
a + nc ≡ 0 by 4ad (a unit mod f) gives f | 4a²d + n; conversely f | n + 4a²d and f ≡ −1 (mod 4ad) give c := (f+1)/(4ad) ∈ ℕ
and f | 4ad(a + nc) hence f | a + nc, b := (a+nc)/f ≥ 1. The maps are mutually inverse. (b) Multiply n + 4Ca² by C:
fg = Cn + 4C²a² = Cn + β² with g := C(n + 4Ca²)/f ∈ ℤ; and 2β = 4aC. Conversely, given β > 0 with 2C | β put
a := β/(2C) ≥ 1; f ≡ −1 (mod 2β) gives gcd(f, C) = 1, so f | C(n + 4Ca²) implies f | n + 4Ca², and f ≡ −1 (mod 4aC);
c = (f+1)/(2β) ≥ 1 since f > 0. (c) Re z = −β/f,
Im z = √(Cn)/f; −β/f + 1/(2c) = (f − 2βc)/(2cf) = −1/(2cf) = −Im z/(2c√(Cn)). Euclidean rays through a boundary
point x₀ are hypercycles of the vertical geodesic at x₀, at distance arsinh(tan θ). (d) Standard: q | x² + Cy² with
q ∤ 2Cy ⟹ (−C/q) = 1; multiplicativity of χ_{−4C}. For primes: −4Cp ≡ 1 (mod d) gives (−Cp/d) = 1; for
d ≡ −1 (mod 4C), (−C/d) = −1 (FAMTRY Lemma 1.4 / SYNTH Lemma A.1), so (p/d) = −1 = (d/p). ∎

(a)–(b) are `POINTWISE_TERNARY`'s (Q_d) (n = ef − 4da², 4ad | f + 1) in form language; (c)–(d) make the paper's
"Planck-scale shrinking target" and T1 explicit. Check: `scripts/z58_ternary_dict_check.py 150` → three independent
counts agree for every n ≤ 150 (`data/z58/ternary/dict_check.txt`).

*Consequence (Assessment, made precise in §3–4).* Representation numbers and equidistribution theorems measure
Heegner points / lattice points in sets of positive measure (fixed regions, congruence and genus conditions). A
certificate is a measure-zero incidence (c). The only "positive-measure" piece of the certificate condition is the
genus condition (d), and that is exactly what T1 and Theorem F act on.

## 3. Theorem F — odd squares kill the genus main term on the local class of the squares

**Setting.** N ≥ 1; ψ a character mod 4N; g ∈ M_{3/2}(Γ₀(4N), ψ) of the form g = Σᵢ cᵢ θ_{Lᵢ} + h, with Lᵢ positive
definite ternary ℤ-lattices whose theta series lie in this space (so the level of each Lᵢ divides 4N),
h ∈ S_{3/2}(Γ₀(4N), ψ), and
(H_δ) det Lᵢ / det Lⱼ ∈ ℚ^{×2} for all i, j (Remark F3: automatic for one scalar nebentypus).
E := Σ cᵢ θ_{gen Lᵢ} (Siegel genus averages). 𝒞₁(2N) := {n ≥ 1 : n ∈ (ℤ_ℓ^×)² for every prime ℓ | 2N}
(n ≡ 1 mod 8 and n a non-zero square mod each odd ℓ | N).

**Inputs** (verification status in `data/z58/ternary/lit_verify.md`):
* (S1) Siegel's formula: r_gen(L, n) = α_∞(L, n)∏_ℓ α_ℓ(L, n) for n ≥ 1 (ternary positive definite), with
  α_∞ = c₃√n/√det L. Local densities depend only on the ℤ_ℓ-isometry class of L ⊗ ℤ_ℓ and satisfy α_ℓ(L, nu²) =
  α_ℓ(L, n) for u ∈ ℤ_ℓ^× (x ↦ ux is a bijection). Unimodular ℤ_ℓ-lattices (ℓ odd) are classified by rank and
  determinant mod squares (O'Meara 92:2). For ℓ ∤ 2N, Lᵢ ⊗ ℤ_ℓ is unimodular (level | 4N). At such ℓ, with
  ε₀ := (−det L/ℓ): α_ℓ(L, 1) = 1 + ε₀/ℓ and α_ℓ(L, ℓ²) = 1 − ℓ^{−2} + ℓ^{−1}α_ℓ(L, 1) (standard unimodular ternary
  densities; supplied by the internal review; consistent with the numerics of (S4)).
* (S2) θ_L − θ_{gen L} ∈ S_{3/2}(Γ₀(4N), ψ) (Siegel–Weil: the genus theta is the Eisenstein projection).
* (S3) S_{3/2} = U ⊕ U^⊥, U spanned by a fixed linearly independent basis of unary theta series
  h_{χ,t} = Σ_{m∈ℤ} χ(m) m q^{tm²} with χ odd *primitive* and the usual admissibility 4t·cond(χ)² | 4N (imprimitive
  series are first rewritten through old unary series h_{χ,tk²}); U, U^⊥ are stable under T(ℓ²), ℓ ∤ 4N, and U^⊥ has a
  basis of simultaneous T(ℓ²)-eigenforms (commuting normal operators).
* (S4) Shimura's T(ℓ²) on weight 3/2 (Shimura 1973 Thm 1.7): (T(ℓ²)f)(n) = a(ℓ²n) + ψ(ℓ)(−n/ℓ)a(n) + ψ(ℓ²)ℓ a(n/ℓ²).
  Used only for the cusp part. For the genus part we use (S1) directly: E(ℓ²) = (1 + ℓ − ε₀(ℓ))E(1) (Step 2).
  Numerical sanity check of this identity on 15 diagonal forms with r(1) ≠ 0: r(ℓ²) = r(1)(1 + ℓ − (−det/ℓ)) for all
  primes ℓ ∤ 2·det with ℓ² ≤ 4·10⁴ (`thmF_check.txt` part 1; the 16th row (2,3,3) has r(1) = 0 and is ineligible, printed
  as FAIL only because the script divides by r(1)). These are coefficient identities, not full eigenform tests.
* (S5) For a simultaneous good-prime eigenform h ∈ U^⊥ with h(1) ≠ 0, the Shimura lift Sh₁h is a non-zero cusp form in
  S₂(Γ₀(2N), ψ²) intertwining the good Hecke operators (Shimura 1973; Niwa 1975 for orthogonality to unary thetas in
  weight 3/2 — secondary source Darreye arXiv:2007.06224 §2, read, stated there for complete eigenforms); decomposing
  it into newforms, Deligne / Eichler–Shimura give |λ_h(ℓ)| ≤ 2√ℓ for good ℓ.

**Theorem F (PROVED relative to (S1)–(S5)).** If g(ℓ²) = 0 for all sufficiently large primes ℓ, then
(i) E(n) = 0 for every n ∈ 𝒞₁(2N);
(ii) the coefficients of the basis series h_{χ,1} (t = 1) in g vanish;
(iii) for every prime p ∈ 𝒞₁(2N) with p ∤ N: g(p) = h⊥(p), where h⊥ ∈ U^⊥ is the component of g − E orthogonal to all
     unary theta series.

*Proof.* **Step 1 (E on 𝒞₁ is a positive multiple of E(1)).** Fix ℓ ∤ 2N. All Lᵢ ⊗ ℤ_ℓ are unimodular ternary with
determinants in one square class (H_δ), hence isometric (S1); so α_ℓ(Lᵢ, n) = α_ℓ(L₁, n) for all i, n. Put
B(n) := √n ∏_{ℓ∤2N} α_ℓ(L₁, n) and κᵢ := c₃/√det Lᵢ. By (S1),
E(n) = B(n) Σᵢ cᵢκᵢ ∏_{ℓ|2N} α_ℓ(Lᵢ, n). For n ∈ 𝒞₁(2N) and ℓ | 2N, n = u² with u ∈ ℤ_ℓ^×, so
α_ℓ(Lᵢ, n) = α_ℓ(Lᵢ, 1). Hence E(n) = B(n)·A with A := Σᵢ cᵢκᵢ∏_{ℓ|2N} α_ℓ(Lᵢ, 1), the same A for every n ∈ 𝒞₁ (n = 1
included). B(1) > 0: at good ℓ, α_ℓ(L₁, 1) = 1 + ε₀(ℓ)/ℓ with ε₀ = (−det L₁/·) a non-principal character (−det < 0
is not a square), so the product is a positive multiple of L(1, χ)/ζ(2) with finitely many factors removed. Hence
E(1) = 0 ⟺ A = 0 ⟹ E ≡ 0 on 𝒞₁ (the cᵢ may have any signs; some bad densities may vanish).
**Step 2 (coefficients at ℓ²).** By (S2), (S3), g = E + Σ_{(ψ',t)} κ_{ψ',t} h_{ψ',t} + Σⱼ hⱼ with hⱼ ∈ U^⊥
T(ℓ²)-eigenforms. Let ℓ ∤ 2N be prime. *Genus part:* ℓ² is a unit square at every q ≠ ℓ (bad or good), so by (S1)
only the density at ℓ and the archimedean factor change: E(ℓ²) = E(1)·ℓ·α_ℓ(ℓ²)/α_ℓ(1) = E(1)(1 + ℓ − ε₀(ℓ)) by the
unimodular densities of (S1) (check: (ℓ + 1 − ε₀)(ℓ + ε₀) = ℓ² + ℓ − 1 + ε₀). *Cusp part:* (S4) at n = 1 (a(1/ℓ²) = 0)
gives hⱼ(ℓ²) = (λⱼ(ℓ) − ε(ℓ))hⱼ(1), ε(ℓ) := ψ(ℓ)(−1/ℓ), |ε| ≤ 1, |λⱼ(ℓ)| ≤ 2√ℓ by (S5) (if hⱼ(1) = 0 the
term vanishes). *Unary part:* an admissible h_{χ,t} has a non-zero coefficient at ℓ² only if t·m² = ℓ² with t | N,
ℓ ∤ N, i.e. t = 1, m = ±ℓ, giving 2χ(ℓ)ℓ (χ odd). Hence
  g(ℓ²) = ℓ·[E(1) + 2Σ_{χ} κ_{χ,1} χ(ℓ)] + O_g(√ℓ).
**Step 3.** Let M = 4N. For each a ∈ (ℤ/M)^×, let ℓ → ∞ through primes ≡ a (mod M) (Dirichlet). The
hypothesis forces Φ(a) := E(1) + 2Σ_χ κ_{χ,1}χ(a) = 0 for all a. Averaging over a kills every χ (each is odd, hence
non-trivial mod M): E(1) = 0. Then Σ_χ κ_{χ,1}χ(a) = 0 for all a; the basis characters χ are distinct primitive
characters, which induce distinct characters mod M, so linear independence of characters gives κ_{χ,1} = 0: (ii).
(With an overcomplete, imprimitive family only the sums over series inducing the same character mod M vanish — e.g.
h_{χ,1} − h_{χ̃,1} = −3h_{χ,9} for χ mod 4, χ̃ its lift mod 12; internal review.) Step 1 gives (i).
**(iii).** For a prime p ∈ 𝒞₁ with p ∤ N: E(p) = 0 by (i); a unary series has p = tm² only with t = p, m = 1, impossible
as t | N; so g(p) = Σⱼhⱼ(p) = h⊥(p). ∎

**Remark F1 (sufficiency of the hypothesis).** A valid support proxy (g(n) ≠ 0 ⟹ R(n) ≥ 1) has g(ℓ²) = 0 for every
odd prime ℓ by T1 (R(m²) = 0 for all odd m). Only the squares of primes are used, and only asymptotically.

**Corollary F1 (𝔐 is the square class; PROVED).** The squares of (ℤ/840)^× are exactly 𝔐 (direct computation:
{1}·{1}·{1,4}·{1,2,4} has 6 elements, listed by `python3 -c` in §7). Hence for every N whose odd prime divisors lie in
{3, 5, 7}, 𝒞₁(2N) ⊇ {n : n mod 840 ∈ 𝔐}, with equality when 105 | N. So **every valid ternary-theta proxy of such a
level has no genus main term at any 𝔐-prime: g(p) = h⊥(p) for all p ∈ 𝔐, p ∤ N**. For general N the same holds at
every 𝔐-prime p that is a quadratic residue modulo every odd prime ℓ | N — in particular whenever the least quadratic
non-residue n_p exceeds the largest prime factor of N (the primes that WITNESS identifies as hardest, d_min ≥ n_p).

**Remark F2 (where the main term survives).** Restrict to n prime to 2N. By Step 1 applied to each joint *unit* square
class 𝒞 (a fixed class in ℤ_ℓ^×/ℤ_ℓ^{×2} for each ℓ | 2N), E is a constant multiple of B(n) on 𝒞. (For n not prime to
2N this fails: x²+y²+z² at level 12 has E(9)/E(1) = 5 ≠ B(9)/B(1) = 3, the density at 3 changes — internal review.)
After Theorem F the genus main term can be non-zero, at primes p ∤ 2N, only on classes 𝒞 ≠ 𝒞₁: p ≢ 1 (mod 8) or p a
non-residue modulo some odd ℓ | N. On the square class, fixed-modulus polynomial identities are excluded
(Mordell–Schinzel; `POINTWISE_TERNARY` Cor 3.2); on the other classes they are *not excluded* — which is not the same
as known to exist. Assessment: in half-integral weight, the Duke template's main term survives F1 only on classes that
the square obstruction leaves open to congruence coverings.

**Remark F3 (on (H_δ)).** If all θ_{Lᵢ} lie in one space M_{3/2}(Γ₀(4N), ψ), the theta transformation law identifies
the quadratic nebentypus of θ_{Lᵢ} with the character of det Lᵢ (up to a convention-dependent factor common to all i),
so (det Lᵢ/ℓ) is independent of i for all good ℓ and det Lᵢ/det Lⱼ is a rational square. (Comparing ε at n = 1 is not
enough when θ_{gen L}(1) = 0, e.g. (2,3,3); internal review.) Finite sanity check of Step 1: for 32 pairs of diagonal
forms with det in one square class, r_L(n)r_{L'}(1) = r_{L'}(n)r_L(1) for every n ≤ 4·10⁴ in 𝒞₁ (`thmF_check.txt`
part 2, 0 violations). These use individual theta series, not computed genus averages, and no class-number data are
certified, so this is a sanity check consistent with (S1), not a verification of it. Sums across different nebentypus
characters are modular on Γ₁ of a common level but are not in the fixed scalar-nebentypus Γ₀ space of the theorem;
for them Steps 2–3 give only Σ_δ E_δ(1) = 0 (gap, §4.4).

**What Theorem F does not cover.** Weight 3/2 forms whose Eisenstein part is not a combination of genus thetas (e.g.
Eisenstein series with odd-character data or the non-holomorphic Zagier series, whose holomorphic part Σ H(n)qⁿ is
mock modular); higher half-integral weights k/2 ≥ 5/2 (theta series of odd-rank lattices of rank ≥ 5; quaternary
lattices give integral weight 2, covered by AUTOMORPH Thm A); and support conditions imposed on residue classes of the
representing vectors (theta series with characteristics). Assessment: the proof uses only "genus part = local densities
× common Euler product" and "cusp eigenvalues ≪ ℓ^{1/2+ε} relative to the main term", so it may extend; not claimed.

## 4. What is left of E1: three regimes

Let g be a proxy as in §3 (ternary thetas plus cusp forms, one scalar nebentypus) and p ∈ 𝔐 a large prime, p ∤ 2N.
Non-genus Eisenstein components are outside this discussion (§4.4).

### 4.1 Eisenstein-carrying regime (Assessment + PROVED pieces)
Possible only off 𝒞₁ (Remark F2). For level 4N with odd prime support in {3,5,7} that is off 𝔐 (Mordell's
identities cover those primes). For larger levels it is the set of 𝔐-primes that are non-residues modulo some ℓ | N;
on it a valid
Eisenstein-carrying proxy would be effective (Duke–Iwaniec, ineffective constants) and validity there *is* (MS)
restricted to that set. **Shimura propagation (PROVED rel. (S1)–(S5), as in Step 2 with n = p):** for a fixed prime
p ∤ 2N and good primes ℓ ≠ p, E(pℓ²) = (1 + ℓ − (−p·det L₁/ℓ))E(p) (only the density at ℓ changes), the cusp part
is O_p(√ℓ) and no unary series is supported on p·□; so if E(p) ≠ 0 and g is valid on all n ≡ 1 (4), then
g(pℓ²) = ℓE(p)(1 + o(1)) ≠ 0 for all large primes ℓ, and validity also forces R(pℓ²) ≥ 1 for all those ℓ: an E1 proof of (MS) via an all-n-valid proxy would prove positivity on infinitely many
composite orbits. Orbit zeros R(t·m²) = 0 with t prime exist (17 ≤ 10¹⁰, §5) but none with m coprime to 1155, so this is
a consequence, not a refutation.

### 4.2 Pure-cusp regime (the regime Theorem F forces on 𝒞₁ ⊇ 𝔐)
g(p) = h⊥(p) = Σⱼ hⱼ(p) — a *sum* of eigenform coefficients; the following concerns a single eigenform h. Waldspurger's
theorem (Waldspurger 1981, cited, not re-read) gives h(t)² = C_h(t)·t^{1/2}·L(½, F ⊗ ψ̄χ_{−t}) for squarefree t, where
F = Sh(h), ψ is the nebentypus and C_h(t) is a local factor depending on t only through its classes at the primes
dividing 4N (the form in which Darreye arXiv:2007.06224 §2 states it is for N odd and complete eigenforms; level 840 has
N = 210 even, so we take the local-class dependence as hypothesis **(W-loc)**). The Kohnen–Zagier plus-space formula
(Thm 1, read) does not apply: the plus space vanishes at n ≡ 1 (mod 4). For p ∈ 𝔐 and ψ = 1 the twist is χ_{−4p}. Under
(W-loc), C_h is constant on each 𝔐 class, and there are two cases:
* C_h = 0 on the class: h vanishes there — trivially valid, ineffective;
* C_h ≠ 0: *effectiveness* on the class = non-vanishing of L(½, F ⊗ ψ̄χ_{−4p}) for **all** large p in the class. When the twisted root number is −1 on the class this fails identically; when it is +1 it is an
  open Goldfeld-type problem (only positive-proportion results are known: Ono–Skinner 1998, Kriz–Li 2019; no result
  for all large primes in a progression — literature status, `lit_verify.md` §6);
  *Validity* (still with C_h ≠ 0) requires L(½, F ⊗ ψ̄χ_{−4p}) = 0 at the in-𝔐 (★)-zeros of the class.
* sizes: |h(p)| ≪ p^{1/2−1/28+ε} (Iwaniec 1987 / Duke 1988, cited), against R(p) ≍ log²p on average — no contradiction
  either way; the cusp coefficient carries no main term to beat.

**Screen (EVIDENCE, ψ = 1 only; `scripts/z58_ternary_waldspurger.py`, `data/z58/ternary/waldspurger_screen.txt`).** 16
Weierstrass models = 15 distinct L-functions (elliptic curves of conductor 14, 15, 20, 21, 24, 27, 30, 32 (two
isogenous models), 35, 36, 42, 45, 48, 56, 63 — conductor supported on {2,3,5,7}; a sample, not an enumeration of all
newforms of these levels; Shimura preimages would have level 4N with N | 2^a3^b5^c7^d, existence not checked), twist
χ_{−4p}, at the 4 in-𝔐 zeros ≤ 4·10⁵ (5569, 9601, 83449, 102001) and 8 controls in the same classes:
* the root number is constant on each tested class, as it must be: twisting first by −4 and then by p, with p ≡ 1 (8) a
  residue at 3, 5, 7, leaves the root number of E^{(−4)} unchanged (the formula χ_{−4p}(−N_F) is not valid for even N_F);
* conductors 21 and 45: root number −1 throughout ⟹ such a proxy vanishes on the class (ineffective);
* the other 14 rows: root number +1 and numerical analytic rank 0 (pari `ellanalyticrank`, default precision; not a
  certified non-vanishing) at ≥ 2 of the 4 zeros ⟹ under (W-loc) such a proxy is invalid (C_h ≠ 0) or ineffective
  (C_h = 0);
* rank-2 twists occur at zeros and controls alike: 11/56 vs 14/112 row-weighted, 9/52 vs 14/104 after removing the
  duplicate conductor-32 row; a small and correlated sample, no statistical conclusion.
* Conclusion (EVIDENCE): none of the 15 tested L-functions supports a simultaneously valid and effective
  single-eigenform proxy under (W-loc) with ψ = 1. Linear combinations of eigenforms are not excluded by this
  single-form screen (fitting the zero constraints is a separate linear-algebra problem), and a proxy only required to
  be valid above all screened primes is not constrained at all. Nothing here suggests a structural reason for
  validity.

### 4.3 Prime-only validity (the named escape)
A proxy only required to satisfy g(p) ≠ 0 ⟹ R(p) ≥ 1 *at primes* escapes Theorem F (it need not vanish at ℓ²) — but then
modularity supplies no reason for validity: on any class where g(p) ≠ 0 for all large p (e.g. Eisenstein-carrying),
validity is literally (MS) on that class. A reason must come from a *recipe* turning representations/Heegner points
into certificates using primality. `POINTWISE_TERNARY` Thm 4.1 / Cor 4.2 (one fixed embedding of bounded complexity):
outside Mordell-type classes a nondegenerate recipe uses ≪ f(p)p^{1/4+ε} of the ≍ p^{1/2±ε} representations, so it
cannot be fed by a positive-density representation theorem. That does **not** exclude bounded-complexity recipes on
thin admissible sets (POINTWISE gives an explicit example after Cor 4.2); it excludes certifying them by
representation/equidistribution theorems. Lemma D(c) is the reason in the (★)/Type II case: the certificate condition
is an exact incidence of a representative with a hypercycle, a measure-zero condition.

**The escapes E1′ (named; alternatives, not a proved classification).**
* (a) bounded-complexity recipes plus a *new theorem about thin admissible sets* — for the dictionary of Lemma D, an
  incidence theorem for Heegner points of discriminant −4Cp on the explicit hypercycles of Lemma D(c) (scale
  1/(c√|D|)); equidistribution currently reaches shrinking targets of size ≥ |D|^{−1/24} (Young), |D|^{−1/8} under
  Lindelöf (AUTOMORPH §4 E1);
* (b) recipes of growing complexity or families with a parameter growing with p (gcds, factorisations);
* (c) encodings outside the fixed-embedding setup (p entering only through side conditions, H5 of POINTWISE).
Lemma D(c) is an exact encoding of the certificate condition, not a proved equivalence of these escapes. The F3 data
suggest (EVIDENCE, finite range) that none of them would need primality beyond non-squareness and gcd(n, 105) = 1 (§5).
Assessment: this is the old B2 / H-A wall seen from half-integral weight.

### 4.4 Gaps (honest list)
* Mixed-nebentypus combinations (modular on Γ₁, outside the fixed-ψ Γ₀ space of Thm F) and non-genus Eisenstein
  series: only Σ_δ E_δ(1) = 0 follows.
* (W-loc) and the general-level Waldspurger statement are cited, not verified from the primary source; the screen
  covers ψ = 1 only.
* Theorem F is about *support* proxies valid at squares; a signed minorant (AUTOMORPH Q2′) is not addressed.
* Higher half-integral weight, theta series with characteristics, mock (Zagier-type) objects: expected to behave the
  same (Assessment), not proved.

## 5. Data (EVIDENCE / CERTIFIED arithmetic on the LOGIC census)

`scripts/z58_ternary_orbit.py` → `orbit_zeros.txt`; `scripts/z58_ternary_coprime.py` → `coprime_zeros.txt` (input:
`data/z58/logic/zeros_1e10.txt.gz`, all n ≡ 1 (4), 5 ≤ n ≤ 10¹⁰, with R(n) = 0; LOGIC, CERTIFIED there).
* 486 non-square composite zeros ≤ 10¹⁰ (largest 9 919 520 121); 244 have a square factor.
* **Shimura-orbit zeros** n = t·m², t prime, m > 1: 17 (801 = 3²·89, 12 681 = 3²·1409, 23 425 = 5²·937, …,
  71 724 681 = 21²·162641); m ∈ {3, 5, 7, 9, 11, 21}. With m coprime to 3: 4; to 15: 2; to 105: 1 (752 257 = 11²·6217);
  to 1155: 0.
* Non-square composite zeros coprime to 105: 24, the last 29 210 401 = 11·31·85661 (decades 10³…10⁷: 4, 5, 9, 3, 3); coprime to 15:
  44, last 7 479 950 569; coprime to 1155: 16, last 17 401 609. LADDER: in 𝔐 none in (17 401 609, 10¹¹].
* Non-square composite zeros per decimal exponent 1…9: 1, 8, 24, 60, 95, 111, 93, 52, 42 (52 in [10⁸,10⁹), 42 in
  [10⁹,10¹⁰)).
* Reading (EVIDENCE, finite range n ≤ 10¹⁰, n ≡ 1 (4)): the non-square composite zeros persist to 10¹⁰ only through the
  factors 3, 5, 7; away from them they stop near 3·10⁷. In this range non-squareness plus coprimality to 105 is all
  the data ask for, and primality is not visibly needed in 𝔐. No asymptotic statement is claimed.

## 6. Verdict, screens, proposed FRONTIER text, bottom line

**Verdict: narrowed.**
* Q-T: no construction. Q-N: Theorem F (PROVED rel. Siegel / Siegel–Weil / Shimura–Niwa / Deligne) — for every
  weight-3/2 proxy built from ternary theta series plus cusp forms, validity at the squares of primes forces the genus
  main term to vanish on the joint local class of the squares, which at level 840 is exactly 𝔐 (Cor F1; unit classes, primes p ∤ 2N). On 𝔐 the
  Duke template has nothing to work with: what remains is a sum of cusp-eigenform coefficients; for a single eigenform
  (under (W-loc)) non-vanishing at all large primes of a class is an open Goldfeld-type problem (false on root-number
  −1 classes), and for the 15 small-conductor L-functions tested (ψ = 1) no valid-and-effective single-eigenform proxy
  exists (§4.2, EVIDENCE).
* This refines AUTOMORPH's E1 discussion (Hecke decoupling of squares and primes stays true; the genus part does not
  decouple) and, in the ternary-theta class, replaces Prop C's conditional conclusion on the square class by an
  unconditional one.
* Escapes left: E1′ (§4.3) — (a) bounded recipes plus a new thin-set (Planck-scale Heegner incidence) theorem,
  (b) growing-complexity / family recipes, (c) encodings outside fixed embeddings. Assessment: B2/H-A.

**FRONTIER §4 hard screens (Theorem F as the best idea).** T1 squares: it *is* T1, used through local densities at the
squares of primes. 8/131: line-blind (negative statement). Tied modulus: the tied event is the Planck-scale incidence of
Lemma D(c); fixed-level forms cannot see it. Fixed p: statement is pointwise in p after the level is fixed.

**Proposed FRONTIER §6/§7 text (do not edit FRONTIER here).**
> *Half-integral weight (z58 TERNARY, Thm F, PROVED rel. Siegel's formula, Siegel–Weil, Shimura/Niwa lift, Deligne).*
> Let g ∈ M_{3/2}(Γ₀(4N), ψ) be a combination of ternary theta series plus cusp forms. If g(ℓ²) = 0 for all large primes ℓ
> (forced by T1 on any valid support proxy), the genus part of g vanishes on every n that is a unit square at all
> ℓ | 2N, and the t = 1 unary thetas (primitive basis) vanish. The squares of (ℤ/840)^× are exactly Mordell's 𝔐, so at level 840 every
> valid proxy is a pure cusp coefficient at every 𝔐-prime: no main term for Duke–Iwaniec. Its non-vanishing is a
> Goldfeld-type central-value problem (single eigenform, local factor non-zero); for 15 small-conductor L-functions
> no single-eigenform proxy is both valid and effective (EVIDENCE). Remaining escapes: thin-set theorems for
> bounded recipes (Planck-scale Heegner incidences, Lemma D(c)), growing-complexity recipes, other encodings = B2.
> Add to §6: "weight-3/2 / ternary-theta support proxies with a genus main term on Mordell's classes".

**Bottom line.** The brief asked whether half-integral weight — the classical technology for pointwise representation
of a single large integer — can carry (MS). AUTOMORPH left it open because odd squares and primes sit in different
Shimura orbits. They do, but the genus (Eisenstein) part does not care about orbits: by Siegel's formula, on integers
prime to the level it depends on n only through local unit square classes and a common Euler product, so vanishing at the squares of primes kills it on the
whole local class of the squares — and at level 840 that class is exactly Mordell's 𝔐. On the target classes a
ternary-form proxy is therefore a pure cusp coefficient, with no main term to beat the cusp error; for a single eigenform, making it
non-zero at every large prime is a Goldfeld-type problem, and none of the small-conductor eigenforms tested gives a
proxy that is both valid at the known zeros and effective. Certificates themselves are Planck-scale incidences of Heegner points with explicit hypercycles, a measure-zero
condition that representation and equidistribution theorems (positive-measure statements) do not see. Nothing here moves (MS); the wall is B2 again, now with a sharp
half-integral-weight description.

## 7. Commands and files
All runs under `ulimit -v 4000000` and `timeout` ≤ 1500.
* `uv run --with sympy python scripts/z58_ternary_orbit.py > data/z58/ternary/orbit_zeros.txt`
* `uv run --with sympy python scripts/z58_ternary_coprime.py > data/z58/ternary/coprime_zeros.txt`
* `uv run python scripts/z58_ternary_thmF_check.py 40000 > data/z58/ternary/thmF_check.txt` (inputs (S1), (S4))
* `uv run python scripts/z58_ternary_dict_check.py 150 > data/z58/ternary/dict_check.txt` (Lemma D)
* `uv run --with cypari2 python scripts/z58_ternary_waldspurger.py 400000 > data/z58/ternary/waldspurger_screen.txt`
* Cor F1: `python3 -c "print(sorted({x*x%840 for x in range(840) if all(x%q for q in (2,3,5,7))}))"` → [1, 121, 169, 289, 361, 529].
* Literature: `data/z58/ternary/lit_verify.md` (research subagent + lane note §8).

## 8. Review log
* **Internal hostile review** (deep-mode subagent, `data/z58/ternary/internal_review.md`): no FATAL; 7 MAJOR, 4 MINOR.
  It re-derived Theorem F Steps 1–3 and (iii) (passes in the unit-class setting), supplied the unimodular local
  densities now used in Step 2, and reproduced all five scripts byte-for-byte (incl. the Waldspurger screen). Repairs:
  * M1/M2: Waldspurger twist now ψ̄χ_{−t}; general-level statement cited with hypothesis (W-loc); screen restricted to
    ψ = 1; valid/effective dichotomy via the local factor C_h; numerical ranks labelled non-certified; 15 distinct
    L-functions, not "all newforms".
  * M3: "unbounded complexity is necessary" withdrawn; escapes listed as alternatives (thin-set theorem for bounded
    recipes / growing families / other encodings); Lemma D(c) is an encoding, not an equivalence.
  * M4: Remark F2 restricted to integers prime to 2N and unit square classes (counterexample E(9)/E(1) = 5 ≠ 3 at level 12).
  * M5: Lemma D(b) now requires β > 0 (counterexample with a = c = −1); D(c) scale ~1/(c√|D|), representative-dependent;
    D(d) discriminant −16Cp and p ≡ 1 (4).
  * M6: unary part stated in a primitive admissible basis; overcomplete-family counterexample noted.
  * M7: "non-square" inserted in all composite-zero summaries; finite-range wording.
  * Minors: Remark F3 via the theta transformation law; mixed-nebentypus sums are Γ₁-modular (outside the theorem, not
    "non-modular"); root-number constancy argued via twisting by −4 then p; (S4) checks labelled as coefficient identities
    with the r(1) = 0 row ineligible; decade counts corrected; duplicate-free 9/52 vs 14/104; "finitely many zeros can
    always be fitted" removed; novelty phrased as a refinement of AUTOMORPH; "verbatim" extension and the quaternary
    remark corrected; `dict_check` now exits non-zero on mismatch; literature notes amended (`lit_verify.md` §9).

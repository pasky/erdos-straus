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
| **F1 odd squares** | AUTOMORPH read F1 as not binding in half-integral weight (squares and primes are different Shimura orbits). **Theorem F (§3, PROVED rel. cited inputs): it binds through the Eisenstein part.** If g(ℓ²) = 0 for all large primes ℓ (which T1 forces on a valid proxy), the genus part of g vanishes identically on the joint local class 𝒞₁(2N) of the squares. At level 840 this class is *exactly* 𝔐 (Cor F1: 𝔐 = the squares of (ℤ/840)^×). So the step where non-squareness is used is the Siegel local-density step; after it, the main term exists only on non-square classes — where Mordell-type congruence identities live anyway. |
| **F2 C-even sub-line** | The proxies see C only through discriminants −4Cp and 2-adic data; nothing examined separates C odd from C even. Theorem F is negative and line-blind, so it proves nothing false; no positive statement is made. |
| **F3 composites** | Not needed by Theorem F (which improves AUTOMORPH Prop C: no hypothesis (H_E), no composite data). Data (§5): 17 Shimura-orbit zeros t·m² (t prime) ≤ 10¹⁰, only one with m coprime to 105, none with m coprime to 1155; composite zeros coprime to 105 end at 29 210 401; in 𝔐 at 17 401 609 (LADDER, to 10¹¹). Above 3·10⁷ every composite zero ≤ 10¹⁰ has a factor 3, 5 or 7 (EVIDENCE): composites bind an E1 proxy only through 3, 5, 7, which the level absorbs. |
| **F4 known zeros** | Nothing is proved positive. In the pure-cusp regime left by Thm F, a valid eigen-proxy must vanish at the in-𝔐 (★)-zeros, i.e. L(½, F ⊗ χ_{−4p}) = 0 there (Waldspurger). Screen (§4.2): for 16 weight-2 newforms of level supported on {2,3,5,7}, the twists either have root number −1 on all of 𝔐 (proxy ≡ 0, ineffective) or are non-vanishing at ≥ 2 of the 4 smallest in-𝔐 zeros (proxy invalid). |

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
proxy on the local class of the squares; Cor F1 identifies that class with 𝔐 at level 840. (ii) The regime split of
E1 (§4): Eisenstein survives only on non-square classes; pure-cusp regime = a Waldspurger / Goldfeld-type
non-vanishing problem; prime-only validity needs a recipe of unbounded complexity. (iii) Dictionary (§2) with the
explicit Planck-scale hypercycle. (iv) Orbit/coprime zero data (§5).

## 2. Dictionary (PROVED, elementary; brute-force CERTIFIED for n ≤ 150)

**Lemma D.** Let n ≥ 1.
(a) Type II solutions (a,b,c,d) are in bijection with triples (C, a, f) of positive integers with
    f ≡ −1 (mod 4aC) and f | n + 4Ca², via C = d, f = 4acd − 1, c = (f+1)/(4aC), b = (nc + a)/f.
    (★) is the sub-case f = 4aC − 1 (c = 1).
(b) Equivalently, with β := 2aC: binary forms [f, 2β, g] = fx² + 2βxy + gy² with fg − β² = Cn, 2C | β, 2β | f + 1,
    f > 0 (then c = (f+1)/(2β)). (★) ⟺ 2β = f + 1.
(c) (Heegner reading.) Put z = (−β + i√(Cn))/f, the root of the form. The condition f + 1 = 2βc is equivalent to
    Re z + 1/(2c) = −Im z/(2c√(Cn)), i.e. z lies on the Euclidean ray from −1/(2c) making angle θ with the vertical,
    tan θ = 1/(2c√(Cn)): a hypercycle of the geodesic Re z = −1/(2c) at hyperbolic distance arsinh(1/(2c√(Cn)))
    ≍ |disc|^{−1/2}. Certificates are *exact incidences* of Heegner points of discriminant −4Cn with an explicit
    Planck-scale-displaced hypercycle.
(d) (Norm form of T1.) For n = m²: 4Cm² + 1 = N_{ℚ(√−C)/ℚ}(1 + 2m√−C). Every prime q | 4Cm²+1 has q ∤ 4C and
    (−C/q) = 1, hence χ_{−4C}(q) = 1; so every divisor lies in ker χ_{−4C} ∌ −1 (χ_{−4C} is odd), and no divisor is
    ≡ −1 (mod 4C). For n = p prime, 4Cp + 1 = N(1 + 2√(−Cp)) is a norm from ℚ(√−Cp) only; a certificate divisor d
    satisfies (p/d) = −1, i.e. the form [d, 2, (4Cp+1)/d] lies in the genus with χ_p = −1 (Jacobi reciprocity, p ≡ 1 (4)).

*Proof.* (a) 4abcd = a + b + nc ⟺ b(4acd − 1) = a + nc. Put f = 4acd − 1. Since 4ad·c ≡ 1 (mod f), multiplying
a + nc ≡ 0 by 4ad (a unit mod f) gives f | 4a²d + n; conversely f | n + 4a²d and f ≡ −1 (mod 4ad) give c := (f+1)/(4ad) ∈ ℕ
and f | 4ad(a + nc) hence f | a + nc, b := (a+nc)/f ≥ 1. The maps are mutually inverse. (b) Multiply n + 4Ca² by C:
fg = Cn + 4C²a² = Cn + β² with g := C(n + 4Ca²)/f — integral since gcd(f, C) = 1; and 2β = 4aC. Conversely
fg − β² = Cn with 2C | β, f | ... gives back f | n + 4Ca² (gcd(f, C) = 1 from f ≡ −1 mod 2β). (c) Re z = −β/f,
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
definite ternary ℤ-lattices whose theta series lie in this space, h ∈ S_{3/2}(Γ₀(4N), ψ), and
(H_δ) det Lᵢ / det Lⱼ ∈ ℚ^{×2} for all i, j (see Remark F3: automatic in one space).
E := Σ cᵢ θ_{gen Lᵢ} (Siegel genus averages). 𝒞₁(2N) := {n ≥ 1 : n ∈ (ℤ_ℓ^×)² for every prime ℓ | 2N}
(n ≡ 1 mod 8 and n a non-zero square mod each odd ℓ | N).

**Inputs** (verification status in `data/z58/ternary/lit_verify.md`):
* (S1) Siegel's formula: r_gen(L, n) = α_∞(L, n)∏_ℓ α_ℓ(L, n) for n ≥ 1 (ternary positive definite), with
  α_∞ = c₃√n/√det L. Local densities depend only on the ℤ_ℓ-isometry class of L ⊗ ℤ_ℓ and satisfy α_ℓ(L, nu²) =
  α_ℓ(L, n) for u ∈ ℤ_ℓ^× (x ↦ ux is a bijection). Unimodular ℤ_ℓ-lattices (ℓ odd) are classified by rank and
  determinant mod squares (O'Meara 92:2). For ℓ ∤ 2N, Lᵢ ⊗ ℤ_ℓ is unimodular.
* (S2) θ_L − θ_{gen L} ∈ S_{3/2}(Γ₀(4N), ψ) (Siegel–Weil: the genus theta is the Eisenstein projection).
* (S3) S_{3/2} = U ⊕ U^⊥, U spanned by unary theta series h_{ψ',t} = Σ_{m∈ℤ} ψ'(m) m q^{tm²} (ψ' odd, t | N); U, U^⊥
  are stable under T(ℓ²), ℓ ∤ 4N, and U^⊥ has a basis of simultaneous T(ℓ²)-eigenforms (commuting normal operators).
* (S4) Shimura's T(ℓ²) on weight 3/2 (Shimura 1973 Thm 1.7): (T(ℓ²)f)(n) = a(ℓ²n) + ψ(ℓ)(−n/ℓ)a(n) + ψ(ℓ²)ℓ a(n/ℓ²).
  θ_{gen L} is a T(ℓ²)-eigenform with eigenvalue 1 + ℓ (ℓ ∤ 2N). CERTIFIED numerically for 15 diagonal forms in the form
  r(ℓ²) = r(1)(1 + ℓ − (−det/ℓ)), all primes ℓ ≤ 199 with ℓ² ≤ 4·10⁴ (`thmF_check.txt`, part 1).
* (S5) For an eigenform h ∈ U^⊥ with h(1) ≠ 0, the Shimura lift Sh₁h is a Hecke eigenform in S₂(Γ₀(2N), ψ²) with the
  same eigenvalues (Shimura 1973; Niwa 1975 for orthogonality to unary thetas in weight 3/2 — secondary source
  Darreye arXiv:2007.06224 §2, read), hence |λ_h(ℓ)| ≤ 2√ℓ (Eichler–Shimura / Deligne).

**Theorem F (PROVED relative to (S1)–(S5)).** If g(ℓ²) = 0 for all sufficiently large primes ℓ, then
(i) E(n) = 0 for every n ∈ 𝒞₁(2N);
(ii) the coefficients of the unary theta series h_{ψ',1} in g vanish;
(iii) for every prime p ∈ 𝒞₁(2N) with p ∤ N: g(p) = h⊥(p), where h⊥ ∈ U^⊥ is the component of g − E orthogonal to all
     unary theta series.

*Proof.* **Step 1 (E on 𝒞₁ is a positive multiple of E(1)).** Fix ℓ ∤ 2N. All Lᵢ ⊗ ℤ_ℓ are unimodular ternary with
determinants in one square class (H_δ), hence isometric (S1); so α_ℓ(Lᵢ, n) = α_ℓ(L₁, n) for all i, n. Put
B(n) := √n ∏_{ℓ∤2N} α_ℓ(L₁, n) and κᵢ := c₃/√det Lᵢ. By (S1),
E(n) = B(n) Σᵢ cᵢκᵢ ∏_{ℓ|2N} α_ℓ(Lᵢ, n). For n ∈ 𝒞₁(2N) and ℓ | 2N, n = u² with u ∈ ℤ_ℓ^×, so
α_ℓ(Lᵢ, n) = α_ℓ(Lᵢ, 1). Hence E(n) = B(n)·A with A := Σᵢ cᵢκᵢ∏_{ℓ|2N} α_ℓ(Lᵢ, 1), the same A for every n ∈ 𝒞₁ (n = 1
included). Since B(1) > 0 (a unimodular ternary ℤ_ℓ-lattice, ℓ odd, primitively represents every unit, and the
Euler product converges to a positive value), E(1) = 0 ⟺ A = 0 ⟹ E ≡ 0 on 𝒞₁.
**Step 2 (coefficients at ℓ²).** By (S2), (S3), g = E + Σ_{(ψ',t)} κ_{ψ',t} h_{ψ',t} + Σⱼ hⱼ with hⱼ ∈ U^⊥
T(ℓ²)-eigenforms. Let ℓ ∤ 4N·∏ cond(ψ'). (S4) at n = 1 (where a(1/ℓ²) = 0) gives, for any T(ℓ²)-eigenform with
eigenvalue λ, a(ℓ²) = (λ − ε(ℓ))a(1) with ε(ℓ) := ψ(ℓ)(−1/ℓ) ∈ {±1, ±i, …}, |ε| = 1. Thus E(ℓ²) = (1 + ℓ − ε(ℓ))E(1) and
hⱼ(ℓ²) = (λⱼ(ℓ) − ε(ℓ))hⱼ(1), |λⱼ(ℓ)| ≤ 2√ℓ by (S5) (if hⱼ(1) = 0 the term vanishes). A unary series h_{ψ',t} has a
non-zero coefficient at ℓ² only if t·m² = ℓ² with t | N, ℓ ∤ N, i.e. t = 1, m = ±ℓ, giving 2ψ'(ℓ)ℓ. Hence
  g(ℓ²) = ℓ·[E(1) + 2Σ_{ψ'} κ_{ψ',1} ψ'(ℓ)] + O_g(√ℓ).
**Step 3.** Let M = 4N·lcm cond(ψ'). For each a ∈ (ℤ/M)^×, let ℓ → ∞ through primes ≡ a (mod M) (Dirichlet). The
hypothesis forces Φ(a) := E(1) + 2Σ κ_{ψ',1}ψ'(a) = 0 for all a. Averaging over a kills every ψ' (each is odd, hence
non-trivial): E(1) = 0. Then Σ_{ψ'} κ_{ψ',1}ψ'(a) = 0 for all a, and linear independence of distinct characters
mod M (group the h_{ψ',1} by the character mod M they induce) gives (ii). Step 1 gives (i).
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

**Remark F2 (where the main term survives).** By Step 1 applied to each joint local class 𝒞 (a fixed square class in
ℚ_ℓ^× for each ℓ | 2N), E is a constant multiple of B(n) on 𝒞. After Theorem F the main term can be non-zero only on
classes 𝒞 ≠ 𝒞₁, i.e. at primes that are *non-squares* modulo some ℓ | 2N. Those are exactly the classes where
fixed-modulus polynomial (Mordell–Schinzel-type) identities are not excluded; on square classes they are excluded
(`POINTWISE_TERNARY` Cor 3.2, Mordell–Schinzel). Assessment: in half-integral weight, the Duke template's main term
survives F1 precisely on congruence-covering territory.

**Remark F3 (on (H_δ)).** If all θ_{Lᵢ} lie in one space M_{3/2}(Γ₀(4N), ψ), then by (S4) each θ_{gen Lᵢ} has
ε(ℓ) = ψ(ℓ)(−1/ℓ), while the Siegel density computation gives ε(ℓ) = (−det Lᵢ/ℓ) (CERTIFIED on 15 forms,
`thmF_check.txt` part 1); hence (det Lᵢ/ℓ) is independent of i for all large ℓ, and det Lᵢ/det Lⱼ is a square. The
local-class rigidity of Step 1 is itself CERTIFIED on 32 pairs of diagonal forms with det in one square class
(`thmF_check.txt` part 2: r_L(n)r_{L'}(1) = r_{L'}(n)r_L(1) for every n ≤ 4·10⁴ in 𝒞₁, 0 violations; most of these
genera have one class, so this checks (S1) rather than the cusp part). Combinations *across* nebentypus classes are not
modular forms and are outside the theorem; for them Steps 2–3 give only Σ_δ E_δ(1) = 0 (gap, §4.4).

**What Theorem F does not cover.** Weight 3/2 forms whose Eisenstein part is not a combination of genus thetas (e.g.
Eisenstein series with odd-character data or the non-holomorphic Zagier series, whose holomorphic part Σ H(n)qⁿ is
mock modular); higher half-integral weights k/2 ≥ 5/2 (quaternary-plus lattices; the same proof works verbatim with
Iwaniec's range, but the input list differs — not written out); and support conditions imposed on residue classes of
the representing vectors (theta series with characteristics). Assessment: the proof uses only "Eisenstein = local
densities × common Euler product" and "cusp eigenvalues ≤ 2√ℓ", so it should extend; not claimed.

## 4. What is left of E1: three regimes

Let g be a proxy as in §3 (or more generally a weight-3/2 form) and p ∈ 𝔐 a large prime.

### 4.1 Eisenstein-carrying regime (Assessment + PROVED pieces)
Possible only off 𝒞₁ (Remark F2). For level supported on {2,3,5,7} that is off 𝔐: Mordell's identities already cover
those primes. For larger levels it is the set of 𝔐-primes that are non-residues modulo some ℓ | N; on it a valid
Eisenstein-carrying proxy would be effective (Duke–Iwaniec, ineffective constants) and validity there *is* (MS)
restricted to that set. **Shimura propagation (PROVED, Steps 2–3 above with t = p):** if E(p) ≠ 0 and g is valid on all
n ≡ 1 (4), then g(pℓ²) = ℓ·E(p)·(1 + o(1)) + O(√ℓ) ≠ 0 for all large primes ℓ ≡ 1 (mod M), so validity also forces
R(pℓ²) ≥ 1 for all those ℓ: an E1 proof of (MS) via an all-n-valid proxy would prove positivity on infinitely many
composite orbits. Orbit zeros R(t·m²) = 0 with t prime exist (17 ≤ 10¹⁰, §5) but none with m coprime to 1155, so this is
a consequence, not a refutation.

### 4.2 Pure-cusp regime (the regime Theorem F forces on 𝒞₁ ⊇ 𝔐)
g(p) = h⊥(p) = Σⱼ hⱼ(p). For a single eigenform hⱼ, Waldspurger's theorem gives hⱼ(t)² = (local factor depending only
on the class of t at the primes dividing 4N)·t^{1/2}·L(½, Fⱼ ⊗ χ_t)·(constant), χ_t = (−t/·), for squarefree t
(Waldspurger 1981, cited; explicit form in the plus space: Kohnen–Zagier Thm 1, read, and Kohnen 1985 — note the plus
space itself vanishes at n ≡ 1 (mod 4), so for p ∈ 𝔐 the general-space version is the relevant one; Darreye
arXiv:2007.06224 §2 states it in that generality, read). For p ∈ 𝔐 the twist is χ_{−4p}, and the local factor is
constant on the class. So
* *effectiveness* of a single-eigenform proxy on a class of primes = non-vanishing of L(½, F ⊗ χ_{D(p)}) for **all**
  large p in the class. When the twisted root number is −1 on the class this fails identically; when it is +1 it is an
  open Goldfeld-type problem (only positive-proportion results are known: Ono–Skinner 1998, Kriz–Li 2019; no result
  for all large primes in a progression — literature status, `lit_verify.md` §6);
* *validity* requires L(½, F ⊗ χ_{D(p)}) = 0 at the in-𝔐 (★)-zeros, i.e. the zeros would have to be "rank ≥ 1 twists".
* sizes: |h(p)| ≪ p^{1/2−1/28+ε} (Iwaniec 1987 / Duke 1988, cited), against R(p) ≍ log²p on average — no contradiction
  either way; the cusp coefficient carries no main term to beat.

**Screen (EVIDENCE; `scripts/z58_ternary_waldspurger.py`, `data/z58/ternary/waldspurger_screen.txt`).** For 16 weight-2
newforms F (elliptic curves of conductor 14, 15, 20, 21, 24, 27, 30, 32 (two), 35, 36, 42, 45, 48, 56, 63 — level
supported on {2,3,5,7}, so Shimura lifts of level-4N forms with N | 2^a·3·5·7) and the twist χ_{−4p}:
* the root number is constant on each 𝔐 class tested (as it must be: χ_{−4p}(−N_F) is fixed by p mod 840);
* conductors 21 and 45: root number −1 at all 4 zero primes and 8 controls ⟹ such a proxy vanishes on the class
  (ineffective);
* the other 14: root number +1, and analytic rank 0 (L(½) ≠ 0) at ≥ 2 of the 4 in-𝔐 zeros 5569, 9601, 83449, 102001
  ⟹ a single-eigenform proxy from F is **invalid**; rank-2 twists occur at zeros and controls alike (zeros 11/56, controls 14/112 twist
  evaluations with w = +1; the two conductor-32 models are isogenous, so they share an L-function and are counted
  twice; the small excess at zeros is not significant at these counts).
* No F of these levels is compatible with being a valid and effective single-eigenform proxy. Linear combinations of
  eigenforms are not excluded (finitely many zeros can always be fitted), and nothing here suggests a structural
  reason for validity.

### 4.3 Prime-only validity (the named escape)
A proxy only required to satisfy g(p) ≠ 0 ⟹ R(p) ≥ 1 *at primes* escapes Theorem F (it need not vanish at ℓ²) — but then
modularity supplies no reason for validity: on any class where g(p) ≠ 0 for all large p (e.g. Eisenstein-carrying),
validity is literally (MS) on that class. A reason must come from a *recipe* turning representations/Heegner points
into certificates using primality. Bounded-complexity recipes from a fixed lattice are excluded off Mordell-type
classes (`POINTWISE_TERNARY` Thm 4.1: they use ≪ f(p)p^{1/4+ε} of the ≍ p^{1/2±ε} representations), and Lemma D(c) shows
why: certificates are measure-zero incidences, invisible to equidistribution.

**The escape E1′ (named).** *A recipe of unbounded complexity (depending on gcds / factorisations, or on a parameter
growing with p) that maps a positive-measure set of Heegner points or lattice points of a fixed genus — non-empty
exactly when p is not a square — onto (★)/Type II certificates.* Equivalently (Lemma D(c)): a *thin-set incidence
theorem* for Heegner points on the hypercycles of Lemma D(c), at Planck scale |D|^{−1/2}. No such theorem exists in
the literature checked (equidistribution reaches shrinking targets of size ≥ |D|^{−1/24}, Young; |D|^{−1/8} under
Lindelöf; see AUTOMORPH §4 E1); and the F3 data say such a theorem may not need primality beyond non-squareness and
gcd(n, 105) = 1 (§5). This is the old B2 / H-A wall seen from half-integral weight.

### 4.4 Gaps (honest list)
* Mixed-nebentypus combinations (not modular forms) and non-genus Eisenstein series: only Σ_δ E_δ(1) = 0 follows.
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
* Composite zeros coprime to 105: 24, the last 29 210 401 = 11·31·85661 (decades 10³…10⁷: 4, 5, 9, 3, 3); coprime to 15:
  44, last 7 479 950 569; coprime to 1155: 16, last 17 401 609. LADDER: in 𝔐 none in (17 401 609, 10¹¹].
* Reading (EVIDENCE): the composite zero set persists to 10¹⁰ (≈ 40 per decade) only through the factors 3, 5, 7.
  Away from them, (★) zeros among non-squares stop near 3·10⁷ — non-squareness plus coprimality to 105 is all the data
  ask for. Primality is not visibly needed in 𝔐.

## 6. Verdict, screens, proposed FRONTIER text, bottom line

**Verdict: narrowed.**
* Q-T: no construction. Q-N: Theorem F (PROVED rel. Siegel / Siegel–Weil / Shimura–Niwa / Deligne) — for every
  weight-3/2 proxy built from ternary theta series plus cusp forms, validity at the squares of primes forces the genus
  main term to vanish on the joint local class of the squares, which at level 840 is exactly 𝔐 (Cor F1). On 𝔐 the
  Duke template has nothing to work with: what remains is a cusp coefficient, whose non-vanishing at all large primes
  of a class is an open Goldfeld-type problem (and false on root-number −1 classes), and whose vanishing at the known
  zeros fails for every small-level eigenform tested (§4.2).
* This corrects AUTOMORPH's reading of F1 in half-integral weight and makes its Prop C unconditional in the ternary-theta
  class.
* Escape left: E1′ (§4.3), unbounded-complexity recipes = Planck-scale incidence for Heegner points = B2/H-A.

**FRONTIER §4 hard screens (Theorem F as the best idea).** T1 squares: it *is* T1, used through local densities at the
squares of primes. 8/131: line-blind (negative statement). Tied modulus: the tied event is the Planck-scale incidence of
Lemma D(c); fixed-level forms cannot see it. Fixed p: statement is pointwise in p after the level is fixed.

**Proposed FRONTIER §6/§7 text (do not edit FRONTIER here).**
> *Half-integral weight (z58 TERNARY, Thm F, PROVED rel. Siegel's formula, Siegel–Weil, Shimura/Niwa lift, Deligne).*
> Let g ∈ M_{3/2}(Γ₀(4N), ψ) be a combination of ternary theta series plus cusp forms. If g(ℓ²) = 0 for all large primes ℓ
> (forced by T1 on any valid support proxy), the genus part of g vanishes on every n that is a unit square at all
> ℓ | 2N, and the t = 1 unary thetas vanish. The squares of (ℤ/840)^× are exactly Mordell's 𝔐, so at level 840 every
> valid proxy is a pure cusp coefficient at every 𝔐-prime: no main term for Duke–Iwaniec. Its non-vanishing is a
> Goldfeld-type central-value problem; small-level single-eigenform proxies are invalid at the known zeros. Remaining
> escape: unbounded-complexity recipes (Planck-scale Heegner incidences, Lemma D(c)) = B2.
> Add to §6: "weight-3/2 / ternary-theta support proxies with a genus main term on Mordell's classes".

**Bottom line.** The brief asked whether half-integral weight — the classical technology for pointwise representation
of a single large integer — can carry (MS). AUTOMORPH left it open because odd squares and primes sit in different
Shimura orbits. They do, but the genus (Eisenstein) part does not care about orbits: by Siegel's formula it depends on n
only through local square classes and a common Euler product, so vanishing at the squares of primes kills it on the
whole local class of the squares — and at level 840 that class is exactly Mordell's 𝔐. On the target classes a
ternary-form proxy is therefore a pure cusp coefficient, with no main term to beat the cusp error; making it non-zero at
every large prime is a Goldfeld-type problem, and the small-level eigenforms tested are not even valid at the known
zeros. Certificates themselves are Planck-scale incidences of Heegner points with explicit hypercycles, which no
representation or equidistribution theorem sees. Nothing here moves (MS); the wall is B2 again, now with a sharp
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
(pending)

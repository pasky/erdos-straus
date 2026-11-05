# Z58_TERNARY — the half-integral-weight escape E1: F1 kills the genus main term of every ternary-theta proxy on the local class of the squares (⊇ 𝔐); what is left is a pure cusp / Waldspurger problem

Status: z58 follow-up lane TERNARY (brief `z52bbriefs/z58_lanes.md` §TERNARY; common rules `z52bbriefs/z53_depth.md`).
Internal; internally reviewed only. **ES is OPEN; nothing here proves or disproves ES, (★), or (MS).**
Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment.
Scripts `scripts/z58_ternary_*`, data `data/z58/ternary/`. Read: `Z58_AUTOMORPH.md` (Thm A, §4 E1, Prop C),
`POINTWISE_TERNARY.md` (Thm 4.1, (Q_d)), `Z57_SYNTH.md` §§0–2, `Z58_LADDER.md` (L2^𝔐 census), `Z58_WILDCARD.md`,
`METAPLECTIC_ES.md` Thm K, `Z53_WILDCARD.md` row 6, `BRAINSTORM/bsB_theta_multiplier.md`, `git grep` Duke / spinor / ternary.

*Checkpoint 1 (this version): §0 falsifier table, §1 statements, §2 dictionary, §3 Theorem F (statement + proof
outline), §5 first data. Proof details, numerical certification of the inputs and the Waldspurger regime follow.*

---

## 0. MANDATORY FALSIFIER TABLE

Mechanism examined: *a quadratic-form / half-integral-weight proxy* — g = Σ cᵢ θ_{Lᵢ} (+ cusp forms), Lᵢ positive
ternary lattices, or a class-group / Heegner count — *whose non-vanishing at p is supposed to force a (★) or Type II
certificate*, made pointwise by the Duke–Iwaniec template (Eisenstein ≫ p^{1/2−ε} beats cusp ≪ p^{1/2−1/28+ε}).

| screen | behaviour |
|---|---|
| **F1 odd squares** | AUTOMORPH read F1 as not binding in half-integral weight (squares and primes are different Shimura orbits). **Theorem F (§3) shows it does bind, through the Eisenstein part:** if g(ℓ²) = 0 for the primes ℓ (as T1 demands of a valid proxy), the genus part of g vanishes identically on the joint local class 𝒞₁(2N) of the squares (n a unit square at every ℓ \| 2N). For level N with prime support in {2,3,5,7} this class contains all of 𝔐. So F1 itself removes the main term on the target classes; primality (indeed anything) can only enter through the cusp part. |
| **F2 C-even sub-line** | The proxies examined see C only through discriminants −4Cp / local data at 2; they do not distinguish the C-odd from the C-even line. Theorem F is line-blind and *negative*, so it proves nothing false. No positive statement is made. |
| **F3 composites** | Theorem F needs no composite data (it improves AUTOMORPH Prop C, which needed H_E + infinitely many composite zeros). Data (§5): 17 Shimura-orbit zeros t·m² (t prime, R(t·m²) = 0) ≤ 10¹⁰, but only one with m coprime to 105; composite zeros coprime to 105 end at 29 210 401 (LOGIC census) and in 𝔐 at 17 401 609 (LADDER, to 10¹¹). So in 𝔐 the data never require primality beyond non-squareness above 1.75·10⁷ (EVIDENCE) — composites do not bind a level-840k E1 proxy; F1 does (Thm F). |
| **F4 known zeros** | Nothing is proved positive. In the pure-cusp regime left by Thm F, a valid eigen-proxy must vanish at the 9 in-𝔐 (★)-zeros, i.e. L(½, F ⊗ χ) = 0 there (Waldspurger), §4. |

No HOT LEAD.

---

## 1. Precise statements attacked

Notation: R(n) = #{(u,B,C) ∈ ℕ³ : 4uBC − u − B = n}; N_II(n) = #{(a,b,c,d) ∈ ℕ⁴ : 4abcd = a + b + nc} (Type II; (★) is
c = 1). 𝔐 = {1, 121, 169, 289, 361, 529} mod 840.

**Q-T (construction).** Is there a positive definite lattice family / class-group or Heegner count G(p), of power
size, such that G(p) > 0 ⟹ R(p) ≥ 1 (or N_II(p) ≥ 1) for primes p ∈ 𝔐, and G(p) > 0 follows (even ineffectively) from
Duke–Schulze-Pillot / Iwaniec / Siegel?

**Q-N (scoped no-go).** Prove that representation-by-forms cannot force the tied divisor event d ≡ −1 (mod 4C), in a
precise class, and name the escape.

What is new relative to prior closures:
* `POINTWISE_TERNARY` Thm 4.1 / paper `thm:ternary`: *bounded-complexity recipes* from a fixed lattice give only
  Mordell-type coverings. Not about the *support/proxy* form, and not about F1.
* `Z58_AUTOMORPH` Thm A: integral weight, killed by T1 at p, p², p⁴. E1 (half-integral weight) left open; Prop C
  CONDITIONAL on (H_E) and on infinitely many composite zeros in a local class.
* Here: half-integral weight, *unconditional on (H_E)*, with F1 alone; plus the dictionary and data.

## 2. Dictionary (PROVED, elementary)

**Lemma D.** For a prime p (indeed any n ≥ 1):
(a) Type II solutions (a,b,c,d) ↔ triples (C, a, f) with C = d, f = 4acd − 1, f ≡ −1 (mod 4aC), f | n + 4Ca²
    [then c = (f+1)/(4aC), b = (nc + a)/f]. (★) is the case f = 4aC − 1.
(b) Equivalently: positive definite binary forms [f, β₂, g] := fx² + 2βxy + gy² with fg − β² = Cn, β = 2aC
    (so 4C | 2β), and 2β | f + 1 [c = (f+1)/(2β)]. (★) ⟺ 2β = f + 1.
(c) Heegner reading: z = (−β + i√(Cn))/f. The certificate condition f + 1 = 2βc says that z lies on the Euclidean
    line through −1/(2c) with Re z + 1/(2c) = −Im z/(2c√(Cn)) — a hypercycle of the geodesic Re z = −1/(2c) at
    hyperbolic distance arsinh(1/(2c√(Cn))) ≍ |disc|^{−1/2}. Certificates are *exact incidences* of Heegner points
    with an explicit Planck-scale-displaced hypercycle, a measure-zero condition.
(d) (norm form of T1) For n = m², 4Cm² + 1 = N_{ℚ(√−C)/ℚ}(1 + 2m√−C); every divisor of a norm coprime to 4C from
    ℚ(√−C) lies in ker χ_{−4C}, and χ_{−4C}(−1) = −1, so no divisor is ≡ −1 (mod 4C). For n = p prime,
    4Cp + 1 = N(1 + 2√(−Cp)) is a norm from ℚ(√−Cp) only; the certificate forms lie in the genus with χ_p = −1.

(a)–(b) are `POINTWISE_TERNARY`'s (Q_d) (n = ef − 4da², 4ad | f + 1) in form language; (c)–(d) make the "Planck
scale" and the T1 mechanism explicit. Proofs: §2.1 (to be written out at final).

## 3. Theorem F — F1 kills the genus main term on the local class of the squares

Setting. N ≥ 1, ψ a character mod 4N, g ∈ M_{3/2}(Γ₀(4N), ψ) of the form g = Σᵢ cᵢ θ_{Lᵢ} + h with Lᵢ positive
definite ternary ℤ-lattices whose theta series lie in that space and h ∈ S_{3/2}(Γ₀(4N), ψ). E := Σ cᵢ θ_{gen Lᵢ}
(Siegel's genus average; g − E is a cusp form). 𝒞₁(2N) := {n ≥ 1 : n ∈ (ℤ_ℓ^×)² for every prime ℓ | 2N}.

**Theorem F (PROVED relative to Siegel's formula, Shimura's T(ℓ²), cuspidality of the Shimura lift of cusp forms
orthogonal to unary theta series, and the Ramanujan bound in weight 2; inputs listed in §3.2).** Suppose g(ℓ²) = 0
for all sufficiently large primes ℓ ∤ 2N. Then
(i) E(n) = 0 for every n ∈ 𝒞₁(2N);
(ii) the unary-theta components of g on the square class of 1 vanish;
(iii) hence for every prime p ∈ 𝒞₁(2N) larger than a constant T(g): g(p) = h⊥(p), the coefficient of a cusp form
     orthogonal to all unary theta series.
**Corollary F1.** If the odd primes dividing N lie in {3, 5, 7}, then 𝔐 ⊂ 𝒞₁(2N) (every class of 𝔐 is ≡ 1 mod 8 and
a square mod 3, 5, 7). So a valid support proxy of this shape is, at every large 𝔐-prime, a pure cusp coefficient: no
main term exists for the Duke template. For general N the same holds at every large 𝔐-prime that is a quadratic
residue modulo every odd ℓ | N (e.g. whenever the least quadratic non-residue n_p exceeds the largest prime of N).

**Proof outline.** (1) Siegel: for n ∈ 𝒞₁(2N), local densities at ℓ | 2N are those of n = 1 (x ↦ ux is an isometry
for u ∈ ℤ_ℓ^×, so α_ℓ(L, nu²) = α_ℓ(L, n)); at ℓ ∤ 2N all Lᵢ are unimodular with determinant in one square class
(single nebentypus), so the factor ∏_{ℓ∤2N} α_ℓ(n)·√n is common to all i. Hence E(n) = B(n)·E(1)/B(1) on 𝒞₁ with
B > 0, and E ≡ 0 on 𝒞₁ ⟺ E(1) = 0. (2) E is a T(ℓ²)-eigenform with eigenvalue 1 + ℓ (ℓ ∤ 2N), so
E(ℓ²) = E(1)(1 + ℓ − ε(ℓ)), ε a fixed quadratic character. Unary thetas on the class of 1 contribute 2κ_kψ_k(ℓ)ℓ (ψ_k
odd). The cusp part orthogonal to unary thetas is a sum of T(ℓ²)-eigenforms with |λ(ℓ)| ≤ 2√ℓ, contributing O(√ℓ).
(3) So 0 = g(ℓ²) = ℓ·[E(1) + 2Σ_k κ_kψ_k(ℓ)] + O(√ℓ); on each class ℓ ≡ a (mod M) the bracket must vanish;
orthogonality of characters (ψ_k odd, trivial character even) gives E(1) = 0 and all κ_k = 0. ∎ (details §3.1)

## 5. First data (EVIDENCE / CERTIFIED arithmetic on the LOGIC census)

`scripts/z58_ternary_orbit.py` → `data/z58/ternary/orbit_zeros.txt`; `scripts/z58_ternary_coprime.py` →
`data/z58/ternary/coprime_zeros.txt` (input: `data/z58/logic/zeros_1e10.txt.gz`, all n ≡ 1 (4) ≤ 10¹⁰ with R(n) = 0).
* 486 non-square composite zeros ≤ 10¹⁰ (largest 9 919 520 121); 244 have a square factor.
* Shimura-orbit zeros n = t·m² with t prime, m > 1: **17** (801 = 3²·89, …, 71 724 681 = 21²·162641); m ∈ {3,5,7,9,11,21}.
  With m coprime to 105 only one remains (752 257 = 11²·6217); none with m coprime to 1155.
* Composite zeros coprime to 105: 24, the last 29 210 401 = 11·31·85661; coprime to 15: last 7 479 950 569; to 3:
  last 7 479 950 569. Above 3·10⁷ every composite zero ≤ 10¹⁰ has a factor 3, 5 or 7.
Reading: composite and orbit zeros constrain an E1 proxy only through the primes 3, 5, 7 (absorbed by the level);
in 𝔐 they end at 1.75·10⁷ (LADDER). The live constraint on E1 is F1 (Theorem F), not F3.

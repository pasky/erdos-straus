# bsC_isogeny_ramanujan — Type I as a pair of orthogonal isogenies; Ramanujan (Pizer) graphs as an existence engine (O176)

**ES is not solved here.** Labels as in DISCOVERIES.md.

## Idea
QUATERNION_ES Prop 2.1 (isogeny reading): Type I(p) ⟺ supersingular E, E' and orthogonal φ₁, φ₂ ∈ Hom(E', E) of degrees
a, b (with u ∈ End E, u² = −d, tr(uφ₂φ̂₁) = 1) such that `[Hom(E',E) : L] = e` divides `deg(φ₁ + φ₂) = a + b`.
Supersingular ℓ-isogeny graphs are Ramanujan (Pizer), so isogenies of a given degree between *any* two curves exist once
the degree is large: a deterministic existence engine on all ≈ (p/12)² pairs (E, E').

## Literature
Pizer, *Ramanujan graphs and Hecke operators*, Bull. AMS 23 (1990); Kane, *Representations of integers by ternary
quadratic forms* (IJNT 2009) and Chevyrev–Galbraith 2014 (every Hom(E', E) represents every n ≫ p^{2+ε} as a degree);
Böcherer–Schulze-Pillot, *Siegel modular forms and theta series attached to quaternion algebras* (Nagoya 1991) (genus-2
theta series of Hom-lattices; representations of binary forms diag(a, b)); Ellenberg–Venkatesh, *Local–global principles
for representations of quadratic forms*, Invent. 171 (2008) (binary-by-quaternary needs det ≫ disc^{C}).

## Barrier screen (construction log)
1. *Degree existence.* Hom(E', E) (quaternary, det (p/4)²) represents every n ≥ C_ε p^{2+ε}. Type I needs a, b with
   ab = m = (pe+1)/4d; taking e large (e ≥ p^{3+ε}) puts a, b in the deterministic range. *(R176 repair D10: vacuous — Type I tuples have
   e ≤ (p+1)² + 1 and ab ≪ p³, so a, b ≥ p^{2+ε} never occurs; the deterministic regime is never reached.)* **Target hypothesis of B3:**
   "bounded multiplicity". Outcome: the event `e | a + b` has probability ≍ τ-weighted 1/e per pair; the main term of the
   configurations at level e is ≍ (pairs (a,b) with ab = m) × (1/e) ≪ τ(m)/e: B3 (main term must be p^{o(1)}).
2. *Orthogonal pairs (binary representations).* Siegel–Weil for the genus of Hom-lattices: Σ_{E,E'} r(Hom(E',E), diag(a,b))
   / |Aut|² = genus-2 Eisenstein coefficient (all pairs (a, b) represented for det ≫ p^{C}, Ellenberg–Venkatesh type).
   Same as bsC_supersingular_transfer: a genus statement; the index condition `[Hom : L] = e | a + b` is not a
   representation datum (R172 D8: genus-invariant data). B2.
3. *Walk version.* A Type I configuration is a closed walk E → E' → E of degrees (a, b) composing to v (deg ab) with
   prescribed Eichler orientation (bsC_eichler_orientation Prop 1): v − a factors through the level isogeny. Mixing of
   non-backtracking walks equidistributes endpoints, not the scalar χ(v) ∈ ℤ/e vs a divisor of deg v (an arithmetic,
   not spectral, coincidence). B2.
* **T1**: no supersingular curves are attached at n = m² (Diff even); the Ramanujan engine has no analogue, consistent.
* **B6**: Pizer's bounds are pointwise in (E, E'); not the issue.

## Cheap numerics
None run (the B3 accounting is exactly CONDITIONAL_ES Prop 2.3 with main term τ(m)/e; QUATERNION_ES §3.4 already exhibits
admissible (d, e) of both ES statuses).

## Assessment
**COLLAPSES (B3 for the large-degree regime, B2 for the genus-2 count).** Ramanujan expansion is a real deterministic
engine, but it produces degrees/representations, which are genus data; the ES index condition costs 1/e. Promise 0.

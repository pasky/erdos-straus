# DIFF_DEEP — the supersingular / Diff-parity route taken to depth (task O176)

Status: internal research note, SPARK phase. **ES is not solved here, nor any infinite case of it.** Labels as in
DISCOVERIES.md. Builds on KUDLA_ES.md (O172, as repaired by R172: D3 Z(T) ≠ ∅ iff |Diff(T)| = 1; D4 congruences are
sufficient, only the genus shadow is necessary; D5 the Type II index T' = [[f,1],[1,f']] is a *chosen* index; D8 Kudla
data are genus-invariant; D9 coset Schwartz functions see the full ray class, but as the split-plane count).
Memos: BRAINSTORM/bsC_*.md. Scripts `scripts/bsC_*`.

**Question (orchestrator).** Is ES at p equivalent to a statement about (small) endomorphisms of *some* of the ≈ p/12
supersingular curves mod p, with an existence theorem lurking in the geometry of maximal orders of B_{p,∞}?

**Answer in one paragraph.** (§1) The quantifier "some supersingular curve" is vacuous: a configuration of Gram T exists
on some curve iff Diff(T) = {p}, which every certificate index satisfies by genus theory; the "every curve" version is
false (Type I certificates live on p^{o(1)} curves). (§2) The ray-class condition *can* be moved onto the curve as a
level structure, and then it is free: every maximal order contains, for every M, special endomorphisms x with
nrd(x) ≡ −1 (mod M). Type II becomes exactly a **level-vs-determinant** inequality for a pair of special endomorphisms
(Thm 2.1: `4h | gcd(h, G)²`, h = det/p, G = level); the deterministic lift misses it by a factor ≍ f^{3/2} ≥ M^{3/2} in
the determinant (Prop 2.4) — the scale barrier B3 in geometry-of-numbers form. (§3) Type I has the same shape with
the Eichler orientation. (§4) What a breakthrough would have to prove, stated as a lattice problem in the genus of
maximal orders.

## 1. The supersingular transfer and its exact hypotheses

**Theorem 1.1 (supersingular transfer; PROVED; = bsC_supersingular_transfer Thm 1).** For positive definite
half-integral binary T: there is a supersingular E/𝔽̄_p with trace-zero x, y ∈ End E of Gram T ⟺ B_T ≅ B_{p,∞} ⟺
Diff(T) = {p}. (Every order lies in a maximal order; Deuring.)

**Corollary 1.2.** ES(p) ⟺ the arithmetic set S_p of certificate-shaped indices is non-empty; every T ∈ S_p has
Diff(T) = {p} (KUDLA_ES Thms 1.2(b)/1.4(b)), so the curves add no condition. (PROVED.)

**Proposition 1.3 (∀E is false; PROVED relative to ET's f_I(p) ≪ p^{o(1)}).** Λ_{d,ab} is an Eichler order of level e;
exactly τ(e) maximal orders contain it; e ≤ (p+1)² + 1. So ≤ 2Στ(e) ≪ p^{o(1)} of the ≈ p/12 curves carry a Type I
certificate. (bsC_supersingular_transfer Prop 3; asymptotic only — numerically f_I(p) ≥ p/12 still holds at p ≈ 10⁴.)

**The hypotheses that make §1 vacuous, and the modification tried for each** (construction log):
* (H1) *the configuration is specified by its Gram matrix* — violated by adding level structure (§2, §3);
* (H2) *the quantifier is "∃ curve"* — "∀ curve" is false (1.3); "a canonical curve" (CM by the least d with
  (−d/p) = −1, or the spine j ∈ 𝔽_p) is QUATERNION_ES Prop 2.2 / the Heegner forms of disc −4p (B2);
* (H3) *Kudla data are genus functions* (R172 D8) — violated only by non-K-invariant Schwartz functions (R172 D9),
  which turn the count into the split-plane coset count (B2);
* (H4) *parity sees quadratic data* — over every base field (bsC_parity_quadratic_only Prop 1); the ray condition
  is quadratic only for M | 24.

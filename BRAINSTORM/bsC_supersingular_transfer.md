# bsC_supersingular_transfer — ES at p as "some supersingular curve mod p has a certificate configuration" (O176)

**ES is not solved here.** Labels as in DISCOVERIES.md. Builds on KUDLA_ES.md (O172, Thms 1.2/1.4, CLAIMED/unreviewed)
and QUATERNION_ES.md (O130). Script `scripts/bsC_supersingular.py` (uses `scripts/bsC_common.py`).

## Idea
O172: a Type I tuple (a,b,c,d,e) of p gives `T = [[d,−1/2],[−1/2,ab]]`, a Type II tuple gives `T' = [[f,1],[1,f']]`,
and Diff(T) = {p}: certificates are supersingular points mod p of Kudla's Z(T). The orchestrator's hope: phrase ES(p)
as "*some* of the ≈ p/12 supersingular E/𝔽̄_p has an endomorphism configuration of a certificate shape", and find an
existence theorem in the geometry of the maximal orders of B_{p,∞} (successive minima, Kaneko, Goren–Love).

## Literature
Deuring correspondence (maximal orders of B_{p,∞} ↔ supersingular j up to Frobenius); Kaneko, *Supersingular
j-invariants as singular moduli mod p*, Osaka J. Math. 26 (1989) (two embedded orders ⇒ D₁D₂ ≥ 4p);
Goren–Love, *Supersingular elliptic curves and small non-integer endomorphisms* (arXiv 2023); Chevyrev–Galbraith,
*Constructing supersingular elliptic curves with a given endomorphism ring*, LMS JCM 17A (2014) (successive minima of
the Gross lattice); Voight, *Quaternion Algebras* (GTM 288), Ch. 23 (Eichler orders), Ch. 30 (optimal embeddings),
Ch. 42 (Deuring); Kudla 1997 / Gross–Keating 1993 (cited only for the reading).

## Statements
**Theorem 1 (supersingular transfer; PROVED).** Let T be a positive definite half-integral binary matrix and
`R_T = ℤ⟨x,y⟩`, `x² = −T₁₁, y² = −T₂₂, xy + yx = −2T₁₂` (an order in the definite algebra B_T). Then there is a
supersingular E/𝔽̄_p and trace-zero x, y ∈ End E with Gram T (for ⟨x,y⟩ = trd(xȳ)/2) **iff B_T ≅ B_{p,∞}, i.e.
Diff(T, 𝒞) = {p}.** *Proof.* ⇐: R_T ⊂ B_T ≅ B_{p,∞} is contained in a maximal order O (every order is), and O ≅ End E
(Deuring). ⇒: two non-commuting pure quaternions generate End⁰E = B_{p,∞}. ∎
**Corollary 2 (the "∃ E" quantifier is vacuous; PROVED).** ES(p) holds iff the set S_p of certificate-shaped T is
non-empty: every T ∈ S_p already has Diff(T) = {p} (O172 Thm 1.2(b)/1.4(b)), so by Theorem 1 it lives on some
supersingular curve. The curves add *no* condition. (Same content as O172 Prop 2.1 and QUATERNION_ES Prop 2.2.)
**Proposition 3 (Type I certificates live on ≪ p^{3/5+o(1)} = o(p) curves; PROVED relative to ET Prop 1.7,
f_I(n) ≪ n^{3/5+O(1/log log n)}, and the divisor bound).** *(R176 repair D4: ET do not prove f_I(p) ≪ p^{o(1)}.)*
For a Type I tuple, `Λ_{d,ab} ⊗ ℤ_ℓ` is an **Eichler order of level ℓ^{v_ℓ(e)}** for every ℓ | e (ℓ odd, ℓ ∤ d, and
`−d ≡ (2a)^{−2}` is a unit square, so ℤ_ℓ[u] ≅ ℤ_ℓ × ℤ_ℓ contains the idempotents and the Peirce decomposition gives
`[[ℤ_ℓ, ℓ^i],[ℓ^j, ℤ_ℓ]]`); it is maximal at all other ℓ (disc = pe, p ∤ e). Local–global for lattices: the maximal
orders containing Λ number exactly `τ(e)`, so at most `2τ(e)` curves carry it. Also `e = (4a²d+1)/(4acd − p) ≤ 4(acd)² + 1 ≤ (p+1)² + 1` (using `2acd ≤ p + 1/e`).
Hence ≤ `2 Σ τ(e) ≪ p^{3/5+o(1)}` curves (p^{o(1)} conjecturally) carry Type I certificates: **"every supersingular curve carries one" is false
for large p.** (Type II: R_{T'} is Eichler at odd ℓ | cd by the same argument since −f ≡ 1 (mod ℓ); the 2-part is not
controlled; Type II version: Assessment.)

## Barrier screen
* **B2 / Prop 2.4 of O172.** Theorem 1 is the class-level statement: deg Z(T) is a GL₂(ℤ)-class function; the
  certificate property is not. The curves are a *genus* object (one genus of maximal orders), so a statement "∃ E with
  config of shape S" equals "S ∩ {Diff = {p}} ≠ ∅".
* **B3.** The ∀E strengthening (which would carry geometric content) is false: certificates are ≪ p^{3/5+o(1)} objects (p^{o(1)} conjecturally; R176 D4) on
  ≈ p/12 curves (Prop 3). Any "for every curve / every maximal order" existence theorem must therefore allow
  configurations of size ≫ (it must produce ≥ p/12 objects), i.e. main term ≫ p^{3/5+o(1)}, which B3 forbids.
* **Canonical E** (curves with CM by the least d with (−d/p) = −1; spine curves j ∈ 𝔽_p for Type II with d = 1): the
  Type I configurations on the CM curve are exactly QUATERNION_ES Prop 2.2 (all content is the divisor condition on
  `m = (pe+1)/4d`); the Type II ones are the Heegner forms of disc −4dp (Ibukiyama orders O(q,r): `i^⊥ ∩ O⁰` carries
  `[q, 2r, (r²+p)/q]`). B2.
* **T1.** At n = m² the analogue of Theorem 1 has no curve at all (Diff even ⇒ B_T ≇ any B_{ℓ,∞} with ℓ | m only to odd
  exponent); consistent, not a mechanism.
* **B6** not relevant (pointwise). Thm 9.1/Prop 10.3: the curve side sees only genus data (Prop 10.3's genus shadow).

## Cheap numerics (`PYTHONPATH=scripts uv run python scripts/bsC_supersingular.py 20000`, 7 s)
2260 primes 5 ≤ p ≤ 2·10⁴: all have Type I and Type II tuples; 0 tuples at odd squares (T1 control).
**Kaneko near-extremality** (EVIDENCE): the least Type I level e (det 2T = pe; Kaneko's floor is e = 1) is ≤ 31 for
every p; the least Type II `c²d` (det 2T' = 16c²dp) is ≤ 24. So certificates are near-extremal pairs of embedded
orders — but (−d/p)-admissible (d,e) pairs are near-extremal for *every* p by genus alone (QUATERNION Prop 2.2).
The bound of Prop 3 is asymptotic only: `C_I(p) = Σ 2τ(e)` exceeds p/12 for 1112/2260 primes here (f_I(p) ~ log³p
is still ≥ p/12 at this scale), so the falsity of ∀E is not visible numerically below 2·10⁴.

## Assessment
**COLLAPSES (B2), with an exact theorem.** The supersingular reformulation is genus-vacuous (Thm 1 / Cor 2); its only
non-vacuous strengthening (∀E) is false (Prop 3, Type I). Where the representative (ray-class) condition *can* be
put on the curve is a **level structure** (bsC_eichler_orientation, DIFF_DEEP §1–2). Promise 1.

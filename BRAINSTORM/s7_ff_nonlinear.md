# s7_ff_nonlinear — Sophie-Germain/Aurifeuillean and Frobenius-digit menus over F_q[T] (O247, mandatory (iv))

## Idea
Over ℤ, thin exponential families escaped ET sterility through windows whose budget is forced by a Sophie-Germain
factorisation ((J)74/(J)75). Conjecture 0.2 (no finite *linear* covering of a neighbourhood of x*_c, q = 3, A = T^k)
says nothing about non-linear menus. Two candidate non-linear menus over F_q[T]:
(a) separable algebraic menus: identities polynomial in U where P = φ(U), φ of degree ≥ 2 (char 3 Sophie-Germain:
4X⁴ + 1 = X⁴ + 1 = (X² + X + 2)(X² + 2X + 2) over F₃; Carlitz-cyclotomic factorisations of Φ_M(X));
(b) the inseparable "Frobenius-digit" menu: every P ∈ F_q[T] is uniquely P = Σ_{i<p} T^i U_i^p, so identities polynomial
in the digits U_i form a *positive-density*, non-linear menu. (R-O247 review fix: the digit map IS continuous at every prime —
P mod ℓ^{pk} determines every U_i mod ℓ^k — it only loses precision by the factor p; the first version wrongly called it
discontinuous. So digit classes are clopen and the compactness framework does apply to them.)

**Lemma 1 (Baire; PROVED).** In the profinite completion Â of F_q[T], let U be open, C a finite union of clopen
(linear-family) validity sets and T₁, …, T_k closed sets with empty interior. If U ⊆ C ∪ ⋃T_i then U ⊆ C.
*Proof.* U ∖ C is open and contained in the closed nowhere-dense set ⋃T_i, hence empty. ∎
**Lemma 2 (thin families are nowhere dense; PROVED under the stated hypothesis).** Let φ ∈ F_q[T][X] be such that φ mod ℓ
is not surjective on F_q[T]/ℓ for infinitely many primes ℓ (e.g. φ = X², q odd; for separable φ of degree ≥ 2 this is the
expected generic case — exceptional/permutation behaviour holds only on restricted sets of residue degrees, Cohen–Fried;
not re-proved here). Then the closure of φ(F_q[T]) in Â has empty interior. *Proof.* A basic open set is fixed mod some
M; pick such ℓ ∤ M and, by CRT, a point of it whose ℓ-coordinate is not in φ(F_q[T]/ℓ); it lies outside the closure. ∎ So (a) can never help cover a neighbourhood of x*_c: Conjecture 0.2 ⟹ no finite covering
by linear + separable thin families (contrast ℤ, where the target was itself a thin family).
**Lemma 3 (lifted digit identities = Frobenius conjugation; PROVED).** Let θ = T^{1/p}, π := Σ θ^i U_i ∈ F_q[θ][U]. Then
π^p = P. If 4/π = 1/X + 1/Y + 1/Z with X, Y, Z ∈ F_q[θ] monic, then 4/P = 4^p/P = 1/X^p + 1/Y^p + 1/Z^p with X^p ∈ F_q[T]
monic (4^p = 4 in F_p). Under F_q[θ] ≅ F_q[T] (θ ↦ T), π corresponds to P^{σ⁻¹} (coefficients Frobenius-inverted). *Proof.* Additivity
of Frobenius. ∎ For q = 3 (x*_c has coefficients in F₃) σ acts trivially, so the π-identities of the digit menu give back
exactly the solutions of P (twisted), no new covering. Digit identities not coming from π (arbitrary polynomial identities
in the U_i) are NOT covered by Lemma 3 and are left open here; since digit classes are clopen (continuity above), they are at
least subject to the same compactness/T1 framework as linear classes.

## Literature
FUNCTIONFIELD_ES2 §0.2 (Conjecture 0.2), FF_THIRDS_CORNER (Liouville lemma), STERILE_DIOPHANTINE Prop 5.1 (Frobenius
u ↦ u³), BRAINSTORM/z15_ff_frobenius ("Frobenius kills Aurifeuille"); Carlitz, Duke Math. J. 1 (1935); Lang–Weil 1954.

## Barrier screen
B1 (compactness): Lemma 1 shows the separable thin menu cannot change any open-set covering statement. T1: in (b) the
cube structure P = π^p is the FF version of "ES for s³ follows from ES for s" — no new mechanism. B2: not reached.

## Cheap numerics
None needed (the statements are structural; Lemma 2's non-surjectivity is visible for X ↦ X² mod any ℓ, q odd).

## Assessment
PROVED (Lemmas 1–3), negative within scope. Over F_q[T] thin (nowhere-dense) menus, e.g. Sophie-Germain/Aurifeuillean
families, cannot help with Conjecture 0.2 (the target is open, not thin); lifted Frobenius-digit identities collapse to Galois
conjugation; general digit-polynomial identities are an open (clopen-class) menu not analysed here. Answer to (iv): no
non-linear covering of x*_c from the analysed menus.

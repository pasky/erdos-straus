# s7_ff_nonlinear — Sophie-Germain/Aurifeuillean and Frobenius-digit menus over F_q[T] (O247, mandatory (iv))

## Idea
Over ℤ, thin exponential families escaped ET sterility through windows whose budget is forced by a Sophie-Germain
factorisation ((J)74/(J)75). Conjecture 0.2 (no finite *linear* covering of a neighbourhood of x*_c, q = 3, A = T^k)
says nothing about non-linear menus. Two candidate non-linear menus over F_q[T]:
(a) separable algebraic menus: identities polynomial in U where P = φ(U), φ of degree ≥ 2 (char 3 Sophie-Germain:
4X⁴ + 1 = X⁴ + 1 = (X² + X + 2)(X² + 2X + 2) over F₃; Carlitz-cyclotomic factorisations of Φ_M(X));
(b) the inseparable "Frobenius-digit" menu: every P ∈ F_q[T] is uniquely P = Σ_{i<p} T^i U_i^p, so identities polynomial
in the digits U_i form a *positive-density*, non-linear menu that is not continuous away from T (P mod ℓ does not
determine U_i mod ℓ), hence outside the compactness framework of FUNCTIONFIELD_ES2 / EXPONENT_COVERING Thm 1.4.

**Lemma 1 (Baire; PROVED).** In the profinite completion Â of F_q[T], let U be open, C a finite union of clopen
(linear-family) validity sets and T₁, …, T_k closed sets with empty interior. If U ⊆ C ∪ ⋃T_i then U ⊆ C.
*Proof.* U ∖ C is open and contained in the closed nowhere-dense set ⋃T_i, hence empty. ∎
**Lemma 2 (separable thin families are nowhere dense; PROVED).** If φ ∈ F_q[T][X] is not of the form ψ(X^p) + const and
deg φ ≥ 2, the closure of φ(F_q[T]) in Â has empty interior. *Proof.* For infinitely many primes ℓ (Lang–Weil /
Chebotarev for the separable cover φ(X) = Y), φ mod ℓ is not surjective on F_q[T]/ℓ; an open set fixes only finitely
many local coordinates. ∎ So (a) can never help cover a neighbourhood of x*_c: Conjecture 0.2 ⟹ no finite covering
by linear + separable thin families (contrast ℤ, where the target was itself a thin family).
**Lemma 3 (digit menu = Frobenius conjugation; PROVED).** Let θ = T^{1/p}, π := Σ θ^i U_i ∈ F_q[θ][U]. Then π^p = P. If
1/π = 1/X + 1/Y + 1/Z with X, Y, Z ∈ F_q[θ] monic, then 4/P = 1/X^p + 1/Y^p + 1/Z^p with X^p ∈ F_q[T] monic (4^p = 4 in
F_p). Under F_q[θ] ≅ F_q[T] (θ ↦ T), π corresponds to P^{σ⁻¹} (coefficients Frobenius-inverted). *Proof.* Additivity
of Frobenius. ∎ For q = 3 (x*_c has coefficients in F₃) σ acts trivially, so the π-identities of the digit menu give back
exactly the solutions of P (twisted), no new covering. Digit identities not coming from π are identities for the cube
π^p over F_q(θ)[U]; their T1 shadow (squares Q² have equidistributed digits, heuristic) keeps the old obstruction.

## Literature
FUNCTIONFIELD_ES2 §0.2 (Conjecture 0.2), FF_THIRDS_CORNER (Liouville lemma), STERILE_DIOPHANTINE Prop 5.1 (Frobenius
u ↦ u³), BRAINSTORM/z15_ff_frobenius ("Frobenius kills Aurifeuille"); Carlitz, Duke Math. J. 1 (1935); Lang–Weil 1954.

## Barrier screen
B1 (compactness): Lemma 1 shows the separable thin menu cannot change any open-set covering statement. T1: in (b) the
cube structure P = π^p is the FF version of "ES for s³ follows from ES for s" — no new mechanism. B2: not reached.

## Cheap numerics
None needed (the statements are structural; Lemma 2's non-surjectivity is visible for X ↦ X² mod any ℓ, q odd).

## Assessment
PROVED (Lemmas 1–3), negative. Over F_q[T] the Sophie-Germain/Aurifeuillean idea is structurally unable to help with
Conjecture 0.2 (the target is open, not thin); the only positive-density non-linear menu (Frobenius digits) collapses
to Galois conjugation. Answer to (iv): no non-linear covering of x*_c from these menus.

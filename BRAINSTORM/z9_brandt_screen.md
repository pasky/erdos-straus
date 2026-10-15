# z9_brandt_screen — exactly how Brandt-matrix / class-number counts of certificate edges fail (O233, goal 4)

## Idea
Goal (4) of O233: a Brandt-matrix count is form-class data. Say exactly how it escapes or fails Prop 10.3. Three levels of
"global data on G_p" are available, and they behave differently.

**(L1) Hecke-equivariant linear data (PROVED, elementary; CONSTRUCTIVE_ES 5.2 in this form).** Let Λ be a linear functional on
ℂ[𝔊⁻_p] with Λ∘T_ℓ = (ℓ + 1)Λ for one ℓ ∤ 2p (R234 repair: ℓ = 2 sits at the level) for which ℓ + 1 is a simple eigenvalue (true for every such ℓ: connectedness + Ramanujan–Deligne).
Then Λ is a multiple of the mass functional f ↦ Σ_L f(L)/|Aut L|. So every functional with this eigen-covariance sees the path indicator 1_path only through
m(p) := Σ_{L path} 1/|Aut L|. (Review repair: this is all that is PROVED. Arbitrary trace-formula quantities or Brandt power
sums need not have this covariance, and nothing is claimed about them.) Separately: the mass-weighted number of path *bases*,
Σ_L #(path bases of L)/|Aut L|, equals the number of χ = −1 words by orbit counting. Full-rank (degree-3) Siegel–Weil gives
nothing beyond this tautology. This number differs from m(p) by class-dependent basis multiplicities. Assessment: L1 data does not
obviously go beyond the word count. That is B6 in spectral form, not a theorem about all Brandt/class-number approaches.
*Proof of the first claim.* (R234 repair: the Brandt weights 1/e(E, C) descend to the ⟨Frob, w₂⟩-quotient as |orbit|/e = 8/|Aut L|, using |Aut L| = 2e·|Stab|.) T_ℓ is self-adjoint for the mass inner product, so ker(T_ℓ − (ℓ+1)) is the constants, and
Λ = ⟨·, g⟩ with T_ℓ g = (ℓ+1)g. ∎

**(L2) Degree-2 data (binary sublattices).** Path-ness needs a primitive plane M = [[v, −1], [−1, t]] with glue ±1 (O224 Prop 3.1,
marked form). Degree-2 Siegel–Weil gives Σ_L r_L(M)/|Aut L| = ε · mass · ∏_v α_v(M) (R234 repair: Siegel's ε = 1/2 for rank 2 in rank 3), positive whenever M is locally represented. That
holds for every M whose genus condition (−p·v⁻¹ a square mod tv − 1, plus the 2- and p-adic conditions; R234 repair) holds. So level L2 guarantees **planes**, and the remaining
condition is the glue residue, which is exactly a Prop 10.3-type residue condition: the class sees the root only modulo
squares, and the path needs the specific roots ±1. This is the precise point of failure: **L2 = genus of (M, c) = Prop 10.3's
quadratic shadow; the certificate condition is the ray-class (residue ±1) refinement.**

**(L3) Class-wise non-linear data (escapes Prop 10.3, but vacuously).** Schiemann (1997): a positive ternary form is
determined up to isometry by its theta series. Hence the Brandt rows (representation numbers) of a class determine whether it
is a path class. So class-wise Brandt data does see the full condition. But "some class has the path property" is the
original problem: no global identity is gained. The escape from Prop 10.3 is exactly as in its R164 scope note: a mechanism
that knows the labelled class (here the theta series, i.e. the factorisation data) is B2.

## Literature
Eichler trace formula; Gross (1987) Heights and special values, §1 (Brandt matrices, theta series of the Gross lattice);
Siegel–Weil (degree ≤ rank); Schiemann, "Ternary positive definite quadratic forms are determined by their theta series",
Math. Ann. 308 (1997); WINDMILL_REDUCTION Prop 10.3 with the R164 scope note.

## Barrier screen
This memo is itself the screen for goal (4). The summary is the three levels above. T1: at n = m² all three levels are empty
(there is no 𝔊⁻_{m²}; CONSTRUCTIVE_ES 5.4).

## Cheap numerics
None needed beyond CONSTRUCTIVE_ES 5.2 (simple Eisenstein eigenvalue checked at 5 primes) and z9_pointer_parity (no residue law for
the raw count P(p)).

## Assessment
PROVED: the L1 eigen-covariance claim (standard linear algebra). L2 and L3 place known results. Assessment (not a theorem)
for "Brandt-matrix / class-number count" routes in general: each of the three natural levels collapses, to the mass m(p)
(L1), to the genus of the plane (L2), or to the problem itself (L3). Promise 0/5. Value: it pins down where a global Fano would have to act. It would have to act on the glue
residue of a binary plane, i.e. on ray-class data mod tv − 1, and that is the modulus that is part of the solution (B2).

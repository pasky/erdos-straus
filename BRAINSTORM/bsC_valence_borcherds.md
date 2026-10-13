# bsC_valence_borcherds — the valence formula as a deterministic existence engine, and why its divisors are too big (O176)

**ES is not solved here.** Labels as in DISCOVERIES.md. Script `scripts/bsC_galois_orbit.py`.

## Idea
The valence formula is a genuinely deterministic existence theorem: a non-zero holomorphic modular form of weight
k > 0 on Γ₀(M) has exactly kψ(M)/12 zeros. Borcherds products have *prescribed* zeros on CM points (Heegner divisors).
If some modular form of positive weight had all its zeros among ES-certificate CM points, certificates would exist.
Dictionary: a Type II certificate (f ≡ f' ≡ −1 mod M = 4cd, ff' = 1 + 4c²dp) gives the primitive form [f, 2, f'] of disc
−16c²dp; the basis change (1,1),(0,1) turns it into `[Mce, 2Mb, f']` (since f + f' + 2 = Mce, 1 + f' = Mb), a **Heegner
point on X₀(M) of discriminant D = −4Mcp and root r ≡ 0 (mod 2M)** — a point of the Heegner divisor Z(D, 0) whose
representative `[MA', B, C]` has the extra shape `C + 1 = B/2` (PROVED, algebra).

## Literature
Borcherds, *Automorphic forms with singularities on Grassmannians*, Invent. 132 (1998), Thm 13.3; Gross–Kohnen–Zagier,
*Heegner points and derivatives II*, Math. Ann. 278 (1987) (Heegner divisors Z(D, r) on X₀(M)); Bruinier, *Borcherds
products on O(2,l) and Chern classes of Heegner divisors*, LNM 1780 (2002) (converse theorem: forms with Heegner
divisors are Borcherds products); Shimura reciprocity / CM theory (Galois acts on Heegner points of disc D on X₀(M)
simply transitively on each (D, r)-family through Cl(D)).

## Barrier screen
**Prop 1 (Galois-orbit obstruction; PROVED relative to Siegel's h(D) ≫_ε |D|^{1/2−ε}; R176 repair D4: the
certificate count on a fixed Z(D, r) is bounded by the divisor bound, not by a (non-existent) ET bound f(p) ≪ p^{o(1)}).**
Let F be a modular form on Γ₀(M) with Fourier coefficients in a number field L, and suppose every zero of F in Z(D, r)
(D = −4Mcp) is a certificate point. The zeros of F form a Gal(ℚ̄/L)-stable set, and Gal(ℚ̄/LK) acts on Z(D, r) with
orbits of size ≥ h(D)/[L:ℚ]. Since #(certificate points on Z(D, r)) ≤ Σ_{c²d = |D|/16p} τ(1 + 4c²dp) ≪ p^{o(1)} (divisor bound; D fixes c²d) and h(D) ≫ p^{1/2−ε}, F has **no** zero
on Z(D, r) unless [L:ℚ] ≫ p^{1/2−ε}. So a valence-formula argument must use forms whose field of definition grows with
p (≈ a ring class field), i.e. forms built from the certificates themselves (circular), or full Heegner divisors —
which are non-empty for genus reasons and contain ≫ p^{1/2−ε} non-certificate points. ∎
* **B2.** Heegner divisors are Γ₀(M)-class (indeed Galois-orbit) objects; the certificate shape `C + 1 = B/2` is a
  representative condition (cf. R172 D8: Kudla/Borcherds data are genus/orbit functions). Bruinier's converse theorem
  closes the loophole "some other form with CM-supported divisor": any such form is a Borcherds product with
  Heegner-divisor support. *(R176 D9: Bruinier's converse theorem is stated for lattices splitting hyperbolic planes;
  a version covering X₀(M) (signature (2,1)) still needs a reference. Prop 1 does not use this sentence.)*
* **B3.** The only forms whose zero sets are small enough (≈ p^{o(1)} points) have degree-p^{1/2} fields of definition;
  counting their zeros is the per-slice lottery again.
* **T1.** At n = m² the analogous D = −4Mcm² Heegner divisors are non-empty (local conditions hold; QUATERNION_ES §4),
  so any certificate-free argument via Z(D, r) would wrongly produce certificates at squares — a T1 failure of the naive
  version, confirming it cannot work as stated.
* B1/B4/B6/Thm 9.1: not engaged.

## Cheap numerics (EVIDENCE; `scripts/bsC_galois_orbit.py 20000`, 18 s)
Slices (c,d) ∈ {(1,1),(1,2),(1,3)}, all primes 5 ≤ p < 2·10⁴: (#certificate pairs)/h(−16c²dp) ≤ 0.25, the maximum
attained at p = 5; typically the ratio is ≈ τ(N)/√p ≪ 1. Certificates are a vanishing fraction of each Galois orbit.

## Assessment
**COLLAPSES (B2/B3) with an exact obstruction (Prop 1).** The valence formula is a real deterministic engine, but its
zero sets on CM loci are unions of Galois orbits of size ≫ p^{1/2−ε}, while certificates number p^{o(1)}. A "small
divisor" modular form would need a growing field of definition — H-A in modular-forms clothing. Promise 0–1.

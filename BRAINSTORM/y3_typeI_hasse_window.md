# y3_typeI_hasse_window — Type I dual Hasse dictionary and the Type I "world overlap" (O211 (d); O207 spark 1)

**ES is not solved here.** Labels as in DISCOVERIES.md.

## Idea (O207 spark 1)
Type I: fg = p² + 4c²d with f ≡ g ≡ −p (mod 4cd) (the cofactors are symmetric: fg ≡ p² and f ≡ −p force g ≡ −p).
If f is prime and |1 − p| ≤ 2√f (Hasse window), Deuring–Waterhouse gives E/F_f with #E(F_f) = f + p (trace
1 − p), so Type I ⟺ 4cd | #E(F_f). O207 also suggested E is ordinary with CM by ℚ(√−d) since f splits there.

## Findings
**(1) The window is the greedy family (PROVED, elementary).** Window ⟺ g ≤ 4(p² + 4c²d)/(p − 1)². Since 4cd | p + g
(f ≡ −p and fg ≡ p² give g ≡ −p) we have c²d ≤ ((p + g)/4)², so g ≤ (4p² + (p + g)²)/(p − 1)²; for p ≥ 17 this
forces g ∈ {1, 3, 5}, g odd. g = 1 (resp. 5) needs p ≡ 3 (mod 4) (the trivial case). **For p ≡ 1 (mod 4) the window
certificates are exactly g = 3: 4cd | p + 3, d ≡ 2 (mod 3), 3 ∤ c** — the classical x = (p + 3)/4 family
(4/p = 1/⌈p/4⌉ + …), a fixed congruence family: B1 (fails whenever every prime factor of (p + 3)/4 is ≡ 1 mod 3).
Numerics (scripts/y3_typeI_hasse.py 20000): 1603/2260 primes have a window certificate; g-distribution {1: 8562,
3: 1941, 5: 234}; odd squares (non-degenerate): 0.

**(2) The CM-by-ℚ(√−d) suggestion is false (EVIDENCE, 0/10737).** The trace-(1 − p) curve has CM field
ℚ(√((p − 1)² − 4f)); in no window certificate p < 20000 is that ℚ(√−d). (The prime f splitting in ℚ(√−d) is a
property of f, not of the Frobenius of this curve: π_f has trace 1 − p, unrelated to the generator of 𝔣 | p + 2c√−d.)

**(3) Type I world overlap (PROVED, elementary).** In Type I the Frobenius x ↦ x^f acts on μ_{4cd} as the power map
ζ ↦ ζ^{−p}: the divisor world is μ_{f+p} (the group {x : x^f = x^{−p}}), p's residue world is F_f^*, and
Hom(μ_{f+p}, F_f^*) has image of order gcd(f + p, f − 1) = gcd(p + 1, f − 1). Unlike Type II (overlap 2, TORSION_FIRING
Thm 3.1), the overlap is p-dependent; but full overlap at level 4cd (4cd | gcd) forces 4cd | p + 1, i.e. p ≡ 3 (4),
where f = p² + 4c²d (g = 1) is trivially a certificate. For p ≡ 1 (mod 4) the overlap at level 4cd is
2·gcd(cd, (p+1)/2)_odd: a fixed set of slices dividing p + 1 — a B1/finite-slice object.

## Barrier screen
B1 (window = one congruence family; overlap = slices dividing p + 1), B2 (outside the window f is a moving modulus
with no point-count meaning), T1 (odd squares: 0 non-degenerate window solutions, as Type I must).

## Assessment
Spark 1 COLLAPSES (PROVED): the dual Hasse window captures only the g = 3 greedy family for p ≡ 1 (4), and the CM
link is false. By-product (3): the Type I analogue of torsion–residue orthogonality has p-dependent overlap
gcd(p + 1, f − 1), and its non-trivial part is the trivial case p ≡ 3 (mod 4) — a clean structural explanation of
why p ≡ 3 (4) is easy and why Type I/II for p ≡ 1 (4) have no homomorphic bridge.

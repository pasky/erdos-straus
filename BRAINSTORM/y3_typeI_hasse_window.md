# y3_typeI_hasse_window — Type I dual Hasse dictionary and the Type I "world overlap" (O211 (d); O207 spark 1)

**ES is not solved here.** Labels as in DISCOVERIES.md.

## Idea (O207 spark 1)
Type I: fg = p² + 4c²d with f ≡ g ≡ −p (mod 4cd) (the cofactors are symmetric: fg ≡ p² and f ≡ −p force g ≡ −p).
If f is prime and |1 − p| ≤ 2√f (Hasse window), Deuring–Waterhouse gives E/F_f with #E(F_f) = f + p (trace
1 − p), so Type I ⟺ 4cd | #E(F_f). O207 also suggested E is ordinary with CM by ℚ(√−d) since f splits there.

## Findings
**(1) The window is the greedy family (PROVED, elementary).** Window ⟺ g ≤ 4(p² + 4c²d)/(p − 1)². (R-O211 repair:
complete argument.) Write f + p = 4cd·a, g + p = 4cd·b (a, b ≥ 1; f ≡ g ≡ −p). Expanding fg = p² + 4c²d gives
4cd·ab − p(a + b) = c, i.e. cd = pd(a + b)/(4abd − 1) ≤ p(a + b)/(4ab − 1) ≤ 2p/3, and likewise c ≤ 2p/3; so
c²d ≤ 4p²/9 and g ≤ (100/9)p²/(p − 1)² < 13 for p ≥ 17; g is odd (g ≡ −p mod 4). For g ∈ {7, 9, 11} use
c²d ≤ ((p + g)/4)² (from 4cd | p + g): g(p − 1)² ≤ 4p² + (p + g)² fails for p ≥ 17. Hence g ∈ {1, 3, 5}. g = 1 (resp. 5) needs p ≡ 3 (mod 4) (the trivial case). **For p ≡ 1 (mod 4) the window
certificates are exactly g = 3: 4cd | p + 3, d ≡ 2 (mod 3), 3 ∤ c, with f = (p² + 4c²d)/3 PRIME and in the
window** (f prime is a genuine extra condition: (p, c, d) = (29, 2, 2) gives f = 291) — a sub-family of the classical x = (p + 3)/4 family
(4/p = 1/⌈p/4⌉ + …), a fixed congruence family: B1 (fails whenever every prime factor of (p + 3)/4 is ≡ 1 mod 3).
Numerics (scripts/y3_typeI_hasse.py 20000): 1603/2260 primes have a window certificate; g-distribution {1: 8562,
3: 1941, 5: 234}; odd squares (non-degenerate): 0.

**(2) The CM-by-ℚ(√−d) suggestion fails (EVIDENCE: in none of the 10 737 window certificates p < 20000; one
counterexample already refutes it as a general claim).** The trace-(1 − p) curve has CM field
ℚ(√((p − 1)² − 4f)); in no window certificate p < 20000 is that ℚ(√−d). (The prime f splitting in ℚ(√−d) is a
property of f, not of the Frobenius of this curve: π_f has trace 1 − p, unrelated to the generator of 𝔣 | p + 2c√−d.)

**(3) Type I world overlap (PROVED, elementary).** In Type I the Frobenius x ↦ x^f acts on μ_{4cd} as the power map
ζ ↦ ζ^{−p}: the divisor world is μ_{f+p} (the group {x : x^f = x^{−p}}), p's residue world is F_f^*, and
Hom(μ_{f+p}, F_f^*) has image of order gcd(f + p, f − 1) = gcd(p + 1, f − 1). Unlike Type II (overlap 2, TORSION_FIRING
Thm 3.1), the overlap is p-dependent; full overlap at level 4cd (4cd | gcd) forces 4cd | p + 1, hence
p ≡ 3 (4) (one-way), and then f = p² + 4c²d (g = 1) is trivially a certificate. (R-O211 repair: the window does not
require full overlap — (p,c,d,f,g) = (7,3,1,17,5) is a window certificate with 12 ∤ 8.) For p ≡ 1 (mod 4) PARTIAL
overlaps exist: at level 4cd the overlap divides 2·gcd(cd, (p+1)/2) (e.g. (17,1,3,43,7): gcd(18,42) = 6); they occur
only on slices whose cd shares odd factors with p + 1 — a fixed finite slice set per p (B1 type).

## Barrier screen
B1 (window = one congruence family; overlap = slices dividing p + 1), B2 (outside the window f is a moving modulus
with no point-count meaning), T1 (odd squares: 0 non-degenerate window solutions, as Type I must).

## Assessment
Spark 1 COLLAPSES (PROVED): the dual Hasse window captures only the g = 3 greedy family for p ≡ 1 (4), and the CM
link is false. By-product (3): the Type I analogue of torsion–residue orthogonality has p-dependent overlap
gcd(p + 1, f − 1); full overlap at level 4cd happens only in the trivial case p ≡ 3 (mod 4), while for p ≡ 1 (4)
partial homomorphic bridges exist on the finitely many slices with gcd(cd, p + 1) > 1 (not exploited here).

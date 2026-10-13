# bsI_tes_cubic_t1 — an honest order-3 T1: 9/n = ω/x + ω²/y + 2/z over ℤ[ω] with 2-primary denominators (O182)

**ES is not solved here.** Deep version: TWISTED_T1.md §3–§5. Scripts `scripts/tw_eis*.py`.
## Idea
Build T1 from parts: anchor = a place where the denominators' normalisation pins inv α to a non-zero constant;
partner = a wild place where the numerator kills inv α; tame places vanish (DRINFELD_ES Thm 2.2(i)).
## Statement (PROVED, Thm 3.2)
For n ≡ 1 (mod 2), gcd(n, 6) = 1: every TES(n) solution has Σ_{π|n} inv_π α = −⟨ω, 2⟩₂ ≠ 0; at n = π³ (indeed π^{3k})
no Type I/II-shaped solution exists, although TES(π³) is solvable (inherited solutions).
## Barrier screen
B5: this is exactly a cubic B5 — any Type I/II route to "TES at all primes" has a false step at cubes.
B1: congruence identities of Type I/II shape cannot cover classes containing cubes (cubes mod 9 are ±1).
## Numerics (EVIDENCE)
8 primes: 161 Type I/II, cubes (5 split + 2 inert + π⁶): 0 Type I/II; controls (no anchor; numerator 3) restore
Type I/II at cubes. Census 746 primes: invariants always (1, 2, 0); 18 primes with no solution found.
## Assessment
Promise 3 as a dictionary item: T1 is not an accident of ℝ or of order 2. Not an ES route.

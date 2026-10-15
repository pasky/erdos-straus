# Hostile review R231 of STERILE_LOWER.md (O228, checkpoint 1) — round 1

Reviewer: R231 (independent hostile review #1). Branch `side-agent/review-sterile-lower-2`, merged `side-agent/sterile-lower`.
Scripts (from scratch): `scripts/review_zl_*.py`. Status: IN PROGRESS.

## Summary verdicts
(filled in at the end)

## Claim-by-claim

### Lemma 3.1 (joint parametrisation of level-1 data)
Re-derived (i): with f = 4acd − 1 and f | N + 4a²d, Nc + a ≡ −4a²cd + a = −a·f ≡ 0 (mod f); b := (Nc+a)/f,
e := (N+4a²d)/f; 4abd·f = 4ad(Nc + a) = N(f+1) + 4a²d = f(N + e)·… — directly: 4abd = (4acdN + 4a²d)/f = ((f+1)N + 4a²d)/f = N + e;
ce = (cN + 4a²cd)/f = (cN + a(f+1))/f = b + a. a ≤ b ⇔ Nc + a ≥ af = 4a²cd − a ⇔ cN ≥ 4a²cd − 2a. Converse by ef = N + 4a²d
(SE Lemma 1.1(i)). (ii): e·f = 4a²d + 1, na + c ≡ 4a²cd + c = c(4a²d+1) ≡ 0 (mod f); 4abcd = (n+f)b = nb + na + c. Converse:
4acd > n is forced (c(4abd − 1) = n(a+b) > nb·… gives 4acd·b > nb), and ef = 4a²d + 1 with e = (a+b)/c. All correct.
Brute force (`scripts/review_zl_joint.py`, own per-n loops over (a, b, d) for P and (a, c, d) for Q, compared as SETS of
tuples, not counts): X = 100: 685 + 1010 data, 0 mismatches; X = 300: 3301 + 4909, 0 mismatches (same totals as the author).
The divisibility f | na + c was asserted for every (a, d, f, c) in the joint loop: never failed.
Minor: "a ≤ b ⇔ b ≥ a" in (ii) is vacuous as written (presumably meant "⇔ c(4a²d+1) ≥ af·… " or simply "require b ≥ a").
**Verdict: SOUND** (cost-model Consequence is Assessment, correctly labelled).

### Computation 4.1 (level-1 survivors)
Re-derived the level-1 box set from M17 directly: level-1 boxes in non-residue cells are P-boxes from N = r (K = 1; K = 2
has no data by M17 Lemma 1.3), residues −(4acd − 1), −(4bcd − 1) with r ∤ cd, and Q/Q⁻¹-boxes from F = r (k = 1),
residues −4a²d, −4b²d with r ∤ e; U-boxes of level 1 lie in P-boxes of level ≤ 1 (M17 Lemma 5.2, case (α, β) = (1, 0)),
so they add nothing. From-scratch enumerator `scripts/review_zl_level1.py` (own loops: P over (a, b, d), Q over (a, c, d)
with the bound c(4ad − 1) ≤ 2r derived from b ≥ a). Result for all 302 primes 3 ≤ r < 2000: **identical** (r, #NR, #survivors)
to `data/zl/level1_survivors.txt`; r ≤ 13 no survivors; r = 17 survivors {5, 7}; r = 19 {2, 3, 10, 13}; r = 23 {5, 14};
least surviving fraction for 17 ≤ r < 2000 is 2/11 at r = 23. With all r-conditions dropped (LOOSE=1) the survivor sets are
unchanged (the dropped data have residue 1 or 0, as checked by hand: r | c forces −a/b ≡ 1). [r ∈ [2000, 20000): see below.]
Note on label: "CERTIFIED by exhaustive exact enumeration" is fine; the claimed *dichotomy* is only about level 1 (stated).

### Lemma 4.3 (U–V factorisation)
Re-derived: with ce = a + b, 4abd = N + e, N = r^{2L−1}, (qa − pb)² = z²r^{2L}:
e·[c(p²b + q²a) + rz²] − ab[(p+q)² + 4rdz²] = (a+b)(p²b + q²a) − ab(p+q)² + erz² − (N+e)rz² = (qa − pb)² − Nrz² = 0.
So Gab = c(p²b + q²a) + rz² holds over ℚ with G := ((p+q)² + 4rdz²)/e, and G ∈ ℤ follows *without* M17D: eG ∈ ℤ, abG ∈ ℤ and
gcd(e, ab) = 1 (a prime dividing e and ab divides N = r^K, excluded by r ∤ ab). Ub, Va, UV identities: correct
(UV·ab = c²p²q²ab + rz²(cq²a + cp²b + rz²) = ab(c²p²q² + rz²G)). Size claim: correct, using c ≤ 2b/e, |qa − pb| ≤ (|p| + q)b,
r/W² = 1/N; it tacitly needs q ≥ 1 (u = −p/q in lowest terms with q > 0) — state it.
Brute force (`scripts/review_zl_lemma43.py`): 7650 random (datum, p, q) instances over 10 (r, L) pairs + 54 small-(p, q)
instances satisfying the size hypothesis: all identities hold, G always integral, U, V > 0, e ≤ 4q²a never violated.
**Defect (MINOR):** the worked check says "u = 11/9 ∈ C₇"; but 11/9 ≡ 5 (mod 17) and the box −f = −63 ≡ 226 (mod 289) ≡ 5
(mod 17), so u ∈ **C₅**. The numbers (z = 3, G = 124, U = 3, V = 9591, UV = 28773) are right.
**Verdict: SOUND** (after the C₅ typo and explicit q ≥ 1).

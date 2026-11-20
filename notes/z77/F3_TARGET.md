Result: For every level N ≥ 4, a covering tuple in orientation A must have deg M ≥ ⌈(N+1)/2⌉ in either search case; this leaves the unbounded-degree lopsided cases and does not settle Conjecture 0.2.  Label: PROVED (relative to `FF_THIRDS_CORNER.md` Lemma 1.2, Corollary 3.2, and Proposition 2.1)
Scope: This is a necessary degree restriction at x*_c in orientation A for q = 3 and A = T², not an exclusion of orientation B or of the remaining degree window. Conjecture 0.2 asserts x*_c ∈ O(3,T²); if true, this gives an uncovered point and hence no finite linear cover, but the converse is not claimed. Nothing here concerns a proof or disproof of integer ES.
Review: cross-model (Opus, `R17_F3_REVIEW.md`)
Triage: NULL
STATUS delta: none

## 1. Target and current exact reductions

The target is Conjecture 0.2 of `FUNCTIONFIELD_ES2.md` §0.2: for each c = 1, 2, the specified slice point x*_c, equal to 1 away from T and with T-adic coordinate u = 1 + cT, is not covered by any linear family; that is, x*_c ∈ O(3,T²). This pointwise claim implies that O(3,T²) is nonempty and therefore that no finite linear covering exists, by the compactness criterion in `FUNCTIONFIELD_ES2.md` §0.1. The reverse implication is not asserted: an uncovered point need not be x*_c. This is a statement about the F₃[T] model, not about ES over the integers.

There are two rigorously separated issues for a tuple of parameter s at level N = ceil(s/2) (k = 2):

1. **Exact approximation.** The Liouville lemma and exact-tuple classification in `FF_THIRDS_CORNER.md` Lemma 1.2 and Proposition 1.4 show that a tuple with E ≡ −u modulo T^(N+1) either has a large side, max(deg w₁, deg C₁+1) ≥ N+1, or is exact, w₁ = −uC₁. The exact alternative is impossible for u = 1+cT: for c=1 its leading coefficient is wrong; for c=−1 substitution at T=1 forces 0=2. Thus the balanced thirds corner, including the cyclotomic tuples with deg w₁ = deg C₁, cannot cover x*_c. This is a theorem, not a probabilistic assertion.
2. **Residual lopsided cases.** The same note, Proposition 2.1, gives a complete finite search at each fixed level. It enumerates the two orientations and the two cases by a bounded monic M; candidates are then verified against the tuple identities and covering congruence. `FF_THIRDS_CORNER.md` Proposition 5.1 further expresses orientation A, case 1 as a forced Euclidean remainder E_M and asks whether E_M divides T^(s−2)+m'w₁² for an admissible factorization M=m'w₁. This is an exact reduction, but no all-level exclusion for these divisibilities is known.

The independent algebraic normal form in `FUNCTIONFIELD_ES3.md` §2 gives the same obstruction in Case B: at x*_c, the CRT residue is forced, and the remaining gcd-part must divide L'. Its degree window only implies (N+1)/4 ≤ deg L' ≤ 2N−3. The current route bounds on the allowable lopsided patterns meet the critical exponent (the zero-excess boundary in `FF_THIRDS_CORNER.md` §7), so summing them does not give a decaying tail. The balanced-corner exclusion therefore does not, by itself, prove the conjecture.

## 2. An all-level low-degree subcase

**Lemma.** For every N ≥ 4, orientation A requires d := deg M ≥ ⌈(N+1)/2⌉ in either case of Proposition 2.1. In case 2 its window is ⌈(N+1)/2⌉ ≤ d ≤ s−N−3 ≤ N−3. This is empty for N ≤ 6, and also for N ≤ 8 if s=2N−1 (within N ≥ 4).

**Proof.** Write z = deg m' and r = deg w₁, so d = z+r and r ≤ d because w₁ | M. In case 1, Corollary 3.2 gives r ≥ N+1−d, hence 2d ≥ N+1. In case 2, the same corollary gives max(z+2r, t−1) ≥ N+1, where t = deg v = deg v₁+2. For h=deg u=1, Proposition 2.1 bounds d+deg v₁ ≤ s−N−3, and s ∈ {2N−1,2N}; thus t−1=deg v₁+1 ≤ N−2. Consequently z+2r ≥ N+1, i.e. d+r ≥ N+1, and again 2d ≥ N+1. Since deg v₁ ≥ 0, Proposition 2.1 gives the case-2 upper endpoint. Comparing it to the lower endpoint gives the stated empty windows. ∎

This is a uniform exclusion, not a bounded computation. It sharpens the case-1 observation in `FF_THIRDS_CORNER.md` Corollary 3.2 by also applying the second Liouville constraint to case 2. It does not constrain orientation B, or orientation A when deg M ≥ ceil((N+1)/2); those unbounded ranges still prevent an all-level conclusion.

## 3. Evidence and its limits

The complete level-by-level search recorded in `FF_THIRDS_CORNER.md` §2 finds no Case B tuple at x*_c for N ≤ 20 (k=2, both c); its attempted N=21 run timed out. The separate complete-range CRT search in `FUNCTIONFIELD_ES3.md` §3 excludes deg L' ≤ 13 at every level (and hence levels N ≤ 8), with its stated independent-code coverage. These are finite exclusions only. In particular, zero hits through level 20 do not imply that all later levels have zero hits, and the lottery model in `FF_THIRDS_CORNER.md` §3 is calibrated evidence, not an upper bound or proof.

The nearby result `FF_STERILE_PUSH.md` §5 establishes that the averaged union-bound route at q=3 fails even with exact tuple counts at its finite stage, whereas `FF_THIRDS_CORNER.md` §7 identifies the critical route bounds for x*_c-allowable patterns. `FF_STERILE_SMALL.md` §5.3 explains why simply extending the union calculation to the level suggested by its tail bounds is infeasible and would establish only the no-finite-cover conclusion, not pointwise sterility of x*_c.

## 4. Proof/refutation status

No proof or refutation was found. In particular, no tuple covering x*_c was found, but finite nonexistence searches do not refute the claim that one appears at a later level. Conversely, the pointwise small-height obstruction is not enough to prove x*_c uncovered: a later lopsided tuple is not ruled out.

A proof by the existing exact-search route would need a uniform argument excluding the forced remainder/divisor coincidences for every level (including case 2 and the opposite orientation). A proof of the weaker no-finite-cover statement could instead use a summable bound for the union-relevant cylinders, or a stronger exact-union/overlap argument; the present critical-exponent estimates do not supply one. These are explicit missing steps, not claims that such arguments are impossible.

## Sources

- `FUNCTIONFIELD_ES2.md` §§0.1–0.2: compactness criterion, pointwise statement of Conjecture 0.2, and the Case A/Case B reduction.
- `FF_THIRDS_CORNER.md` §§1–3, 5–7: Liouville exclusion, complete finite search, lottery calibration, and lopsided-pattern barrier.
- `FUNCTIONFIELD_ES3.md` §§1–3: exact CRT search, degree constraints, finite census, and measure-route assessment.
- `FF_STERILE_PUSH.md` §5 and `FF_STERILE_SMALL.md` §5.3: q=3 union-bound and computational limitations.

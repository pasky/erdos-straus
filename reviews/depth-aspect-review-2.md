# Hostile review R187 (reviewer 2 of 2, independent) of O178 DEPTH_ASPECT.md — Thms 3.1 and 2.5

Reviewer: side agent R187 (branch `side-agent/review-depth-2`), reviewing `side-agent/spark-depth-aspect` as merged at
commit c1cf4de8. Did not read `reviews/depth-aspect-review.md`. From-scratch scripts: `scripts/review_da2_*.py`.

## Summary verdicts

(filled in below, claim by claim)

| claim | verdict |
|---|---|
| Thm 3.1 (ℤ: sterile points on the r-generic line for all large primes r) | **SOUND** (minor repairs D1–D5; none affects the conclusion) |
| Thm 2.5 (F_q[T], q = 3^r, r ≥ 27 / q ≥ 1.3·10^16) | see §2 below |

## 1. Theorem 3.1 (integer side)

### 1.1 What I re-derived (independently)

1. **Box reduction for general r** (MORDELL17 Lemma 1.1 via the POINTWISE_MORDELL §2.1 table). I re-derived every row
   of the §2.1 table directly from the statement of ET Prop 1.9 (pp. 7–8 of `sources/elsholtz-tao-1107.1010.pdf`): at
   x(u) a congruence n ≡ ρ (mod r^k m'), r ∤ m', holds iff ρ ≡ 1 (mod m') and u ≡ ρ (mod r^k); the gcd conditions of
   I2, I3, II3, I4/II1 put r into at most one of the two moduli. The splitting into P / Q / Q⁻¹ / √Q / U / U⁻¹ uses
   only that r is odd (II3: (ad)_r | a²d; I2 with r | f: the change of variables t = (Fg+1)/(4ac) to a Q-datum).
   Nothing used r = 17. Lemma 1.3 (Jacobi reciprocity) is also valid for every odd r, but Thm 3.1 does not need it.
2. **Box values as ES data.** For a Q-datum, 4abd − 1 = Fe gives box −4a²d ≡ −a/b = −y/z for (x,y,z) = π^I(a,b,c,d);
   √Q boxes are the ≤ 2 square roots of a Q value; U boxes are −(x/y + x/z) for (x,y,z) = (iab, iac, ibc) (Lemma 2.2);
   P-data map to N-points (i, j, a', d') of Σ^II_{r^K}, K = k + α ∈ [k, 2k] — I re-expanded
   (4ni−1)(4nj−1) = 4r^K a'n + 1 ⟺ 4ija'd' = i + j + r^K a' (ET (2.15)), and since k ≥ ⌈K/2⌉ the level-k box lies in
   the ball −f mod r^{⌈K/2⌉}, f = 4y/r^K − 1. All boxes are dilation-invariant, and π^I, π^II are injective modulo
   dilation, so per level ≤ f(r^k) values for each of Q, Q⁻¹, U, U⁻¹ and ≤ 2f(r^k) for √Q: **6f(r^k)** is right, and
   one P-ball per N-point of Σ^II_{r^K} (the author's "≤ 2 per point" is a harmless factor-2 overcount).
3. **Brute-force check of 1.–2. for r = 11, 13, 17, 19, 23** (`scripts/review_da2_rgeneric.py`, from scratch). It reads
   all classes of the seven families literally off ET Prop 1.9 for every modulus M ≤ 2·10⁵ (2·10⁴ for r = 17), cuts them
   with the r-generic line, and tests each resulting box against the *predicted* boxes built only from the ES solutions
   of 4/r^k (all ordered solutions, k ≤ kmax) and the solutions of 4/r^K with r^K | y, z (K ≤ 2kmax). Results:
   0 level-0 boxes for every r; every brute-force box of level ≤ 3 (r = 11) resp. ≤ 2 (r = 13, 17, 19, 23) lies in a
   predicted box (103, 34, 30, 47, 33 boxes tested; **0 failures**). The test is not vacuous: the predicted union covers
   5/18 (r = 19) and 9/22 (r = 23) of the unit residues at level 1 and 119/342, 223/506 at level 2.
4. **The N-point bound for Σ^II.** I read ET §3 (pp. 18) and Lemma 2.8 (p. 15). The Type II bounds a ≤ b,
   b < ce ≤ 2b, n/4 < acde ≤ n are derived from (2.14), (2.15) alone (once a ≤ b is imposed), and the four regimes
   (e, ad, ac, cd ≤ n^{2/5}, from e²(ad)(ac)(cd) = (acde)² ≤ n²) use only (2.13), (2.19), (2.20), (2.21) and the divisor
   bound τ(m) ≤ m^{O(1/log log m)} with m ≤ n^{O(1)}. No coprimality and no primality of n is used. So
   #{N-points of Σ^II_n} ≪ n^{2/5 + O(1/log log n)} with **absolute, effective** constants, uniformly in n; this is the
   claimed f_II^N bound (counting all sextuples bounds the dilation classes).
5. **Measure bookkeeping.** With n = r^K, n^{C/log log n} ≤ r^{CK/log log r}; −⌈K/2⌉ ≤ −K/2; the P series is
   ≤ 2A Σ_K r^{−K(1/10 − C/log log r)} and the non-P series ≤ 6C_{1/12} Σ_k r^{−k/4} (Browning–Elsholtz), both
   → 0 as r → ∞. The non-residue units have Haar measure (r−1)/(2r). So the sterile set in the non-residue cells has
   measure ≥ (r−1)/(2r) − S(r) > 0 for r ≥ r₀. Correct.
6. **Cor 4.2 for general r.** A finite union of classes is clopen and misses x(u), hence misses a basic neighbourhood
   {x ≡ u (r^L), x ≡ 1 (Q)} with 8·3·∏_{5≤q<r} q | Q. Its primes have p ≡ 1 (24), (q/p) = (p/q) = 1 for odd q < r
   (p ≡ 1 mod 4), (2/p) = 1 (p ≡ 1 mod 8) and (r/p) = (u/r) = −1: least non-residue exactly r; infinitely many by
   Dirichlet. Correct.
7. **Novelty inside the campaign.** DISCOVERIES (H)/(I): MORDELL13E, 17, 17B, 17C, 17D all end CONDITIONAL ("no
   unconditional sterile point", DISCOVERIES l. 431, MORDELL17C l. 95); x* refuted ((F)11); TYPEI2/3 sterility of x̂_9 open
   (and is Type-I-only); POINTWISE_SIZE Thms M, C, F are statements about formal runs of programs (C is H-conditional) and
   produce no sterile point; the LORENZINI_W "sterile set" (Thm 4.2) concerns a different covering problem. MORDELL17 §2
   proved convergence of the box series at fixed r = 17 but never let r → ∞. So the claim "first proved sterile Mordell
   point other than square points" is accurate for the campaign. Literature: I know of no published statement of this
   kind (ET's remark p. 6 only gives the square obstruction, which lives in the residue cells, not the non-residue
   cells); I did not run a fresh literature search, so this part is Assessment.

### 1.2 Defects in Thm 3.1 (no FATAL, no MAJOR)

**D1 (MINOR) — Browning–Elsholtz is unchecked and makes "effectively computable r₀" depend on an unverified
constant.** Location: Thm 3.1 header ("Browning–Elsholtz f(n) ≪_ε n^{2/3+ε} for all n") and proof line "Hence the Q/U part
of S(r) is ≤ 6C_ε Σ_k …". The original (Browning–Elsholtz, Illinois J. Math. 2011) is not in `sources/`; I could only
check ET's paraphrase (p. 6: "the recent result in [8], which gives the bound f(n) ≪_ε n^{2/3+ε} for all n"), and I could
not check whether its implied constant is effective. The citation is not needed. *Repair:* (i) Q, Q⁻¹, √Q: Q-data are
N-points of Σ^I_{r^k} with r ∤ e (MORDELL17 Lemma 2.1), and ET §3's Σ^I argument (Type I bounds of Lemma 2.8, whose proof
uses only (2.1)–(2.9) and ef ≥ 5, then the four regimes e, f, cd, ac ≪ n^{3/5}) counts them by n^{3/5+O(1/log log n)} with the
same absolute effective constant as in §1.1 item 4; this gives ≤ 4·r^{k(3/5 + C/log log r)} Q-type boxes at level k. (ii) U,
U⁻¹: MORDELL17 Lemma 5.2 (proof r-general: it uses only e ≡ −1 when r | i, Lemma 5.1(ii) and the reciprocity step of
Lemma 1.3) puts every U-box meeting a non-residue cell inside a P-ball of the same centre; U⁻¹ follows by the inversion
symmetry of P (Lemma 1.1). So the U types add no measure in the non-residue cells and S(r) can omit them. Then r₀ is
effective via Nicolas–Robin alone. Alternatively keep BE and drop "effectively".

**D2 (MINOR) — normalisation of the N-point bound.** Location: proof, "f_II^N(n) ≤ n^{2/5 + C/log log n} with an absolute
(effective) C". ET's argument gives ≪ (an absolute implied constant A) and an O(1/log log n); the displayed inequality without
A holds only for n ≥ n₀ after enlarging C. Harmless here (n = r^K ≥ r ≥ r₀), but say so, or carry A (the proof's
"2Σ_K" should read "2AΣ_K"). Also "≤ 2 per point" in §3's preamble is an overcount: each N-point of Σ^II_{r^K} (a, b
ordered) gives one P-ball −f_ET mod r^{⌈K/2⌉}; the reflection is another N-point. Not wrong.

**D3 (MINOR) — the caveat paragraph is now stale / the scope sentence should be precise.** Location: Remark (5) and the §3
preamble "the proofs use only that r is an odd prime". The reduction I re-derived uses: r odd (so the 2-part sits in the
r-free modulus), the gcd conditions of Prop 1.9, (ad)_r | a²d, and the I2 change of variables. No step uses r = 17, any
residue symbol at r, or the size of r (my brute force for r = 11, 13, 17, 19, 23 agrees). Repair: replace Remark (5)'s
"a hostile R-review is still needed" by a pointer to this review and list explicitly that MORDELL17 Lemma 1.3 is not
used (already noted) and Lemma 5.2 is optional (D1).

**D4 (MINOR, presentation) — how large r₀ is.** Remark (2) says log log r₀ ≈ 20C. The binding constraint at accessible r
is not the log log loss but the level-1 terms themselves: `scripts/review_da2_level1.py` (EVIDENCE) gives
6f(r)/r + 2f_II^N(r)/r = 2.01 (r = 883), 2.12 (r = 1999), 1.07 (r = 7019), 1.11 (r = 8423), 0.58 (r = 11171); even this
single term is > 1/2 for many r ~ 10⁴. So the remark is right that the theorem says nothing at computable r; suggest adding
this one line so nobody reads Thm 3.1 as "r ≳ 10⁴".

**D5 (MINOR, wording) — "sterile".** Thm 3.1 uses sterile = "in no class of any of the seven ET Prop 1.9 families" (as in
MORDELL13E/17), whereas TYPEI2/3 use it for Type-I certificates only. The theorem body states the meaning, but the
headline "sterile Mordell points exist" in Remark (2) and any DISCOVERIES entry should keep "for the seven ET families"
attached; it says nothing about non-polynomial or growing-parameter identities (Remark (4) already notes ES is untouched).

**Verdict Thm 3.1: SOUND.** The proof is short and every imported step holds for general odd r with absolute
constants; I found no quantifier or uniformity error. Repairs D1–D5 are presentational / robustness.


# Hostile internal review: Z58_MORDELL

Reviewed `ba0f16ca..3b2691d8` (both commits), the MORDELL/common brief, all added scripts/data, and the cited prior results. **Do not accept the current conclusions unchanged.** S1's H_d criterion, S2 as explicitly quantified over H_d, G0, G's counting identity, and C1's degree assertion survive scrutiny. Several advertised consequences do not. No claim here settles ES; ES remains open.

Scope note: `mgen_nonmordell_sample_5e7_1e8.txt` was already dirty and continued growing during review. Numerical findings below use its **committed 73-row version**, not the concurrent additions. The memo and other project files were not edited.

## Findings

1. **FATAL — The advertised finite-(★)-certificate no-go confuses H_d certificates with all polynomial (★) certificates.** Locations: §0 item 1, §§4–6, especially lines 18–19, 305–306, 343–351.

   S1 is an exact theorem about **fixed (u,C), variable B** certificates (and their u/B mirrors). It does not classify certificates with **fixed (u,B), variable C**. This is not merely a terminology concern: an S1-sterile point can belong to the latter kind.

   **Explicit counterexample:** x_{11,7} is S1-sterile (7 is a quadratic non-residue mod 11), but it lies in
   `p ≡ −15 (mod 176)`, which has the polynomial certificate
   `(u,B,C) = (4,11,(p+15)/176)`.
   Indeed x_{11,7} is 1 mod 16 and 7 mod 11, exactly the CRT class 161 mod 176. Consequently **every** positive prime with
   `p ≡ 1 (mod 1680), p ≡ 7 (mod 11)`
   has this single certificate. These are genuine Mordell primes; for example p=15121 is prime and the witness is (4,11,86). This directly refutes the unqualified summary statement with M=1680. It also exhibits a finite refinement of the class-1 Mordell fibre that does shrink the remaining problem.

   **Fix:** call the property **H-sterility**, or consistently say “sterility for the fixed-(u,C) menu.” Keep S2's actual quantification over finite unions of H_d. Delete the inference to arbitrary finite (★) certificates, arbitrary polynomial identities, or “every finite refinement.” If a no-go for all polynomial certificates is wanted, separately classify the fixed-(u,B) classes and intersect the two sterile sets. C1 explicitly lists this missing family, so its conclusions cannot be fed into S1 without that additional work.

2. **MAJOR — The extension from class 1 to all six classes and the §4 fibre description are false/unsupported.** Locations: §2 final paragraphs; §4 lines 275–278; §6 “Killed as scoped theorems.”

   S1/S2 prove statements for the 1-point and classes p≡1 mod M. Bounded failures to hit points in the other five classes are not sterility theorems. The final “killed ... every Mordell class” framing is not repaired by an EVIDENCE parenthesis. Moreover, even the finite-level assertion “the Mordell lifts covered at 840ℓ are just those with p mod ℓ in the hit set” is false:

   * At L=10920, class 1801 has p mod 840=121 and p mod 13=7. R=7 is S1-sterile, but **d=455** covers it: −1801 mod 455=19 and 19 divides 114=(455+1)/4. Class 7729 gives the second extra covered lift. Thus the table's 14 covered lifts are not six copies of a two-residue hit set.
   * At L=14280, class 1201 has p mod 840=361 and p mod 17=11 (S1-hit), but is **uncovered by the H_d,d|L menu**. Conversely class 7249 (529 mod 840, 7 mod 17) is covered by d=119 although R=7 is S1-sterile.
   * At ℓ=19 there are likewise three extra covered sterile-labelled lifts and three uncovered hit-labelled lifts.

   **Fix:** preserve the correct table, remove the false fibre identification, and present the S1 status only as a proxy outside class 1. State the all-five-class problem as open. Remove the unproved `≈ τ((ℓ+1)/4)/ℓ` assertion: it has no derived asymptotic here, ignores the j-family, and its displayed divisor-function argument is not even an integer when ℓ≡1 mod 4.

3. **MAJOR — Lemma O's useful pointwise invariance is repeatedly promoted to a nonexistent equality of empirical/prime-conditional laws.** Locations: §0 item 2; §3.2; §6 and proposed FRONTIER text.

   The CRT proof is correct **with a size argument**: at a common cutoff X, every pair weight is a function of p mod 8 and odd-prime quadratic characters; all six classes fix the former and the characters at 3,5,7 identically. Higher 2-adic digits do not enter: squares modulo 2^a, a≥3, are exactly the units congruent to 1 mod 8. This addresses the 2-adic concern positively.

   But M_gen(p)=Φ(p;ε(p)) does **not** say M_gen has equal values, equal class means, or equal laws across the actual primes in the six classes. Size varies, and so does the distribution of ε(p). Ordinary equidistribution in each **fixed** progression modulo 840Q does not control the growing collection of moduli and p-dependent cutoffs in the full sum. The conclusion “every difference ... lives in X” is therefore not proved. Nor does the lemma identify every observed difference with just the quartic/cubic characters mod 5/7: those describe restrictions to the six-class group, not an attribution of individual finite-sample fluctuations.

   Minor formal issue within the statement: the vector over **all** primes q≥11 is not a sign vector at q=p, where (p/p)=0. Relevant pair factors satisfy q<p, so this is easily repaired.

   **Fix:** state a cutoff version M_gen,X and its exact independence of the choice of Mordell class **holding the other local data fixed**. An equal-law statement is valid in an explicitly defined finite/Haar local model; a prime version needs a suitably uniform averaging hypothesis and a limiting formulation. Downgrade the proposed statistical attribution to Assessment; do not call all class differences in X PROVED. Allow a zero entry or restrict the character vector to the relevant primes below X.

4. **MAJOR — The claimed statistical indistinguishability and complete avoidance are contradicted by the supplied data.** Locations: §3.4 lines 217–219 and proposed FRONTIER text.

   Recomputed the complete 158955-prime Mordell sample from the C engine and calculated moments directly. For QR versus S1-sterile QNR groups:

   | ℓ | QR mean | sterile-QNR mean | difference / descriptive SE | QR R≤4 / count | sterile-QNR R≤4 / count |
   |---|---:|---:|---:|---:|---:|
   | 11 | .1173618 | .1229591 | 25.33 | 25/79128 | 5/47900 |
   | 13 | .1211361 | .1222947 | 5.28 | 24/79284 | 6/53048 |
   | 17 | .1229063 | .1253197 | 11.64 | 16/79118 | 14/69892 |
   | 19 | .1208479 | .1220495 | 5.52 | 19/79335 | 10/53132 |
   | 23 | .1202317 | .1212823 | 4.75 | 22/79386 | 8/50658 |

   Here descriptive SE is sqrt(s_QR²/n_QR+s_sterile²/n_sterile); this is not a claim of a rigorous random-prime sampling law. Nonetheless, “statistically indistinguishable” has neither a specified equivalence margin nor support, and is very far from the usual meaning at ℓ=11. The low-R rates also cannot simply be declared equal.

   “Avoid ... completely” and “hit classes carry no low-R primes” contradict the table's own **one** exception: **p=21106849, R(p)=4, p mod 19=15**. The grouping proxy can still be useful; its effect is not an equality theorem.

   **Fix:** say “sterile-labelled groups have substantially smaller means than hit-labelled groups, but differ measurably from QR groups.” Report effect sizes and the exception. If equality of low-tail rates is important, test a prespecified comparison rather than inferring it from overlapping mean ranges. The six Mordell class SDs are .03764–.04231 and descriptive SEs .000231–.000260, so §3.2's hypothetical SD bound can be replaced by actual measurements.

5. **MAJOR — The 22-class set is an incomplete-menu avoidance set, not the (★)-uncovered or intrinsically hard set.** Locations: §0 item 3; §3.4; proposed FRONTIER text and bottom line.

   The 22-class enumeration is correct for **H_d with d|840**. But eleven of these classes are 5 mod 8, and **every positive integer p≡5 mod 8 already has** `(u,B,C)=(1,2,(p+3)/8)`. This elementary family is even cited in prior Z56_FAMTRY Prop 2.1. Adding just that legitimate polynomial (★) family reduces the 22 survivors to **11**. Thus half of the advertised hard set is already proved positive. The G*-zeros 37 and 157 are examples where membership in this 22-class set does not mean (★)-failure.

   In addition, S1-sterility is a property of a special *whole profinite point*, not an independent property of a residue that can be combined freely across primes. The memo's own (2 mod 5,4 mod 7) exception, covered by d=35, demonstrates interactions between individually sterile-labelled coordinates.

   **Fix:** name the set `A_840^H`, “uncovered by the divisor-of-840 H-menu.” Distinguish it from a true zero-admissible set and from empirical low-count classes. State that all (★)-zeros are in its 1-mod-8 half. Replace the causal/exhaustive language “hardness is cut out by sterility” with a bounded empirical association, and explicitly discuss the joint-coordinate exceptions. This is not remedied just by attaching EVIDENCE to an overbroad noun.

6. **MAJOR — C1's degree theorem is sound, but its certificate-validity clause needs missing hypotheses and its no-go is overextended.** Locations: §0 item 5; §5; §6.

   The degree case analysis is complete: two positive degrees with total >2 force the product to dominate U+B; total 2 with two degree-one factors contradicts irreducibility; every remaining degree pattern has two zeros. No counterexample to this algebraic assertion was found.

   However U,B,C are allowed to lie in Q[x,y], with arbitrary nonzero rational constants. The subsequent integer congruences and “valid iff” claim do not follow as stated. For example, for f=x²+840y²,
   `U=C=−1, B=(f−1)/3`
   satisfies the identity. At (x,y)=(31,1), f=1801≡1 mod 3 satisfies the displayed congruence, but the triple is not a positive-integer certificate. Nonintegral fixed coordinates give an additional obstruction; `U=1/2, C=1, B=f+1/2` is an identity but never an integer certificate.

   More fundamentally, C1 treats **global polynomial identities**, not all algebraic uses of the representation. It neither excludes rational-function formulas on selected domains, implicit algebraic constructions, nor rules restricted to prime-representing points. “Two non-polynomial uses remain,” “algebraic use ... killed,” and “can therefore enter only through ... B2 or Frobenius” are unsupported exhaustiveness claims.

   **Fix:** keep the polynomial degree theorem. For its arithmetic corollary assume the two fixed coordinates are positive integers and f(x,y)>0; otherwise say there may be no valid integer points. Restrict the no-go to fixed global polynomial triples (or finite menus of them). Do not declare all other algebraic approaches dead or all possible arithmetic rules equivalent to B2. Also observe finding 1 when using S1 to discuss C1's congruence families.

7. **MAJOR — The NONCONG_LIFTS comparison overlooks its explicit correction about fixed slices versus full polynomial families.** Locations: §2 Novelty and §4 discussion of ES refinements.

   NONCONG_LIFTS Thm 2.6 proves the R=2 exclusion for **fixed-slice witness classes**, not the full ET polynomial menu. Its R267 repair at the end of §5 explicitly states that for k=4,
   `x_{11,2} ∈ {n ≡ 79 (mod 143)}`.
   Thus this point is **not sterile for the full ES menu**. Invoking it as the sterile-point explanation for the ES-menu refinement experiment is misleading. The bounded fact that each tested refinement leaves some lift uncovered is correct, but does not prove any particular limiting point survives all ES identities.

   **Fix:** write “fixed-slice ES witness classes” in the novelty comparison, quote the R267 limitation, and separate the H-menu theorem from the full ES/POINTWISE_MORDELL programme. HCF's <(ℓ−1)/3 bound and FAMTRY's class-1 obstruction are credited accurately. The exact H-point criterion is a plausible small campaign increment; the class-1 hardness and full-residue secondary effects are already substantially in RESIDUE_HARDNESS §§1–3, so credit those as prior explanation, not newly established causal structure.

8. **MINOR — Several numerical statements do not match their committed data.** Locations: §§0, 2, 3.2–3.5.

   * **Non-Mordell mean:** the weighted mean R/L² from `classstats_1e8.txt` is **.1662258**, not .164. The all-class average is approximately .164; it must not be labelled “off 𝔐.” Mordell mean is .1246240.
   * **Non-Mordell M_gen sample:** the committed first 32 rows have mean **.1554042**, not .154. All committed 73 rows have mean **.1533237**, also not .154 rounded to three decimals. None is below c_V. Freeze a sample before quoting its size and mean; do not mix an earlier running mean with “first 32.”
   * **Marginal low counts:** the table says “all primes p≡1 mod 4.” With that population, p=5 contributes an extra R≤4 observation: mod 3 the counts are **268/6**, not 268/5; mod 7 the count for residue 5 is **4**, not 3. If the intended population is unit primes modulo 840 (p>7), state it; the existing table then matches.
   * **Other-five-class fractions:** `sterile2_d3e4.txt` has minimum **2/5**, maximum **7/8** (ℓ=17), not a range “between 7/14 and 24/29.” 24/29 is the ℓ=59 value, not the overall maximum.
   * **Hit-group sample sizes:** 158955 is the size of the entire Mordell sample, not the size satisfying a hit condition for a given ℓ. The latter counts are 31927, 26623, 9945, 26488, 28911, as correctly displayed in §3.4.

   **Fix:** correct the numbers and explicitly name the population/window for each count. The other displayed class means, zero-class counts, table group ranges, and covering-table counts reproduce.

9. **MINOR — S1's converse needs one short integrality justification; the bounded criterion implementation should expose its exact j bound.** Location: §2 S1 statement and proof; `z58_mordell_sterile2.py:30–40`, duplicated in bymod.

   The theorem asserts that t=(4CR+1)/ℓ is automatically integral under the j-family divisibilities, but the proof derives the criterion from an already-integral t and does not explicitly prove that assertion in reverse. It is true:

   From 4CD_j=ℓ+j+1, `(j+1)(4CR+1)=ℓ(4Cj−1)`. If j+1=hℓ and δ=ℓ−R≥1, this would imply `4C(hδ−1)=h+1` with hδ>1. For δ=1, h≥2, the left side is at least 4(h−1)>h+1; for δ≥2 it is at least 8h−4>h+1. Hence ℓ∤j+1, so t is integral. Then `m=4C−t=(4C+1)/(j+1)>0`, and the reduction's converse applies.

   Also, `4D_j≤ℓ+j+1` gives the exact finite bound
   `j≤floor((ℓ+4R+1)/(4(ℓ−R)−1))`.
   This proves the scripts' looser `4ℓ+10` cutoff is safe, rather than leaving it looking heuristic.

   **Fix:** add these two lines to the proof/check documentation; preferably use the exact bound in the implementations. Explicitly require m>0 in the reduction converse. The step-4 exclusion of a≥2, including C=1 and ℓ=3, and the integer rounding in step 6 are correct.

10. **MINOR — G's mean-value commentary needs an averaging domain; τ(N)≍log N is not a pointwise fact.** Location: §3.1 after Lemma G.

    G's divisor-character count, injectivity of k↦−k mod d, and S_q(N)≥0 are correct. The unrestricted mean of S_q(N) is L(1,χ_q). But **in this lemma's d-sequence**, N=(d+1)/4 lies in the particular square class 4⁻¹ mod q. On a fixed nonzero square class modulo q, the conditional mean is **2L(1,χ_q)**, not L(1,χ_q). One sees the two contributions from the principal and χ_q twists of the convolution 1*χ_q; S_q(N) is identically zero on non-residue classes. Moreover τ(N) can be 2 at prime N, so it is only its average that grows like log N.

    **Fix:** either delete the mean-value aside or specify the unrestricted versus conditioned averages and give a short derivation. Keep “relative 1/log effect” as an averaged interpretation, not a pointwise bound. No change to Lemmas G0/G themselves is needed.

11. **MINOR — The falsifier table is mostly honest about having no positivity mechanism, but its M2 uniqueness claims are too strong.** Location: §0′ F1/F3.

    It is appropriate to say the no-go strengthens on the C-even subfamily, and to mark F4 inapplicable to a nonexistent M2 rule. The four R8 least-non-residue lookups and the nine (★)-zero lookups all check out. “No HOT LEAD” is the correct verdict.

    However “odd squares in 𝔐-classes have representations with y≠0” needs **some**, not a universal reading: 11²=121 is in 𝔐 and cannot have a nonzero-y representation. Also uniqueness of the representation is not a primality characterization, and “primality could only enter through uniqueness” is not justified. For example the non-square composite
    `122089 = 11²·1009 ≡ 289 (mod 840)`
    has exactly one positive representation `143²+840·11²` (hence the same four sign variants as a prime). This is cheaply checked by y≤12; inert scaling also explains it.

    **Fix:** use an existential square example, and say uniqueness is one possible property to investigate, not the only possible use of primality or a sufficient composite screen. Re-scope M1 in this table as in finding 1. The table's numerical consistency checks are not independent evidence of an exhaustive hardness mechanism.

12. **MINOR — Reproduction/provenance and formal wording should be tightened before CERTIFIED/frontier use.** Locations: notation/Q1, §§2, 3.5, 7, 8; cover script header.

    * The sample files have no headers specifying columns, generator, seed, selection index, or snapshot size. `§3.5` says “see file for the count completed,” but the file has no such record. Store a fixed input list and sampling command/seed; put column definitions in a README or headers.
    * The cover script claims symbolic verification by `z58_mordell_identities.py`, which does not exist in the tracked tree. Its five ES families are algebraically consistent with their displayed parametrizations, but do not cite a nonexistent verification artifact.
    * The refine reproduction command says `python scripts/z58_mordell_refine.py ...` “run from scripts/,” which doubles the directory. From the repository root use `uv run --with numpy python scripts/z58_mordell_refine.py ...`.
    * The cited sterile1 “table” does not actually print the zero-prime lookups. Add a small reproducible lookup command or record the explicit prime/least-NR/residue triples.
    * Ordinary diagonal primes are not elements of Zhat^×. Say “the closure in Zhat, intersected with Zhat^×,” or use the corresponding unit cylinder. The compactness equivalence for prime coverage should concern **sufficiently large primes**: passing to the unit part of a closure discards possible isolated prime exceptions. S2's explicit neighbourhood/Dirichlet proof is unaffected.
    * The header says “internally reviewed” while §8 is TODO. After repairs, record this review and which findings were addressed; a review request is not a completed review.

    **Fix:** make the artifacts genuinely reproducible and keep CERTIFIED confined to bounded calculations, PROVED confined to the actual scoped statements, and Assessment for causal/statistical interpretation.

## Proof audit and recomputation record

All new computations used `ulimit -v 4000000` and `timeout` at most 600 seconds. No dense Cartesian-product geometry/large-array computation was used.

* **S1 steps 1–3:** a=0 contradiction, both modular reductions, invertibility in the converse, and the two possibilities for m are correct. **Step 4:** `2t+1≤16C/9+11/9<4C` and `t<4C−1` hold even at ℓ=3,C=1. **Step 5:** the direct case and forward j-family algebra are correct; the missing reverse integrality argument is supplied in finding 9. **Step 6:** integrality gives t+1≤2C, so the small-R exclusion is correct. **S2:** clopen avoidance plus Dirichlet is valid for finite H_d unions; compactness is not needed for that one direction.
* Re-ran `uv run --with sympy python scripts/z58_mordell_sterile2.py 30000 60`: **byte-identical output, zero mismatches**. Independently used the derived exact j bound for all odd primes ℓ<1000: integrality, no small-R hits, and no quadratic-residue hits all passed. Hit counts for ℓ=11,…,59 are exactly **2,2,1,3,4,3,4,3,2,3,6,5,5**.
* Rebuilt/reran `z58_mordell_classstats.c` at **10^7 and 10^8**: both committed classstats files reproduce byte-for-byte. Re-ran bymod on the new dump: byte-identical to `bymod_1e7_1e8.txt`. The C loop bounds and the ordered-triple interpretation are correct for these runs. Computed the moments in finding 4 from the new prime dump rather than the rounded aggregate file.
* Independently reran the screen enumerator to **9·10^6**: the 14 prime zeros and the 285 non-square composite zeros through 7999801 match the screen lists exactly. Verified all 14 prime-zero residues and all 38 G*-zero residues lie in the stated 22-class H-menu set. Recomputed the least-NR lookups: Mordell (★) zeros have `(p;n_p,R)` = (5569;13,5), (9601;13,7), (83449;13,2), (102001;23,19), (712321;23,11), (1724209;13,6), (1726201;19,13), (5212561;11,2), (8813281;17,5). The four Mordell R8 zeros give **(23,10),(19,3),(29,10),(13,5)** as claimed.
* Recomputed the complete §4 covering table. ES survivors are **6,34,40,52**; the nonsquares at 9240 are exactly **2041,2521,3361,5161**. At 10920 they are **2641,3361,4201,9601**; at 14280 **2521,5209,10921,11089**. H-menu Mordell survivors are **6,48,58,88,90,108**, with nonsquare counts **0,18,22,40,36,42**. Every listed one-prime ES refinement still leaves at least one lift of each of the four base nonsquare classes. These are bounded menu results, not sterile-point proofs.
* Reaggregated `mgen_zeros.txt`: all **9** Mordell (★) zeros have ratio in **[.0838918,.1149746]**, all below c_V; **18/20** Mordell G*-zeros are below, with precisely the two stated exceptions **1105441,564661441**. Of the **14** non-Mordell G*-zeros above 1000, **13** are above c_V, exception **23929**. The 34-row union count is correct. These certify vacuity **at these zeros**, not the full proposed explanation of L6.
* The 96-row Mordell sample has min/max/mean **.1085683/.1395680/.1269714**, with **44/96=45.833%** below c_V. These quoted rounded numbers are correct. Independently reran the M_gen engine on **5569,23929,1105441,8813281,50073769,52597249**; every printed column matches its stored row. I did not recompute every large-prime M_gen row or independently rescan the R8/G* zero censuses to 10^10.
* **G0:** reciprocity is valid since p≡1 mod 4 and p∈H_d implies gcd(p,d)=1; hence a nonsquare prime factor of d exists. On 𝔐, 3,5,7 are residues and 2 is a residue too, yielding d≥n_p≥11. **G:** the exact split and nonnegativity check out, subject only to the averaging correction above.
* **C1:** degree analysis complete, as detailed in finding 6. Independently checked all **2370** Mordell primes ≤10^6 have exactly one positive x²+840y² representation. Enumeration of primitive reduced forms of discriminant −3360 gives **16**, all ambiguous, consistent with the cited idoneal fact. This does not validate the extrapolation from polynomial identities to every algebraic/arithmetic use.

**Recommendation:** retain the exact H-point theorem and the bounded data, correct the menu distinction first, and rewrite the headline/verdict as a narrowly scoped obstruction plus descriptive statistics. Do not propagate the current proposed FRONTIER text.

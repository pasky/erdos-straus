# Internal hostile review of Z66_IE1.md

## Verdict: ACCEPT-WITH-FIXES

The central new arguments are salvageable and substantial: the precisely stated compactness theorem L, the four-square gap certificate K, the no-retraction argument G (relative to the explicitly disclosed Wilmers input), and the model E survive scrutiny. **The memo must not be circulated unchanged.** There is a reversed literature theorem, a missing hypothesis making Definition 3.1/Lemma 3.2 literally false, and several materially overstated summaries. I found no fatal obstruction to the repaired main results.

No model/provider/auth/quota error occurred. An attempted fresh download of Smith's PDF returned HTML rather than a PDF; I used the supplied complete text, including the proofs preceding Theorem 3.11 and the open questions, rather than trusting its damaged formula OCR.

## Issues and concrete fixes

1. **MAJOR — Missing class-membership hypothesis makes arc points vacuous off the class.**
   **Location:** §3 Definition 3.1, lines 156–157; Lemma 3.2, line 167; Theorem K, lines 214–216.
   The definition quantifies over subrings of M containing `(n-r)/q` without first requiring this element to belong to M. If `n` is not congruent to `r mod q`, there are no such subrings, so the condition is vacuous. For example, in M = ℤ take n = 2 and the class 1 mod 2. The definition calls 2 an arc point, but u = B = C = 1 gives ES★(2). Theorem L already includes the missing congruence hypothesis, so its central equivalence is not damaged.
   **Fix:** Define an arc point for the class to mean **n > 0 and n ≡ r (mod q), and** the stated component condition. Specify q ≥ 1 and standard integer r, q. Thereafter say “for any class containing n” where appropriate.

2. **MAJOR — Smith Theorem 3.11 is quoted backwards; §8's extra residue-field obstruction is unsupported.**
   **Location:** §2 Smith bullet, line 118; §8, lines 431–436; the same reversed quotation in `lit_ie1.md` §8.
   For distinct odd primes p, q with p standard, Smith proves
   `(p/q) = 1 ⇒ (q/p) = 1`, except that the conclusion is −1 when both primes are 3 mod 4. The memo instead asserts `(q/p) = 1 ⇒ (p/q) = 1`. This is not an innocent interchange when only p is standard. The direction is independently recoverable from Lemma 3.7: m a nonresidue modulo standard p implies p a nonresidue modulo m; take its contrapositive. Lemmas 3.8–3.10 give the other congruence cases. Smith's subsequent inference from “q has no quadratic nonresidues” to congruence restrictions on q, and Question 5.2 asking about the converse, confirm the direction.
   Therefore square-mimicking `(n/ℓ) = 1` does **not** supply `(ℓ/n) = 1` by this theorem. The claimed √ℓ in every IE₁ prime residue field and the application of L65 Proposition 4.2 do not follow.
   **Fix:** Correct the quotation, include “distinct odd,” and delete that §8 residue-field conclusion unless another source proves it. Retain the independent Bezout exclusion of polynomial-type models. Also retain the stronger Count₂ theory's full QR result: it is unaffected. Correct the research evidence file separately; this review did not edit it.

3. **MAJOR — F1 drops the essential clopen hypothesis.**
   **Location:** §0 F1 row, line 44.
   “T proves no existential statement whose real solutions avoid every odd-square integer point” is false as a characterization. IOpen already proves, at nonsquare positive primes, the existential relation `s ≥ 0 ∧ s² < n < (s+1)²`. It has no integer point at any square, but its real locus is not clopen in the ambient variety. U64 nevertheless supplies IOpen arc countermodels. The nonvanishing multipliers in K are precisely what repairs this defect.
   **Fix:** Restore “clopen in the real zero set of its displayed equations over t > 0,” and the uniform prime/class/tail qualification from L(b). Do not reduce “arc certificate” to mere integer nonsolvability at squares.

4. **MAJOR — The headline and concluding method claims exceed Theorem L/K and obscure L65's explicit distinction.**
   **Location:** title; §3 Readings, lines 205–210; §4 following K.1, lines 238–240; §7 line 419; §9 lines 451–453, 485–501, 505–510; O4″.
   L characterizes **odd-square component-landing countermodels**, not all uses of analytic arcs, all integer-landing arguments, or all unprovability methods. L65 §5.5 explicitly corrected the inference that arc refutations must be pointwise square landings: its Proposition 5.5/Theorem D also use polynomial nonsolvability along a whole progression. K does not rule out every such mechanism. Nor does K imply that a failure is “invisible at every integer landing point”: it rules out the all-finite-subrings odd-square component property; it says nothing comparable about all nonsquare integer points.
   **Fix:** Consistently name the method “odd-square component landing” (including U64/L65's square-landing constructions). Replace “the only known unprovability technique ... exactly” by the actual scoped equivalence. Replace “invisible at every integer landing point” by “not an odd-square component-landing counterexample.” Preserve L65 Theorem D as a separate polynomial-solvability mechanism. The narrower conclusion that K kills every U64 Proposition 6.2 square arc is correct.

5. **MAJOR — The literature barrier conflates Π₁ statements with arbitrary number theory and contradicts its own evidence.**
   **Location:** §2 final literature bullet, lines 135–136; K.2, lines 244–250; associated summary/frontier claims.
   “No independence result for a concrete number-theoretic statement is known” is too broad. The evidence file itself gives IE₁ ⊬ Pell, from D'Aquino's Pell ⇔ exp over IE₁ and IΔ₀ ⊬ exp. This is a concrete true number-theoretic Π₂ principle, even if its unprovability is deduced rather than stated in the abstract. Also, unboundedness of primes is normally Π₂, and MRDP is a formalization scheme, not simply another natural true Π₁ sentence “of this kind.” Historical open-problem quotations do not prove a present-day exhaustive nonexistence claim.
   **Fix:** Say “our search found no natural unrelativized number-theoretic **Π₁** independence result of the required kind,” and distinguish this from known Π₂ examples such as Pell. Use Bertrand's postulate, rather than unboundedness of primes, as the bounded prime-existence Π₁ candidate. State MRDP's separate status explicitly. Keep the absence-of-known-results claim labelled Assessment/NOT FOUND.

6. **MAJOR — ES truth is not a necessary condition for unprovability.**
   **Location:** §7, “What ‘IΔ₀ + exp ⊬ ES’ would require,” lines 416–420.
   The first bullet is “ES true.” Unprovability alone does not require truth. If ES has a standard counterexample, EFA can verify that bounded failure and hence cannot prove ES (assuming consistency). The intended interesting case is independence conditional on standard truth.
   **Fix:** Change the heading to “If ES is true, what an EFA countermodel would require.” Say that the *existential sentence asserting an ES counterexample* would then be a false Σ₁ sentence true in the nonstandard model. Apply K specifically to the campaign's nonsquare prime counterexample, not to an unspecified arbitrary n.

7. **MINOR — The negative-Pell formula is not an arc certificate as displayed.**
   **Location:** Remark K.3, lines 263–265.
   `{x²+1 = ty²}` has integer points `(t,x,y) = (1,0,±1)`. Definition 3.1 defines certificates absolutely, not relative to a residue class. Saying “for the class 121 mod 840” does not remove these points from the displayed set.
   **Fix:** Display `x²+1 = ty² ∧ t = r+qv` for a class containing no 1, with v an additional coordinate. Its entire real locus over t > 0 is clopen, and its integer square points would force t = 1, excluded by the congruence. The Legendre descent argument itself is sound with p a positive prime ≡ 1 mod 4 and a minimal **nontrivial** positive Pell solution; state those hypotheses explicitly in the first bullet.

8. **MINOR — The “two squares” necessary-feature sentence is vacuous.**
   **Location:** K.2, lines 248–250.
   Every model of the base arithmetic already has an element, 8, modulo which −1 is not a sum of two squares. This cannot describe a difficult new residue-field requirement. K's genuine conclusion is failure of P₄ (indeed each fixed P_k), not merely failure of P₂.
   **Fix:** Replace “two” by “four” and say “some **nonstandard** positive modulus.” Such a modulus must be nonstandard since every standard instance of P₄ has standard witnesses. The comparison with formally real residue fields can then remain as a sufficient example, not an equivalence.

9. **MINOR — F4 omits ‘nonstandard’ and is false for standard primes.**
   **Location:** §0 F4 row, line 47.
   A prime of M_E need not have constant term ±1: the standard prime 2 is a counterexample, and all standard primes are explicitly listed in E(iii).
   **Fix:** Say “a **nonstandard** prime of M_E has n(0) = ±1.” Also make explicit that congruence modulo “every k” throughout the model statements means every positive **standard** integer k.

10. **MINOR — E cites G.1(b) outside its stated hypotheses.**
    **Location:** §6 “What M_E does not satisfy,” lines 389–390.
    G.1 is stated for models of IOpen, whereas M_E deliberately fails IOpen. Thus that citation alone cannot justify failure of every P_k in M_E.
    **Fix:** Strengthen G.1(b)'s hypothesis to a nonstandard discretely ordered ring (its proof already works there), or give the direct argument: apply P_k to the positive element x and evaluate `xy = 1+Σz_i²` at x = 0. No change to E's conclusion is needed.

11. **MINOR — Q2's syntactic explanations and proof-source label need tightening.**
    **Location:** results paragraph line 35; §7 lines 406–412.
    “Every Π₁ sentence is ∀Δ₀, so all its quantifiers are already bounded” forgets its outer unbounded universal quantifiers. Moreover the stronger claim of an ES-like bounded existential polynomial presentation uses MRDP, not just HP. The displayed presentation still has a disjunction and a tuple of universal variables, so “exactly the syntactic shape of ES” is unnecessarily literal.
    **Fix:** Say “the matrix is bounded.” Label the polynomial-presentation argument as relying on formalized MRDP (Dimitracopoulos survey Theorem 4 confirms the cited result). If a single polynomial is intended, replace the disjunction by
    `(P⁺−P⁻−w−1)(P⁻−P⁺−w−1)=0`, with `0 ≤ w ≤ P⁺+P⁻`.
    This gives the relevant bounded-existential Diophantine type, not the special ES equation. The negative answer to Q2 is correct.

## Independent checks and accepted proof steps

### L and the transfer machinery

- Read **all 533 lines** of Z66, U64 Theorems A/A′/A″, Lemmas 2.3–2.4 and Proposition 6.2, and L65's requested lemmas/theorems/propositions, including the actual warning in §5.5 preceding Theorem D.
- Interpreted R(M) correctly as the ordered real closure of **Frac(M)**. A discretely ordered ring is an ordered domain, so the tautological point makes sense without embedding M in ℝ.
- Checked finite generation of the relation ideal over ℤ; finitely many semialgebraic components; definability over ℝ_alg; elimination of each algebraic parameter using its isolating definition and RCF quantifier elimination. Thus integer-coefficient quantifier-free component formulas are legitimate. Over a non-Archimedean field the relevant notion is **semialgebraic** connectedness, as the memo says, not arbitrary topological connectedness. The exact BCR theorem-number attribution was not independently reverified; the mathematical facts used are standard and correct.
- Checked quantifier-free absoluteness between M and R(M), transfer of the finite partition, and transfer of existential intersection with S. The (★) positive locus really is relatively clopen over t > 0: at a finite boundary limit, `4C ≥ 1/u+1/B` prevents u or B from vanishing, and the original equation then prevents C from vanishing. Analyticity is not needed for this component argument.
- Checked L(a)⇒(b) by pulling back the clopen certificate to the relation variety, including the residue coordinate. Checked L(b)⇒(a) by finite satisfiability/compactness and choosing the offending component as a certificate. This works for arbitrary T ⊇ IOpen, with the class-membership repair above; no effective enumeration of certificates is needed.
- The “arc point” property is independent of changing a generating tuple: an integer point of the relation variety is a homomorphism A→ℤ, and polynomial coordinate changes preserve the component formulation. This could use a sentence of explanation but is not a gap.
- U64's **square-landing** arcs produce these points: enlarge the finite set to include the finitely many polynomials in the component formula if needed; their eventual signs match M, and connectedness carries the integer endpoint into the same real component. U64's extra gcd requirements are unnecessary for (★). Its GCD Type I/II systems also have relatively closed positive loci over t > 0 and the cited odd-square obstruction/descent.

### K, the literature chain, and L65

- Checked that IOpen provides a nonnegative square-root floor, both gaps are ≥ 1 at nonsquares, and P_k supplies the two multiplier identities. On the real equation variety neither gap can vanish; their positive-sign locus is clopen. At an integer point the two strict inequalities force s ≥ 0 and place t strictly between consecutive squares. Thus K is correct after fixing Definition 3.1.
- Independently enumerated square-sum residues modulo 8 for k = 1,2,3,4. The respective sets are `{0,1,4}`, `{0,1,2,4,5}`, `{0,1,2,3,4,5,6}`, and all residues. P₁–P₃ are false; Lag ⇒ P₄ uses x−1 and y=1. The Π₁ presentation uses `0 ≤ z_i < x` and `1 ≤ y ≤ kx`, via division with remainder, available over IOpen.
- Ran `pdftotext` on **both requested PDFs**. Jeřábek's remark immediately after Theorem 5.7 really says Lag is provable in IΔ₀ + Count₂(Δ₀), and credits the iWPHP proof using only Legendre-symbol multiplicativity. His printed `iWPHP(IΔ₀)` notation in that remark should be understood in the surrounding Δ₀-definability context, not as a new axiom scheme.
- Checked the WPHP forms, not just their names: Jeřábek defines injective WPHP as no injection from 2a into a; Bovenzi–D'Aquino's Δ₀-WPHP excludes injections from (1+ε)z into z and explicitly reports its provability from Ω₁. Taking ε=1 gives the needed injective scheme. The Ω₁ and exp rows of K.1 therefore follow. The quoted Bovenzi–D'Aquino Legendre theorem has nonzero, mixed-sign, square-free, pairwise coprime coefficients, as the evidence file records.
- **The claimed correction to L65 is fair if phrased as overturning an Assessment, not refuting a theorem.** L65 Proposition 5.2 only establishes compatibility of individual witness relations at selected squares, explicitly leaves joint arcs open, and labels its optimism an Assessment. K supplies exactly the missing joint obstruction, using floors and the two gaps. It does not invalidate Proposition 5.2 or settle Bez/PB/TS/E(−1)/QR_std.

### G and E

- Read D'Aquino's supplied full text. The Wilmers PA-initial-segment quotation appears on printed p.87; McAloon's analogous result appears on p.85. G accurately discloses that it relies on these quotations rather than an inspected original theorem.
- Checked all of G1 assuming **unital** ring homomorphisms (state this convention explicitly): numeral division gives residues, kernel equals ⋂k kM, the kernel is divisible and a ℚ-vector space, and a Bezout combination of two kernel elements cannot be a unit.
- Checked I∪−I is a subring because the PA cut is closed under the inherited addition and multiplication; x−e(x) remains in it. In PA, maximal 2-power and 3-power divisors exist; their complementary factors are respectively odd and prime to 3. Their e-images force both power divisors into the kernel; any common divisor >1 would force 3|2. Bezout then contradicts G1(c). Alternatively, restrict e to the PA cut and use Lag there plus G.1(a), which gives an even shorter proof. Both arguments are valid.
- Checked G.1(a)'s positivity/monotonicity argument and G.1(b)'s evaluation contradiction. Neither assumes that a ring homomorphism is order-preserving; positivity is derived where needed.
- Recomputed E's Bezout ideal argument in **both j=0 and j≥1 cases**. The positive rational generator γ of αℤ+βℤ exists even if one of α,β is zero. For j=0 it is integral; for j≥1 γh has zero constant term. The quotients f′/γ and g′/γ have integral constants, and the correcting coefficients a₀+xr₁, b₀+xs₁ lie in R. No coefficient-membership hole was found.
- Checked the rational-function integer-part argument, including negative infinitesimal remainder and nonintegral rational constant. Read Glivická–Glivický's **complete** paper at `/tmp/z66_ie1_lit1/arxiv_1701.02001.txt`: Theorem 3 and Corollary 6 are the claimed results. E really satisfies their IOpenLin, not merely a misleading weaker ring analogue. Its nonnegative part satisfies Robinson Q: successor/predecessor, recursion, and the order/difference axioms follow from the discretely ordered ring. The source's syntactic definition of linear formulas is somewhat narrower in presentation; the floor argument supplies the stated induction.
- Checked the full classification of irreducibles, PB quotient injection and surjection, PD's three constant-term cases, and universal **ring-language** specialization. In (v), “do not all vanish” should preferably read “none vanishes” (avoid the roots of the product); the required stronger choice is available.
- Checked the positively closed transfer for T1 and other stated nonexistence systems; positivity of f(s) on [0,∞) permits the evaluation path to 0. The (★) contradiction at n(0)=1 and the ES contradiction `4 ≤ 3` both work. The cyclotomic polynomials x^(2^j)+1 are irreducible and cofinal by degree. Fractional Euclidean division does not provide a floor for √x, so failure of eIOpen is consistent with the other properties.
- The phrase “both halves ... fail separately” should be understood as the two established negative results, IOpen ⊬ MS and IOpenLin+Bez ⊬ MS. The memo has **not** proved eIOpen+Bez ⊬ MS. “First open combination” is an Assessment about this particular displayed ladder, not a theorem of minimality among all theories.

### Q2, computational replay, and scope of verification

- Checked HP V.5.26, V.5.29, V.5.34 and the surrounding conservativity discussion against the archived chapter text in `/tmp/z66_ie1_lit2/hajek_pudlak_chV_jina.md`. The quoted theorem numbers and directions are right. HP explicitly calls the PH/LinH connection only apparent/formal and says no relation is proved; the memo must not strengthen this. The conditional conservativity implication in §7 is correct: a Π₁ ES sentence provable in Ω₁ but not in IΔ₀ would separate them.
- Checked the Dimitracopoulos survey's formalized-MRDP Theorem 4 and Lag Theorem 11 in the existing OCR. The Con(Q) argument and its bounded Diophantine reformulation establish Q2's negative answer, subject to the wording repairs above. Historical sources establish what was open then; current universal “none known” assertions remain literature-search assessments.
- Read the entire K1 script and its saved output. Exact Fraction arithmetic, long division, membership by integral constant term, leading-coefficient positivity, and both rearranged equations are correct. `Y < X` is merely a lexicographic symmetry reduction, which is legitimate; it is not being used as the model order.
- Replayed `python3 scripts/z66_ie1_k1_search.py 2 2 2 4` through `uv run --no-project`, under `timeout 600` and `ulimit -v 4000000`, piping to `diff -u data/z66/ie1/k1_search.txt -`: **exit 0, no differences**. This reproduces 220 positive box elements, zero hits at the three protected targets, and the positive controls. The script bounds the two enumerated variables, solves for the third without a box bound, and caps reported positive hits at five; describe it that way rather than implying that every output count is a complete solution count.
- Independently verified the positive controls algebraically: `4·1·(8x/3+2)·1−1−(8x/3+2)=8x+5`; and the triple `((x+2)/2,x+2,x+2)` sums reciprocally to `4/(x+2)`.

Only this review file was written. No memo, evidence file, or script was changed.

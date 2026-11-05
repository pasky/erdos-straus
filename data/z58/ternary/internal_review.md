# Internal hostile review: z58 TERNARY

Reviewed range: `6e3260a9..0e1ebdae` (all five commits, all 12 changed files). Memo line references refer to `0e1ebdae`. This review does not edit the memo. **ES remains OPEN.**

## Decision

**Request changes. No FATAL counterexample found to the scoped genus-main-term obstruction, Theorem F(i),(iii), relative to its standard inputs.** The local-density argument and separation of the order-ℓ Eisenstein/unary contributions from the order-√ℓ cuspidal contributions survive hostile checking. Corollary F1's arithmetic is correct.

However, several **MAJOR** claims around that theorem are wrong or insufficiently scoped: the Waldspurger twist omits the nebentypus, the screen suppresses possibly zero local factors, the claimed necessary unbounded complexity contradicts the cited POINTWISE result, Remark F2 extends unit-square invariance to nonunits, and two literal formulations in the dictionary/unary conclusion require repair. These affect the falsifier table, verdict and proposed FRONTIER text, not just background prose. The numerical tables reproduce; reproduction does not validate these inferences.

## Findings

### MAJOR 1 — Wrong general Waldspurger twist; the latest citation fix still does not cover the asserted scope

Locations: `Z58_TERNARY.md:28,189–200,204–205`; `scripts/z58_ternary_waldspurger.py:1–5`; `data/z58/ternary/lit_verify.md:§4,§8`.

The setting allows nebentypus ψ, including nontrivial quadratic characters supplied by ternary determinants. The formula in §4.2 silently uses ψ = 1. In the cited Darreye paper, §2.2, equation (2.3) explicitly defines

`χ_t = ((−1)^k t / ·) χ`,

and the newform is twisted by `conjugate(χ_t)`. Thus in weight 3/2 the general twist is by `conjugate(ψ) χ_{−t}`, not just `χ_{−t}`. At p ∈ 𝔐, `χ_{−4p}` alone is correct for trivial ψ, not for the full class of Theorem F. One can absorb ψ into a fixed twist of F, but then the screened newform/conductor changes and this must be explicit.

I visited and read the relevant source, not just its abstract: https://arxiv.org/html/2007.06224#S2.SS2 . The same section says **“assume that N is odd”** before its Waldspurger statement, starts with a **complete eigenform**, and its Theorem 3 supplies a bounded function `c_f(t)`; it does not itself state the asserted arbitrary-level, fixed-local-class nonzero-factor formula. Level 840 has N = 210, which is even. Moving the citation from Kohnen–Zagier's plus space to this secondary statement does not repair all these scope issues.

**Fix:** State the nebentypus-correct twist. Either explicitly restrict the numerical screen to ψ = 1, or identify the fixed ψ-twisted newforms actually tested. Cite a precise general/even-level Waldspurger statement with the required local test-vector hypotheses, including the local-class dependence of its factor. Do not present Darreye's narrower statement as that theorem. The correct observation about the standard weight-3/2 plus space vanishing at p ≡ 1 (4) should remain.

### MAJOR 2 — Central nonvanishing does not imply an arbitrary half-integral-weight coefficient is nonzero

Locations: `Z58_TERNARY.md:28,193–215,260–261,276,285–287`; script introductory comments.

From `|h(p)|² = C_h(p) sqrt(p) L(1/2,F⊗χ)` one cannot infer `h(p)=0 ⇒ L=0` without **C_h(p) ≠ 0**. Local factors can vanish. The memo itself names a concrete mechanism: a plus-space form has zero coefficients at all these p, regardless of those central values. An arbitrary lift/test vector in a fixed Hecke eigenspace need not have nonzero local evaluation on 𝒞₁.

Consequently, “a valid eigen-proxy must have rank ≥ 1 twists” and “the other 14 ... proxy ... invalid” are false without an effectiveness/nonzero-local-factor qualification. A form identically zero on the target class passes these particular validity constraints but is ineffective there. If a correct local theorem makes C constant throughout this class, the desired **valid-and-effective exclusion** can be recovered: C = 0 is ineffective; C ≠ 0 is numerically contradicted by a nonzero central value at a known zero. That is a different statement from declaring every associated eigen-proxy invalid.

The table contains 16 curve models, **15 distinct L-functions**, not an enumeration of all newforms of the listed levels or all levels supported on four primes. “No F of these levels” is too broad. The manuscript acknowledges the isogenous duplicate later, but the opening count and universal-sounding conclusion still overstate the sample.

**Fix:** Add the nonzero-local-factor/effectiveness dichotomy wherever the screen is summarized. Say “none of the 15 tested L-functions, under the stated character and local-factor hypotheses, supports a simultaneously valid and effective single-eigenform proxy.” Keep this **EVIDENCE**, not a theorem: `ellanalyticrank` at default precision is numerical, and the script discards its leading-value output. Record precision and values/error control if claiming certified nonvanishing. A finite screen also does not constrain a proxy only required to be valid above all the screened primes.

### MAJOR 3 — The purported necessary unbounded-complexity escape reverses the scope of POINTWISE_TERNARY

Locations: `Z58_TERNARY.md:53,218–230,264,277`; compare `POINTWISE_TERNARY.md:12–15,196–218,402–415`.

“Prime-only validity needs a recipe of unbounded complexity” and “bounded-complexity recipes ... are excluded” do not follow. POINTWISE explicitly permits **bounded-complexity recipes on thin sets**; its Corollary 4.2 warns against exactly this inference and gives a counterexample to the broader exclusion. The upper bound `f(p) p^(1/4+ε)` is not a bound of zero. The excluded route is obtaining enough admissible representations from a mild/positive-density representation theorem, for one fixed embedding. Thin-set existence is a separate escape, not synonymous with unbounded algebraic complexity. Parameter-dependent families and side-condition-only encodings are other explicitly scoped gaps.

Nor is an arbitrary unbounded-complexity recipe from a fixed genus logically equivalent to a Heegner incidence theorem for Lemma D(c). The dictionary converts existing Type II certificates into particular forms; it supplies neither the proposed map from a fixed genus nor an equivalence of those existence problems. “Non-empty exactly when p is not a square” also needs a domain and a new hypothesis: a fixed genus can have other local obstructions.

**Fix:** Replace necessity/equivalence by alternatives: (a) bounded recipes plus a new theorem about thin admissible sets; (b) growing-complexity/family recipes; (c) other encodings outside the fixed-embedding setup. Describe Lemma D(c) as an exact encoding of one certificate condition, not a proved equivalence of all escapes. Carry this correction into the verdict and proposed FRONTIER entry.

### MAJOR 4 — Remark F2 incorrectly replaces unit-square classes by Q_ℓ-square classes

Location: `Z58_TERNARY.md:152–157`.

Step 1 uses multiplication by a **unit**, which preserves the lattice. Two integers in the same `Q_ℓ^× / Q_ℓ^{×2}` class may differ by ℓ² and need not have equal local densities. Thus E is not generally a constant multiple of the stated B on those larger classes.

Exact counterexample: take `L = x²+y²+z²`, regard its theta series at level 12 (N = 3), and take n = 1,9. They are in the same square classes over Q₂ and Q₃. This genus has one class; `E(1)=6`, `E(9)=30`. At every good prime ℓ ∤ 6, multiplication by 3 is a unit, so `B(9)/B(1)=3`. But `E(9)/E(1)=5`, not 3. The changed density at 3 is precisely what the proposed extension omits.

**Fix:** Restrict this remark to integers prime to 2N and joint **unit** square classes, or fix each bad-prime valuation in addition to the unit square class. For the prime-regime discussion take p ∤ 2N, where this repair suffices. At 2, say “nonsquare in Z₂^× (mod 8),” not merely “nonsquare modulo ℓ.” Also distinguish “not excluded by the square obstruction” from “known to admit a Mordell identity”; the former is not the latter.

### MAJOR 5 — Lemma D(b), literally stated, includes negative-a/negative-c objects

Locations: `Z58_TERNARY.md:60–82`.

Part (b) imposes f > 0 but never β > 0. Divisibility `2C | β`, `2β | f+1` does not impose a sign. For example

`C=1, n=2, β=−2, f=3, g=2`

satisfies every listed condition: `fg−β²=2`, `2|−2`, `−4|4`, and the binary form is positive definite. Yet the inverse gives `a=−1`, `c=−1`, not positive Type II data. Reading β := 2aC as retaining positive a avoids the counterexample, but then (b) has not stated an independent forms-side characterization as its converse claims.

**Fix:** State `C ≥ 1`, `β > 0`, `f > 0`, `g ∈ Z`, with the listed determinant/divisibility conditions. Then a, c, g and b are positive and the inverse is correct. The brute-force script cannot catch the omission because it only generates β from positive a.

Related dictionary repairs (not objections to the valid algebra):

* In (c), the exact distance is correct, but `arsinh(1/(2c sqrt(Cn))) ~ 1/(c sqrt(|disc|))`. The claimed `asymp |disc|^(−1/2)` is only uniform for fixed/bounded c. Type II permits growing c. Say so, and specify that the incidence uses the displayed representative in H; it is not an SL₂(Z)-invariant condition on a bare Heegner class.
* In (d), explicitly restrict the prime/genus-reciprocity sentence to p ≡ 1 (4). The norm and `(p/d)=−1` calculations are correct. However `[d,2,(4Cp+1)/d]` has discriminant **−16Cp**, not the −4Cp discriminant of (b),(c). For C=1,p=5,d=3 it is `[3,2,7]`, discriminant −80. State the discriminant change; do not silently identify these two form families. The primitive form's genus-character sign is still −1 when p ≡ 1 (4).

### MAJOR 6 — Theorem F(ii) needs an actual unary basis, not all odd characters

Locations: `Z58_TERNARY.md:107–108,118,129–140`.

The character-average argument kills the **sum of the coefficients with a given induced character on units**. It does not kill each t = 1 coefficient in the overcomplete family currently allowed. Distinct imprimitive characters can induce the same character on units but give different theta series at indices divisible by level primes.

Explicit identity: let χ be the primitive odd character modulo 4 and let χ̃ be its imprimitive extension modulo 12. Then

`h_{χ̃,1} = h_{χ,1} − 3χ(3) h_{χ,9} = h_{χ,1} + 3 h_{χ,9}`.

Thus `g = h_{χ,1} − h_{χ̃,1} = −3 h_{χ,9}` vanishes at ℓ² for every prime ℓ > 3, yet its displayed expansion has nonzero coefficients on two t = 1 series. All these series can be placed in the same level-576 trivial-nebentypus space. Grouping induced characters gives 1−1=0, not vanishing of both original coefficients. The ambiguity does not affect E(1) or the prime conclusion.

**Fix:** Choose a standard linearly independent unary basis with primitive characters and admissibility conditions (in the usual normalization `4 t cond(χ)² | 4N` and the prescribed nebentypus). First express imprimitive-character series using old unary series. Then state (ii) for the t = 1 components in that basis. Alternatively state only the invariant conclusion actually proved on integers prime to the level.

### MAJOR 7 — Dropping “non-square” makes the falsifier-table data claims false

Location: `Z58_TERNARY.md:27`; repeated shorthand in §5.

“Above 3·10⁷ every composite zero ≤ 10¹⁰ has a factor 3, 5 or 7” is false as written. For example `10007² = 100140049` is in that interval, is coprime to 105, and is an R-zero by T1. Similarly, composite zeros coprime to 105 do not simply “end at 29 210 401.” Both scripts correctly exclude squares; the prose must do the same.

**Fix:** Insert “non-square” in every such summary and retain the domain n ≡ 1 (4) and the finite upper bound. Change “composites bind ... only through 3,5,7, which the level absorbs” to a finite-data observation. A finite census cannot establish an asymptotic restriction, and absence of orbit zeros for m coprime to 1155 is not a proof that arbitrary composite constraints are absorbed by the level.

### MINOR 1 — Remark F3's conclusion is right, but its offered proof has a zero-coefficient gap; mixed-character sums are modular

Locations: `Z58_TERNARY.md:159–165,234`.

A single scalar nebentypus does force the common determinant square class for nonzero ordinary lattice theta series. Use the **theta transformation law**, which identifies the quadratic character with the determinant character (up to the common convention-dependent factor). Equality on all good primes then forces the determinant ratio to be a rational square.

The current comparison at n=1 cannot recover ε when `θ_gen L(1)=0`. This is not a hypothetical edge case: `(2,3,3)` in the supplied table has a local obstruction at 3 to representing 1, so its genus coefficient is also zero. Its equality at ℓ² is 0=0 and says nothing about ε. Comparing at a locally represented n would also repair the argument. Numerical checks on other forms are not a proof for this case.

Moreover, sums across nebentypus characters **are modular on Γ₁ of a common level**; they need not transform by one character on Γ₀. Replace both “not modular forms” claims by “not in the fixed scalar-nebentypus Γ₀ space of this theorem.” The mixed-determinant gap is real; do not make it disappear by redefining modularity.

### MINOR 2 — Screen level and root-number explanations are mathematically inaccurate

Locations: `Z58_TERNARY.md:204–206`; `scripts/z58_ternary_waldspurger.py:1–3`.

* Prime support on {2,3,5,7} does **not** imply the lift comes from `N | 2^a·3·5·7`. Conductors 27,36,45,63 have v₃ > 1, whereas a lift at level dividing 2N under that restriction cannot. Replace by `N | 2^a 3^b 5^c 7^d` for suitable exponents, and state existence/level of any particular half-integral-weight lift separately.
* `χ_{−4p}(−N_F)` is zero for even N_F, not a root-number sign. The familiar coprime-discriminant twisting formula cannot be used in that form on the even-conductor rows. The constancy conclusion can be rescued: first twist by −4, then twist by p. Since p ≡ 1 (8) and is a residue at 3,5,7, `χ_p(−cond(E^(−4)))=1`; hence the root number is the fixed root number of E^(−4). Explain the bad-prime handling rather than using the invalid formula.

### MINOR 3 — Numerical and test claims need more precise labels

Locations: `Z58_TERNARY.md:111,162–164,210–214,249`; both check scripts.

* All 15 nonzero-r(1) rows pass the **coefficient identity at n=1**, not a full Hecke-eigenform test. The 16th row `(2,3,3)` prints `FAIL` because division by r(1) is undefined, not because an identity was disproved. Test the division-free equality and distinguish “ineligible for fitted ε” from “failed.”
* The 32 pair checks use individual theta series, not computed genus averages; no genus class-number certification is supplied. Keep their correct description as finite sanity checks, not a numerical verification of Siegel's formula or genus-class-number assertions. The same-class forms may have cusp contributions that agree on the sampled class.
* `z58_ternary_dict_check.py` prints mismatches but exits successfully even if they occur. Make a nonzero mismatch count a nonzero exit status. The dictionary test checks (a),(b), not (c),(d); its finite search bounds are adequate (see audit below).
* “≈40 per decade” is not an accurate description of the whole composite census. Counts by decimal exponent 1 through 9 are **1,8,24,60,95,111,93,52,42**. Say “42 in [10⁹,10¹⁰), 52 in [10⁸,10⁹)” if that is the intended late-range observation.
* The printed 11/56 and 14/112 are correct **row-weighted** counts. Deduplicating the conductor-32 pair gives **9/52** and **14/104**. These observations also share the same primes and are not independent Bernoulli trials. Prefer “too small and correlated a sample for a statistical conclusion” to an unsupported significance claim.
* “Finitely many zeros can always be fitted” is false in a fixed finite-dimensional space without a nullspace/dimension argument. Say “linear combinations are not excluded by this single-form screen; fitting the constraints is a separate linear-algebra problem.”

### MINOR 4 — Literature/status/novelty wording

Locations: `data/z58/ternary/lit_verify.md:§2,§3,§5,§6`; `Z58_TERNARY.md:25,167–171,262–264`.

* The Duke–Schulze-Pillot paraphrase must keep spinor-exception qualifications. Genus and spinor-genus averages are not interchangeable for all integers; local representability and bounded anisotropic valuations alone are not a blanket ternary representation theorem. This does not obstruct the memo's sufficiently-large-prime use, where finitely many unary square classes can be removed.
* The coefficient-bound paragraph's claim that `k/2−1/2−1/28` is equivalent when k is the odd numerator of the weight is an algebraic typo. For weight k/2 the displayed correct exponent is `k/4−1/4−1/28`; at weight 3/2 this is 13/28.
* The Cohen paragraph's “for positive integer r” includes r=1, the exceptional nonholomorphic weight-3/2 case discussed immediately afterward. Restrict the holomorphic Eisenstein statement appropriately (r ≥ 2). Do not silently apply the holomorphic result to the Hurwitz series.
* Retain the distinction between quantitative nonvanishing, positive-proportion results under hypotheses, and all-large-prime nonvanishing. The checked source list does not justify a blanket positive-proportion attribution to every cited twist theorem.
* AUTOMORPH's actual assertion was that squares and primes decouple **through Hecke structure**, and F1 does not bind “the same way.” That remains true. The new argument adds genus local-density rigidity; call it a refinement/stronger scoped obstruction, not a refutation of orbit decoupling. It replaces the conditional local-square-class conclusion of Prop C in this narrower theta class, not arbitrary non-genus Eisenstein statements.
* “Same proof works verbatim” for higher weights is stronger than the later “not claimed”; remove the former. Quaternary lattices have integral weight 2, not higher half-integral weight. Likewise, distinguish a sum of cusp eigenforms from a single Waldspurger central-value problem in the bottom line.

## Theorem F: adversarial proof audit

### Step 1 and the common Euler product — passes in the stated unit-class setting

* At ℓ ∤ 2N, unimodularity plus equal determinant square class does give the same ternary Z_ℓ-isometry class. No additional Hasse invariant is missing for unimodular lattices over odd Z_ℓ. State explicitly that the lattice levels divide the chosen modular level, or supply the standard justification from scalar theta modularity; this is the exact place that condition is used.
* `α_ℓ(L,nu²)=α_ℓ(L,n)` for a **unit** u is correct: multiplication of vectors by u is a bijection modulo every ℓ^k. There is no extra |u| factor. In Step 1, n is a unit square at every bad prime, so this applies exactly as required.
* The archimedean factor separates as κ_i sqrt(n), so the displayed A really is independent of n and the good-prime Euler product really is common. It is not necessary that the lattices be in the same global genus, and some/all bad-prime densities may vanish.
* B(1)>0 is legitimate, not merely an assertion that an arbitrary product of positive numbers is positive. At good odd primes the unit density is `1+χ(ℓ)/ℓ`, with χ the imaginary quadratic character of −det L. The product is a positive multiple of `L(1,χ)/ζ(2)`, with finitely many factors removed. χ is nonprincipal because the relevant rational discriminant is negative. This also explains convergence. Consequently E(1)=0 forces A=0 even when the c_i have signs or are complex.

The attempted objection “local densities change at primes dividing n, so there is no common B(n)” fails: those changes occur inside a factor that is the same for every lattice at good primes. The genuine nonunit objection applies only to Remark F2, not Step 1.

### Step 2 — passes, with the unary normalization repair in MAJOR 6

The weight-3/2 Hecke coefficient formula is correctly normalized: no missing power of ℓ in the middle term, and the final term is ψ(ℓ²)ℓ a(n/ℓ²). The genus eigenvalue 1+ℓ is correct for these ordinary ternary genus theta series at good primes; it is not the generic eigenvalue of every weight-3/2 Eisenstein series.

There is a useful independent local check of the particular identity needed here. At a good prime, write `ε=(−det L/ℓ)`. Then

`α_ℓ(1)=1+ε/ℓ`,
`α_ℓ(ℓ²)=1−ℓ^(−2)+ℓ^(−1)α_ℓ(1)`.

Their ratio, multiplied by the archimedean factor ℓ, is `ℓ+1−ε`. All other finite densities are unchanged by unit scaling. This proves the needed genus coefficient identity even when the bad-prime product, and hence E(1), is zero.

There is no overlooked noncuspidal/non-genus term in g−E **within the theorem's setting**: it is explicitly `Σ c_i(θ_Li−θ_gen Li)+h`, a cusp form by S2. Unary theta cusp forms account for the non-tempered weight-3/2 part; the remaining component is U-perp. Non-genus Eisenstein series arise only after enlarging the setting.

The Shimura–Niwa cuspidality input is standard and the secondary source really does explicitly state the orthogonal-to-unary qualification. Its quoted formulation is for complete eigenforms, whereas the proof chooses simultaneous good-prime eigenforms. The standard good-prime version suffices: Sh₁h is a nonzero cusp form when h(1)≠0, intertwines good Hecke operators, and its good eigenvalues satisfy Deligne by its integral-weight newform decomposition. Add this explanation or an exact theorem reference; one does not need a conjectural Ramanujan bound or a bad-prime newform theory here. If h(1)=0, the relevant coefficient vanishes directly, so no nonzero-lift hypothesis is missing.

For a fixed admissible unary series and a sufficiently large good prime ℓ, `tm²=ℓ²` does force t=1 and m=±ℓ. The factor `2χ(ℓ)ℓ` is correct because χ is odd. The O_g(√ℓ) error is justified by a finite eigenform decomposition.

### Step 3 and (iii) — pass

Dirichlet's theorem supplies unbounded primes in each invertible residue class. Dividing by ℓ and taking the limit removes the cusp error. Every unary character is odd, hence nonprincipal, so averaging really kills the unary terms and leaves E(1)=0. The only repair needed is the distinction between individual coefficients and grouped induced characters in (ii).

For a prime p ∤ N, a unary term supported on `tm²` cannot contribute at p unless t=p, which is inadmissible. Thus E(p)=0 on 𝒞₁ gives (iii). No positivity of h-perp and no nonvanishing assertion is being smuggled into this conclusion.

### Corollary F1 and propagation

The CRT computation is exactly right: the unit-square groups at 8,3,5,7 have sizes 1,1,2,3, and their six residues are `[1,121,169,289,361,529]`. The inclusion for odd prime support contained in {3,5,7}, and equality when 105|N, are correct. “Level 840” means 4N=840, N=210. The least-nonresidue sufficient condition follows using p ≡ 1 (4) and quadratic reciprocity, with primes dividing the level excluded as stated.

The §4.1 propagation formula is correct for a **fixed prime p ∤ 2N**, a proxy in Theorem F's theta-plus-cusp setting, and good primes ℓ distinct from p: the genus contribution is `(1+ℓ−ψ(ℓ)(−p/ℓ))E(p)`, the non-unary cusp contribution is O_p(√ℓ), and there is no unary term on that orbit. These hypotheses should be stated; “or more generally a weight-3/2 form” at the start of §4 does not allow non-genus Eisenstein forms to inherit this proof. The restriction ℓ ≡ 1 (M) is harmless but unnecessary for the leading term.

## Dictionary audit beyond the findings

D(a) is correct in both directions. In particular gcd(f,4aC)=1 justifies the modular multiplication/inversion, f>0, and an integral positive numerator divided by f gives b≥1. With β>0 supplied, (b)'s gcd(f,C)=1 follows from f≡−1 (2β), and makes the reverse implication valid. D(c)'s real/imaginary-part identity and the arsinh hypercycle-distance formula are correct. D(d)'s norm obstruction is valid even for imprimitive χ_{−4C}: a prime dividing 4Cm²+1 divides neither 2Cm nor C, hence has (−C/q)=1; multiplicativity excludes −1 modulo 4C. The genus sign for the stated prime domain is also correct after noting the discriminant change.

The n≤150 test's finite search is exhaustive, not just an unexplained box: from c≥1 one gets `4abC≤n+a+b`, hence `a,b≤(n+1)/3` and `C≤(n+2)/4`. The loops exceed these bounds. The other two enumerations terminate at genuine divisor bounds. Their agreement is useful, but does not test the omitted sign condition because all three constructions start with positive variables.

## Reproduction and number audit

All executions used `ulimit -v 4000000` and timeouts ≤1500 seconds; at most two computational jobs ran concurrently. Python was run through uv. No large census was regenerated: the existing LOGIC input and the LADDER cross-reference remain trusted upstream inputs.

The following completed and were compared byte-for-byte with the committed outputs:

* `uv run --with sympy python scripts/z58_ternary_orbit.py` — identical.
* `uv run --with sympy python scripts/z58_ternary_coprime.py` — identical.
* `uv run python scripts/z58_ternary_thmF_check.py 40000` — identical, including the explained zero-denominator FAIL row.
* `uv run python scripts/z58_ternary_dict_check.py 150` — identical, zero mismatches.

The full Waldspurger rerun, `timeout 1500 uv run --with cypari2 python scripts/z58_ternary_waldspurger.py 400000`, also completed within its timeout. All 19 output lines match `waldspurger_screen.txt` byte-for-byte; stderr is empty. This reproduces the arithmetic screen, not a rigorous certification of the numerical analytic ranks.

Independent parsing/recalculation confirms:

* 500 non-square zeros in the LOGIC input: 14 prime, 486 composite; 244 composite zeros with a nontrivial square factor; maximum composite 9,919,520,121.
* 17 prime-squarefree-part orbit zeros; m values {3,5,7,9,11,21}; surviving m-coprimality counts 4,2,1,0 for 3,15,105,1155. The lone 105 survivor is 752257=11²·6217; the largest orbit entry is 71724681=21²·162641.
* Composite non-square zeros coprime to 105: 24, maximum 29210401=11·31·85661; decade counts 4,5,9,3,3 for exponents 3 through 7. Coprime to 15: 44, maximum 7479950569. Coprime to 1155: 16, maximum 17401609. Within 𝔐, the LOGIC maximum is also 17401609, consistent with the separate LADDER extension through 10¹¹; that much larger run was not repeated here.
* Screen rows have conductors 14,15,20,21,24,27,30,32,32,35,36,42,45,48,56,63. At the four zero primes: 45 (+1,rank0), 11 (+1,rank2), 8 (−1,rank1) evaluations. At the eight controls: 98 (+1,rank0), 14 (+1,rank2), 16 (−1,rank1). Every +1 row has rank0 at at least two zero primes. The only −1 rows are conductors 21 and 45. These numbers agree with the memo, subject to its stated duplicate and the mathematical qualifications above.
* Independently enumerated R via `(4uC−1)B=n+u`, using B≥u and the derived bound `4u²C−2u≤n`. R is zero at 5569,9601,83449,102001. R at controls 8089,8929,19681,20521,87649,89329,102841,103681 is respectively **16,18,16,8,6,10,18,12**. Thus the zero/control labels are not merely inferred from a filename.

## Safe retained conclusion

With ordinary lattice theta series in one scalar-nebentypus space, standard level conventions, and a properly specified unary basis, prime-square vanishing kills the genus term on the **unit** local square class. At level 840 this includes exactly the Mordell residue classes, and the remaining prime coefficients are cuspidal and orthogonal to unary theta series. This is a worthwhile scoped obstruction to the genus-main-term strategy, not a solution of ES, not a prohibition on thin bounded-complexity recipes, and not by itself the claimed general Waldspurger invalidity screen.

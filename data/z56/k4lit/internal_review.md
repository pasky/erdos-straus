# K4LIT internal hostile review

**Verdict: MAJOR REVISION.** No FATAL defect in the elementary hidden-prime construction in Lemma P(a), or in (b) in its intended range. There are substantial overstatements of what that construction proves, a materially underspecified weighted-sieve sketch, and incorrect literature summaries. ES is not proved or disproved here.

This review reads `Z56_K4LIT.md`, the script and both numerical outputs, all three literature reports, and the relevant parts of `Z55_P415.md` and `Z54_HCKILL.md`. Primary checks include the Iwaniec 1972/1976 page images, FI 2009 §§1, 6–7, Nath–Xie v3, Matomäki, Sedunova, Dimitrov, Teräväinen, Maynard II, Lichtman, Pascadi, Polymath8a, Stadlmann, Wright, Merikoski and Tao–Teräväinen. Cached abstracts and `/tmp/gmpp.txt` confirm the recent-preprint claims noted below. Reading a statement is not verification of its proof.

## Findings

### 1. MAJOR — The construction does not attain f at the advertised sieve parameter

**Location:** §0 H2, §1 (L), §3 Remark 1, §7 Lemma-P bullet.

For fixed ε and `D = x^(1/2−ε)`, the odd cofactor has parameter

`s'_q = log(x/q)/log z = [(1/2+ε)/(1/2−ε)]s + O(1/log z)`,

where `s = log D/log z`. Thus the limiting sifted ratio is at the *larger* parameter, not f(s). For instance, at ε = .05 and s = 1, the limit parameter is 11/9, with positive f(11/9), whereas f(1) = 0. The displayed `s' = s(1+O(ε))` does not turn into `s' = s+o(1)` as x grows with ε fixed. Hence “no improvement over the general semi-linear sieve” and “f is asymptotically sharp within the parity-forced class” are not established by this example. The zero-S-mass result is a different, valid assertion.

The formula `f(u) = 2 sqrt(e^γ/(πu)) arccosh(sqrt(u))` is correct on [1,2], and extends to [1,3]. The odd model does yield this function: for fixed 1 < u < 3 its survivors have exactly one inert prime, so summing `m = ℓb`, `b ∈ S`, using the PNT in progressions and Landau's theorem yields it. This is not proved in the memo, and the unrestricted Remark 1 needs a range/continuation and a uniformity statement. Its displayed formula for S(𝒜,z) also presupposes that the hidden primes exceed the sifting cutoff (e.g. z≤D in (a)); otherwise it needs the additional condition q∤P(z). A finite-x mixture is weighted by `1/q`, not represented exactly by q = 1.5D.

**Fix:** State only the proved zero-S-mass obstruction in H2/§7. Give the cofactor-model asymptotic separately, at `u = [(1/2+ε)/(1/2−ε)]s`, initially on a compact subinterval of (1,3). If an extremality claim is desired, prove an appropriately ordered ε→0 limit or a separate logarithmic-slack construction, and state its remainder class; do not assert sharpness for fixed ε from the current calculation.

### 2. MAJOR — The application to shifted-prime sieve data is not proved

**Location:** §3 Setting (“factor φ, which is irrelevant here”), Consequence, and its joint-density parenthesis; H2 and §§7–8.

The construction matches `g(d)=1/d`. Shifted primes have local density `g(q)=1/(q−1)`, not 1/q. For example, at q=3 the two predictions differ by X/6, vastly exceeding the allowed power-saving remainder. Equality of sieve dimension or convergence of the ratio of Euler products does not make these main terms interchangeable in an information-theoretic counterexample. The example therefore does not prove the asserted no-go statement for N₂'s *actual* shifted-prime sieve data.

Nor does it prove a joint-data obstruction. The memo explicitly disclaims constructing one, which is good, but its parenthesis says the exact joint density “has h(q,q)=0” without the necessary exception: `h(3,3)=1/2`, as correctly recorded in P415 Step 2, because the two roots coincide at 3.

**Fix:** Restrict the Consequence to the specified scalar density 1/d and the specified error class. Delete the inference to actual P(4,15) data, or supply a new construction matching those data. Restore the exception at 3. Keep the comparison to prime sieving explicitly Assessment-level.

### 3. MAJOR — The asserted endpoint of the barrier and the method-exclusion language are too strong

**Location:** §3 Remarks 2–4, H2, §4.1 row 1, §4.3, and §§7–8.

“It disappears only at EH level” is false for the *positive S-mass obstruction* proved by Lemma P. With full data to `D=x^θ`, any fixed θ>1/2, and sufficiently small remainders, sieve to `z>sqrt(x)` with `log z/log x→1/2`. The semi-linear lower function is positive at `s→2θ>1`. For odd n≡1 mod4 every survivor is in S, since two inert factors ≥z cannot fit below x. Thus full-data positivity is already available just above exponent 1/2. An F-asymptotic near exponent 1 is a different question. Remark 2's disclaimer about the intermediate range does not repair Remark 4.

Likewise Lemma P neither proves that switching is the only possible additional information nor gives an additive necessity theorem “one exact shift per level 1/2.” The 3/4 discussion is implementation bookkeeping, not a lower bound for every multiplicative approach. P415 explicitly calls its levels *sufficient levels found*, not barriers. Its A1/A2 exclude full-family confinement identities under stated hypotheses, not every possible use of norm-form prime technology; the blanket exclusions in H3/§7/§8 lose that qualification.

**Fix:** Distinguish (i) the model zero-mass counterexample below 1/2, (ii) positivity above 1/2 with full data, and (iii) near-level-one asymptotic results. Replace “must,” “only,” “impossible at BV level,” and universal exclusions by statements about the specific implementations audited. Retain “EH-hard” only as an explicitly scoped Assessment, not as a consequence of Lemma P. Mark the 3/4 budget as sufficient bookkeeping for the proposed route.

### 4. MAJOR — (★K)/(★K′) is not yet a precise conditional implication

**Location:** H5; §1 (K); §4.1 row 2; §4.2 in its entirety; §8 final paragraph.

The route is plausible, but the stated hypotheses do not yet encode the estimates used in the sketch:

* H5, the ranking, and §8 use r, while the actual hypothesis uses r*. This distinction is decisive: r>0 only gives SOTS; r*>0 gives S for odd arguments.
* `g*` and `𝒳` are unspecified. In particular `g*(3)=0`: if 3 divides p+4, then 3 divides 4p+1 and its primitive representation count is zero. This is not the unweighted density 1/2. Away from the determinant primes the primitive-weight local calculation must be performed (the expected inert-prime density for q≥7 is 1/(q−2)). The prime 5 is not in the semi-linear sifting set, but affects the r*-weight and the exceptional local factors because it divides the determinant.
* (★K′) says only “the analogue.” It gives no summation ranges, coefficient dependence, main term, endpoint uniformity or summable error over the switched m,q variables. Saying its level is x^(1/8) is not an estimate.
* The proposed alternative `r* ≤ r ≤ 4τ` plus a small-divisor majorant does **not** automatically lose only an absolute constant. The mean of τ has a logarithmic factor whereas that of r does not. A growing log loss destroys the fixed-η comparison. FI §7 explicitly warns that crude estimates cannot afford to lose the signs of the sieve weights, and evaluates the r-sum using Lemma 4.1 instead.
* The primitive expansion and hyperbola reduction need an actual argument. For odd N an exact identity is `r*(N)=4 Σ_{e|N} μ²(e)χ₋₄(e)`, equivalently `Σ_{k²|N} μ(k)r(N/k²)`. This is not the unweighted symmetric divisor sum for r. The factor 4 and squarefree/primitivity bookkeeping cannot simply be suppressed in an asserted identity.
* “FI's divisor-function-weighted A(θ) is exactly (★K)” is inaccurate. Their sentence concerns divisor weights on progression-error sums and immediately says Cauchy's inequality handles them. FI's statement concerns r, a different pair of forms, additional parameters, and different local factors. It motivates an analogue; it does not identify it with the present primitive-weight estimate.

**Fix:** Keep this as **Assessment: proposed conditional route**, not a proved conditional theorem. Define the primitive mass and all local densities; specify (★K′) or state directly a uniform switched upper bound of the required size. Prove the primitive expansion/truncation and the claimed EH implication, including any divisor-weighted errors. Use r* consistently in every summary. Do not offer the τ-majorant argument as an established constant-loss substitute.

The last Cauchy–Schwarz step itself is sound: `Σ_{p≤x} r*(4p+1)² ≤16 Σ_{n≤4x+1}τ(n)² ≪ x log³x`. The proposed weighted lower bound would therefore give a count `≫ x/log⁶x`, and already implies infinitude without this step.

### 5. MINOR — The CRT formula is correct only with the missing coprimality condition

**Location:** H5 and §4.2 “Why (★K) is hard,” second bullet.

For odd e with `(d,e)=1`, the formula is correct:

`a = −4 + 15d (4d)^(-1) mod de`.

Indeed a≡−4 mod d and `4a+1 ≡ −15+60d(4d)^(-1) ≡0 mod e`. It is not a formula when 4d is noninvertible modulo e. In unrestricted divisor expansions common factors must be treated; solvability requires `(d,e)|15`, and the CRT modulus is then lcm(d,e), not de. On the actual primitive support, inert d and split-only divisors e are coprime, but expansion before primitive cancellation need not have that property.

**Fix:** State the coprime case explicitly and separate exceptional common factors before opening the weight. No sign or factor-15 correction is needed.

### 6. MAJOR — Matomäki's theorem is misstated as an impossible S-condition

**Location:** §2 table, row “p − 1 ∈ S in short intervals”; broad “p+A∈S” wording in H1 and the first table row.

For every odd prime p, p−1 is even and hence is **not** in S as defined in this memo. Matomäki 2007 Theorem 1 is about `b*(p−1)=1`, primitive representations, and her sieve works on p≡3 mod8. The equivalent S-condition is `(p−1)/2 ∈ S`. The supporting report A1.4 already makes this distinction correctly. Similarly, the Iwaniec 1972 specialization giving p+4∈S is valid, but arbitrary p+A∈S cannot be asserted without parity/local qualifications (odd A makes p+A even for odd p).

**Fix:** Replace the short-interval row by the exact b* statement or `(p−1)/2∈S`; restrict the general one-shift summary to admissible shifts/odd parts, or just state the verified p+4 specialization.

### 7. MAJOR — Sedunova's weighted count is silently converted to an integer count

**Location:** H1 unconditional-neighbours bullet; §2 Sedunova row; cf. lit_A A2.2 and lit_C §0.

Sedunova's `s_Γ^(7)(x)` counts matrices/representations, not distinct values of n. The definition on p.3 explicitly counts quadruples. Thus Theorem 2's `≫x/log x` is a weighted count (equivalently involving r(n−2)r(n+2), with the parity-dependent conversion); it does not supply that same lower bound for the number of distinct squarefree n. The reports sometimes preserve “weighted,” but the memo drops it. The factor bound 7, Theorem 3's `floor(2/θ)`, and the claimed level 1/6 are correctly transcribed.

**Fix:** Add “representation-weighted” wherever the order of magnitude is stated. Claim only infinitude of distinct n unless a moment/weight-removal argument with its actual weaker quantitative bound is supplied. Treat the det-15 port in §4.4 as an unproved plan, not an automatic theorem with the same factor bound.

### 8. MAJOR — The Dimitrov benchmark fails a basic local check as stated

**Location:** H5, §2 Dimitrov row, §4.2 final bullet; lit_A A1.5.

The cached Dimitrov Theorem 1 really does print the global main term `φ(q)^(-1) Σ_{p≤X}r(p−1)`, so the report is not inventing that quotation. However, it cannot be a valid general AP-distribution theorem as written. Take q=8, a=7. Then p−1≡6 mod8 and r(p−1)=0 identically, whereas the claimed main term is one quarter of the global sum, which is of order X/log X by the quoted single-shift theorem. This contradicts its claimed smaller remainder. There is also a strong bias already modulo 3; an independent bounded computation gives the mass in p≡1,2 mod3 as 355112 and 1420300 at X=10^7, approximately 1/5 and 4/5, not halves.

**Fix:** Do not advertise this as a verified state-of-the-art theorem without resolving the missing/incorrect local main terms or a missing restriction in the source. Mark it “source states this; local-density issue unresolved.” For the present route, formulate the correctly biased Titchmarsh distribution problem rather than treating a global uniform-density formula as a usable benchmark.

### 9. MAJOR — Blanket assertions about beyond-BV levels omit restrictions and a contrary source statement

**Location:** H3 “Every such result”; H4; §5 final sentence; §§7–8; lit_B verdict and lit_C §2.12.

The numerical exponents in the named fixed-residue results are correct, but “every beyond-1/2 result needs one fixed integer residue and well-factorable weights” is false as a blanket statement. Polymath8a and Stadlmann, discussed immediately afterwards, are exceptions in residue flexibility. Maynard I (already in report B) has absolute-value estimates for structured factored moduli, rather than the weighted formulation of Maynard II.

More significantly, Wright 2609.35950 p.4, immediately after Corollary 3.3, explicitly recalls his fixed-residue exceptional-character result up to `q<x^(2/3−ε)` (reference [20]). Therefore “prime levels ≤0.52” is true only for the specified *uniform-in-residue* results, not for all Siegel-zero-conditional prime levels. The omitted fixed-residue result still does not solve the coupled-residue problem, but the numerical universal ceiling is wrong. Merikoski's 0.61634 threshold is also not a stand-alone ordinary Type-I theorem: it assumes the Type-I and Type-I-χ inputs and comparison-sequence conditions of Theorem 15, as report B correctly records.

**Fix:** State separate ledgers for fixed-residue weighted, structured-modulus, smooth/coherent-residue and uniform-residue results. Qualify the ≤0.52 ceiling by residue uniformity and mention Wright's secondary fixed-residue 2/3 statement. Keep Teräväinen's 3/7 and 2/5 optimality explicitly relative to Lemma 9.2's factorization problem, not all conceivable semi-linear weights. None of these corrections supplies the missing P(4,15) estimate.

### 10. MAJOR — Verification provenance and exhaustive-sounding conclusions are inconsistent

**Location:** opening Reading guide, H1 “all verified,” H3 heading, §2 heading, §5; supporting reports' verdicts.

The Reading guide says every hot lead was cross-checked personally. §5 expressly says numerous hot-lead items were not. Report B labels BFI Theorem 10 SECONDARY via Maynard/Lichtman, FI2003 SECONDARY via Wright, and the Opera de Cribro text UNVERIFIED. Report A labels Linnik and Hooley secondary. These distinctions must survive headings such as “source-verified map” and “all verified.” The existing explicit secondary qualifiers on individual Linnik/Hooley/FI2003 entries are good, but do not make the universal headings accurate.

“No unconditional or conditional source states it,” “not in the literature,” and “every known method” go beyond a bounded search. The practical assessment can be strong without claiming exhaustive knowledge. Also report C's Banks table/§2.14 says the route is removed/becomes vacuous without the memo's appropriate “if correct, unrefereed” caveat. Its Lü–Wang–Wu mechanism verdict is an assessment, not pure research or an independently checked disproof.

**Fix:** Provide per-item provenance: primary statement read, secondary restatement, abstract only, or unverified proof. Say “no such theorem was located in the searches described.” Correct the personal cross-check assertion. Preserve the memo's recent-preprint caveats in the supporting reports and label applicability/validity judgements separately from source transcription.

### 11. MINOR — Iwaniec 1976 is quoted essentially correctly, but the asymptotic qualification is missing

**Location:** H2, §2 “Level and parity facts,” §3 Remarks 1–2, §5, §8; report B1.1.

The page images confirm Theorem 2's hypotheses `a'≡1 mod4`, `P⊂{p≡−1 mod4}`, the standing sieve-density hypotheses, `Q^6<z²≤A`, and remainder sum over `d<A/Q`, `d|P(z)`. Its relative error includes `((L+log Q)/log A)^γ` (times the stated K,s factor). Setting Q=A^ε with fixed ε leaves an O(ε^γ) error, not automatically o(1). One needs the appropriate limiting choice/control. Moreover this theorem as printed has z≤sqrt(A); it does not directly justify the numerical natural-sequence rows with z>A^(1/2). Those rows are nevertheless correct by the exact parity reduction to S and Landau's theorem.

Corollary 2 (2.1) gives a sufficient near-EH-level error hypothesis for an asymptotic; it does not prove that EH is necessary. For a proper subset P of the inert primes, congruence alone fixes total Ω_Q, not necessarily Ω_P; avoid explaining the general theorem by conflating the two.

**Fix:** Include the error and limit qualification, cite Landau/parity for the s<2 natural model, and replace “needs EH” by “this theorem obtains the asymptotic from an EH-type hypothesis.”

### 12. MINOR — Numerical transcription and interpretation need correction, though both runs reproduce

**Location:** §3 Remark 1 numerical bullet and final bound; `scripts/z56_k4lit_lemmaP.py`, especially lines 41–52, 72–94.

Both stored runs reproduce byte-for-byte. There is no W(z)-truncation bug for these arguments: the prime table extends to `max(2D+2,xN+2)`, covering every z used. The hidden-prime sift count correctly counts multiplicity, and all tested d are squarefree inert-composed, coprime to every hidden q, and below D in these runs. The printed zero S-mass is justified by construction, not independently enumerated.

But “sieve data for small d agree to ≤10^-5 relative” is false. At x=10^12, d=4389 has error −1.59×10^-3; even d=31 is +1.11×10^-5 and d=231 is +8.29×10^-5. The second run has maximum displayed error about 1.48×10^-3. The reported crude totals 0.363 and 3.16 use `D·#hidden_primes/X`, not `D·π(2D)/X` as the memo says. They do not verify the asymptotic aggregate remainder hypothesis at these sample sizes.

The script's s' substitutes q=1.5D. It is an illustrative representative, not the exact model parameter. At x=10^13, s=1, the actual s'_q range is 0.99356–1.04082 and crosses the threshold 1. The displayed f formula must not be used outside its valid range if different CLI parameters are supplied; likewise the small-d check requires coprimality with the hidden primes, not just inert squarefreeness.

**Fix:** Correct the error claim and #q/π notation; label representative s' explicitly or report the `1/q`-weighted average of f(s'_q). Add parameter/range checks if the script is intended for arbitrary CLI values. Keep these calculations EVIDENCE, not a certificate of the global sieve hypothesis or sharpness.

### 13. MINOR — The proof of admissibility in (b) needlessly changes ε

**Location:** §3 proof, paragraph beginning “Admissible.”

In the intended range `D≥1`, `x^ε≤z`, `zD≤x^(1−ε)`, one has `log z ≍_ε log x` and X≍_ε x/log x. The displayed `O(X x^(−ε)log x)` already is `o(X x^(−ε/2))`. Replacing ε by 2ε is unnecessary and obscures that the original stated range meets the Consequence. Using the prime-counting bound, rather than π(2z)≤2z, gives the sharper relative bound `O(Dz/x)≤O(x^(−ε))` directly.

**Fix:** State D≥1 and the intended z range explicitly and give one of these comparisons, without changing ε. For the dyadic reciprocal-prime asymptotic cite the PNT in progressions (or a sufficiently strong Mertens-in-progressions estimate); a bare unspecified o(1) Mertens remainder would not by itself resolve the 1/log z leading term.

### 14. MINOR — Separate claim labels and make the prime restriction in §4.3 explicit

**Location:** §1 (K), §4.2 heading, §4.3 heading/display, and unlabelled literature/strategy assertions in §§0, 2, 7–8.

The required “exactly one of PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment” convention is not met. The same proposed implication is both CONDITIONAL and Assessment, and the §4.3 heading combines PROVED with Assessment. “Verified,” “OPEN,” and a bare literature-map heading are not substitutes for those claim-status labels. This is especially important where a sketch or a sufficient-level model can be mistaken for a theorem.

The §4.3 pointwise identity is correct under its stated hypotheses: z>N^(1/4) permits at most three inert factors with multiplicity, and parity leaves 0 or 2. With all sums explicitly over `p≤x, p≡1 mod8`, and z>(4x+1)^(1/4), the displayed counting relation is actually equality. Without that prime restriction it counts the wrong target. The label “PROVED identity” must not cover the subsequent 3/4 necessity language (Finding 3).

**Fix:** Give the identity its own PROVED statement, the proposed route and level budget their own Assessment statements, and classify each literature result separately from its provenance. Use CONDITIONAL for an implication whose proof is actually supplied, or Assessment for the current sketch, not both on the same claim. Put the prime restrictions under the summation signs. No ES overclaim was found.

## Checks that pass

**PROVED (review calculation): Lemma P's elementary core.** For each hidden q, n=qm with q≡m≡3 mod4 is odd and ≡1 mod4, and has an inert divisor. If d≤D<q, or d|P(z) with q>z, then (d,q)=1. The two conditions on m define exactly one class modulo 4d, so each counting error is bounded by 1. Summing gives the asserted per-d error and then the aggregate bound. PNT in progressions gives

`Σ_{D<q≤2D,q≡3(4)}1/q ~ log 2/(2 log D)`,

hence X~x log2/(8 log D) and `Σ|r_d|/X ≪_ε x^(−2ε)` in (a). In (b), under its product restriction, the stronger relative bound is `≪Dz/x`. Thus the abstract zero-S-mass Consequence with density 1/d is valid. It is meaningful, not vacuous: a natural parity-forced integer sequence, rescaled to the same X, has positive S-mass and admissible errors, whereas this bounded-multiplicity sequence has none. It does not decide the shifted-prime or joint-data problem.

**EVIDENCE (reproduction):** Both commands completed within a 600-second timeout and a 6,000,000-KiB virtual-memory limit, using `uv run --with numpy python`:

* `scripts/z56_k4lit_lemmaP.py 12 0.45 8`: byte-identical to `lemmaP_1e12_045.txt`; SHA-256 `8f3a19f1545ecf64f07cde357b0ac1dd17665d0fdafa579c2b7cadc4be4e07da`.
* `scripts/z56_k4lit_lemmaP.py 13 0.49 7`: byte-identical to `lemmaP_1e13_049.txt`.

The shorter timeout respects the brief's global ≤600-second rule rather than its conflicting example using 900 seconds. Auxiliary checks used arrays of at most 10,000,001 elements, not Cartesian-product allocations.

**EVIDENCE (source transcription audit):**

| Item | Audit result |
|---|---|
| FI 2009 Theorems 2, 3, 4 | Correctly conditional on A(θ) for θ<1 sufficiently close to 1; upper bound unconditional. Thm 4 is Λ-weighted ≍x, not an unweighted count of distinct primes. |
| FI 2009 Theorem 5 | Correctly an unconditional single-shift r-weighted asymptotic in disguise, via BFI Thm 9. |
| FI §§6–7 quotations | The “β=1 / D<sqrt(x)” and “weighted by a divisor function” quotations are genuine. Their extrapolation to ★K needs Finding 4's repairs. |
| Iwaniec 1972 Thm 1 | S₁ does impose proper representation; the p+4 specialization is valid. |
| Iwaniec 1976 Thm 1 / Cor. 2 | β=1 and the displayed lower function are correct; (2.1) contains E(N,N^(1−ε)) with an O(ε^γ) main-term error. |
| BFI Thm 10 | 4/7 is correctly restated in Maynard II Theorem A; original BFI not independently read here. |
| Maynard II Thms 1.1 / 1.2 | 3/5 triply well-factorable; 7/12 for well-factorable upper linear-sieve weights: correct. |
| Lichtman 2309.08522 Cor. 1.5 | 66/107, triply well-factorable and one fixed nonzero residue: correct. Thm 1.7 has the additional stated residue-size restrictions. |
| Pascadi 2505.00653 Thm 1.3 | 5/8 triply well-factorable; 3/5 upper linear-sieve weights, unconditionally: correct. |
| Teräväinen Lemma 9.2 / Remarks 9.3–9.4 | 3/7 and 2/5 and the stated optimality are correct for the specific partial-factorization assertions. |
| Polymath8a Thm 1.1 / Stadlmann Thm 1, Cor. 2 | 1/2+7/300 and 1/2+1/40 respectively, with smoothness/coherent-residue qualifications: correct. They do not directly cover the required full semi-linear support. |
| Wright Thms 3.1 / 3.2 | 30/59 individually and 16/31 averaged with residue uniformity: correct, subject to exceptional-zero strength/window hypotheses. See omitted fixed-residue 2/3 in Finding 9. |
| FI2003 via Wright Thm 2.1 | 233/462 correctly restated; remains secondary. Report B's displayed FI2003 error must remain inside the factor ψ(x)/φ(q), as it is in Wright, not be written as an unscaled additive O-term. |
| Merikoski Thm 15 | Threshold `(1+sqrt(e))/(1+2sqrt(e))≈0.61634` correct; not merely a scalar level assumption. |
| Tao–Teräväinen Thm 1.6 | At most two Λ factors and the quotation about divisor correlations are correct; applying this diagnosis to the det-15 problem is an assessment. |
| Nath–Xie v3 Thm 1.1 / Remark 1.1 | Ω(p+2)≤9, lower bound x/log^(5/2)x; EH-variant remark gives ≤3. The v1 bound 11 must not be substituted for v3. |
| Sedunova Thms 2 / 3 | Numerals and levels correctly quoted; preserve representation weights (Finding 7). |
| GMPP / Lü–Wang–Wu / Banks | Cached statements confirm almost-all-shift averaging, the claimed fixed-shift Möbius cancellation, and the claimed constant 0.003 respectively. These checks do not validate the new proofs. GMPP's “first non-factoring thin sequence” sentence occurs in the paper, not its cached abstract. |
| Other norm-form, averaged-correlation and integer-SOTS neighbours | Consistent with the supplied reports at the level used by the memo; no independent proof audit or exhaustive literature certification is claimed. Linnik/Hooley remain secondary; A1/A2 applicability remains scoped to full-family confinement. |

**Assessment (overall):** Keep the elementary model obstruction and the useful FI comparison, but remove the leap from those observations to universal sharpness, a forced switching budget, or an exhaustive “known-hard” theorem. The literature calibration is worth retaining after the parity, weighting, local-density and provenance corrections. The new weighted route remains a research specification, not a completed implication.

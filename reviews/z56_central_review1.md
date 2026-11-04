# Hostile review: Z56_CENTRAL

**Overall verdict: CORRECT-WITH-FIXES.** The central analytic results survive: Theorem L, its precisely quantified corollaries, Theorem U, and Proposition P's count bound are sound. However, the memo overstates the fixed-band reduction and the known exponent-pair obstruction, supplies an insufficient proof for its strengthened DC consequence, and certifies the wrong numerical residual. These are mandatory corrections, not stylistic preferences. No ES proof is claimed.

Reviewed the entire memo, scripts and tables; TDCAL §1, Lemma S(a), Prop C and Prop D(iii); TDF §3.3; LIT_CHECK; and the relevant cached primary texts. In particular, I re-extracted `/tmp/lit/2512.05652.pdf` and `/tmp/lit/2306.05599.pdf`. No memo or existing script was edited.

## Findings

1. **MAJOR — Fixed-band CNT is not CNT_poly; the claimed generic bridge is unjustified.** Location: `Z56_CENTRAL.md:127–135`, propagated at lines 25–26, 337 and 350.

   The *displayed definition* of CNT_poly and the ensuing exponent calculation are valid, provided η > 0 and B ≥ 0. But this is a uniform theorem for **all real x, independently varying y, all θ, and x-dependent λ ∈ [x^{-1/8},x^{1/8}]**, with a common starting threshold. It is not equivalent to a theorem for every fixed λ with a polynomial implied constant: the latter may have an uncontrolled λ-dependent starting threshold. Nor does an explicitly position-dependent constant have to be polynomial (it could be exponential). Original CNT is weaker still: it is restricted to prime p and the tied choices x = p + 2U, y = 2U, A = U², θ = 4.

   **Fix:** retain the actual CNT_poly hypothesis and its proof, explicitly add B ≥ 0, and delete “Any proof … would deliver CNT_poly” / “essentially any proof of fixed-band CNT.” Throughout the summaries, say “the all-x, length-decoupled, polynomially uniform hypothesis CNT_poly.” List extending the prime/tied setting and obtaining uniform thresholds as additional requirements, not automatic consequences.

2. **MAJOR — The claimed obstruction from all known exponent pairs is false; the cited paper itself gives a better pair.** Location: lines 29–30, 155–156 and the “only” wording at line 339; distinguish these from the correctly restricted finite search at lines 145–146.

   Trudgian–Yang, arXiv:2306.05599, **p. 3, Lemma 1.1 (1.6)**, explicitly gives `(715/10238 + ε, 7955/10238 + ε)`. For this pair, at ε = 0,

   `(1−3κ)/(4(λ−κ)) = 8093/28960 = 0.2794544198895…`,

   so the same argument works for `δ > 6387/28960 = 0.2205455801105…`, strictly improving `123/556 = 0.2212230215827…`. In particular some slices with exponent above 0.279 are reachable by a known pair. LIT_CHECK quotes this paper but checks only its A/B processes and EPC discussion.

   **Fix:** either incorporate this explicitly verified improvement (without asserting global optimality), or consistently qualify the obstruction as applying only to the tested descendants of the two selected seeds. Corollary L3's sufficient range and its finite-search maximum are correct; they do not establish a best-known barrier. Extend LIT_CHECK if using the improved pair.

3. **MAJOR — The advertised “same proof” of TD ⇒ DC with only a loglog loss leaves a log U loss.** Location: lines 233–234 and 343; compare `Z55_TDF.md:266–270`.

   The cited Erdős–Turán proof gives, with M = |E1⁺| and H = floor(U^η),

   `count(I) ≤ |I|M + O(M/H + U^{1−η} log H)`.

   Replacing M by `O(U(log log U)^{5/2})` does **not** remove the last logarithm. At |I| ≍ U^{-η}, this is still larger than the claimed bound.

   **Fix (the conclusion is salvageable):** supply a localized positive-kernel argument. The Fejér kernel F_H is ≫ H on |v| ≤ 1/(2H). Therefore every interval J of length 1/H satisfies

   `count(J) ≪ M/H + H^{-1} Σ_{1≤|h|<H}|T(h)| ≪ U^{1−η}(log log U)^{5/2}`.

   Cover an arbitrary I with |I| ≥ U^{-η} by O(H|I|+1) such intervals. This proves the desired `count(I) ≪ U|I|(log log U)^{5/2}`. State this proof instead of attributing the improvement to the existing proof. Proposition P alone does not establish any nonzero-mode density hypothesis.

4. **MAJOR — The CERTIFIED identity residual is for harmonic centering, not Theorem L's E_band.** Location: lines 41–42 and 273–275; `scripts/z56_central_slices.c:8–9,50–55`.

   The program prints `FLc = count − yH = −F_L`. Its `resid` uses **Eband_h**, whereas Theorem L uses **Eband** with the logarithmic main term. These differ by an O(y/L) term which matters to the advertised number. For x = 10000000651, y = 632, δ = 0.20, the actual theorem residual is

   `D − Main − (E_band − 2F_L) = 0.631850009559724373…`,

   whereas the harmonic-centered residual is `0.315917818941133393…`, printed as 0.316. Scanning all 2400 stored cases finds the maximum logarithmic residual at this same input (0.6319 from rounded columns). Thus both “≤ 0.32” and “max = 0.316” are false for the stated quantity. The O(1) theorem is unaffected.

   **Fix:** calculate `resid = Derr − (Eband + 2*FLc)` and report approximately 0.632, or explicitly rename the checked quantity as the harmonic-centered variant. Correct the header's false equation equating the ψ-difference sum with count minus mean. At larger x, `Derr − 2*FLc` is a proxy for E_band with an O(1) error, not its exact value: give it a different name rather than redefining the already-defined E_band. RMS F_L values are unaffected by the sign convention.

5. **MINOR — Sup-norm and literature-status claims need narrower wording.** Location: lines 27–29, 67–76, 155–158, 168–169 and 244.

   The statement at line 74 correctly limits the Ω obstruction to bounding the difference by endpoint absolute values. “SID cannot follow from any pointwise bound on Δ” is broader than this argument establishes. Also, Ivić–Zhai's displayed estimates are not the best available bounds at every length: the global Δ exponent 0.314483… quoted in LIT_CHECK already gives a nontrivial short-difference bound for lengths x^{0.32}, below x^{1/3}. What is true is that **these two Ivić–Zhai estimates** improve on the length bound only beyond exponent 1/3. Their substitutions 5/16 and 11/36 are correct.

   The historical Jutila/EPC conjecture statements and the search-limited SID assessment are supported. A search finding no twisted result does not independently certify that every TW parameter regime is an established open problem; “whether finitely many twists suffice is open” has no cited support beyond not being established here.

   **Fix:** say “the endpoint sup-norm/triangle-inequality route cannot give SID,” “the cited Ivić–Zhai estimates,” and “Assessment, search-limited: not established in the checked sources.” The quoted Ω with its logarithm actually excludes SID(1/2) too; `η ≤ 1/2` is a valid but non-sharp necessary condition.

6. **MINOR — The exponent-pair script evaluates depths 0–8, not ≤ 9.** Location: lines 145–146; `scripts/z56_central_pairs.py:12–21`.

   `range(9)` evaluates the seeds and eight generations, generating but never evaluating generation nine. The A/B formulas, θ objective and reported fractions are correct. I independently enumerated all A/B words through length nine with exact fractions: the distinct best objectives remain `155/556`, `511/1850 = 0.276216…`, and `1313/4754 = 0.276188…`. Thus the numerical maximum survives, but the supplied script does not certify the advertised search. The name-based B-pruning happens to be harmless for this seed, since B(Bourgain) = Bourgain and B² is the identity.

   **Fix:** use ten evaluated generations or state length ≤ 8. Keep this restricted search separate from claims about all known pairs (item 2).

7. **MINOR — Table 8.2 and several numerical readings disagree with the data.** Location: lines 42–43, 294–320.

   At `gen16`, the last common slice RMS is **1.69**, not 1.86; 1.86 is the penultimate slice. The full observed RMS range is approximately **0.52–2.56**, not 0.55–1.8. Square/near-square means range to **−0.12** (`nsq10`), not only −0.3 to −1.1; their central-band means include **−0.18** and **−0.30**, outside the stated −0.5 to −1.2 range. All reported dyadic means in those two families are indeed negative.

   F_L itself is not a decreasing function of δ, nor is |F_L|. The first generic input already has FLc values `26.6532, −44.7670, −33.1630, −28.8176`. Only the **sample RMS values** displayed in Table 8.1 decrease in δ.

   **Fix:** correct the last-slice entry and ranges, and replace the monotonicity assertion by the precise empirical RMS observation. Growth with M is a broad trend, not monotonicity in every row.

8. **MINOR — Table 8.1's y/model columns describe the first sample, not the whole family.** Location: lines 264–292; `scripts/z56_central_stats.py:16–20`.

   Every printed Table 8.1 entry matches the regenerated stats. However, y = 632 is not constant even in gen10 (632–634). In sq10 it ranges **632–1410**, and x ranges **10000200001–248401563201**; nsq10 has essentially the same wide range. The corresponding model values range about **10.26–12.80**, not a single 10.26. The script correctly normalizes each observation by its own sqrt(y), but prints y and the model only from the first observation. Also `nb = min(...)` means Table 8.2 uses the last **common index**, not necessarily each sample's last slice.

   **Fix:** label the y/model columns “first sample,” preferably give ranges, and explain the common-index convention. Do not imply that these square controls form a tight window around 10^10.

9. **MINOR — Small-control metadata is inaccurate/ambiguous.** Location: lines 319–320.

   The test data include p = 193 with **U = 3**, so the range is 3–54, not 4–54. The absolute maximum |Ec| = 19.2957 at p = 5101441 and Ec = 17.2631 at p = 329617 are correct. “Largest relative value” is undefined: 329617 maximizes |Ec|/sqrt(y), but 409 has the larger |Ec|/y (3.0947/8 versus 17.2631/46).

   **Fix:** specify the normalization and correct U's range. Identify the U = 3 case as outside the campaign's usual U ≥ 4 convention, though the strip count remains well-defined.

10. **MINOR — A degenerate Hessian is not the zero Hessian; the ensuing duality discussion is only formal.** Location: lines 37–39 and 251–259.

    All three displayed second derivatives in Remark H are correct, and their determinant is zero; the matrix itself has rank one for positive h,n. The summary's “its Hessian vanishes identically” is false. Furthermore, Vaaler and stationary phase introduce h,n-dependent weights, so grouping by N = hn generally produces a **weighted restricted divisor coefficient**, not an unweighted τ_c(N). A standard divisor Voronoi formula cannot simply be applied to such a restricted coefficient.

    **Fix:** write “the Hessian determinant vanishes identically.” Keep the differentiation as PROVED and explicitly qualify the grouped-sum/Voronoi narrative as a formal analogy, or supply a transform with the actual weights. The linearity along rays and the obstruction to a directly applicable nondegenerate-Hessian theorem are sound.

11. **MINOR — Make the otherwise correct Theorem U parameter reduction explicit.** Location: lines 167–171, 187 and 199–200.

    State η,c > 0 and 0 < δ < 1/4. The proof's “c ≤ 1/2 may be assumed” is not automatic if one silently keeps the claimed output exponent min(η,2c). It is justified here because TW includes SID, and the quoted Ω forces η ≤ 1/2 (indeed < 1/2). Replacing c by min(c,1/2) therefore does not change the claimed exponent range. In that range η′ < 1, so the O(1) harmonic/main-term errors are absorbable. Without this explanation the displayed error bound alone would impose an extra restriction when η′ > 1.

    **Fix:** add that one-sentence justification, or initially state/prove U for 0 < η ≤ 1/2 and 0 < c ≤ 1/2 and explain the reduction. Also ensure the taper construction has transition regions of length O(w), which gives the stated derivative L¹ bounds uniformly even for very narrow θ-bands.

12. **MINOR — Logical/status labels are not consistently maintained in the summaries.** Location: lines 19–21, 33, 62, 75, 141–146, 167–171, 251–259 and 335–343.

    `SID + EPC ⇐ CNT_unif` at line 33 reads as asserting that CNT_unif proves EPC. The correct statement is `CNT_unif ⇒ (EPC ⇒ SID)` (or “under EPC, CNT_unif ⇒ SID”). Corollary L3 lacks the required PROVED label, its finite computation needs its own CERTIFIED/EVIDENCE label, and the CNT/TW status statements should be Assessment rather than bare “Open.” EPC should be explicitly labelled CONJECTURE. Separate the unconditional identity from its EPC consequence, and the Hessian computation from its heuristic interpretation, rather than sharing composite status headings.

    **Fix:** perform a claim-by-claim label pass with one of the requested labels per claim. PROVED is appropriate for Theorem U's *implication* and for Proposition P relative to the cited theorem; neither asserts TW/CNT itself. Qualify U's summary phrase “any position” by its stated central position range. The memo consistently preserves ES as open.

13. **NIT — M_t is a residue difference, not a derivative.** Location: lines 164–165.

    The **integrand** defining M_t is the derivative with respect to u of the residue main term; M_t(x,y) is its difference between x+y and x.

    **Fix:** change the parenthesis accordingly. The displayed formula and its t → 0 limit are correct.

## Verified proof details

**Theorem L(i).** The signs are correct: |P₁| = yH(L) − F_L. Q ⊂ P₃ follows from the strict lower product inequality. The possible extra k lies in `(L,L+Ly/x)`, of length < 1, and its m-interval has length < y/L < 1. These two requirements hold for fixed K and 0 < δ < 1/4 once x is large. Thus |P₃| = |P₁| + R with R ∈ {0,1}. The exact residual is

`R + 2y(H(L)−log L−γ) − [(x+y)log(1+y/x)−y]`,

which is O(1). This checks the main-term algebra and explains item 4.

**L(ii)/(iii), L1/L1′/L2/L3.** Saito et al. Lemma 19 has exactly the hypotheses used (q = 1, both shifts zero, N ≥ 1, N′ = 2N); there is no omitted central-range condition. Triangle-inequality subtraction at x and x+y is legitimate. The dyadic N²/x terms sum geometrically, λ−κ ≥ 0, and the remaining O(1) block is harmless. EPC gives `(ε′ + 1/4 − δ/2)/(1+ε′) ≤ 1/4 − δ/2 + ε′`. The covering count and harmonic correction in L1 are correct. L1′ gives `2δ = min(η/(2B+1),1/4)` under its actual uniform hypothesis. L2 is exactly the reverse use of L(iii). A(Bourgain) is `(13/194,76/97)` at ε = 0; `155/556` and `123/556` are correct, and strict inequalities permit absorbing the Bourgain ε and log x. These facts do not supply the stronger claims flagged above.

**Theorem U.** Fourier normalization and the t/2 argument are correct. The ζ identity gives constant terms g(±L₀), the pole contribution ∫_{−L₀}^{L₀}g, and the negative integral with `(g+g′)(L₀−log v)` and `(g−g′)(log v−L₀)` with exactly the stated signs. Changing variables gives the stated `2u^{-1/2}e^V` bound. The band shifts left by `(1/2)log(n/x)`, so both sandwich directions, including endpoint behavior and the narrow-band zero minorant, are correct. The derivative norms give `||ĝ||₁ ≪ log(2/w)`; the high-frequency integrals are `O_j(y x^ε (x^c w)^{1−j})`, with the logarithmic ζ tail absorbed by x^ε. For w = x^{-c/2}, the boundary cost is y^{1−2c}, yielding min(η,2c) after item 11's parameter clarification.

**Proposition P.** `(A,θA] ⊂ (A,eA] ∪ (eA,e²A]` holds including endpoints for θ ≤ e². The PDF's Corollary 1.2 really has exponent `t+1+δ(t,1)/2`. F(X) = X is admissible; t = 1 gives β = 1 and δ = 1, hence 5/2. In the fourth-root range y = 2U ≥ x^{1/5} eventually, and log log x ≍ log log U. The E1⁺ bound follows by inclusion. The alternative NT/11/4 route is consistent with the quoted class condition and partial summation. The substitution in TDCAL Prop D(iii), leaving `TU^{1/2+ε}` unchanged, is valid. A long-interval lower bound for ΣΔ_H only rules out a uniform O(y) estimate for this *unrestricted dominating sum*; it does not disprove an O(U) bound for the fixed central slice or a different argument.

## Reproduction performed

All executed external commands had timeouts ≤ 300 seconds; Python/C work used `ulimit -v 4000000`. I regenerated stats with `scripts/z56_central_stats.py`; the output is byte-identical to `data/z56/central/stats.txt`. I independently enumerated A/B words through length nine with rational arithmetic. I compiled the existing C program and directly reran the first gen10, sq10 and nsq10 inputs with `Z56_DIRECT=1`; all three output lines match the stored lines exactly. An independent SymPy divisor enumeration at x = 100000007, y = 200 gives D−Main = −247.0226287509 and Ec = −60.2513723802, confirming the memo's four-decimal check. I scanned every e10 residual, all table rows and all small controls; a 60-digit evaluation of the exact residual formula confirms item 4. These tests validate the computations subject to the centering/metadata corrections above, not the unproved hypotheses.

# Hostile review 2: Z56_CENTRAL

**Verdict: CORRECT-WITH-MINOR-FIXES. No MAJOR findings.** Theorem E is valid with its stated exponents, including uniformity at t = 0. Corollary E1 is the correct existential equivalence for each fixed K ≥ 1. The substantive mathematical and numerical corrections requested in review 1 have been made; the literal one-label-per-claim cleanup remains incomplete, and one summary still uses an overstrong “only.” Neither ES nor unconditional SID/CNT is claimed proved.

Reviewed the entire current memo, review 1, LIT_CHECK, the three relevant computation scripts, stored statistics and controls. Independently re-extracted the cached Saito et al. and Trudgian–Yang PDFs. No memo or existing script was edited.

## Findings

1. **MINOR — Review-log item 12 is not fully completed: composite status headings remain.** Locations: `Z56_CENTRAL.md:20`, `:47`, `:336`.

   “Identity PROVED; consequences CONDITIONAL” and “PROVED computation; Assessment reading” still share composite headings, despite review 1 explicitly asking to separate them. The intended distinction is understandable and the subsequent mathematical claims are correctly qualified, so this is not a false theorem. Nevertheless, the requested literal rule is one label per claim. Give the identity and its conditional consequence separate labelled statements; give Remark H's Hessian calculation a PROVED heading and the duality interpretation a separate Assessment heading. The unproved hypotheses, EPC, Corollary L3 and the finite search otherwise have the requested labels, and the erroneous implication to EPC is gone.

2. **MINOR — The proposed FRONTIER text still says the unconditional equivalence holds “only” above the numerical threshold.** Location: §10, the Trudgian–Yang bullet.

   Corollary L3 proves a **sufficient range for this exponent-pair argument**, not failure of the equivalence below that range. The main corollary and the finite-search qualification are now correct. Replace “the equivalence holds only for δ > …” by “this argument proves the equivalence for δ > ….” This is a residual wording issue from review 1 item 2, not a failure of the improved pair or its arithmetic.

3. **NIT — State E1's fixed K and admissible δ explicitly.** Location: `Z56_CENTRAL.md:240–243`.

   A fully explicit formulation is: for every fixed K ≥ 1, under EPC,

   `∃η > 0, ∃δ ∈ (0,1/4): CNT_unif(η,δ;K)` iff `∃α > 0, ∃c > 0: TW(α,c;K)`.

   The existing wording is mathematically defensible: K is inherited, and if CNT_unif is defined for a larger δ, restricting its A-range to any smaller positive δ < 1/4 suffices. Different exponent names also make clear that E1 does not preserve η or assert the equivalence at prescribed parameters. No strengthening beyond U and E is needed. Neither theorem changes K, requires a simultaneous hypothesis for all K, or supplies constants uniform in K.

## Theorem E: line-by-line audit

**Decomposition (§4.1, lines 245–253).** Correct. P₁ and Q are disjoint since L² < x. The proof of L(i) gives Q ⊂ P₃ and at most one point in P₃ ∖ Q, uniformly in the permitted y-range once x is large. Swapping k and m conjugates the unit-modulus weight, hence the non-central contribution is the P₁ sum of `2 cos(t log(m/k))`, with an O(1) remainder even for growing t. Since `log(m/k) = log(m²/x) − log(n/x)`, replacing n by x costs at most `O(|t| y/x)` per point. The bound `D(x,y) ≪ y x^ε` follows from the divisor bound and y ≍ x^{1/4}; it is unconditional.

**Abel summation and EPC (lines 250–253).** Correct, with the needed partial-sum uniformity actually present in the cited lemma. Saito et al. Lemma 19 permits every N ≤ N′ ≤ 2N, not just full blocks. For `c(v)=2 cos(t log(v²/x))`, `|c(v)|≤2` and `∫_N^{2N}|c′(v)|dv≤4|t|log 2`. Abel summation therefore multiplies the maximum partial ψ-sum by O(1+|t|). With the EPC pair `(ε′,1/2+ε′)`, its first term is at most `x^ε N^{1/2}` after choosing ε′ sufficiently small; the `N²/x` term is also bounded by this for 1 ≤ N ≤ L. The geometric sum over blocks is `O((1+|t|)x^{1/4−δ/2+ε})`. The final block below 1 contributes O(1). Apply this separately at z=x and z=x+y. No conjectural twisted exponential-sum estimate is being smuggled into this step: the twist is handled entirely by variation.

**Thin central bands (lines 254–260).** Correct. With w=x^{−η/8}, all nonempty bands have θ∈(1,e^w]⊂(1,4] for large x; the last truncated band is admissible. There are `J≤2δ log x/w+1` bands, and every lower endpoint lies in [L,L′]. The definition in §1 is uniform over **all** θ∈(1,4], including these x-dependent thin bands. Thus its constant and starting threshold do not deteriorate with J. The phase changes by at most `2w+y/x`, and `∑S_j≤D(x,y)`. Summing the hypothesis errors costs `J y^{1−η}`. Replacing the frozen weights in the harmonic main terms costs `O(|t|w y log x)`, since the band harmonic sum is O(log x). These are precisely the displayed central errors. Uniformity only for θ=4 would not suffice, but that is not the hypothesis used here.

**Euler–Maclaurin and signs (lines 261–266).** Correct. The two finite sums are exactly

`Main_t/y = x^{−it}∑_{m≤L′}m^{−1+2it} + x^{it}∑_{m≤L}m^{−1−2it}`.

In `∑_{m≤X}m^{−s}=ζ(s)−X^{1−s}/(s−1)+R(s,X)`, the remainder on Re s=1 is uniformly `O((1+|t|)/X)`. Consequently the first sum contributes **plus** `(L′²/x)^{it}/(2it)` and the second contributes **minus** `(x/L²)^{it}/(2it)`. Since L′=x/L, these cancel exactly, not approximately. The remaining zeta terms are exactly the two terms defining G(x) in §4, in reverse order. There is no sign reversal and no missing factor 2.

**Near t=0 and comparison with M_t (lines 265–267).** Correct. The Euler–Maclaurin remainder has no 1/|t| loss. After combining the poles,

`ζ(1+2it)x^{it}+ζ(1−2it)x^{−it} → log x+2γ`.

The finite sums are continuous in t, so the uniform remainder estimate extends to zero. Also

`G′(u)=(it/u)[ζ(1+2it)u^{it}−ζ(1−2it)u^{−it}]`.

For |t|≤1, boundedness of `tζ(1±2it)` proves O(1/u) uniformly, without requiring t log u to be small. For |t|≥1, the usual bound on ζ on Re s=1 gives the stated `O((1+|t|)log(2+|t|)/u)`. Integrating proves the claimed `M_t−yG(x)` bound; at zero, M₀ is exactly Main from §1.

**Exponent bookkeeping (lines 268–270).** Correct. Let r=min(δ,η/4). The three potentially largest errors, expressed as powers of y, are

- non-central ψ-error: `y^{1−2δ+4c+4ε}`;
- summed band errors: `y^{1−η/2}log x`;
- phase freezing: `y^{1−η/2+4c+4ε}`, also covering its logarithmic harmonic counterpart after an arbitrarily small ε loss.

For c=min(η/16,δ/4), their savings are at least δ, η/2 and η/4 respectively. The omitted terms really are smaller: O(1); `O(x^{−1/2+c+ε})` from replacing n by x; `O(x^{−1/4+δ+c})` from Euler–Maclaurin; and `O(x^{−1/2+c}log x)` from integrating G. Here c≤δ/4<1/16 and r<1/4. All are absorbed by `y^{1−η″}` for every positive η″<r. Choose ε small relative to r−η″ and absorb logarithms; the displayed reuse of ε is conventional harmless relabelling. No preliminary restriction η<1/2 is needed for this proof.

## Corollary E1 audit

From CNT_unif with any admissible positive η,δ, E supplies a positive c and any positive η″<min(δ,η/4). Conversely, U supplies CNT_unif for every prescribed δ∈(0,1/4), with any positive output exponent smaller than min(η,2c). Thus the existential equivalence, for the same fixed K, follows exactly. It is not an equivalence with SID alone, with prime/tied CNT, or with CNT at the same numerical exponent. The summaries consistently retain EPC and the strengthened uniform hypothesis when asserting the twisted equivalence.

## Audit of all 13 review-log fixes

| Review 1 item | Result in current files |
|---|---|
| 1 — fixed-band/CNT_poly bridge | **Applied.** B≥0, common thresholds, all real x, decoupled y and the x-dependent λ-range are explicit. The automatic bridge is withdrawn in §3 and the summaries. No new quantifier error. |
| 2 — unconditional exponent pair | **Applied mathematically.** TY Lemma 1.1 is quoted in the LIT_CHECK addendum; the pair, θ=8093/28960 and δ-threshold are correct. Seeds include all four TY pairs; no global optimality is asserted by the search. Residual summary wording: finding 2. |
| 3 — TD ⇒ DC logarithm | **Applied.** P2's positive Fejér kernel gives a 1/H-local count without summing 1/h. H=floor(U^η) implies 1/H≤2U^{−η}; covering then gives the stated loglog-loss version at the advertised scale. It does not prove unrelaxed DC, and the summary explicitly says “with a … loss.” |
| 4 — wrong residual | **Applied.** C header and code use FLc=−F_L and `resid=Derr−(Eband+2FLc)`. Direct data have separate log/harmonic residual columns; non-direct data are explicitly proxies. The scanned maximum is 0.6319 at the stated input, agreeing with 0.632. |
| 5 — literature/sup-norm wording | **Applied.** Endpoint route, cited Ivić–Zhai estimates, Li–Yang improvement, search-limited status and η<1/2 all appear. The unsupported finite-twist “open” claim becomes “not addressed here.” |
| 6 — search depth | **Applied.** `range(10)` evaluates depths 0 through 9, and generation stops after depth 9. Exact fractions and the displayed leading objectives reproduce. |
| 7 — Table 8.2/readings | **Applied.** gen16 ends at 1.69, observed ranges and negative biases match the regenerated statistics, and only sample RMS F_L is asserted to decrease. |
| 8 — first-sample/range metadata | **Applied.** Table 8.1 distinguishes first-sample y/model from per-observation normalization; wide square-family ranges and the common-index convention are disclosed. Stats regeneration is byte-identical. |
| 9 — small controls | **Applied.** U=3–54, the out-of-convention U=3 case, absolute maximum and sqrt(y)-normalized maximum are correctly identified. Independently rescanned. |
| 10 — Hessian/formal duality | **Applied mathematically.** Determinant zero/rank one is stated; weighted regrouping and the absence of an applicable standard Voronoi formula are explicit. Composite heading remains: finding 1. |
| 11 — U parameters/tapers | **Applied.** η,c>0, the Ω-based reduction and output-exponent preservation are justified. Transition-width and derivative L¹ estimates are uniform for narrow bands, including the zero minorant. |
| 12 — status labels | **Mostly applied.** EPC, L3, finite search, hypotheses and implication direction are fixed; strict one-label-per-claim formatting is not fully done (finding 1). |
| 13 — residue terminology | **Applied.** The integrand is described as a derivative and M_t as the difference of residue main terms. |

No substantive new analytic error is introduced by these fixes.

## Reproduction and scope

All executed shell commands used `ulimit -v 4000000` and individual timeouts ≤120 seconds. Re-extracted Saito Lemma 19 and TY Lemma 1.1 directly from cached PDFs; ran the rational pair search; regenerated statistics byte-identically; compiled the C program and reran the first gen10, sq10 and nsq10 inputs with direct band counts, byte-identically; scanned all 2400 stored logarithmically centered residuals and all small controls. Compilation succeeds with an existing misleading-indentation warning at C line 42 (two independent if statements); it does not affect these results. No full large-x rerun was necessary or performed.

ES is repeatedly and correctly declared open. U is an unconditional **implication**, E is conditional on EPC, and neither TW nor CNT_unif nor SID is asserted established. The unconditional new count bound remains Proposition P, not a power-saving central-slice asymptotic.

# z58 FRONTIER / summary consistency review

**Verdict: ACCEPT-WITH-FIXES. ES and (MS) remain OPEN.** Review of `side-agent/z58-summary` at
`e86eb46440fde0aa6edc9da34f0e65c8e3660667`, against the sixteen lane memos and cross-model reviews on
`main` at `345b35500a576d504efa202af36293c252fb9907`, and `/home/pasky/projects/math/z52bbriefs/z58_summary.md`.
Locations below use the reviewed branch's line numbers. This is an export-consistency review, not a new proof audit
or a rerun of the production censuses. All sixteen memo/review pairs were compared; candidate findings from three
independent source-comparison passes were adjudicated against the source statements.

The principal copied numerical values agree with the memos/reviews: TRYO's 355 096 166 and four component counts;
LADDER's 128 491 751 / 585 009 682, 9 / 18 zeros and 17 401 609 cutoff; LOGIC's 486 / 16 and 0.1246 / 0.1189;
DISPROOF's 868 562 / 777 973, exact sample endpoints and both new R₈ zeros; WITNESS's records and 201 / 97 maxima;
WILDCARD's 4545, 22 / 107, 142 and eight d-odd zeros; FFIELD's displayed census tables. The problems below are
primarily scope, attribution and verification-status compression, not changed digits.

The detailed Kandukoori–Ramesh–Kumar priority note is substantially faithful: July PDF/commit dates, nine analytic
axioms in July, October standard-axiom CI closure, no local rebuild or fresh analytic audit, unknown public-access
chronology, and no supersession of count-note A–D are all retained. Do not turn that into established public priority
or independent development. The paper-side changes correctly remain proposals requiring the user.

## Required corrections, priority order

1. **Reconcile the new BM theorems with the existing square-screen text.**
   **Location:** `FRONTIER.md` §4 items 1 and 13, lines 583–586 and 645–654; new §3 BM block, lines 523–534.
   **Current:** “Local/genus/spinor/Siegel–Weil/BM-type steps are all true at m²”; “There is no BM obstruction at any
   n ≥ 2”; then the new text says the positive-integral BM set is empty iff n is a square, followed by “Every known
   zero is a non-BM failure”. Item 13's reference to U_n supplies its intended scope, but item 1's blanket
   assertion about BM-type steps is now false on the two newly analysed models; make the distinction explicit.
   **Corrected:** “The older local/genus screens do not by themselves force a point. On the all-solution ES surface
   U_n, the positive-integral BM set is nonempty for n ≥ 2. In contrast, on the displayed (★) surface and Type II
   threefold, for n ≥ 1, positive-integral BM nonemptiness detects exactly non-squareness (numerator 8: exclusion of
   □ ∪ 2□). Thus BM itself does fail at squares on these models, but nonemptiness is not sufficient for a positive
   integral point.” Replace “Every known zero” by “The listed known non-square zeros, on their respective models”.
   Add `n ≥ 1` to the exported emptiness criterion. Retain the positive-real-region qualification; without it these
   models have integral points at every n.
   **Source:** `Z58_STRUCT.md` Thm A(vii), §1 object distinctions and §3 contrast with U_n; `Z58_STRUCT2.md` Thm B(viii),
   Thm 4.1; `REVIEW_STRUCT.md` required fix 1 and `REVIEW_STRUCT2.md` model/positivity qualifications. The new theorem
   requires repairing this pre-existing FRONTIER wording, not silently changing the meaning of “BM”.

2. **Remove the universal proof-organization requirement reintroduced after review.**
   **Location:** `Z58_SUMMARY.md` §2 lesson 4, lines 133–134; §5.1, lines 255–256;
   `FRONTIER.md` §7.18, lines 2012–2013.
   **Current:** “Every surviving mechanism-level idea must therefore produce a Type II witness with (n/f) = −1 at a
   fixed p, cross B2, and use non-squareness at a named step”; “Any mechanism must…”; “What a mechanism needs…”.
   **Corrected:** “PROVED witness constraint: for odd positive n, every positive Type II witness supplies
   f = 4acd − 1 with (n/f) = −1.
   Assessment / proposed strategy: seek a pointwise Type II construction using non-squareness and resolving the tied
   divisor-class event. This is not a necessity theorem about how every proof of CONV-II, (MS-II), or ES must be
   organized; no such mechanism was found.” Keep the existing caveat that c ≥ 2 is a strategy, not forced at 10¹⁷.
   The summary's Assessment heading and FRONTIER's general scope disclaimer help, but the universal “must” wording
   should not override the source's explicit witness/proof distinction.
   **Source:** `Z58_CONVF.md` §0, lines 9–11, expressly says this is “a necessary feature of witnesses, not a theorem
   about how proofs must be organised”; `REVIEW_CONVF.md` Lemma 1.3 finding, Autopsy scope, F1 and required fix 1;
   `REVIEW_TRYF.md` full-spectrum/proof-technique finding; existing `FRONTIER.md` §4 scope paragraph.

3. **Restore the threshold alternative in the C-even screen.**
   **Location:** `FRONTIER.md` §4.2, lines 612–613; `Z58_SUMMARY.md` §2 character-layer/surrogate F2 cell, line 103.
   **Current:** “one through the c = 1 line needs a step that fails on the C-even sub-line”; “only even-C-positivity
   arguments are ruled out”.
   **Corrected:** “An argument that also proves C-even positivity over a range containing a certified R₈ zero is
   refuted. It must distinguish that sub-line, or use a threshold excluding those zeros. The new zeros require
   P₈ ≥ 23 296 553 281 for a claim over p > P₈ in 𝔐; they do not refute eventual C-even positivity or an argument
   starting at 10¹⁷. For full numerator-8 Type II, the prime census requires P₈ ≥ 35 569 for p > P₈, but does not
   prove positivity beyond that cutoff.” In the summary cell say “only even-C positivity claims whose asserted range
   includes the zeros are ruled out”.
   **Source:** `Z58_TRYF2.md` §0 F2 and §4(b), `REVIEW_TRYF2.md` required fix 1; `Z58_TRYF.md` §0 F2 and
   `REVIEW_TRYF.md` F2 finding; `Z58_DISPROOF.md` §4 new zeros; `Z58_WILDCARD.md` numerator-8 census.
   The old paragraph immediately above the addition already preserves “or a larger threshold”; the addition drops it.

4. **Keep the polynomial hypothesis in the one-parameter rigidity export.**
   **Location:** `FRONTIER.md` §3 Mordell case splits, lines 536 and 542–544; apply the same precision to the summary's
   MORDELL scope description where necessary.
   **Current:** “every integral positive one-parameter (★) family lies in one H_d residue or one K_{u,B} class”;
   “polynomial certificates U, B, C ∈ ℚ[x, y] … have two constant coordinates, so they reduce to fixed-modulus congruences”.
   **Corrected:** “Lemma P: if nonzero U, B, C ∈ ℚ[t] satisfy 4UBC − U − B = a + Mt identically, with integers a and
   M ≥ 1, two coordinates are constant. When they give positive-integral certificates, the family is contained in
   one H_d residue or K_{u,B} class.” For C1 retain the algebraic rigidity statement, but write “The congruence
   interpretation assumes the constant coordinates are positive integers and the identity supplies a positive-integral
   solution at some point with f > 0.” Arbitrary one-parameter algorithms, rational or piecewise families are not covered.
   **Source:** `Z58_MORDELL.md` §2 Lemma P and §5 Prop C1 / Arithmetic corollary;
   `REVIEW_MORDELL.md` Lemma P finding, required fix 1 and the explicit reminder that C1's positivity/integrality
   hypotheses are essential. “One-parameter” without “polynomial identity with affine parameter n” loses the theorem's
   main restriction. The C1 sentence is a clarification of what “certificates” means, rather than a separate
   allegation that the export intentionally includes non-positive solutions.

5. **Make the automorphic class, proxy validity and prime-set quantifiers explicit.**
   **Location:** `FRONTIER.md` §3, lines 503–510; `Z58_SUMMARY.md` AUTOMORPH row, line 69, §2 lesson 3 and §6 scope list.
   **Current:** “GL₂ Hecke eigenvalue systems of integral weight, their n^j-twists”; “Collision-freeness holds at a
   positive-density set of primes”; summary: “no a ∈ ℋ_M equals R on n ≡ 1 (4)”. The exports do not define “valid and
   effective”, and their escape wording singles out prime-only arguments with error outside ℋ.
   **Corrected:** “For each fixed finite combination in 𝓗_M: holomorphic newform/Eisenstein eigenvalue systems of
   integral weight k ≥ 1 and level dividing M, their n^j-twists (j ≥ 0 integer), and the specified character-weighted
   real-parameter divisor sums with finitely many derivatives. At odd primes p ∤ M, Theorem A applies. Its
   positive-density collision-free prime set depends on the chosen combination; no common positive-density set for
   all 𝓗 is asserted. Valid means a(n) ≠ 0 implies R(n) ≥ 1 for every n ≡ 1 (4) coprime to M; effective means a(p) ≠ 0
   at every sufficiently large 𝔐-prime in the domain. No such proxy exists, and no a ∈ 𝓗_M equals R on all n ≡ 1 (4)
   coprime to M.” Preserve the existing square-vanishing and no-±-collision hypotheses when inserting this wording.
   Add: “Prime-only support/equality does not provide square vanishing and is not excluded by this
   theorem.” Carry the analogous prime-only-support escape into the TERNARY caveat list as well.
   **Source:** `Z58_AUTOMORPH.md` §1 Q2, §2 definition, Thm A and Cor A1(a–c);
   `REVIEW_AUTOMORPH.md` definition finding, Density and quantifiers, required fix 4. For TERNARY:
   `Z58_TERNARY.md` §4.3, line 269, and `REVIEW_TERNARY.md` proof-audit point 6.
   The class is not all GL₂ automorphic systems, and validity at primes alone is a different hypothesis. The
   per-proxy prime-set qualification is protective precision: the current wording does not explicitly assert a
   universal set. The principal repairs are the holomorphic class restriction and all-integer validity.

6. **Do not call the brute-force Q-refutation “short”; keep the Mordell domain of witnessing.**
   **Location:** `FRONTIER.md` §3 Logic, lines 562–565; `Z58_SUMMARY.md` §2 Logic row, line 104; §5.2, line 261;
   `FRONTIER.md` §7.18 calibration, lines 2019–2020.
   **Current:** “a counterexample has a short Q-refutation”; “each zero is a short Q-refutation of the rung below it”;
   “must … factor any composite zeros above 10¹⁷”.
   **Corrected:** “A counterexample p gives a brute-force Q-refutation of length p^{O(1)}, not a known
   poly(log p)-length refutation. For a class-restricted rung the zero must belong to its domain.” For witnessing:
   “An S¹₂ proof of (MS) yields a polynomial-time hit-or-nontrivial-factor-pair algorithm on n > 10¹⁷ with
   n mod 840 ∈ 𝔐; it must find hits at those primes and split any composite R-zeros in that domain.” This is neither
   a general factoring algorithm nor a complete-factorization guarantee.
   **Source:** `Z58_LOGIC.md` Prop 2.1(b), proof and length remark; Thm 3.1 / Cor 3.2;
   `REVIEW_LOGIC.md` per-claim findings explicitly distinguish p^{O(1)} from poly(log p) and zero composites from
   general factoring. The surrounding MS⁺ discussion suggests the Mordell domain, and FRONTIER's §3 already names
   it; the requested local qualification makes the compressed witnessing statements unambiguous when reused.

7. **Restore the unit restriction in square cancellation and the analytic domains.**
   **Location:** `Z58_SUMMARY.md` §2 character-layer/surrogate F1 cell, line 103; §0 surrogate bullet and TRYF row;
   `FRONTIER.md` §2.4 TRYF bullets, lines 270–272; summary's bare TRYF2 Theorem A formulas in §§0–1.
   **Current:** “the Jacobi layer cancels L₀ exactly”; displayed TRYF layer bound and “Thm 3.2 is CONDITIONAL on HCE(δ)”
   without their prime congruence domains or the unevaluated onset.
   **Corrected:** “For n = m², on the unit-restricted sum gcd(d,m) = 1, the Jacobi layer cancels the principal layer
   termwise; non-unit d cannot be hits and are excluded.” State the layer theorem for primes p ≡ 1 (4), asymptotically
   (equivalently the source's ε-dependent bound, p ≥ p₀(ε), 3 ≤ X ≤ 2p). State HCE(δ) for a fixed δ > 0 and all
   sufficiently large primes p ≡ 1 (24), and its conditional conclusion in that same domain. “No numerical onset is
   evaluated.” In the summary write TRYF2's bound as “M₂(p) ≥ c₀ log²p for every sufficiently large prime
   p ≡ 1 (4)” (FRONTIER already states this correctly). When discussing HCE against the twelve original R₈ zeros,
   retain that only six are in its 1 mod 24 domain.
   **Source:** `Z58_TRYF.md` §0 F1/F3, Thm 2.1 and remarks, §3 HCE / Thm 3.2;
   `REVIEW_TRYF.md` F2/F3 discussion and required fixes 2–3; `Z58_TRYF2.md` §3 Thm A and
   `REVIEW_TRYF2.md` Thm A finding. The unrestricted principal sum at a composite square is not the sum to which the
   cancellation assertion applies. The o(1) notation already signals an asymptotic statement; the analytic-domain
   additions make its scope explicit rather than correcting a claimed numerical threshold.

8. **Reconcile the global CERTIFIED definition with the disclosed partial re-verification.**
   **Location:** `FRONTIER.md` Labels, lines 12–14, versus new §2.4 census bullets, lines 246–252.
   **Current:** “CERTIFIED = an exact finite computation, independently reproduced”; TRYO and LADDER then explicitly
   say “One engine” with independent checks of 8 732 primes / 42 832 inputs rather than the entire production ranges.
   **Corrected:** Add an explicit convention: “For the z58 data, CERTIFIED denotes the exact finite computation in the
   cited memo, with its stated engine and independent-check coverage. It does not mean a second full-range census;
   the ranges independently reproduced or checked pointwise are specified separately.” Alternatively narrow the
   global definition consistently. Do not change the numerical claims to EVIDENCE merely because the complete census
   was not independently rerun: that would disagree with the source classification.
   **Source:** `Z58_TRYO.md` §8.6, `REVIEW_TRYO.md` Numerical audit; `Z58_LADDER.md` §2 and review log,
   `REVIEW_LADDER.md` zero-census finding. Both reviews explicitly accept one-engine high-range certification with
   partial independent checks. This is an inconsistency in the global wording, not a hidden defect in those disclosures.

9. **Correct the literal lane-verdict attribution.**
   **Location:** `Z58_SUMMARY.md` §0, lines 20–22, and §6, lines 288–289.
   **Current:** “Every lane's verdict is ‘narrowed’, except WILDCARD…”; “Every z58 lane says ‘narrowed’…”.
   **Corrected:** “No lane supplies a HOT LEAD. The structured probes report ‘narrowed’; TRYO, TRYF, TRYF2 and CONVF
   report no proof/no pointwise mechanism, not an exhausted target. WILDCARD reports ‘strengthened (choice of target) /
   inconclusive (mechanism)’.” If a single campaign-level “narrowed” reading is desired, label it Assessment rather
   than attributing that literal verdict to every memo.
   **Source:** `Z58_TRYO.md` title/status, `Z58_TRYF.md` status and §7 verdict, `Z58_TRYF2.md` status and §6,
   `Z58_CONVF.md` status; `REVIEW_CONVF.md` opening explicitly calls the all-large-prime target INCONCLUSIVE;
   `Z58_WILDCARD.md` one-line verdict and §6. This is a status-label correction, not evidence of a new lead.

10. **Do not downgrade the fully checked DISPROOF sample to a partial cross-check.**
    **Location:** `Z58_SUMMARY.md` §6 finite-data caveat, lines 290–293; qualify §3's blanket verification introduction
    if it is intended to include the sampled search.
    **Current:** “The censuses (… DISPROOF samples) are one-engine certificates with partial independent checks.”
    **Corrected:** “The large interval censuses have the engine/cross-check coverage listed in §3. DISPROOF is a sampled
    search, not a census; every one of its 868 562 inputs was independently checked for primality and for an explicit
    R/𝔊* witness. Both new R₈ zeros were independently exhaustively enumerated. This still gives no interval-wide
    completeness claim.”
    **Source:** `REVIEW_DISPROOF.md` Independent numerical verification, especially the all-868,562 witness check;
    `Z58_DISPROOF.md` §7.1. The summary's own §3 already states the stronger verification correctly.

11. **Use the literature audit date, not the Lean commit date, for the addendum.**
    **Location:** `FRONTIER.md` opening addendum, line 10.
    **Current:** “literature addendum to 2026-10-30 in Z58_LIT.md”.
    **Corrected:** “z58 literature addendum, sources accessed/searched 2026-11-05 (`Z58_LIT.md`); bounded searches,
    not a completeness guarantee. The K-R-K standard-axiom CI closure is at the 2026-10-30 commit.”
    **Source:** `Z58_LIT.md` opening verification conventions, §1 Q1 and §2.4 API/search status;
    `REVIEW_LIT.md` review date and chronology checks. Keep the detailed §1 priority qualifications unchanged;
    the date clarification is not a finding that the detailed priority note overclaims public priority.

12. **Point the extended R₈ list to the files that actually contain it.**
    **Location:** `FRONTIER.md` §4.2, line 605.
    **Current:** after the two new zeros, “The screen is in data/z58/screens/.”
    **Corrected:** “The original twelve-zero screen is `data/z58/screens/r8_zeros_1e10.txt`; the two new zeros are in
    `Z58_DISPROOF.md` §4 and its archived `data/z58/disproof/runA/` / `runB/` runs, independently verified in
    `data/z58/xreview/REVIEW_DISPROOF.md`.”
    **Source:** source-file grep: neither new zero occurs in `data/z58/screens/`; `Z58_DISPROOF.md` lines 142–143 and
    §8 archived-run pointers. This correction does not require changing or regenerating the screen files.

No changes to the summary, FRONTIER, source memos, papers, or screen data are made by this review.

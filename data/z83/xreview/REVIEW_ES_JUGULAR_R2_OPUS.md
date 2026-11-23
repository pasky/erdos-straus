<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="9c4050395">
A separate reviewer subagent was asked to review the changes in `git log 9c4050395..`. Its request and review follow.

Request: review changes since 9c4050395 carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Full hostile cross-lab Claude Opus Round-2 review of Wave z83 Lane 7, notes/z83/ES_JUGULAR.md §§5–9 and §0. Try to falsify the distinction U versus the explicit oracle theory, the standard-progression theorem for Euclid/Farey/Gauss/DL with adversarial choices, strict T1 transport, and the uniform fibre classification in monic function fields including the specialization/valuation proof. Compare Lane 1 bb06ac1bc and Lane 8 ef857a629; check F1–F4. Independently replay representative small numerical tests (cap any replay at ≤15 min; no need to rerun the old slow census).

Commit log:
commit 2f698f9d1760557db3252ee9e837460653656c21
Author: Petr Baudis <pasky@ucw.cz>
Date:   Mon Nov 23 05:29:58 2026 +0100

    Separate standard Euclidean digit traps from square specialization; classify large-field ES fibres

 data/z83/es_jugular/r2-ffib.txt   | 46 +++++++++++++++++++
 data/z83/es_jugular/r2-otherA.txt | 35 +++++++++++++++
 data/z83/es_jugular/r2-words.txt  | 29 ++++++++++++
 notes/z83/ES_JUGULAR.md           | 93 +++++++++++++++++++++++++++++++++++++--
 scripts/z83_jug_ffib.c            | 55 +++++++++++++++++++++++
 scripts/z83_jug_words.py          | 38 ++++++++++++++++
 6 files changed, 292 insertions(+), 4 deletions(-)

Review:
**Verdict: accept with fixes.** I found no mathematical error in §§5–9. The main fixes are to the §0 block and to triage and attribution, plus a few smaller substantive notes.

## What I replayed (under 15 minutes in total)
- **`z83_jug_words.py`:** the output matches `r2-words.txt` byte for byte, and all built-in assertions pass. I also checked p=37, a=8, b=14 (m=3, r=3, t=5) and the counts quoted for both R₈ zeros by hand.
- **`ffib`:** I compiled it and ran 12 representative rows: q=5,7,11 at (2,1), (3,1), (3,2), (4,1), (4,2), plus two other-A rows. All match the data files exactly.
- **An independent brute force** that shares no code with `ffl_es.c`. For q=5 and 7, A=T, n=2, it searches all monic X and all Y of degree ≤6 and solves for Z. It matches the note's closed form (b=−1,−2, or one of v, bv, bv² equal to −1) for every P, and the per-fibre totals (8/10 and 15/21) agree.
- **Theorem C's polynomial semantics for Euclid:** I ran a symbolic Euclid run over ℚ[N] with adaptive refinement on 300 random pairs. At N=1+m·t, t≈10¹², it matches integer Euclid quotient by quotient with no mismatch.
  - With a *fixed* modulus, the Euclid length is not constant, because constants like 346 = 2·173 and 64 appear. So the step "refine the neighbourhood at every step" is essential, and the note does say so.

## Substance, by the attacks you asked for

**1. U versus the oracle theory U_𝔒 (§6).** The distinction holds.
- T_Π satisfies every axiom of U_𝔒: `IOpen` gives the algebraic floors (integer-part property), z82 §2 gives Farey on real-closure targets, and Lane 1 §§6–8 give DL, Lag and reduction with a matrix.
- The best-approximation argument from the local bracket is right. Outside the bracket the two errors add with the same sign. In a tie at the mediant, "smaller denominator" picks q_{n−1}, the regular convergent.
- The induction-rule construction of rational Farey inside U is sound.
- **Sharpening to add:** real-closure Farey already follows from `IOpen`, a Bézout row and rational Farey (take the floor of Q²t, then apply the z82 §2 lemma). So U_𝔒 sits inside U+Lag, and Lag is the only piece not known to be in U. Say this explicitly.

**2. Theorem C under adversarial choices.** Correct.
- Euclid terminates as a formal run: on equal degrees it is rational Euclid on the leading coefficients, and on unequal degrees the remainder has degree at most that of the divisor.
- The Gauss argument is right: the convergents dominate every competing vector, both roundings at denominator 1 are needed, and the shear completes the reduction.
- The DL argument works: transcendence of α_l freezes the valuations at the bad places, and the D-escape is a genuine divisor of h coprime to b. The N=1+2^s example is valid; 17 is a 2-adic square but not a rational one.
- The square specialization is right: zero constant term gives a multiple of m², a nonzero one gives a unit mod m, and at least one of each sort occurs.
- **Caveat to state in the note:** these are fixed-length straight-line programs with no loops. That is far from a Herbrand menu of a U-proof, which can use the witnesses of arbitrary induction-rule theorems.
- **Sharper form to add:** the host version also yields that the gate axioms plus all true universal ordered sentences (DC) do not prove ES.

**3. Strict T1 transport (Lemma D and §8).** Correct.
- The signed triple and (3,10,90) at 9 both check.
- The control n=3k−1 with (n,k,nk) checks: k+n+1 = 4k.
- The gcd exceptional classes (T,T+2 and T,T+3) are correct.

**4. Theorem E, the fibre classification.** I checked it line by line and found no gap.
- **Positive certificate:** with X=(P+D)/A we get E=D, and D divides P+X.
- **Same-side pairs at X=(T−u)^d:** every root is u plus a constant, so only E=1 or 2 is possible.
- **Mixed pairs:** the valuation at u=β excludes a factor T−u in E.
- **Valuation at u=∞:** unbounded roots have valuation −1 and bounded roots satisfy v(w−γ)=e/k_γ. Then t=e and s_γ=k_γ follow from C(γ)=1.
- **A proper selection is impossible:** the coefficient of V^{s′} has a unique minimal term of valuation −t′<0, yet it must be a constant.
- **e=0:** reduction puts E in 𝔽_q[T].
- **Counting:** the zero bound on a nonzero coefficient polynomial gives the count. Sharpness, via the AP modulo AL, is fine.

**Data caveat (should be stated):** for n=4, k=1 the ratio maxOther/q² keeps rising: 2.0, 2.9, 3.3, 4.0, 4.3, 4.9, 5.5 for q=7…29. So the data neither confirm nor refute the exponent at n=4. At n=3, k=1 the ratio levels off near 4.7.

**5. Comparison with Lane 1 (bb06ac1bc) and Lane 8 (ef857a629).** The note is consistent with both. Lane 1 scopes T_Π's `IE₁⁻` status as unknown, and the note does not overclaim.
- Lane 8 §4 already has the parsimonious host, Euclid, DL, rational Farey, standard traps on progressions and the corollary for its U_X fragment.
- What C genuinely adds is Gauss reduction with a matrix (a non-linear witness block, outside Lane 8's U_lin), the resultant-based DL that needs no parsimony, and supplied-seed Newton lifts.
- The §7 PID paragraph largely repeats Lane 8's parsimonious construction without credit.

**6. Falsifiers F1–F4.**
- **F1:** passes. Polynomial evaluations can only give strict square patterns.
- **F2:** passes. C is a failure theorem, so numerator-8 failures cannot contradict it, and the word decoder works mod 4.
- **F3/F4:** the note makes no positive claims there, so there is nothing to falsify.

## Fixes required
1. **Review line.** §0 still describes only round 1. Mark C and E "cross-review owed" until this review is archived.
2. **Regression in §0.** The Result line no longer mentions Theorem B, which round 1 asked to be recast. The Scope also lost two caveats: "no interior bichromatic pair" and "the family criterion selects a divisor ratio; the rank bridge does not". Restore all three.
3. **Triage.**
   - "RECORD inherited only" is not a triage class and repeats round 1's RECORD/STATUS inconsistency; use none, with a pointer to Lane 1.
   - C is not BARRIER-BROAD. It is the H-free strengthening, for one named gate class, of the existing STATUS row "Finite procedures fail at trap points". Merge it with Lane 8 §4 into one FRONTIER entry, and consider a one-clause STATUS update there.
   - E as HEADLINE is too strong, since it concerns the function-field analogue in the regime where that analogue is already false. RECORD or BARRIER-SCOPED fits better; the one-clause STATUS append is fine after review.
4. **Attribution.**
   - FUNCTIONFIELD_ES §1 only has R=−1 and −2. The −D family with D dividing A+1 also appears in `EXSET_FUNCTION_FIELD.md` Definition 1.4, for the U_q analogue; cite it.
   - Credit Lane 8 for the §7 PID paragraph.
5. **Six versus eight.** §9 first says at most eight successes at n=k+1, then proves six. Make six the headline and tighten the script's ≤8 assertion to ≤6; the data are consistent (maximum 4 at k=1, 3 at k=2).
6. **Readability.** §§6–8 are dense and repetitive with defensive non-claims, which round 1 already flagged. Compress them.

I edited and committed nothing in the repo. The replay scripts and the binary are in `/tmp/rv83`.
</code-review>
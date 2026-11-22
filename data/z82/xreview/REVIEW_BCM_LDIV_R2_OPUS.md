<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="6001c6b4f">
A separate reviewer subagent was asked to review the changes in `git log 6001c6b4f..`. Its request and review follow.

Request: review changes since 6001c6b4f carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Full hostile Round-2 Claude Opus cross-lab review of Wave z82 Lane 2B (notes/z82/BCM_LDIV.md §§6–9, §0; also inspect scripts/z82_bcm_matching.py and data/z82/bcm_ldiv and distinguish their scope). Verify model/valuation/PA-word/counting/leastness/order arguments and cross-lane compatibility at cited refs. Pressure-test first-residue coherence at every free, row, sphere and square-safe edge, primes outside C, pre-entry/old freezes, matching concentration, quadratic no-minimum and principal-unit rank. List every error, scope or replay issue and give an explicit verdict. No edits. Cap any replay at ≤15 minutes, ulimit -v 6000000, ≤2 compute processes, Python via uv run --offline --no-project python -B. ES in ℕ is open.

Commit log:
commit 8112b2172a0fa577e57f59cf829c9dc8ffe7a122
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sun Nov 22 20:49:12 2026 +0100

    Mark Round 2 cross-review outstanding after provider authentication failure

 notes/z82/BCM_LDIV.md | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

commit 3decd62d1f01afdb9d4e2a87370415c43d239fb5
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sun Nov 22 20:48:47 2026 +0100

    Coordinate squarefree residue words and separate quadratic leastness at second precision

 notes/z82/BCM_LDIV.md | 86 ++++++++++++++++++++++++++++++++++++++++++++++++---
 1 file changed, 81 insertions(+), 5 deletions(-)

Review:
**Verdict: ACCEPT WITH FIXES.** I found no mathematical error in §§6–8. §9 holds as far as I could check its cited refs. The fixes are about scope, form and the export text. They should be applied before §§6–9 are exported. This review covers Round 2 of z82 Lane 2B (`notes/z82/BCM_LDIV.md` §§6–9 and §0, commits `3decd62d1` and `8112b2172`). I checked it against z81 `FAREY_PROOF` §§2–4, 7, 11–14 and Lane 2A `FAREY_IE1` at `ff4a75afe`. I only re-checked the z81 machinery where §6 changes it. ES in ℕ remains open, and nothing here is a CLAIMED proof.

## Replays (limits respected: ulimit -v 6000000, one process, about 2 s in total)
- **`scripts/z82_bcm_matching.py`** runs and its output matches `data/z82/bcm_ldiv/matching.txt` byte for byte. Its scope is §1's (Q) only. Neither the script nor the data covers §§6–7, and the note does not claim they do (§5 says EVIDENCE for §1).
- **My own toy check of §7's (Q2)**, written to `/tmp/q2r/q2.py` with no repo edits. Setup: A=512, 74 retained primes, a random perfect matching, word (2), 6 planted matched pairs, the non-planted second-digit rule, and CRT modulo h². I checked every divisor t of h² in (A⁴,16A⁴); only exponent patterns summing to 4 can land there. The hits are exactly the 6 planted products (pq)², and t=A⁴ is not a hit. The first digit (2) points to at most 2 partners, and 2 occurs, so the "at most two" lifting count is tight. Second-digit uniqueness holds. This is a finite check of the arithmetic only. It tests neither the counting in PA nor the no-minimum statement.

## Substance
- **§6 word lemma.**
  - The bound K^N ≤ τ(m)^⌈log₂K⌉ lands in C.
  - The union bound over the old divisor list gives ≤ τ(m)K^N/T.
  - Restricting to a subset of density ≥1/c costs a factor c, so T∈C exists. The Skolem cells keep C initial.
  - Divisors of m stay old in the host because τ(m)∈C.
- **§6 (C1).**
  - Normalized tests reduce to nonzero polynomials. Every polynomial over the old residue field lifts to a normalized test, so "no bad prime above C" really does give a generic embedding of the residue field.
  - The kernel is exactly mR: x/m lies in A and is integral everywhere.
  - The cases all hold: free lines, rows (PA chart partition by the content of b, coprime contents), spheres (U≠0 chart, degree ≤3e, smooth even when s̄=0), the seed (restriction along P=(1+LZ)²), Dirichlet lines (primitive first) and primes above C (never entered).
- **Pre-entry and old freezes.**
  - When a labelled prime enters, its word value avoids every test frozen earlier: tests frozen before the cohort was declared are excluded from the options, and tests frozen later had their bad primes pre-entered.
  - Patching in step 5 uses invariant 2 at a product of exceptional primes that lies in C.
  - Second-digit prescriptions do not interact with Vandermonde digits, which act deeper.
- **§7 (Q2).**
  - A prime of exponent 1 contradicts the unit digit, so t must be (pq)².
  - Two partners sharing the second digit would force r₁ ≡ ±r₂ mod p², which is impossible.
  - Concentration: Var X_j = O(N), and the definable greatest J is nonstandard.
  - Entropy bound (4e)^s/s!: the bad product is ≤ (2A)^{2s}, which is in C in both branches of s. Removals are o(N).
  - The "no host code mod all p²" corollary is valid because τ(h²)∈C.
- **§8.**
  - Every H(1+1/d) is a divisor above the threshold, so 0 < v(g−1) ≤ v(ε)/2. With distinct values the smallest one dominates, residue characteristic is 0, and F has trivial valuation, so the classes are independent mod F\*.
  - The ℤ+Xℝ[X] counterexample and the Bézout integral-closure argument are both correct.
- **§9 against 2A.** Words change no valuation at primes above C and only choose permitted digits at primes in C. So 2A §3.1's per-place embeddings, the §4.1 fibres and the late-Dirichlet gap survive. The coupled §5 edge needs only its two fresh residues to be independent.

## Errors and issues to fix
1. **§0 regression.** The Result and Scope lines no longer carry the reviewed §2 theorem or its scope: the z78 tower fails plain successors below every BCM bound at P, also in elementary copies and in convex subrings containing P. The new "BCM repair … force" clause is §8's result, not §2's. Restore §2 to both lines.
2. **§0 STATUS delta replaced by unreviewed material.** The R1-accepted delta was replaced by one that depends on §§6–7, which are not yet reviewed. Keep the R1 delta as the exportable text and mark the new one "pending R2".
3. **"cofinally many residue-one unit scales" is the wrong direction.** It should say that the values v(g−1) are coinitial in the positive value group, hence infinite rational rank. Also, §8's hypothesis is "all-old-multiple + end-initial D + integer part", not BCM as such.
4. **Stale base text.**
   - §3's rank proof and its Assessment still require √2∉F, which §8 removes. Add a pointer or rewrite.
   - The §5 export Assessment ignores §§6–8. §8 should qualify the z78 §1E / FRONTIER BCM-repair line.
5. **The 2A refs are not reachable from this branch.** `545cd7ace` and `ff4a75afe` are not ancestors of HEAD, and `notes/z82/FAREY_IE1.md` does not exist here. Cite them as `side-agent/z82-farey-ie1` / `git show ff4a75afe:…`. Also, 2A §12 is itself Round 2 material with its cross-review still owed (`0cd05e9f9`), so §9's "PROVED rel. … §12" inherits an unreviewed input.
6. **Cross-lane trap.** 2A §12 states that the marked model has no least hit of (A²+u)²|h+(A²+u)Y. In the §6 variant, §6's positive scheme makes that atom (and §1's (Q)) minimizable. §9 should say explicitly that 2A §12's negative is specific to the §1 variant.
7. **Minor wording and notation.**
   - "square of a scalar squarefree resultant": "resultant" is wrong.
   - `r∈S\{p}` should range over the retained set, because h/(pr) is not integral for the discarded prime.
   - "D≻B (allow equality)" should be ⪰.
   - "for planted primes enlarge it by (pq)²" is redundant.
   - "cohort" clashes with z81 §7's "cohort" (batch of entered centres).
   - "One T_g" in the delta should read "one T_g variant".
8. **Replay gap.** §7 has no stored finite check. My toy above passes and could be added as EVIDENCE.
9. **Under-specified but not wrong.**
   - Step 2 relies on p > E_old, not p ≥ 2E_old, under the look-ahead variant. The constant K absorbs this, but say so.
   - The interleaving of countably many cohorts per edge with z81's ω-sequence of tasks is asserted, not laid out.

## Debate points (scope, not errors)
- §7's barrier is shown only for the model it stipulates. A second host word for the lifts mod p², deviating only on bad primes whose product lies in C, looks like a plausible route to coordination at square precision, at least on C-primes. So the note's "full coordination open" is the honest scope, and the "sharp precision barrier" wording must stay qualified, as it currently is.
- (C1) is a positive result in a relaxation. Triaging it as BARRIER-SCOPED alongside §7 is acceptable only as context for (Q2).
</code-review>
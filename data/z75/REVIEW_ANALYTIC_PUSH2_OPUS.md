# Round 2 cross-model review record

Commit f6da56646, reviewed by `functions.review` (smart, anthropic/claude-opus-5-5), range `280d4fe12..f6da56646`. This file is the lane's digest of the returned read-only review, not a second review of the edits.

> Verdict: ACCEPT WITH MINOR FIXES. The mathematics in `notes/z75/ANALYTIC_PUSH2.md` (commit f6da56646) holds, and I found no fatal or major gap. One sentence in the theorem should be reworded (fix 1 below). The result is a careful port of an existing method, so its novelty is low. I edited nothing.

Opus rechecked the reduced progression, distinctness and positivity, BV+BT weighted error of order h t^{−7/2}, both multiplier harmonic masses, selector tails, Taylor majorant, coefficient sum and signed shift-uniform transfer. Its toy run reported 19,233 verified words across the four slices (1,2),(0,3),(2,2),(3,5). It accepted the comparisons to Z56 and Z68 and the absence of any conclusion beyond 3/4 on ES or below L[1/2] for the cap.

Requested fixes and disposition:
1. State the all-integer witness threshold and exponent separately: now written V≥δL, exceptional count O(H exp(−cL)).
2. Clarify the a+b≥3 restriction is used for U₇ and the square screen, not in counting primes in reduced classes: added.
3. Link the actual review; specify unspecified c, ineffective onset; attribute the method and qualify priority: added.
4. Compare with the bounded-B CRT ceiling EXSET_BEYOND_CRT Cor 2.5, and the whole-avoider all-integer bound EXSET_I3 Cor 7.1: added, with the hypothesis on the architecture.
5. Explicitly distinguish witnessing the extra targets from making progress toward pointwise U₇: added.
6. Supply a replay and clarify the missing non-residue-bias implication: added. The reviewer found the adaptive planting bound correct, but suggested moving it into the original note; it remains here because the user froze ANALYTIC_BREAK.md. Master files were not edited under the lane rules.

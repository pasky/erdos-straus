<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="9385737c9">
A separate reviewer subagent was asked to review the changes in `git log 9385737c9..`. Its request and review follow.

Request: review changes since 9385737c9 carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Focused Round 2 export recheck only. Compare notes/z83/BCM_TS_LDIV.md §0, §§6–8 at 35d0cb3ff with all fixes requested in data/z83/xreview/REVIEW_BCM_TS_LDIV_R2_OPUS.md. Dependency is bb06ac1bc on Lane 1; no merging or editing. Are all actionable points addressed in the scoped theorem, in particular reserve versus large primes, T_Π, the upper/source interfaces and the combined row? Give EXPORT ACCEPT or concrete residual fix; cap any replay ≤15 min.

Commit log:
commit 35d0cb3ff708be5c1fd29619f48eae7dc32913fa
Author: Petr Baudis <pasky@ucw.cz>
Date:   Mon Nov 23 04:18:58 2026 +0100

    Apply R2 Opus fixes; pin reviewed dyadic interface and delimit the smooth-product obstruction

 notes/z83/BCM_TS_LDIV.md | 34 ++++++++++++++++++----------------
 1 file changed, 18 insertions(+), 16 deletions(-)

Review:
**Verdict: EXPORT ACCEPT on the mathematics of the scoped theorem.** There are three small residual fixes, all in the export text only. The orchestrator can apply them at export without another review round.

I compared §0 and §§5–8 at 35d0cb3ff against the 8 fixes requested in `REVIEW_BCM_TS_LDIV_R2_OPUS.md`, and checked the Lane 1 side at bb06ac1bc. I merged and edited nothing. The only replay was `scripts/z83_bcm_sparse.py` (well under a minute); its output is byte-identical to `data/z83/bcm_ts_ldiv/sparse.txt`.

## What each requested fix became

| # | Requested fix | Status |
|---|---|---|
| 1 | Re-pin the Lane 1 dependency | ✔ §0 and §6 now both cite bb06ac1bc, §§1,3,6–8, and the R2 review at 31bb465d2. The fix §6 relies on (each `(T−s_j)/D_j` integral at every depth) is in bb06ac1bc and not in 852dcb457. bb06ac1bc is not an ancestor of HEAD; that is expected, and the export note says to bring both branches in together. |
| 2 | Reserve vs. large primes in the Result | ✔ It now says P has a root mod every reserve modulus and, with positive signs, mod every scalar cut prime. That matches §7: the primes of h are all reserve primes, and h doesn't depend on the signs. |
| 3 | Scope of §7, and T_Π | ✔ §7 now holds across the z81/z82 class, but only under the stated conditions (contraction, Bézout, reserve roots, generic fibres at the coarse maximal ideals). It explicitly does not cover T_Π, where the mixed marking modulus need not be a unit at those ideals. Lane 1 §9 agrees: T_Π's failure uses the §1 lacunary h instead. |
| 4 | Stale §5 | ✔ Relabelled, with a new Round 2 Assessment at the end of §8 (but see R2 below). |
| 5 | STATUS delta | ◐ It now has a label and pointer, is merged into one row, and says neither model contains the other. Two problems remain (R1). |
| 6 | Triage | ✔ RECORD dropped; now METHOD-CX / BARRIER-BROAD / BARRIER-SCOPED. This means the STATUS change rides on Lane 1's RECORD row; it would help to say that explicitly. |
| 7 | Interface with z81 §12 | ✔ The replacement invariant is correct: ordinary edges born later are Gauss/monic over the current marked field. For spheres it is enough that the residue field is infinite, pseudofinite and of characteristic 0, so the four-square form contains a hyperbolic plane. The Farey temporary completions now continue the current pair chain, so there is no fork for Tarski–Vaught. |
| 8 | Minor points | ✔ Tarski–Vaught now says "arbitrary φ". "log h∼L" is replaced by two-sided bounds; I checked against BCM_LDIV §1 that `h∉C` and h stays inside the power cut. The positive fragment is now placed in the §3 variant, not T_F. That is more accurate than the reviewer's wording, since T_F itself has no affine least search. §7.1 is retitled "Reduction". |

## Residual fixes (export text only)

**R1 — the combined STATUS row.**
- **Missing pointer.** The row says "each fails full L(Div)". For T_Π that failure is relative to BCM_TS_LDIV §§1–2 (IE1_DECIDER §9), so the pointer should read `rel. BCM_TS_LDIV §§1–3,6–7; IE1_DECIDER §§6–9`.
- **Dropped qualifiers.** Merging lost three qualifiers from Lane 1's delta. Add "T_F misses quadratic dyadic lifting; both fail BCM (z81 §15); no IE₁⁻ assertion."
- **No replacement target.** The delta doesn't say what it replaces. It should replace the last sentence of STATUS.md:143, "Full `L(Div)` in another variant is open.", together with Lane 1's compress clause. That row is already very long, so compress it rather than adding to it.

**R2 — §5 header.** "superseded by the Round 2 proposal" reads as superseding all of §5, which would drop the root-trace screening line for §§1–2. Change it to: "superseded where they conflict; the §§1–2 root-trace FRONTIER line stands."

**R3 — Round 2 Assessment.** It assigns T_F only to the fine-prime lock ("squarefree-product lock (including T_pf)"). By §7's own new scope sentence T_F has both locks, so write "(T_F and T_pf; not established for T_Π)". Two optional improvements: give the literal replacement text for FRONTIER §4.18 instead of an instruction, and reword "the raw cardinality of the choice set (2)", which is unclear.

## Spot-checks of the new content

These found no errors:
- **Root counting in the §3 variant.** The finite root lists rely on R/qR being a domain. That follows from `q|a ⇔ w_q(a)>0`.
- **Prime-power lifting.** The step dividing `G(r+qu)` by q is valid.
- **Sign claim.** With positive signs, the Result still holds as stated.
- **Scope.** No ES, IE₁⁻ or ℕ claim is made.
</code-review>
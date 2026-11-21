<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="57f350ad2">
A separate reviewer subagent was asked to review the changes in `git log 57f350ad2..`. Its request and review follow.

Request: review changes since 57f350ad2 carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab Round-2 review of notes/z79/PROTH_ALLM.md and scripts/z79_proth_* and data. GPT-6.2 Astra author lane (OpenAI). Independently attack Theorems 4–6, exponent bound, QR barrier, gluing scope, and intersection CRT, verify finite claims and labels. Return full review as tool output; do not edit repo or spawn side agents. Python via uv run --offline --no-project python -B with timeout ≤1800 and ulimit -v ≤6000000.

Commit log:
commit 97a3f8701f9bd9487242490e63a419b59e7f9327
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sat Nov 21 15:22:58 2026 +0100

    Separate all upper cubic signs and intersect odd-order and periodic core methods with explicit lift tests

 data/z79/proth/intersection.json | 34 ++++++++++++++++++++++
 data/z79/proth/r2-replay.txt     |  4 +++
 notes/z79/PROTH_ALLM.md          | 47 ++++++++++++++++++++++++++----
 scripts/z79_proth_r2.py          | 63 ++++++++++++++++++++++++++++++++++++++++
 4 files changed, 143 insertions(+), 5 deletions(-)

Review:
**Verdict: ACCEPT with revisions.** I found no mathematical error in Theorems 4–6, the Corollary, the QR boundary, the §7 gluing proposition or the Theorem 6 CRT construction. Every finite claim replays, and my own independent checks agree. The revisions needed are about labels, triage and the review line: as committed, the note implies more than it has earned.

## Replay and independent checks
All run with `uv run --offline --no-project python -B`, `ulimit -v` ≤ 4–6 GB, and timeouts.

- **The author's script** `scripts/z79_proth_r2.py` passes all four stages in 0.3 s.
- **Theorem 4, brute force at j=2 (H=511=7·73).** I generated U₂ in full from the gcd-1 and gcd-3 ratios; it has 72 elements. Of the sign vectors, (+,+) and (+,−) are in U₂, while (−,+) and (−,−) are not. That is exactly the claim.
- **Corollary, new instance j=7.** Starting from the tower-6 exponents, I built the full word myself:
  - The level-5 word gives 3⁶.
  - The cubing transfer to level 6 gives coordinates (3¹⁸ mod H₅, 1 mod N₆). The correction factor is (1,27), and their product is 3¹⁸ in C₆.
  - The W-lift to level 7 gives (3¹⁸, 1), and the correction is (1,3). The result is **3¹⁸ ∈ U₇ on the full modulus 2²¹⁸⁷−1**, which matches 6·3^{j−6}=18. The text for the transfer, the uncubed last step and the (1,27)/(1,3) factors is all correct.
- **Theorem 5 seeds.** I recomputed every ord_p(2) and every log₂(−5) by brute force; all match the table. Every p≡7 mod 8 and p=2q+1, and none is Wieferich.
  - The odd order and the solvability of 2^b≡−5 hold at h=49, 7³·23, 7·23³ and 7⁶.
  - The orders q_p·p^{e−1} are pairwise coprime, and the kernel-size lift argument is correct.
- **QR boundary.** The brute-force check is empty, as claimed, for p∈{7,23,31,47,71,79,103} with r=1, and r=3 where h<10⁶. I re-derived the proof: the 2-part of ord_l(p) is exactly 2, reciprocity gives (l/p)=+1, and (2/p)=+1.
- **§7 proposition.** The reduction modulo (1−ζ_p) argument is sound. Note that p=3 is already excluded by the odd-order hypothesis, since ord₃(2)=2.
- **Theorem 6.** Recomputed independently:
  - v₂(T)=51, 36|T, and 23|T, so the 47 square row survives.
  - 2^O≡1 mod M, gcd(z,M)=1 and gcd(z−1,gcd(M,O))=1.
  - My own cover gives exactly the stored 28 misses, 64 of the 92 lifts are hit, and only the X row is omitted.
  - The construction checks out: a≡5 mod 8 gives v₂(o)=2 and gcd(o,O)=4; 14≡o/2≡2 mod 4; h≡21 mod 72 gives 3∥h; a|h+1 because 2^b≡−1 mod a. The O′-part can be handled without factoring O.

## Substantive critique
1. **Theorem 5 is a corollary of z78 Theorem 8**, the result proved in z78 §7, applied to LTE-lifted seeds. Its t=0 case, h=49 with a=5, is already the m=25 row of z78 §9. What is new is only that this is an explicit infinite family of odd order handled by mechanism II. That is modest and probably not STATUS material.
2. **The Corollary has no use yet for cores.** At j=6 it just reproduces z78 §10, and the note should credit that. At j=7 the Test-1 cost is g^{3⁶}=g⁹, which three slots cannot pay. The note half-says this; it should state explicitly that no new core h follows for j≥7.
3. **Theorem 4 is a structural lemma about a method, not a result about ES.** The note's own STATUS delta concedes this ("not new all-s ES families"), yet the Triage line still says RECORD for §5. That contradicts itself; it should be DATA or METHOD.
4. **Theorem 6 is a correct CRT combination of two already proven mechanisms.** That they can coexist was expected, so this is low-value for STATUS. At most it deserves one clause in the existing §1C row, not a new item.

## Form and label issues (must fix)
- **The Review line is misleading.** It cites Opus "ACCEPT … fixes incorporated" for the whole note, but §§5–8 were added after that review. It should say "Round 2 §§5–8: cross-review owed (this review)".
- **The §0 Label omits dependencies:**
  - LTE and quadratic reciprocity (§6).
  - The computer-assisted z78 tower-6 certificate behind the Corollary.
  - The computer-assisted Theorem 3 that Theorem 6 relies on.
- **Triage "RECORD (§§1–6,8)" is over-broad.** I suggest RECORD for §§1–4 only, and DATA or METHOD for §§5, 6 and 8. §7 as BARRIER-SCOPED is fine.
- **The replay text overstates what is checked.** It says "all upper-layer masks through j=7", but the script checks the single-layer generators for j=2..7; the masks follow by multiplication. Also, the intersection replay re-derives coverage from the row positions only. The validity of the rows comes from `z79_proth_check.py`, and the note should say so.
- **The data README is out of date.** `data/z79/proth/README.md` does not mention `intersection.json` or `r2-replay.txt`. No generator for T and O is committed ("Data generation is separate"), which is acceptable for certification but not for reproducing the discovery.
- **The commit message is vague.** "intersect odd-order and periodic core methods" is wrong: Theorem 6 has nothing to do with the odd-order family.
- **The Theorem 6 proof has a redundant step.** "choose a>3" is unnecessary, since a≡21 mod 2⁵² already forces it.

Nothing here claims or implies ES in general. The scope statements in the note are accurate.
</code-review>

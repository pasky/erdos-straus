<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="main">
A separate reviewer subagent was asked to review the changes in `git log main..`. Its request and review follow.

Request: review changes since main carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab Claude Opus review of Wave z83 Lane 7 (notes/z83/ES_JUGULAR.md). Try to break every theorem; check F1 (odd squares) and F2 (numerator 8) on every pointwise mechanism; independently replay key computations on small cases. Cap any replay at ≤15 min.

Commit log:
commit e78d466c074dd0a0be358df2e64aaba3c665e811
Author: Petr Baudis <pasky@ucw.cz>
Date:   Mon Nov 23 03:43:23 2026 +0100

    Prove one-way saturation on the Mordell classes and force hybrid drops on a failed-jump family

 data/z83/es_jugular/anchor.txt    |    1 +
 data/z83/es_jugular/basin-1.txt   |    3 +
 data/z83/es_jugular/basin-121.txt |    3 +
 data/z83/es_jugular/basin-169.txt |    3 +
 data/z83/es_jugular/basin-289.txt |    3 +
 data/z83/es_jugular/basin-361.txt |    3 +
 data/z83/es_jugular/basin-529.txt |    3 +
 data/z83/es_jugular/dyadic.txt    |   44 +
 data/z83/es_jugular/holes.txt     | 2902 +++++++++++++++++++++++++++++++++++++
 data/z83/es_jugular/horder.txt    | 1039 +++++++++++++
 data/z83/es_jugular/hybrid.txt    |   15 +
 data/z83/es_jugular/panel.txt     |   28 +
 data/z83/es_jugular/paths.txt     |    6 +
 data/z83/es_jugular/seal.txt      |    3 +
 data/z83/es_jugular/seals.txt     |    3 +
 notes/z83/ES_JUGULAR.md           |  125 ++
 scripts/z83_jug_anchor.c          |   48 +
 scripts/z83_jug_basin.c           |   54 +
 scripts/z83_jug_dyadic.py         |   67 +
 scripts/z83_jug_holes.c           |   28 +
 scripts/z83_jug_horder.c          |   51 +
 scripts/z83_jug_hybrid.py         |  102 ++
 scripts/z83_jug_panel.py          |   66 +
 scripts/z83_jug_paths.py          |   40 +
 scripts/z83_jug_seal.c            |   29 +
 scripts/z83_jug_seals.py          |   43 +
 26 files changed, 4712 insertions(+)

Review:
**Verdict: no mathematical error found. Theorem A is correct as far as I can check. Theorem B and the "move" framing claim more than they deliver, and the triage is wrong.** I made no edits and no commit; everything below is text only.

Scope reviewed: commit `e78d466c0`, which adds the note `notes/z83/ES_JUGULAR.md`, 10 scripts and 15 data files.

## Replays (all under 15 min, `ulimit -v 6000000`)
Every output I regenerated matches the committed file byte for byte:
- **Matched in full:** `horder` (5..10⁹, 91 s), `seal`, `holes` (both primes), `anchor` (to 10⁸), `hybrid`, `seals`, `paths`, `dyadic`, `panel`.
- **Reduced `basin` run** (to 3·10⁵, residue 1 mod 840): matches the note exactly (127 primes, 9,113,580 vertices, 730,633 sinks, max distance 9).
- **Uncertified primes:** all 1,037 are 17 mod 24, none 1 mod 24, so that claim holds.

I also wrote and ran some independent checks of my own:
- **Budget lemma, brute force:** every multiset of m odd letters in ℤ/2m, for m = 1,3,5,7,9, has a signed subsum equal to m. m−1 identical letters fail, so the bound is sharp. The unsigned "2m−1 letters" version holds exhaustively for ℤ/6, ℤ/10 and ℤ/14, and for 20k random 29-letter samples in ℤ/30. The 14+14 adversarial example fails, as the note says it should.
- **General k ≡ 7 (8) split:** for p ≡ 1 (8) up to 3·10⁵ and primes k < 400, the stated premises held 6,484 times, and each time an actual coprime A, C with AC | K and k | A+C was found. Zero failures.
- **Four-slot claim:** 32,692 opposite-sign words p = txv−x−v. Every one has some slot among t, x, v, a, b divisible by 4.
- **Literal BFS for every prime p ≡ 1 (8) below 60,000:** all 1,491 saturate (R = QNR). No sealed orbit exists among the odd-order 17 mod 24 primes there.

## Theorem A (walk saturation): proof checked step by step, holds
- **Facts 1–2:** correct. In fact the reachable set R equals C exactly: the odd part of any reached vertex is itself reached.
- **Fact 3:** the Furstenberg compactness step via z82 A is correct.
- **Escape from small-denominator arcs:** the "shadows double" argument is correct. The rationals are spaced at least 1/Q² apart and 3/(8Q²) < 1/Q². Dirichlet then gives Q < s ≤ 8Q².
- **Bilinear bound:** the block spacing of 1/(2s) is right (j(d₁−d₂) < s/2, so s cannot divide it). All error terms are at most M⁻⁸. After normalising by |A|², the Erdős–Turán discrepancy is O(M⁻⁴ log^{160}M) = o(M⁻²).
- **Endgame:** the index is ≪ log²⁴p. Burgess with r = 4 gives exponent 21/64 < 1/3, which is valid for prime moduli. From there H = QR follows.
- **Even-order extension and the 17 mod 24 dichotomy:** both checked, including that the positive-character integers below m ∈ {5,7,9} are exactly the powers of 2.

Challenges:
1. **The Result line undersells A.** The theorem covers all large p ≡ 1 (24), not just the six Mordell classes. It also covers all large p ≡ 1 (8) with even ord_p 2, with an exact dichotomy in the remaining class. As a consequence, only finitely many p ≡ 1 (24) fail to saturate, and the census shows none below 10⁹. This supersedes z82 H's bound of O_ε(X^ε) possible nonsaturations; say so.
2. **The threshold is ineffective** (it comes from Furstenberg). This should be stated in §0, not only implied in §3.
3. **Value for ES is nil by the note's own Exit paragraph.** Saturation reduces hitting an exit exactly to the existence of an (S) word. That is precisely the part STATUS §2 lists as open on these classes. So A is a statement about the method, not a RECORD.

## Theorem B (forced split plus moves): true, but its integral content is classical
- **T is just the classical Type II split at k = 31.** T = (K, gpA, gpC) with AC | K and 31 | A+C. The W → planes → U → pivot route is a re-description of a point found independently.
- **The three-plane bridge is trivial transport.** Both points of each move lie on a rational slice conic, so a single line in that slice already joins them. The rank ≥ 2 property is decoration, and the "no orbit invariant" corollary follows from this. The note concedes transport but still headlines "reach integers".
- **"Relative density one on the failure set" adds no ES coverage.** Vaughan's exceptional-set bound, X·exp(−c log^{2/3}X), is far below X/log^{3/2}X, so ES on almost all of any such family already follows. Only the explicit pointwise criterion and the budget lemma are genuinely new here, and their novelty is modest.
- **Sharpness wording:** the 28-mark sharpness example uses 2 distinct primes with multiplicity 14 each. It is sharp for *occurrences*, not for the *distinct*-mark condition used in the density clause. Say so.
- **Sieve exponents check out:** dimensions 7/4, 13/8 and 5/2, and the coefficient f(1−η) < 1.
- **FHRSS input matches the archived text:** Table 2 row (11) gives τ = 8 with L = {1}, so m′ ≡ 1 (8). This reuses z82's twice-reviewed application.

## F1 / F2 checks
- **F1 (odd squares):** at n = s², every odd l dividing (s²+k)/4 has (l/k) = +1 by reciprocity, so no mechanism in B can start. My test found no square n = s² (s < 400) at which the premises hold.
- **F2 (numerator 8):** at 8/11, 8/17, 8/131 and 8/241 the general-k premises fail for every prime k ≡ 7 (8). The dyadic condition v₂ ≥ (h−1)/2 is what blocks 17 and 241; 11 and 131 never give an integral window.
- **A, the 29-mark exit and the 4-slot word claim** conclude only 4/p solutions (t ≡ 4 (8), not 8 | t), so they make no numerator-8 claim.
- No violations found.

## Form
- **Triage is inconsistent.** "RECORD" together with "STATUS delta: none" contradicts AGENTS §3, since RECORD goes to STATUS §1. I propose BARRIER-SCOPED, matching z82 WALKS_FIBRES: replace the FRONTIER z82 line (currently "closure > (log p)^{A₀}") with "R = QNR for large p ≡ 1 (24) and for even-order 1 (8); exact dichotomy at odd-order 17 (24)". Theorem B should be METHOD-CX/NULL.
- **Rewrite the Result line.** Lead with A at its true scope. Recast B as "forced ET split on a density-one subset of the z82 J failures; moves are transport only". Cite Vaughan for the density point.
- **Order and readability.** Put A before B. The prose is very compressed and some sentences are hard to parse ("Numerator four will be used in both merged fractions", "eight even above 2p/5", "the last pivot is a different move").
- **Small inconsistency:** the F3 row says "all eight composites", but `dyadic.txt` lists 9 non-square composites. The count is 8 only if 17401609 is counted under F4.
- **Data hygiene is fine.** No binaries are committed, and the replay block is accurate.
</code-review>
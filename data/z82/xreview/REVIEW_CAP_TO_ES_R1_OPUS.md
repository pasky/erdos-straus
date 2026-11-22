<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="main">
A separate reviewer subagent was asked to review the changes in `git log main..`. Its request and review follow.

Request: review changes since main carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab Claude Opus review of Wave z82 Lane 1B (notes/z82/CAP_TO_ES.md). Check every proof step, quantifier, scope, hypothesis, label, and falsifier check. Cap any computational replay at ≤15 minutes.

Commit log:
commit 269f63009a9fe04fc91a33432ed749e7fdada867
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sun Nov 22 19:52:14 2026 +0100

    Classify global cap pivots and bound linked squarefree denominators

 data/z82/cap_to_es/moves.txt    |  22 +++++++
 data/z82/cap_to_es/normal.txt   |   5 ++
 data/z82/cap_to_es/panel.txt    |  48 +++++++++++++++
 data/z82/cap_to_es/transfer.txt |   8 +++
 notes/z82/CAP_TO_ES.md          | 130 ++++++++++++++++++++++++++++++++++++++++
 scripts/z82_c2es_moves.py       | 120 +++++++++++++++++++++++++++++++++++++
 scripts/z82_c2es_normal.py      |  80 +++++++++++++++++++++++++
 scripts/z82_c2es_panel.py       |  86 ++++++++++++++++++++++++++
 scripts/z82_c2es_transfer.py    |  63 +++++++++++++++++++
 9 files changed, 562 insertions(+)

Review:
**Verdict: ACCEPT WITH FIXES.** These are minor scope and wording fixes. I found no fatal error in any proof step, and nothing in the note is presented as ES. The labels are honest: ES in ℕ is still stated as open, and the Schinzel H condition is attached only to prime-carrier sharpness.

## Replay
- I ran all four engines from the repo root under `ulimit -v 6000000`; each takes under 1 s. All four stdouts are byte-identical to `data/z82/cap_to_es/*.txt`.
- `panel` has to be run from the root, because it reads `data/z58/...` by a relative path. It fails if run from `scripts/`. The note's instructions do say root, so this is acceptable.
- **Independent second check** (`/tmp/rv82/indep.py`). This is a different method: a numpy brute-force `(x,y)` scan for the integral solutions, plus a normal-form reduction in the `A_i` coordinates with the Vieta step.
  - It reproduces the solution counts: 15 at 409, 9 at 2521, 15 at 3361, 26 at 21841.
  - It confirms that the 3361 hybrid `(870, 100830, 97469/3)` shares its normal form with none of the 15 integral solutions.
  - This certificate originally had no independent check; it now has one. It is worth recording in §5.
- I also brute-checked small primes `p≡1 (4)` up to 409. No ES solution has a pair with square ratio, and `y ≤ H` holds every time, as the mixed-word barrier requires.

## Proof steps checked line by line (all correct)
- **Theorem A**
  - The pivot sums to 1, stays positive and is an involution.
  - The valuation table is right in both cases (`a>0` and `a=0`), and so is the exit to `(0, b−a, b−a)`.
  - After exit, the unit share is always the last pivot, and pivoting the share with valuation `i` gives `(0, i, i+j)`. That induction is sound.
  - Restricting to reduced words is legitimate: any word reduces to one with no adjacent repeats and the same orbit point.
- **Model W**
  - `(ΣA)² = ΠA` holds.
  - `A_i' = (A_j+A_k)²/A_i` and its Vieta form are correct.
  - Squareclasses are preserved per label.
  - The inverse-polynomial integrality argument is valid.
- **Markoff normal form**
  - The `r_i>2` bound is right, and the limit argument (`2R_i = R_jR_k` at two indices, giving `4=0`) is correct.
  - Constancy on edges is right, so the normal form is a complete invariant.
- **Corollary and "price" paragraph**
  - `T(2D−p) ≤ p²D` and `u ≤ p` for `D ≥ p` hold.
  - The odd-square argument holds: `T≡3 (4)`, and `gcd(T,Z) | p`.
  - The valuations `(1,2)` for the cubic packet and the test `h−c ≤ c` are correct.
- **Lemma B**
  - Both charts and the bounds `3q≤p+1`, `7q≤2p+1` and `8q≤3p+1` check out, including the `(p+f)/q ≡ 3 (4)` step.
  - The examples are right: `p≡17 (28)`, and 409/117/59.
  - The reciprocity chain giving `(q/p) = −1` is correct.
- **Proposition C**
  - The `uv|x` step holds, and the margin `p+3` is right.
  - The function `4uv − p(u+v+1)` is increasing for `u,v > p/4`.
- **Mixed-word barrier**: the bound `y ≤ p(p+3)/6` holds, as do `z | pxy` and the `l ≡ 3 (4)` versus `a²+b²` contradiction.
- **Theorem D**
  - Equation (1) is correct, as is `TA ≤ n²`, giving `D ≤ n³ + 4n⁴`.
  - The exact expansion of `D` is right.
  - The exclusions at `k=7` (mod 7) and `k=3` (mod 3 and mod 4) are correct.
  - The sharpness family is right: `p³ ≡ −4 (11)` and `s ≡ 7 (8)`.
  - Irreducibility of `F` holds. The fixed-prime test only needs `j=0` at 11, which is fine because `9240/44 = 210` is a unit mod 11. The degree-5 count works at primes `>5`.
  - The Lucas/BLS certificate is correct, with a separate base allowed per factor.
- **Split quartic**
  - `g₁g₂ = (p²+287)² + 4Cp` is correct, and `g₂−g₁ = −68(X−24)` with `g₁(24) = 1441`.
  - The discriminants `960` and `−5568` are right.
  - The sieve ranges are sound. In the large-`l` range, `U² − j(2l)² = disc` has O(log X) solutions by the ideal and unit-ratio argument (consecutive solutions differ by a factor at least the golden ratio).
- **Theorem E**
  - The reciprocal identity is right, `(S,r)=1`, and the denominator is exactly `r` with `r | x,y`.
  - The collision bound holds: `ar²v ≤ x^.124` is far below `ℓ`.
  - The fraction `−ar²/v` recovers `a, r, v`.
  - V itself was already reviewed twice by Opus (`REVIEW_CAP_RECORDS_OPUS2.md`), so leaning on it is fine.
  - The F1 Jacobi claim holds: `(a/f) = (v/f) = 1` and `(−1/f) = −1`.

## Issues to fix
1. **Prop C is missing a hypothesis.** Its statement never says `p ≡ 1 (4)` prime, but it depends on Lemma B, which fails for `p ≡ 3 (4)` (e.g. `4/3 = 1 + 1/6 + 1/6`, ratio 1). State the hypothesis.
2. **§2 "zero hits throughout `q>2p` … even if `q` composite" needs `p∤q`.** Lemma B assumes `p∤q`, and when `p | q` the ratio is unconstrained by B. z81 HC uses prime `s > 2p`, so that case is fine, but the composite extension must say `p∤q`.
3. **The "hybrid" `(s,a,b,m)` is used before it is defined.** The §1 certificate relies on it, but the chart only appears in §5. Define it in §1, or point forward explicitly.
4. **The title is ambiguous.** "Moving the *first* denominator" (and A's "all first denominators simultaneously") sits oddly with content that is about the nonintegral coordinate's denominator `z`. Clarify which coordinate is meant, or retitle.
5. **Garbled or unexplained sentences.** These include:
   - "This includes Type I, Type II and moving all coordinates" (Theorem D);
   - "This also explains why a bare `s²+1` cannot replace our ratio";
   - "No inference of distinctness just from the number of divisors";
   - the parenthetical "Chart I cannot give `p|x` …", which is redundant since the chart I derivation already assumes `p∤x`.

   The opening Assessment is barely parseable. Jargon (`HC`, `K`, `R₈`, `Z₇`, `U₇`, `(★)`, "C-even line") is used with no pointers.
6. **"Linked" is redundant in D.** For packets with `x,y` integral, clearability under the group already forces `D | gcd(x,y)`: an unlinked prime has `a=0`, which is trapped. Saying so would simplify D's scope sentence.
7. **One data line is not mentioned.** `normal.txt` contains a "quartic" seed at 3361 (0 squareclass candidates), which the note never discusses.
8. **Triage is debatable.** BARRIER-SCOPED fits A, B and C. D is a sharp PROVED height theorem, and E gives new PROVED exceptional-set rates for a relaxation (exponent-one linked squarefree). Neither is a barrier. Suggest "BARRIER-SCOPED (A–C); D/E scoped relaxation results", with a FRONTIER mention beside the z81 cap-1 entry. "STATUS delta: none" is defensible, because E explicitly does not improve V or any ES exceptional set.
9. **CERTIFIED coverage should name the independent check.** The §5 lead says "one lane engine per file … not independent". Under AGENTS rules, name the independent-check coverage, which is now this review's brute-force replay for 409, 2521, 3361 and 21841.

## Debate points (no fix needed)
- **Does A shut out the intended programme?** Only for the three named pivots and polynomial maps that are integral on W. The note says this plainly, and the secant Assessment admits that chords and pencils are open. Fine.
- **Is D's `O(n⁴)` informative for ES?** It caps only the locally clearable stratum. The z81 unlinked jumps remain unbounded, and the note says so. There is no overreach.
</code-review>
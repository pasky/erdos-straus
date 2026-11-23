<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="09ad7b409">
A separate reviewer subagent was asked to review the changes in `git log 09ad7b409..`. Its request and review follow.

Request: review changes since 09ad7b409 carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Focused Round 1 verification only, not Round 2. As an independent hostile Claude Opus reviewer, verify the R1 fixes to notes/z83/IE1_DECIDER.md. Focus on the new henselian local quotient/image corollary and the explicit masked-seed valuation, order, scalar CRT/splitting, specialization and coinitial-queue transfer audit in §§3.1,4. Flag any false claim, missing hypothesis or bad citation. Are they sound relative to the named z81–82 inputs? Concise verdict. Cap replay at ≤15 min, use ulimit -v 6000000 and uv run --offline --no-project python -B if replay is needed. Read only, no writes.

Commit log:
commit 0b58a4cda3e792705392419f57056053188030d8
Author: Petr Baudis <pasky@ucw.cz>
Date:   Mon Nov 23 03:12:09 2026 +0100

    z83: audit masked seed transfers and sharpen the dyadic image obstruction

 data/z83/ie1_decider/digits.txt |  2 +-
 notes/z83/IE1_DECIDER.md        | 48 +++++++++++++++++++++++++++++++----------
 scripts/z83_ie1_digits.py       |  2 +-
 3 files changed, 39 insertions(+), 13 deletions(-)

commit 6e4b83725dc5a48b08ea53391c2eb21f4c5db5ee
Author: Petr Baudis <pasky@ucw.cz>
Date:   Mon Nov 23 03:09:04 2026 +0100

    z83: archive full hostile Opus R1 review of the dyadic separator

 data/z83/xreview/REVIEW_IE1_DECIDER_R1_OPUS.md | 108 +++++++++++++++++++++++++
 1 file changed, 108 insertions(+)

Review:
**Verdict: ACCEPT. I found no false claims.** I checked the R1 fixes against z79 §4, z81 §§2–4, 11–12 and z82 §§7–11, and both new pieces hold. The problems left are citation and wording fixes.

**Replay.** `scripts/z83_ie1_digits.py` runs with rc=0, and its output is byte-identical to `data/z83/ie1_decider/digits.txt`. The only change in that file is the label of the "37 controls" line.

## The henselian quotient/image corollary (§3) is sound

- **`A=R/hR` is local with residue field F₂ and maximal ideal `2A`.**
  - `h` is even, because an odd `h>1` would itself be an odd divisor.
  - An odd `x` and `h` have coprime gcd under `D₂`, so Bézout makes `x` a unit. `2` is not a unit because `h` is even.
  - `A/2A = R/2R = F₂`.
- **Henselian.** The expansion `f(c+2Y)=2(b+Y+2G(Y))` with `G=sY+Y²H(Y)` is formal and needs no cancellation of 2.
  - The packed-coefficient §1 scheme then gives the lift. This also covers non-monic `f`, which is Stacks condition (2).
  - The converse via Lemma 10.153.3(2) is correct, because the reduction of `Y+2G−b` is linear.
- **Image `D`.**
  - It is a quotient of a henselian local ring, hence henselian local.
  - The kernel lies in `2A`.
  - A Bézout local domain is a valuation domain, by the coprime-row argument given.
  - The proof that `√2` is not in `Frac D` is correct: integral closure puts it in `D`, it lies in `2D`, so `1=2z²`. This uses `2≠0` in characteristic zero.
  - The corollary correctly retracts R1 item 7's overreach that the image would be "relatively algebraically closed".

## The §3.1 and §4 transfer audit is sound

- **Seed sandwich.** Ascending peeling is correct. The coefficient of `Z^k` in the remainder is `2^k g_k`, and `2∈C`, so it never divides by `M₀` or by `8NL`, neither of which is in `C`.
  - The reverse inclusion holds because `X` is integral.
  - The relation `Q=(1+M₀Z)²` follows from `X=((1+M₀Z)²−1)/M₀`.
  - Serving `1+M₀Z` first with digit 0 is legitimate under the z81 §3 rules: content 1, reduction 1 at `l=2`, and avoidable zeros at the other entered primes.
- **Valuation restriction.** Invariants 1–2 and the z81 §12 per-place embeddings over all of `K` restrict exactly as z81 §12 already allows for square-tested lines.
- **Order.** Relative Gauss at `X/H` (or `X/N`) holds since nonzero elements of `S_old` are at least `1/c` in size.
- **Scalar CRT.**
  - `gcd(1+M₀s, M₀D)=1` follows from the freeze at primes of `D` and from `m≡1` at primes of `M₀`.
  - `m` is odd and `Q↦m²`, so the multiple-of-`m²`-or-coprime dichotomy and the PA avoidance of finite supports both go through.
  - The z82 §10 `b₀` step is correctly limited to finite scalar congruence systems, not to arbitrary representatives modulo `H`.
- **Splitting and specialization.**
  - The z82 §9 constant splitting extension at a polynomial birth ends at `K`, with a free scalar point `o`.
  - Persistence of the horizontal prime holds, and the `Q` fibre at birth is `A[X]/(1+cX)≅A`, which is regular over `K`. So `−1` is still a nonsquare.
- **Digit lifting.** The Newton identity is correct. A cut pure dyadic `h` is a PA power of 2 that is at most `N^j`, so `h|N^j`.
- **Coinitial queue.** The bound `q≤36L√y<y` holds and `q>C`. The `K(q)∩A[q]=K[q]` replay is z81 §11's.

## Fixes owed (none affects correctness)

1. **Missing Bézout citation in the corollary.** Its label cites only §1 and Stacks. Locality and "quotient of a Bézout domain" both need `IE₁⁻ ⊢` signed Bézout (z79 `IE1_BASE` §4).
   - Locality could instead come from the scheme with `G=sX`.
   - The valuation-domain step genuinely needs Bézout for `R`.
2. **Stacks citation.** The arbitrary-polynomial criterion is Algebra Lemma 10.153.3(2), **Tag 04GG**; Tag 04GE is the section. The "More on Algebra, henselian pairs" pointer is a detour.
3. **Labels omit the z81 sections the audit relies on.**
   - The §3.1 label ("z81 §§2–5,7, z82 §§7–11") and the §0 Label omit **z81 §12** (per-place embeddings) and **z81 §11** (used by §4).
   - The §4 label omits z81 §12.
4. **Wording overstated or understated.**
   - "Does not have to be algebraically closed" understates it: the proof shows `Frac D` is never algebraically closed in characteristic zero.
   - "Explicit violations of this image condition" is loose. The following paragraphs derive consequences for the receiving field, which T_F then violates.
5. **One remaining line of audit.** The claim of "the other z82 positive properties" also relies on z81 §7's Lag/Dirichlet sphere births being independent of the seed. That is evidently true, but it is not listed in the audit; one sentence would close it.
6. **Review line.** After this verification, the §0 Review line can cite this R1 verification. The corollary has now had one hostile Opus check.

Process is fine: the lane touched only the note, script and data, no master files. Opus reviewing Astra work satisfies the cross-lab rule.
</code-review>
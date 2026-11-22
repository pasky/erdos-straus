<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="main">
A separate reviewer subagent was asked to review the changes in `git log main..`. Its request and review follow.

Request: review changes since main carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab Claude Opus review of lane z81-specific-class (notes/z81/SPECIFIC_CLASS.md). The author is a GPT-6.2 Astra lane. Verify every theorem, analytic/sieve/Kloosterman estimate, exponent, hypothesis, falsifier screen (F1–F4), and scope claim. Check closely that no step secretly violates the sieve-limits-note / z80 Theorem LM barriers or smuggles in an unproved uniformity assumption. Cap any computational replay to ≤ 15 minutes.

Commit log:
commit b349d18b1cc972eea8f250a4639f8873764d1a0d
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sun Nov 22 15:01:05 2026 +0100

    z81: resolve the prescribed divisor-ratio window threshold on integer intervals

 data/z81/specific_class/controls.txt |   3 +
 notes/z81/SPECIFIC_CLASS.md          | 104 +++++++++++++++++++++++++++++++++++
 scripts/z81_spec_windows.py          | 100 +++++++++++++++++++++++++++++++++
 3 files changed, 207 insertions(+)

Review:
**Verdict: ACCEPT WITH FIXES.** I re-derived the four proved results (W, S, the Corollary and P) and they hold. The conditional (DR) is stated honestly as an unproved new input. No proved step breaks the sieve-limits/noBcap or z80 Theorem LM barriers. The fixes needed are scope disclosures and triage bookkeeping, not repairs to the mathematics.

**Replay.** `scripts/z81_spec_windows.py` takes 0.2 s and its output is byte-identical to `controls.txt`. I also re-checked independently:
- the constants I(1/log 3) = 0.0041548 and b* = 0.523495;
- the pair-collision formula behind (2);
- the m = 4ab−1 quadruple claim (333 out of 333 cases satisfy 4ABCD = A+B+nC).

## Substance: what I verified

- **§1 identity.** 4/n − 1/m = q/(nm). Both denominators are integers because d₁ | m and q | d₁+d₂. The divisor-ratio set D_q(m) equals the signed exponent box, as stated. The handling of even n and n ≡ 3 (mod 4) is correct.
- **Group lemma (2).** d ≤ M·ΣP_g² − 1 holds. My exact expectation is M·3⁻ᵏ + (5/9)ᵏ − 2·3⁻ᵏ when M is even, so (2) holds. The (5/9)ᵏ correction for pairs whose differences are all even is necessary, and the note includes it.
- **Amplification to (3).** Given the support S, each translate S+g_i is an independent fresh chance, so the bound M·dˢ is right. With s = (β+4)√l the tail is O(L⁻⁴), slightly better than the O(L⁻³) written.
- **Factor exposure.**
  - Harmonic mass H = (1−e)l − 2 log l + O(1).
  - Siegel–Walfisz applies because q ≤ (log R)^{β/e+}.
  - b ≤ X^{4/l} keeps Shiu valid.
  - The multiplicative error (1+O(L⁻⁵))^{4l} is 1+o(1).
  - The j > 4l tail is L^{h−4 log 2}.
  - The (5/9)^J mixture term is L^{−4h/9} and the j < s term is L^{−h}; both are negligible against I(a) ≤ 0.0174 for β ≥ 0.9.
  - The Poisson lower tail plus the 3⁻ʲ tilt gives hI(a/h), which tends to I(a) as e → 0.
- **Lower bound in W.** It follows from |D_q| ≤ 3^{Ω(m)} together with Sathe–Selberg at α = a < 2.
- **Theorem S.**
  - The small-pair union bound (log q)²/q is right.
  - Shiu in progressions applies because q ≤ D^{1/2}, with A taken as the larger of the pair.
  - The triple dyadic sum gives L^{3v−1}.
  - Choosing v = α/3 gives the exponent −I(α) + α log 3 − β, which is strictly below −I(α) because α < β/log 3.
  - The case β > log 3 is also correct.
- **Corollary.**
  - The Markov step is correct.
  - The identity 4abcd = a+b+nc holds.
  - The minimum modulus lies in [n/q, 2n/q+1].
  - Minor: the condition "q ∤ ab" is automatic for any coprime a, b with q | a+b, not only when q ∤ n.
- **Theorem P.**
  - Upper side: at most C·L^{1−u} certificates can exceed Y, which is o(band) when u > 1−b. Turán–Kubilius controls Ω_{≤Y}. Shiu bounds the cofactor at (log Y)^{v−1}. At v = 1/3 the exponent is (u+ε) log 3 − b < 0.
  - Lower side: rerunning W with band (e^{L^e}, e^{L^u}] needs b + u < 1 to get Σ log d_q = o(L), which holds.
  - The threshold b* = log 3/(1 + log 3) is correct.
- **(DR) algebra.**
  - The Fourier form (4) equals K − 1.
  - z^J = X^{σ/2+o(1)} and ∏m_q = X^{o(1)}, the latter because σ < I*.
  - The wrap-around cost is O(L) values of t, and (5) follows.
  - The Fubini statement and the mixture-sharpness computation, giving exponent max(0, σ/2 − d), are correct.
- **F1 reciprocity.** For odd squares, the Legendre symbol (−q/r) equals (r/q) at every odd r dividing m. When 2 | m, q ≡ 7 (mod 8). The case q | s is handled. So −1 is never present at a square, and the 132 square tests confirm it.
- **Barriers.** Every proved step is a statement about one window or one integer, and the inputs are uniform in q (Siegel–Walfisz with fixed A = β/e; Shiu with modulus at most the square root of the length). No joint uniformity across windows is used anywhere outside (DR). The per-window factors F_q depend on full factorizations, so (DR) is not class data at bounded level and does not formally contradict noBcap or LM.

## Substantive challenges the note should absorb

1. **(DR) is not new in kind.** If P(every window in S fails) ≤ C^{|S|}·∏p_q for all |S| ≤ J, then K ≤ exp(C·J·z·p) = X^{o(1)}. So (DR) follows from the uniform C^k-multiplicativity hypothesis already contemplated in `EXSET_CHAR_FORCING.md` Calculation 4.2. What is genuinely new is W's envelope L^{−I*}, which makes multiplied envelopes give a power saving where the earlier Fourier envelopes reached only exp(−L^{0.42}). The note should say this directly instead of only calling (DR) "a new explicit input".
2. **(DR) is band-critical, and odd squares refute its natural extension.** On the band q ~ L^β with 1 < β < log 3, odd squares (√X of them) give K ≥ X^{−1/2}·exp(σL^β/(2β)), which is super-polynomial. So any (DR)-type or multiplicativity hypothesis there is false for every σ > 0. The same multiplicativity would otherwise predict E finite, which is exactly the §4.2 heuristic failure. (DR) at q ≤ 2L survives F1 only because the squares' atom has exponent 1/2, far above σ/2. The F1 row needs this as an explicit warning against strengthening the hypothesis.
3. **State the barrier against (DR) explicitly.** The note's own sharpness section shows that an atom of size exp(−CL^{3/4}) violates (DR). LM shows that class marginals mod Q ≤ N^{A₀} cannot exclude such atoms. So any proof of (DR) that replaces F_q by class majorants of level ≤ N^{A₀} is ruled out. The §4 "Assessment" paragraph only gestures at this; it should be a labelled Assessment line.
4. **Give the size of the saving.** δ < σ/2 < I*/2 ≈ 0.0021. The Result line should give this number.
5. **Choice of indicator.** The note is titled for the specific class, yet (DR) uses F_q = incompleteness of all classes. Theorem S gives the same marginal rate for the −1-miss indicator, and (5) works with that indicator, which is the minimal event an ES failure needs. Either state (DR) with the −1-miss indicator as the primary target or justify using full incompleteness.
6. **Primes.** W and the Corollary say nothing about prime n, because L^{−0.002} is much larger than 1/L. This is disclosed, but it means W has no ES content beyond the conditional. That should be stated in the §0 Scope line.
7. **Priority.** W is an Erdős–Hall-type threshold with log 3 in place of log 2, for divisor ratios. The note disclaims priority only for the techniques, not for the theorem. A literature check is owed (Erdős–Hall 1978 and the later work on divisors in residue classes).

## Form and bookkeeping

- **Triage.** "TARGET" with "STATUS delta: none" is inconsistent: a TARGET takes a slot in STATUS §2, which is capped at six, so one item must be demoted. Suggested classes:
  - P: BARRIER-SCOPED, one FRONTIER §6 line.
  - W and S: a FRONTIER §7 data/sub-problem line.
  - (DR): a FRONTIER §7 open sub-problem, unless the author proposes the STATUS §2 swap explicitly.
- **§0 labels.** The inputs omit Turán–Kubilius (used in P), Shiu in progressions (S and P) and quadratic reciprocity (F1).
- **Stale pointers.** "`notes/z81/LIT.md` on the lit branch" is stale: LIT.md is now on main. The branch base predates the z81-lit merge, but it only adds new files, so no conflicts are expected.
- **Notation.** The Corollary should read O(L^{−I*/2+o(1)}), not O(L^{−I*/2}).
- **Prose.** Several sentences are too cryptic to audit, for example "At primes in the dyadic range below it is Type II", "the q-band consists of first-denominator offsets", and "In the suggested m=4ab−1 family" (suggested by whom?). The Linnik-caps and EH/BV remarks in §4 are unsupported assertions; they are labelled Assessment, which is acceptable, but should be marked as such in the text.
- **"CERTIFIED" label.** It is used for sanity checks of identities (the toy torus value K = 568/513 carries no information). Suggest "replay control" instead.

**No CLAIMED proof of ES; nothing here needs flagging to the user as such.**
</code-review>

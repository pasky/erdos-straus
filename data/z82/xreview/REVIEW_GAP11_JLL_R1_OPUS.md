<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="main">
A separate reviewer subagent was asked to review the changes in `git log main..`. Its request and review follow.

Request: review changes since main carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab Claude Opus review of Wave z82 Lane 4 (notes/z82/GAP11_JLL.md). Verify every sieve bound, integral, distribution level, JLL shifted mean-square step, and constant rigorously. Cap any replay at ≤15 min.

Commit log:
commit 882718100500f4a8707f519f97f2b1a88a168b0f
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sun Nov 22 19:28:55 2026 +0100

    Port the fixed-shift JLL mean square and quantify two-window sieve thresholds

 data/z82/gap11_jll/check.txt |  24 ++++++
 notes/z82/GAP11_JLL.md       | 180 +++++++++++++++++++++++++++++++++++++++++++
 scripts/z82_gap11_check.py   | 111 ++++++++++++++++++++++++++
 3 files changed, 315 insertions(+)

Review:
**Verdict: accept with fixes.** I found no mathematical error in anything I could check. Every constant, integral and margin I recomputed matches the note. The fixes needed are to labels, the dependency chain and the STATUS delta. The JLL port (Theorem 1) was only spot-checked, not fully verified.

The diff adds three files: `notes/z82/GAP11_JLL.md`, `scripts/z82_gap11_check.py` and `data/z82/gap11_jll/check.txt`. No master files were touched, which is correct for a lane.

## Checks I ran (about 3 min of compute)
- **Script replay:** `scripts/z82_gap11_check.py` runs in 0.4 s and its output is byte-identical to `check.txt`.
- **Census for Theorem 2 (my own, EVIDENCE only):** for each of the six hard classes I counted primes p ≡ r (mod 840) whose u has no inert factor. I compared this with (A_k/192)∫dt/(√log(t/λ)·log t).

  | k | ratio at X=1e8 | ratio at X=1e9 |
  |---|---|---|
  | 3 | 0.948–0.958 | 0.959–0.965 |
  | 7 | 0.967–0.979 | 0.976–0.979 |

  The ratios are uniform across classes, including the s=7 fibres (r=361, 529 at k=3), and rise toward 1 at roughly a 1/log X rate. This supports both A_k and the per-class uniformity.

## Substance: what I verified
- **The A_k constant.**
  - C_k equals √(L(1,χ)(1−1/k)∏_inert(1−q⁻²)/π).
  - The local factor is 1 at split primes and 1−1/(t−1)² at inert primes, with 840/φ(840) = 840/192.
  - The (Q/φ(Q))·∏_split(1−1/t) collapse is valid because every nonsplit prime of 840 divides Q on each fibre.
  - A₃/C_V3 = 2e^{γ/2}/√π, the usual e^{γκ}/Γ(κ+1) relation.
  - The certified interval code rounds in the right direction, the tail bound 3/(N−1) is valid, and the result is consistent with z80 `coeff.csv` (2.21323772 is an upper bound from a shorter truncation).
- **The JLL port (Theorem 1), checked against the source text:**
  - The pairing gives t = b(c−a). The recalled-label determinant is b(P*−p*nF), and its second coordinate ≡ bP* is a unit mod p*.
  - The box then gives ‖b(n−n′)F r‖ ≤ 32/p*. So changing the second separation test in (5.11) is genuinely necessary; keeping the old test would leave a gap. The note handles this correctly.
  - Lemma 6.13's measure is unchanged under multiplication by b.
  - Prop 5.3: t ≠ 0 and primitivity still hold, using Y ≤ exp(2K L^{0.2}) < z.
  - Prop 6.15 / E₂: Shiu applies in the class b mod a.
  - Removing λ|H by positivity is sound.
- **The Siegel-zero replacement (H3).** I checked Theorem 24.20 in the Montgomery–Vaughan III draft: it explicitly allows an exceptional zero provided |s−β| ≥ 1/log q. The split into small |t| (rough-Möbius Siegel–Walfisz via the smooth convolution plus Rankin) and large |t| (the Perron rectangle stays more than 1 away from the real zero) is correct. This removes JLL's reliance on the 2026 Banks and Green Siegel-zero preprints, [1] and [11]. That is a real improvement.
- **Type I and weight removal (H1, H5, H6).**
  - The Bonferroni truncation at j = L^{0.1} is valid; the remainder is at most C(ω, j+1).
  - The selected-band multiplier is 1/(t−1).
  - The Selberg denominator lower bound has subtractand 0.3 < 1, and the dimension is 3/2.
- **Theorem 3 (conditional).**
  - τ = 40625/83844 and identity (3) are correct.
  - The single switched tail costs 3/4 (half of z81's 3/2).
  - The margin is about 0.0029 > 1/350.
- **Theorem 3a (unconditional).**
  - I rederived the cost (A²√(a/2)/d_p)·J₂ from the Y/(48 log Y) count, the e^γ and A/√2 upper factors and the harmonic measures.
  - C_sw = e^{−3γ/2}/C_G follows from the Selberg G-asymptotic, and C_m·C_sw/C_V = e^{−γ/2} follows using z81's identity.
  - The chord majorant and the substitution t = 1/(2+s²) are correct.
  - By hand the margin is about 0.0045, above 1/250 = 0.004. It is tight but certified.
- **Theorem 4 (growing-gap tail).** The Stirling exponents check out: (s−1)(t−1)+t log t−½, the identity t log t−I(t) = t−1, s = −1/(2e) and −1/3, and D·log Z = L·l^{−ε/2}. The Paley–Zygmund minors are also correct: a unit minor for different supports, and determinant ±2 with a |G[2]| factor for the same support.
- **Corollary 3.1 positivity.** The reciprocity step (t/k) = (−k/t) holds for k ≡ 3 (4), and the case 2|s forces k ≡ 7 (8).

## Required fixes
1. **Label honesty.** JLL v2 is an unrefereed 2026 preprint, and its §§5–6 adapt the unrefereed [22] (Lü–Wang–Wu, 2026) and [30] (OpenAI, Poisson–Dirichlet law). The house rule is "PROVED rel. *published*" theorems. So Theorems 1, 2 and 3.1 should say "PROVED rel. the unrefereed JLL v2 §§5–7 lemmas (incl. [22,30])", or be labelled CONDITIONAL. The dependency Assessment omits [22,30] entirely, and the STATUS delta's "rel. the fixed-shift JLL port" needs the same qualifier.
2. **STATUS delta omits Theorem 4.** It improves the z81 headline in STATUS §1D (l^{3/2} → l^{1−1/(2e)+ε}). The delta should propose a replacement for that clause, or say explicitly why it is excluded.
3. **Theorem 3a, vector sieve.** The term F(s₃)f(s₇) needs Iwaniec's asymptotic *equality* for the β-sieve main sums, not just the upper bound; say so. Also say that Nath–Xie is used through its proof, not its stated (A1).
4. **Theorem 1 is checked only at spot-check level.** I did not re-verify the §6 path counts or the Prop 6.5 frame equidistribution with b in place. The note asserts these are unchanged. A map table "JLL item → change → why unchanged" would make a second review feasible.
5. **Triage.** I would call this RECORD rather than HEADLINE. It upgrades ≍ to ∼ on single windows and removes the FHRSS-for-general-k dependence, but it does not move the "where everything ends" barrier. The note itself says it does not give the joint B₃·B₇ estimate.

## Form and minor points
- The prose is extremely dense, with imperative asides ("Do not…") inside proofs, and the title is cryptic.
- The script's "recalled-label phase" assert only restates det ≡ bP mod q, and the final t-loop only checks an identity. Drop them or label them sanity checks, and consider adding the cheap census above as an EVIDENCE line.
- Montgomery–Vaughan III is a course draft; cite a published Korobov–Vinogradov source for Dirichlet L-functions as well.
- I did not check the BFI, Maynard, Lichtman and Pascadi level claims or any priority question for shifted Motohashi analogues. A priority check is still owed.

No ES claim is made; the scope statements are accurate.
</code-review>
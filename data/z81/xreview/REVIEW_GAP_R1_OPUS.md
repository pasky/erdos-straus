<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="main">
A separate reviewer subagent was asked to review the changes in `git log main..`. Its request and review follow.

Request: review changes since main carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab Claude Opus review of lane z81-gap (notes/z81/GAP_ES.md). The author is a GPT-6.2 Astra lane. Verify every theorem, sieve/norm-form citation, exact failure criterion for k=3,7,..., falsifier screen (F1–F4), and model calculation. Check closely for any hidden gaps in g>=11 proofs, unproved FHRSS/sieve inputs, or overfitting in the model. Cap any computational replay to ≤ 15 minutes.

Commit log:
commit 4feccee15c3b0d44bb55ccf078be1a0cca22217e
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sun Nov 22 15:01:26 2026 +0100

    Bound the full genus threshold and test multi-window gap tails

 data/z81/gap/audit.txt         |  32 ++++++++++
 data/z81/gap/bulk_pairs.txt    |  96 +++++++++++++++++++++++++++++
 data/z81/gap/design.md         |   3 +
 data/z81/gap/forecast.txt      |  60 ++++++++++++++++++
 data/z81/gap/letters.txt       |  26 ++++++++
 data/z81/gap/packets.txt       |   6 ++
 notes/z81/GAP_ES.md            | 134 +++++++++++++++++++++++++++++++++++++++++
 scripts/z81_gap_audit.py       |  70 +++++++++++++++++++++
 scripts/z81_gap_controls.c     |  54 +++++++++++++++++
 scripts/z81_gap_letters.c      |  53 ++++++++++++++++
 scripts/z81_gap_letters_run.py |  27 +++++++++
 scripts/z81_gap_model.py       |  49 +++++++++++++++
 scripts/z81_gap_packets.py     |  45 ++++++++++++++
 13 files changed, 655 insertions(+)

Review:
**Verdict: ACCEPT WITH FIXES.** I found no mathematical error in any of the PROVED or CONDITIONAL items. The g ≥ 11 statements have no hidden unconditional claim. The problems are in the narrative, the labels and the scope.

## What I checked and found correct

**§1, Lemma A and Theorem B (genus threshold K_gen).**
- **Reduced-form step:** at most O(T log T) reduced forms have A ≤ T. With Siegel this gives a form in the chosen genus with A ≥ b^{1/2−o(1)} and C ≤ b^{1/2+o(1)}. The odd value D taken from A, C, A+B+C is primitive, and −b is a square mod D.
- **Genus signs:** (D/b) has the right sign in both cases b ≡ 1 and b ≡ 3 (4).
- **Lift:** the parities of r and v give s ≡ 3 (4). Coprimality excludes t | v, and s ≪ b²/D + bD ≪ b^{3/2+o(1)}.
- **Case q ≡ 1 (8):** u = −p/q has the required symbol. At every prime power of k = qs, −1 and bp lie in the same squareclass: at t | s because t < q, at q because both are squares.
- **Case q ≡ 5 (8):** 2 | x breaks χ₃, and p breaks χ_{3q}.
- **Seeded constructions** are correct, and the exponent arithmetic α + 3α²/2 is correct.
- **Brute-force check:** the claimed break holds in all 1755 cases q ≡ 5 (8) and 94 cases q ≡ 1 (8) up to 3·10⁵.
- **Size of s:** the worst-case exponent log s/log b falls from 1.76 to 1.49 to 1.44 as b grows (b in 100–400, 5000–5300, 20000–20200), which is consistent with 3/2+ε.

**§2.**
- **Structure lemma:** the plentiful-subgroup argument and the exclusion of H = QR via the seed are correct, and the sieve exponent 1 − 1/(2r) is correct.
- **Dickson construction, both stages:** I checked admissibility, distinct roots, and that every first-M seeded window fails because its residues come from a fixed positive-rational list. (q_s/k) = −1 at prime levels, and t forces g < ∞.

**§3.**
- The k = 7 discrete-log criterion is exact.
- The corollary, the 5569 example (41 ≡ 6 mod 7), the 3^d(1−(−1/3)^s)/2 sign count, and the density argument (δ²/2 > 0) all check out.

**§4 (the quadratic forcing g = 19).**
- All four identities C + Dk = k·w_k² hold, and P(0) = 47161.
- The coefficients, the discriminant −4CL², the fixed-divisor argument and the residue mod 2660 all check.
- P(z) is prime for 26 values of z < 400.

**§5 citations.**
- Achenjang–Woo, arXiv:2611.16062, exists. It is not in the z81-lit corpus. Its abstract matches: linear forms with pairwise independent homogeneous parts plus one imaginary-quadratic norm.
- Nath–Xie Thm 1.1 (p = m²+n²+1, Ω(p+2) ≤ 9), JLL (b(p−1), mn − 1 = ah, Siegel-zero input via Banks [1] and Green [11]) and the FHRSS 1.1(2) hypotheses all check. The §2 supply meets the FHRSS hypotheses (modulus coprime to 6, residue + 3 a unit).
- Pollack: existence for p ≥ 5 is confirmed from the abstract. The "§2" genus fact and the p^{1/4+o(1)} bound are not verified, but both are elementary or low-stakes.

**Constants and models.**
- I recomputed A₃ = 2.21323 and A₇ = 2.24051 from the closed forms independently; they match `coeff.csv`.
- I ≈ 0.0041548 and 4/I ≈ 962.7 are correct, and the Chebyshev bound for the random box is correct.

**Replays and falsifiers.**
- The audit, bulk controls, forecast and letters runs all reproduce the committed outputs exactly. Together they took under a minute.
- Every table entry matches these outputs and `data/z80/xreview/r3_opus/forecast_check.txt` (for example 6010 = 0.3184·18878).
- The F1–F4 rows are confirmed by the audit run.

## Issues to fix

1. **§6 overclaims.** The note says exponent budgets "reduce the gross high-tail error". On the count of g ≥ 111 through 5·10¹² the controls predict 0.311, the z80 genus-pair model 0.390, and 9 are observed, so the count did not improve. Only the mean-one location improved: 75 (z80) to 103 (controls), against an actual 127. The note must say this.
2. **§4 is missing its built-in cap.** With one shared (C, D, T):
   - 3 windows give a conic;
   - 4 windows give two quadrics in P³ (14v² = 3u² + 11w², 7v² − 2u² = 5w₁₅²), a genus-1 curve;
   - 5 windows give three quadrics in P⁴, genus 5 if nonsingular, so only finitely many (C:D) by Faltings.

   So this exact shape cannot push g to infinity even under Bunyakovsky; say so. Also, `packets.txt` only searches the 3, 7, 11 identities. The k = 15 identity was a lucky find, which is fine because the identity itself is the certificate.
3. **§0 label is incomplete.** It omits FHRSS Thm 1.1(2), whose Thm 3.9 extension is unproved in that text (used in §2 and §3). It also omits Pollack, Dickson (§2), and the fact that the §6 theorem is proved only inside the model.
4. **The ex-ante design claim cannot be verified.** `design.md` was committed together with the results, and it shows a revised roughness rule ("to avoid empty populations"). "Zero-fit" should be scoped to the parameters, not the choice of architecture: two models were built and they err in opposite directions.
5. **The "pointwise sufficient family" in §2 adds almost nothing.** The author concedes that its density-one part has g = 7. Demote it to a remark.
6. **Minor points:**
   - The composite controls allow primes ℓ in (B, 123] to divide n, so Pr(ℓ | x_k) is 1/ℓ there instead of 1/(ℓ−1) as for primes. This bias is undocumented.
   - On 𝔐, x₇ is always even, so the route through k = 3 failure in §3 is only needed off 𝔐.
   - The K_gen constant is ineffective, and the Theorem B statement should say so.
7. **Form.**
   - Symbols are reused for different things: b, v, h, r, q.
   - Several sentences are garbled: "p=1 mod 840 and at every odd prime ℓ<q" (a "mod" is missing), "(r,1)=1", "Prefix z81_gap_ in both C source names", "prime cutoff Z greater than 840".
   - The prose is very dense.
8. **Process.**
   - The note proposes triage BARRIER-SCOPED but gives no FRONTIER §6 line. A suggested line: "Jacobi/genus confinement alone cannot force g beyond K_gen ≪ q^{1+3/(8√e)+ε} ≪ p^{0.187} (ineffective)."
   - The branch predates the z81-lit merge, so `git diff main..` shows `LIT.md` and the lit data as deleted, yet GAP_ES cites `LIT.md` §4.5. Merge it; do not apply the two-dot diff.

**Challenge to the note's value.** K_gen is a real pointwise theorem, but it only caps what quadratic-character confinement alone can force. It says nothing about the first successful window g. With ineffective constants it gives nothing numerically (p^{0.186} ≈ 211 at the 127-record). STATUS delta "none" is right.

I did not write a review file or commit anything. The orchestrator can save this text, for example as `data/z81/xreview/REVIEW_GAP_OPUS.md`.
</code-review>
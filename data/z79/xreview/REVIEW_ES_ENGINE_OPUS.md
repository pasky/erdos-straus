<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="main">
A separate reviewer subagent was asked to review the changes in `git log main..`. Its request and review follow.

Request: review changes since main carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab review of notes/z79/ES_ENGINE.md and scripts/z79_* on this branch. Check every proof especially BZ input and exponent, finite-screen loops and novelty/marketing. Give your full review text in response; please do not modify files. Obey strict repo rules; Python only (ulimit -v 1000000; timeout 180 uv run --offline --no-project python -B ...).

Commit log:
commit 6e642925b26472dc1c851427d17215d83a276afd
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sat Nov 21 13:40:32 2026 +0100

    z79: split cyclotomic successors on cube divisors and count square-lock primes

 data/z79/es-engine/check.txt |  30 +++++++++++
 notes/z79/ES_ENGINE.md       |  68 +++++++++++++++++++++++++
 scripts/z79_es_engine.py     | 117 +++++++++++++++++++++++++++++++++++++++++++
 3 files changed, 215 insertions(+)

Review:
# Hostile cross-lab review: `notes/z79/ES_ENGINE.md` and `scripts/z79_es_engine.py` (commit 6e642925b)

**Verdict:** I found no mathematical error, and the script replays bit-for-bit. The HEADLINE triage and the STATUS §1C delta should both be **rejected**. Theorems A and B, the smooth multipliers and C(i) are the classical Type II congruence n ≡ −u (mod tu−1), 4 | t, with one extra condition, y³ | n−1, that does nothing. A one-line class does everything B claims, and does it better. The note gives no credit to prior work in the repo. Theorem D is the only part with non-trivial content. It is correct and uses Baier–Zhao correctly, but the note shows no reason why it matters for ES.

## 0. Scope of the diff
`git diff main..` also shows changes to STATUS, FRONTIER, WAVES, OPERATIONS, ANALYTIC_WILD and a deleted xreview file. Those are not branch edits. The branch forks at 9c58ba4f7, and main has since gained c66c0b62c. The branch itself touches only the three z79 files. **Merge it; do not apply `git diff main..HEAD` as a patch**, because that would revert c66c0b62c.

## 1. Substance, proof by proof

**Theorem A (identities and Jacobi sign): correct.**
- I checked tu = y²−x² = y²−y+2 = A+1 using x² = y−2.
- Since y³ ≡ −1 (mod A), the condition k ≡ u+1 is equivalent to A | n+u. Then n = Av−u = tuv−u−v, and the triple (Cuv, nCv, nCu) checks.
- The residues mod 8 check: y ≡ 3, A ≡ 7, u ≡ 2, t ≡ 4.
- The Jacobi step is right but garbled. "(d/A)=(−1/d)(A/d)" should read (d/A) = (A/d) (since d ≡ 1 mod 4) = (−1/d) = 1 (since A ≡ −1 mod d).
- The hypothesis n ≡ 1 (mod 4) is really 4 | k. That should be said.

**The central objection: the cube divisor does nothing.** The certificate uses only A | n+u and n ≡ 1 (mod 4). The condition y³ | n−1 is just a way of writing that divisibility, plus a restriction to a thinner sub-progression.
- Every n ≡ −u (mod A(x)) with n ≡ 1 (mod 4) has the triple and the Jacobi sign −1, whether or not y³ divides n−1.
- I checked this with a /tmp script (no repo files written). For x = 9, all 36,727 members up to 10⁹ pass. y³ divides n−1 for none of them.
- For x = 1 the "nested" family is just Mordell's class n ≡ 5 (mod 7), cut down to 27 | n−1.
- So two of the note's claims are false as framing:
  - "No search for a divisor of the shifted number": the certificate is literally A | n+u.
  - "Split successor": A+1 = tu holds by definition for every Type II class.
- The identity Φ₆(x²+2)+1 = (y−x)(y+x) is cute, but it is a parametrisation of the classes, not a new mechanism.

**Theorem B (density and the sequence tending to 1): correct but trivial.** The parts I checked all hold:
- x ≡ 1 (mod 24) and x ≡ 0 at the primes ≥ 5 of M give y ≡ 2 and A ≡ 3 there, and 3 | y.
- A is coprime to M, and the progression is reduced.
- Q ≪ M¹¹ and log M = O(√(log log X)), so Q ≤ log X and Siegel–Walfisz applies.
- The tail argument works: Brun–Titchmarsh up to x ≤ X^{1/12}, then the integer count above that.

The trouble is that the plain class t = 4, u = M, A = 4M−1 (C = 1) does strictly better:
- It needs n ≡ 1 (mod M) and n ≡ −M (mod 4M−1).
- Its modulus is about 4M² rather than M¹¹.
- It has the same Jacobi sign −1, because M ≡ 4⁻¹ is a square mod A.
- It gives the same X/(log X)^{1+o(1)} primes per block, tending to 1 profinitely.

I checked it: for M = 840 and M = 110,880, the first 20 primes found in the class all give valid (★) triples with Jacobi sign −1. The note's own C(i) (t = 4, u = w) already exposes this.

"Every fixed menu misses the tail" is automatic for any family that tends to 1 and is certified by Type II classes of growing modulus. FRONTIER B1 ("Fixed witness menus and covers, again") already covers that ground.

Two further points on B:
- Every member is certified by a *single* ET class, so the claim "not an ES exceptional-set estimate" adds nothing over a Dirichlet argument.
- The relative positive prime density is weaker than Vaughan's almost-all result. Its only edge is that the classes are written down.
- The Siegel–Walfisz input makes the threshold X₀ *ineffective*. The note's wording ("explicit", "single formula") should say so.

**Uniform smooth multipliers: correct but trivial.** The sequence kH·2^{jD}+1 is constant mod A, because D = φ(A). The cubefree Proth remark is right. But it confirms that the y³ condition is an artificial restriction, not something that illuminates the Proth problem.

**Proposition C: correct.**
- C(i) is visibly an identity.
- C(ii):
  - n+23 = 24(a+b)A holds.
  - A ≡ −1 (mod 23) at (5, 17).
  - n ≡ 1 (mod 840) and also n ≡ 1 (mod 23).
  - The Hensel lift works (the derivative 3·5² is a unit mod 23).
  - The 2τ(s) representation bound and the N^{2/3+o(1)} count hold.
- C(ii) gap: the proof of the Jacobi sign never handles a and b both even, where A ≡ 0 (mod 4). The argument "(−23/A) = (A/23)" assumes A is odd. The claim still holds, by (A/n) = (A_odd/n), (2/n) = 1 and (2/23) = 1, and the script does test even pairs. But the written proof should cover this case.
- I did not re-verify the U₇ claim via Z68_U7F Lemma 1(a).

**Theorem D: correct. This is the real content.**
- **Baier–Zhao input.** I checked it against arXiv math/0602116. It is **Theorem 4**:
  Σ_{q ≤ x^{2/9−ε}} q · max_{(a,q)=1} |ψ(x; q², a) − x/φ(q²)| ≪ x/(log x)^A.
  - The **weight q** and the exponent **2/9** are quoted correctly.
  - The weight is essential. Plain Bombieri–Vinogradov at level X^{1/2} only gives total error X/log^A, which swamps the main term X^{1−α}.
  - Restricting to the distinct b = Mq ≥ MQ gives error ≪ X/(MQ log^H). Against the main term X/(M²Q log Q), the ratio is M·log/log^H, which is fine.
  - The condition α < 2/9 is exactly what is needed for 2MQ < X^{2/9−ε}.
  - The citation should name Theorem 4 and note that it is ineffective.
- **Mertens, multiplicity and sign.** All check:
  - The ℓ-sum tends to log(5/4).
  - Each q has at most 5 qualifying ℓ, because six such primes multiply to more than Q^{6/5}, which exceeds 2Q+1.
  - q ≡ 3 (mod 8) forces q+1 = 4·odd, so t = 4ℓ ≡ 4 (mod 8).
  - The Jacobi sign: (q/p) = (−u/q) = −(ℓ/q) = −1, using (ℓ/q) = (q/ℓ)(−1/ℓ) = (−1/ℓ)² = 1.
- **Error terms.** Both are small:
  - Prime powers contribute O(Q√X log²X), negligible since α < 1/4.
  - Overlaps of pairs contribute O(X/(M²Q²) + Q²), which is o(main) since α < 1/3. So Bonferroni works.
- **Critique.** The note never says what the repeated factor q² | p+u buys for ES. "Genuine negative divisor repeated" is description, not consequence. The power-sized letters live on a set of X^{1−α} primes, a vanishing proportion.

## 2. Novelty, priority and form
- **Prior work is not cited.** `notes/z78/PROTH_ALLM.md` Thm 2 and `notes/z78/WILD_ES.md` §1, both already in STATUS §1C, use the same mechanism.
  - The shape is n = k·y³+1 with A = y²−y+1 dividing y³+1.
  - The extra condition there is z² − z + 2 ≡ 0 (mod H), which is exactly A+1 ≡ 0.
  - z79 just takes y = x²+2 so that y²−y+2 factors over ℤ.
  - AGENTS §3 requires a priority check for HEADLINE. None was done, even inside the repo.
- **The note contradicts itself.** Its assessment says "no unrestricted ES density record or external priority claim", yet it triages itself HEADLINE with a STATUS delta. Under the STATUS test, adding a §1C row about "nested Φ₆ square-limit constructions" *would* mislead a reader.
- **Recommended triage:** NULL/DATA, or at most one FRONTIER §6 line: "Growing-modulus single Type II classes give ES on X/(log X)^{1+o(1)} primes per block tending to 1; trivial via t = 4, u = M." Theorem D could be kept as an Assessment-level lemma until someone finds a use for it.
- **Smaller form issues:**
  - "Required parity" should say x ≡ 1 (mod 8).
  - "1 is not in a prime-divisor class" is undefined.
  - The wording around "tends to 1 along factorial multiples of w's modulus" is muddled.
  - "M<x≤24M" is correct but loose; in fact x ≤ 2M.
  - The Review field reads "none", which is correct for a lane note, and there is no WAVES line, which is also correct.

## 3. Script `scripts/z79_es_engine.py`
- **Replay.** Under the required limits (ulimit 1 GB, timeout 180) it runs in 0.15 s, and its output is identical to `check.txt`.
- **Code checks.**
  - The `jac` function is correct.
  - The x loop is bounded by n^{1/4}, which more than covers the needed y³ ≤ n.
  - The lock loop covers every prime q ≡ 3 (mod 8) up to √n, with u = (−n) mod q² and 2 ≤ u ≤ q. That correctly relaxes D's window on ℓ.
  - The binary y-bound x + S/x² is always at least S^{1/3}, so no solution is missed.
  - Both parities of (a, b) are covered.
- **Weaknesses.**
  - The F1 and F4 screens are **tautological**. `star()` asserts a valid (★) triple with Jacobi sign −1. So a hit on an odd square or a known (★)-zero would contradict the data or reciprocity, not falsify any theorem. And a hit would crash inside `star`/`binary` before the final `assert not (...)` lines are reached.
  - For Z₇ the binary test is vacuous, since none of those numbers is 1 mod 840. The note says as much.
  - The R₈ control is also vacuous in the A and D tests: their certificates are C-odd.
  - It is fine as a consistency check. It should not be presented as a falsifier table.
  - It tests the redundant y³ kernel. The honest test would be "n ≡ −u (mod A(x)) for some x" (for x = 1, that is n ≡ 5 mod 7).

## 4. Required changes before any promotion
1. State plainly that the A/B certificate is the Type II class A | n+u, and that y³ | n−1 is an optional sub-progression. Drop the "no divisor search" and "split successor" framing.
2. Compare Theorem B with the t = 4, u = M class. Then either show some property that class lacks, or downgrade B.
3. Cite PROTH_ALLM Thm 2 and WILD_ES §1 as the source of the mechanism.
4. Cite BZ as Theorem 4 and mark Theorems B and D as ineffective (Siegel–Walfisz).
5. Fix the Jacobi wording in A, and cover A even in C(ii).
6. Change the triage away from HEADLINE and withdraw the STATUS delta.
</code-review>

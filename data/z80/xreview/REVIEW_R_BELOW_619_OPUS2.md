<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="main">
A separate reviewer subagent was asked to review the changes in `git log main..`. Its request and review follow.

Request: review changes since main carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Second independent hostile Opus cross-lab review, particularly the just-added §4.1 of notes/z80/R_BELOW_619.md in d21e482f5. Check the partial-pin exposure order for arbitrary mixed composites k and conditional equal-sum conic bad rows, its use of z79 local Haar completion and all prime transfer and constant statements. Audit §§1–5 independently; ensure the novelty relative to the two-prime/full-trace Plancherel reduction is scoped and no fixed-4 exponent record claimed. Look for any needed formal repairs to the proofs or scripts or §0. Return a verdict by result. Read-only; for Python use ulimit -v 6000000; timeout <=1800 uv run --offline --no-project python -B.

Commit log:
commit d21e482f5ded562f70498ce36ea0551e3f1625c4
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sat Nov 21 17:33:59 2026 +0100

    Reverse the partial pin to control mixed-period collisions in balanced boxes

 data/z80/r_below_619.txt   |  1 +
 notes/z80/R_BELOW_619.md   | 30 ++++++++++++++++++++++++++++++
 scripts/z80_r_below_619.py | 29 +++++++++++++++++++++++++++--
 3 files changed, 58 insertions(+), 2 deletions(-)

commit b11b31cdb3966358823f51ec6c00504ff994340c
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sat Nov 21 17:31:24 2026 +0100

    Apply Opus scope and provenance fixes and archive full review

 data/z80/xreview/REVIEW_R_BELOW_619_OPUS.md | 90 +++++++++++++++++++++++++++++
 notes/z80/R_BELOW_619.md                    | 18 +++---
 2 files changed, 100 insertions(+), 8 deletions(-)

commit f2c0476308d36df42fbbdcee5e9619d368bde6ea
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sat Nov 21 17:11:30 2026 +0100

    Transfer centered word moments with an upper sieve; gain for large numerators

 data/z80/r_below_619.txt   |  17 +++++++
 notes/z80/R_BELOW_619.md   | 109 +++++++++++++++++++++++++++++++++++++++++++++
 scripts/z80_r_below_619.py |  96 +++++++++++++++++++++++++++++++++++++++
 3 files changed, 222 insertions(+)

Review:
**Verdict: accept every theorem. The repairs below are formal; there are no substantive errors.**

This is a second hostile Opus review covering all of §§1–5, with most weight on §4.1 from d21e482f5. I made no writes. `scripts/z80_r_below_619.py` replays byte-identically to `data/z80/r_below_619.txt` (`ulimit -v 6000000`, `uv run … python -B`, 0.7 s). No master files were touched, which is correct for a lane. Nothing claims a fixed-4 exponent record, and nothing implies one.

## Verdicts by result

**§1, formula (1) and the coherent-lift lower bound (2): ACCEPT, as METHOD-CX.**
- The Fejér coefficients 1−|m|/H and the prefactor W/J (=W²/(TQ) with T=WJ/Q) check out.
- The m<0 stationary points, numbering about cH, each give an integral of size about J/√(aW). That yields the total H^{3/2}√J.
- The exponent works out to (8−25t)/2: it is 1/19 at t=6/19 and 0 at 8/25, and 8/25 > 6801/21497.
- On scope: (1) is an exact rewriting of z79 `ANALYTIC_PUSH` §7 (9)–(11), the two-prime/full-trace Plancherel reduction (expand the square, use the full j-lattice, apply Poisson against Fejér). The only new content is (2), a lower bound on the absolute majorant.
- Suggest adding one sentence saying exactly that. Also, "no Kloosterman sheaf in (11)" and "Deligne cannot be justified" are Assessments sitting under a PROVED header.

**§2, bound (3): ACCEPT.**
- I re-derived the identity ad(qv−g) = qN/M + qv/M + ad(qn₀/M−g) + qa²d/M and the window width K/S + S(KU+B)/M ≪ t₀.
- S ≫ 1 holds because U, B ≪ D < M. Positivity holds with a large constant in the B-cut.
- The crossovers are right: (3) improves on D^{1/3} for M > n^{1/3}, gives O(n^ε) for M ≥ n^{3/7}, and gives no gain at M=4.

**§3, the enveloping upper transfer (5): ACCEPT.**
- The Bonferroni weight S is nonnegative, and S·G = 1 on primes in (X,2X].
- On a reduced class, terms whose divisor shares a prime with l vanish exactly.
- The error terms check out: G_l − G = O(L⁴/z), the ∏_{p|l,p>z} factor is 1+O(L/z), and P_z·G ≪ 1/L.
- For the Selberg pieces I checked |λ_d| ≤ 1 and the Markov argument giving 3/4 of the mass at h ≤ T.
- Citing Ramaré, Ramaré–Ruzsa and Green–Tao is correct and sufficient for priority.

**§4, coefficients (6) and the Type I endpoint: ACCEPT.**
- The constants come out right: 3·(3/π²)/8 = 9/(8π²) and K₃/96 = 1/(112ζ(3)).
- Condition (4) holds, with total absolute Haar mass ⟨(Z+|m|)²⟩_* = O(L^{2s}).
- The chart-disjointness identities hold for any θ < 1/2.
- The sentence extending E to A′ cubes, requested in the first review, is now present and correct: the error margins do not depend on θ.
- Type I: the v-fold lcm is ≤ (4Y^{26/25})^v < X. Hence λ < 25/(26v), which doubles the BV endpoint and gives the eightfold coefficient gain. K.1 still uses BV/BT for the witness primes.

**§4.1, balanced-cube factorial moments and (7): ACCEPT.** I tried to break it hardest at the points below.
- **Step 1.** Conditioning only on n ≡ x_j mod k with k | f_j makes every partner's compatibility modulus k′ = (f_i,k) divide a single determinant:
  - different projection: k′/(ACD) ≪ X^{2w}/D;
  - same projection: h′ | d_i − d_j, so k′/(ACD) ≪ X^w/(AC).
  
  For the pair chart, unequal sums give X^{w−g}. In the equal-sum case with large k′, the z79 conic count needs no target assumption, so the bad-j harmonic mass is ≪ X^{11w−g/2}L. Off-diagonal cubes correctly exclude swaps, the only distinct atoms with an identical event. The crude row bound X^{o(1)} is valid under any polynomial-modulus unit condition.
- **Step 2.** Truncating at small h only needs completion, not projection deletion. The local factors are independent of z and u (z79 §§6.1, 11). Mixed pin tuples are handled uniformly.
- **Step 3, the key step.** If h | (f_j,u), then h divides the product of the pairwise gcds (f_j, f_{i_t}), so some t has (f_j, f_{i_t}) > T^{1/b}. Since k | u, the pin-cylinder probability times 1[z ≡ x_j mod k] equals Pr(pins ∧ n ≡ x_j mod k). The exposure order (partial event at cost 1/φ(k), then i_t via B(j,k), then the rest at X^{o(1)} each) is legitimate for nonnegative terms. The multiplicity of each (h,k) term is ≤ 1.
- **Recursion and transfer.** The recursion gives M^b + O(X^{−κ}). The Poisson pair-partition count gives O(L^{sm}). The transfer needs vθ < 1 and has absolute Haar mass ⟨(Z+M)^v⟩_*. Markov then gives exceptions L^{−sm}.
- **Constants.** 3(3/π²)(1/v)²/2 = 9/(2π²v²) and 1/(14ζ(3)v³), which are 9/(32π²) and 1/(896ζ(3)) at v=4 with rates log⁻⁴ and log⁻⁶. These are scoped correctly: there is no arbitrary saving at the full coefficient of (6).
- This resolves z79 §8's open "balanced mixed pinning" step, and makes G's inexplicit c_A explicit.

**§5: ACCEPT.**
- The Burgess r=2 tail is X^{−1/80+ε}.
- In the Jacobi mean square, nonsquare ij gives U²/X and square ij gives (1+log Y)/Y.
- The identity χ_{p*}(k) = (k/p) holds, including k=2.
- BM_LVALUE Thm A's L(1,χ)² gives the (log log)² bound.

## Formal repairs needed
1. **§0 (required).** d21e482f5 did not update §0, so §4.1 is missing from it.
   - Add (7) to the Result line.
   - Change the Review line: "accepted all theorems" predates §4.1. Cite this second review for §4.1.
   - Triage: RECORD for §4.1.
   - STATUS delta: replace §1A's "at smaller c_A" clause with explicit constants. For each even v, R ≥ (9/(2π²v²)−ξ)log²p outside O(π/log^{v}) and f_II ≥ (1/(14ζ(3)v³)−ξ)log³p outside O(π/log^{3v/2}). This includes the v=4 squared rates. The Type I coefficient 2C_I(25/(26v))³ stays rel. BV/BT.
   - At export, the FRONTIER line 2931 also needs the same update.
2. **Step 1 bad set.** Define the pair-chart bad set explicitly and independently of k: j is bad if it has an equal-sum, nonidentical, nonswapped partner i with (f_i,f_j) > A_*B_*X^{−g/10}. This is what the proof uses, but it is only implicit.
3. **Notation clashes.**
   - b is used for the moment order, a pair coordinate, and §3's log exponent.
   - M is both the numerator and the Haar center.
   - The local tag (8) collides with "z79 §11 (8)" in the same subsection.
   - h′ differs from z79 §11's h′ = h/(4,h).
   - v is both a log-volume and the moment order in §4.
4. **§4.1 label.** Also cite z79 §1 (injectivity) and the §11 conic count.
5. **Script.** `partial_pin` checks a tautology: Pr(A)·1[z ≡ r mod k] = Pr(A ∧ n ≡ r mod k) when k | u. It is a fine sanity check, but the output "partial vs full pins verified" should say "exact identity on toy CRT fibre". It tests none of Step 1's estimates.
</code-review>

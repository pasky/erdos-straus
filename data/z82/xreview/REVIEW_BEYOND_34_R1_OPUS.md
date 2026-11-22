<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="main">
A separate reviewer subagent was asked to review the changes in `git log main..`. Its request and review follow.

Request: review changes since main carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab Claude Opus review of Wave z82 Lane 3 (notes/z82/BEYOND_34.md). Check every analytic bound, uniformity in growing k/moduli, hypothesis statement, scope, and F1–F4 screen. Cap any replay at ≤15 min.

Commit log:
commit de8cdfa4c0a5876eadec3684876a76e5f7db127a
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sun Nov 22 19:49:54 2026 +0100

    Seed rare gap windows and quantify the truncated void and full-count moment obstruction

 data/z82/beyond_34/controls.txt |   2 +
 notes/z82/BEYOND_34.md          | 123 ++++++++++++++++++++++++++++++++++++++++
 scripts/z82_b34_controls.py     |  81 ++++++++++++++++++++++++++
 3 files changed, 206 insertions(+)

Review:
**Verdict:** I found no mathematical error and no proof gap in any of the analytic results (A, B, C⇒, H, S, T). The problems are about scope, wording and propagation: the description of (P), how Theorem S is credited, and the STATUS delta. Nothing here claims ES, and no master file was edited, as the rules require.

## Substance, item by item

**Theorem A (seeded rare hits): sound.**
- **Parameters.** I re-derived them. Balancing the mean exponent `b(s−1)−1/2` (with the seed's `l^{s−1}` gain) against the transfer budget `−(1+b)` gives `b=−1/(2s)` and `v=1−1/(2e)≈0.816` at s=e. At s=3 the whole tilted Poisson band removes the `l^{−1/2}`, giving `b=−1/3` and `v=2/3`. `β−uI(s)=1−u` holds in both cases.
- **Seed distinctness.** Cross-products are at most `d²≤K^{1/5}<q`, and `(d,q)=1` follows from `(4t+1,P)=1`.
- **Lower sieve (1).** It is uniform in the pin and in d ≤ K^{1/10}: the progression has length at least K^{0.9}, the level is K^{1/3}, and s = 10⁴/3. The Markov cuts leave a fixed positive mass.
- **s=3 layers.** They satisfy `T_q3^j≤K` because √l beats 26 log l.
- **Transfer.** With the target set of size T, the second moment is (5/9)^j·|G[2]| = o(1). The transfer budget is `D log Z = 10Cc₀L` exactly, using `δ+u=1` and `v=1+b`.
- **Scope of the gain.** It is a log-log-factor gain only. Seeds can never give more than `l^{O(1)}`, because primes ≤ L carry harmonic mass about log l. The note says this correctly.

**Theorem B (truncated void, two-sided): sound.**
- The D formula, `d=.495229` and the Harris construction all check out. Bits with p = `1/(r−J+1)` conditioned on "at most one success per row" reproduce the exclusive law exactly. Void and the conditioning event are both decreasing, so FKG applies. The relative-error Bonferroni argument is handled correctly, and so is the warning against total-variation transfer.
- **Challenge:** the barrier is tied to u=.249, but the note never says why that value. State the reason. Exposing μ = L^{.751} windows forces `u≤.249`, and in that range `d≤2u≤.498<.751`. That makes the barrier hold for the whole recipe, not just one point. For larger u the truncated d rises to about .64 (at u≈.36, where u+d=1).
- B overlaps SPECIFIC_CLASS J's rare-window D formula. The genuinely new part is the lower void bound, which the note credits correctly.

**§3 budget L^{min(2u,1−u)} ≤ L^{2/3}: correct** as an expected-hit count in the CRT model. It is consistent with GAP_ES's endpoint and with FRONTIER's existing 2/3 supply-law lines. Merge it there rather than adding a new line.

**Proposition C: the implication is valid; the framing is the main objection.**
- I checked the Parseval majorant, the means 1/3 and 5/9 (using (Reχ)²=(1+Reχ²)/2), the rate 0.053245 > .05, and that SW applies (q ≤ (L^{.01})^{76}).
- **Hostile point:** "There is no ES count in it" is misleading. Since `1[P_i(−b_i/m_i)=0] ≤ A_i`, the left side of (P) majorizes the joint band-window miss rate. (P) therefore assumes exactly the step from a pointwise value to an average that z81 paid for with |P̂|, which is where its .4707 came from. The "wider margin" is bought with that extra assumption, not gained.
- On rows whose non-band part is 1 (probability about L^{−.01} per window), the phase is the deterministic −1. There (P) is literally the ES box question.
- I could not falsify (P): quadratic and genus obstructions show up in Ā through |P̂(χ₂)|², and F1 rows cost about √X. Still, it should be described as "ES-adjacent phase independence", and the claim should not appear in the §0 Result as a margin gain.

**Proposition H: correct.** The New Thm 5 product over g<p≤x was checked against `sources/henriot-erratum-2014.pdf`. The Rankin steps (σ=k/L, Y=e^{L/k}) give 1/k! = e^{−.75kl}. Henriot needs no "no fixed prime divisor" hypothesis, so the obstruction is genuine.

**Lemma T: correct.** Numerically, v = 2.30988, m = 0.4705162, x* = 0.40249. z81's (.4,.3,.3) choice gives 0.4705286, which is near-optimal. I(·) = 7.5·10⁻⁶ < 8·10⁻⁶. The Fubini/conjugation reduction holds for complex degree-1 polynomials.

**Theorem S: correct but classical.**
- The triple (1,(p+1)/d′,(d′+1)/4) is valid (v₂(p+1)=1, d′≡3 mod 4, 3B ≤ p+1), the 11d′ trick gives distinct d′, and A = 2^v yields `2^v−1`.
- This is just the classical fact `E τ(p+1)^v ≍ L^{2^v−1}`, which carries over to R through the u=1 line. Say so and cite it, and merge it with the Linnik-spike line from BM_CORRECTED_COUNT Prop. 3.1 instead of presenting it as a new barrier.

**Large-sieve budget:** the arithmetic is right (it caps the saving at (log N)^{3/4}). It is correctly labelled Assessment, since `μ≍t³` is an assumption.

## Form and process
1. **STATUS delta is incomplete.** The (log L)^{3/2} bound is also quoted at `STATUS.md` lines 28 and 111 and `FRONTIER.md` lines 1150 and 2793, and all four must change at export.
   - It is an internal log-log-factor gain, so it barely passes the STATUS test. Replace in place; don't add length.
   - Cross-review owed: per AGENTS §3 this must be an Astra review (this one is Claude-on-Claude).
2. **§0 Triage covers only A and B.** I propose:
   - C: NULL/CONDITIONAL, not STATUS material.
   - H: METHOD-CX.
   - T: BARRIER-SCOPED, merged into the z81 (M) line.
   - S: merged as above.
   - Also set `Review:` to point at this review.
3. **F1 row says "for prime q", but A uses composite windows.** The Jacobi-symbol version covers them; add one clause.
4. **CERTIFIED block:** it should state the engine (a single Python script with two internal methods, direct divisor pairs vs. allocation sums) and that there is no independent coverage. `controls.txt` has no provenance line.
5. **Readability.** The note is very dense, and several "Indeed …" sentences hide multi-step estimates. §5 drifts into tangents (divisor-closed sets, p₁p₂ exceptionality); trim or cut.

**Replay:** `scripts/z82_b34_controls.py` ran in 0.4 s (`ulimit -v 6000000`, timeout 300), its assertions passed, and the output is byte-identical to `data/z82/beyond_34/controls.txt`.
</code-review>
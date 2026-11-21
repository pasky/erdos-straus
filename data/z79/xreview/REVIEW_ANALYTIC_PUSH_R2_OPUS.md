<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="f208aa16a">
A separate reviewer subagent was asked to review the changes in `git log f208aa16a..`. Its request and review follow.

Request: review changes since f208aa16a carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab Round-2 review of notes/z79/ANALYTIC_PUSH.md and scripts/z79_analytic_r2.py, especially §§5–6. GPT-6.2 Astra author lane. Check signed ell pooling, two stationary phases including perturbation and smooth endpoints, Farey pair bound, bin freezing/Fourier/divisor enlargement, product kernel and TY hypotheses, squared LP over dyadic endpoints and full numerator polytope. No repo writes, no side agents, all Python via ulimit -v 6000000; timeout 180 uv run --offline --no-project python. Full verdict; flag every defect.

Commit log:
commit 742fc327d1c688088bf5160e34e791ba839f0ae5
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sat Nov 21 13:57:10 2026 +0100

    Pool dual fourth and sixth powers after a second Poisson transform: 6801/21497

 data/z79/analytic_r2_lp.txt | 40 +++++++++++++++++++
 notes/z79/ANALYTIC_PUSH.md  | 96 ++++++++++++++++++++++++++++++++++++++++++---
 scripts/z79_analytic_r2.py  | 49 +++++++++++++++++++++++
 3 files changed, 179 insertions(+), 6 deletions(-)

Review:
## Verdict: the 6801/21497 bound stands. I found no fatal defect.

I reviewed commit `742fc327d` (§§5–6 of `notes/z79/ANALYTIC_PUSH.md`, `scripts/z79_analytic_r2.py`, `data/z79/analytic_r2_lp.txt`) as the hostile cross-lab Round-2 review. The claim R(n) ≪ n^{6801/21497+ε} is correct as far as I can check it. Fallbacks: if TY Lemma 1.1 fails, the Bourgain pair still gives 999/3157; without exponent pairs, the classical second derivative test gives 25/79. Both still beat 13/41.

Several presentation defects should be fixed before export (list below). My check is relative to two inputs I did not re-prove: z78 §7 / z79 §2, and Trudgian–Yang (TY) Lemma 1.1, whose statement I checked but not its proof. I made no repo writes.

### What I checked and how
- **LP replay:** I reran the script exactly as instructed; the output matches `data/z79/analytic_r2_lp.txt` byte for byte.
- **Independent LP check:** 200k random points per pair, over the whole numerator polytope (μ, α, β, γ) and the interior of the (x, e, i) box rather than just vertices. No violations; the strict conditions f+2s<0 and γ>j+p held everywhere. Testing only the corners is valid: each fibre is a box whose bounds are affine in the base variables, so every point is a convex combination of (vertex, corner) points.
- **Binding vertex by hand:** γ=8−z, j=2, e=l=1, y=4, u=2+z, f=2+2z. The diagonal/kernel tie gives z=(8−2λ)/(3+κ+λ) and θ=(8−z)/(25−3z). The values 7/4, 281/160, 1951/1094 and the saving 620/881377 are all correct.
- **Signed ℓ pooling:** z78 §7 does a triangle in ℓ, then Cauchy in Q per ℓ. So (1/L)Σ_ℓ √(2)_ℓ ≤ (n^δ)^{1/2}·((1/L)Σ_ℓ(2)_ℓ)^{1/2}, and pooling ℓ inside the (ℓ,m) Cauchy is legitimate. The normalisation of (5) is correct, including the (I/K)·D_I term. Pooling is load-bearing: with sample count V₀ instead of E·V₀, the "bin correction" slack becomes −383/21497 and the proof fails.
- **Both stationary phases:**
  - G_s = a u^{4/3} and G_ss = −u²/6 at s=0, which gives −u²/12 in g, confirmed via the implicit derivative y_s=(2/3)y⁻¹.
  - The constants c=(a/3)(3/(4a))⁴ and c′=(3/(4a))⁶/48 are correct.
  - A numerical (mpmath) check of the exact critical value against (6) gives a remainder/(s₀+s₁)² that stays bounded.
  - B₀=X|ℓ|h³p₀/W⁴, w=νW/(h²p₀) and V₀=B/Y are correct.
  - The extended-by-zero leading amplitude is smooth, so no sharp m-cutoff gets Poisson-transformed.
  - The errors O((1+B/Y)B^{-3/2}) are O(B^{-1/2}).
- **Farey bound (7):** the proof is correct (fraction pairs ≤ min²+ηD₁²D₂², multiplicity EV₀/(D₁D₂)). Brute force at A₀≈4000–6000 gives count/(A₀+ηA₀²) ≤ 1.
- **Bins, Fourier, divisor step:** w₆ depends only on the samples. The residual Bσ(w₆−mid)φ is O(1) with row derivatives. The remainder Bσ² is controlled with derivatives (ρ_w=O(s²), ρ_s·∂s=O(σ²)). The bound |α′_{p₀}|≤τ(p₀) and the positive extension of the squared column sum are fine.
- **Kernel and TY hypotheses:** TY (1.1)–(1.2) allow any interval I⊆[N,2N], σ=4 (f′=y x⁻⁴ exactly), y≥N^σ, and constants depending on σ. (1.3) with θ=13/84, the last pair of (1.6), and B(715/10238, 7955/10238)=(1418/5119, 2917/5119) are all verified. The new pair is TY's own hull vertex k₋₄ in (1.14). Over all of TY's hull vertices, k₋₄ maximises z here (next best is k₋₅, at 8305664/26252893), so a different known pair gains nothing further.

### Defects (none fatal)
1. **Dropped cross-term in the decreasing-kernel bound.** The |d|≥1/J part actually costs (J/A₀+1)(J/B)^{1/2}; the note writes min(1,(J/B)^{1/2}). This is only valid via the trivial bound (the normalised quantity is ≤1, so when J>A₀ the J/A₀ term already dominates). This should be said explicitly.
2. **Undefined symbol.** "For a kernel bound uniform by D" uses D for what is really the Λ=min(1,B^κU₀^{λ−κ−1}) bound. "Equivalently" there is also wrong: it is an alternative, not an equivalent.
3. **Missing explicit statement in §5:** the midpoint signs cancel in c_{Q+2k}·c̄_Q (e(mhk)=1), so the second Poisson sum has no half-integer shift and ν is a genuine integer, as (7) requires. It is implicit only through §2.
4. **"Published exponent pair" is unverified wording.** TY Lemma 1.1 is TY's own combination of Sargos, Huxley and Bourgain, and I did not check the paper's journal status. Either cite it as an arXiv v3 lemma (noting it is hull vertex k₋₄), or verify publication.
5. **Misleading script comment.** `# … If J>E V use trivial bound` describes code that is not there. It is harmless because the asserts pass without it, but it should be removed or reworded.
6. **Heavy notation overload**, which a referee will hit:
   - σ means three things: z78's hQ/(2W), the (hN/W)² here, and TY's exponent.
   - y is the stationary point, the exponent of Y, and TY's y=3|cd|BU₀³.
   - B is a scale, the B-transform and "B tails".
   - c, P, p, u, s, f and D each carry two or three meanings.

   At minimum, rename the LP exponents (e.g. ŷ, f̂).
7. **Readability of the (5) paragraph.** It packs in several defensive meta-sentences ("This order does not replace…", "one must not first…"). A short displayed chain of inequalities would be clearer.
8. **Unneeded clause.** "Bounded-length intervals … when U₀=O(1)" never applies, since U₀=NI≥N.
9. **Stale wording in §4.** The "Round 2 target, not an estimate" paragraph now says "we now execute it below" but keeps its Assessment heading. A pointer to §5 would be enough.

### Scope and process
Scoping is honest: §0 Label, Scope and Review all say "§§5–6 cross-review owed", and the ES and exceptional-set exponents are correctly marked as unmoved. Following the lane rule, the commit touches no master files. The STATUS delta n^θ M^{1−4θ} is algebraically right. This review counts as one cross-lab review. A second check of the z78 §7 reduction and of TY Lemma 1.1 would be prudent before calling it a record over 46/145. External priority remains unverified.
</code-review>

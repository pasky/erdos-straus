<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="main">
A separate reviewer subagent was asked to review the changes in `git log main..`. Its request and review follow.

Request: review changes since main carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Independent cross-lab Claude Opus hostile mathematical review for z78 lane 5. Re-derive all exponent optimizations independently (signed dispersion patch / 3/10, both deletion budgets including 2sqrt2 GRH cap, sharp short-window factorial tail). Attack each cited external theorem's actual hypotheses, conductor uniformity and GRH error conventions; disprove if possible the arbitrary valuation parity packet including carrier inside S, norm lower bound despite signed terms, scaling, screenings and all claims. Check script if wanted only via ulimit -v 6000000; timeout 180 uv run --offline --no-project python ... . No edits or commits. Return full review text including verdict and exact repairs; must report any auth/quota/provider error. Do not read the whole repository.

Commit log:
commit 2a17841f3dd38c9aee5a7f52f9ba8bc30f957bbd
Author: Petr Baudis <pasky@ucw.cz>
Date:   Fri Nov 20 20:31:07 2026 +0100

    z78: replay parity packets, signed dispersion and exponent screens

 data/z78/analytic_wild_checks.txt |   9 +++
 notes/z78/ANALYTIC_WILD.md        |   7 +++
 scripts/z78_analytic_wild.py      | 117 ++++++++++++++++++++++++++++++++++++++
 3 files changed, 133 insertions(+)

commit b6e6b7c9a7816e34808dcc21a12b7316aa7ebba4
Author: Petr Baudis <pasky@ucw.cz>
Date:   Fri Nov 20 20:29:09 2026 +0100

    z78: single-valuation planting gives the GRH cap leading constant 2 sqrt(2)

 notes/z78/ANALYTIC_WILD.md | 31 ++++++++++++++++++++++++++++---
 1 file changed, 28 insertions(+), 3 deletions(-)

commit c603fe303ca490112cb89218b06e835f958b3f1d
Author: Petr Baudis <pasky@ucw.cz>
Date:   Fri Nov 20 20:25:48 2026 +0100

    z78: sharp almost-all square-divisor rank in GRH-length windows at primes

 notes/z78/ANALYTIC_WILD.md | 24 +++++++++++++++++++++---
 1 file changed, 21 insertions(+), 3 deletions(-)

commit 6fb0a137dffeed844d9e0f9618d97751f4652eb1
Author: Petr Baudis <pasky@ucw.cz>
Date:   Fri Nov 20 20:19:45 2026 +0100

    z78: sharp adaptive-window entropy floor for the z75 deletion budget

 notes/z78/ANALYTIC_WILD.md | 18 +++++++++++++++++-
 1 file changed, 17 insertions(+), 1 deletion(-)

commit 56b8134936cdc7275554d382c3fa6a1bf8847ed9
Author: Petr Baudis <pasky@ucw.cz>
Date:   Fri Nov 20 19:44:37 2026 +0100

    z78: construct a coherent patch in the signed square-sieve dispersion norm

 notes/z78/ANALYTIC_WILD.md | 25 +++++++++++++++++++++++++
 1 file changed, 25 insertions(+)

Review:
# Cross-lab hostile review (Claude Opus) of z78 lane 5: `notes/z78/ANALYTIC_WILD.md`, `scripts/z78_analytic_wild.py` and `data/z78/analytic_wild_checks.txt`

**Verdict: ACCEPT with minor repairs.** I found no mathematical error. The headline is correct as a CONDITIONAL result on Dirichlet GRH: log(1+e*) ≤ (2√2+o(1))√(log₂R·log₃R). Sections 1–3 are correct as PROVED scoped results. Nothing here claims ES, so no CLAIMED flag is needed. I made no edits or commits, and had no auth, quota or provider errors.

## Form

- **Diff base.** The branch is 4 commits behind `main` (the exact-census commits). Because of that, `git diff main..` falsely shows about 60k deleted lines under `data/z78/exact/**`, `R17_EXACT.md` and other files. The real change is `git diff main...HEAD`: 3 files, 217 lines added. Integrate it by merge or rebase, not by applying the two-dot patch. There are no file overlaps.
- **Rule compliance.** Lane rules are respected: no master files were edited, and §0 has all five fields. The replay is deterministic. I reran it with the stated ulimit and timeout and the output matches `analytic_wild_checks.txt` exactly.
- **Notation reuse.** D means V/W in §1, the CRT modulus 4∏v in §4, and D_k in §§2–3. u, X and k also change meaning between sections. Each section should state that notation is reset.
- **Unit ambiguity.** "2√2" appears in two different units. In §3 it is in u-units; in §0/§4 it is in t-units (t = log₂R). In t-units the §3 square-dividing architecture costs 4.

## Substance, re-derived independently

**§4 parity packet (headline local lemma): correct.** I attacked it from several directions:
- *The sign of K mod q.* (K/q) = (R/q) = (q/R) = −1, and when K is even, q ≡ 7 (8) so (2/q) = 1. So the odd primes of K at odd valuation have symbol product −1.
- *The carrier.* If (V₀/q) = +1, an exterior carrier with odd valuation and symbol −1 must exist. If V₀ itself has symbol −1 (carrier inside S), g = V₀ works.
- *The congruence.* −g lies in the square subgroup U, and j = [U:H] is odd. So (−g)^{−j} = −g^{−j} lies in H, which gives g^j∏v^{2a_v} ≡ −1 mod q.
- *Parity of overflow.* At v ∈ S the overflow is w − 2b = j·1_{v|g} + 2a_v − b_v. This is even both for odd b_v (v divides g) and for even b_v. At the exterior carrier it is j − b_s, also even.
- *Other primes.* There is no overflow at 2 or anywhere else. The identity sums to 4/R. Scaling by n/R leaves the denominator unchanged, every overflowing prime divides A₀ and hence y, and r is coprime to n.
- *Independent stress test* (my own code, kept in /tmp only, not in the repo). It used a different carrier choice (largest instead of first), n of the form R, R² or R·p³, and squarefree R ≡ 1 (8) up to 4000 with q < 3000. All 20,117 packets passed. Of these, 3,313 had some b_v ≥ 2 in S, 650 had an odd b_v ≥ 3, and 3,438 had a proper subgroup H. The repo script does not report high-valuation coverage.

**§4 GRH count: correct.** This is the hypothesis and convention audit for the cited theorems:
- *Coefficients.* The indicator 1_{q≡−R (D)}(1−χ_R)/2 has coefficient ℓ¹ norm exactly 1 and mean 1/(2φ(D)). Here (R,D) = 1 because R's primes are 1 mod 8 and S's are 3 mod 4, and χ_R is primitive of conductor R.
- *Explicit formula under GRH.* The smooth Mellin form plus the zero count N(T+1) − N(T) ≪ log(m(T+2)) (Davenport ch. 16) gives O(√X log m), uniform in conductor m ≤ RD.
- *Trivial zeros.* They contribute O(1), since ŵ(−m) ≪ 2^m and X > 2.
- *Imprimitive lifts.* O(log RD) in total.
- *Main term versus error.* √X·log R ÷ (X/φ(D)) = 1/(D(1+t)⁵) → 0, so the count holds.
- *Height.* u = 2t + O(√(t log t)) is forced by the √X·log R error, so 2√2 is the true constant of this method, not a slack artefact.

**§4 deletion and optimisation: correct.**
- *Bad windows.* At most (3B)^k·O(B log D) windows have a short relation.
- *Index and minima.* |H| > B^k by box injection. Minkowski II for the sup cube gives ∏λᵢ ≤ det. Rounding in a real (non-integral) basis, then shifting by L, gives nonnegative a_v ≤ 2L.
- *Log cost.* 2u/(k+1) + ((k−1)/(k+1))(log D + O(k + log u)).
  - With log D = k·log(k log k) + O(k) (which matches θ(p′_k; 4, 3)) and k = b√(u/log u), this is 2/b + b/2, minimised at b = 2, giving 2√(u log u).
  - With u ~ 2t this is 2√2·√(t log t).

**§3: correct.**
- *Coprimality.* gcd(q, d) = 1 is forced, since a common prime would divide p while being ≤ √T < p.
- *Brun–Titchmarsh.* Montgomery–Vaughan applies with y = 2T and m = 4d² ≤ 4T^{1/4}, and only one constant is incurred (not Cᵏ).
- *Tail.* The d > T^{1/8} tail is O(T^{−1/8} log T), negligible against exp(−O(log₂T·log₃T)).
- *Rankin.* With z = k log k the bound is exp(O(z/log z)) = exp(O(k)).
- *Exceptional set.* Markov at e^k plus Σe^{−k} = o(1) gives one exceptional set for all k.
- *Sharpness.* The progression lower bound matches up to O(k).
- *Maximal rank.* (1±δ)u/(2 log u) holds, using log(k log k) = log u + O(1).

**§2: correct.**
- *Supply bound.* The Mertens and elementary-symmetric bound loses only k·log log u, which is o(k log k) for k ≥ u^η.
- *Certificate floor.* 2/b + b/2 ≥ 2 holds, and the excluded ranges are dominated as stated.

**§1 signed dispersion patch: correct.**
- *Signs and Fourier bounds.* The Rudin–Shapiro prefix bound is O(√m) with no log loss. The row's DFT is P_m(z)(1 − z^m) − z^{2m}, which is O(√q). The zero modes are −1, 0 and q−1, matching z76 §2. I checked the double-root row: the discriminant 4(1 − 16c²n²) vanishes when 4cn ≡ −1.
- *Patch.* Every k − k₀ lies in [0, 1 + 5D/4], which is below (q−1)/2 when P ≥ 10D. Only O(1) primes are exceptional, since log P ≫ log n.
- *Exactness of centring.* Centring removes exactly the frequencies with q|h or r|h.
- *Exponents.* The majorant exponent is (β−γ) + (β − t + γ)/2. Its maximum over the four vertices of {α, γ ≥ t, β ≥ α, β ≥ γ} is 3/2 − 5t, which is positive exactly when t < 3/10.
- *Consistency with z77.* With random-like rows the same norm reproduces z77's diagonal n^{θ−ρ/2}.
- *Consistency with z76.* The mock S_Q stays far below z76's per-Q bound (P²√W ≫ PD), so there is no conflict with the proven 0.3186.

## Challenges and exact repairs

1. **Theorem 1, P range.** The theorem assumes 2P ≤ W, but a prover may choose any P ≥ D. Use a patch of min(⌊P/2⌋, #C) values of C; for P ≥ 2W every C is distinct mod q. Then Σ|A|² ≫ min(P,W)·D², and the exponent only grows. Also note that z77's imprimitive discard needs P² ≤ W, i.e. θ ≥ 2/7. On (1/4, 2/7) the comparison is therefore with a framework that z77 does not itself validate.
2. **ε-bookkeeping in §1 and §5.** Replace "under n^ε bookkeeping compare exponents" with an explicit argument. For a target t < 3/10 at precision ε, use blocks α = γ = t + η with η > ε. The detector then forces P ≥ D·n^{η−ε} ≫ 10D, and the excess is 3/2 − 5t − O(η) > 0.
3. **"At α=γ=θ".** That block is already trivially bounded by n^θ. State that the obstruction lives at α = γ = θ + η.
4. **§4 versus §3.** The comparison "at the same X" is only heuristic. §3 fixes A and is almost-all in a prime p, while §4 is pointwise in R with A = 2 + o(1). Label it as such and give both constants in t-units (4 versus 2√2).
5. **Citation.** Cite the smooth explicit formula from Iwaniec–Kowalski §5.5 or Montgomery–Vaughan §12. Keep Davenport ch. 16 for N(T+1) − N(T).
6. **Sharper cap.** Write the cap as max_v (j·1_{v|g} + 2a_v − b_v)⁺/2 and (j − b_s)/2. "≤ j + max a_v" is true but loose.
7. **Script coverage.** Add a counter for S containing b_v ≥ 2 and odd b_v ≥ 3, as in my stress test.
8. **Triage and STATUS.** The mathematics is sound for the CONDITIONAL row. Replacing O(·) by an explicit constant is a minor record, and a reader of STATUS would not be misled without it. If promoted, change only the existing phrase to "exp((2√2+o(1))√(log₂R·log₃R))". Add "constant of this method", "cross-review: this file" and "priority unverified".
   - The structural gain worth recording in FRONTIER is that arbitrary valuations can be planted singly, which supersedes z75 §6(ii)'s "valuation exactly two" fix.
   - Add §6 one-liners for the coherent mock patch (a 3/10 floor for signed Cauchy in C using only row-size, complete-Fourier and CRT information) and for the §2/§3 certificate floors (BARRIER-SCOPED).

**Scope check.** Nothing claims ES, a lower bound on e*, positivity at the known zeros, or an improvement to R(n). The falsifier screens are correct: 17,401,609 = 47·370,247 and 131 fall in the classical branch, and 4545 (which has a factor 3) is classical too.
</code-review>

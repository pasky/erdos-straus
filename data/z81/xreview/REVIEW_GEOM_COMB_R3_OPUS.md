<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="a19388a02">
A separate reviewer subagent was asked to review the changes in `git log a19388a02..`. Its request and review follow.

Request: review changes since a19388a02 carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab Claude Opus R3 on Round 2 additions in notes/z81/GEOM_COMB.md §§8–10. Audit the 2α largest smooth-gap prime-probability limit in BOTH types (rough labels, Smith-form covariance, absolute Haar mass, ET small corner and BT); the unconditional dyadic-only fixed-r family with P⁺(2x)≤p^.39 and β>3/8 (Pascadi 1.3(i) hypotheses, packing sieve weights, uniform r subtraction with all-cancel exponents and true full-8 box, distinct prime supply and density distinction); sharpness of targeted Euclidean transference via binary codes and exact positive Coppersmith envelope. Falsifiers and small checks; no global ES claim. Flag any gap or overstated sharpness. Cap computational replay ≤10 minutes, ulimit -v 6000000. Give review text, do not edit files.

Commit log:
commit 2e4482d31ce490d59c450c6ff05d74c8924ec2d8
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sun Nov 22 16:18:45 2026 +0100

    Determine smooth-gap normal order and realize a dyadic-only success on a prime family

 data/z81/geom_comb/r2.txt | 13 +++++++
 notes/z81/GEOM_COMB.md    | 85 ++++++++++++++++++++++++++++++++++++++++---
 scripts/z81_gc_r2.py      | 92 +++++++++++++++++++++++++++++++++++++++++++++++
 3 files changed, 185 insertions(+), 5 deletions(-)

Review:
# Hostile cross-lab review (Claude Opus R3): `notes/z81/GEOM_COMB.md` §§8–10, commit `2e4482d31`

**Verdict.** I found no fatal gap in Theorems F or G or Proposition H. Each proof holds at the level of detail written. There are several form and labeling problems, one dependency that needs flagging (Pascadi is a preprint), one stale scope sentence, and a triage that is set too high. There is no global ES claim, and none is implied.

## 0. Replay and my own checks (about 2 min total, `ulimit -v 6000000`)

- **Provided script.** `scripts/z81_gc_r2.py` runs in 1 s and its output is byte-identical to `data/z81/geom_comb/r2.txt`.
- **What the replay actually tests.** The "finite CRT variance" check only confirms the trivial identity E[N²] = Σ_compatible 1/φ(lcm) on a toy period. It does not test the o(1) bound on same-k pairs or the sign of the cross-k covariance. The max-gap check (y = 13, p ≤ 1009) confirms that the reconstruction matches direct fractions, not the asymptotic. Labelling it EVIDENCE is fine; calling it a test of §8 would overstate it.
- **Smith-kernel bound (my brute force).** For k ∈ {195, 231, 91, 87}, over all 2×2 matrices with nonzero determinant, the largest fibre of (u,v) ↦ (u^a v^b, u^c v^d) on ((Z/k)^*)² is:
  - exactly 2^ω(k) for entries in {−1,0,1};
  - exactly 4^ω(k) for entries in {0,1,2}.

  So both bounds hold and are attained.
- **Literal check of the G box model (my script `/tmp/rv/g_check.py`).**
  - Setup: r = 839, with 346 primitive w satisfying (9.1). I took w = 11, b = 7549 ≡ −2, v = 11, F = 105bv, and every squarefree n < 4000 coprime to 2Fr with p = 8Fn − r prime and p ≡ 1 (840): 157 primes.
  - The predicted 8-hit (some exponent combination on the letters of n) matched `window(p,8,x,full)` with 0 mismatches.
  - The 4-window at 2x succeeded every time (II via b/2).
  - 50 of 157 were 8-fail/4-succeed. At such a small r the deletion step is not yet effective, as expected.

## 1. §8, Theorem F

**Smooth-sum estimates.**
- (8.1) checks out: y^s = l/(log l)², the first-power sum is about l/log l = o(l), and H^{−s} = L^{−c/α+o(1)}.
- The lower set T checks out: h log h ≈ c·l/((1−ε)α), C^h = L^{o(1)}, H ≤ k ≤ H² for ε < 1/4, and k ≡ 3 (4).
- The threshold 2α also matches the heuristic count L²·Ψ-density ≈ L^{2−c/α}.

**Lower side.**
- The atoms give genuine smallest-denominator solutions: ab | x because ab is odd, (b,k) = 1 because Z > k, and k < p.
- Sieve bookkeeping is fine: the fundamental lemma applies since log(level)/log Z → ∞, and the coprimality cost (B/Z+1)L is negligible.
- Covariance:
  - Atoms at different k are independent or incompatible, because every common prime exceeds Z > |k−k′|, so their covariance is ≤ 0.
  - Same-k off-diagonal: the 8-type cell argument is correct. Proportional rows must be identical or reversed. Reversal is excluded by the disjoint a and b ranges (Type II); for Type I, rows containing both 1s and 2s force λ = 1. Every occupied cell exceeds Z > k, which justifies the L/k class sums. The total l·L⁸·Σ_{k≥H} 2^ω(k)/k² → 0 because H grows faster than every power of L.
- Transfer: I re-read z80 `R_BELOW_619.md` §3. Condition (4) holds: Σ|c_i| ≤ X^{.12+o(1)} and absolute Haar mass ≤ E_*(N+µ)² ≤ L^{O(1)}. (5) needs only an upper bound on Σ(N−µ)² over primes, so Chebyshev gives a miss rate of O(1/µ). That is correct, and (5) has been Opus-reviewed several times.

**Upper side.**
- In (8.2), the case split on longest-active versus longest-passive is sound.
- The claim that BT lines are primitive (slope < X ≤ p) is correct.
- The small Type I corner has local scale K and uses Cauchy with τ², giving L^{−c/(6α)}; everything else is L^{o(1)}.
- The exponent cap exp(MU) comes correctly from E's combined corollary.

**Subpower-tail refinement and dual x-smooth bound.** Both are fine. The Ψ(X,(log X)^α) = X^{1−1/α+o(1)} input is classical; for the dual bound, de Bruijn deserves a citation.

**Minor issues in §8.**
- Theorem F's header lists BT and Brun-type sieves, but the §0 label omits BT, Dirichlet and E. Align them.
- Notation is heavily overloaded:
  - L = log X here, but L is a constant in §7's E, whose corollary F invokes.
  - l = log₂X, while l, l_i, l′ are primes nearby.
  - h means #primes in T, the Hölder moment, and ma in §10.
  - c is both a constant and an ET coordinate.
  - s is the Rankin exponent and also primes in G.
  - e is the sieve modulus, the exponents e_i, and (β−3/8)/10.

  This makes the hostile audit materially harder; rename before any promotion.
- "Relation to sibling results" points at commits on side-agent branches (`35c8495c`, `403fec59`) and uses opaque labels (W/S/WP, K_gen). These pointers will rot; cite note paths and §s instead.

## 2. §9, Theorem G

**Pascadi Thm 1.3(i).**
- I verified Definition 1.1 and (1.2) against `https://arxiv.org/html/2505.00653v1`. The definition requires 1-bounded sequences supported on q_i ≤ Q_i for every Q₁Q₂Q₃ = Q with each Q_i ≥ 1. The theorem's constant depends on a, which is fine for a = −r fixed.
- Greedy packing works: total size ≤ .615+o(1), waste < 2·.002, and .619 < .62 < 5/8. The bound of m! on multiplicity within a group holds because the prime atoms are > z, e is z-smooth and the 8F atom is fixed. The sieve weights may be signed.
- **Flag:** this is an arXiv preprint. The label should say "(preprint)", as STATUS does for FHRSS.
- **Flag:** the repo excerpt `sources/lit2026f/pascadi-2505.00653-excerpt.txt` paraphrases the theorem ("form as in Maynard II") and omits Definition 1.1. Record both verbatim, since the packing argument depends on the exact definition.
- **Suggest:** state the fallbacks. Lichtman's unconditional 66/107 gives β > 41/107 ≈ .383; Maynard's 3/5 gives β > 2/5. In particular, .39 itself depends on Pascadi.

**(9.1).**
- When i_w + j = 0 the product is a rational ≠ −1, so only finitely many r are bad.
- Otherwise each case forbids at most 2 values of w, so a primitive w survives because φ(r−1) → ∞.
- (b/p) = (b/r) = −1 for r ≡ 7 (8): checked.
- p ≡ 1 (840) follows from r ≡ −1 (840) and 840 | 8F: checked.
- x is odd and the planted valuations are 1 because n is z-rough and the planted primes are fixed: checked.

**Prime supply.**
- The densities g(e) are independent of d. The sieve lower bound is uniform in F because the planted primes only increase the product.
- c₀ is absolute (astronomically small) once η and m are fixed. The overcount is at most (2/η)^m. F cancels between the main term and Y.

**Deletion.**
- The C_η classes per h and the two-form upper sieve are right. The singular series is bounded because Σ_{s|F, s∉{3,5,7}} 1/s ≤ 1, and Σ_h 1/h ≪ 1/η.
- The lost count C′_η·Y/(rL²) is uniform in r, W and F, so a large r beats c₀.
- The "only via 2" statement holds because the 4-box at 2x equals the 8-box plus the coordinate 2 with budget 1.

**Exponent variant.** The arithmetic checks: D₊ + 4e < 5/8 ⇔ 7e < 10e; n′ ≪ X^{β−2e}; and t_i < X^e.

**Problems in §9.**
- **"Hard primes" in the Result line is undefined and overstated.** These are just p ≡ 1 (840); most have a k = 3 solution elsewhere. Replace with "infinitely many p ≡ 1 (840)".
- The distinct-supply bullet (≫ X/log X) does not need the e-sieve. A positive proportion of smooth shifted primes is classical (Friedlander / Baker–Harman exponents below .31), and with k = 3 a hit is generic. Present this as a by-product, not as new strength.
- **Stale scope sentence.** §6's Replay scope still says "no unconditional infinite fixed-k doubly smooth B family". G now gives an unconditional infinite fixed-k family for the 4-only pattern, at k = r large and exponent .39. That sentence needs an update (partial: not k = 31, not arbitrary β, not the both-fail pattern).

## 3. §10, Proposition H and the bilinear box check

**Proposition H.**
- R² = min wt(z) over Az = t, and 4S² = min wt(uA) over u·t = 1. Both are correct.
- The union bounds 2^{dH₂(δ)−m} and 2^{m−d+dH₂(δ)} → 0 when H₂(δ) < 1/2. The dual event also gives full row rank.
- Realization via primes ≡ ±1 at m primes r_j, with (n,x) = (k,x) = 1, is correct.
- Θ(d) is right: the lower constant is δ/2 < .055 and the upper constant is log 2/π ≈ .22.

**Overstatements in §10.**
- "More explicitly … there are examples" is a probabilistic existence statement, not an explicit one.
- The scope line says "dimension-sharp". It is only order-sharp; the constant is not determined.
- This is the classical random-code / Construction-A sharpness of transference (cf. Conway–Thompson, Banaszczyk). §10 should carry an explicit "standard, no priority" remark, as Lemma C does.

**Bilinear box check.** The arithmetic is right: the envelope is h³−3h, attained at (h−1, h+1), and hV − 2√V is increasing. But it is an elementary range computation, not a Coppersmith statement; "exact positive Coppersmith envelope" oversells it. Its value is small: it only restates the 1/3 onset from §5.

## 4. Form and triage

1. **Result line.** The §0 Result was rewritten to cover only the unreviewed §§8–9. It drops Theorems A and E, which are the reviewed content still carried in Label and Scope. Keep a clause for A and E.
2. **Triage HEADLINE is too high.**
   - §9 is an unconditional method counterexample: smoothness, Davenport, a generator and a QNR together do not force the 8-window. That is METHOD-CX / BARRIER-SCOPED.
   - §8 bounds the smooth-difference route: no approach can supply y-smooth gaps above exp((2α+ε)U) for almost all p. At most it is a one-clause addition to the existing STATUS §1D "Actual additive windows" row. That row already has 5 lines against a 6-line cap, so the addition needs compression, and it fails the AGENTS §3 "misled without it" test as a separate item.
3. The label list is incomplete: it is missing BT, Dirichlet, E's corollary, and the preprint status of Pascadi.
4. The notation overload (§1 above) and the branch-commit pointers both need fixing before promotion.

**Recommendation.** Accept F, G (rel. a preprint) and H as PROVED at sketch level once these are fixed:
- the Result line ("hard primes", restore A and E);
- the Pascadi preprint flag plus the fallback exponents;
- the §6 scope sentence;
- "order-sharp" and a no-priority remark for H;
- a triage downgrade to BARRIER-SCOPED / METHOD-CX, with at most a compressed §1D clause.
</code-review>
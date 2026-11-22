<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="main">
A separate reviewer subagent was asked to review the changes in `git log main..`. Its request and review follow.

Request: review changes since main carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab Claude Opus review of Wave z82 Lane 1A (notes/z82/CAP_CONST.md). Check every proof step, quantifier, scope, hypothesis, label, and falsifier check. Cap any computational replay at ≤15 minutes.

Commit log:
commit 7200714aee8a0165aabe063c218d997721c2549b
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sun Nov 22 19:42:10 2026 +0100

    z82 cap: prove fixed-E hierarchy and single-f sieve thresholds

 data/z82/cap_const/hierarchy.txt |  10 +++
 notes/z82/CAP_CONST.md           | 119 +++++++++++++++++++++++++++++
 scripts/z82_cap_hierarchy.py     | 159 +++++++++++++++++++++++++++++++++++++++
 3 files changed, 288 insertions(+)

Review:
**Verdict: ACCEPT WITH MINOR FIXES.** I found no mathematical error in Theorems H, C, L or P, in the §1 chart, or in the HC pairing. The fixes concern how the replay is described, the §0 export text, and presentation.

This was a hostile review of commit `7200714ae`: `notes/z82/CAP_CONST.md`, `scripts/z82_cap_hierarchy.py` and `data/z82/cap_const/hierarchy.txt`. No master files were touched, which matches the lane rules.

## Replay (well under the 15-minute cap)
- **Lane script:** `scripts/z82_cap_hierarchy.py` runs in about 1 s and its output is byte-identical to `hierarchy.txt`.
- **My own script** (`/tmp/z82rev/chk.py`, outside the repo) checked three things:
  - **Exponent list, both directions.** For A<120, caps 0–3 and unit n: 34,529 labels, 0 mismatches. A label is legal exactly when it is on the §1 list. The lane script only tests the listed labels pass, not that unlisted ones fail.
  - **Theorem H construction.** 9,750 random hits, with exponents 1,2,4,…,2E+2, v_s(A)≥2 allowed and u₁ sharing primes with n: 0 failures.
  - **Root count in Theorem P.** ρ_h(t)=gcd(h,t−1) holds for all the h and t tested.

## Substance, step by step
- **§1 chart.** The identity, its converse, D>0 and x>0 all check. The valuations give 2a−d when a<d and ≥a when a≥d. The legal exponent list, the reciprocity argument giving Jacobi −1, and the reduction of z81's V to the same chart (x=(nA+D)/f) are correct. The n=21 failure is genuine.
- **Theorem H.**
  - The exponents 1,2(i−1) are legal for every v_s(A)≥1.
  - If s divides both n and u₁, then v_s(x)=1 and there is no overflow.
  - Labels are unique: D<ℓ, the exponents are distinct, and k<Q. The size bounds Q, 4D < H^{1/10} and [k,k′] < Y^{1/10} hold.
  - Both directions of (1) check, as do the Shiu levels, the Cauchy/BT/BV step, mass t^b per dyad (t^B in total), and the binomial truncation (Taylor remainder sign).
  - The level O(t^{B+1}) and the choice t∝(log N)^{1/(B+1)} give the exponent (E+3)/(E+4).
  - At E=1 the construction is exactly z81's C1, so "recovers, does not improve" is right.
  - Observation: requiring u₂ to be G-supported is unnecessary, because exponent 2 ≤ 2a is always legal even when s divides n. My test confirms this. Requiring it for u₃,… is necessary: 1,599 illegal cases when those share a prime with n.
- **Theorem C.** I checked each substitution against `sieve-limits-note.tex` (`lem:squarebase`, `lem:smoothR`, `thm:noBcap`) and `EXCEPTIONAL_KARY2.md` Lemmas 4.1–4.3.
  - The square base only needs classes containing no unit square, and the §1 Jacobi argument supplies that.
  - The class-count function has F(p)=B and F(p^a) ≤ B^a. The Euler-factor absorption inequality, the choice k=B+1 (smooth tail summable, total (log y)^B), the Shiu fourth-moment bound and the W(E) leak all check.
  - The block sum gives λ^{B/(B+1)}.
  - The §2 majorant is a legitimate member of C's universe: the repair is an ordinary residue combination with selectors at the primes of k. So the exponent is attained.
  - Caveat: this is a substitution sketch over internal, unrefereed machinery. I verified the substitutions, not the whole KARY machinery.
- **Theorem L.** Rankin, the Euler-product bound (E+1)^{1/(1+θ)} = o(λ), and minimising over Q to get N^{1−θ/2} all check. It is consistent with the positive result in `EXSET_LINNIK_CAPS` Theorem 4.2: there c_ε ≈ ε/(8D(3+2ε)) < ε/2.
- **Theorem P.** The root count, the bound M_h ≤ (1+log Y)·#{d|h : d≤Y}, the Rankin step with C(1−σ)<1, the CRT moment, and the final exponent 2−1/a−1/C all check.
- **HC pairing.** I verified both directions, b∤j, k ≪ p^{0.03} and 4|k.
- **Falsifier screens.** All 19 items are addressed and the F1–F4 outputs match the data file.

## Required fixes
1. **Mislabelled replay claim.** The note and data file say "V/C1 identical ordered triples: 99", but `ratio()` never runs C1. It only checks that V's formula equals the chart packet at (f, a²r⁴w). Reword both the note and the script's print line.
2. **Missing export deltas.** §0 does not propose the updates Theorem C makes necessary:
   - FRONTIER lines 1165 and 2792 still say "(KARY3 ceiling still Assessment)";
   - the `CAP_INTERPOLATION.md` §5 "KARY3-type ceiling" row.
   
   Mark these "cross-review owed". The STATUS delta's phrase "squarefree-root-only bound" is also confusing, since at cap 1 every root is squarefree.
3. **Missing corollary.** The Result line claims sharpness at "polynomial level", but C is stated only at level λ. Add the corollary explicitly, using the projection and budget argument of `thm:main`: family primes ≤ N^A and Σ|aᵢ| < N.

## Recommended
4. Resolve the notation collisions in §2: Z is both e^t and the hit count; A, B, E, H, V, W and D each have two meanings.
5. Make the script's exhaustive check two-directional, like mine.
6. The data line "3967 … supports" counts packets, not distinct supports.
7. In P, mark the sentences about "almost every carrier" and the CTS/HC interpretation as Assessment.
8. Name `sieve-limits-note` `thm:noBcap` in the §0 label.

## Debate
The strongest objection is that C's ceiling concerns majorants of everything avoiding the class mixture. True failures need not avoid every C_E class, because of the composite-input trap. The note says this itself ("not … majorants of a smaller set of true failures"), so it is a scope limit, not a defect.

H is a real new result for E≥2 (5/6 at cap 2), but only within the cap relaxation, and its inputs are internal and unrefereed. It has no implication for ES.
</code-review>
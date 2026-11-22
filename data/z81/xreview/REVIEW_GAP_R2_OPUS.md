<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="403fec59a">
A separate reviewer subagent was asked to review the changes in `git log 403fec59a..`. Its request and review follow.

Request: review changes since 403fec59a carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Focused hostile Claude Opus cross-lab review of z81-gap Round 2 additions, notes/z81/GAP_ES.md §§8–12 and §0 plus R2 controls only. Author GPT-6.2 Astra. Please test Theorem C/C′: CRT Möbius truncation, negative association, simultaneous thinned Bonferroni joint transfer, BV harmonic and endpoint exponents at K=log X and (log X)^log3. Verify effective K_gen Tatuzawa removal and K_sub two-generation rank-two BV (Lenstra–Pomerance) selection, and conditional fixed-K_sub separation. For E independently derive the 840 vs 210 normalized constants, Selberg prime-base upper sum and triangle integral/margin under D(0.9908) (including alternative narrow input with BV). Check rank/degree obstruction, finite phase model including phase vs unmarked controls and scripts, labels/priorities/falsifiers. Cross-pointers git show side-agent/z81-specific-class:notes/z81/SPECIFIC_CLASS.md §§1–2; side-agent/z81-geom-comb:notes/z81/GEOM_COMB.md §2. Cap computational replay to ≤15 minutes (all replays should take under 2 min), ≤2 processes with ulimit -v 6000000, Python via uv run --offline --no-project python -B. Do not commit or edit the note; return nonempty review verbatim for me to save.

Commit log:
commit c779d519ab1758f0595fd49cc5d00d89559a998e
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sun Nov 22 16:28:28 2026 +0100

    Control logarithmic gap tails, effective subgroup breaks and the two-shift level

 data/z81/gap/crtcheck.txt   |   3 +
 data/z81/gap/margin.txt     |   2 +
 data/z81/gap/phase.txt      |  39 ++++++++++++
 notes/z81/GAP_ES.md         | 148 ++++++++++++++++++++++++++++++++++++++++++--
 scripts/z81_gap_controls.c  |  25 +++++++-
 scripts/z81_gap_crtcheck.py |  39 ++++++++++++
 scripts/z81_gap_margin.py   |  13 ++++
 scripts/z81_gap_phase.py    |  47 ++++++++++++++
 8 files changed, 310 insertions(+), 6 deletions(-)

commit 5f9778b4153422623be6b982f9b0303ff82b9056
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sun Nov 22 15:54:51 2026 +0100

    Specify linked omega-phase controls before the Round 2 benchmark

 data/z81/gap/round2_design.md | 3 +++
 1 file changed, 3 insertions(+)

Review:
# Review of z81-gap Round 2: `notes/z81/GAP_ES.md` §0 and §§8–12, plus the R2 controls

**Reviewer:** Claude Opus, cross-lab review of Astra (GPT-6.2) work. **Commits reviewed:** 5f9778b41 and c779d519a, since 403fec59a. §§1–7 of the note are unchanged apart from §0. I did not commit anything and did not edit the note. I compiled `controls.bin` for the replay and deleted it afterwards.

**Verdict: ACCEPT WITH FIXES.** I found no mathematical error in Theorems C, C′, D and E, in the Dickson separation, or in §12. Every replay is byte-identical to the committed outputs. The fixes needed are:
- an internal priority overlap that has to be reconciled before any STATUS promotion;
- one stale "ineffective" label;
- label and wording repairs;
- one script output that prints a value it never computes.

## 0. Replays (all under 5 s; `ulimit -v 6000000`, `uv run --offline --no-project python -B`)

- **`z81_gap_margin.py`:** matches `margin.txt` exactly.
- **`z81_gap_crtcheck.py`:** matches `crtcheck.txt` exactly.
- **`controls.c` compile plus `z81_gap_phase.py`:** identical to `phase.txt` (checked with `diff`), in 4.5 s.
- **Independent margin check (my own code):**
  - J(0.48615) = 0.0174470, by two methods: a Simpson rule on the s-form, and a direct midpoint double integral of the (t,v) triangle integral (0.0174471).
  - The true margin of (E) at (τ, ζ) = (0.99078, 0.48615) is 2.5·10⁻⁴. The rational bound of 8·10⁻⁵ is correct but conservative.
  - Scanning over ζ, criterion (E) first becomes positive at τ ≈ 0.99072. So D(0.9908) is essentially the sharp threshold of *this* criterion, with about 10⁻⁴ of slack.
  - For the narrow variant, the threshold is τ ≈ 0.99884, and the true margin at 0.99885 is 4.5·10⁻⁵, matching the script.
- **Independent check of the control p = 4063936801 (own trial division, box and subgroup enumeration):**
  - Windows 3 and 7: no −1 in the subgroup, box misses.
  - Window 11: subgroup contains −1, box misses.
  - Windows 15–51 all miss. Window 55 hits, with x = 1015984214.
  - So K_gen = K_sub = 11 and g = 55, as claimed.

## 1. Theorem C (headline)

### Checks that passed

1. **Interval comparison lemma.**
   - The Möbius coefficients are bounded by 2^{|T|}.
   - The truncation error is at most Σ_{j≤D} C(|S|,j)·C(|S|−j−1, D−j) ≤ 2^{D+1}·C(|S|,D+1), which is below the stated (1+3^{D+1})·C(|S|,D+1).
   - A compatible label set T is a single progression modulo 4∏r, with error O(1/X).
   - The factorial moment is at most (mH)^{D+1}/(D+1)!. Valid.
   - The phrase "enlarging the harmless base 6 to an absolute constant if needed" is sloppy. Replace it with an explicit (C·m·Z)^{D+2}/X.
2. **Negative association (NA).**
   - For a single band prime r, the vector of window marks has at most one 1, so it is NA (covariance zero after removing the all-zero value; this is Joag-Dev–Proschan).
   - NA is preserved under independent unions over r and under independent thinning coins.
   - "Hit" is increasing in the set of marks, so "no hit" is decreasing.
   - Products over disjoint windows are therefore bounded by products of means. Valid, and stated correctly as holding only in the CRT law.
3. **Group lemma.**
   - Pairs of exponent vectors with different supports have a ±1 2×2 minor, so they are pairwise independent.
   - With d = ⌈log K/log 3⌉, the mean count is at least about 1. The same-support pairs contribute O(5^d·2^{ω(k)}/φ(k)²) = K^{−0.53+o(1)}.
   - The second moment then gives a hit probability bounded below by a constant. Valid, including at composite k.
4. **BV selection at K = L and K = L^{log 3}.**
   - Band primes satisfy r ≥ L^{20}/2, so K < T^{1/3} and BV applies on each dyad.
   - Siegel–Walfisz could not cover this, since k ≈ L^{1.1} is not below (log r)^A. BV is genuinely needed, and the constants are correctly called ineffective.
   - The dyad errors sum to (log R)^{1−A}.
   - The discard threshold 1/(K·l²) leaves a relative class error of O(l^{−3}), hence a likelihood ratio 1+O(l^{−2}) over d = O(l) letters.
   - At most K·l²·(20l)^{1−A} = o(K) moduli are discarded.
5. **Exponents, rederived.**
   - The Poisson layer at H = u·l − log l + O(1) gives L^{−uI(t)}·l^{1/2−t}. With log Z = L^u·l^{1/2} it gives L^{−uI(t)}·l^{−t/2}.
   - d/du[β − u·I(a/u)] = t − 1 > 0, while the transfer budget forces δ + u ≤ 1. The optimum is therefore at β − uI = 1 − u, which gives u = (β/(3e·log 3))·3^{1/β}.
   - Hence δ₀ = 1 − 1/(e·log 3) = 0.665142 at β = 1 (t = e), and δ = 2/3 at β = log 3 (t = 3).
   - The ratio t = e·3^{1−1/β} runs over [1, 3] on [b₀, log 3], with t = 1 exactly at b₀.
   - δ₀ is the optimum of this one-layer thinning method. The note correctly makes no claim that it is sharp.
6. **Bonferroni with thinning.**
   - M is even, and the remainder is at most C(N, M+1).
   - The CRT expectation is at most e^{−μ} + (e/10)^{10μ}.
   - With D = 1000·M·l, the first transfer error is (3e/1000)^D. That beats the (2J)^{M+1} terms (log(2J) ≈ β·l) by a huge margin.
   - With c₀ < 10^{−4}, D·log Z ≤ 10⁴·c₀·L, so the second error is exp(−(1−o(1))L).
   - "g > K ⇒ no thinned hit" is correct. A hit at composite k still gives a Type II solution: k | A+B and AB | x.
7. **Part 2.**
   - The range b/log 3 < u − v and u < 1 − b is non-empty exactly when b < b₀.
   - Siegel–Walfisz is legitimate there, since k ≤ L^b ≤ (L^v)^{b/v}.
   - For K = L^{o(1)}: if the box misses, then P(R = −1) = 0 for the random ratio R = ∏g^{ξ−ξ′}. This gives 1 ≤ Σ_{χ odd}∏(1+Re χ)/2, which is valid. The CRT mean is φ(k)·exp(−H/2), and over about K/4 windows this gives exp(−(1/8)·K·l).
8. **Consistency checks.**
   - Odd squares (falsifier F1) have no band hit at any window, since every band prime is Jacobi-positive. There are only about √X of them, far below X·exp(−L^{0.665}).
   - The §6 random model predicts about X·exp(−I·L·l/4), which is consistent with C being only an upper bound.
   - GEOM_COMB A (infinitely many primes with J fixed failing windows) does not contradict a density bound.

### Issues

**C1 (required): priority and overlap with the sibling lane.**
- `side-agent/z81-specific-class` at 6df48876a, SPECIFIC_CLASS §6 Theorem J, was committed 9 minutes before c779d519a. It already contains:
  - the same one-interval Boolean-Möbius coupling, with the same (1+3^s)·C(d,s) truncation bound;
  - b_* = log 3/(1+log 3), which is exactly this note's b₀;
  - "entire band at b < b_*: O(X·exp(−c_b·L^b))", which is essentially Part 2 in shape;
  - a "rare-window extension" capping its own calculation at 0.582306.
- GAP §8 cites only 35c8495c0 §§1–2, and its Assessment says the growing-prefix estimate was not located. That claim must be corrected.
- What is genuinely new here:
  - the thinning plus limited-order Bonferroni step, which exposes about μ windows per term instead of k. This lets log Z be L^{1−δ} rather than L^{1−κ};
  - the use of composite levels.
- Together these beat SPECIFIC's 0.582. At β = 0.635 the interpolation gives δ ≈ 0.60, and at K = L it gives 0.665.
- The note should cite SPECIFIC §6 for the lemma, for b₀ = b_*, and for the Part 2 shape. It should also state the supersession. The orchestrator should keep a single §1D row; GEOM_COMB §8 proposes another §1D addition.

**C2 (labels).** Theorem C's header should add Siegel–Walfisz (Part 2) and z80 G's Fourier majorant (the K = L^{o(1)} case).

**C3 (minor).** Part 1's theorem statement does not mention the β-interpolation that the proof claims. Either state it or drop "as well as the interpolation".

## 2. Corollary C′

- The checks pass:
  - unit-digit law, with label probability 1/(r−1), which is still NA;
  - BV at modulus 4d ≤ X^{o(1)}, with the (2(J+m))^{D+1} multiplicity costing only L^{O(1)};
  - H′ = (1−v)·l − 2·log l;
  - Poisson lower tail L^{−(1−v)·I(a/(1−v))}, with the tilt geometric because a > (1−v)/3;
  - (5/9)^d cost L^{−4/9}, which is negligible since I(a) ≤ 0.018 at β ≥ 0.9.
- Overlap: SPECIFIC §6 J already proves the joint fixed-k band-window bound L^{−kI(a)} on primes, by exact-list pinning. C′'s added content is combining this with J/2 from fixed genus windows, plus a different (BV-Möbius) transfer among primes. This should be cited. C′ is at most a scoped corollary, not a STATUS item.

## 3. Theorem D (effective K_gen and K_sub)

**Auxiliary-prime lemma.**
- The b₀-free smooth count is (1−1/b₀)·Y·(1 − log u).
- The b₀-free character sum is S(Y) − χ(b₀)·S(Y/b₀), using Burgess or the trivial bound.
- This leaves mass at least (1−1/b₀)(1/2 − log u) − o(1) with u < √e, which needs ξ < √e·η.
- 2 is a residue of q, so all such b are odd. Correct and effective.

**Tatuzawa removal.**
- The discriminants Δ_b are distinct, and at most one is exceptional.
- Tatuzawa gives h ≫ b^{1/2−κ} effectively, so Lemma A's reduced-form count goes through.
- For a non-least nonresidue b, the sign conditions still hold: (p/b) = 1 because b < q, and (−p/q | b) = −(−1/b). So "B verbatim" is justified.
- Exponents: α + 3α²/2 = 0.18612 and α + 2α² = 0.19762. The rounded values 0.187 and 0.198 are safe.

**Lenstra–Pomerance selection.**
- I checked against the verbatim statement in `UNIT_REPORT_ADJ51.md`. Q = 4y lies in [T^{1/3}·log T, √T].
- √T·Q·(log T)^5 ≈ 128·y²·(log y)^{12} = o(T).
- A bad b has discrepancy ≫ T/b, since prime powers contribute only o(T/y).
- s(T) > 8, so at most one prime b satisfies s(T) | 4b. The claim "at most one" holds.

**Subgroup argument.**
- (b/s) = (−s/b) = (p/b)(q/b) = −1.
- So p maps to (−,+) and b to (−,−), spanning (ℤ/2)².
- G/⟨p,b⟩ is then 2-divisible, hence of odd order, so −1 ∈ ⟨p,b⟩. Also s ≠ b.

**q ≡ 5 mod 8 at level 3q.** (2/3) = (2/q) = −1 and (p/3) = 1. Correct.

**Issue D1 (required, consistency).** Line 9's "Assessment / proposed FRONTIER §6 line" still reads "K_gen ≪ q^{1+3/(8√e)+ε} ≪ p^{0.187} (ineffective)". Theorem D makes this effective. Rewrite the line, otherwise the export will propagate a stale label.

**Issue D2 (minor).** The §0 Label lumps "effective Burgess, Tatuzawa … Pollack in §§1,10" together. Theorem B in §1 remains Siegel-ineffective. Also add effective Linnik to §0.

## 4. Conditional separation (Dickson) and the control

- I checked the construction line by line:
  - p+11 ≡ 12b mod b², so F ≡ 1 mod b and F ≡ b⁻¹ mod 11.
  - log₂3 ≡ 8 ≡ −2 mod 10. The exponents (−2, 1, −1) sum to values in [−4, 4], which never reaches 5.
  - The ordinary windows are Jacobi-obstructed by reciprocity and the supplement at 7 mod 8.
  - Admissibility holds at b, at t, and at small primes (bF = 1 + (p−1)/12).
  - The window at t has the pair 1, p.
- The claim that 11 is minimal is correct, by §3.
- **Issue S1 (script).** `crtcheck.py` prints "Kgen=Ksub= 11" but computes only K_gen through `genus()`. K_sub = 11 does follow mathematically, from K_sub ≥ K_gen and from b ≡ 2 being a generator mod 11, and my independent enumeration confirms it. Either add a subgroup check or say in the note that K_sub is implied rather than computed.

## 5. Theorem E (conditional on D(0.9908))

I rederived the constants independently.

**Lower sieve.**
- φ(840) = 192, so there are about X/(192·log X) primes p ≡ 1 mod 840.
- V(z) ~ C_V/(ζ·log X), and the linear-sieve lower function is f(s) = 2e^γ·log(s−1)/s.
- Together these give S/U ≥ (2/τ)·log(τ/ζ − 1). Correct.
- The shapes x₃ ≡ 1 mod 210 and x₇ = 2(1 + 105t) are right, so c = 1 or 2, and x₇ may carry extra powers of 2.

**Switched upper sieve.**
- The prime r₂ lies in one class mod 210, so it counts about Y/(48·log Y) with Y = X/(4c·m·r₁). The factor 192/(4c·48) = 1/c is correct.
- The deletion density (1+f)/(ℓ−1) is correct.
- g₀ = g/(1−g) = (1+f)/(ℓ−2−f) gives dimension 3/2.
- 1/G_{mr₁}(B) ≤ w(mr₁)/G(B), by splitting each d into its part dividing mr₁ and the rest. Correct.

**Constant cancellation.**
- The cancellation C_m/(C_G·e^γ·C_V) = c holds:
  - at ℓ > 7, (1−g)·w = 1 gives local ratio 1 for both e = 0 and e = 1;
  - the zeta powers satisfy 1/2 − 3/2 + 1 = 0;
  - the only factor at ℓ ≤ 7 is Σ2^{−a} = 2 for q = 7.
- The per-q cost is (3/2)(2/τ)^{3/2}·J/2. The q-independence of this cost is a nice feature.
- The measures dt/(2t) and d√v, and the triangle 0 ≤ v ≤ 1 − 2t, are correct.
- The ordering condition is consistent: B ≤ X^{τ(1−ζ)/2} < z.

**Triangle integral.**
- The inner integral has the closed form w₀(1+t)/(3(1−t)²·t^{3/2}).
- Substituting s = √(1/t − 2) gives exactly 2s²(s²+2)(s²+3)/(3(1+s²)²).
- 4s² minus the integrand equals (14s⁴ + 10s⁶)/(3(1+s²)²). So the stated upper bound is valid.

**Narrow alternative.**
- It is coherent: BV at Y^{0.4999} on r₂, plus one one-sided lower-weight estimate at 0.99885.
- This is not a lower level. It is a narrower set of required estimates at a higher level, and the note's wording handles this correctly.

**Issue E1 (wording).** §0 Scope says E "needs distribution level 0.9908". Change "needs" to "assumes" or "uses"; the body itself says (E) is not a necessity result. It would also help to record that 0.9908 is within 10⁻⁴ of this criterion's threshold (≈ 0.99072).

**Comparison with W2.** `POINTWISE_WINDOW.md` W2 used an integer base with dimension 5/2. The prime base with dimension 3/2 is what makes the constants cancel. Novelty is limited to the explicit numerical level; FI09 is the technical precedent, as W2 already notes.

## 6. §12 rank and degree obstruction

All of the following check out:
- the chart formula A = (4 + 3B² − 7D² − h²)/(2h);
- the degree-4 part equals N(h + B√−3 + D√−7), via the identity (Z−Y+X)² + 4ZY = (X−Y−Z)² + 4ZX;
- the fibre ideal: the two monic quadrics are equivalent to the linear relation plus A² + 3B² = 3, the ring is free of rank 4, and the localisation is a field. So P_h is absolutely irreducible for h ∉ {±√3 ± √7};
- P + c irreducible for a connected hyperplane arrangement, via constants on each hyperplane and deg(F − a) < d;
- the Lang–Weil local consequence.

The scope is stated correctly. This is BARRIER-SCOPED / METHOD-CX.

## 7. §9 phase controls (EVIDENCE) and scripts

**Design compliance with `round2_design.md` (committed 34 minutes before the results):**
- units are required at both pairs, and at the previous pair through `prev = −1`;
- phase is 3^{ω(last side)} ≥ φ(level);
- the first pair uses marginals;
- backoff goes to linked-unmarked, then to marginal, and is reported (bulk 0, endpoints 1);
- the RNG seed is fixed.

The unlinked arm reproduces Round 1 (10.05, .00788), which is a useful built-in check. Every table entry matches `phase.txt`.

**Issue P1 (interpretation).** "Linking changes the deep tail more than the mark" is true, but the effect at 5T is a nearly uniform ×1.56–1.58 inflation:
- ≥111: 0.3113 → 0.4867.
- ≥127: 0.01784 → 0.02812.
- Bulk ≥47: 10.05 → 15.88, so the bulk fit gets worse.
- The early-record cell is the exception, at ×3.1.

So there is no evidence of a tail-specific correlation being captured. The finite-ω phase mark is a null (+0.5–2%). Triage this as NULL/DATA, WAVES line only.

## 8. §0, labels, falsifiers

- Promoting C to HEADLINE/RECORD in §1D is defensible: it is an unconditional statement about actual first denominators, and it is correctly not an ambient exceptional-set improvement. It needs C1 reconciled first and a single merged §1D row.
- D is better placed as a FRONTIER §3/§6 update than in STATUS. E fits FRONTIER §7 or the W2 row.
- The falsifier supplement (F1–F4) is adequate. F1 is consistent with C, as noted in §1.
- Notation collisions to tidy: J (window count vs the integral), U (units vs √(1/ζ−2)), b (b₀−η vs the nonresidue), c and e (constants vs (q+1)/4 and e_q).

## Summary of fixes

**Required**
- C1: cite SPECIFIC_CLASS §6 at 6df48876a (the coupling lemma, b₀ = b_*, the entire-band and Part 2 shape, J for C′, and the 0.582 rare-window bound now superseded), and correct the priority sentence.
- D1: fix the stale "(ineffective)" proposed FRONTIER line.

**Recommended**
- C2 and D2: complete the labels.
- E1: "needs" → "assumes", and note the threshold of about 0.99072.
- S1: add a K_sub check to `crtcheck.py`, or state that it is implied.
- P1: soften the §9 interpretation.
- C3 and the lemma constant: tidy as noted.

With these fixes I would accept §§8–12 as labeled. ES remains OPEN; nothing here is a claimed proof.
</code-review>
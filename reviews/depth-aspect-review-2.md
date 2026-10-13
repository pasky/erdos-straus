# Hostile review R187 (reviewer 2 of 2, independent) of O178 DEPTH_ASPECT.md — Thms 3.1 and 2.5

Reviewer: side agent R187 (branch `side-agent/review-depth-2`), reviewing `side-agent/spark-depth-aspect` as merged at
commit c1cf4de8. Did not read `reviews/depth-aspect-review.md`. From-scratch scripts: `scripts/review_da2_*.py`.

## Summary verdicts

| claim | verdict |
|---|---|
| Thm 3.1 (ℤ: sterile points on the r-generic line for all large primes r) | **SOUND** (minor repairs D1–D5; none affects the conclusion) |

No FATAL and no MAJOR defects.
| Thm 2.5 (F_q[T], q = 3^r, r ≥ 27 / q ≥ 1.3·10^16) | **SOUND** (minor repairs E1–E4; E1 = the side claim "relative measure ≥ 0.97" is unsupported as written for r = 34, 35 but true on recomputation). Suggestion E5: the method very likely reaches r ≥ 10. |

## 1. Theorem 3.1 (integer side)

### 1.1 What I re-derived (independently)

1. **Box reduction for general r** (MORDELL17 Lemma 1.1 via the POINTWISE_MORDELL §2.1 table). I re-derived every row
   of the §2.1 table directly from the statement of ET Prop 1.9 (pp. 7–8 of `sources/elsholtz-tao-1107.1010.pdf`): at
   x(u) a congruence n ≡ ρ (mod r^k m'), r ∤ m', holds iff ρ ≡ 1 (mod m') and u ≡ ρ (mod r^k); the gcd conditions of
   I2, I3, II3, I4/II1 put r into at most one of the two moduli. The splitting into P / Q / Q⁻¹ / √Q / U / U⁻¹ uses
   only that r is odd (II3: (ad)_r | a²d; I2 with r | f: the change of variables t = (Fg+1)/(4ac) to a Q-datum).
   Nothing used r = 17. Lemma 1.3 (Jacobi reciprocity) is also valid for every odd r, but Thm 3.1 does not need it.
2. **Box values as ES data.** For a Q-datum, 4abd − 1 = Fe gives box −4a²d ≡ −a/b = −y/z for (x,y,z) = π^I(a,b,c,d);
   √Q boxes are the ≤ 2 square roots of a Q value; U boxes are −(x/y + x/z) for (x,y,z) = (iab, iac, ibc) (Lemma 2.2);
   P-data map to N-points (i, j, a', d') of Σ^II_{r^K}, K = k + α ∈ [k, 2k] — I re-expanded
   (4ni−1)(4nj−1) = 4r^K a'n + 1 ⟺ 4ija'd' = i + j + r^K a' (ET (2.15)), and since k ≥ ⌈K/2⌉ the level-k box lies in
   the ball −f mod r^{⌈K/2⌉}, f = 4y/r^K − 1. All boxes are dilation-invariant, and π^I, π^II are injective modulo
   dilation, so per level ≤ f(r^k) values for each of Q, Q⁻¹, U, U⁻¹ and ≤ 2f(r^k) for √Q: **6f(r^k)** is right, and
   one P-ball per N-point of Σ^II_{r^K} (the author's "≤ 2 per point" is a harmless factor-2 overcount).
3. **Brute-force check of 1.–2. for r = 11, 13, 17, 19, 23** (`scripts/review_da2_rgeneric.py`, from scratch). It reads
   all classes of the seven families literally off ET Prop 1.9 for every modulus M ≤ 2·10⁵ (2·10⁴ for r = 17), cuts them
   with the r-generic line, and tests each resulting box against the *predicted* boxes built only from the ES solutions
   of 4/r^k (all ordered solutions, k ≤ kmax) and the solutions of 4/r^K with r^K | y, z (K ≤ 2kmax). Results:
   0 level-0 boxes for every r; every brute-force box of level ≤ 3 (r = 11) resp. ≤ 2 (r = 13, 17, 19, 23) lies in a
   predicted box (103, 34, 30, 47, 33 boxes tested; **0 failures**). The test is not vacuous: the predicted union covers
   5/18 (r = 19) and 9/22 (r = 23) of the unit residues at level 1 and 119/342, 223/506 at level 2.
4. **The N-point bound for Σ^II.** I read ET §3 (pp. 18) and Lemma 2.8 (p. 15). The Type II bounds a ≤ b,
   b < ce ≤ 2b, n/4 < acde ≤ n are derived from (2.14), (2.15) alone (once a ≤ b is imposed), and the four regimes
   (e, ad, ac, cd ≤ n^{2/5}, from e²(ad)(ac)(cd) = (acde)² ≤ n²) use only (2.13), (2.19), (2.20), (2.21) and the divisor
   bound τ(m) ≤ m^{O(1/log log m)} with m ≤ n^{O(1)}. No coprimality and no primality of n is used. So
   #{N-points of Σ^II_n} ≪ n^{2/5 + O(1/log log n)} with **absolute, effective** constants, uniformly in n; this is the
   claimed f_II^N bound (counting all sextuples bounds the dilation classes).
5. **Measure bookkeeping.** With n = r^K, n^{C/log log n} ≤ r^{CK/log log r}; −⌈K/2⌉ ≤ −K/2; the P series is
   ≤ 2A Σ_K r^{−K(1/10 − C/log log r)} and the non-P series ≤ 6C_{1/12} Σ_k r^{−k/4} (Browning–Elsholtz), both
   → 0 as r → ∞. The non-residue units have Haar measure (r−1)/(2r). So the sterile set in the non-residue cells has
   measure ≥ (r−1)/(2r) − S(r) > 0 for r ≥ r₀. Correct.
6. **Cor 4.2 for general r.** A finite union of classes is clopen and misses x(u), hence misses a basic neighbourhood
   {x ≡ u (r^L), x ≡ 1 (Q)} with 8·3·∏_{5≤q<r} q | Q. Its primes have p ≡ 1 (24), (q/p) = (p/q) = 1 for odd q < r
   (p ≡ 1 mod 4), (2/p) = 1 (p ≡ 1 mod 8) and (r/p) = (u/r) = −1: least non-residue exactly r; infinitely many by
   Dirichlet. Correct.
7. **Novelty inside the campaign.** DISCOVERIES (H)/(I): MORDELL13E, 17, 17B, 17C, 17D all end CONDITIONAL ("no
   unconditional sterile point", DISCOVERIES l. 431, MORDELL17C l. 95); x* refuted ((F)11); TYPEI2/3 sterility of x̂_9 open
   (and is Type-I-only); POINTWISE_SIZE Thms M, C, F are statements about formal runs of programs (C is H-conditional) and
   produce no sterile point; the LORENZINI_W "sterile set" (Thm 4.2) concerns a different covering problem. MORDELL17 §2
   proved convergence of the box series at fixed r = 17 but never let r → ∞. So the claim "first proved sterile Mordell
   point other than square points" is accurate for the campaign. Literature: I know of no published statement of this
   kind (ET's remark p. 6 only gives the square obstruction, which lives in the residue cells, not the non-residue
   cells); I did not run a fresh literature search, so this part is Assessment.

### 1.2 Defects in Thm 3.1 (no FATAL, no MAJOR)

**D1 (MINOR) — Browning–Elsholtz is unchecked and makes "effectively computable r₀" depend on an unverified
constant.** Location: Thm 3.1 header ("Browning–Elsholtz f(n) ≪_ε n^{2/3+ε} for all n") and proof line "Hence the Q/U part
of S(r) is ≤ 6C_ε Σ_k …". The original (Browning–Elsholtz, Illinois J. Math. 2011) is not in `sources/`; I could only
check ET's paraphrase (p. 6: "the recent result in [8], which gives the bound f(n) ≪_ε n^{2/3+ε} for all n"), and I could
not check whether its implied constant is effective. The citation is not needed. *Repair:* (i) Q, Q⁻¹, √Q: Q-data are
N-points of Σ^I_{r^k} with r ∤ e (MORDELL17 Lemma 2.1), and ET §3's Σ^I argument (Type I bounds of Lemma 2.8, whose proof
uses only (2.1)–(2.9) and ef ≥ 5, then the four regimes e, f, cd, ac ≪ n^{3/5}) counts them by n^{3/5+O(1/log log n)} with the
same absolute effective constant as in §1.1 item 4; this gives ≤ 4·r^{k(3/5 + C/log log r)} Q-type boxes at level k. (ii) U,
U⁻¹: MORDELL17 Lemma 5.2 (proof r-general: it uses only e ≡ −1 when r | i, Lemma 5.1(ii) and the reciprocity step of
Lemma 1.3) puts every U-box meeting a non-residue cell inside a P-ball of the same centre; U⁻¹ follows by the inversion
symmetry of P (Lemma 1.1). So the U types add no measure in the non-residue cells and S(r) can omit them. Then r₀ is
effective via Nicolas–Robin alone. Alternatively keep BE and drop "effectively".

**D2 (MINOR) — normalisation of the N-point bound.** Location: proof, "f_II^N(n) ≤ n^{2/5 + C/log log n} with an absolute
(effective) C". ET's argument gives ≪ (an absolute implied constant A) and an O(1/log log n); the displayed inequality without
A holds only for n ≥ n₀ after enlarging C. Harmless here (n = r^K ≥ r ≥ r₀), but say so, or carry A (the proof's
"2Σ_K" should read "2AΣ_K"). Also "≤ 2 per point" in §3's preamble is an overcount: each N-point of Σ^II_{r^K} (a, b
ordered) gives one P-ball −f_ET mod r^{⌈K/2⌉}; the reflection is another N-point. Not wrong.

**D3 (MINOR) — the caveat paragraph is now stale / the scope sentence should be precise.** Location: Remark (5) and the §3
preamble "the proofs use only that r is an odd prime". The reduction I re-derived uses: r odd (so the 2-part sits in the
r-free modulus), the gcd conditions of Prop 1.9, (ad)_r | a²d, and the I2 change of variables. No step uses r = 17, any
residue symbol at r, or the size of r (my brute force for r = 11, 13, 17, 19, 23 agrees). Repair: replace Remark (5)'s
"a hostile R-review is still needed" by a pointer to this review and list explicitly that MORDELL17 Lemma 1.3 is not
used (already noted) and Lemma 5.2 is optional (D1).

**D4 (MINOR, presentation) — how large r₀ is.** Remark (2) says log log r₀ ≈ 20C. The binding constraint at accessible r
is not the log log loss but the level-1 terms themselves: `scripts/review_da2_level1.py` (EVIDENCE) gives
6f(r)/r + 2f_II^N(r)/r = 2.01 (r = 883), 2.12 (r = 1999), 1.07 (r = 7019), 1.11 (r = 8423), 0.58 (r = 11171); even this
single term is > 1/2 for many r ~ 10⁴. So the remark is right that the theorem says nothing at computable r; suggest adding
this one line so nobody reads Thm 3.1 as "r ≳ 10⁴".

**D5 (MINOR, wording) — "sterile".** Thm 3.1 uses sterile = "in no class of any of the seven ET Prop 1.9 families" (as in
MORDELL13E/17), whereas TYPEI2/3 use it for Type-I certificates only. The theorem body states the meaning, but the
headline "sterile Mordell points exist" in Remark (2) and any DISCOVERIES entry should keep "for the seven ET families"
attached; it says nothing about non-polynomial or growing-parameter identities (Remark (4) already notes ES is untouched).

**Verdict Thm 3.1: SOUND.** The proof is short and every imported step holds for general odd r with absolute
constants; I found no quantifier or uniformity error. Repairs D1–D5 are presentational / robustness.

## 2. Theorem 2.5 (F_q[T]: no finite linear covering of ES_q(T^k) for q = 3^r, r ≥ 27, and all odd q ≥ 1.3·10^16)

### 2.1 What I re-derived

1. **Reduction to one cylinder per Case B tuple.** Lemma 1.1 of FUNCTIONFIELD_ES3 splits every family valid at a
   slice point into Case A (equal-side types; E | a0 + b0, also for types {2,3} since a0⁻¹ + b0⁻¹ = (a0+b0)/(a0b0)) and
   Case B (mixed; E | D = 1 + T^{k+j+γ}L'g'); validity is the cylinder E ≡ −u (mod T^{N+1}) plus conditions independent of
   u. With s = k + j + γ fixed, Lemma 3.1 (shift (j, γ) → (j − 1, γ + 1), D unchanged) shows the best cylinder has
   j − γ ∈ {0, 1}, i.e. N(s) = k − 1 + ⌈(s − k)/2⌉ = ⌈(s + k − 2)/2⌉; by the converse in Lemma 1.1 that family is itself
   valid on its cylinder, so the union over (N, γ) of the cylinders of one tuple has mass ≤ q^{−(N(s)+1)}, i.e.
   q^{1−N(s)} relative to the c-slice (mass q^{−2}). (B) does not involve k and N(s) increases with k, so k = 2 is the
   worst case. Correct.
2. **Lemma 2.1 (R1)–(R4).** Re-expanded by hand: g'·(m'wC = T^s + v) and g'v = w + C give C(L'w − 1) = g'T^s + w;
   multiplying by m'w gives CEm'w = (E + 1)T^s + m'w². Correct. Also s ≥ 3 (s = 2 forces w = C = T, m' = 1, v = 0).
3. **Lemma 2.2 counting.** Each of the four reconstructions determines the whole tuple from the stated data (I traced
   each: (R1) v then an ordered triple factorisation of the monic degree-s polynomial T^s + v; (R2) L', then g' | L' and
   E | D, then w = (E+1)/L', C = (D/E + 1)/L'; (R3) (w, g'), E | g'T^s + w, then C, L', m', v; (R4) (m', w), E | T^s + m'w²).
   The choice counts q^{t−2} (T² | v, lc v = lc(w + C) ∈ {1, 2}, q odd), q^{a−1} (monic, T ∥ w), q^{y+z}, q^y, q^z are right.
   The optimisation min(s − 3 − σ, 2σ/3) ≤ 2(s − 3)/5 is right, and the per-s exponent
   ⌊2(s−3)/5⌋ + 1 − ⌈s/2⌉ ≤ −max(1, s/10 + 1/5) holds for all s ≥ 3 (checked s ≤ 10⁴). Patterns ≤ s²(s+1)(s−1) ≤ (s+1)⁴.
4. **Lemmas 2.3–2.4 (Case A).** Re-derived (A0)–(A4) by hand from EF = T^α a1' + b1 and E = a1'b1K − 1. In Lemma 2.4:
   z ≠ 0 forces λ ≤ max(f, β) ≤ α, so the λ-range is finite (≤ (α+1)³ patterns is right); in the case f ≥ β, z has
   exact degree f − λ and lc ∈ {1, 2}, giving ≤ 2q^{f−λ} ≤ 2q^f; in the case f < β, deg z = β − λ; (A4) gives
   q^{λ}·q^{κ−1}·q^{f} = q^{λ+α−β−1}; g' | K/T because E + 1 = T·L'·H = a1'b1K. The reduction to γ = 0 is right (E | a1 + b1,
   lc(s) and L' do not depend on γ; the congruence only weakens). Correct.
5. **From-scratch enumeration of 𝓕(s)** (`scripts/review_da2_caseB_enum.py`, own F_p arithmetic, directly from (B),
   not via (R1)): q = 3, s = 3..13: |𝓕(s)| = 0, 2, 4, 10, 8, 8, 4, 24, 12, 14, 36 — identical to §4's famcount list —
   with 0 failures of (R2)–(R4) and 0 violations of the per-pattern bound (both the stated 16^s·q^{min} form and the
   proof's four-bound minimum).
6. **The union-bound numbers** (`scripts/review_da2_largeq.py`, own implementation, log-space). Two versions:
   *stated* = Lemma 2.2 as stated (B(s) = max(2·3^s, 2^s·2^{3s}, 2^{2s}) = 16^s times q^{min exponent}); *fine* = the minimum
   of the four bounds of Lemma 2.2's proof with their own prefactors (2·3^s; 2^{y+z}·2^{s+2y+z}; 2^{s+y}; 2^{max(s,z+2m)}),
   which is what `bsE_largeq.py` uses. Case A as in Lemma 2.4 (B_A = 4·6^α). Exact pattern sums for s, α ≤ 100, rigorous
   ratio-test tail of the theorem's crude closed form beyond 100:

   | r | in-range Case B (stated / fine) | Case A | tail s > 100 | total (stated / fine) | author |
   |---|---|---|---|---|---|
   | 27 | 1.33·10⁻³ / 1.39·10⁻¹⁰ | 3.1·10⁻¹² | 2.56·10⁻² | 2.70·10⁻² / 2.56·10⁻² | 2.6·10⁻² |
   | 33 | 1.56·10⁻⁶ / 1.90·10⁻¹³ | 4.3·10⁻¹⁵ | 2·10⁻³² | 1.56·10⁻⁶ / 1.9·10⁻¹³ | < 2·10⁻¹¹ |

   Further rows (fine / stated totals): r = 28: 1.93·10⁻⁷ / 3.99·10⁻⁴ (author 1.9·10⁻⁷); r = 29: 1.75·10⁻¹¹ / 1.29·10⁻⁴
   (author < 2·10⁻¹¹); r = 34, 35, 36: 6.5·10⁻¹⁴, 2.2·10⁻¹⁴, 7.2·10⁻¹⁵ / 5.2·10⁻⁷, 1.7·10⁻⁷, 5.8·10⁻⁸. The author's fine in-range Case B value at r = 27 (1.385·10⁻¹⁰) is reproduced to
   4 digits; my Case A is slightly smaller than the author's (3.1 vs 4.2·10⁻¹²: bsE_largeq.py uses larger prefactors
   24·3^α, 2^{3α}·2^κ, which is conservative). **At r = 27 the total is entirely the crude tail beyond s = 100**; the
   exact part is 10⁻¹⁰. Both versions give < 1, so the theorem holds even with Lemma 2.2's *stated* constant.
7. **Crude closed form.** 4Σ_s (s+1)⁴(16q^{−1/10})^s q^{−1/5} + 24Σ_α (α+1)³(16q^{−1/2})^α q^{−1/2} (s ≥ 3, α ≥ 1) dominates the
   stated bound term by term (16^s ≥ B(s); 24·16^α ≥ 4·6^α; exponents as in item 3, and ⌊(α−1)/2⌋ − α ≤ −(α+1)/2). My values:
   0.290 at 3^33, 0.155 at 1.3·10^16, **0.130 at 3^34** (claimed "< 0.48": true), 0.061 at 3^35, 0.030 at 3^36; it equals 1 at
   q ≈ 1.20·10^15 (log₃ q ≈ 31.6). So "< 1 for q ≥ 1.3·10^16" is true with a factor ≈ 10 to spare.

8. **Exhaustiveness / logic.** Lemma 1.1 of O173 checked against the definition of linear families and Lemma 6.2 in
   FUNCTIONFIELD_ES §6.2 (A·a0, A·b0 | P + E ⟺ T^k L | P + E; at x_u, P ≡ 1 mod E because T ∤ E, so X ≡ T^{−k}; the four
   type residues). Countable union of cylinders of total relative mass < 1 ⇒ the uncovered part of the c-slice has
   positive Haar measure; its points are in O(q, T^k); O ≠ ∅ ⇒ no finite covering (FUNCTIONFIELD_ES2 §0.1, R166-reviewed).
   No quantifier problem: the counts are uniform in q (only δ(n) ≤ 2^n, δ₃(n) ≤ 3^n and q odd are used) and in c.

### 2.2 Defects in Thm 2.5 (no FATAL, no MAJOR)

**E1 (MINOR) — "relative measure ≥ 0.97 for q = 3^r, r ≥ 27" is not supported as written for r = 34, 35.** Location:
Thm 2.5 statement and proof. The proof evaluates the pattern sums only for 27 ≤ r ≤ 33 and uses the crude closed form
for r ≥ 34, for which it states "< 0.48 at q = 3^34"; that gives only ≥ 0.52. The crude form is 0.130 (r = 34) and
0.061 (r = 35), and drops below 0.03 only at log₃ q ≈ 36.0. The claim is nevertheless true: my pattern sums give totals
≤ 5.2·10⁻⁷ for r = 34, 35, 36 even with Lemma 2.2's stated constant. *Repair:* extend the `bsE_largeq.py` table to
r ≤ 36 and cite it (or weaken to "≥ 0.97 for 27 ≤ r ≤ 33, ≥ 0.87 for r ≥ 34"). Also note that `bsE_largeq.py` as
committed stops at the first r with total < 1 (r = 27), so the quoted r = 28..33 values are not reproducible by its
documented invocation; add an option to continue.

**E2 (MINOR) — which constant is evaluated.** Location: proof, "evaluates … the pattern-wise minimum exactly". The script
uses the four bounds of the *proof* of Lemma 2.2 with their own divisor prefactors (2·3^s, 2^{y+z}·2^{s+2y+z}, 2^{s+y},
2^{max(s,z+2a)}), not Lemma 2.2's stated B·q^{min}. Both are valid, both give < 1 (§2.1 item 6), but the text should say
which one is used, and state that at r = 27 the total 2.6·10⁻² is entirely the crude tail beyond s = 100 (the exact part
is 1.4·10⁻¹⁰).

**E3 (MINOR) — loose numerical statements.** "< 0.48 at q = 3^34" (actual 0.130) and "< 1 for q ≥ 1.3·10^16" (the crude form
already equals 1 at q ≈ 1.20·10^15). Both are true upper statements; the second can be sharpened to q ≥ 1.3·10^15 if wanted.

**E4 (MINOR, label hygiene) — dependence on the unreviewed O173 lemmas.** The theorem is "PROVED, given O173 Lemmas 1.1,
2.1, 3.1, …", and DEPTH_ASPECT's header says O173 is "CLAIMED, under review R173"; there is no
`reviews/functionfield-es3-review.md` on this branch or on main. I re-derived the three lemmas as used here (§2.1 items
1, 2, 8; Lemma 2.1 (a), (b) and the degree count deg v ≤ max(a, b) − deg g', deg(m'wC) = s) and found them correct, so for
the purposes of Thm 2.5 this condition can be recorded as discharged by R187 (pending R173 for the rest of O173).

**E5 (not a defect; Assessment + EVIDENCE) — the threshold r ≥ 27 is an artefact of the truncation, not of the method.**
With the proof-level four-bound minimum the per-s Case B sum decays geometrically much earlier than the crude rate
16q^{−1/10} suggests. `scripts/review_da2_rate.py` (grid search of the asymptotic exponent max_pattern min(e1..e4) − 1/2 per
unit s, in units of log q) gives rate −0.012 (q = 3^10), −0.025 (3^12), −0.046 (3^16), −0.071 (3^27); the stated-B rate
4 log 2/log q − 1/10 is negative only for r ≥ 26. Exact sums for s ≤ 150: 3.7·10⁻² (q = 3^10), 2.1·10⁻³ (3^12), 2.5·10⁻⁵
(3^16), with per-s terms at s = 150 of order 10⁻⁹, 10⁻²⁴, 10⁻⁵²; at q = 3^9 the sum is 5.4 and at 3^8 it is 3.6·10⁷. Case A
(≈ (6q^{−1/2})^α) is negligible for all these q. So the same lemmas very likely give **no finite linear covering of
ES_{3^r}(T^k) for every r ≥ 10** (q ≥ 59049), once a rigorous tail is written (e.g. bound the pattern exponent beyond
s₀ by the exact LP max of min(e1, …, e4), splitting the max(1, z + 2m) term, times (s+1)⁴ patterns). Recommended as a
cheap follow-up; it does not affect the soundness of Thm 2.5 as stated. (The remark "the exponents are not the obstacle;
the constants are" is fair only with a sharp divisor bound: with δ(n) ≤ 2^n the loss 2^s = q^{s·log 2/log q} is itself an
exponent at fixed q, which is why q = 3^9 fails above.)

**Verdict Thm 2.5: SOUND** (E1 is a mis-supported side claim about the size of the uncovered set, true on recomputation;
E2–E4 presentational/label).

## 3. Overall

* Thm 3.1: **SOUND**. Repairs D1 (avoid or qualify Browning–Elsholtz for effectivity), D2–D5 (presentation).
* Thm 2.5: **SOUND**. Repairs E1 (extend the table to r ≤ 36 or weaken 0.97), E2–E4. Suggestion E5 (likely r ≥ 10).
* Novelty (Assessment): Thm 3.1 is, as far as the campaign files show, the first unconditional sterile point for the
  seven ET families outside the square classes; it is a genuinely new logical status, but it is an r → ∞ statement with
  an astronomically large, effectively computable r₀ and says nothing about r = 13, 17.

Replay:
```
PYTHONPATH=scripts uv run python scripts/review_da2_rgeneric.py 19 200000 2     # (also 11 ... 3, 13/23 ... 2, 17 20000 2); ~1-3 min each
uv run --with sympy python scripts/review_da2_level1.py 5 20000 150             # D4 numbers
uv run python scripts/review_da2_caseB_enum.py 3 13                             # §2.1 item 5, ~1 min
uv run python scripts/review_da2_largeq.py 100 27,28,29,33,34,35,36             # §2.1 items 6-7, ~5 min per r
uv run python scripts/review_da2_rate.py; uv run python scripts/review_da2_rate.py 150 10,12,16   # E5
```

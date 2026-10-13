# R175 — hostile review of O175 (SIGNLAYER_DEEP.md + BRAINSTORM/bsB_*.md)

Reviewer: R175 (branch side-agent/review-signlayer). Author files merged from side-agent/spark-signlayer.
From-scratch scripts: `scripts/review_sl_*.py` (own F₃[T] arithmetic; nothing imported from `scripts/bsB_*`).
Data: `data/review_sl_*`.

## Summary verdicts

| Claim | Verdict |
|---|---|
| SIGNLAYER Lemma 1.1 (Case B on the slice = finite search per level K; L'', r, g' forced by (h₁, h₁', K)) | SOUND (re-derived; brute-force verified against direct factorisation of D); MINOR wording defects D1–D3 |
| §2 complete enumeration, CERTIFIED through K = 17 / 19 | SOUND-AFTER-REPAIRS: counts and exact measures reproduced independently through K = 13; the translation "K ≤ 17 ⇒ all N ≤ 18 (j ≤ 17), every L', g" is wrong (D4, MAJOR) |
| Covered measure 0.333 → 0.4906, "≈ 50 % stays uncovered" | numbers SOUND (exact rationals through K = 13); labels EVIDENCE/Assessment acceptable after D5–D6 |
| Lemma 3.1 (symmetries u ↦ u⁻¹, u(T) ↦ u(−T)) | (i) SOUND; (ii) true but the written proof has a GAP (needs FF2's QR degree parity) (D7) |
| "x* orbit = the four height-1 slice points" | FALSE as stated (six height-1 points; two are covered) (D8) |
| Lemma 3.2 (degree imbalance at x*) | SOUND; "necessarily lopsided" slightly overclaimed (D9) |

(Memo verdicts follow in later sections.)

## SIGNLAYER Lemma 1.1 — SOUND

*Dependence on FF2.* The lemma takes as input FF2 §0.2's Case B reduction (validity of a family at x_u ⟺ D = 1 + T^k a0 b0
= 1 + T^{N+1}L'g has a monic divisor E with E ≡ −u (mod T^{N+1}), E ≡ −1 (mod L')), which R166 re-derived and found
SOUND, and which only uses x ≡ 1 at every prime ≠ T (so it holds at every slice point x_u, not only x*). Note
lc E = 1 because the two terms of the Case B sum have different degree, so the cofactor E' is monic as well. I accept
the reduction. Lemma 1.1 is valid only for the **sub-slice u ≡ 1 (mod T), u ≢ 1 (mod T²)** (v(0) ≠ 0). This is
where h₁(0) ≠ 0 is used (D5).

*Re-derivation.* E = −1 + L'h, E' = −1 + L'h' (from E ≡ −1 mod L'; this also holds for E' because D ≡ 1 mod L').
EE' = D ⟺ L'hh' − h − h' = T^{N+1}g. E ≡ −u (mod T^{N+1}) ⟺ L'h ≡ −Tv, so h = Th₁ with h₁L' ≡ −v (mod T^N) and
h₁(0) ≠ 0. Reducing the identity mod T gives T | h'. (The proof says "same for E'". That step needs this one-line
argument, which the proof leaves out. MINOR, D2.) So h' = Th₁' and T h₁h₁'L' − h₁ − h₁' = T^{N+γ}g', where
N + γ = K + 1. The leading term T h₁h₁'L' cannot cancel. This gives a + b + deg L' = K + deg g', i.e.
a + b + deg L'' = K. Since gcd(g', T) = 1, Tg' | h₁ + h₁'. That gives r and (I), (II). r ≠ 0, because r = 0 forces
h₁h₁'L'' = T^K with all three factors T-free, so K = 0 and h₁ = h₁' = 1, contradicting h₁(0) = −h₁'(0).
deg r ≤ max(a, b) − 1 − deg g' < a + b. So L'' = quo(T^K, h₁h₁') and r = L''h₁h₁' − T^K are forced. **In addition,
g' = (h₁ + h₁')/(T r) is forced**, so the whole tuple is a function of (h₁, h₁', K). This is how the enumeration
uses it; the statement lists g' as a free coordinate. The admissible N are exactly ⌈K/2⌉ + 1 ≤ N ≤ K + 1, from
0 ≤ γ = K + 1 − N ≤ N − 1. The cylinders for different N are nested, so the union over N is the N₀ cylinder,
N₀ = max(2, ⌈K/2⌉ + 1). D = 1 + T^{K+2}L'g' does not depend on N. The converse direction checks out. As a
by-product, j = 0 (N = 1) is impossible: it would force K = 0. This proves one of FF2's unproved "consequences"
(R166 D5) on the slice.

*Bound.* deg L' = deg g' + deg L'' ≤ (max(a, b) − 1) + (K − a − b) ≤ K − 1. The stated "deg L' ≤ 2K" is true but
loose (MINOR, D3).

*Independent machine check* (`scripts/review_sl_caseB.py brute 6 3`, `data/review_sl_brute_6_3.txt`). For every
N ≤ 6, 0 ≤ γ ≤ N − 1, monic T-free L' of degree ≤ 3 and every monic g' | L', I factored D = 1 + T^{N+1+γ}L'g'
completely, by trial division with my own irreducibles. For each monic divisor E with E(0) = −1, E ≡ −1 (mod L')
and v(0) ≠ 0, I recorded (N, γ, L', g', E). Result: **126 families**, identical as a set to those predicted by
Lemma 1.1 (enumerating (h₁, h₁') with K ≤ 10 and expanding over N). Nothing is missing and nothing is extra. So
Lemma 1.1 is correct both as algebra and as a search reduction.

**D1 (MINOR, wording).** "correspond bijectively to tuples (h₁, h₁', g', L'', r)". The bijection is with the data
(N, γ, L', g', E). A Case B *family* also carries (a0, b0, types), and many (a0, b0) share the same L = lcm and
g = gcd. Also, g' and L'' are functions of (h₁, h₁', K). Repair: "with the divisor data (N, γ, L', g', E); moreover
the whole tuple is determined by (h₁, h₁', K)".
**D2 (MINOR).** Proof: write the line "mod T, h' ≡ 0, so h' = Th₁'".
**D3 (MINOR).** Replace "deg L' ≤ K + max deg h ≤ 2K" with the sharp bound deg L' ≤ K − 1 − min(a, b).

## §2 complete enumeration (CERTIFIED through K = 17 / 19) — SOUND-AFTER-REPAIRS

*Completeness per level.* By Lemma 1.1, every Case B family on the sub-slice at level K comes from a pair of monic
(h₁, h₁') with h₁(0) = −h₁'(0) ≠ 0 and a + b ≤ K. The author's enumeration (`bsB_caseB.c`, read: it loops over
exactly these pairs and then applies the forced L'', r, g') is therefore complete per level, **given FF2's Case B
reduction**. CERTIFIED is an acceptable label for "no Case B family at x*_c with K ≤ 19", conditional on the
correctness of one C implementation for K = 14..19.

*Independent reproduction* (`scripts/review_sl_caseB.py enum 13`, Python, own arithmetic, 55 s; output
`data/review_sl_caseB_K13.txt`). Solutions per K = 2..13: 2, 4, 10, 8, 8, 4, 24, 12, 14, 36, 104, 48. This is
**identical** to the author's list. Exact union measures (Haar on v ∈ F₃[[T]]^*):
1/3 (K ≤ 2..4), 11/27 = 0.4074 (K ≤ 5..7), 37/81 = 0.4568 (K ≤ 8, 9), 113/243 = 0.4650, 343/729 = 0.4705,
349/729 = 0.4787, 1051/2187 = 0.4806 (K ≤ 10..13). These agree with the author's 0.333, 0.407, 0.457, 0.465, 0.471,
0.479, 0.481. x*₁, x*₂ and ι(x*_c) = 1/(1 − cT) are uncovered for all K ≤ 13. (K ≤ 15 run: see the addendum below
if it completed.) Sanity: the K = 2 pair is FF2's cylinder family, as the author says.

**D4 (MAJOR, overclaimed certified range).** §2, bullet 3: "x*₁ and x*₂ are not covered by any Case B family with
K ≤ 17, **i.e. with N ≤ 18 (j ≤ 17) and every admissible L', g**". This is false as a translation.
K = N + γ − 1 and γ ranges over 0..N − 1. So K ≤ 17 contains a family with given N only if γ ≤ 18 − N. "Every
admissible g" (γ up to N − 1) needs 2N − 2 ≤ 17, i.e. **N ≤ 9 (j ≤ 8)**. With K ≤ 19 it is N ≤ 10 (j ≤ 9), which
the "Update" paragraph states correctly. The same slip is repeated in AGENT_REPORT_O175 if it quotes "N ≤ 18";
check it. Repair: "complete for all families with N + γ ≤ 18; in particular for all N ≤ 9 (j ≤ 8) with every
admissible L', g (deg L' ≤ K − 1 is automatic)". The comparison with FF2's range (deg L' ≤ 7, j ≤ 8) remains
correct: K ≤ 17 contains it.

**D5 (MINOR, scope of "the slice").** Lemma 1.1, the measures, and "random slice points" all refer to the sub-slice
u = 1 + Tv with v(0) ≠ 0, i.e. u ≡ 1 + cT (mod T²), c ≠ 0. It is normalised to measure 1. The rest of FF2's slice
x ≡ 1 off T (u(0) = 2, or u ≡ 1 mod T²) is not treated: the derivation uses h₁(0) ≠ 0. Repair: say "sub-slice" (or
define "slice" this way in §1) wherever measures are quoted.

**D6 (MINOR→MAJOR for the narrative; labels).**
(a) §1 "Consequence for the heuristic": "the naive expected number of solutions at a fixed point is
Σ_K poly(K)·3^{−K}-type, **convergent**". Lemma 1.1 refutes FF2's specific divergence argument: the sum over
ℓ = deg L' is truncated at ℓ ≤ K − 1, and D does not depend on N. But Lemma 1.1 does **not** by itself give
convergence. A level-K solution covers a cylinder of measure (1/2)·3^{−⌈K/2⌉}, not 3^{−K}. The only a priori bound
on #sol(K) is the number of (h₁, h₁') pairs, ≈ K·3^{K}, and with that bound the expected-count sum diverges. The
convergence rests on the **observed** growth #sol(K) ≈ 3^{K/4} (ratio ≈ 1.3–1.5 per two levels, versus the
critical 3 per two levels). That is EVIDENCE, not a consequence of the lemma. Repair: state the expected-coverage
sum as Σ_K #sol(K)·3^{−K/2}. Say it converges iff #sol(K) = o(3^{K/2}) (with summable excess), and note that the
data (not Lemma 1.1) suggest this.
(b) "Reading" §2: "O(3, T²) ∩ slice has positive measure" also needs Case A to be absent on the sub-slice. The
support for that is four points with deg a0, b0 ≤ 3. It is labelled EVIDENCE, but it is very weak; say so. Also,
the limit "≈ 0.5" is an extrapolation of a monotone sequence (0.4806 at K ≤ 13, 0.4906 at K ≤ 19) whose increments
are not shown to be summable. Assessment is the right label, and "appears to converge to ≈ 0.5, not 1" should
read "the increments are consistent with a limit well below 1".

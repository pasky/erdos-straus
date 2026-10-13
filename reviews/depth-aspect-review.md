# R178 — hostile review of O178 DEPTH_ASPECT.md (reviewer 1 of 2, full document)

Reviewer branch: side-agent/review-depth-1 (merged side-agent/spark-depth-aspect at 0c6e57d2 basis).
From-scratch scripts: `scripts/review_da_*.py`; outputs `data/review_da/`.

## Summary verdicts

**No FATAL, no MAJOR; 14 MINOR.** All numerics were reproduced exactly by from-scratch code.

| claim | verdict |
|---|---|
| §1.1 table of q-power moduli, parity kill | SOUND (m1 scope wording) |
| §1.3 EVIDENCE: q = 3 misses 1233 primes ≤ 10⁶ (q = 7: 3518; q = 11: 259 ≤ 2·10⁴) | SOUND, reproduced exactly to 10⁶ with complete bounds (m2 wording) |
| Lemma 1.3 (repaired scope) | SOUND (near-trivial) |
| §1.2/1.4 Assessments | labels appropriate |
| Lemma 2.1 (R1)–(R4) | SOUND |
| **Lemma 2.2** (Case B ≤ C^s q^{2(s−3)/5}) | SOUND |
| Lemma 2.3 (Case A identities) | SOUND |
| Lemma 2.4 (Case A count) | SOUND-AFTER-REPAIRS (m4: z-count needs T ∣ z; m5 garbled sentence) |
| **Theorem 2.5** (q = 3^r, r ≥ 27; odd q ≥ 1.3·10^16; ≥ 97 %) | SOUND relative to O173 Lemmas 1.1/2.1, R166 step (1) and ES2 §0.1 (Lemma 3.1 not needed, m7). The union bound was recomputed: < 1 for all r ≥ 27 (and r = 26) even with the cruder stated constants (m8, m9). Consistent with O179 Thm 3.2 (Haar-null in R̂^*, positive on a null slice). |
| **Theorem 3.1** (sterile r-generic points for all large r) | SOUND relative to the cited inputs. The general-r transfer of MORDELL17 Lemmas 1.1, 2.1–2.3 and Cor 4.2 was re-derived, and brute-force checked for r ≤ 31 at levels ≤ 2. ET's O(1/log log n) is uniform for N-points. The BE input can and should be replaced by ET-only inputs for the effectivity claim (m11). |
| §4 EVIDENCE (Case B/A counts, masses 1.74/0.088) | SOUND, reproduced (m6 convention) |
| By-product #{cfg − c − f = n} ≪ n^{1/3+o(1)} | SOUND (m10 one line) |
| Labels | appropriate throughout. Thm 2.5 inherits any R173 defect in O173 Lemmas 1.1/2.1. |

## §1 (ℤ, prime-power moduli)

**1.1 table + parity — SOUND (minor wording).** Re-derived: (I-t), (II-e) rows are CONDITIONAL_ES Lemma 1.2 with
t, e = q^s. (I-cd) agrees with ET's slicing {n ≡ −f (4cd)} ∩ {n² ≡ −4c²d (f)} (ET line "n = −f mod 4cd", p. 8 of
arXiv 1107.1010). (II-cd): f f' = 16abc²d² − 4cd(a+b) + 1 = 4cd(4abcd − a − b) + 1 = 4c²dn + 1 since
4abcd = cn + ce = cn + a + b. `scripts/review_da_slices.py` checks both on all 5386 Type I/II tuples of the primes
5 ≤ n < 400 (complete t-range, see below): 0 violations. Parity: 4abd = q^s n + 1 resp. n + q^s; for n ≡ 1 (4) both
need q^s ≡ 3 (4), i.e. q ≡ 3 (4) and s odd. Correct. (s = 0 is parity-dead for n ≡ 1 (4) and trivially solving for
n ≡ 3 (4), so all failures are ≡ 1 (4); the q = 3 failures are in fact all ≡ 1 (24).) See m1 for the q = 2 scope.

**1.3 numerics — SOUND (independently reproduced exactly).** `scripts/review_da_qpow.py` (from scratch; sympy only
for integer factorisation) uses complete bounds that I derived independently of ET Lemma 2.8: any denominator of a
solution of 4/n is ≤ 9n⁴/8 (x₁ ≤ 3n/4, x₂ ≤ 2nx₁, x₃ ≤ n x₁x₂), and x = abdn, tn = 4x/n − 1 give t < 9n²/2 for
Type I; for Type II, e ≤ a + b ≤ ab + 1 and n + e = 4abd ≥ 4(e − 1) give e ≤ (n + 4)/3 (checked on the tuples above).
Every solution is rebuilt in exact rationals. Results (`data/review_da/`):
| q | range | my failures | author | max least s |
|---|---|---|---|---|
| 3 | 5 ≤ p ≤ 10⁶ | **1233** (42 below 2·10⁴) | 1233 (42) | 7 (author: 7) |
| 7 | 5 ≤ p ≤ 10⁶ | **3518** (915 ≤ 2·10⁵) | 3518 | 5 |
| 11 | 5 ≤ p ≤ 2·10⁴ | **259** | 259 | 1 |
First q = 3 failures 241, 409, 769, 1249, 1321, … and first q = 7 failures 5, 13, 29, 53, 61, … agree with the
document. (The author's `data/bsE/q3_1e6.txt` lists only 20 failures + the 4 record primes, so only the count and
the first 20 could be compared list-wise; they agree.)

**Lemma 1.3 — SOUND in its repaired scope (near-trivial).** If 4a_s b_s d_s = Xn + 1 identically in X = q^s with
a_s, b_s, d_s affine in X, exactly one factor is non-constant. If a_s is, a_s ≡ (4bd)^{−1} (mod q^s) (4bd is prime to
q), so q^s | a_s + b iff q^s | 1 + 4b²d: bounded s. If d_s is, s ≤ v_q(a + b). Correct. Gaps of scope only: the
Type II row (4abd = n + q^s) is not stated (same proof works), and "v_q(1 + 4b²d) = ∞ is impossible" is just
1 + 4b²d ≠ 0. The periodicity sentence (ℓ | q^s n + 1 ⟺ q^s ≡ −n^{−1} (ℓ)) is correct.

**1.2 / 1.4 — Assessment / CONJECTURE labels appropriate.** The per-s means are from the truncated engine (noted by
the author). The verdict "dead" is an Assessment and is supported by the numerics.

## §2 (F_q[T])

From-scratch code: `scripts/review_da_ff.py` (own F_q[T] arithmetic; sympy `gf_factor` only as a black-box
factoriser over F_p), `scripts/review_da_thm25.py` (union-bound arithmetic). Logs in `data/review_da/`.

**Lemma 2.1 (R1)–(R4) — SOUND.** Re-derived: g'·(m'wC = T^s + v) and g'v = w + C give C(L'w − 1) = g'T^s + w (R3);
times m'w: C·E·m'w = (E + 1)T^s + m'w², so E | T^s + m'w² (R4). Non-vanishing: deg g'T^s = s + y > a, and
v_T(m'w²) = 2 < s. Machine check: every tuple of 𝓕(s) for q = 3, s ≤ 14; q = 5, s ≤ 9; q = 7, s ≤ 8 satisfies
EE' = 1 + T^sL'g', (R3) with quotient exactly C, (R4), and L' = (E + 1)/w.

**𝓕(s) enumeration — independently reproduced.** I enumerate 𝓕(s) by a different route from the author
(author: (w, C) and v := −T^s mod wC; mine: v with T² ∥ v and lc v ∈ {1, 2}, factor T^s + v, split into ordered
triples (m', w, C) with T ∥ w, T ∥ C, T ∤ m', then test v | w + C with monic, T-free quotient g'). Counts
|𝓕(s)|, q = 3, s = 4..14: 2, 4, 10, 8, 8, 4, 24, 12, 14, 36, 104 — identical to §4. q = 5, s = 3..9: 0,0,0,4,8,20,0;
q = 7, s = 7, 8: 4, 24 — identical to `data/bsE/fc5.txt`, `fc7.txt`. *Completeness of (B) against Lemma 1.1*
(`famcheck`): brute force over (L', j, γ, g', all monic E | D with E ≡ −1 (L'), T ∥ E + 1, monic E') for
q = 3, k = 2 (deg L' ≤ 3, j ≤ 5: 126 families), q = 3, k = 3 (deg L' ≤ 2, j ≤ 4: 46), q = 5, k = 2 (deg L' ≤ 2,
j ≤ 3: 16): every family maps to a tuple of 𝓕(s). So O173 Lemma 2.1's parametrisation is confirmed on data.

**Lemma 2.2 — SOUND.** Every step re-derived. (i) y + t ≤ max(a, b) — in fact = max(a, b), since lc(w + C) ∈ {1, 2} ≠ 0
(q odd). (ii) Choices: w monic, T | w: q^{a−1}; v: lc fixed, T² | v: q^{t−2} (×2 for the lc); L' monic T-free:
≤ q^{y+z}; (w, g'): q^{a−1+y}; (m', w): q^{a−1+z}. (iii) Reconstruction: route (R2) recovers w = (E+1)/L',
C = (E'+1)/L', m' = L'/g'; (R3) recovers C, L', m'; (R4) recovers L', g', C. (iv) Degrees for divisor counts:
deg D = s + 2y + z ≤ 3s, deg(g'T^s + w) = s + y ≤ 2s, deg(T^s + m'w²) = s (z + 2a ≤ s for a ≤ b). (v) The
minimum: t − 2 ≤ s − 3 − σ, least pairwise sum of (a−1, y, z) ≤ 2σ/3, min ≤ 2(s − 3)/5. Correct.
*q-independence of the constants:* δ(n) = max ∏(eᵢ + 1) over factorisation patterns with Σ eᵢ deg Pᵢ ≤ n, and
e + 1 ≤ 2^e gives δ(n) ≤ 2^n for every q; δ₃(n) = max ∏ C(eᵢ+2, 2) ≤ 3^n (C(e+2,2) ≤ 3^e). The bounds are used
only as multiplicities of the reconstruction step, never with a q-dependent degree, so B ≤ 16^s uniformly in q.
Correct. (2^n is attained only when T^s + v splits into distinct linear factors, which needs q ≥ n; for the
theorem this is irrelevant.)

**Lemma 2.3 — SOUND.** (A0)–(A4) re-derived line by line (E = a1'b1K − 1, F + b1 = a1'z, b1KF = T^α + z,
zE = T^α + b1²K, b1(a1'KF − 1) = T^α a1' + F). The z = 0 exclusion is correct (b1 = 1, F = −1, K = −T^α,
E + 1 = −T^α a1' = T·g'a1'·H forces α = 1, g' = 1, lc E = −1 ≠ 1 = lc s). Note T ∥ K (not only T | K): K = T·g'·H
with T ∤ H. Machine check: every Case A tuple found (below) satisfies (A0)–(A4), z ≠ 0, E, F, K monic,
f = α − β − κ.

**Lemma 2.4 — SOUND-AFTER-REPAIRS (m4, m5).** The bound is correct but two counting steps are under-justified:
the number of z with deg z ≤ f − λ (resp. β − λ) is q^{f−λ+1} in general, which exceeds the stated 2q^f when
λ = 0. It is rescued by T | z (z = b1KF − T^α and T | K), which gives q^{f−λ} — not stated. Also the parenthesis
ending the proof is garbled ("(Here δ(3α) ≤ δ(α)·… is absorbed is not needed: …"). Independent enumeration
(from the definition: a1', b1 monic T-free coprime, E monic divisor of T^α a1' + b1, E ≡ −1 (a1'b1), T ∥ E + 1,
g' | K/T): q = 3, α = 1..6: 0, 0, 2, 4, 10, 8 tuples (a1', b1, E) — identical to §4 — and 0, 0, 2, 8, 16, 16 tuples
(a1', b1, g', E); q = 5, α ≤ 4: 0. See m6 on the counting convention.

**Theorem 2.5 — SOUND (relative to the stated inputs; minor repairs m7–m9).**
*Logic.* (1) Every Case B family valid somewhere on the c-slice maps to a tuple of 𝓕(s), s = N + 1 + γ (O173 Lemma
2.1); its validity set on the slice is the cylinder u ≡ −E (mod T^{N+1}); γ ≤ j = N + 1 − k gives
N ≥ ⌈(s + k − 2)/2⌉ = N(s), so all families with the same tuple lie in the single cylinder of level N(s), of
relative mass q^{1−N(s)} (k = 2: q^{1−⌈s/2⌉}). This needs **only γ ≤ j**, not O173 Lemma 3.1 — the dependence on
Lemma 3.1 can be dropped (m7). (2) Case A: every family gives a tuple (a1', b1, g', E) of Lemma 2.4 (the derivation
of Lemma 2.3 uses only E | a1 + b1, E ≡ −1 (L'), T ∥ E + 1, lc), and its cylinder (mod T^{k+γ+α}) lies in the
γ = 0 cylinder, so the validity of the γ = 0 family is not even needed. (3) The bound sums over the tuples of
*all* c, which is a valid (if wasteful by ≈ q − 1) bound for each single c-slice. (4) Larger k only enlarges
N(s) and the Case A modulus; 𝓕(s) does not depend on k. (5) Uncovered set is closed (complement of a union of
clopen cylinders) of measure ≥ 1 − bound > 0; any point of it is in O(q, T^k), and O ≠ ∅ excludes a finite
covering by the ES2 §0.1 compactness criterion. No quantifier problem: the constants 16^s, 4·6^α do not depend
on q, and for each fixed q the series are summed over all s, α.
*Arithmetic.* Recomputed (`review_da_thm25.py`) with the *document's* stated constants B ≤ 16^s, B_A ≤ 4·6^α and the
exact pattern sets (not (s+1)^4), plus a rigorous geometric tail:
| r (q = 3^r) | Case B (s ≤ 100) | Case A | tail | total (mine) | author's total (route-wise constants) |
|---|---|---|---|---|---|
| 26 | 6.0e−3 | 9e−12 | ∞ (S=100) / 4.5e−3 (S=300) | **1.05e−2 (S = 300)** | — (not claimed) |
| 27 | 1.3e−3 | 3e−12 | 6.4e−3 | 7.7e−3 | 2.6e−2 |
| 28 | 4.0e−4 | 1e−12 | 5e−8 | 4.0e−4 | 1.9e−7 |
| 29 | 1.3e−4 | | | 1.3e−4 | 1.8e−11 |
| 33 | 1.6e−6 | | | 1.6e−6 | 2.0e−13 |
The author's totals for r ≥ 28 are much smaller than mine because `bsE_largeq.py` uses route-specific constants
(2·3^s, 2^{y+z}·2^{s+2y+z}, 2^{s+y}, 2^{max(s, z+2a)}) instead of the uniform 16^s stated in the text; I checked
those route constants and they are valid (δ evaluated at the actual degree). Either way the bound is < 1 for
all r ≥ 27, and the relative uncovered measure is ≥ 0.97 (mine: ≥ 0.992 at r = 27). Crude closed form: 0.171 at
q = 3^34 (claimed < 0.48 ✓), 0.200 at 1.3·10^16 (claimed < 1 ✓); it is in fact < 1 already for q > 1.37·10^15.
The dominant term is s = 8 with exponent −1 (16^8/q per pattern), so the decay is ≈ 1/3 per r, as observed.
By-product: with S = 300 the bound is < 1 also for r = 26 (m9).
*Consistency with O179 Thm 3.2.* O179 proves O(q, A) is Haar-null in R̂^*. The c-slice (x ≡ 1 at every prime
≠ T) is itself a Haar-null subset of R̂^*, so positive *slice* measure of O ∩ slice is consistent with O being null
in R̂^*. O179 §6 asks exactly for a count C·3^{(1/2−δ)K} on the slice, which is what Lemma 2.2 gives in exponent
form (δ = 1/10), with q-uniform constants. No contradiction.
*Inputs.* O173 Lemma 1.1 (Case A/B dichotomy and the cylinder description), O173 Lemma 2.1 (parametrisation (B);
confirmed on data above), R166 step (1) (Case A degree estimate: re-derived above, only uses E ≡ −1 − cT (T²)),
ES2 §0.1 (compactness). O173 is under parallel review (R173): **Theorem 2.5 inherits any defect found there in
Lemmas 1.1/2.1.** The label "PROVED, given …" is appropriate.

**By-product #{(c,f,g): cfg − c − f = n} ≪ n^{1/3+o(1)} — SOUND.** g ≤ n^{1/3}: (gc − 1)(gf − 1) = gn + 1. g > n^{1/3},
c ≤ f: f(cg − 2) ≤ cfg − c − f = n... precisely cfg = n + c + f ≤ n + 2f, so f(cg − 2) ≤ n and (cg ≥ 4 once
n ≥ 27) cf ≤ 2n/g < 2n^{2/3}, c ≤ √2·n^{1/3}; then f(gc − 1) = n + c gives ≤ τ(n + c) choices of g. Correct, and
elementary (the stated "cf ≤ 2n^{2/3}" needs the one-line justification above; m10).

## §3 (transfer to ℤ)

**Theorem 3.1 — SOUND (relative to the stated inputs; MINOR repairs m11–m13).** I checked the three steps of
Remark (5) and the measure argument independently.

*(i) MORDELL17 Lemmas 1.1, 2.1–2.3 for general r.* Re-read line by line with 17 ↦ r. The only arithmetic facts used
are: r odd (so the factor 4 sits in the r-free part, and the T-generic table of POINTWISE_MORDELL §2.1 is stated for
general T), the gcd conditions of I2/I3/II3 (which put r into exactly one modulus), and the algebra of Σ^I/Σ^II.
No step uses 17 ≡ 1 (mod 8/16) or any reciprocity at 17. Reciprocity enters only in Lemma 1.3 (√Q empty, odd
levels), which Thm 3.1 does not need, because √Q is simply counted: ≤ 2 roots per Q-datum, since r ∤ 4a²d for a
Q-datum (f = Fg ≡ −1 (mod 4ad)). The count 6f(r^k) = Q + Q⁻¹ + 2·√Q + U + U⁻¹ is right. Lemma 2.3's half-level
nesting (K = k + α, α ≤ K/2, union = level ⌈K/2⌉) is r-free. Cor 2.4 (no level-0 box) is r-free.
*Machine check (`scripts/review_da_rgen.py`, from scratch).* I read the seven classes literally off the statement
of ET Prop 1.9 (arXiv 1107.1010 p. 8) and imposed the r-generic condition: n = 1 modulo the r-free part of the
modulus, n = u modulo the r-part, and all square roots for I3. All parameters were ≤ 400. I compared the result
with a predicted superset built only from the objects the proof counts: −y/z, the roots of n² ≡ −y/z, −e and −1/e
(e = x/y + x/z) for ordered solutions (x, y, z) of 4/r^k, and −f, −f* mod r^{⌈K/2⌉} for N-points of Σ^II_{r^K}
(r ∤ cd, K ≤ 2k). For r ∈ {5, 7, 11, 13, 19, 23, 29, 31} at levels ≤ 2 there are **0 level-0 boxes and 0 brute-force
boxes outside the predicted superset** (46–132 boxes per r, all eight sub-types occurring). Controls: deleting
the Q/U part of the prediction leaves exactly the II2 / I2(r | f) / II3(r | e) boxes uncovered (the Q-types, 12 at
r = 13). Deleting the P part leaves nothing uncovered at these levels (r = 13, L = 150): the U-boxes and the P-boxes
found there lie in other predicted boxes. So the check is not vacuous, and the type assignment of Lemma 1.1 is confirmed for general r.

*(ii) ET's O(1/log log n) for N-points.* ET Lemma 2.8 (Type II part, p. 15) uses only a ≤ b, (2.2) ce = a + b and
(2.15) 4abcd = a + b + nc, so it holds for every N-point of Σ^II_n with y ≤ z. ET §3 (p. 18) then uses
(acde)² ≤ n², the fact that one of e, ad, ac, cd is ≤ n^{2/5}, and the divisor bound on (2.13), (2.19)–(2.21), whose
arguments are integers ≤ n^{O(1)}. All implied constants are absolute and effective (the divisor bound τ(m) ≤
m^{O(1/log log m)} is effective). So f_II^N(n) ≤ n^{2/5 + C/log log n} for n ≥ n₀, with absolute C and n₀. With
n = r^K: n^{C/log log n} = r^{CK/log log(r^K)} ≤ r^{CK/log log r}. Correct. (R83 m1 already made this point for
r = 17; it is r-uniform.)

*(iii) U-boxes ≤ f(r^k).* MORDELL17 Lemma 2.2 (U-datum ↦ the solution (iab, iac, ibc) of 4/F, box −(x/y + x/z))
is r-free. The box is a function of the ordered solution, so #U-boxes ≤ f(r^k). Correct.

*Browning–Elsholtz input.* The paper (Illinois J. Math. 55 (2011)) is not in `sources/`. I could only check ET's
quotation (p. 6: "[8] … gives the bound f(n) ≪_ε n^{2/3+ε} for all n and all ε > 0"). The *effectivity* of the
BE constant, which "effectively computable r₀" needs, is therefore unverified (m11). BE can be avoided. The Q, Q⁻¹
and √Q boxes come from N-points of Σ^I_{r^k} (MORDELL17 Lemma 2.1), and ET's §3 proof counts these by
n^{3/5+O(1/log log n)} (MORDELL17 §2 already uses this for D_Q). The U and U⁻¹ boxes that meet a non-residue cell
lie inside P-boxes: this is MORDELL17 Lemma 5.2, whose proof is r-free, and U⁻¹ is covered too because P is
inversion-closed. My r-generic brute force agrees: without the Q/U prediction no U-type box is left uncovered.
This gives the theorem with ET-only inputs, with margins 2/5 (Q) and 1/10 (P).

*Uniformity, measure, averaging.* S(r) ≤ 6C_ε Σ_k r^{−k(1/3−ε)} + 2Σ_K r^{−K(1/10 − C/log log r)}. Both series are
geometric with ratio → 0 as r → ∞, so S(r) → 0. There is no hidden r-dependence in the constants (C_ε and C are
absolute). Haar measure on ℤ_r has mass 1, the non-residue cells have total mass (r − 1)/(2r), and a level-k box
has mass r^{−k}. The union of boxes is open, so its complement in the non-residue cells is compact, with measure
≥ (r − 1)/(2r) − S(r) > 0 for r ≥ r₀, and every point of it is sterile. The "averaging over cells" is just this
subtraction. It is needed because the K = 1 P-boxes (≤ 2f_II^N(r) ≪ r^{2/5+o(1)} of them) are whole cells.
*Cor 4.2 for general r.* A finite union of classes is clopen. It misses {x ≡ u (mod r^L), x ≡ 1 (mod Q)} for some L,
and we may take 840·∏_{q<r} q | Q. Primes in that class satisfy p ≡ 1 (8), p ≡ 1 (3), (q/p) = (p/q) = 1 for odd
q < r (since p ≡ 1 (4)), (2/p) = 1 and (r/p) = (u/r) = −1. So their least QNR is r, and p ≡ 1 (24). Correct.
*Novelty/labels.* "PROVED relative to …" is the right label. The statement concerns finite ET-class coverings
only (Remark (4)), and the document says so.

## §4 (numerics)

**§4 EVIDENCE — SOUND (cross-validated).** Case B counts at q = 3 (s ≤ 14), q = 5 (s ≤ 9), q = 7 (s ≤ 8), and Case A
counts at q = 3 (α ≤ 6) and q = 5 (α ≤ 4), are reproduced exactly by my own enumerations, which take different routes
from the author's (§2 above). Union-bound masses: from my counts, Σ_s |𝓕(s)|·3^{1−⌈s/2⌉} = 3.48 for s ≤ 15 (using the
author's s = 15 count, 48), and divided by the q − 1 = 2 c-slices this is **1.74**, as stated. Case A: Σ 3^{−α}·#E = 0.176,
i.e. **0.088** per slice. The words "mean … of a c-slice" are what make these numbers right. Thm 2.5 instead bounds
each slice by the total over all c (see m6). The Case A ↔ Case B(α + 1) coincidence holds on my data *for the
(a1', b1, E) count*. With g' included (the tuples of Lemma 2.4) the Case A counts are 0, 0, 2, 8, 16, 16, and the
coincidence fails (m6).

## BRAINSTORM memos (bsE_*)

* bsE_sierpinski_moving_integer: still states "ℓ | N_s iff s ≡ −log_q p (mod ord_ℓ q)". The document's
  corrected form is log_q(−p^{−1}). It also still states "Witnesses at depth s need a factor ≥ q^s/2, i.e. a large
  prime factor of N_s". DEPTH_ASPECT §1.3 withdrew this (a large divisor need not have a large prime factor). And it
  says "failures … no congruence pattern beyond p ≡ 1 (24) dominance". In fact **all** 1233 q = 3 failures are
  ≡ 1 (mod 24) (my recount), so it is not just dominance. (m14)
* bsE_qpower_moduli_Z / AGENT_REPORT: "1233 of the 78496 primes ≤ 10⁶". π(10⁶) = 78498, and the 78496 are the
  primes 5 ≤ p ≤ 10⁶. (m2)
* bsE_large_q_char3, bsE_et_casework_depth, bsE_large_r_sterile: the claims match the deep file and are sound as
  reviewed above. bsE_padic_interpolation: "PROVED for the natural shapes" is correct in Lemma 1.3's repaired scope.
  bsE_depth_characters, bsE_q3_explicit_constants: Assessment only, no defects.
* AGENT_REPORT_O178, Results §1: "Lemma 1.3 (PROVED): exponential-polynomial / q-adically analytic witnesses". The
  "q-adically analytic" scope was withdrawn in the document (review repair). The report should match it. (m3)

## Defects

No FATAL. No MAJOR.

**MINOR**
* **m1** (§1.1, after the table). "So q = 2 is impossible" holds for the (I-t), (II-e) rows only. For the (I-cd),
  (II-cd) rows, c = 2^u, d = 2^v is unobstructed. Also, "for q ≡ 3 (mod 4) only odd s contribute" is for n ≡ 1 (4).
  *Repair:* "for the t- and e-rows, q = 2 is impossible …; for n ≡ 1 (mod 4) and q ≡ 3 (mod 4) only odd s contribute."
* **m2** (§0 (I1), §1.3, report, bsE_qpower memo). "1233 of the 78496 primes below 10⁶". *Repair:* "of the 78496
  primes 5 ≤ p ≤ 10⁶". Optionally add that all 1233 failures are ≡ 1 (mod 24).
* **m3** (AGENT_REPORT_O178 Results §1). It says "q-adically analytic witnesses". *Repair:* "witnesses affine in q^s"
  (Lemma 1.3's repaired scope). Lemma 1.3 could also add the Type II row (4abd = n + q^s; same proof).
* **m4** (Lemma 2.4 proof, both cases). The z-count "≤ 2q^f" (resp. "2q^{β−λ}") is false as written when λ = 0:
  polynomials of degree ≤ f − λ number q^{f−λ+1}. It is true because T | z (z = b1KF − T^α and T | K). *Repair:*
  insert "Since T | K, (A3) gives T | z, so z has ≤ q^{max(f,β)−λ} choices."
* **m5** (Lemma 2.4, last parenthesis). The sentence "(Here δ(3α) ≤ δ(α)·… is absorbed is not needed: …" is garbled.
  *Repair:* "(In the case f ≥ β, deg(T^α + b1²K) ≤ α because 2β + κ = α + β − f ≤ α, so δ(α) suffices for E.)"
* **m6** (§4 and bsE_caseAB_shift). The Case A "tuples" in §4 are triples (a1', b1, E), but Lemma 2.4 counts
  (a1', b1, g', E). The CONJECTURE #A(α) = #B(α + 1) holds only in the first convention (with g': 0, 0, 2, 8, 16, 16).
  Also, the §4 masses are per-slice means (total/(q − 1)), whereas Thm 2.5 uses totals. *Repair:* state the
  convention in §4 and in the memo.
* **m7** (Thm 2.5 hypotheses). The proof does not need O173 Lemma 3.1. γ ≤ j already gives N ≥ N(s), and nested
  cylinders then lie in the level-N(s) one. *Repair:* drop Lemma 3.1 from the list of inputs (this shrinks the
  dependence on R173), or keep it with "(only γ ≤ j is used)".
* **m8** (Thm 2.5 proof, arithmetic). The text states B = max(2δ₃(s), δ(s)δ(3s), δ(2s)) ≤ 16^s, while
  `bsE_largeq.py` uses route-specific constants with δ at the exact degree (2·3^s, 2^{y+z}·2^{s+2y+z}, 2^{s+y},
  2^{max(s, z+2a)}). These are valid, but the printed totals (1.9·10⁻⁷ at r = 28, < 2·10⁻¹¹ for r = 29..33) come from
  them, not from the stated constants. With the stated 16^s my totals are 7.7·10⁻³ (r = 27), 4.0·10⁻⁴ (r = 28),
  1.3·10⁻⁴ (r = 29), 1.6·10⁻⁶ (r = 33). These are still ≪ 1, so the theorem and "≥ 97 %" are unaffected. *Repair:*
  one sentence saying the script uses route-wise constants (δ at the actual degree), or quote both sets of numbers.
* **m9** (Thm 2.5 range, optional). With the exact pattern sums to S = 300 and the stated 16^s constants, the bound is
  1.05·10⁻² < 1 also at r = 26 (q = 3^26). The crude closed form is < 1 already for q > 1.37·10^15; the stated
  1.3·10^16 is correct but not sharp. *Optional repair:* r ≥ 26 (after an independent re-run), or leave it as is.
* **m10** (§2.1 Remark, by-product). "c ≤ f we have cf ≤ 2n^{2/3}" needs a line: cfg = n + c + f ≤ n + 2f gives
  f(cg − 2) ≤ n, and since cg ≥ 4 once n ≥ 27, cf ≤ 2n/g < 2n^{2/3}. *Repair:* add it.
* **m11** (Thm 3.1 inputs). "Effectively computable r₀" relies on the Browning–Elsholtz constant being effective,
  which was not verified (paper not in sources/). *Repair:* replace BE by ET-only inputs. Q/Q⁻¹/√Q are counted by ET
  §3 for N-points of Σ^I_{r^k} (n^{3/5+O(1/log log n)}). U/U⁻¹ boxes in non-residue cells are inside P-boxes
  (MORDELL17 Lemma 5.2, r-free proof; P is inversion-closed). Alternatively, check BE's paper for effectivity and cite
  it.
* **m12** (§3, intro paragraph). "MORDELL17 Lemmas 1.1, 2.1–2.3 (stated for r = 17; the proofs use only that r is an
  odd prime …)". This is confirmed. *Repair (clarity):* add "the √Q count uses r ∤ 4a²d (≤ 2 roots), which holds
  because f ≡ −1 (mod 4ad); Lemma 1.3 is not needed". Also cite this review's brute force (r ≤ 31, levels ≤ 2) as
  EVIDENCE for the general-r table.
* **m13** (§2 Thm 2.5 "What this does…" paragraph). "At q = 3 the same union bound is > 1 (§3)" should point to §4.
* **m14** (bsE_sierpinski_moving_integer). The memo was not updated with the §1.3 repairs (periodicity formula, the
  withdrawn large-prime-factor claim) and understates the mod-24 pattern. *Repair:* copy the corrected sentences from
  DEPTH_ASPECT §1.3.

## Scripts and data of this review
* `scripts/review_da_qpow.py q NMAX`: q-power ET families over ℤ, complete bounds derived independently (t < 9n²/2,
  e ≤ (n + 4)/3), exact rebuild. Logs `data/review_da/q3_1e6.txt`, `q7_1e6.txt`, `q7_2e5.txt`, `q11_2e4.txt`.
* `scripts/review_da_slices.py`: the slicing identities of table 1.1 on all Type I/II tuples of primes < 400.
* `scripts/review_da_ff.py caseB|caseA|famcheck`: own F_q[T] arithmetic. 𝓕(s) via factorisation of T^s + v, Case A from
  the definition, forward completeness of (B) against brute-force Lemma 1.1 families. Logs `data/review_da/ff*.txt`.
* `scripts/review_da_thm25.py [S]`: the Thm 2.5 union bound with the stated constants and exact pattern sets, plus a
  rigorous geometric tail. Logs `data/review_da/thm25_S100.txt`, `thm25_S300.txt`.
* `scripts/review_da_rgen.py r L KMAX`: r-generic boxes from the literal ET Prop 1.9 classes vs the Thm 3.1 box
  superset. Log `data/review_da/rgen.txt`.

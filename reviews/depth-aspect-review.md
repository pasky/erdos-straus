# R178 — hostile review of O178 DEPTH_ASPECT.md (reviewer 1 of 2, full document)

Reviewer branch: side-agent/review-depth-1 (merged side-agent/spark-depth-aspect at 0c6e57d2 basis).
From-scratch scripts: `scripts/review_da_*.py`; outputs `data/review_da/`.

## Summary verdicts

(filled in as the review proceeds)

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

## §4 (numerics)

## Defects

# R244 — hostile review of O235 (EXP_NEAR_SQUARE.md, memos z11_*, report AGENT_REPORT_O235)

Reviewer branch side-agent/review-exp-near (merged side-agent/exp-near-square at 3caecd49). From-scratch scripts:
`scripts/review_r244_*.py`. Work in progress — sections added claim by claim.

Merge note: the author's branch tracked `.pi/active.lock` (a per-agent lock file); untracked on the reviewer branch
(MINOR housekeeping, D0 below).

## Verdict summary
(filled in at the end)

## Claim-by-claim

### C1. Result 1.1 (binary core Π_ℓ{4, −2} of 4^s + 105 covered by 10 classes) — **SOUND** (certificate replayed from scratch)
`scripts/review_r244_cantor105.py` (no mordell_lib): every class is rebuilt from its ET Prop 1.9 parameters (Prop 1.9
statement checked in sources/elsholtz-tao-1107.1010.pdf, p. 7–8: II1 = "−e mod 4ab, e | a+b, (e,4ab) = 1", II2 =
"−4a²d mod f, 4ad | f+1"); the Type II identities were re-derived by hand and checked symbolically in sympy
(II1: n = 4abt − e, 4/n = 1/(abt) + 1/(n·m·b·t) + 1/(n·m·a·t), m = (a+b)/e; II2: n = ft − 4a²d, c = (f+1)/(4ad),
b = ct − a, 4abd − n = t, so 4/n = 1/(abd) + 1/(acdn) + 1/(bcdn)); D₁₉, D₄₁, D₁₉₁ come with explicit ES(q)
((5, 96, 9120), (11, 154, 6314), (48, 9169, 84061392)). Periods L_M = lcm ord_{q^e}(4) recomputed: supports
D₁₉ {3} (L = 9), II2 919 {3,17}, D₄₁ {2,5}, D₁₉₁ {5,19}, II1 35288 {2,5} (L = 100), II2 419 {11,19}, II2 1787 {19,47},
II2 27551 {19,29}, II1 32008 {2,5} (L = 500), II1 213384 {2,3,29} (L = 1044) — matching the document. 2-parts (8 | M for
the II1 classes) are compatible with ν₂ = 105. All 2⁸ patterns over S = {2,3,5,11,17,19,29,47} are covered (hence all
2¹⁵ over ℓ ≤ 47 and all of C). Each covering was additionally realised by a genuine integer exponent s (s ≡ σ_ℓ mod ℓ²⁰,
CRT) with n_s mod M computed directly, and for each class one actual member 4^s + 105 (up to 1401 bits) was solved
exactly. Remark (not a defect): the subcover is not minimal — II1 35288 receives 0 first hits when the classes are tried
in the listed order, so 9 classes suffice.

### C2. Lemma 1.2 (CRT of squares at label points) — **SOUND-AFTER-REPAIRS** (minor: proof gap at q | k, citation, one overclaim nearby)
Re-derivation. For odd q the q-component ν(μ)_q = 4^μ + k depends on μ only through μ mod ord_{q^e}(4) (mod q^e). If all
ℓ | ord_q(4) carry the exact integer label x, then μ ≡ x (mod ord_q(4)), so ν(σ) ≡ 4^x + k = s_x² (mod q) (s_x ∈ ℤ[1/2],
q ∤ num s_x), a non-zero square mod q, hence (Hensel, q odd) a unit square in ℤ_q — so only ord_q(4) matters, and the
clause "for every e with ord_{q^e}(4) supported on those ℓ" is not needed for the square conclusion (harmless). ν₂ = k =
105 ≡ 1 (mod 8). By CRT, ν(σ) ≡ m² (mod M) with gcd(m, M) = 1, m odd; such a primitive square class is not solvable by
polynomials (Mordell/Schinzel as quoted by ET p. 7), while every ET Prop 1.9 class is (ET Prop 1.9 converse) — exactly the
T1 argument of EXPONENT_COVERING Thm 1.2. Divisor classes D_q (q | M) need ν_q ≡ 0, impossible at a pure q. ✓
From-scratch checks (`scripts/review_r244_squares.py`): (i) the integer square points are *provably complete* (not only
"checked −6 ≤ x ≤ 40"): for x ≥ 0, (y − 2^x)(y + 2^x) = k; for x = −a, ((y−1)/2)((y+1)/2) = k·4^{a−1} with coprime
consecutive factors {d·4^{a−1}, k/d}. Results: 105 → {−2, 2, 3, 4}; 33 → {−2, 2, 4}; 273 → {2, 4} (4⁴ + 273 = 529 = 23² ✓,
also 4² + 273 = 17²); 297 → {3} — all match the document. (ii) D₁₉: μ ≡ 4 (9); D₄₁: μ ≡ 8 ≡ −2 (10) (μ₂, μ₅); D₁₁: μ ≡ 2 (5);
D₁₃: μ ≡ 3 (6) (μ₂, μ₃) — matches. (iii) Random test (20 000 (q, σ) pairs, q < 2·10⁴, labels {2, 3, 4, −2}): at every pure q,
ν(σ) ≡ s_x² (mod q) and is a non-zero QR. No counterexample.
Defects: D2 (q | k not covered by the proof), D3 (citation), D4 ("true mixed-point set = C₄" overclaim).

### C3. Lemma 3.1 (unit-square point ⟺ c₀ + k = 4^j) and "no finite ET/divisor covering" — **SOUND-AFTER-REPAIRS**
Re-derivation. ν(x) (x ∈ ℤ) has odd components the rational N = c₀4^x + k; N ∈ (ℤ_q^×)² for all odd q ⟺ N is a square
of ±2^j (j ∈ ℤ) — a rational that is a square in ℚ_q for almost all q is a square, and the unit condition kills odd
primes. 2-component: ν₂ = k (limit of c₀4^s + k, s → ∞ 2-adically… i.e. s → ∞ in ℕ), so additionally **k ≡ 1 (mod 8)** is
needed (D5). Case analysis: c₀ odd — x > 0 gives N odd > 1; x = −a < 0 gives c₀ + k·4^a odd > 1; so x = 0, c₀ + k = 4^j ✓.
c₀ ≡ 2 (mod 4) — x ≥ 0: N odd > 1; x < 0: c₀ + k4^a ≡ 2 (mod 4) ✓ impossible. **c₀ ≡ 0 (mod 4) is not treated and the
stated equivalence is false there**: c₀ = 4c₁ gives a unit-square point at x = −1 iff c₁ + k = 4^j. Brute force
(`review_r244_squares.py l31`, c₀ < 130, k < 1100, k ≡ 1 (8), x ∈ [−12, 40)): the document's criterion fails in exactly 20
cases, all with 4 | c₀: (12, 1), (28, 9), (28, 57), (48, 1), (60, 1), (92, 41), … (e.g. 12·4^s + 1 = 3·4^{s+1} + 1). D5.
Lists: 7 + 9 = 15 + 1 = 16, 23 + 41 = 31 + 33 = 7 + 57 = 64 ✓, all k ≡ 1 (8) ✓; j ≥ 2, k ≡ 1 (8) ⟹ c₀ ≡ 7 (8) ✓;
j = 1 ⟹ (3, 1) ✓; c₀ + k ≡ 1 (3) automatic ✓.
"No finite covering" — what exactly is proved. EXPONENT_COVERING **Cor 1.5 does not apply** (it is stated only for
k·2^m + 1, b = 2, c = +1); (3, 1) and (15, 1) are the even-m subfamilies of Cor 1.5's k = 3, 15 (a sub-family of an
uncoverable family is *not* automatically uncoverable, but here the obstruction point m = 0 is even, so it persists).
The author correctly cites Thm 1.4 + Remark 1.3 instead: the proof of Thm 1.2/1.4 uses only that n_s mod M is
eventually periodic, ν is continuous on Ẑ and n_{s_j} → ν(μ) for s_j → ∞, s_j → μ — all true for c₀4^s + k (s_j → 0 in
Ẑ, s_j → ∞ gives n_{s_j} → (k at 2; c₀ + k = 4^j at odd q)). Excluded class types: precisely finite unions of ET
Prop 1.9 classes and divisor classes D_d (d odd > 1), covering {n_s : s ≥ s₀} for any s₀ — and in fact more: every
non-primitive class (ν(0) is a unit mod every odd M) and every primitive class solvable by polynomials (the class of ν(0)
mod M is a primitive odd-square class, not polynomial-solvable by Mordell/Schinzel as quoted in ET p. 7). It does NOT
exclude coverings using other sufficient conditions (e.g. classes with ES proved for each member by a non-polynomial
argument), and of course says nothing about ES for these n_s. With these scope words the claim is PROVED (relative to
the reviewed Thm 1.4 and ET's quotation of Mordell/Schinzel, which I could not access directly).

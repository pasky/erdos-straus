# STERILE_EXPLICIT (O219) — independent hostile review #2 (R223)

Reviewer: R223 (side agent, branch side-agent/review-sterile-explicit-2). Round 1, document not edited.
Scope: STERILE_EXPLICIT.md as merged from side-agent/sterile-explicit; scripts se_box.c, se_tail.py, se_r0.py;
data/se/*. From-scratch scripts: scripts/review_se2_*.py. The parallel review (R222) was NOT read before writing this.

## Summary verdicts (filled in progressively)

(in progress)

## A. The reduction Theorem 3.4 → (S) → finite certificate (task focus (a))

**A.1 Sterility ⇐ (S).** I re-derived the chain for a general odd prime r:
* Box types: M17 Lemma 1.1 (general r: R187's re-derivation + brute force r ≤ 23 from the literal Prop 1.9 classes; I did
  not redo the literal-class brute force). Level-0 boxes are impossible (M17 Cor 2.4, r-free: 4/1 has no solution).
* M17 Lemma 1.3 is **used** here (√Q = ∅; Q only at odd k; P only at odd K; this is what lets (S) carry 2D_Q instead of the
  6f(r^k) of DEPTH_ASPECT §3, which explicitly says "Lemma 1.3 is not used"). I re-derived it for general r: the proof uses
  only Jacobi symbols at f and g ((−1/f) = −1, (d/f) = 1 from f ≡ −1 (mod 4d), (−d/g) = 1 from g | 4a²d + 1, hence
  (−d/r)^k = −1; for P, (r^K/f) = −1). r-free. ✓
* M17 Lemma 5.1 (Q-box ≡ −a/b, P-box ≡ −a/b) and its in-cell consequences: for Q, r ∤ a, b, d always (4abd ≡ 1 mod F),
  r | c ⇒ box ≡ 1·(residue) (since a ≡ −b); for P with r ∤ cd, r | b ⇔ r | a and then −f ≡ −f' ≡ 1. Hence restricting D_P to
  r ∤ ab and D_Q to r ∤ abcde loses nothing **in the non-residue cells**. r-free. ✓
* U ⊂ P (M17 Lemma 5.2): both cases r-free (α > β: reduction to a Σ^II_{r^{α−β}} point (b', c', a', i) with r ∤ a'i; the P-box of
  level ⌈(α−β)/2⌉ = (K'+1)/2 is one of the two boxes counted for the ordered datum or its reflection; α = β impossible since
  4i ≤ 3). ✓ Q⁻¹ = Q as sets (reflection a ↔ b). ✓
* Weights: P-datum boxes of level (K+1)/2 (M17 Lemma 2.3: every (P)-datum box of level k lies in the box of its Σ^II point at level
  ⌈K/2⌉ ≤ k), Q-boxes of level k; Haar measure r^{−level}; non-residue cells have measure (r−1)/(2r). Total box measure < cell
  measure ⇒ a non-residue u in no box (positive measure of such u). Cor 4.2 for general r: the neighbourhood class
  {x ≡ u (r^L), x ≡ 1 (Q)} with 8·3·∏_{q<r} q | Q is primitive, contains infinitely many primes, all with least QNR exactly r
  (QR mod every q < r incl. 2 via p ≡ 1 (8); x_r ≡ u non-residue). ✓
* From-scratch brute force (`scripts/review_se2_identities.py`, all P-data for r^K ≤ 2·10⁶ and all Σ^I_F points for F = r^k ≤ 6000,
  13 primes 3 ≤ r ≤ 43): Lemma 1.1 (i)–(iv), Lemma 1.2 sizes, the Q identities, f ≤ F + 2, ≤ 2 Q-points per (a, d) (M17C 2.1(iv)),
  the three f-route congruences of §3.2, 4a, 4c, 4d | f + F, P-data only at odd K and Q-data only at odd k (in fact *no* data at all
  at even exponents), every in-cell Q-box a non-residue, the −a/b centres, and the in-cell exclusions: **0 failures**; it reproduces
  D_P(17³) = 32, D_P(17⁵) = 121, D_Q(17³) = 73 (M17).
Verdict A.1: **SOUND** (relative to M17 Lemma 1.1 for general r, which rests on R187).

**A.2 Quantifier "for every prime r ≥ 2³²".** How infinitely many r are covered (`se_r0.py`, re-read line by line):
1. r ∈ [2^b, 2^{b+1/4}), b = 32, 32.25, …, 600 (2273 ranges). For each odd K the term 2D_P(r^K)r^{−(K+1)/2} is bounded by
   (max over the table cells covering N ∈ [2^{Kb}, 2^{K(b+1/4)})) × 2·2^{−b(K+1)/2}: the tables bound D_P(N) for **every** integer N in
   a cell (se_box takes the box bounds at the cell's N-enclosure, and nothing in se_box depends on r), and the weight is maximal at
   the bottom of the r-range. Same for Q with weight 2·2^{−bk}. ✓
2. For N ≥ 2^{600} (P) resp. 2^{100} (Q) the tail term lists Σ c N^e (ln N)^p (all e ≥ 0, p ≥ 0 after the m1 capping, hence
   nondecreasing in N) are evaluated at the top N of the range. Cells straddling 2^{600} take max(table, tail). ✓
3. r ≥ 2^{600.25}: every N = r^K is in the tail, and d/d(ln r) of r^{Ke−(K+1)/2}(K ln r)^p is ≤ 0 iff p ≤ ((K+1)/(2K) − e)·ln N; the
   checked condition p ≤ (1/2 − e)·600 ln 2 implies it for all K ≥ 1, N ≥ 2^{600}. Likewise for Q (p ≤ (1 − e)·100 ln 2). So each term
   of S(r) is ≤ its value at b = 600, while (r−1)/(2r) increases. ✓
4. The per-range series in K: the loop stops when a tail term is < 10^{−30} and adds 10^{−20} "geometric remainder" without proof.
   True (successive odd-K tail terms decay by a factor ≤ 2^{2(b+1/4)·0.4797 − b}·((K+2)/K)^{p} ≤ 0.7 for b ≥ 32), but unstated: minor m-A1.
Verdict A.2: **SOUND** (minor m-A1). The quantifier is handled by a finite grid in log r plus a monotone tail, not by scaling.

**A.3 What the certificate actually depends on numerically at r ≈ 2³²** (decomposition with the author's own tables/tails,
`/tmp`-free recomputation in §C): S(b = 32) = 0.486702 = Q(k=1) 0.35044 + P tail (K ≥ 19, N ≥ 2^{600}) 0.10932 [of which K = 19 alone
0.0924, K = 21 0.0143] + P(K=1) 0.02460 + P(K=3) 0.00232 + P(K=5..17) 3·10⁻⁵ + Q(k≥3) 1.4·10⁻⁸. Margin to 1/2: 0.0133.
Remark (not a defect): the tail is extremely lossy against the tables — the *table* term at K = 17 (N ≈ 2^{544}) is < 10⁻⁶ while the
*tail* term at K = 19 is 0.092. Extending P_q1 to 2^{700} would remove ≈ 0.1 from S and is the cheapest way to lower r₀.

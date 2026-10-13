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

## §3 (transfer to ℤ)

## §4 (numerics)

## Defects

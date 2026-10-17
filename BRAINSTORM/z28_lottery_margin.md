# z28_lottery_margin — model exceptions sit where the expected count is O(1) (O257; NONCONG_LIFTS §2.1–2.3)

**Idea.** Use exact E_k (k = 7…25, primes ≤ 10⁸, `scripts/z28_lab.c`, 30 s) to ask whether model exceptions are
structural or a thin-lottery phenomenon, and what that means for "screening" k = 4 laws.
**Results.** E_k lists agree with O194/O197 and Pomerance–Weingartner Table 1 (known data). Large exceptions are squares
mod k with highly divisible p − 1 and large least non-residue (e.g. 20/2763601: non-residue primes ≤ 29 only {19, 29}).
Mean f_k(p)/log³p at p ≈ 3·10⁴: 0.159, 0.072, 0.043, 0.030, 0.025, 0.019 (k = 4, 8, …, 24); minimum f: 23 (k = 4), 4 (k = 8),
0–1 (k ≥ 12).
**Literature.** Pomerance–Weingartner, Ramanujan J. 69 (2026) / arXiv:2511.16817 (Table 1); MODEL_SPECIFIC §1, §5 (count law,
"luck" of m = 4); TES_FINITE (O194).
**Barrier screen.** (J)41/R207 D1, R266 D-41: model failures refute only threshold-free k-uniform laws; a law valid for
p > P₀(k) (Schinzel's conjecture is one) is untouched. Every lift law of O253/O257 is threshold-free, so the screen
applies to them.
**Cheap numerics.** `logs/z28_Ek_primes_1e8.txt`; counts via `z28_lab cnts`.
**Assessment.** EVIDENCE. The numerical 4-specificity is a factor ≈ 2 in the mean and ≈ 6 in the minimum at 3·10⁴ — a
margin, not a mechanism; the proved 4-specific mechanism of this relay is Thm 2.6 (z28_complete_levels).

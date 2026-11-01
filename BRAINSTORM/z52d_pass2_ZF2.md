# z52d Pass 2 — batch ZF2 (12 §1 items that Pass 1 `skipped`)

1. Counts: nothing 11, covered 1 (Z1432 → `BRAINSTORM/z45_etale_descent.md` §0, Props 1–5), interesting 0, needs-compute 0, skipped 0.
2. Premise failures: Z0569 (Graham 1964 has no "finite exception list": distinct reciprocal squares give exactly [0, π²/6−1) ∪ [1, π²/6); for 4/n the exceptions are n ∈ {1,2,5,6}); Z0326 (ES(n) is Δ₀, so MRDP is needed only for the failure set).
3. Reusable numbers: the (★) word set {4uBC−u−B} has 1 154 non-square odd gaps ≤ 10⁹ (+63 in (10⁹,4·10⁹]); per-decade counts fall after 10⁷ (299, 229, 145); every finite set of (u,B) pairs misses p ≡ 1 mod lcm(4uB) (Z1018/Z0506). Fixed-quadratic-field (★) certificates cover only ≈ X^{1/2} primes (Z0419).
4. Elementary PROVED by-products: (★)(n) ⟺ ∃u,m: 4u | m+1 ∧ m | n+u (Presburger + divisibility, Z1472); the divisor involution makes every level-row label word a palindrome, so Sperner parity is always even (Z1897); bounded NS degree of the integer (★) encoding is deg ML(1/P)+3 and comes out maximal everywhere (Z2795).
5. Outcomes: `data/z52b/pass2/outcome_ZF2.jsonl` (lint: 0 flagged); scripts `scripts/z52d_p2_ZF2_*`; data `data/z52b/pass2/ZF2/`.

## Reproduction (all under `timeout`, `ulimit -v 8000000`)
* Z1018 gap census: `gcc -O2 scripts/z52d_p2_ZF2_Z1018_conductor.c -lm -o c && ./c 1000000000` (3 min, 1 GB) → `Z1018_gaps_1e9.txt`;
  `scripts/z52d_p2_ZF2_Z1018_gapbits.c 4000000000 1000000000` (~10 min, 250 MB) → `Z1018_gaps_1e9_4e9.txt`.
* Z2795: `uv run --with numpy python scripts/z52d_p2_ZF2_Z2795_nsdeg.py k p…` (k ≤ 7: 2²¹ cube points).
* Z0419: `uv run --with sympy python scripts/z52d_p2_ZF2_Z0419_fixedfield.py X` for X = 10⁶, 10⁷, 10⁸.
* Z1472: `… scripts/z52d_p2_ZF2_Z1472_linear.py 20001 3001`; Z1897: `… scripts/z52d_p2_ZF2_Z1897_sperner.py 20000 40`;
  Z0326: `… scripts/z52d_p2_ZF2_Z0326_mrdp.py 150`.

## Notes per item (terse; full records in the outcome file)
* **Z1018** gap set of S = odd squares (T1) ∪ 1 154 non-squares ≤ 10⁹ (14 primes ≡ 1 (4) = FRONTIER §2.1 list; 10 primes ≡ 3 (4), last 6 266 527); no conductor for any finite level set; S is not a semigroup.
* **Z1897** the row word of labels (A: d ≡ 1, B: d ≡ −1, O: other mod 4C) over the sorted divisors of 4Cp+1 is a palindrome (d ↔ N/d inverts classes), so #fully-labelled cells is always even; checked for 1 125 primes < 2·10⁴ × 40 levels.
* **Z0419** McMullen's trick = Lucas-sequence determinants f_{2m} (Prop 2.1/Thm 2.2); certificate trace field is Q(√(C(Cw²+p))).

# z9_order3_fano — is there a "Q mod 3 on L/√−3 L" pigeonhole for TES? No: the cubic symbol does not control λ-adic divisibility (O233, goal 3)

## Idea
O224 Thm 1.3: for ES the numerator 4 sits exactly at the character level. The 2-adic Hasse invariant χ(w) = −1 forces
4 | (some pentagon entry), with zero further bits, and 2^k costs one fair bit per extra level. The analogue for TES
(TWISTED_T1 §3: 9/n = ω/x + ω²/y + 2/z over O = ℤ[ω], 2-primary denominators, anchor 2, partner λ = 1 − ω, 9 = unit·λ⁴)
would be a word family with a cubic character χ₃ such that χ₃ = target forces λ⁴ | (some entry). If so, the 16 certified
non-BM failures of TES (TES_FINITE Thm 2.1) would have to be primes with no target-χ₃ word, a sharp test.

**Word family (Type II, c = 1 shape, the analogue of ES's slice T).** For an assignment (i, j, k) of c = (ω, ω², 2), put
`c_i π + c_j v + c_k u = T u v`, (T, u, v) ∈ O³, T ≠ 0. This gives the point `T/π = c_i/(uv) + c_j/(πu) + c_k/(πv)`, the
analogue of ES's t/n = 1/(uv) + 1/(un) + 1/(vn) for tuv − u − v = n. It is a TES solution iff 9 | T and the denominators
(T/9)·x_m are 2-primary. The set is finite (|u| or |v| ≤ (3 + √(9 + 4|π|))/2). χ₃(w) := inv_π of TWISTED_T1's α at the word
point (tame cubic symbol, `tw_eis.tame_symbol`). Thm 3.2(c) forces χ₃ = 2 on every solution, and the computation confirms
this on all solutions found (calibration).
**Missing analogue of the pentagon.** In ES one word carries five numerators (t, u, v, A, A*) because the coefficients are
equal (frieze symmetry). With c = (ω, ω², 2), the Type I numerator coming from A = Tu − c_j satisfies
A/(c_kπ) = c_j/(A*π) + (c_i/c_k)/v + c_i/(A*v). Its coefficient triple (c_j, c_i/c_k, c_i) is not the TES triple. So a TES
word carries a single TES numerator T, and there is nothing for a pigeonhole to choose between.

## Literature
TWISTED_T1 Thm 3.2 (order-3 T1, cubic reciprocity); TES_FINITE Thm 2.1/3.1 (16 certified failures, not Brauer–Manin);
FOUR_ADIC_INPUT Thm 1.3, Prop 1.4 (Fano pigeonhole, 2^k bit law); Gross–Lucianovic (ternary forms ⟷ quaternion orders).
There is no cubic counterpart: orders in degree-3 central simple algebras are not even Clifford algebras of ternary forms
(Haile–Knus–Rost–Tignol on generalised Clifford algebras of binary cubic forms give cyclic algebras, but not with the
orthogonal-group / Fano structure used here).

## Barrier screen
The ES Fano mechanism needs (i) a quadratic form whose 2-adic invariant is the character (CHI_FLIP), (ii) frieze parity
(two even entries out of five) and (iii) the "exactly two isotropic points on a 3-point line" count. (i) is quadratic in
nature. A cubic Hilbert symbol has no quadratic form behind it, so there is no "Q mod λ² on L/λL". (ii) fails because
the coefficients are unequal (above). T1₃ (cubes) is unaffected: it is a reciprocity statement, not a pigeonhole.

## Cheap numerics (EVIDENCE; `scripts/z9_tes_words.py`, `scripts/z9_tes_agg.py 800`, `data/z9/tes_words_800.txt`)
Covers all 67 split primes 7 ≤ N(π) ≤ 787 (2-primary π), 13 of them TES failures.
* χ₃ takes all three values. The classes 1 and 2 have identical statistics (an involution exchanges them), and 0 is
  slightly different. **P(v_λ(T) ≥ k | χ₃)** for k = 1..4: χ₃ = 2: 0.257, 0.062, 0.013, 0.003; χ₃ = 0: 0.227, 0.053, 0.011,
  0.0016. So the λ-adic valuation of T is essentially independent of χ₃. Each further λ costs a factor 4–5, as for a fair
  draw with slight bias, and χ₃ = target does **not** force λ⁴ | T (in ES, χ = −1 forces 4 | entry with probability 1).
* At every one of the 13 failure primes there are 428–1368 words with χ₃ = target. At 7 of them (61, 79, 97, 151, 211, 367,
  769) some target words even have λ⁴ | T; these fail only at the 2-primary normalisation of the anchor. So **the TES
  failures are not "no target-character word" failures**: they are bit failures (λ-adic and anchor levels), the
  analogue of 8/131, 8/241, not of an ES-five failure.
* The slice is a strict sub-lottery: 26 of the 54 solvable primes have no solution in this shape (they are solved by other shapes).

## Assessment
Negative, with a structural reading (Assessment): TES's numerator 9 = λ⁴ lies several "trits" above its character level.
ES's numerator 4 lies exactly at it (zero bits, O224). That is a coherent explanation of why TES has certified failures at
primes (16 below 30 000) while ES-five has none to 10⁸. It also sharpens O224's requirement (ii): a proof of ES-five must
use the zero-bit property of 4, which TES lacks. EVIDENCE (one Type II slice; Type I words and the other shapes not
enumerated). Promise for an existence mechanism: 0/5; as an explanation of the TES/ES contrast: 2/5.

# y4_seven_control — 7/n: the T1-bearing, failure-free sibling with none of 4's structure (O212, goal (c))

## Idea
y4_t1_numerators: the numerators whose shot family has T1 are exactly M ≡ 0, 3 (mod 4). Among them only 3 (trivially),
4 and 7 have no failing prime ≤ 10⁸ (MODEL_SPECIFIC census). So 7 is the natural control for any proposed
"4-specific reason why ES never fails": if 7 never fails *without* that structure, the structure is not what makes a
numerator failure-free. (It can still be what a *proof* of ES uses.)

## Facts about 7 (each checked)
* T1 in the 7-shot family, for all g (2 splits in ℚ(√−7)): PROVED (y4_t1_numerators Cor 2(b)); 0 shots at odd squares.
* Odd squares ≤ 10⁸ are all solvable for m = 7 (MODEL_SPECIFIC §1, other-shape solutions). Same as 4.
* No length-3 character fibre: S₇ contains χ = +1 members and non-members ((J)32 Thm 3.1(c)); S₇(p) = ∅ at 10 primes
  ≤ 10⁵ (last 12601), while 7/p is solvable there. **New check** (`scripts/y4_seven.py 601`, 9905 words): membership in
  S₇ is NOT a function of (n mod 56, (A/n), (A*/n), (t/n), (u/n), (v/n)); 282 of 386 feature classes are mixed. So
  no simple Jacobi refinement of χ makes S₇ a fibre.
* Prop 1 of y4_catalogue fails for 7: the e ∈ {1, 3} slices cover only p ≡ 2, 4, 6 (mod 7); for p ≡ 1, 3, 5 (mod 7)
  there are still {±1}-unit-group slices (e = 6, 2, 2), so 7 shares the broader {±1} reading (R-O212 repair).
* Type I alone never fails for 7 (all primes ≤ 10⁶); Type II alone fails at 3, 31, 43, 127, 211, 421, 463, 631, 12601
  (`ms_census 7 10⁶ p −1 {1,2}`). For 4 both never fail; for 8 Type I fails exactly at the true failures.
* Mean count: m·mean f_m/(4·mean f_4) = 1.09 for m = 7 (MODEL_SPECIFIC §5.1), so mean f_7 ≈ 0.62·mean f_4, against
  ≈ 0.45 for 8 and ≈ 0.37 for 11 (which fails at 37; 3 is trivial).

## Literature
MODEL_SPECIFIC (O197) §§1, 3, 5; Pomerance–Weingartner Table 1 (row m = 7: no failure in their range).
Schinzel's conjecture for m/n and Sierpiński's 5/n are open; 7/n is not known for all n either (to my knowledge).

## Barrier screen
This is a control, not a mechanism. Numerator harness: SQ₅ and Prop 1 pass for 4 and have no 7-analogue; the shot,
T1 and relaxation layers are shared by 4, 7 and 8.

## Assessment (EVIDENCE + Assessment)
7/n is failure-free to 10⁸ without a character-fibre slice structure, without an e ≤ 3 slice at every prime, and with T1.
So 4's structural specialties (χ-fibre, Prop 1, Mordell witnesses) are **not necessary** for a failure-free record:
the record is consistent with count size (MODEL_SPECIFIC §5.3) for both. This sharpens the reading of O208's barrier:
the needed "4-specific input" is a requirement on a **proof**, and the χ-fibre is the only known candidate with a
proof shape. It is not an explanation of the numerics. A proof of 7/n (open) would need its own input that is false
for 8 and 11. No candidate is known.

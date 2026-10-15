# z1_square_numerator — "4 = 2² is a square" (brief angle 3): dead, and what survives (O224)

## Idea
Exploit that 4 is a perfect square, 2-adically and archimedeanly (4/p = (2/√p)²; Q mod 4 versus Q mod 8 = 2·4), in contrast
to 8 = 2·□, 11, ….

## Literature
MODEL_SPECIFIC §1 census (complete failure lists, primes ≤ 10⁸, m ≤ 24; agrees with Pomerance–Weingartner Table 1);
FOUR_SPECIFIC Prop 1.1 (shot-T1 for M ≡ 0, 3 mod 4).

## Screen
* Squares fail: 9/p fails at 3 primes ≤ 10⁸ (last 19), and 16/p at 37 (last 83449) (`data/ms/prime_fail_1e8.txt`).
  So "numerator is a square" cannot be the input. Full T1 holds for 16 (every 4 | M, (J)49) and fails for 9.
* 2-adic squares: 4·(odd square) and 4·u² for 2-adic units u give 36/p (36 ≡ 4·9) and 4·17 = 68 (17 ≡ 1 mod 8, a 2-adic
  square times 4). Both contain 4 | M, so S_M ⊊ χ-fibre (MODEL_SPECIFIC Thm 3.1(b)) and they inherit the depth bits of
  their 2-part only when 8 | M. For 4·odd the extra cost is the odd factor (3-adic or ℓ-adic slices, not forced:
  z1_small_prime_pigeonhole). 12/p and 20/p fail (20 at 2763601).
* What survives is not squareness but the **exponent** v₂(M) = 2 together with odd part 1: the isotropy test of an odd
  unimodular ternary ℤ₂-lattice lives exactly at Q mod 4 (FOUR_ADIC_INPUT §1). Q mod 2^k for k ≥ 3 lives on L/2^{k−1}L and
  costs bits (z1_depth_bits).

## Barrier screen
T1: 16 and 36 have T1 and still fail, so T1 + squareness is not enough (B7-type siblings). B1: unchanged.

## Cheap numerics
Data reuse only (`data/ms/prime_fail_1e8.txt`). No new script.

## Assessment
Angle 3 is dead as stated (refuted by 9/p and 16/p). Its correct residue is the v₂ = 2 statement of FOUR_ADIC_INPUT §1, which
explains the target and does not prove existence. Promise 0/5.

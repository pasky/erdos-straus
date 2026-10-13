# bsE_qpower_moduli_Z — ET moduli restricted to powers of one prime q (O178)

## Idea
Use depth-aspect technology (character sums mod q^s beat Burgess: Postnikov, Iwaniec, Milićević) by restricting the moduli
of the ET slices to powers of a fixed prime. Type I with t = q^s: the integer N_s = (q^s p + 1)/4 moves with the modulus.
Type II with e = q^s: N = (p + q^s)/4. (c, d) slices: p² + 4q^{2u+v}, 4q^{2u+v}p + 1 (DEPTH_ASPECT §1.1 table).
## Literature
Elsholtz–Tao, arXiv:1107.1010, Props 2.3/2.7; Postnikov (1956, characters mod p^n via the p-adic logarithm);
Iwaniec, Acta Arith. 24 (1974); Milićević, Compositio 152 (2016) (sub-Weyl in the depth aspect).
## Barrier screen
Parity: q = 2 is impossible, and q ≡ 1 (4) never helps p ≡ 1 (4). For q ≡ 3 (4) only odd s contribute. B2: the mass per
modulus is ≍ log²p/q^s, so the family is a fixed finite slice set (s = O(1)) plus a geometrically small tail. It therefore fails
i.o. under a uniform Hardy–Littlewood heuristic (CONJECTURE), and the fixed part fails i.o. under H. B3/B6: depth tools need
intervals, and the divisors of one integer are not one. T1: trivially respected.
## Cheap numerics (`scripts/bsE_qpow.c`, checker `scripts/bsE_qpow_check.py`)
q = 3: 1233 of the 78496 primes ≤ 10⁶ have no solution in the family (first 241, 409, 769, …). q = 7: 3518. Odd squares: all empty
(T1 control). The mean count per s decays by ≈ 1/3 per step.
## Assessment
COLLAPSES (B2), with explicit counterexamples. The depth aspect matters only where the problem is *forced* to a
prime power. That happens at r-generic / slice points (DEPTH_ASPECT §§2–3).

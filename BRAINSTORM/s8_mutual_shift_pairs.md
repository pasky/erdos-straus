# s8_mutual_shift_pairs — Type II as mutual shift pairs with a 2-adic quotient (O258; SYNTHESIS_SPARKS8 §1)

**Idea.** Write every Type II solution as a pair (x, y) with x | cn + y, y | cn + x and quotient N = (cn + x + y)/(xy) ≡ 0 (mod 4c).
The c = 1 line is "some pair of MP(p) has 4 | N". The b = 1 line, after the duality of Prop 1.3, is "some pair of MP(p) has a
coordinate ≡ 0 (4)". So the two lines are the two 2-adic faces of one set MP(p).
**Literature.** ET (Elsholtz–Tao 2013) Type II parametrisation; LATTICE_MEETING (d = 1 line); PARITY_AUDIT (★) = c = 1 line.
**Barrier screen.** A pure reparametrisation, so B1–B6 apply unchanged. T1: every pair of MP(m²) has v₂(x) ≤ 1 and v₂(N) ≤ 1
on its even coordinate (by ET Prop 1.6). The piecewise-linear structure of y ↦ −p mod y returns ET's window form (Prop 1.4): B2.
**Cheap numerics.** `scripts/s8_mp_check.py 1500`: MP(n) by brute force against the (x, s) parametrisation and both line
criteria; 122 n (primes, odd squares, 105), 0 mismatches.
**Assessment.** PROVED dictionary (Props 1.2–1.4). It is useful as a 2-adic organisation of the lines (spark 2 of §7), not as
an existence mechanism.

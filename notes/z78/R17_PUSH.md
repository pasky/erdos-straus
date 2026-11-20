Result: Every nonsquare cylinder meets P-centres of arbitrarily high level, and a geometric tail allowance applies down to r=17. Label: PROVED (rel. ZL Lemma 1.2 and the PL §4 log powers)
Scope: The limit set of centres is not the precisely weighted covering; no conclusion of sterility at 17 or on integer ES.
Review: none (checkpoint)
Triage: DATA
STATUS delta: none yet

## 1. Tail (PROVED relative to the z76 inputs)

The logarithmic derivatives with respect to log N of the individual positive normalized terms, from the first actual exponent beyond the respective 800- and 100-bit boundaries, are at most −.02+2/(800 log 2)<−1/64 and −.24+2/(100 log 2)<−1/5. Thus for r≥17 each step of two exponents multiplies a term by at most 2^(−1/8)<12/13 in P, and 2^(−8/5)<1/3 in Q. Here use r>16 and compare integer powers. Starting with .014 and .000010 as in PL §4, the combined oriented mass is ≤ .364/floor(sqrt(r))+.000030. For r≥4096 the old PL allowance may also be used; both are upper bounds, not measurements. The use of log derivatives is termwise in the dominating sums, not on the irregular datum counts themselves.

## 2. The limit set at 17 (and at every odd prime)

**PROVED (relative to Dirichlet's theorem).** For any odd prime r, every nonsquare cylinder u mod r^j contains P-centres of unbounded level, already with a=c=1. Take a prime ℓ≡−u mod r^j, ℓ≡3 mod 4 (Dirichlet). By reciprocity (r/ℓ)=(−ℓ/r)=−1. Therefore N=r^K≡−1 mod ℓ for K=(ℓ−1)/2 (odd) and for every K in this class modulo ℓ−1. Put d=(ℓ+1)/4 and b=(N+1)/ℓ. Then 4bd=N+e for e=b+1, all parameters are units at r (in particular r∤d as u≠1 mod r), and the oriented P-centre is −ℓ. Take K arbitrarily large so the box is inside the prescribed cylinder. Distinct ℓ may be used as j grows. Thus the nonsquare part of the sequential limit set as K→∞ is the *entire* nonsquare locus. The union of the positive-radius boxes is open dense there; any sterile subset is nowhere dense, even when positive in Haar measure. This is not a finite covering or a disproof of sterility at 17.

**PROVED (obstruction to the most direct lifting rule only).** For the fixed prime key f=ℓ above the admissible odd exponents must satisfy r^K≡−1 mod ℓ. The periods ord_ℓ(r) are unbounded even with the same prescribed low digits of the centre: all ℓ of order ≤H divide the fixed nonzero product of r^i−1, 1≤i≤H. Consequently a fixed phase K mod M cannot decide presence of *these individual prime keys* (otherwise take a period >2M and compare K with K+2M). The auxiliary datum is divisibility in ℤ by a unit prime to r, not Hensel solvability in ℤ_r. This does not exclude a finite automaton for existence of some other surviving child; it shows precisely what information an exact key-by-key Hensel recursion misses.

# y5_ocensus_hard_primes — census of the least certificate vertex o*(p), p ≡ 1 (8) ≤ 10⁷ (O213, brief item (b))

## Idea
By y5_transport_is_ptolemy, SQ₅(p) for p ≡ 1 (8) is exactly the statement "some positive word at p has its opposite
vertex o ≡ 7 (8)". Define o*(p) as the least such o. Is o* a better-behaved quantity than the least QNR (via (J)9:
λ(p) ≤ 3)? Where do the hard primes sit?

## Cheap numerics (`scripts/y5_ocensus.c`, log `logs/y5_ocensus.txt`; CERTIFIED as exhaustive computations)
All 165 976 primes p ≡ 1 (8) with p ≤ 10⁷:

| o* | interior words (letters ≥ 2) | formal words (letters ≥ 1) |
|---|---|---|
| 7 | 156 416 (94.2 %) | 157 186 |
| 15 | 6 240 | 5 513 |
| 23 | 2 262 | 2 290 |
| ≥ 39 | 459 | — |
| max | **2431 at p = 21841** (next: 335 at 691 681) | 239 at 6 154 009 |

Position of the first success (ties broken P_h > P_c > P_m), interior: P_h 56 696, P_c 91 590, P_m 17 690 (formal: 56 289,
94 254, 15 433). Among the primes with o* = 7 (interior), the three positions fire for 55 432, 141 236 and 109 333
primes respectively (not exclusive).

T1 control: none of the 499 odd squares ≤ 10⁶ has a certificate with o ≤ 3000 (formal words). Consistent with T1.

Hard primes (interior, o* ≥ 119): 7 940 521, 21 841, 238 681, 981 481, 8 984 641, 3 191 281, 4 362 121, 1 249 921,
691 681, 6 154 009.
(R211 repair: the list is incomplete — the full interior list o* ≥ 119 has 17 primes, adding 372 121, 501 841, 944 329,
1 749 001, 3 975 721, 7 183 201, 8 586 481; "≡ 1 (mod 120)" was false for 6 154 009 and 944 329, both ≡ 49 (mod 120).)
* All 17 are quadratic residues mod 840 (mod 8, 3, 5 and 7): p mod 840 ∈ {1, 121, 169, 361} (R211 repair).
* Their least QNR is n_p ∈ {11, 13, 17, 19, 23, 29}, and their least QNR prime ≡ 7 (8) is between 23 and 191 (R211
  repair; 191 at 8 586 481).
* The outlier p = 21841 = 1 + 2⁴·3·5·7·13 is ≡ 1 mod 3, 5, 7, 8 and 13 (n_p = 11), with o* = 2431 = 11·13·17
  (P_h position).

## Comparison with least-QNR theory
* o* is not a residue-symbol quantity. At o = 7, positions P_c and P_m fire through divisor events of p + 7 and
  7p + 1 that are unrelated to (p/7). Only P_h is QNR-shaped: (p/o) = −1 with o ≡ 7 (8) is forced, and o ≥ the
  least Jacobi non-residue in the progression 7 (8).
* The tail of o* is governed by locally square primes, as the ET/Mordell picture predicts. (J)26/(J)27 showed that
  primes near sterile points behave like primes near squares. o* is just another coordinate on the same lottery.
* Burgess-free? A bound o* ≤ (log p)^C would give, through P_c/P_m/P_h, a certificate found in time polylog × factoring.
  This is the polylog-height question of (J)9/(J)35, the same complexity barrier: it would yield QNRs (R211 repair: only for o_h*; a P_h certificate forces (p/o) = −1, while small o in P_c/P_m forces no small
  non-residue).

## Barrier screen
B6 (pointwise), B2 (divisor events in P_c/P_m), B1 (P_h is a congruence covering). T1 respected.

## Assessment
EVIDENCE: o* ≤ 2431 for interior words and o* ≤ 239 for formal words, at all p ≡ 1 (8) ≤ 10⁷. The heavy tail sits at
locally square primes. No structural improvement over the t_min / λ(p) formulations of (J)9. The single outlier 21841
is a fingerprint worth keeping: the interior five-slice problem at 21841 has only large-o certificates.

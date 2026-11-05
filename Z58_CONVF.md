# Z58 CONVF — tryhard lane: 4abcd = a + b + nc for all large primes p ≡ 1 (mod 24)

Status: NO PROOF (ES is open). This memo records (i) exact reformulations (PROVED), (ii) the obstruction that any proof
must pass (PROVED), (iii) new certified sub-family data, (iv) the attack lines tried and the precise step where each dies.
Scripts: `scripts/z58_convf_*`; data: `data/z58/convf/`.

## §0 Mandatory falsifiers (stated at first commit; re-checked in §6)

* **F1 (odd squares n = m²).** Every witness f = 4acd − 1 satisfies (n/f) = −1 (Lemma 1.3), so no argument that only
  uses n (mod f) can work; the step that uses non-squareness must be the one producing an f with (n/f) = −1.
* **F2 (d-even half, numerator 8).** Restricting to d even is the statement 8abcd' = a + b + nc; it has 22 prime zeros
  ≤ 10⁹ (last 35 569). An argument is only credible if the restriction "d even" visibly breaks it (e.g. it must use
  d = 1 or d odd somewhere, or the a = 1 / c = 1 sub-families with d odd).
* **F3 (4545 and the 285 composite c = 1 zeros ≤ 8·10⁶).** 4545 = 3²·5·101 ≡ 9 (mod 24); the composite c = 1 zeros are
  ≡ 1 or 9 (mod 24) (71 resp. 214 of them). Any argument that works for all n ≡ 1 (mod 24) non-square must fail at the
  71 composite c = 1 zeros ≡ 1 (24) if it only uses the c = 1 line, and must not apply to 4545 at all (threshold or
  a step using primality/non-divisibility by 9).
* **F4 (the 14 primes ≤ 10¹⁰ with no c = 1 witness).** 409 … 8 813 281. Any argument confined to c = 1 is false there.
  All 14 have witnesses with a = 1, c ∈ {2, 3} (data/z58/convf/wit_hard.txt), so an argument confined to a = 1 is
  consistent with them — but a = 1 alone has its own zeros {193, 2521, 66529}.

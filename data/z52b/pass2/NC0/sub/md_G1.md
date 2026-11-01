# z52d Pass 2 NC0 — G1 interesting items

## Z0353 — FF failures of ES_q(T,P) concentrate on P with many-factor P−1 (interesting)
* What: decision engine `scripts/bs_ff_es.py` (Lemma 1.3, A=T, 3 monic denominators). For monic irreducible P, T∤P, degree n,
  record ES failures and the factor count of P−1 (monic, same degree).
* Numbers, q=7 (`data/z52b/pass2/NC0/sub/Z0353_q7_out.txt`): failures/irreducibles: n=2 6/21, n=3 21/112, n=4 25/588, n=5 16/3360.
  Failure rate by #irreducible factors of P−1 (factors counted with multiplicity):
  - n=4: 1 factor 2/112 (1.8%), 2: 11/273 (4.0%), 3: 6/126 (4.8%), 4: 6/77 (7.8%)
  - n=5: 1: 0/560, 2: 2/1162 (0.17%), 3: 6/1057 (0.57%), 4: 5/448 (1.1%), 5: 3/133 (2.3%)
  - Mean #factors(P−1): n=5 failing 3.56 vs ok 2.53.
* q=5 (`Z0353_out.txt`): failures at n=2,3,4,5,6: 2, 2, 1, 0, 0 of 10, 40, 150, 624, 2580. All 5 failing P have P−1 with an F_5 root,
  but this does NOT hold at q=7 (n=2..5: 9 of 68 failing P (n≤5) have no root of P−1 in F_7), so the root condition is not a rule.
* Why it might matter: the FF analogue of "p−1 smooth ⇒ hard" (Z0353) shows a monotone trend in the within-degree rate; the
  Z-side hard primes (601, 1801, 2521) are the ES analogue. Caveat: the trend may be a generic count effect (#factors of a random
  degree-n polynomial grows like log log); a degree-profile-matched control is not yet done.
* Reproduce: `python3 scripts/z52d_p2_NC0_Z0353.py 5 7` (≈4 min, one core; uses `scripts/bs_ff_es.py` with Q set from argv).
* Next: at q=7 and q=11 for n=6 (≈10^4 irreducibles, a few CPU-hours in pure Python — port es_solutions to C or cap by degree),
  compare failure rate against a control matched on the factor-degree profile of P−1 (not just the count).

## Z0323 — four monic terms over F_5[T] cover the 3-term failures at deg ≤ 4 (interesting)
* What: 3-term engine (`scripts/bs_ff_es.py`, A=T, Q=5) fails on P = T²+4T+1, T²+2 (deg 2), T³+3T²+2T+2, T³+3T+2 (deg 3),
  T⁴+T²+2T+2 (deg 4); no 3-term failures at deg 5, 6 (2580 primes).
* 4-term witnesses (exact identities; `data/z52b/pass2/NC0/sub/Z0323_wide_out.txt`): T/(T²+2) = 1/T + 3/(T(T²+2)) (repeated
  denominators), and for T⁴+T²+2T+2 a witness with denominators of degrees 3, 4, 7, 13 (`(0,0,1,1),(0,0,0,2,1),(0,0,4,4,1,3,1,1),(0,0,0,3,4,0,1,0,4,0,3,0,2,1)`, coefficients low→high).
* Caveat: the 4-term search with X1,X2 of degree ≤ n−1 finds nothing (`Z0323.py`), so witnesses need denominators of degree up to n+1 (n≤3) or 4 (n=4).
* Reproduce: `python3 scripts/z52d_p2_NC0_Z0323.py 4` (≈2 min; the n=4 widening is in `scripts/z52d_p2_NC0_Z0323_wide.py`, ≈4 min).
* Next: distinct-denominator filter on the witnesses.

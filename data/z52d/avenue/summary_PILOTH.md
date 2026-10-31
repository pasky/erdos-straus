# z52d avenue — batch PILOT (replica PILOTH), 40 items

ES is OPEN. Lines are judgements about missing theorems, not proof steps.
Outputs: out_PILOTH.jsonl (40 lines); checks in checks_PILOTH/.

## Histogram: status x plausibility (count)
| status | p=0 | p=1 | p=2 | p=3 | total |
|---|---|---|---|---|---|
| known-true | 0 | 0 | 0 | 2 | 2 |
| known-false | 5 | 2 | 0 | 0 | 7 |
| circular | 7 | 5 | 0 | 0 | 12 |
| harder-than-open | 0 | 1 | 0 | 0 | 1 |
| open-plausible | 0 | 2 | 1 | 0 | 3 |
| unclear | 4 | 8 | 3 | 0 | 15 |

## Plausibility >= 2 AND novelty >= 1
- Z0089 (p2,n1): analogue in O_K, K=Q(sqrt3): totally positive ES via finite unit-orbit covering. Not a step over Z.
- Z1644 (p2,n1): fixed m, all large n: m/n = sum of 4 distinct unit fractions. Depends on Elsholtz 2001 (NOT verified).
- Z2068 (p3,n1): calibration only; Davenport-type pointwise 4-cube theorem (recalled, unchecked).

## Recurring missing theorems
- "One integer, one divisor-in-class event" (ES restated): Z0210, Z0978, Z1333, Z1464, Z1580, Z1681, Z1813, Z1967, Z1987, Z2099, Z2778, Z3060.
- "Fixed finite menu covers all p = 1 (mod 24)": Z1838, Z2228, Z2877, Z2899, Z3183 (known-false under H).
- "Descent to a finite base via positivity-preserving involutions": Z1454, Z2258 (known-false; U_n linear in each variable).
- "Power-saving averaged exceptional set": Z0003 (unclear); Z1929 is the sieve version.
- Numerator family a/n (a=4 is ES): Z1425 (harder-than-open); numerator 9: Z0735.

## Checks run
- Z0003 premise is wrong: FUNCTIONFIELD_ES.md §5 gives failure proportion <= (Phi(A)+o(1))/log n (Chebyshev, one sparse family); RH only replaces Bombieri-Vinogradov. No FF power saving to transfer.
- Z0735 (9/n): exact search (x in [n/9, n/3], Rav test): three-term failures exactly {2,5,11,19} for all n <= 20000. Matches BRAINSTORM/ident_numerators.md. Not a proof for all n.
- Z3183: p = 1 (mod 24), p <= 10^5 (1181 primes). Cap C<=30: 13 unhit. Cap C<=3000: 6 unhit (409, 577, 5569, 9601, 23929, 83449). 7 primes hit only at levels in (30, 3000]. Fixed cap fails i.o. under H.
- Z0210: the box lift is automatic when |F| < M, so the item is ES with a polynomial height bound. Circular.
- Z1967: for p = 1 (mod 3), 3/p is never two-term (divisors of p^2 are 1 mod 3; -p is 2 mod 3).

## Not run (queued in out_PILOTH.jsonl `next`)
- Z1454 Mobius-reflection integrality test; Z1464 adaptive greedy C-rule for p = 409, 577; Z2138 rewrite graph for p <= 500; Z2433 slice rank over F_3, F_5; Z0026/Z0831 square-certificate classification.

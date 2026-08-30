# UNIT J21 report

## Delivered

- Appended `notes.md` §56, “The extremal window: the congruence-certificate ceiling, and the census.”
- Appended `verify.py (bc)` after `(bb)`; default work is about 3 seconds inside the full harness, and all larger scans are behind `ES_FULL_SCAN=1`.
- Left `PROJECT.md` and `paper/` untouched.

## Theorems and scope

- **Theorem 56.1 (proved, effective ceiling constant):** a complete integer certificate, or a reduced prime-bearing certificate, for `W>T` has modulus divisible by every prime `ell<=T`, `ell=3 mod 4`. Hence `log Q >= theta(T;4,3)=(1/2+o(1))T`. The `D=1` class is instantiated explicitly by `(u,v,w)=(1,(ell+1)/4,1)`. This is the prime-progression extension of Theorem 33.1, not claimed as an independent new mechanism.
- **Theorem 56.2 (proved, effective ceiling constant):** a reduced hard-prime class certifying `ck_min>T` has modulus divisible by every prime from 5 through `T`, hence `log Q >= theta(T)-log 6=T+o(T)`. The proof uses the active prime-core refinement and Corollary 52.2; the character-sign step is explicit CRT/quadratic reciprocity, avoiding any multiplicative-progression confusion.
- The Linnik corollary is scoped to the certificate + `Q=exp((alpha+o(1))T)` + generic least-prime recipe. Type I saturates the certificate exponent; the proved Type-II ceiling leaves a factor-two constant gap. The text retains §54’s conservative effective `L=5.2`; under GRH, `L=2+epsilon` gives the conditional `(1/2-epsilon) log p` lower sequences.
- The “beyond log” statement is labelled an **Assessment** about that architecture. It explicitly does not claim a universal no-go for every congruence-informed construction.

## Exact census data

- `W`, complete Lemma-16.1 harvest through modulus 3000:
  - default: 9,732 hard primes below `10^6`, maximum 335 at 954,409;
  - full: 82,887 hard primes below `10^7`, maximum 2,495 at 2,031,121.
- `ck_pr`:
  - default: 3,202 hard primes below `3*10^5`, maximum 461 at 171,481;
  - full: 9,732 hard primes below `10^6`, maximum 898 at 538,561.
- `D`:
  - default maximum 102 at 92,401;
  - full maximum 217 at 414,241.
- §56 records all strict record sequences and maxima normalized by `log p`, `log p log log p`, and `(log p)^2`. They are labelled finite informational data with no growth-law inference.

## Memory and regression design

- Prime generation is chunked into bounded intervals.
- `W` tests small moduli first and exits per prime at the first hit.
- Type-I scans keep unresolved-prime maps only, skip exact genus-forced signs before factoring, factor one norm at a time, and retain at most one residue set of size `4ck`.
- Counts, record sequences, maxima, normalized maximizers, final guards, and factorization counts are regression assertions.

## Validation

- `ast.parse`: passed.
- Final full default harness: passed, `all checks passed`, 101.93 s, 334,560 KB peak RSS.
- Isolated `ES_FULL_SCAN=1` execution of exact `(bc)`: passed in 11.79 s, 109,984 KB peak RSS.
- A global `ES_FULL_SCAN=1` run activates unrelated legacy full-scan blocks and exceeded 400 seconds before reaching `(bc)`; no result from that interrupted run is used.
- `git diff --check`: passed.
- Section order: §56 is the sole final top-level section.
- Control bytes: zero in changed files.

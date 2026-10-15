# z5_pm_sqpm — the prime-modulus core of SQ_±: a free genus filter, exponent 1/2, CONJECTURE PM-SQ_± (O229; CAP_GROWING §3)

**ES is not solved here.**

## Idea
O218 spark 1 (sieve the slots of SQ_±). Restrict to words with A = tu − 1 = ±ℓ prime. Then (Lemma 3.1, PROVED)
χ = (n/ℓ) = (−u/ℓ) and the word exists iff ℓ | n + u with u | ℓ ± 1: **every prime ℓ with (n/ℓ) = −1 turns every hit
n ≡ −u (mod ℓ), u | ℓ ± 1, into a χ = −1 word** — the genus layer is free; the size layer is a residue in a set R(ℓ) of
size ≍ τ(ℓ² − 1). For |u| ≤ 6 (u ≠ −1, −4) u | ℓ ± 1 is automatic: "n + u has a prime factor in the non-principal genus
of ψ_u = (−u/·)" — the shift-dual of the |t|n ± 1 slot table.

## Literature
SYNTHESIS_SPARKS4 §2 (SQ_±, slot table, no finite t-set under Dickson); Montgomery's large sieve; Titchmarsh divisor problem.

## Result
* Prop 3.2 (PROVED): #{n ≤ N, n ≡ 1 (8): no prime-modulus χ = −1 word} ≪ N exp(−c (log N)^{1/2}).
* Calibration (Assessment): the prime-modulus class mass of SQ_± is ≍ log X (measured 2.06·log N at 10⁶) vs (log X)² for
  ES (Vaughan): the "easier" signed twin is *harder on average* for the large sieve; its ease is pointwise.
* **CONJECTURE PM-SQ_±**: every non-square n ≡ 1 (8) has a prime-modulus χ = −1 word. EVIDENCE: 0 exceptions ≤ 10⁶
  (z5_sqpm_prime.py), random checks to 10¹¹, adversarial n ≡ 1 (mod 8∏_{q≤31} q) ≈ 10¹³ still have ≥ 21 tickets with
  |u| ≤ 300. Unlike PM-II (exception 3361), stacking residues cannot kill it: tickets come from LARGE primes of n + u.

## Barrier screen
T1: (n/ℓ) = +1 for all ℓ ∤ m when n = m² — no ticket ever (CERTIFIED: 0 odd squares marked ≤ 10⁶). B2: R(ℓ) is a
moving divisor set. Forcing: the total character ψ_u(n + u) is a function of n mod 4|u|, = +1 on residue classes of
squares, so genus forcing only covers non-residue classes (B1; e.g. u = 3 forces n ≢ 2 mod 3). Pointwise: lottery
with ≈ 2 log n tickets (Poisson failure ≈ n^{−2}, summable — heuristically finitely many exceptions).

## Cheap numerics
z5_sqpm_prime.py 1000000 (7 min), z5_sqpm_verify.py, z5_sqpm_adversarial.py.

## Assessment
PROVED (average, exponent 1/2) + CONJECTURE PM-SQ_± (EVIDENCE to 10⁶). A clean exception-free prime-modulus test bed.
No pointwise mechanism.

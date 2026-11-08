# Z64_SDEEPF — tryhard lane on conjecture (S): length-3 words with Jacobi symbol −1

Lane: SDEEPF, wave z64. Fresh/unprimed (no FRONTIER, no Z5*/Z6*, no HJ_DEEP/DEDEKIND_ES/BRAINSTORM read).
Scripts: `scripts/z64_sdeepf_*`; data: `data/z64/sdeepf/`.

## §0 Statement and mandatory falsifiers

**(S).** n ≡ 1 (mod 4), n not a square. A *length-3 word* of n is A = tu − 1 with integers t, u, v ≥ 2,
tuv − u − v = n, gcd(A, n) = 1. Claim: if n has a word, it has one with Jacobi symbol (A/n) = −1.

Falsifiers to be answered at the end (§F):
* **F1** odd squares n = m²: every argument must break there; identify the step.
* **F2** sub-family arguments (fixed parity of t, u, v, A) must be screened on `data/z58/screens/r8_zeros_1e10.txt`
  and `star_prime_zeros.txt`.
* **F3** composites: say whether primality is used.
* **F4** the 14 primes of `star_prime_zeros.txt` and the 38 of `gstar_zeros.txt` satisfy (S) — verify.

Status key: PROVED / CONDITIONAL (on what) / CERTIFIED (computation) / EVIDENCE.

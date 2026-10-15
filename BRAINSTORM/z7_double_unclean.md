# z7_double_unclean — U2: words with A and B both unclean; CONJECTURE U2 (O231)

## Idea
A | N_t, N_u and B | N_t, N_v. So "A and B both contain a ψ-odd prime" is a cheap certificate of unforcedness that
uses only the two coupled divisors. Let U2 count such words: N₋ ≤ U2 ≤ U (PROVED).

## Results (UNFORCED_WORDS §4)
* EVIDENCE, all 464 288 primes p ≡ 1 (8) < 3·10⁷:
  * U2 ≥ 1 everywhere;
  * Σ N₋/Σ U2 = 0.873 and Σ U2/Σ U = 0.882;
  * min N₋/U2 = 0.620 (p = 23 125 409);
  * at the three O230 failures of N₋ ≥ U/2, N₋/U2 ≈ 0.70.
* Over n ≡ 1 (8) ≤ 2·10⁵ (composites too), U2 = 0 only at 105.
* **CONJECTURE U2:** for odd non-square n ≡ 1 (4), U2(n) = 0 ⟺ n = 105. Unrefuted: N₋ ≥ U2/2 (to 3·10⁷, primes ≡ 1 (8)).
* For n ≡ 5 (8), Mordell's word (1, 3, (n+3)/2) has A = 2 and B = (n+1)/2 both ψ-odd.
* A deterministic sub-family: words with q | A and q | B (q = least NR prime) are in U2. Such a word exists at 86 % of
  primes ≡ 1 (8) < 3·10⁵ (`scripts/z7_lnr_family.py`), not all (B2).

## Literature
None; new invariant.

## Barrier screen
* B2: U2 ≥ 1 needs the coupled divisors A ≡ −1 (mod t) of tp + 1 to both carry ψ-odd primes, a divisor event in
  moving moduli.
* T1: U2(m²) = 0.
* B6: the ratios are averages.

## Cheap numerics
`scripts/z7_types.c` columns 3–5.

## Assessment
EVIDENCE + a trivially PROVED sandwich. A tighter descriptive invariant than U. "N₋ ≥ U2/2" is a candidate
distributional law, unlikely to be an injection (see z7_haar_strata: failures of N₋ ≥ U/2 are a family-size effect).

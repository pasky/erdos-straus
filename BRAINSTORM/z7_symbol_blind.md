# z7_symbol_blind — the t-side is symbol-blind: the anti-Landau kernel of CONJECTURE U (O231, goal 1)

## Idea
Which uncleanness can a deterministic argument certify? ψ(N_u) = ψ(u) and ψ(N_v) = ψ(v) are symbol-visible: an NR
u makes the u-side unclean for free. But ψ(N_t) = ψ(tn + 1) = 1 identically. So the t-side's uncleanness (≥ 2 ψ-odd
primes) is never visible to a symbol.

## Results (UNFORCED_WORDS Lemma 2.1)
* (a) ψ(u) ≠ ψ(v) ⟺ certificate.
* (b) ψ(u) = ψ(v) = −1: unforced ⟺ tn + 1 ∉ C_n (C_n = clean integers).
* (c) ψ(u) = ψ(v) = +1: three symbol-blind sides.
* Every non-certificate unforced word needs the event "tn + 1 ∉ C_n". In the U = 0 world, all words with NR u (in
  particular u = q, the least NR prime) are non-certificates with clean tn + 1. This is a strong Landau-type constraint
  on a growing family, but it is not contradictory by any symbol argument (B1).
* Type split of non-certificate unforced words (EVIDENCE, z7_ratio.c, p ≡ 1 (8)):
  * (−,−) is 35–38 % at min ≥ 1, 63–71 % at min ≥ 3;
  * at p ≡ 5 (8), (−,−) is ≈ 48 % at min ≥ 1, 55 % at min ≥ 3.
* Least-NR families (`scripts/z7_lnr_family.py 300000`, 6 457 primes ≡ 1 (8)):
  * a word with u or v = q: 96 %;
  * q | gcd(A, B), which forces all three sides unclean: 86 %;
  * q | tn + 1 with ψ(u) = ψ(v) = −1: 76 %;
  * neither of the last two, worst case q = 29 (p = 87 481).

## Literature
* Burgess (1962) for q.
* Landau–Bernays densities for C_n ∩ [1, x] (≍ x/√log x).
* Distribution of C_n in the progression 1 (mod n): no result at the needed scale, x ≈ n·T with T small. It would
  need equidistribution of the Landau set in progressions to moduli ≈ x, beyond Bombieri–Vinogradov-type ranges
  (Assessment).

## Barrier screen
* B1: symbol evaluations are all +1 on n ≡ 1 (mod M).
* B2: the q-families need divisors in classes mod u.
* T1: C_{m²} = everything, so U(m²) = 0 (respected).
* B3: n/a. B6: the percentages are averages.

## Cheap numerics
`scripts/z7_lnr_family.py`, `scripts/z7_ratio.c`.

## Assessment
PROVED kernel lemma + EVIDENCE. It identifies the precise non-congruence input any U-proof must supply: one value
tn + 1 ∉ C_n on a word with NR u, v. That is a "Landau-negation in a moving progression". Promise 1.

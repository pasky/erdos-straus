# y3_primemod_census — prime-modulus Type II: census, growth law, the 3361 exception, sieve screen (O211 (c))

**ES is not solved here.** Labels as in DISCOVERIES.md.

## Idea (O207 spark 2)
O207's supersingular dictionary (TORSION_FIRING §1) covers Type II certificates with a PRIME modulus h. p = 3361 is
the unique prime ≤ 10⁷ without one. Is it the last? What is the growth law of N_II^pr(p) := #{(c, d, h) : h prime,
4cd | h + 1, h | p + 4c²d} (all h, no range cut)? Is there a Chen-type sieve handle at a single p?

## Census (EVIDENCE; scripts/y3_census.c, exhaustive over all certificates via (4cdt − p)j = c + t)
| range | #primes | mean N_II | mean N_II^pr | min N_II^pr (at p) |
|---|---|---|---|---|
| [2¹⁰, 2¹¹] | 137 | 48.7 | 15.5 | 2 (1093) |
| [2¹¹, 2¹²] | 255 | 61.2 | 18.0 | **0 (3361)** |
| [2¹³, 2¹⁴] | 872 | 91.7 | 24.0 | 3 (8581) |
| [2¹⁶, 2¹⁷] | 5709 | 157.2 | 35.4 | 1 (76441) |
| [2¹⁷, 2¹⁸] | 10749 | 184.6 | 40.0 | 5 (152461) |
| [2¹⁸, 2¹⁹] | 20390 | 212.9 | 43.9 | 6 (291481) |
| [10⁵, 10⁶] | 68906 | 222.9 | 45.4 | 5 (152461) |
| [10⁷, 10⁷+2000] | 121 | 402.0 | 70.2 | 34 |
| [10⁸, 10⁸+1000] | 54 | 680.8 | 113.1 | 38 |
Every p with N_II^pr ≤ 1: 13, 193, 3361 (0), 76441 — all with p − 1 divisible by many small primes (3360 = 2⁵·3·5·7,
76440 = 2³·3·5·7²·13, 192 = 2⁶·3): stacked quadratic residues, so (h/p) = 1 for every small prime h, and by
reciprocity no small prime can fire ((pd/h) = −1 is necessary). Growth: mean N_II^pr / log²p ≈ 0.27–0.33 across
10³–10⁸; mean N_II / log³p ≈ 0.10–0.12. (R216 repair: R216's complete census to 10⁸ (data/r216/census_1e8.txt) gives
full-block values drifting down, 0.289 → 0.261 and 0.124 → 0.093 over [2¹⁰, 2²⁶); the upper ends come from short
windows; exceptions with N_II^pr ≤ 1 to 10⁸: exactly 13, 193, 3361, 76441.) Exhaustive (tf_primemod.c, O207 code): 3361 unique ≤ 10⁸ (≈ 2.8 h run; 5 761 453 primes).
Adversarial (scripts/y3_adversarial.py 200): p ≡ 1 (mod 4·∏_{q≤Q} q), Q ∈ {13, …, 29}, p up to 1.3·10¹¹: 4–20
slices with cd ≤ 200 carry a prime-modulus certificate (min 4 at p = 600601). Odd squares (T1): 0 throughout.

## Sub-conjecture
**CONJECTURE PM-II.** Every prime p ≥ 5, p ≠ 3361, has a Type II certificate with prime modulus h; moreover
N_II^pr(p) ≫ log²p / (something tending to ∞ slowly) — EVIDENCE: exhaustive to 10⁸ (tf_primemod rerun, data/y3/primemod_1e8.txt), census above.
For p ≡ 3 (mod 4) it is trivial (p + 4 ≡ 3 mod 4 has a prime factor ≡ 3 mod 4; y3_euclid_schur_forcing Prop E1).

## Sieve screen (Chen-type handle at a single p)
* PM-II is *stronger* than Type II-ES (it fails at 3361), so any single-p sieve proof of it would prove Type II-ES
  for p ≠ 3361: B2/B3 apply verbatim (the modulus 4cd | h + 1 is attached to the solution; a fixed slice set fails
  i.o. under H; the main term at fixed p is the polylog lottery).
* Chen's switching (P₂ instead of prime) is the wrong direction: ES accepts any h; the prime restriction only serves
  the supersingular dictionary. Relaxing to "h has ≤ 2 prime factors" interpolates between PM-II and Type II.
* On average over p (B6) Σ_{p≤N} N_II^pr(p) ≍ N log N is the standard Bombieri–Vinogradov count over prime h with
  moduli 4cd ≤ h^{1/2−ε} (Assessment: standard, not written out).
* Per slice, prime-modulus firing ⟺ M = p + 4c²d has a prime factor with Frobenius c_∞ in ℚ(ζ_{4cd})
  (y3_frob_infinity): failure probability ≈ (log p)^{−1/φ(4cd)}-type (Assessment) — large for big slices, so the
  count is driven by many weakly-firing slices: again the lottery.

## Assessment
EVIDENCE + CONJECTURE (PM-II). Clean sub-conjecture with one exception; no new proof handle (B2/B3/B6).

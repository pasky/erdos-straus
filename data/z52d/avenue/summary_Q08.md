# z52d avenue — batch Q08 (113 items) summary
ES is OPEN. Rows: `out_Q08.jsonl`. Per-row labels are Assessments unless they cite a PROVED/CERTIFIED source. This was a non-proof-attempt
batch: analytic-technique transfers (Z25xx–Z31xx), geometry/sibling worlds (Z00xx–Z07xx), and 17 calibration-only rows.

**Status × plausibility** (rows: status; columns: plausibility 0/1/2/3)
| status | 0 | 1 | 2 | 3 | Σ |
|---|---|---|---|---|---|
| known-true (gap named) | 0 | 0 | 1 | 30 | 31 |
| known-false | 30 | 0 | 0 | 0 | 30 |
| circular | 28 | 1 | 0 | 0 | 29 |
| open-plausible | 0 | 12 | 1 | 1 | 14 |
| unclear | 5 | 0 | 1 | 0 | 6 |
| harder-than-open | 3 | 0 | 0 | 0 | 3 |
Novelty: 0 → 61, 1 → 50, 2 → 2 (Z0119 calibration lemma; Z2965 Faltings, plaus 0). Plaus-3 rows are calibration/averaged (yield none/partial).

**Plausibility ≥ 2 AND novelty ≥ 1**: none has an ES yield. The only rows with any yield are averaged:
* **Z2597**: *Σ_{n≤N} f(n) = N·P(log N) + O(N^{1−δ})* (power-saving total count; B6). **Z2619/Z2636**: fixed-depth sieve densities (superseded by 3/4). The others (Z2522, Z2575, Z2953, Z2960, Z3072, Z3118, Z3148, Z3156, Z0098, Z0119, Z0172, Z0287, Z0342) are calibration with yield none.

**Recurring missing theorems**
1. *Two-sided pointwise asymptotic from cancellation* (false i.o. by Linnik, Prop 3.1; only §7.1 power savings remain): Z2599, Z2917, Z2999, Z2628.
2. *Modular hyperbola with height-dependent target* (= §7.1, open, plaus 1): Z2958, Z3149 (the k-reparametrisation is PARITY_AUDIT's 𝓗 verbatim).
3. *ES on the least-non-residue lines / splitting classes* (finite coverings blocked if x** is sterile; (★)-version false): Z2614, Z2949, Z3066, Z3170, Z2941.
4. *One-coordinate polylog window* (open, §7.2; two-coordinate windows false): Z3087, Z3167.
5. *Sub-lotteries of (★)* (prime/P₂/large-prime/smooth parameters; circular): Z2582, Z2907, Z3096, Z3165, Z3171, Z2633, Z0705.
6. *No group action / no transport* (M3; finite Aut U_n): Z0082, Z0175, Z0176, Z0237, Z0646, Z2932, Z0486, Z0464; sideways descent: Z0533, Z0538, Z0612.
7. *Regime/dichotomy architectures* (each regime is B2): Z2512, Z3002, Z2941. 8. *Galois/Frobenius forcing* (parity, never class): Z2860, Z3120, Z2644.

**New in this pass** (`scripts/z52d_avenue_Q08_ap_smooth.py`, < 60 s)
* **Z0119 (PROVED)**: 4/n = 1/x + 1/(x+d) + 1/(x+2d), d ≥ 1, forces 4 | n (2-adic valuation of 4y(y² − d²) = n(3y² − d²)). Checked for n < 2000.
* **Z0705 (PROVED)**: in every solution for a prime p the largest denominator is divisible by p (explains Pass 1's 'minz ∈ pℤ'; 1227 solutions checked).
* **Z3089**: by Lemma CT a certificate divisor needs a prime ℓ with (ℓ/p) = −1, so y-smooth certificates fail whenever y < lnr(p): i.o. for y = o(log p·log₃p).
* **Z2949/Z2970/Z3066/Z3170** (cheap falsifications): the 14 (★)-failures ≤ 10¹⁰ have least non-residues 5–23 (577: 5, 409: 7). Three have (p/11) = −1,
  and 78 pairs satisfy p < p′ < p². So 'failure ⇒ QR at small primes' and '(★) on (p/ℓ) = −1' are false; no repulsion is seen in range.
* **Z0098**: cone |x|_v ≥ 1 is trivial (4/p = 1/((p−1)/4) − 4/(p(p−1))). **Z0638**: ℤ[1/2], ℤ[1/3] have one-line identities. **Z2958/Z3149**: k_d = complementary divisor.

**Corrections.** Z2578 (large-q FF ES is false for most P, ff_erdos_straus Thm 2.1). Z2963: M_BM needs an upper bound on L(1, χ_p), so Siegel points
the wrong way, and BM_LVALUE already gives ≥ 0.92 M₀. Z2631: the slice window has length ≍ p, not polylog. Z2644: per-(c,d) density is not Chebotarev.

**Assessment.** No Q08 architecture escapes B1/B2/B3/B6 or the tied modulus. The one concrete decidable sub-question is Z3066: decide
x** (deeper MORDELL13E search or a sterility proof). A covering would give the first every-p theorem on a Mordell-hard splitting class ((p/11) = −1).

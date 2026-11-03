# Z55 HCO hostile cross-model review

Reviewed `side-agent/z55-hco` at `d575cb39d9f9c58e115692eb79ad0d5a43487ae3`.
**Verdict: ACCEPT-WITH-FIXES.** The new proofs survive and the decisive numerical checks agree.
The pointwise target remains open; this strengthens the finite-range evidence and narrows particular approaches, not ES itself.
All shell work used `ulimit -v 6000000` (initial inspection: 2097152) and explicit timeouts.

## Per-claim audit

| Claim | Classification | Finding |
|---|---|---|
| §1 divisor/word reformulation | CORRECT-WITH-FIX | U: `v(tc−1)=p+c`; T: `(cu−1)(cv−1)=cp+1`. The group formulation must discard nonunit prime factors, or restrict to `c<p`. |
| L2.1 quadratic parity | CORRECT | Reciprocity and multiplicativity give exactly the claimed identity and odd valuation sum; `p∤k` is essential and stated. |
| P2.2 fixed-divisor/cofactor congruences | CORRECT | All four equivalences hold, including positivity and the T-line cancellation. The odd-c mod-8 condition is retained. |
| Cor 2.3 logarithmic obstruction | CORRECT | Linnik supplies infinitely many locally square primes; each of the three possible small-μ cases contradicts reciprocity. This is only a logarithmic obstruction. |
| C3.1 census to 10¹² | CERTIFIED claim passes audit | Code and archive consistency inspected; fresh census below 10⁸ agrees exactly; all 126 recorded HC≥44 primes independently pass SymPy minimality and witness checks. Full 10¹² enumeration was not rerun here. |
| E4.1 minimum-HC moduli | EVIDENCE reproduced | Exact min/median/max exponents: 0.137721066 / 0.345977876 / 0.635974771; 101/126 exceed log²p. This restriction to `c=HC(p)` is consequential. |
| §4 least-nonresidue statistics | EVIDENCE reproduced | All 126 have least QNR≥11; 100 have ≥17; comparison fraction is exactly 596/2409. |
| E4.2 locally square families | EVIDENCE reproduced in part | All five archived histograms give the stated fractions; fresh full y=29,31,37 runs reproduce histograms, counts and maxima. Sample-size causation is not established. |
| E4.3 height dependence | EVIDENCE reproduced | Aggregation agrees byte-for-byte, including endpoint tail fractions. Neither monotonicity at every height nor the model's asymptotic law follows. |
| Quoted UPPER T4.2/T4.3 and HCHYP U | CORRECT as quoted | Rechecked the sieve/Rankin and confinement reductions: fixed-parameter constants and the Henriot dependence are retained; no pointwise bound follows. These are inherited results, not new HCO theorems. |
| §§0,2.3,5 methodological conclusions | CORRECT-WITH-FIX | Honest “not proved” headline, but minimum-HC data do not justify requiring non-polylogarithmic μ anywhere in the allowed coordinate window. |

## Proof reconstruction

1. **L2.1.** Any prime ℓ dividing `p+4k` is odd, not p, and does not divide k.
   Since `p≡1 (4)`, `(ℓ/p)=(p/ℓ)=(−4k/ℓ)=(−k/ℓ)`.
   Multiplying over prime powers yields `(k/p)=(-1)^{sum of nonresidue valuations}`.
   At an odd square every coprime Jacobi symbol is +1, so the nonresidue hypothesis disappears.
   The character bit does not isolate −1 in a larger unit group; the stated limitation is sound.
2. **P2.2.** For U, fixing d gives `p′≡−c (d)`; fixing e requires `ce | p′+c+e`.
   For T, `gcd(c,d)=1` gives `p′≡−c⁻¹ (d)`.
   Also `e≡−1 (c)`, so `ce | cp′+1+e` is equivalent to `e | p′+(e+1)/c`.
   Every resulting positive quotient is a positive certificate divisor.
   Selecting the smaller modulus chooses one of two certificate families containing p; it is not a universal covering.
   Their modulus products are `c(p+c)` and `cp+1`, giving the stated square-root upper bound.
3. **Cor 2.3.** Set `M=8∏_{3≤q≤Y}q` and take the least prime `p≡1 (M)`.
   Linnik gives `log p≤L₀ log M+O(1)≤1.02L₀Y+O(1)`; `p≥M+1` ensures infinitely many distinct p.
   The last theta estimate is needed only eventually and already follows from the prime number theorem.
   Reciprocity gives `(q/p)=1` for every prime q≤Y, including q=2.
   If μ≤Y, then `c≤μ+1<p`: from d≥c−1, T's e≥c−1, or U's ce≥c, respectively.
   Re-derived UPPER L3.1: `(d/p)=(2/p)^a(−c/d_odd)`; this is −1 for both `4|c` and `c≡−p (8)`.
   Thus μ=d or T's μ=e contradicts smoothness immediately.
   For U's μ=ce, both c,e are Y-smooth and `de=p+c` forces `(d/p)=(c/p)(e/p)=1`, again impossible.
   Nothing in this argument excludes μ≤log²p, still less all polylogarithmic moduli.
4. **Inherited rates.** UPPER's classes are distinct above 16K²; Rankin truncation and the large sieve give T4.2.
   For T4.3, the moving Siegel–Walfisz cutoff makes the summed errors bounded and leaves the stated `(log log x)²` saving.
   HCHYP's subgroup confinement, primitive nonproportional linear forms, and fixed-X Rankin weights give U using its stated Henriot bound.
   This review does not independently reprove the external analytic sieve theorems.

Decisive external sources checked: Heath-Brown, *Zero-Free Regions for Dirichlet L-Functions…*, Theorem 6,
`P(a,q)≪q^5.5`, in the [author's paper](https://ora.ox.ac.uk/objects/uuid:b63b8b4f-ad21-4de4-a86b-c82fdfc87997/files/m23439806c997d19e6ad333ac00b75a12);
and Sorenson–Webster, [Theorem 1.1](https://arxiv.org/html/1509.00864v1),
`ψ₁₂=318665857834031151167461`, validating the census's twelve-base primality test throughout its input range.

## Numerical checks and new sensitivity check

- Rebuilt the C census and reran `[0,10⁸)` with four threads: sorted output identical, including HC=64 only at 21841.
- Re-ran aggregation: chunks tile `[0,10¹²)`, zero archived failures, totals 9,401,951,850 and 9,401,972,490.
- Re-ran `verify.py`, `certsize.py`, `parity_check.py`, and `qnrstats.py`: 126 valid/minimal HIGH records;
  certificate-size output identical after sorting; 234,541 parity tests, zero violations; QNR counts agree.
- Recomputed E4.1 thresholds: 86 moduli >1000, 101 >log²p, 118 ≥p^0.2. All stated rounded ratios agree.
- Fresh adversarial runs: y=29 gives 14,673 primes/max HC 23; y=31 gives 525/15; y=37 gives 13/7.
  The y=29 maximizing prime can differ because two primes tie and OpenMP selects a first maximum; the histogram is identical.
- Census audit: segmented sieve endpoints, trial division, 128-bit modular products, complete divisor enumeration,
  and guarded buffers are consistent. The `<10⁶` factor shortcut is valid after stripping all primes below 1000.
  The same-kernel picount and guarded-rerun archives are corroboration, not independent full-range replications here.
- **New independent check:** `scripts/z55_xrev_hco_window.py` exhausts fixed-d and fixed-e congruences with
  `c,μ≤B=floor(log²p)` for all 126 HIGH primes, validating every found witness by integer arithmetic.
  Results: 25 already have such a certificate at HC; **76 more have one at a larger c**; 25 have none within this window.
  Thus 101/126 have small-modulus certificates in this enlarged window, reversing the minimum-HC headline fraction.
  Examples: p=21841 uses `(c,d,e)=(68,67,327)` on U, μ=67, rather than μ=575 at HC=64;
  p=691681 uses `(71,691752,1)` on U, μ=71, rather than μ=4872 at HC=56.
  This is finite evidence, not a polylogarithmic theorem or a refutation of Cor 2.3.

## Required fixes, in priority order

1. **Narrow §5 and the §§0/2.2 interpretation.** Replace the proposed necessity of non-polylogarithmic μ with an explicitly
   open question over the entire allowed c-window. Include the 76/101 sensitivity result; the existing minimum-HC caveat
   does not make the stronger conclusion follow. The logarithmic smoothness obstruction kills neither polylogarithmic
   moduli nor every pointwise congruence-based approach. Say “no method found here,” not a proved impossibility.
2. **Do not promote target equivalence to ordinary ES.** HC finiteness implies ES; ordinary ES's converse to this
   particular certificate family is not proved here. “ES-sufficient coordinate-constrained target” is the safe formulation.
3. **Repair §1's unit-group wording.** For example p=17,c=68 gives `p+c=85` with a nonunit prime factor 17 modulo 68.
   Say “use only prime factors coprime to c,” or restrict the search to `c<p` using UPPER L1.2.
4. **Qualify E4.2's causal wording.** Decreasing maxima are compatible with shrinking samples; they do not demonstrably
   “follow” from sample size when both the family and height also change. Keep model projections explicitly heuristic.

After these fixes: accept the proofs, finite census and descriptive evidence; the pointwise target is **inconclusive**, not dead.

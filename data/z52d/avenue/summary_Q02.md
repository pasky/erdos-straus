# z52d avenue — batch Q02 (113 items) summary
ES is OPEN. Rows: `out_Q02.jsonl` (labels are Assessments unless a PROVED/CERTIFIED source is cited). 70 rows are calibration only.
**Status × plausibility** (columns: plausibility 0/1/2/3)
| status | 0 | 1 | 2 | 3 | Σ |
|---|---|---|---|---|---|
| known-true | 0 | 0 | 1 | 48 | 49 |
| circular | 23 | 0 | 0 | 0 | 23 |
| known-false | 19 | 1 | 0 | 1 | 21 |
| open-plausible | 0 | 2 | 6 | 4 | 12 |
| unclear | 2 | 6 | 0 | 0 | 8 |
Novelty: 0 → 67, 1 → 42, 2 → 4 (Z1337, Z1877, Z2854, Z0212). Plaus-3 rows are calibration lemmas (yield none), not ES routes.

**Plausibility ≥ 2 AND novelty ≥ 1**: 21 rows, **all with yield none** (calibration). The ones worth keeping:
* **Z2086**: *Σ_{p≤X, p≡1 (Q)} R(p) ~ F(Q)·ΣM(p)* (Titchmarsh-divisor-type, in APs) ⇒ R(p) ≤ (1−c)M_BM(p) i.o.: a provable lower deviation, twin of Linnik's upper one.
* **Z0212**: *every prime with an ES solution having 4 | some denominator has an all-even (8/p) solution* (failure sets agree, {17, 241} < 2·10⁴).
* **Z0728 / Z0892–Z0894**: *local factor F (RESIDUE_HARDNESS) explains numerator-20 and FF 'p ≡ 1 mod smooth'/pseudosquare depressions* (main term, B3).
* Others: Z1877, Z0138, Z0128, Z0306, Z0115, Z0285 (proved below), Z0752, Z2483, Z2775, Z1731, Z1322, Z2266, Z2864, Z0241, Z0355.
No row yields a new proof architecture for ES; the only ES-yield rows open at all are Z0148 (one-coordinate window J(p) ≪ (log p)^A = FRONTIER §7.2,
plaus 1) and Z1934's growing-level identity cell ((J)10, plaus 1).
**Recurring missing theorems**
1. *Strictly stronger sub-world lottery / union of lines* (circular): Z0147, Z0202, Z0201, Z0726, Z0260, Z0109, Z0743, Z0744, Z0875, Z3107, Z0113, Z0729, Z0123. 2. *Exact restatement of the tied divisor event* (group ring, theta quotient, numerator set): Z1098, Z3057 (= P03 Z3003), Z1989, Z0107, Z0140, Z0264, Z0104. 3. *Signed / positivity transfer*: Z0128, Z0306, Z0307, Z0639, Z1940 (trivial identities); Z0308, Z1152, Z2334 (no signed→positive move). 4. *Forcing the class by reciprocity / Chebotarev / subset products* (parity, never class): Z1051, Z1479, Z1315, Z2773.
5. *T1 kills every periodic or fixed-level exact count*: Z1934, Z1935, Z0108. 6. *Size*: Z1941, Z0201, Z0138, Z0241 (max > p^{3/2}/2).
7. *FF results do not transfer* (density, char 2, Chebotarev): Z0206, Z0296, Z0477, Z2498, Z2576, Z2577, Z2627, Z3175, Z0301, Z0302, Z0892–Z0894.
8. *Numerator ladder / blindness*: Z0120, Z0121, Z0122, Z0214, Z0729, Z0752, Z0242, Z0014, Z0149. 9. *Bounded search windows*: Z1784 (false), Z1942, Z0148.
**New in this pass** (scripts `scripts/z52d_avenue_Q02_*.py`, timeout ≤ 120 s, ulimit 4 GB)
* Z0113 (`_lcm.py`): lcm world = branch (ii) [k ≡ −p (4), m | p+k, m ≡ −1 (k)] ∪ Type I branch (iv). Branch (ii) fails ≤ 10⁶ exactly at
  {193, 2521, 66529} = the López b = 1 failure set; (iv) rescues 193, 66529, not 2521 ⇒ lcm world fails ≤ 10⁶ only at 2521 (one engine; matches the stored census < 2·10⁴).
* Z1877 (`_mult.py`, PROVED): (1+1/x)(1+1/y)(1+1/z) = 1+4/n is solvable for every odd n by explicit identities (x = ⌈n/4⌉, w ∈ {1,2,3}),
  odd squares included — no T1. Pass 1's "397/400 failures" was a search-bound artefact.
* Z1935 (PROVED): a signed count |S| ≤ R depending only on n mod M vanishes on every Mordell-hard class (they contain odd squares).
* Z0108 (PROVED): a uniform identity m(p)/p with 4 | m(p) on a square class would give a square-class identity for 4/p — Schinzel forbids it.
* Z0138 (PROVED): 4/p as 4 distinct unit fractions with max ≤ C·p is impossible for p ≫_C 1 (p-adic valuation); natural scale ≳ p^{5/4}.
* Z0212 (`_twoadic.py`, PROVED lemma): every solution has v₂-profile a₁ = a₂ > a₃; existence-level 8/p ⟺ "4 | some" holds for p < 2000.
* Z0128: 4/p = 1/x + 1/y − 1/z with x = (p+3)/4, y = (px−1)/3, z = pxy (p ≡ 1 (12)), so z ≍ p⁴ by a fixed identity.
* Z1941: Pass 1 data give min_p (min-max)/p^{3/2} = 0.511 ≥ ½ (HARDNESS_MAP bound) but unbounded above (15.9 at 4049): K·p^{3/2} worlds are bounded-mean lotteries.
**Corrections to inputs**: Z1877 (Pass 1 bounded search), Z0107/Z0140 ("multiple of 4 in M(p)" is not a weakening: divisor closure),
Z0206 (FF fixed-P counts are Chebotarev statistics, not Katz–Sarnak), Z1337 (Furstenberg/Kotani are almost-sure, not every-realisation),
Z0477 (large q does not even give FF ES pointwise), Z1941 (slope-0.54 question settled by the p^{3/2}/2 bound).
**Assessment.** Q02 is the calibration end of the queue, as expected. Nothing escapes B2 / T1 / B-fin. The useful outputs are several small,
proved lemmas that close items cleanly (Z1877, Z1935, Z0108, Z0138, Z0113), plus one proof-shaped calibration theorem worth a short lane: Z2086.

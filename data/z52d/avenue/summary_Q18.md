# z52d avenue — batch Q18 (113 items) summary
ES is OPEN. Rows: `out_Q18.jsonl`. Per-row labels are Assessments unless they cite a PROVED/CERTIFIED source. This was a non-proof-attempt
batch, mostly the external-problem catalog (Z0408–Z0675): 86 rows are "calibration only", handled briefly.
**Status × plausibility** (rows: status; columns: plausibility 0/1/2/3)
| status | 0 | 1 | 2 | 3 | Σ |
|---|---|---|---|---|---|
| known-true (gap named / calibration fact) | 0 | 0 | 0 | 84 | 84 |
| circular | 9 | 0 | 0 | 0 | 9 |
| known-false | 8 | 0 | 0 | 0 | 8 |
| unclear | 3 | 3 | 0 | 0 | 6 |
| open-plausible | 0 | 3 | 1 | 0 | 4 |
| harder-than-open | 2 | 0 | 0 | 0 | 2 |
Novelty: 0 → 98, 1 → 15, 2 → 0. Plaus-3 rows are calibration facts (yield none), except Z0537 (thin families), Z0604 (ES *conditional on*
H⁻_BM; the main term is PROVED) and Z0633 (the known 3/4 exceptional-set bound).
**Plausibility ≥ 2 AND novelty ≥ 1** (none has an ES yield):
* Z0500: *Ford-type divisor-range local laws model the fluctuations of R(p)* (variance model only). Z0513: *Crocker/Pan exceptions to p + 2^a + 2^b
  are covering-structured*. Z0587: *the ES surface is not hyperbolic, so Darmon–Granville-type finiteness does not apply.* Z0588: *Campana-point
  counts on cubic surfaces are height averages* (B6).
Nearest to a lane (nov 0): **Z0669** (plaus 2), *Haar survival of the residue model decays like exp(−c log³X)*, which gives CRT
exceptional-set bounds at best (capped at 3/4). **Z0537** (plaus 3): Aurifeuillean identities, bases 3, 5, 6, 7, vs the open families of FRONTIER §7.8.
**Recurring missing theorems**
1. *Forced-class divisors must still divide the tied integer* (circular for p > 8 813 281; ℓ = 4Ck − 1 | 4Cp + 1 ⟺ ℓ | p + k): Z0430, Z0431,
   Z0432, Z0498 (sub-products = divisor condition), Z0408 (Stewart form; squares force exactly ker χ_{−4C}).
2. *Rational/Heegner/parity-forced points* (rational ≠ integral; B3): Z0423, Z0424, Z0425; norm/binary-form certificates Z0593 ((J)3).
3. *Pointwise lower tail* (H⁻_BM-type, circular): Z0670, Z0683, Z0773, Z0604 (singular series = M_BM, gap = H⁻_BM), Z0414 (ES₅).
4. *Bounded/congruence procedures* (B1, known-false): Z0440, Z0561, Z0573, Z0649, Z1231, Z0443 (pigeonhole, B4); Z0631 is the infinite
   covering, i.e. ES restated.
5. *Averages / density machinery* (B6): Z0418, Z0421, Z0499, Z0502, Z0572 (finite Dirichlet polynomial at fixed p), Z0588, Z0602.
**New in this pass** (script `scripts/z52d_avenue_Q18_sizes.py`, p < 2000; EVIDENCE)
* **Z0624 correction**: "all positive ES solutions are ≪ n²" is false. Max z reaches p^{3.6} (p = 1999), with z ≍ p⁴/16 at p ≡ 3 (4).
  The least achievable max denominator is ≤ 0.503 p² for p < 2000, largest at 577. With Q03 Z0644's lower bound p^{3/2}/2 (PROVED), the
  dividing line lies in k ∈ [3/2, 2] for this range. "Some solution ≤ C·p²" implies ES, but equivalence with ES is not known (Z0511).
  (★) solutions alone have max denominator ≤ p(p + 1)/3.
* **Z0498** (PROVED, elementary): for 4C | 24, (ℤ/4C)^× is an elementary 2-group. So 4Cp + 1 has a divisor ≡ −1 (mod 4C) iff −1 lies in the
  span of its prime-factor classes. This corrects Pass 1's "not a constraint". Davenport-type bounds force the identity, not the target −1.
* **Z0512/Z0590** (Assessment): Crocker-type failures need *forced compositeness*, which covering congruences supply. ES failures need *forced
  confinement* of divisors, and congruences supply that only for finitely many slices (the Dickson "n = 1 shadow").
* **Z0441**: R(p) is always even, so its parity is useless. An M5 route needs an involution whose fixed-point count sees (·/p).
**Corrections.** (★)-universal rows (Z0408, Z0430, Z0498) now read p > 8 813 281 ((★) fails at 577, where ES holds). Z0573 (only congruence parts are Chebotarev); Z0582 (premise refuted).
**Assessment.** Q18 is calibration. Every pointwise mechanism in the catalog uses an M1–M5 input that ES lacks, or reduces to the tied-divisor event.

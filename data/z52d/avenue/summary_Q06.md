# z52d avenue — batch Q06 (113 items) summary
ES is OPEN. Rows: `out_Q06.jsonl`. Per-row labels are Assessments unless they cite a PROVED/CERTIFIED source. This was a non-proof-attempt
batch: 31 rows are "calibration only" (L-value/τ correlations, distribution statistics), and many more are class-group/quaternion/form "templates".

**Status × plausibility** (rows: status; columns: plausibility 0/1/2/3)
| status | 0 | 1 | 2 | 3 | Σ |
|---|---|---|---|---|---|
| known-false | 36 | 0 | 0 | 0 | 36 |
| circular | 27 | 0 | 0 | 0 | 27 |
| known-true (gap named) | 0 | 0 | 0 | 23 | 23 |
| unclear | 15 | 2 | 0 | 0 | 17 |
| open-plausible | 0 | 5 | 2 | 0 | 7 |
| harder-than-open (GLH-beyond / Chowla / GRH ⇒ ES) | 3 | 0 | 0 | 0 | 3 |
Novelty: 0 → 60, 1 → 50, 2 → 3 (Z3181, Z0332 calibration; Z0483 Siegel-zero dichotomy, plaus 0). All plaus-3 rows have yield none or average-only.

**Plausibility ≥ 2 AND novelty ≥ 1**: none has ES yield.
* **Z0652** (plaus 2, barrier-side): *for every κ < 1/3, infinitely many Mordell-hard p have least witness > exp((log p)^κ)*. This sharpens H4_NOT_POLYLOG (κ < 1/12, or 1/6 rel. (G)) and OMEGA13 (1/4). It fixes the scale a proof must reach and gives nothing toward ES.
* **Z3188** (plaus 2): 2/3-adic equidistribution of minimal certificates. Average statement only (B6).
* Calibration lemmas, yield none: Z2863 (2-adic local factor), Z2983 ((6/p) = the p ≡ 1 (24) interaction, RESIDUE_HARDNESS), Z0025, Z0278,
  Z0347, Z0699/Z0789 (shift correlations = trial-form u-lines), Z0738 (p ± 1 smooth enrichment of m/p failures; p + 1 half possibly a new main-term axis).

**Recurring missing theorems**
1. *Quaternion/CM/supersingular side is congruence data* (QUATERNION_ES Props 2.2, 5.1): Z2741, Z2821, Z2831, Z2843, Z2922, Z3029, Z3055, Z3074, Z3172.
2. *Representation theorem / one-class genus closes ES* (POINTWISE_TERNARY Thm 4.1, T1): Z2912, Z2914, Z2925, Z3075, Z3029, Z3048.
3. *Reciprocity/genus/Rédei pins the class* (parity only, CLASS_FORCING Thm 2.1): Z2739, Z2825, Z2881, Z3030, Z3119, Z3131, Z2824, Z3090, Z3094.
4. *Idoneal/Siegel finiteness for I3/U* (M1a absent: polylog count): Z2768, Z2769, Z0475; numerology variant Z3181.
5. *Polylog least witness / level*: the witness modulus W(p) is refuted i.o. (OMEGA13): Z0230, Z0379, Z0534(a). The open one-coordinate forms are
   HC(p) and E(p) (§7.2): Z0534(b), Z0284, Z0521, Z0539, Z0651. Union-of-growing-Chebotarev restatements: Z0658, Z0659, Z0667.
6. *Tied modulus defeats multiplicative/sieve/hyperbola machinery*: Z0532, Z0547, Z0553, Z0660, Z2968, Z2997, Z0211 (§7.1).
7. *Privacy across levels/windows*: Z2951, Z2967, Z3112, Z0542, Z3142 (union of lines, = out_P00 #2).
8. *Main term only* (BM_LVALUE T ∝ L(1,χ_p)², RESIDUE_HARDNESS F): Z2930, Z0690, Z0698, Z0763, Z0827, Z0879, Z0886, Z0905.

**New in this pass** (scripts `scripts/z52d_avenue_Q06_*.py`, timeout ≤ 120)
* **Z2967**: Pass 1's 45 'rational relations' among divisor-class indicators (C ≤ 12, p < 2000) are exactly trivial: F(a) = F(a⁻¹) (34 inverse pairs,
  N ≡ 1 mod 4C) plus F(1) = 1 (11). The 80 non-trivial columns have full rank (`…_annihilator.py`). There are no annihilator relations.
* **Z0803 correction**: '(★)-zeros have small h(−4p)' (13/14 below median) is conditioning on p mod 8 only. The zeros are ≡ 1 (3), which forces
  χ_{−4p}(3) = −1. Against p ≡ 1 (24) neighbours the mean quantile is 0.53 (6/14), i.e. null (`…_hzeros.py`).
* **Z0542**: a prime N_C = 4Cp + 1 is a certain failure (its divisors are ≡ 1 mod 4C), so Maynard–Tao/almost-prime forcing works against ES.
* **Z2870**: for t | 24 ((ℤ/t)^× of exponent 2), level-t failure ⟺ −1 ∉ span of the prime-factor classes, a Landau-type norm condition. This is where M2 lives in ES.
* **Z0379**: 'W(p) ≤ C·ℓ(p)^κ' is refuted under GRH (ℓ ≤ 2 log²p) by OMEGA13. Pass 1's data agree.
* **Z0284**: polylog E(p) (least e-slice) is NOT excluded by OMEGA13, which bounds M = 4uC − 1 ≈ p/e, the opposite direction. It is an open one-coordinate target.
* **Z0905**: L-value tails move M_BM by ≤ 8 % (BM_LVALUE: M_BM ≥ 0.9225·M₀ at p ≡ 1 (8)), so the left tail of R is not an L-value effect.

**Corrections.** Z3030: Pass 1's d = 1 zero is the mod-4 parity exclusion ((J)89 Lemma 4.1), not T1. Z2967 and Z0803 as above.
Z0475: the U sporadic list exists ({105, 2961, 3985, 25305, 111969, 978145}), and Pass 1 misread it. Z0539: the 4 'no C ≤ 200' primes are (★) zeros.

**Assessment.** Q06 is dominated by class-group, quaternion and quadratic-form templates (Gauss, Lagrange, Duke, Gross–Zagier, idoneal). All of them
collapse onto three proved facts: the order/genus side is congruence data, representation theorems are T1-blind, and reciprocity gives parity, not
class. No item supplies M1a or M2 at moving moduli. The only non-calibration plaus-2 row (Z0652) is barrier-side.

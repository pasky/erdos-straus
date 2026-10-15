# AGENT_REPORT_O226 — odd-r / odd-s absence explained; q = 9, k = 1 closed (checkpoint 1)

Main file: `FF_ODD_ABSENCE.md`. Scripts `scripts/zc_*`. Data/log `data/zc/` (certificate log `data/zc/certify9_k1.txt`).

**SHARP:** *a root-product (Weil-reciprocity) law*. Every k = 1 Case B tuple (m'wC = T^s + v, w + C = g'v) satisfies
**E(0)^s = ε(pattern) = ±1** (exact sign formula). Every k = 1 Case A datum satisfies E(0)^{2α} = 1. The proof is ten lines:
evaluate the two equations at the roots of v, w and m' and multiply (Lemma 1.1, valid over any field). So the slice u₀ = −E(0)
can carry a level-n family only if ord(−u₀) ∣ 2n. This explains O220's SHARP exactly: q = 27 has nothing off F₃^* below level 13
(and at s = 13 all 24 classes appear), and q = 9 has nothing at odd s. Bonus (Cor 1.7): the same identity gives a **pattern parity
law for k ≥ 2** (w₁(0) = −C₁(0) makes the law a parity condition on (s, a, z, t)). About 74% of the patterns are empty: the archived
exact q = 9 counts have 0 tuples in all 5 210 violating patterns. The route-bound sums drop by a factor ≈ 4 (q = 3: 1466.7 → 389.2;
q = 9: 41.9 → 11.2). No Galois descent is involved: the F₃ flavour comes only from the leading coefficients ±1.

## Results
1. **Lemma 1.1 / Thm 1.2 / Thm 1.4 / Cor 1.5 (PROVED):** the law and the vanishing theorem. The scope: a family of level n can
   lie on slice u₀ only if u₀^{2n} = 1 and u₀ ≠ 1. For Case B the sign is pinned down further: (−u₀)^s = ε(s; a, z, t).
   Checks: the exact sign formula was tested on all dumped tuples (q = 9, s ≤ 12: 8 915 tuples; q = 5, 7, 27, s ≤ 9) with 0
   failures, using an independent Python re-verification of each tuple. The Case A law was checked on q = 9 (α ≤ 6) and q = 27
   (α ≤ 4) data. An independent brute force (`zc_brute.py`, q = 9, s ≤ 5) found 0 failures.
2. **Prop 1.6 (PROVED, sharpness):** for any monic D ∣ T^s + 1 of positive degree < s with D(0) ≠ −1, the tuple
   (m', w, C, g') = (D + 1, 1, (T^s + 1)/D, 1) is a level-s tuple with E(0) = D(0). So every u₀ with u₀^s = −1 is populated at
   level s. EVIDENCE that all classes allowed by the law are populated: q = 9 for s ≤ 12, and q = 27 at s = 13.
3. **Theorem 2.2 (PROVED, computer-assisted, O216 standard): q = 9, A = T has no finite linear covering.** This closes the last
   open k = 1 case (r = 2). With (J)56 Thm 8.1, ES_q(T) has no finite linear covering for every q = 3^r, r ≥ 2.
   - **Method:** union bound restricted to the 4 primitive slices P₈ (u₀⁴ = −1). There only levels with 4 ∣ n survive, and for
     Case B only patterns with ε = (−1)^{s/4}.
   - **Exact P₈ counts** for s = 4, 8, 12, 16, 20 give mass 1.75996. At s = 20, 17 of the 950 patterns timed out and are
     bounded by routes instead (0.099).
   - **Route bounds** for s = 24..80 add 1.108. The tail beyond s = 80 is ≤ 0.0258, and Case A (4 ∣ α) is ≤ 0.1705.
   - **Certified total** ×1.01 = **3.195 < 4** (`scripts/zc_certify9.sh`, fails closed; `zc_certify9.sh 1` regenerates
     s ≤ 16 and the Case A input byte-identically).
   - **Why the ±i slices were not used:** they carry an exact mass of 2.17 over 2 slices, which is more than 1 per slice, so a
     union bound cannot work there. The primitive slices carry 0.44 per slice.
4. **Goal (3):** already done before this task — (J)56 §8 (Lemma 7.4, Thm 8.1) covers every r ≥ 20, and the helpers take q as a
   float. Nothing further was needed.

## Trust points for the reviewer
- **The sign formula ε.** It is used to filter patterns, both in `zc_sum9.c` (`eps_ok`) and in `zc_enum.c` (`zc_eps_ok`). The
  proof is Lemma 1.1, and it is checked on the data. In addition, s = 16 with the filter off puts 0 P₈-tuples in all 514
  incompatible patterns.
- **The slice filter** `SLICEF == 2` (E(0)⁴ ≠ 1) and the mult-2 orientation for a < b. The swap maps E(0) ↦ 1/E(0), and P₈ is
  closed under inversion.
- **The Case A filter** 4 ∣ α in `zc_caseA9.py`, justified by Thm 1.4. The proof needs a check that lc(z) ∈ F₃^*: in the
  cancellation case the exponent of λ is 0.
- **Cross-method agreement** of exact counts: s = 12 has 214 of 237 patterns checked against the candidate-search routes, with 0
  mismatches; s = 16 has 85 of 215, also 0 mismatches. The s = 20 counts rest on the O220 enumerator (validated by O220 and R221)
  and are not cross-checked independently.
  The s = 20 exact mass is 8·10⁻⁵ against its bound of 2.9, so it matters only through the claim that the count is complete.

## Compute
About 2 h on ≤ 2 cores. The s = 20 per-pattern runs took about 40 min.

## Sparks
* **ℤ-analogue (goal 4):** the law is a reciprocity statement in μ_{q−1}. Over ℚ only μ₂ survives, so the ℤ analogue is a
  Jacobi-symbol constraint — essentially the classical Mordell quadratic-residue obstructions. I expect nothing new at the
  E(0)-level. The *pattern parity law* (Cor 1.7) might have an ℤ shadow, though: a sign/parity relation between the "degree
  pattern" (sizes of the factors) of a Type II solution and the residue class of p, through the Hilbert product formula at ∞
  and 2. Lemma 1.1 applies verbatim over ℚ[n], so polynomial ES identities of shape (R) must have W(0)/C(0) = ±1 at n = 0.
  That may be a cheap check against the polynomial-identity literature.
* Feed Cor 1.7 into the k ≥ 2 certificates (Thm 5.2 q = 9: 3.58 → smaller; q = 3 s₀ 84 → 74). It does not close q = 3, where
  union bounds fail even with exact counts.
* Higher laws: the root-product trick works for any relation where the defining equations make every local symbol a power
  of T. Variants with T^s replaced by T^s·u(T) (deeper digits of the slice point) might constrain the second T-adic digit
  as well, which would cut cylinders inside a slice.
* The ±i slices at q = 9 carry an exact mass > 1 per slice: they might be genuinely covered by finitely many families. If so,
  that would be a k = 1 "partial covering" phenomenon worth deciding.

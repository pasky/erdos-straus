# O275 independent self-review record

This is the author's record of the independent `functions.review` result on commits `9b2a9cc8..dbb88f9b`, not a newly solicited parent hostile review.

**Reviewer verdict:** sound, with small fixes needed; no mathematical errors found in Lemmas 2.1/2.2, Theorems 3.1/3.2/5.1, Lemma 4.1 or Proposition 4.2. Every census figure reproduced. No ES theorem is claimed.

## Independent checks reported

- Both committed scripts rerun with 8 GB virtual-memory limit, timeout and one core. C census to 10^6: about 3 seconds, peak 97 MB; exact agreement with the report.
- Separate temporary code recomputed component failures through p≤13,000.
- Eight four-form fixtures reproduced; least-non-residue isolation checked in five fixtures.
- Theorem 3.2 checked at H=6, M=840, p=5516281 and 18164161: roots 4–6 isolated, eight-vertex residue component at 1.
- Proposition 4.2 checked on path (1,2,17,257,4129,33289) at a prime near 2·10^13.

These additional fixtures are reviewer-reported, not outputs of the committed scripts.

## Comments and disposition

1. **Missing attribution / novelty scope:** accepted. SIGN_IDENTITY Lemma 1.1 already contains the endpoint encoding, sign identity and size bound; CONSTRUCTIVE_ES Prop 4.1(c) contains the prime sign case. Added citations and limited novelty wording to unique-parent / forest structure. Mentioned DEDEKIND_ES's related Farey graph.
2. **Alleged smaller-neighbour gap in Theorem 3.2:** no mathematical gap: the displayed classification of *every* divisor v=d or dL_i already includes smaller neighbours, with L_i>H+1. Added this explicitly, including i−1∤i+1, to remove ambiguity.
3. **Composite-n units:** accepted clarification. The bichromatic iff statement is explicitly restricted to unit-endpoint edges; it covers every relevant edge at primes p>3, not all composite certificates.
4. **Enumeration wording:** AP and SPF enumeration are distinct algorithms using a common exact predicate. Clarified this rather than implying wholly independent arithmetic formulations. The Python residue-parent check is a third formulation on the stated smaller range.
5. **Minor wording:** changed the C cutoff from “exact” to “necessary”; defined T1; made the admissibility ℓ≥13 range explicit. Maximum depth was already labelled as over all selected inputs, not just p≡1 mod4.

No substantive theorem was withdrawn or strengthened during repairs. Parent hostile review remains pending.

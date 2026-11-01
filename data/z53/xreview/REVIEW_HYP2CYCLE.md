# Z53 HYP2CYCLE — independent hostile review

**Verdict: ACCEPT-WITH-FIXES.** The strengthened sufficient condition survives: Theorem R really proves MIX ⇒ R2′ ⇒ R2.
The numerical evidence supports square-root scale, not literal MIX(1/2). The determinant-method closure must remain a
statement about the evaluated black-box bound, not an impossibility theorem for the method. ES remains OPEN.

Reviewed: `side-agent/z53-hyp2cycle`, commit `9a9d214ef1ca95ee533f620bd8563a9e0fd235af`, `Z53_HYP2CYCLE.md`.
All shell executions had memory/CPU limits and wall-clock timeouts; computations used at most a 6,000,000-KiB address-space limit.

## Per-claim audit

| Claim | Classification | Independent derivation / qualification |
|---|---|---|
| Definitions, N(U,U)=2N₄, N₂≤U/2 | CORRECT | At primes, a common divisor of u,B divides p and is <p; hence gcd=1, the two divisibilities imply product divisibility, and cycles are disjoint. |
| Lemma B | CORRECT | Both odd forces odd k. For u=2ᵃu′ even, B odd, v₂(k)≥2 iff p+u+B≡0 mod 2ᵃ⁺²; the odd part of 4u is already imposed by f. The lift modulo 4u is unique. |
| Proposition C(a,b) | CORRECT | Möbius expansion gives local factor (1+1/(ℓ(ℓ−1)))²−1/(ℓ−1)²=1+ℓ⁻². Thus M₂→15(log 2)²/(2π²). Restricting both coordinates odd changes the 2-factor from 5/4 to 1/4. Uniform allowed k mod 4 gives M₄/M₂→1/5. |
| Proposition C(c) | CORRECT | Both-odd pairs have slice probability 1 or 1/2 according to their odd classes; mixed pairs have probability 1 or 1/2 according to whether the even vertex is 0 or 2 mod 4. Equal limiting subweights give 3/4. These are model asymptotics, not identities of actual N-counts. |
| Proposition C′ | CORRECT | A B=n+u implies (A/n)=(u/n)(B/n) at unit endpoints. DK's sign polynomial gives −1 for the five slices when n≡1 mod 4, +1 when n≡3 mod 4. Independently reran all 160 latter cells and 283,977 words. For k=1, collapse [[B,1,u]] to [[B−1,u−1]]; the same Dedekind expression survives. |
| Proposition S | CORRECT-WITH-FIX | m≡a mod q, m≡1 mod q+1 gives q(q+1)∣m²+2q+1; the displayed size inequalities hold for q≥13. Replace “every unit is a square mod n” by “every unit has Jacobi symbol +1 at square n.” A is a unit by (ku−1)(kB−1)=kn+1, so DK applies without assuming unit endpoints. |
| Lemma A | CORRECT | k>4U makes the sum s=u+B the unique residue −n mod k. Its product is (n+s)/k; the positive-square discriminant recovers the unique distinct unordered pair. The sufficient n≥16U³ condition and n≥2¹⁶ specialization check out. |
| §3 CF/matrix/strip dictionary | CORRECT-WITH-FIX | Determinant is 1 by direct multiplication; sum/product give the strip. HJ length 3 presupposes k≥2, automatic at the large fourth-root scale, not for every allowed U. E.g. p=11,U=3,{4,5} has k=1. State this restriction for the HJ dictionary. |
| §3 fixed-difference identity | WRONG for general odd n | n=15,U=6,u=9,B=12 satisfies u∣n+3 and B∣n−3, but uB=108∤36=n+u+B, so it is not counted by N₂. Restrict to primes, or retain the product-divisibility filter. |
| Lemma G | CORRECT | B=r or u+r, r=uθᵤ. For B<u, {u/B}=1/θᵤ−1; for B>u it is 1/(1+θᵤ). Equality to θ_B is exactly the return congruence. See proof audit below. |
| Theorem R | CORRECT | Nonnegative smooth tube majorant, bounded h₂=0 marginal, summable high-frequency tails and O(U³ε/δ²) retained coefficients give precisely the displayed estimate. No first-order cancellation is smuggled in. |
| MIX corollary | CORRECT-WITH-FIX in formulation | With 0<η≤1 and ε<η/8, δ=U⁻η/² is allowed and H≤U^η eventually; substitution gives U¹⁻η/²⁺³ε. For R2, explicitly quantify MIX uniformly over all large primes and the chosen fourth-root-scale interval. |
| Proposition D arithmetic | CORRECT-WITH-FIX | T=V, including translations because the polynomial remains multi-affine, not merely T≥V as the proof says. Then b₁b₂b₃/(b₁+b₂+b₃)≥b_min²/3. HB14 gives `V^{2/(3√3)} ≥ B_min^{2/√3}`. These lower bounds concern the displayed upper-bound expressions only. |
| Proposition D “closed”, subdivisions | GAP at the broadest reading | The grid calculation charges every ambient subbox. It proves that this full-grid, uniform per-curve-bound implementation gives no power saving; it does not rule out occupancy pruning, exploiting auxiliary curves, or other uses of the same theorem. Scope the conclusion accordingly. |
| §6 upper-bound / ES facts | CORRECT | An upper bound alone permits N₄=0; a constant model mean <1 supplies no positivity. Improving only the fourth-root block does not lower the cube-block p¹/³ global benchmark. “ES-inert” should mean no standalone implication, not no possible indirect use. |
| §4/§5 empirical dynamics and MIX | EVIDENCE, reproduced | Finite statistics are consistent with the CRT model and square-root-size sums. They neither prove a random-map law nor N₂=p^o(1); the latter remains conjectural. |

For C's error term, absolute inner-sum errors are bounded using Σ_{d≤X}μ²(d)/φ(d)≪log X and
Σ_d μ²(d)/(φ(d)[d,e])≪1/φ(e) for squarefree e. Summing e gives O(log²U/U); the omitted lcm tails are
O(log³U/U) by grouping squarefree lcms and their multiplicative divisor weights. No prime-counting theorem enters.

## Hardest check: Theorem R / MIX

1. At a prime, every domain vertex and its image are nondivisors, so Lemma G's hypotheses hold. The majorant only needs
   the true-cycle ⇒ graph implication. The asserted union identity also holds: a wrong-branch hit would force r∣u² or
   u+r∣ur with gcd(r,u)=1, impossible on the relevant intervals. Independent exact-rational checks: 8,826 (p,U) cases,
   123,264 domain vertices, 3,788 returning vertices; zero mismatches.
2. Periodization/unfolding gives χ̂(h)=δ ψ̂(δh₂)ΣⱼJⱼ(h), |χ̂|≤10δ. The h₂=0 terms must be summed as a function:
   Σᵤχ₀(θᵤ)≤12δU. Bounding these Fourier terms by a small Weyl-sum hypothesis would have been invalid; the memo does not.
3. Put L=U^ε/δ. Nonstationary integration by parts plus the O(1+|h₂|) central frequencies gives
   Σ_h₁|Jⱼ(h)|≪1+|h₂|. Therefore the |h₂|>L tail, including |W|≤U, is
   O_M(U δ⁻¹ U⁻ε(M−2)), hence O(U⁻A) since δ⁻¹≤U and M is freely chosen.
   For |h₂|≤L, the tail |h₁|>U^ε(14|h₂|+1) is
   O_M(U δ L² U⁻ε(M−1)), also O(U⁻A). This fills in the memo's compressed summation argument.
4. The remaining frequency count is O(U³ε δ⁻²), all inside H=15U²ε/δ; multiplying by 10δ proves R.
   Thus *any uniform power saving* suffices. This is not a claim that MIX is proved or logically weaker than R1.
5. The summary's “both coordinates lie in (1/f(u))ℤ” is false: p=17,U=2,u=3,B=4 has θᵤ=1/3.
   Lemma G correctly says θ_B and Γⱼ(θᵤ), the two sides of its equality, lie in (1/B)ℤ.

## Recomputations and sources

- Fresh compiled exhaustive run on [5,4·10⁹): **189,961,810 primes, max N₂=7, max N₄=5**. Both full histograms agree
  exactly with the sum of the three stored ranges; no reliance on sampling for these maxima.
- Existing independent `brute.py`: **59,959 cases, zero mismatches**. Additional independent product counts agree with
  all first 3,000 stored rows at each of 10⁸ and 10¹². The 1,124-square family rerun agrees byte-for-byte with stored data.
- Fresh model U=1000: EN₂=0.36493, EN₄=0.07297, EN₃=0.09235, E|dom f|/U=0.69316. Pair moments U=200 reproduce
  dispersion 0.9882 (N₂), 1.0113 (N₄). These agree with the memo's rounded numbers.
- Fresh full-frequency C runs reproduce both H=100 rows at 10¹⁶ and the H=180 row at 10¹⁸ byte-for-byte.
  Independently reducing phases modulo 1 in integer arithmetic reproduces the full H=32 grid at 10¹²+39 and the h₁=0
  columns at 10¹⁶+61 and 10¹⁸+3. Normalized maxima: **3.306734, 5.422897, 4.939039**; all agree with stored rounding.
- These maxima occur at (0,22), (0,94), (0,167), all within the actual √U cutoff. They equal **2.678250, 4.527064,
  4.109045 times √U**, respectively: literal constant-one MIX(1/2) fails at these inputs. This is not an asymptotic
  disproof of a big-O or smaller-exponent hypothesis, but “holds numerically” is not an accurate label.
- HB14 verified directly in [Heath-Brown, Annals 155, Theorem 14, p.562](https://arxiv.org/pdf/math/0405392), with
  coefficient-free T defined on p.555. The affine statement matches [Reuss's thesis, Theorem 2, pp.11–12](https://ora.ox.ac.uk/objects/uuid:5b49acc6-bc16-45bf-972a-6dff1977db02/files/mf4caf4ad1898f690a43918adec47f418).
  Thus the cited exponents and box hypotheses are confirmed, not merely copied from the memo.
- Reproducer: `scripts/z53_xrev_hyp2cycle_audit.py /tmp/xrev_HYP2CYCLE` via bounded `uv run --no-project`.
  Not independently rerun: every individual large-window scan row and every auxiliary control; no such certification claimed.

## Required fixes, in priority order

1. **MIX wording/quantifiers:** retain Theorem R, state a uniform asymptotic hypothesis with its constants and scale range.
   Remove “holds with η≈1/2 numerically.” Say “observed square-root scale; compatible with a conjectural uniform
   U¹/²⁺ᵒ⁽¹⁾ bound and hence MIX(η) for fixed η<1/2.” The U³/⁴⁺ε consequence needs the corresponding family of exponents.
2. **Determinant closure:** restrict to the black-box bound multiplied by a uniform per-curve bound, including the stated
   full-grid calculation. Replace the proposed FRONTIER phrase “certifies ≥… auxiliary curves” by “its stated upper-bound
   expression is ≥…”. Actual curves need not number that many. Repair translated T≥V to T=V using multi-affinity.
3. **Exact statements:** fix the summary denominator claim; restrict the fixed-difference identity to primes or add product
   divisibility; state k≥2 for the HJ dictionary; replace “every unit is a square” by the correct Jacobi statement.
4. **Labels:** change “true size p^o(1)” to conjectured size. Say the dynamics *matches tested CRT statistics*, not that a
   random-map law is established. Model ratios do not prove equal difficulty or equivalent bounds for N₂ and N₄.

With these fixes, **“narrowed, with one strengthened sufficient condition” is justified**: a valid new conditional
reduction, an unhelpful evaluated determinant bound, and useful finite-range/model checks—not an ES advance.

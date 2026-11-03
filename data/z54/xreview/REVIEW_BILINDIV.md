# Z54 BILINDIV — independent hostile review

**Verdict: ACCEPT-WITH-FIXES.** Theorem T and its conditional power saving survive. The algebra interpretation contains a false PROVED assertion; two peripheral scope/proof statements need repair. “Narrowed, with one new sufficient condition” is justified after those repairs, not a power saving or an ES result.

Reviewed `side-agent/z54-bilindiv` at `65e973656295bfd5fc51890e840a604d6ce2baa3`, not a moving branch. ES remains OPEN.

## Per-claim audit

| Claim | Classification | Independent derivation / qualification |
|---|---|---|
| §0 Lemma A; trivial bound | CORRECT | A solution has k=(p+u+B)/(uB)>4U, hence s=u+B is its unique residue in (2U,4U], m=uB and D=(B−u)². Conversely the two displayed roots recover the pair. One B per u follows from the residue class modulo u and interval length U<u; thus N₂≤U/2. |
| Lemma 3.1(a–d) | CORRECT | gcd(u,B) divides p and is <p, hence is 1; the two divisibilities imply product divisibility. Substitutions s=u+B, d=uB and B(ku−1)=p+u are reversible. Square-discriminant parity follows from D≡s² mod 4. |
| Lemma 3.1(e); fourth-root sizes | CORRECT | XY=kp+1 follows by multiplication. X≡−1 mod k forces Y≡−1 mod k. Positive k and X<Y recover u<B. Substituting U≍p^(1/4) gives every listed scale. |
| §3 rank-two identity; étale order; D=0 | CORRECT | αᾱ=m, α+ᾱ=s and km=p+s imply α(kᾱ−1)=p+ᾱ. The quotient is free of rank two; its rational algebra is étale iff D≠0 and nonreduced iff D=0. |
| §3 “A_k≅ℤ×ℤ exactly when D is a nonzero square” | WRONG | At p=100000037, U=100, k=5176, roots are 115 and 168, so D=53². Evaluation identifies A_k with {(a,b)∈ℤ²:a≡b mod 53}, an index-53 order, not ℤ². Fix: A_k⊗ℚ≅ℚ×ℚ iff D is a nonzero square; A_k≅ℤ² only for D=1. |
| Theorem T | CORRECT | Nonnegative χ majorizes integral w; absolute Fourier convergence permits interchange; h=0 contributes ≤4δE; paired frequencies contribute ≤8δ∑|T(h)|. Schwartz decay of order A+1 bounds the tail by C E(δH)^−A=C E U^−εA. |
| TD corollary | CORRECT-WITH-FIX | E≤∑τ(p+s)≪U^(1+ε/2). With δ=U^(−η+ρ), H=U^(η−ρ/2), the main and frequency terms are ≤U^(1−η+ε). Choose A≥(2η+ε)/ρ for the tail, or explicitly reduce to 0<ε≤1 before using the printed A≥4/ρ. Small U is absorbed into the constant. |
| Remark 4.1 small differences | CORRECT | u divides p+w, so each w contributes at most τ(p+w); summing gives W₀U^ε in the fourth-root range. Weighted Fourier majorization also works, with total weight replacing E; covering pieces must be nonnegative and dominate all remaining cycle levels. |
| §4.2 first-order, curvature, even modes | CORRECT | Substitution gives the displayed G_h. Twice differentiating W²=k²θ²−4θ−4p/k gives W″=−4(kp+1)/W³. Finally w=s−2u* and integral s give e(hw)=e(−2hu*). The intermediate-W analysis is explicitly not supplied. |
| Proposition 4.3 main inequality | CORRECT | Parseval supplies total squared mass ≫U. Nonstationary integration removes |ν|<hU. Constant-sign second derivative ≫hU³ gives |cν(k)|≪(hU³)^−1/2; thus maxν‖cν‖₂≪(hU)^−1/2. Dividing retained squared mass by this maximum yields ∑bν≫h^(1/2)U^(3/2), exactly under assumption (iii). |
| Proposition 4.3 reverse-order “trivial size ≍U” | GAP (limited) | The reverse triangle bound is exactly ∑φ(s_k/U), but no uniform lower bound ≫U for this weighted strip count is proved. The memo itself has only E≪U^(1+ε) and numerical/model sizes. Retain the exact identity; call ≍U a model size, not a proved obstruction for this reverse order. |
| Proposition 5.1(a) | CORRECT | Congruences recover the integral roots; kU<X≤2kU is equivalent on X≡−1 mod k to U<(X+1)/k≤2U because k>1. x≍p^(3/2), q=p give q≍x^(2/3), and both quoted error terms have size p^(1/2+ε). Fouvry–Iwaniec is genuinely an average over rs. |
| §5.2 divisor bound | CORRECT | Summing τ(p+s) over 2U integers and using p≍U⁴ gives E≪U^(1+ε). The Huxley direct-insertion discussion is not an impossibility theorem and is labelled Assessment. |
| Proposition 5.3 | CORRECT | θ∈(2/3,1), u∈(1.5U,2U] gives the claimed one-sided pairs. The fourth-derivative bound is Uλ^(1/14)+U^(3/4)λ^−(1/14), λ≍h/U. Erdős–Turán with H=U^(1/15) gives discrepancy O(U^−(1/15)). Cauchy–Schwarz and ∑τ²≪U^(1+ε) give the second assertion. |
| Proposition 5.4 | CORRECT-WITH-FIX | One point per u, B, k is valid for unordered Sol. Multi-affinity preserves T=∏B_i; ∏log B_i/∑log B_i≥(log B_min)²/3 gives the required exponential factor. But the translated coefficient norm need not exceed p; repair below. For short sides use the proof's piecewise X≥1, not the unjustified combined max expression unless boxes are padded to allowed radii. |
| Proposition 5.5 | CORRECT | Tangent/chord enclosure has area O(L/U+L³/U²), hence <1/2 for sufficiently small c and large U; three noncollinear lattice points are impossible. On a primitive line, s(t) is quadratic with leading coefficient −ab; subtracting the two superlevel lengths gives ≤2√(2U/(ab)), plus at most two integer endpoint errors. The square test has degree four, hence genus ≤1 componentwise. |
| Assessments, TD/MIX, verdict | CORRECT-WITH-FIX | TD remains explicitly conditional; no implication between TD and MIX, positivity, or global method impossibility is proved. Fixed-Q models, double dual and near-curve discussion are appropriately non-theorems. Remove the unsupported reverse-order ≍U assertion and keep all implementation restrictions in any FRONTIER text. |

## Required fixes, in priority order

1. **Correct the split-order assertion (§3 and review log).** Rational splitting is not integral splitting. For roots u<B, evaluation has image a≡b mod (B−u), index B−u. This error is not used in Theorem T, so it does not invalidate the sufficient condition.
2. **Repair the translated-height justification (§5.4).** Translating F at the memo's own solution (115,168,5176) gives coefficient norm 869567<p=100000037. For an integer translation (a,b,c), its quadratic coefficients include a,b,c and its constant is abc−a−b−p. If M is the coefficient norm, p≤M³+3M; since p≥16U³≥128, M≥3 and log M>1, which is all the comparison needs. Nonintegral centers can be handled by integer translation and bounded padding; keep constants consistent. State the short-side comparison piecewise.
3. **Scope the reverse-order conclusion (§4.3).** No cancellation after summing ν is an identity, not a lower bound for the weighted candidate count. Replace “trivial size ≍U” by the exact nonnegative sum and its proved upper bound O(U^(1+ε)); any ≍U claim is Assessment/EVIDENCE. The forward-order obstruction under (iii) remains proved.
4. **Make the corollary's epsilon convention explicit.** Either assume ε≤1 without loss, or choose the tail exponent depending on ε as in the table. This is a parameter-bookkeeping fix, not a loss in the result.

## Recomputations

All shell executions used `ulimit -v 6000000` (or stricter), a CPU limit, and an enclosing timeout ≤900 seconds. Original scripts were inspected before execution; geometry uses O(E) working storage, not an E×E array. Extraction and temporary outputs are in `/tmp/xrev_BILINDIV/`.

- Recompiled all three C programs; only misleading-indentation warnings occurred. Regenerated inputs using the supplied SymPy generator.
- **TD:** all 73 H=20 rows and all 16 extended rows agree exactly with stored output, including the three 10¹⁸ inputs. Their normalized maxima are 3.192, 2.386, 2.358 at H=178. These remain floating-point EVIDENCE, not certified uniform bounds.
- **Independent enumeration:** scanning m, rather than k, at p=1000000000177 gives E=2835, E⁺=1639, N₂=0. Direct evaluation of each Fourier mode, without the C recurrence, gives max/√E⁺=2.0607829964, RMS=1.2110136672, and |T(1)|/√E⁺=1.2272785412, agreeing at printed precision.
- **300 primes >10⁸:** reran both quadratic pair brute force and strip counting; zero mismatches in N₂ or N₄, ΣN₂=113.
- **Fixed-Q:** both full factorization runs agree: N_rel(1)=5253/4792, N_rel(27720)=3025/2803. All intermediate Q columns agree too.
- **Rich lines:** reran all 8000+4000 inputs; all 3654 nonempty output rows match. At U=316: cycles 292/2921 and 160/2921 versus controls 266/2469 and 159/2469 for richness ≥3 and ≥4. At U=1000: 69/1437 and 38/1437 versus 61/1185 and 36/1185. The stated percentages and conditioning are correct.
- **Geometry/anatomy spot check:** first 10¹² row reproduces L3=46, Lmax=W=10, P₁=A2=675, A1=357, cov3=197, direction (5,−11). Remaining full geometry rows were not rerun; no theorem relies on their exact ranges.
- Reproduction/assertion script: `scripts/z54_xrev_bilindiv_check.py`. Run after generating the original outputs in `rerun/`: `ulimit -v 6000000; ulimit -t 120; timeout 150s uv run python scripts/z54_xrev_bilindiv_check.py /tmp/xrev_BILINDIV`.

## Source checks and proof dependencies

- Read [Fouvry–Iwaniec, primary PDF](https://matwbn.icm.edu.pl/ksiazki/aa/aa61/aa6134.pdf), equations (3) and (5), Theorem 1. The memo quotes their restrictions and error correctly. Its bibliographic pagination should be 271–287, not 65–75.
- Read [Heath-Brown, arXiv:1601.04493v3](https://arxiv.org/pdf/1601.04493), p.1 equation (1), explicitly citing Titchmarsh 5.13. This verifies the exact classical fourth-derivative input used in Proposition 5.3, including its second term and derivative-ratio hypothesis.
- Read [Reuss's thesis](https://ora.ox.ac.uk/objects/uuid:5b49acc6-bc16-45bf-972a-6dff1977db02/files/mf4caf4ad1898f690a43918adec47f418), Theorem 2, p.12. It matches the HB15 restatement. The original CIME chapter was not checked; retain “relative to HB15 as restated.” Absolute irreducibility here follows since uB and u+B+p are coprime in the polynomial ring and F is linear in k.
- Proposition 4.3's integral bound can be derived without trusting a citation: split at |F′|≤√r, a set of length ≤2/√r when F″ has constant sign and |F″|≥r; integrate by parts on the two complementary intervals. Partial summation adds the fixed amplitude variation. This gives the required O(r^−1/2).
- Huxley/Ford/Shiu are not decisive inputs to the proved conclusions checked here; no new verification of their original papers is claimed. The memo appropriately does not use its unverified Shiu/near-curve quotations as theorems.

**Bottom line:** accept the Fourier reduction, anatomy lower bounds, forward-order restricted obstruction, and elementary geometry. Repair the false algebra statement and the limited height/scope issues before recording them as PROVED. The numerical evidence agrees; neither TD nor a balanced-block power saving is established.

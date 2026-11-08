# Retro cross-model review — Z65_LIFT (Astra)

**Verdict: ACCEPT-WITH-FIXES.** Theorem G, G_k, Prop O, the abelian ES application of Prop E, and Lemma S survive.
The blanket characteristic-p realisability claim and the inference from order transparency to a construction no-go do not.
ES remains OPEN. This independently reviews the merged memo at `311454873`, not merely the prior Opus recommendations.

## Sources and reproducibility
- Re-fetched `https://arxiv.org/pdf/2609.20572v1`; SHA-256 is identical to `data/z65/lift/src/swz.pdf`:
  `559f98c6c94aa80a4b7130c91784441f227de665c54463e71718592806e89316`.
- Read SWZ §§2–8 directly: EKS reduction, moment construction, new tail, Cartier-fixed central datum, alignment, lifting and quotient.
  This verifies the memo's extraction, not an independent certification of every theorem imported by this unrefereed paper.
- Checked Wewers `math_0205026.txt`: Thms 2–3, Lemma 1.4(3)(4), Cor 1.11, Defs 2.1, 2.7, 2.10;
  Obus `1208.3909.txt` §3, Lemmas 3.1–3.5 and Thm 3.6; `1703.01191.txt` Thm 1.15 and Prop 6.2;
  Hernández `1112.2425.txt` Thm 3.1. Source files are under `data/z65/lift/src/`.
- All shell executions used `ulimit -v 4000000` and timeouts ≤1800 s. Scratch output: `/tmp/xrev_retro_lift_astra/`.
- Original `z65_lift_goodred_check.py 1500 4`, `1500 8`, and `z65_lift_fpt_check.py`: byte-identical to committed outputs.
- New `scripts/xrev_retro_lift_astra_check.py`: independent direct-y enumeration, streaming triples, raw G2 tests rather than G3 shapes.
  Run with `timeout 300 uv run --no-project scripts/xrev_retro_lift_astra_check.py` under the memory limit. PASS.
- Re-ran `z64_equiv_orbifold.py 100000000`: same 15 sporadic odd n, none prime ≡1 (4); no r=5 odd n.

## Per-claim audit
| Claim | Classification | Independent check |
|---|---|---|
| Lemma A input: p≡1 (4) forces a triangle quotient | CORRECT | Riemann–Hurwitz excludes h≥1 and r≥6; r=4 reduces to a two-term fraction or the reproduced sporadic list; r=5 gives no odd n. A two-term 4/p requires p≡3 (4). |
| G0: extension and faithful special-fibre action | CORRECT | Genus≥2 gives the unique smooth minimal model. Equivariant H¹ specialisation plus Lefschetz excludes a nontrivial automorphism specialising to identity: its Lefschetz number cannot be 2−2g<0. |
| G1: exactly i(g) simple fixed points per residue disc | CORRECT | Weierstrass gives a distinguished degree-i(g) polynomial; finite-order characteristic-zero linearisation excludes derivative 1 at a fixed point of a nonidentity element. |
| G2(a),(b) | CORRECT | Each orbit meets the disc in one I-orbit, of size Pm/e. A cyclic stabiliser meets P in its π-subgroup. Counting non-P and P\{1} stabiliser elements gives both displayed identities and the ≥2(P−1) bound. |
| G3: tame singleton, wild cluster ≥2, at most one non-p-power | CORRECT | Each nonzero tame contribution is ≥1/2 while the sum is <1. An empty wild cluster contradicts G2(b); a singleton contributes P(1−1/π)<P≤2(P−1). |
| G4: only (m,p,pm), 3m=p+1 | CORRECT | Three-point wild clusters fail by denominators. In a two-point cluster unequal p-exponents fail valuation cancellation; equal exponent a≥2 forces (4p^(a−1)−1) to divide p+4, impossible. For a=1, 3m−1 divides p and is divisible by p. |
| Converse | CORRECT | The AS curve has genus (p−1)(m−1)/2 and cyclic C_pm action; Oort applies. One can also lift explicitly via z^m=((1+λy)^p−1)/λ^p, λ=ζ_p−1: reduction is z^m=y^p−y, infinity is tame since gcd(m,p)=1, and generic indices are (m,p,pm). This covers p≡2 (3) even outside G's p≡1 (4) hypothesis. |
| Corollary: all ES curves at p≡1 (12) have bad reduction | CORRECT | Direct contradiction to G's necessary p≡2 (3). This is about the unmarked curve; marked-cover bad reduction is a different, weaker obstruction. |
| G_k, k≥4, p>k | CORRECT | The same calculation replaces 4 by k; the high-exponent divisor kp^(a−1)−1 exceeds p+k. The remaining case gives (k−1)m=p+1. |
| KT1 / no p² denominators | AGREE | Independent count: 11,800 triples, 122 raw-G2 survivors, all Mordell; zero p² denominators. |
| KT3 | AGREE | Independent count: 4,965 triples, 39 raw-G2 survivors = 38 identity triples plus (2,2,7) at p=7, outside p>8. |
| Prop O, p∥G | CORRECT | Wewers Lemma 1.4(3) preserves the primitive-tail index; (4) divides the wild index by p on the central separable cover. Reversing gives exactly the memo's formulas. |
| Prop O ⇒ BR DEAD as a construction route | CORRECT ONLY WITH NARROWER SCOPE | It shows that lifting a fixed datum cannot change its signature. It does not show that constructing a datum cannot produce previously unknown discrete invariants; see Fix 1. |
| Lemma P | CORRECT | A unique maximal p-valuation cannot cancel; three denominators divisible by p² give too small a sum. Two give p/4<a≤p²/(4p−2)<(p+1)/4, impossible. |
| Prop E for abelian ES covers | CORRECT | Abelian Type I is impossible. In Type II the two wild generators have inverse p-parts and generate P; Lemma P makes P=C_p. Integer σ and vanishing-cycle sum 1 force one primitive tail with σ=1. |
| Prop E for arbitrary cyclic p-Sylow with m_G=1 | CORRECT-WITH-FIX | Obus proves the two numerical possibilities for **étale tails**. Identifying this with Wewers's exceptional full stable reduction outside mild reduction needs qualification; see Fix 3. |
| Cyclic (★)-covers outside special-map lifting | CORRECT | Their marked reduction is exceptional, whereas Wewers's special data exclude σ=1. Good reduction of the unmarked Mordell curve is consistent with this. |
| Lemma S | CORRECT | In S_p an element whose order is divisible by p is a p-cycle. Counting 0,1,2,3 such inertia generators excludes reciprocal sum 4/p. The pair (X,Mon), not every possible larger automorphism group, is excluded. |
| SWZ M1–M5 | CORRECT-WITH-FIX | Extraction matches the source, with ambient-normalizer and vanishing-cycle notation corrections in Fix 4. SWZ Thm 4.8 has no wild critical points, hence three primitive tails; the memo's general Prop O uses Wewers, not that narrower interface. |
| Chevalley finite/cofinite lemma | CORRECT | A constructible image in Spec Z is finite or cofinite. |
| Chevalley ⇒ polynomial identities ⇒ data must grow with p | GAP (Assessment) | Existence over algebraic closures does not give polynomial integer witnesses or even a rational section. No implication to Elsholtz–Tao's rational/polynomial identity obstruction is supplied. |
| fpt example | CORRECT / AGREE | 2/(p+1) has initial digits 1,p−2; first carrying occurs at digit 2, so Hernández gives 3/p+1/p. Original exact check reproduces for p<2000. |
| Other dictionary rows and H★ | Assessment | No new ES implication is proved; H★ is a possible escape, not a proved necessary form of every future characteristic-p argument. |

## Falsifier table
- **F1:** The elementary Mordell congruence excludes squares, and characteristic-zero triangle-group realisation is input-blind.
  But “curves, covers, deformation data and lifts all exist for any signature” (§5.2) is not established by Riemann existence.
  It supplies a characteristic-zero cover, not a special G-map in a specified residue characteristic; GR and Prop E impose actual restrictions.
  Moreover characteristic n=m² is undefined, as the memo itself recognises for composites in F3. Delete the universal geometric-success claim.
- **F2:** The numerator-8 classification is valid. I checked all 12 supplied R₈-zero primes: none is 6 (mod 7), so none activates the identity.
  This is consistent with their zeros, not evidence that geometry detects the restricted c=1/C-even obstruction.
- **F3:** Verified the supplied list has 285 nonsquare composites. There is no characteristic-n construction; passing to a prime factor is a different problem.
  “ES is inherited” is conditional on ES at that factor, not an unconditional proof of all composite cases.
- **F4:** Independently checked all 14 (★)-zero and 38 𝔊*-zero entries are primes ≡1 (12); all six 𝔐 classes mod 840 are also 1 (12).
  Thus G really excludes good-reduction ES curves there. The existing R/R₈ zero certifications themselves were not rerun; this memo relies on their congruences, not their enumeration algorithms.
- No HOT LEAD survives or is claimed. These screens do not justify a universal no-go for constructing characteristic-p data.

## Required fixes, in priority order
1. **Narrow the BR conclusion everywhere, including proposed FRONTIER text.** Prop O is a preservation theorem, not an impossibility theorem.
   “Lifting a supplied triple adds no existence result” is correct; “a char-p construction can only realise a triple supplied as input” is stronger and unproved.
   A constructed map necessarily *has* discrete invariants; that does not mean those invariants had to be chosen beforehand.
   Keep GR DEAD on p≡1 (12); describe BR as fixed-datum lifting/type I, with datum construction unresolved. KT2's pre-registration does not repair its logical inference.
   The existing H★/canonical-object caveat is helpful, but must govern the headline rather than merely appear as an escape afterward.
2. **Repair F1, §5.2 and the proposed FRONTIER sentence.** Replace universal characteristic-p realisability with the proved characteristic-zero statement.
   For example, at p=13 the cyclic cover v^52=t^13(t−1)^2 has signature (4,26,52), reciprocal sum 4/13, and genus 19.
   It exists in characteristic zero but has no good-reduction model by G and no special C_52-map reduction by E. Thus the claimed availability of every geometric step cannot hold for prescribed cover data.
   At squares state that this characteristic-p mechanism is not defined with p=n and supplies no new T1 test; do not assert that its geometric steps all succeed there.
3. **Qualify Prop E's generality.** Obus Thm 3.6 explicitly indexes primitive/new **étale** tails (`1208.3909.txt:356–367`).
   Wewers Def 2.1 is used in the mild-reduction framework, where all tails are étale. The sum alone does not exclude extra inseparable components/tails for higher cyclic p-power Sylows.
   Restrict E to p∥G (all its abelian ES applications already satisfy this), or state only the exceptional numerical étale-tail pattern in the general case.
4. **Correct source/scope shorthand.** Write N_{S_p}(P)=P⋊F_p^×, not unqualified N(P) as though this holds in every G≤S_p.
   In M3 write Σ_prim σ+Σ_new(σ−1)=1; a positive-genus new tail contributes σ_new−1, not σ_new.
   Profiles determine the tail numerical types, not a unique group G; SWZ constructs G by generating the aligned tail groups.
   Explicitly restrict the PSL₂ remark's “σ_x=1/2 plus one new tail 3/2” to Type II. Type I instead has two primitive 1/2 tails and no new tail.
   Supply a precise source/hypotheses for “any ES triple can be realised so” with p∥G, or delete this unused Macbeath assertion.
5. **Remove the unsupported finite-type strengthening.** Keep Chevalley's lemma; do not infer polynomial witnesses or the necessity that the data grow with p.
   Even Spec Z[u]/(u²−2) has a point in every algebraically closed fibre but no rational section; geometric fibre existence supplies no polynomial witnesses.

## Decision
**ACCEPT-WITH-FIXES**, not rejection of the core mathematics. G/G_k, O, Lemma P, the scoped E application and S are useful and withstand this audit.
The previous review's numerical corrections reproduce. Its acceptance of universal geometric success and the broad BR no-go was too generous.
After the fixes, the defensible conclusion is: good reduction gives only Mordell; SWZ's actual degree-p monodromy pairs are excluded;
fixed-datum bad-reduction lifting does not solve the discrete ES problem, while constructing suitable new data remains unresolved.

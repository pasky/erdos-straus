# Hostile review of Z55_CROSSU

**Overall verdict: major revision.** The elementary identities are largely correct and the core enumeration passes independent checks. The advertised structural closure is false as stated; several numerical summaries and the pair-test interpretation are also wrong. No proof of ES or (★) is supplied. The explicit OPEN disclaimers are appropriate, but do not excuse false claims of excluding whole mechanism classes.

## Checks performed

Read the entire memo, all four specified scripts, all of `stats.txt` and the pair summary; processed all 1,339 TSV rows. Consulted GX §1, Lemma 4.1 and EXACTSUM §0 only for background. All executed checks used `timeout 300`, `ulimit -v 4000000`, and `uv run python` for Python; computations were streamed/small, not Cartesian-product array allocations.

Independent trial factorization and squarefree-divisor enumeration at the prime p = 1,000,345,561 ≡ 1 (24), window (5,500,1000,250057), produced 220 shell points, 112 in S₃. On **all 220**, integer/range/congruence checks for j, both modular-inverse identities, the floor identity, second ceiling remainder and switching congruence passed. All three hits passed the SL₂ matrix and determinant identities:

- (u,w,d) = (33,8731,57287), (109,3749,133415), (281,1459,342819).
- Tested integral twists c = 1,3,4,5,−2 and c = j,j+u: `2wtu = cp + cu + 2w`, the reciprocal identity and S_{p,c} all passed.
- Signed c = −1 checked separately at p = 1,007,633,689: (u,w,d,t′) = (17,21887,23019,1354), (113,14763,34127,302).
- Exact rational Dedekind sums passed both displayed identities and standard reciprocity at (u,d,j) = (293,2019,174), (389,2025,141), (221,2033,5), (73,2039,44), (57,2099,40). Corresponding s(d,u) values: −66/293, 157/389, −55/17, −71/73, −41/171.

Compiled the C engine independently. Compared independently enumerated counts, all N_c/G_c/E_c, VRG and histograms to the engine and TSV at p = 1,000,345,561, square n = 100,020,001, composite n = 10,000,000,001, and hard prime 3361: agreement to the stored six-decimal precision. Prime-factor Legendre tests correctly implement squares and c·squares for squarefree u; E_c correctly excludes nonunits. Each subset of distinct odd factors produces one squarefree w; no within-run double counting was found. All 1,339 rows have badj = 0, and no (tag,n) rows repeat. Re-running the supplied stats script reproduced `stats.txt` byte-for-byte.

## Numbered findings

1. **BLOCKING — §4.1's central rigidity theorem is false, and its scope is radically overstated.**
   The asserted impossibility `1−1/a = 1/b` for a,b ≥ 2 fails at a = b = 2. This occurs in a legal shell, not just abstractly: p = 1,007,633,689, (U₀,U₁,Y,X) = (1,5,5,25190842). Its genus points are (u,w,d,j) = (5,1009653,499,1) and (5,1497,336551,4), with weights +1/2 and −1/2. Swapping these and fixing the off-genus points is a sign-reversing bijection of S₃.
   Moreover, “bounded-to-one” lacks an asymptotic bound and a definition of pointwise balancing; every map of a finite shell is bounded-to-one. Across different moduli, negative weights are 1/|□_{u′}|, not 1/|□_u|. Only a *same-u* balance requires exactly |□_u|−1 negative points. If every negative point has square-class size at least q_min, balancing a hit requires at least q_min(1−1/q_hit) negative points, not ≍ q_hit.
   **Fix:** replace this with that elementary weight bound under explicit grouping hypotheses, and, if wanted, a no-single-pair statement when q_min > 2. Require q_min → ∞ for a uniform bounded-group obstruction. Delete the claimed closure of all pairing/switching/descent mechanisms in §4.1, §6, proposed FRONTIER text and bottom line. Reindexing a sum preserves its weights tautologically; it does not prove that a transformation cannot expose cancellation, approximate cancellation or a positivity inequality. Nor does aggregate (CU) require separate equidistribution in every u-fibre.

2. **MAJOR — §4.2's switching congruence is correct; “changes no sign” is false, and the domain is misstated.**
   The identity j′ ≡ 2p⁻¹j⁻¹ (u), the hit-to-hit criterion and hit-to-genus criterion are correct algebraically. But at p = 1,063,647,049, two actual standard-window S₃ points are (89,23343,22783,j=1) and (89,22783,23343,j=32). Both are genus points, |□₈₉| = 44, and switching changes f from +43/44 to −1/44.
   Switching also need not preserve S₃: the new level is w, which can be 1 mod 4. It acts only on the subset where the new w = d satisfies the window/squarefree conditions, not on the whole index multiset. The heading's complementary divisor `(p+u)/d` is 2w, whereas the actual switch is w ↔ d.
   **Fix:** state the correct partial involution, add w ≡ 3 (4) for its S₃ domain, and say it is *not generally weight-negating*, rather than sign-preserving or ruled out as a mechanism. Propagate this correction to §6 and FRONTIER text.

3. **MAJOR — §4.6 uses the wrong endpoint exponent for its CRT threshold.**
   Since d = 4uC−1 = (p+u)/(2w), w ∈ (p^β,p^γ] gives d between scales p^{1−γ} and p^{1−β}. A sufficient product-larger-than-p threshold is K(1−γ) > 1 (with constants/asymptotic margin), not K > 1/(1−β). The latter uses an upper bound as a lower bound.
   Concrete standard-window counterexample: p = 1,007,633,689 has hits (u,w,d) = (53,67909,7419), (69,3733,134963). The d's are coprime, but their product is 1,001,290,497 < p, although K = 2 > 1/(1−1/3). “Typical p has ≍ log²p hits with coprime moduli” is also neither proved nor measured here; CRT uniqueness for a prescribed tuple does not count integers with arbitrary tuples without further summation.
   **Fix:** correct β to γ in the sufficient threshold, specify scale/fixed tuples, and label the typical-count assertion CONJECTURE or remove it.

4. **MAJOR — several analytic/geometric non-results are promoted into universal exclusions (§4.3, §4.5–§4.8, §6).**
   On positive integer points, the multilinearity argument correctly excludes the standard Vieta operation that changes one coordinate while holding two fixed. The coordinate-permutation subgroup is indeed {identity, x↔y}; S_{p,c}: xyz = cx+y+cp and the displayed conic factorization are correct. None of this excludes transformations changing multiple coordinates or proves “Markoff-type orbits do not exist here.”
   Likewise the usual incomplete Kloosterman completion bound is an **upper bound** on error of order √p with logarithms, not an error lower bound ≥ √p or a theorem that this is the “only” fixed-p power-saving tool. EXACTSUM Theorem N concerns n-uniform blockwise estimates combined by triangle inequality; it does not automatically exclude all hybrid sums involving p/d and d̄/p. The unspecified determinant-method exponents and Heilbronn–Porter error claims do not establish further no-gos.
   **Fix:** retain the precise coordinate-fibre result as PROVED, and label the tool discussion Assessment: “these particular standard estimates do not yield the target; no alternative mechanism was found.” Give actual cited estimates, domains and upper-bound notation, or drop unsupported quantitative assertions. Treat ≍ log²p event counts and ≍ U₁ log p sparse-shell sizes at fixed p as heuristics unless separately established.

5. **MAJOR — the statistical denominator is not the genus-conditioned variance for general c.**
   `z55_crossu_stats.py` divides every class by the same sum of `VRG`, which the engine computes only from j ∈ □_u. Under the stated independent genus-conditioned model, the appropriate variance is
   `V_c = 4 Σ_{S₃, gcd(c,u)=1, j∈c□_u} (1/q_u)(1−1/q_u)`, q_u = |□_u|.
   Nonunit exclusions matter: c = 3,6,9,12 lose many fibres. At squares `VRG=0` although nonsquare twisted layers fluctuate, explaining the script's NaNs. Thus these ratios are well-defined common-scale diagnostics at primes, not calibrated z statistics for all c.
   **Fix:** output V_c and recompute class-specific standardized statistics, explicitly retaining their heuristic independence assumption; alternatively rename the current numbers common-V₁-scaled residuals and remove significance/equal-variance interpretations. Do not infer equality of distributions from small residual means.

6. **MAJOR — several numerical bounds in §5 and proposed FRONTIER text contradict the data.**
   Recomputed over the six random-prime tags:
   - sd(N_c−G_c)/√mean(VRG) ranges from **0.75239** (c=12, 10¹⁰) to **1.18171** (c=−1, 10¹²), not 0.9–1.1 for all classes.
   - Mean differences include **−0.673355** (c=16, 10¹³) and **+0.589434** (c=−2, 10¹⁴), outside ±0.55.
   - Across all 18 classes, corr(c=3,c=9) = **−0.267788** at 10¹², violating |ρ| ≤ 0.25. The stats script prints only the six-class subset {1,2,3,4,5,−1}, not all 18.
   - At 10¹⁰ the first all-point histogram bin is **6446/66796 = 0.0965028**, a deviation **0.0034972**, not ≤ 0.002. “At every size” also needs restriction to random-prime samples, not controls/hard primes.
   **Fix:** generate all summary ranges directly from the stated populations, correct every repeated bound, and name which correlations were actually computed. Re-evaluate after finding 5 rather than adjusting a tolerance to preserve the conclusion.

7. **MAJOR — §5.2's pair null and implementation do not justify “coincide” or “no structure.”**
   The recorded percentages agree with the three-line pair output, and the TSV confirms 769 hits at 10¹²–10¹³. But `random.choices` samples with replacement, producing a multiset, unlike the actual hit set. The exact independent genus-Bernoulli model uses point probabilities q_i = 1/|□_{u_i}|; conditional on fixed hit count its subset weights are proportional to ∏ q_i/(1−q_i), not replacement sampling proportional to q_i. The current null can be a declared descriptive benchmark, not the exact conditional genus null.
   There are also concrete code errors: `mean_u(null)` omits all primes with exactly one hit from its numerator, while dividing by *all* hits; the TSV contains 52 such primes. `U1 = max(u in dumped S₃)` is not the specified window endpoint. Pair observations share vertices and primes, so “pair se ≈ 1.5%” is not a justified independent-binomial standard error. Differences 22.13% vs 19.38% and 40.43% vs 36.97% cannot simply be declared identical.
   **Fix:** correct the singleton mean and use the actual U₁; specify/implement a defensible set-valued null; obtain uncertainty by prime-level simulation/bootstrap, including null Monte Carlo uncertainty. Preserve a reproducible dump-generation command/file manifest. Until rerun, withdraw the means-based “entirely because” explanation, the uniform-shell factors 2–40 (not computed by the supplied script), and categorical structurelessness conclusions.

8. **MAJOR — marginal histograms and selected tests are being read as cross-u equidistribution.**
   Ten pooled bins of j/u do not test uniformity over every unit class at each u, independence across u, or distributions in the unmeasured coordinates d,t,d̄. Genus histograms show more than a first-bin excess: at 10⁹, bin 7 is 0.11933 and bin 6 is 0.07683; at 10¹² bins 3 and 6 are 0.09270 and 0.09350. There is no finite-u square-residue baseline or goodness-of-fit analysis supporting “and nothing else.” The literal parenthetical “j ≤ √u are perfect squares” is false.
   **Fix:** describe only observed binned marginals and the tested pair statistics; compare genus bins with the appropriate finite-u square-residue distribution before interpreting shape. Say actual integer squares contribute to the genus class, not that all small j are squares. Replace “uniform,” “statistically indistinguishable,” and “no cross-u structure” by “these tests did not identify a mechanism,” with explicit limitations.

9. **MAJOR — §4.10's claimed orthogonality does not follow and is generally false.**
   On S₃, reciprocity gives `(d/p) = −(j/u)` (Jacobi symbol on the right). Hence genus-c points have `(d/p) = −(c/u)`, not always −1. For c=1, both the hit and genus contributions have symbol −1, so their weighted inner product with this symbol is **−(R−G)**, not zero. Calling this orthogonality assumes the cancellation being sought. Nontrivial fixed fibre reweightings also cannot be excluded merely because they leave the event's definition unchanged.
   **Fix:** say the symbol is constant on each fixed-u genus coset and cannot distinguish its exact class from other classes within that coset. Remove the orthogonality claim and any implication that all fixed multiplicative correlations have been excluded.

10. **MINOR — two literal identity statements are wrong although Lemmas A–C themselves pass.**
    The §3 Reading says the residue, both modular inverses and second remainder are “the same integer j.” They are related quantities, not equal: at (33,8731,57287), j=1 but u⁻¹ mod d=1736 and d⁻¹ mod p=30314031; the second remainder generally equals j⁻¹ mod u. In §4.5, d̄/p is claimed to lie in `[j/u, j/u + 2w/(up))`, but it equals the **excluded upper endpoint**.
    **Fix:** write “determine j by the formulas above”; replace that interval with the exact equality `d̄/p = j/u + 2w/(up)`, or the valid bin `[j/u,(j+1)/u)`. Explicitly exclude u=1 throughout the j-based statements (as the numerical windows already do). Lemma C's coset sums are correct with unit c, or with nonunit summands defined as zero; make that convention explicit.

11. **MINOR — numerical certification is broader than the engine's actual assertions.**
    The engine checks only `u*(u⁻¹ mod d) = 1+jd` after constructing j = −d⁻¹ mod u. It does not compute d̄ mod n or check Lemma A(c)'s two mod-p identities, the floor identity, Lemma B or Lemma C. `badj=0` therefore does not certify those statements on all 1,339 runs. Composite/square controls also require a separately stated extension of any prime-only claim. The claimed agreement with the other engine has no comparison artifact among the specified files.
    **Fix:** accurately enumerate the check performed and distinguish it from the algebraic proof and this review's smaller independent checks; add a reproducible comparison/assertion harness if full-run certification is desired. Keep the otherwise correct genus/coset/histogram implementation.

12. **MINOR — hard-prime emptiness is misstated.**
    The first seven (★)-zero primes do have G=0, but only the first five have empty S₃. At 83449 and 102001, `nsh3=1`, with the point off-genus. At the remaining seven the recorded G range 0.1–1.903824 is correct; 3361 has R=G=2 and 5101441 has R=2, G=1.515152. The 19-sample residual mean −0.387880 and sample sd ≈0.678 support the rounded −0.39 ±0.68, provided ± is explicitly identified as sample sd, not error on the mean.
    **Fix:** replace “empty S₃” with “empty genus support (five have empty S₃, two have one off-genus point)” and specify the meaning of ±.

13. **MINOR — the claim-label discipline and review metadata are not satisfied.**
    §4.4 mixes a PROVED header with an Assessment conclusion; §4.8 similarly mixes labels without separating claims; §5 says both EVIDENCE and CERTIFIED without identifying exactly which assertions carry which label. The conditional implication in §1 is not explicitly CONDITIONAL, and PROVED headings shelter heuristic readings. “CONJECTURE-strength” is not the requested single label. The header refers to internal review “§8,” but only §7 exists and it says review pending.
    **Fix:** give each distinct claim exactly one label; separate algebraic identities, finite-run checks, conditional implications and heuristic readings. Label §1's implication CONDITIONAL (in fact M ≫ log²p, (X-w) and (CU) already suffice without using T_u). Update review status only after fixes and review. Retain the ES/★ disclaimers, but change the verdict to “elementary reformulations; no cancellation mechanism found,” not “proved closures” based on reindexing tautologies.

## Numbers that do check out

For the 1,000 random primes (200,200,150,150,150,150): common-V₁ pooled residuals are c=1 **−1.611455**, c=−1 **+2.158224**, c=2 **−0.124775**, c=4 **−0.047323**, c=25 **+2.195716**. Thus the quoted −1.61 and the other §5.3 pooled values are arithmetically correct, subject to finding 5's interpretation.

The c=1 variance ratios are **1.089584, 1.102434, 0.944011, 0.858839, 0.840355, 0.905015**, agreeing with the rounded list. All-point histogram totals at 10¹² and 10¹⁴ are **293195** and **1615911**. The c=1 mean G−E is within ±0.08 in each random-prime tag. The prime-sample common-scale |z| ≤ 2.5 statement agrees with the supplied tables. Positive square twists vanish on the square controls as reported; this is not an ES result.

The Dedekind identities need no repair: inverse invariance and oddness give s(d,u)=−s(j,u), and p≡−u (d) plus reciprocity gives the second formula. Lemma A's class index, Lemma B's three-step characterization/matrix identity, and Lemma C's parametrized reciprocal identities are valid under the stated range and u>1. These are useful elementary reformulations, not a cancellation theorem.

**Disposition:** retain these identities and the corrected finite computations. Do not export the proposed FRONTIER “scoped closures.” The lane found no mechanism; ES and (CU) remain open, and this memo does not establish a general obstruction to finding one.

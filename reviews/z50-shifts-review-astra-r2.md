# Hostile cross-model review, round 2: z50 lane D / shifts

Reviewed `EXSET_SHIFT_DIVISORS.md` at `10b0ca7a`, the round-1 review and subsequent diff, the binding z48–z50 contexts (including z50 §6), main-repository `EXSET_I3.md` §7, and the relevant (D)-ledger/source scopes. **Erdős–Straus remains OPEN.**

## Overall verdict

**SUBSTANTIAL REPAIR ACCEPTED; remaining scope/formulation repairs required.** The endpoint-family arithmetic budget survives. The author correctly withdraws the T hit estimate as a proved input and explicitly excludes conditional chains, fibre mixtures, refinements, and non-CRT evaluations of character-polynomial majorants from the corresponding caps. Corollary 3.2 is correct. The repaired prime-witness floor works, with a small domain correction in its proof.

However, the document still does **not** establish the campaign fallback: a barrier for a demonstrated method class strictly larger than those previously barred. Corollary 5.2 is a substantive arithmetic budget followed by a formal cap on a specified output shape; operationally it remains a **design constraint on hypothetical non-CRT implementations**, not a demonstrated new obstruction to an existing non-CRT method. “Not restricted to CRT” does not prove the asserted set-theoretic incomparability.

There are genuine proved arithmetic/model statements here, not just a tautology: in particular the single-shift estimates, conditional NA, and the quantitative V/W marginal budget and precision bound. Corollary 3.2 is a routine but valid further consequence of NA. I do not certify publication priority for these statements. There is **no new exceptional-set exponent**, no proved T hit estimate, and no demonstrated qualifying expansion of the barrier ledger.

## 1. Round-1 required repairs

| R1 requirement | Verdict | Reason |
|---|---|---|
| 1. Withdraw blanket scope extensions | PARTIAL | The main scope paragraphs correctly exclude chains/refinements/losses merely bounded above; §1.3 and the claimed incomparability still overstate the result, and the new definition drops `R≥0`. |
| 2. Prove the T estimate or restrict the proved result to V/W | FIXED | Lemma 5.0(a) for T is now Assessment, and 5.1–5.3 are conditional for T. This is the explicitly permitted downgrade, not a proof of the missing estimate. |
| 3. Repair Proposition 2.4 and all progression floors | PARTIAL | The unrestricted/progression distinction, 2^a·p witnesses, totient bound and small-coordinate computations work; the written exceptional-coordinate statements still accidentally include c=1,2 in a false generic argument. |
| 4. Restore CRT scope and supply the odd-line reduction | PARTIAL | Truncation, CRT-only evaluation and the odd-line Jacobi argument are correct; the `2N` cutoff needs the omitted restriction `v_i≤N` (or a changed cutoff). |
| 5. Correct the audit and acknowledge existing U bounds | FIXED | The false iff is removed, the prime-local 1/2 bound is acknowledged, and lane E legitimately supplies the native both-line 2/3 cap and upper bound. |
| 6. Correct analytic hypotheses and citations | PARTIAL | Selberg–Delange replaces the invalid Shiu use, and the no-fixed-prime-divisor construction works. The correlation survey is now honestly a memory-based Assessment, not the exact theorem-by-theorem citation audit requested. |
| 7. Repair labels and numerical prose | PARTIAL | Profiles, error terminology, first-moment ranges, and event-count/coordinate-reach distinction are repaired; the newly specified half-point estimator does not give the printed values, and some scope/label prose remains too strong. |

The partial verdicts do not mean the old major mathematical defects persist unchanged. Most are now local, readily repairable defects; the unresolved claim of an expanded method-class barrier is the substantive remaining issue.

## 2. New material: mathematical attack

### Corollary 3.2 — SOUND, exactly in its stated model

For fixed full prime-power fibre b, the indicator of earlier failures is decreasing in blocks disjoint from the current failure block. NA therefore gives

`P(fail_v ∩ A | b) ≤ P(fail_v | b) P(A | b)`.

Dividing by the positive conditioning probability gives the claimed hit inequality. No conditional-NA closure theorem is needed. Importantly, the comparison is with the **original marginal within b**; it is not a theorem that successive additional conditionings monotonically increase every already-conditioned hit probability.

I independently enumerated the capped model with shifts `{4,7,12}`, caps `2^3·3^2·5·7·11·13`, total period 360360 and full small-prime period 2520. Across all coordinates and all subsets of the other coordinates there were **24096 nonempty conditioning tests, zero violations**.

The model interpretation is also correct: if a chain's hit probability falls below its original global marginal, some adverse reweighting of the original fibre marginals must have occurred. But that does **not** identify the mechanism on actual integers. Neither the nonsquare restriction nor the integer interval has the product law used in the proof. The nine-prime profile is not the full fibre, and §6.5 records no fibre-conditioned hit counts at all. Thus the sentences “§3.2 and §6.5 show this drift on actual integers” and, especially, §7's “on integers the reweighting is the quadratic-profile drift” need an EVIDENCE/Assessment qualification. The data are consistent with that explanation, not a proof that it is the only obstruction to an integer chain argument.

### Odd-line χ-polynomial CRT-mean reduction — SOUND mechanism; missing cutoff hypothesis

For every positive `v≡7 (8)`, including composite v,

`(2/v)=1`, whereas `(-1/v)=-1`.

Thus `2^a≢-1 (v)` for every a≥0. Every witness divisor d has an odd prime factor q, and `(d,v)=1` gives q∤v. Excluding `n≡-v_i (q)` therefore excludes the corresponding witnesses. Each excluded residue is nonzero, so at most `min(r,q-1)` residues are removed. The same construction works for a mixture of the odd and 4ℤ lines: on the latter every witness divisor is odd and >1.

If `v_i≤N`, then d≤N+v_i≤2N. The product density

`∏_{3≤q≤2N}(1-r_q/q)`

has logarithmic cost at most `2r(log log(2N)+3)`, by splitting at q=2r as in the source. Conditioning on n≡1 (8) does not alter this odd-prime product. Global nonnegativity of P and P(0)≥1 then give the claimed lower bound for the **CRT mean**, without any restriction on polynomial degree.

The current statement forgets `v_i≤N`. This is a real hole in the displayed avoider inclusion, not merely notation. Take

`N=10, v=47, n=137≡1 (8)`.

Then `n+v=184=8·23`, with no odd prime factor ≤2N, but `d=46≤N+v=57` divides n+v and is −1 modulo 47. Thus n belongs to the displayed small-prime avoider set but is not an avoider for the truncated witness count. Restrict the shifts to v_i≤N, or use `Y=N+max_i v_i` throughout, with `log log Y` in the bound. I am not claiming the numerical mean bound itself is false for arbitrary shifts; the given proof does not establish it with the stated cutoff.

The repair that distinguishes CRT means from exact interval sums is otherwise complete. The document now correctly leaves genuine non-CRT character methods open.

### Lemma 5.0(b) — SOUND floor, with a small-coordinate proof-domain correction

The repaired mechanism works. Here are the details that make the numerical constants safe.

* For c≥3, a pure power `2^i`, 0≤i≤3, can be −1 modulo c only for c∈{3,5,9}. This follows from divisors of 2,3,5,9. **For c=1,2 the assertion is false**, so the phrase “the latter hold only for c∈{3,5,9}” needs `c≥3`, and the generic T bullet must also exclude c=1,2. For example, at c=2,n=9, M=19 has factor pair (1,19), both −1 modulo 2. T₂ fails for its endpoint predicate, not because no such factor pair exists. The finite check correctly handles it.
* Choose a suitable n-class modulo 16, or a compatible reduced prime class modulo 8 (V/W) or 8c (T), so that a≤3. It is harmless to restrict to a further prime subclass when the original condition only specifies p modulo 2 or 4; this loses an absolute factor.
* For V/W and even c>64, a=0. A forbidden prime class is counted modulo `lcm(8,c)`, not by pretending 8 and c are coprime. Relative to primes in the chosen class modulo 8, Brun–Titchmarsh removes at most
  `8/φ(lcm(8,c)) · (1+o(1)) ≤ 8/φ(c) · (1+o(1))`.
* For odd c>64, there are at most four forbidden classes modulo c. CRT with the chosen class modulo 8 gives a removed fraction at most
  `8/φ(c) · (1+o(1))`.
  Both o(1)'s are uniform for c≤(log N)^3. Since φ(c)≥20, both fractions are ≤0.45 for all sufficiently large N. Thus the claimed slack is legitimate; no four-class subtraction on a non-coprime modulus is required.
* I independently checked φ(c) for 65≤c≤200000: its minimum is 20, attained only at c=66. The elementary bound `φ(c)≥sqrt(c/2)` handles the rest. This numerical threshold is correct.
* For T with c≥3 outside {3,5,9}, one factor in every factorization of 2^a·p is a pure power of 2, so the required pair of −1 residues is impossible. For odd c the p-class modulo c is `2^{-a}`; for even c, a=0 and it is 1. The compatible class modulo 8c is reduced. With `X≈cN/2^a`, Siegel–Walfisz gives a main term of order `X/(φ(8c) log X)≫N/log N`, uniformly for c≤(log N)^3. Discarding p≤2c and the lower endpoint is negligible. Ineffectivity is correctly acknowledged.

Both requested finite runs return `no witness found for: []`, including c=1,2. Inspection of the predicates confirms why p>max(2c,8) suffices to promote a retained witness to a reduced prime progression: the congruences and endpoint residues depend only on `(a,p mod 8c)`, and the variable endpoints are then past their small positivity cutoffs.

**Required local edit:** handle c≤64 first, or explicitly write `c≥3` in the pure-power assertion and generic T bullet. The floor theorem itself need not be downgraded.

### Lemma 5.1′, Theorems 5.1 and 5.3 — SOUND product budgets; restore the remainder convention

The variable-loss inequality is immediate from monotonicity of `min(1,C_eπ_e)` in π_e. It correctly allows varying C_e and correctly says that an event can contribute only when `C_e<1/(1-h_e)`. For C_e≥C>1, the nontrivial arithmetic inputs are the count of costly coordinates and the failure floor. These now hold for V/W.

The mesh version of the 5.3 optimization is sound. A finite mesh away from β=1,2, with a small initial segment absorbed into the `(log N)^{log 2+o(1)}` term, justifies the moving-cutoff argument. The coordinate reach and event count are no longer conflated. The precision-table algebra remains correct. As in R1, this is about unconditional whole-coordinate events, not arbitrary subevents or conditional probabilities.

However, the **new definition no longer requires R(N)≥0**. The algebraic inequality about the product needs no such hypothesis, but the sentence “So such a bound gives no θ>log 2” about the *entire upper bound* does. A signed negative remainder may cancel the product main term. Restore R≥0 in the method-class definition, or explicitly restrict every cap to the product component and say nothing about a signed total. This was present in the round-1 scope and must not disappear during repair.

There is another small hypothesis omission in Remark 5.4: its conclusion about `Σ log(1/P(¬F_e))` requires **π_e=P(¬F_e)**, not merely π_e≥P(¬F_e). With loose marginal bounds, the valid upper bound uses the larger product ∏π_e and yields no constraint on the smaller exact-marginal product. For example π_e=1, C_e=1, R=0 gives the trivial upper bound regardless of the exact marginal costs. State exact marginals as well as R=o(√N). The correction concerning unrestricted R was otherwise right.

### Remark 4.1 — SOUND repair

For `v_i=4k!i`, primes p≤k have the single root 0, while p>k have at most k<p roots. Hence the product has no fixed prime divisor. Even if one works directly with n=8m+1, p=2 never divides a form; for odd p≤k the roots coincide, and for p>k there are still fewer than p roots. The fixed-k Nair–Tenenbaum application is therefore not defeated by the old hypothesis omission. Its constants are fixed-k constants, not a growing-dimensional theorem. The displayed log-power conclusion is routine and superseded, as now stated.

### §1.2 and lane E — SOUND incorporation

Main-repository `EXSET_I3.md` §7 defines the native classes and their mod-8 refinements, includes t=1,2, proves Corollary 7.1 for whole-avoider CRT majorants, and states the BV/BT/Mertens U upper-bound transfer. Those are precisely the inputs used here. The odd line is now covered by a larger native universe, rather than by the invalid inference from a cap on just the 4ℤ subfamily.

Preserve lane E's restrictions: native presentation, whole-avoider majorants on all n≡1 (4), not a blanket prime-input theorem; non-reduced endpoint-pair presentations remain outside it. The current section respects the relevant native/non-native distinction. These results are lane E's contribution, not a new theorem of lane D.

## 3. Chain evidence and numerical repairs

All computations used `ulimit -v 8000000` and explicit timeouts of at most 60 seconds. No N=10^8 census or large factorization sampling was repeated.

Requested reruns:

```
uv run --with sympy python scripts/z50_shifts_floorcheck.py 2 200000 1
no witness found for: []

uv run --with sympy python scripts/z50_shifts_floorcheck.py 64 200000
no witness found for: []

uv run python scripts/z50_shifts_chain.py | tail -3
127 0.2017 0.0889
128 0.0838 0.0488
# steps with conditional hit < marginal hit: 45 of 48
```

The chain's headline count survives, but its implementation has two interpretive issues:

1. It subtracts the square density s=.0004 without renormalizing. This cancels in all successive ratios **except the first**, where `prev=1` should be `1-s` if the numerator remains unnormalized. At v=4 the current code computes `.695665`; the true nonsquare conditional hit is `.6955432173`.
2. The code deliberately compares against all-integer marginals, whereas “conditional hit among surviving nonsquares versus the marginal” should specify that change of population, or preferably use the nonsquare marginal `(1-mf)/(1-s)` consistently.

Using correct nonsquare normalization on both sides gives **45 below, 2 above (v=12,44), 1 equal (v=4)**. At v=119 the conditional hit is `.0217391304` against nonsquare marginal `.221082433`; at v=120,124 it is 0. Thus the qualitative evidence and 45/48 count are robust. These ratios use rounded stored census fractions; they are not a fresh certification of the large census or an exact fibre-drift experiment.

The newly specified **half-point estimator still disagrees with the printed numbers**. Sorting the 4ℤ grid by φ(v), taking the first adjacent straddling pair and interpolating log φ gives:

| x | bracket v values | log φ_half / log log x |
|---|---|---:|
| 10^8 | 12,20 | .678203 |
| 10^16 | 28,36 | .688985 |
| 10^24 | 40,48 | .691059 |
| 10^32 | 48,60 | .644823 |

I used stable input order for equal-φ ties; the listed crossings are unambiguous for these data. The claimed `.65,.66,.66,.64` and §6.1's range `.64–.66` are not reproduced. Replace them with the actual estimator output, or specify and reproduce a different estimator. The standard-error, profile-encoding, and first-moment-range repairs are otherwise satisfactory.

## 4. Scope, labels, and novelty

### What still overclaims

* **§1.3:** “constrain any argument whose output has product form across shifts” remains too broad. Add whole-coordinate, unconditional-marginal, once-per-event, and loss/remainder qualifications, or simply refer to the exact class in §5.2. Conditional chains also have product form.
* **Corollary 5.2's incomparability:** defining a class without requiring CRT evaluation does not exhibit a member outside all the (D)-classes. Output shape and evaluation mechanism are different axes, and a method may admit multiple presentations. The candid admission that no existing non-CRT theorem has been reduced to this shape is useful, but it does not prove either non-inclusion. Replace the categorical conclusion with “the hypotheses do not require CRT evaluation; no strict extension of, or incomparability with, the ledger classes is established here.”
* **§3.3(i):** the cited floors prove `cost(v)≤log log N+O(1)`, not `cost(v)≍log log N` uniformly in v. Growing shifts have cost tending to zero. Either write the upper bound or explicitly restrict to fixed admissible v and also invoke Theorem 2.2. The cross-reference “Lemma 5.2” should be “Lemma 5.1′”.
* **§5.4/§7:** the precision requirement is correctly withdrawn for chains and refinements. Do not replace that old overclaim by a new assertion that integer chains can fail only through quadratic-profile tilt. The model corollary and the finite data do not prove that. A one-sided product upper bound also need not be a two-sided “near-independence theorem”; the necessary output shape is the precise claim.

### Summary table and final labelled outcome

Rows 1–2 are satisfactory, with lane E's native scope understood. Row 3 is satisfactory for the formal model result but needs the cutoff repair in the χ reduction and evidence-only phrasing about integer profile causation. Rows 4–5 correctly distinguish V/W from T; the total-bound interpretation in row 5 inherits the missing R≥0 issue. Row 6's 45/48 headline survives proper normalization, but remains EVIDENCE. Row 7 should not say that all repairs are complete before resolving this review.

The §7 PROVED list is broadly defensible after the small χ-cutoff and floor-domain repairs, and with the product/total distinction restored. Keep Lemma 5.0(b) for T proved separately from the conditional T hit estimates. The missing T input is not just a named progression moment: the factor-convolution/Shiu and small-factor bookkeeping in R1 must also be completed. Finally, **Conjecture 2.6 must remain labelled CONJECTURE**, not be swept into the final “CONDITIONAL / Assessment” bullet.

### Plain answer to the campaign question

**A proved V/W arithmetic budget and a narrowly defined product-form cap: yes. A demonstrated new barrier theorem for a method class not already barred, in the sense required by the campaign: no.** The document supplies a useful design constraint and genuine local theorems, but neither an instantiated non-CRT class covered by the new cap nor a strict enlargement of the previously barred classes. Even a proved incomparability would not by itself satisfy z50's stronger “strictly larger” fallback. No new exceptional-set theorem beyond lane E is obtained.

## 5. Final verdict table

| Item | Verdict | One-line reason |
|---|---|---|
| Corollary 3.2 | SOUND, model | NA gives the displayed conditional inequality; independent exhaustive toy check passes. |
| Integer interpretation of fibre drift | SCOPE REPAIR | Model NA and aggregate nonsquare ratios do not identify all integer dependence with profile reweighting. |
| Odd-line χ CRT reduction | MINOR REPAIR | Jacobi and density arguments work; add v_i≤N or replace the cutoff 2N. |
| Lemma 5.0(b) | SOUND after domain edit | BT≤.45 and Siegel–Walfisz supply work; route c=1,2 solely through the finite cases. |
| Small-coordinate finite checks | VERIFIED | Both required runs return an empty failure list. |
| Lemma 5.1′ | SOUND | Monotonicity gives the variable-loss product inequality. |
| V/W Theorems 5.1, 5.3 | SOUND | Quantitative marginal bounds and the mesh optimization justify their budgets. |
| Corollary 5.2 as a total-bound barrier | REPAIR | Restore R≥0; otherwise a negative remainder can cancel the product. |
| T versions | CORRECTLY CONDITIONAL | The missing progression hit estimate is no longer asserted proved. |
| Remark 5.4 | MINOR REPAIR | Require exact marginals π_e=P(¬F_e), in addition to the repaired remainder condition. |
| Remark 4.1 | SOUND | Factorial-spaced shifts remove the fixed-prime-divisor obstruction. |
| Lane E audit | SOUND | The cited native 2/3 cap and transfer cover both lines with the stated restrictions. |
| Chain evidence | VERIFIED headline; MINOR REPAIR | Correct normalization still gives 45 below, 2 above and 1 equal. |
| Half-point numerical claim | NOT REPRODUCED | The stated estimator gives .678,.689,.691,.645, not .65,.66,.66,.64. |
| Claimed incomparability / expanded barrier class | NOT ESTABLISHED | CRT-free hypotheses are not an example or a proof of non-inclusion. |
| Genuine theorem content / campaign fallback | YES local theorems / NO fallback | Nontrivial marginal/model mathematics survives, but no new exceptional exponent or demonstrated larger method-class cap. |

## Required repairs, in priority order

1. **Finish the scope repair:** restore R≥0 for a cap on the total output, narrow §1.3, and withdraw the unproved incomparability/expanded-class conclusion. Explicitly describe the campaign outcome as a design constraint with proved arithmetic inputs, not a demonstrated enlargement of the ledger.
2. **Separate model truth from integer evidence:** qualify the fibre/profile-drift conclusions in §§3.1, 5.4 and 7; do not impose model-only necessities on arbitrary integer chains.
3. **Close the local proof hypotheses:** add the χ-reduction shift cutoff (or change Y), restrict the generic pure-power/T argument to c≥3, and add exact marginals in Remark 5.4. Keep the T hit estimates conditional on the full missing progression argument.
4. **Repair reproducible numerics:** normalize the first chain step and identify the marginal population; recompute the half-point values with the stated estimator. The 45/48 chain headline can stay.
5. **Clean up labels and references:** replace uniform `cost≍log log N` by the proved upper bound or a fixed-v statement; fix Lemma 5.2→5.1′; keep Conjecture 2.6 labelled CONJECTURE; update the “all repairs applied” claim and, if retaining the literature survey as more than Assessment, supply exact theorem citations.

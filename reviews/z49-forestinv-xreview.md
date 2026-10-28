# z49 forestinv — hostile cross-model review

**Verdict: SOUND, with minor attribution, exposition and test-harness corrections.** No fatal or major mathematical defect found in the reviewed revision. Theorem 2.6 is complete and its proof is rigorous. The reported independent census sub-range agrees exactly. This is **not** a positive step toward the inverse theorem or a new general obstruction to QNR-based methods.

Reviewed snapshot: `side-agent/z49-forestinv`, commit `c462e1b2`, in worktree `erdos-straus-claude-agent-worktree-0046`. This review and its independent checkers are in the reviewer's own worktree. The source worktree was not edited. Read both wave briefs, the relevant frontier/prior-result material, the entire submitted document, and all seven submitted scripts. In particular I checked the underlying statements in `DEDEKIND_ES.md`, `FOREST_DEEP_FABLE.md` and `LOWER_TAIL_ASTRA.md`, rather than relying on the submitted novelty descriptions.

## Findings by severity

### Fatal

None.

### Major

None in this revision. The withdrawn factorisation-blindness claim really would have been false; its withdrawal and the restricted scope of 2.6 are essential, not cosmetic. Do not restore it in a synthesis. Likewise 5.4 obstructs only the **bichromatic** short-word contribution of fixed-finite-support cylinders, not nonzero signed short-word mass or unrestricted identities.

### Minor

1. **Theorem 2.6 corrects, not merely extends, one sentence of DK §9.2.** That source says polynomial identities with “u, v constant” are impossible. They plainly exist: `(T,U,V)=(ab+2,1,1)`. The submitted theorem correctly includes them. Describe the relation as “completes the classification and corrects DK's constant-endpoint assertion,” not just an extension of a correct coefficient comparison. This is an error in the prior source, not in 2.6.
2. **`z49_forestinv_lemmas.py` is not a fail-loud verifier.** It prints L1–L6 failure counts and numerator-8 witnesses but exits successfully even when these are nonzero/nonempty (lines 59–75). Add assertions or a final nonzero exit, including the numerator-8 controls. My actual rerun has all counts zero and both control lists empty; this does not invalidate the saved results. Separately `verify.py` (5c) tests only inclusion in the expected singleton, not equality/nonemptiness. Its actual output is the expected singleton, independently confirmed below.
3. **The Bernoulli-number gloss in Prop 5.3 is underexplained.** The cylinder-to-interval assertion and its consequences are sound. The further “i.e. of generalised Bernoulli numbers” clause deserves a reference or an explicit finite-character expansion, including dependence of coefficients on small character values/residue classes and treatment of primes dividing endpoint denominators. It is not itself proved merely by the cylinder observation. Easiest editorial repair: omit that unused gloss; neither 5.4 nor the class-number example needs it.
4. **State the domain locally in 4.2.** Its use of the fixed `V=4ℤ ∪ (8ℤ+7)`, the QNR claim for the odd part, and the density normalization assume `n ≡ 1 (mod 8)`. This is established earlier and is the intended reading, so I do not reject the proposition; repeat it in the proposition to prevent reuse in the `n ≡ 5 (8)` branch. Also label every non-square composite row of §3.1 explicitly: “composite” there excludes the separately listed squares.

These are not grounds for calling the repaired mathematics unsound. In particular, I found no missing polynomial case or census counterexample to disguise as a “major” finding.

## Claim-by-claim audit

### Theorem E′ — accepted

The coprimality argument is valid without coprime endpoints: `A | n+v` and `A ≡ −1 (v)` imply `gcd(A,n)=1`. For odd `v ≡ 3 (4)`, reciprocity gives `(−v/A′)=(A′/v)`. With `A=2^a A′`, this is `−1` for `v ≡ 7 (8)` and `−(−1)^a` for `v ≡ 3 (8)`; multiplication by `(2/n)^a` gives the asserted sign in both cases. For `4|v`, the displayed computation is correct, including the odd part of v. The `A′=1` and `A=2` boundaries are now handled correctly. At `n ≡ 1 (8)` an odd-square A′ is impossible, since its Jacobi symbol cannot be −1.

This is substantially the calculation already in FDF Theorem E, with the conclusion recorded for general n and the other mod-8 branch. It is not a new composite-existence theorem.

### Lemmas 2.3 and 2.4 — accepted

For 2.3, `gcd(u,n)=gcd(u,v)=gcd(v,n)`, and substitution gives exactly the claimed gcd-indexed bijection. Requiring `g|t′` is necessary; it must not disappear in a summary of “lifting.” The union is disjoint because the lifted endpoint gcd is exactly g.

For 2.4, write `n+v=gM`. A divisor `A ≡ −1 (v)` is coprime to g, so `A|gM` iff `A|M`. Conversely a divisor of M in that class reconstructs positive integral t and the partner. The modulus remains **v**, not `v/g`. Loops are legitimately included by the word-incidence convention.

### Lemma 2.5 and Prop 2.8 — accepted

The factor-endpoint characterization follows from `v(ta−1)=a(b+1)` and `gcd(a,ta−1)=1`. The diagonal specialization and `tn+1=(b+1)^2` are correct. The displayed numerator-8 identity sums to `A/(nm)=8/n`; its hypotheses do not apply to 17 or 241.

For 2.8, direct expansion of `(a+2)(ak+2)−(a+2)−(ak+2)` gives `a[k(a+1)+1]`. With `a ≡ 5 (8)`, `n ≡ 6k+5 (8)`, so the iff `k ≡ 2 (4)` is correct. At k=2 the endpoint gcd is `gcd(a+2,2)=1`. The reduction to a divisor of n+1, and the prime-factor criterion for `(n+1)/2`, are both valid. These are relation/congruence families, not a solution for a natural unrestricted factor class.

### Theorem 2.6 — accepted, complete classification

Here is the exhaustive argument, independently checked:

* For nonzero polynomials in the domain `ℚ[a,b]`, total degrees add under multiplication. If either endpoint degree is at least 2, choose U of maximal endpoint degree. Then `dT+dU+dV ≤ max(2,dU,dV)=dU`; consequently `dT=dV=0`. The equation forces `U=(ab+c)/(cc′−1)`, with `cc′≠1`, and hence degree exactly 2. Cancellation of leading terms on the right cannot create a missing case: it only strengthens the degree upper bound.
* If both endpoint degrees are at most 1, the ab term cannot cancel, so the total product degree is exactly 2. The four degree triples listed in the proof are exhaustive. The constant-endpoint case is family (i).
* For a linear U and constant nonzero V=c, U would divide `ab+c`. This polynomial is primitive and linear in a over `ℚ[b]`, with coefficients b and c coprime, hence irreducible. The symmetric case is identical.
* With both endpoints linear and T=c′ constant, `(c′U−1)(c′V−1)=c′ab+1` contradicts the same irreducibility. Both factors really are nonconstant because c′ is nonzero.

Both surviving shapes satisfy the identity by substitution. No assumption of positivity or integrality was smuggled into the algebra; those enter only when specializing to integer words. The explicit exclusion of zero polynomials is necessary. The result says nothing about rational functions, factor relations, divisibility loci or factorisation algorithms. This scope is accurately stated in the current revision.

### Props 4.2 and 4.3 — accepted in the stated section domain

For 4.2, `v | A+1` and `n ≡ −v (A)` reconstruct the word. No positivity obstruction remains for positive n. Distinct allowed divisors give distinct classes: the only potential collision in `[1,A+1]` is `{1,A+1}`, and 1 is excluded. The QNR assertion follows from E′ and existence of compatible n in the `1 mod 8` class.

The density proof does not illegitimately count an unrestricted infinite union of progressions. The bound `A≤2n+1` truncates the exponents at finite X. For any fixed `0<ε<1`, the sum of the `+1` errors is `Oε(X^ε)` by the geometric growth of `2^a A′`. The tail densities are bounded by a convergent geometric series. This justifies both existence and the claimed upper bound. The relative normalizing population has density `φ(A′)/(16A′)`, as asserted.

For 4.3 the Jacobi character modulo an odd nonsquare is nonprincipal and has exactly `φ(A)/2` negative unit classes. The finite exception calculation reruns exactly. The quoted totient lower bound and `τ(m)≤2√m` imply the desired strict inequality above 10^5 (the sufficient ratio is already greater than 1 at that endpoint and increases). All odd nonsquares A≥17 avoid the exceptional list. CRT preserves infinitely many `n≡1 (8)` in a missed class. This does **not** establish failure of the union over 2-powers of A′, or obstruct choosing a different modulus from n.

### Prop 5.3 and Thm 5.4 — accepted, with the minor exposition note above

For a prefix β, let `P_j/Q_j` be its HJ value, with previous convergent `P_{j−1}/Q_{j−1}`. The exact cylinder in q/p is

`[Q_j/P_j, (Q_j−Q_{j−1})/(P_j−P_{j−1}))`.

Indeed the remaining complete quotient ranges over `(1,∞]`, and the corresponding Möbius map is monotone. This also fixes endpoint inclusion and exact termination; one need not wave away rational boundary cases. I independently checked these intervals for 9,745 prime/prefix pairs of depths 1–4. The finite-support and short-expansion conventions in 5.3–5.4 are indispensable and now correct.

The length-3 dictionary fixes endpoint `u=b₁`; depth 2 also fixes t, and depth 3 fixes the whole word. For length 2, `p=b₁b₂−1`; it can be represented by the boundary word `(t,u,v)=(b₂+1,b₁,1)`, so its endpoint b₁ also belongs to the fixed root set. Length 1 contributes only q=1 and is non-certifying. Thus 5.4(b) really does reduce to a fixed finite set of roots, including boundary words. Apply LTA Thm 3.2 with H containing these roots to get 5.4(c), **conditional on Dickson**. There is no new obstruction theorem here beyond that earlier result.

For `p≡1 (4)`, the class-number example follows by subtracting the first-quarter sum from the zero half-interval sum. The short contribution is bounded by `τ(p+1)+τ(p+3)+τ(p+4)=p^{o(1)}`, while `h(−4p)=p^{1/2+o(1)}`. Hence essentially all the excess lies at longer expansions. This does not determine the existence of a short QNR.

### Other labelled statements

Lemma 1.1, the level factorization 2.2, the sub-product description 2.7, the slot observation 4.1, and the digit-locality statement 5.2 are correct elementary identities or explicitly cited prior results. The HJ/BHK/Rademacher/class-number finite checks in 5.1 all rerun successfully. No global identity displayed here forces a certificate.

## Computation audit

All executions used `ulimit -v 8000000` and explicit timeouts. The independent checkers committed with this review import none of the submitted code.

**Independent census:** `reviews/z49-forestinv-xcheck.c` fixes each n, uses a smallest-prime-factor sieve to enumerate divisors v of n+u, and tests the original predicate `uv | n+u+v` directly. It restricts to `u≤v`, with `(u−1)^2≤n+1`; this is exhaustive, including diagonals. This differs from the submitted census's global `(u,t,v)` arithmetic-progression enumeration. Arrays are bounded by the requested N≤2,000,000, and divisor-buffer capacity is asserted.

For every `9≤n≡1 (8)≤10^6`:

| Population | Count | U_cop failures | U failures |
|---|---:|---:|---:|
| primes | 19,552 | 0 | 0 |
| composite nonsquares | 104,948 | 160 | 6 |
| odd squares | 499 | 499 | 499 |

The six nonsquare U failures are exactly `105, 2961, 3985, 25305, 111969, 978145`. All 160 nonsquare failure records, including the coprime/noncoprime flags, agree byte-for-byte with both a submitted-code rerun and the corresponding prefix of `ucop_failures_1e8.txt`. The independent computation traversed 7,871,743 unordered words and 3,262,494 U-words, checking the gcd decomposition and E′ at witnesses. Maximum least prime V-line is 116 at 3361. No composite coprime to 105 fails in this sub-range.

**Independent boundary/sign check:** `reviews/z49-forestinv-xcheck.py` instead uses the unique possible smaller neighbour `−n mod v`, with diagonal candidates added. Over all `5≤n≡1 (4)≤4000`, it checks 26,092 unordered words and 14,944 U-endpoint incidences, including 500 A=2 incidences; all pass. It also checks the cylinder intervals and numerator-8 identity in 2.5 independently.

**Submitted verifiers:** `verify.py` reproduces 5,602 witnesses in (5), 6,187 in (5b), the singleton boundary set in (5c), all 2,960 BHK/Rademacher pairs, and the exact Prop 4.3 exception list, with zero failures. `lemmas.py` reports zero failures for L1–L6 and empty numerator-8 controls. The hard-prime and square control output matches the archive (including its extra 11,131 rows).

**Other §3 data:** fire-rate and sporadic-statistics scripts rerun with byte-identical output. These are exact sample statistics, not probability theorems; the document generally makes that distinction correctly. The high-range domain count independently gives 10,714,285 candidates, 325 squares, and 10,713,960 nonsquares. The 119 archived failure rows have rescue histogram `{7:89,12:23,15:4,20:1,24:1,36:1}`. A submitted-engine rerun on `[10^9,1.05·10^9]` tests 59,520 nonsquares, reproduces precisely the two archived U_cop failures (1,021,254,465 and 1,040,087,265), and finds no U failure.

**Limit of this review's certification:** I did not independently recompute the whole 10^8 census or the whole 10^9–10^10 scan. Their archived totals are consistent with the code, checked sub-ranges and aggregation; this review is not a second full-range certificate.

Reproduce the independent parts from this worktree:

```sh
ulimit -v 8000000
timeout 30 gcc -O2 -Wall -Wextra -Werror reviews/z49-forestinv-xcheck.c -lm -o /tmp/z49-forestinv-xcheck
timeout 240 /tmp/z49-forestinv-xcheck 1000000
timeout 180 uv run python reviews/z49-forestinv-xcheck.py /home/pasky/projects/math/erdos-straus-claude-agent-worktree-0046
```

## Honest novelty grades

Scale: **0/5** = prior/classical or repackaging; **1/5** = elementary refinement/example/new data; **2/5** = genuinely additional but narrow classification; **3–5/5** would require a materially new mechanism/barrier or substantial progress. These are campaign-relative grades, not claims of external priority.

| Result | Grade | Assessment |
|---|---:|---|
| Lemma 1.1 | 0/5 | Classical easy congruence class. |
| Theorem E′ | 1/5 | Explicit general-n/2-part formulation of essentially the existing reciprocity calculation. |
| Prop 2.2 | 0/5 | Existing level factorization. |
| Lemma 2.3 | 1/5 | Useful exhaustive gcd bookkeeping of DK's scaling map. |
| Lemma 2.4 | 1/5 | Immediate coprime-divisor cancellation; the retained modulus is useful to state. |
| Lemma 2.5 | 0/5 | Existing factor-endpoint/diagonal construction; numerator-8 specialization is elementary. |
| Theorem 2.6 | 2/5 | Complete free-bivariate-polynomial classification, beyond and partly correcting DK's partial claim. No arithmetic existence consequence. |
| Prop 2.7 | 0/5 | Divisor/sub-product tautology. |
| Prop 2.8 | 1/5 | Elementary relation family; useful counterexample to an overbroad barrier, not a new general mechanism. |
| §3 census | 1/5 | Additional finite data and gcd split, not a theorem beyond its range. |
| Prop 4.1 | 0/5 | Slot algebra and E′ restated. |
| Prop 4.2 | 1/5 | Shadow dictionary plus a valid elementary density estimate. |
| Prop 4.3 | 1/5 | Quantified fixed-modulus nonconverse; much weaker than ruling out QNR-guided search. |
| §§5.1–5.2 | 0/5 | Classical/campaign dictionaries, independently rechecked. |
| Prop 5.3 | 0/5 | Standard CF-cylinder geometry and character-sum consequence. |
| Thm 5.4 | 0/5 | Direct finite-root corollary of LTA Thm 3.2, not a new barrier. |

**Bottom line:** retain 2.6 as a small, genuinely complete classification and retain the composite census as useful data. The remaining labelled results are sound elementary bookkeeping or prior-result corollaries. No inverse theorem, natural-class composite theorem, QNR attachment mechanism or new global forcing identity has been established.

# z50 ncrt — Astra hostile review 2

Reviewed `EXSET_BEYOND_CRT.md` completely at `7fdb915d004f31d18535d77b25523af652a09a91`, review 1 (D1–D14), and the read-only main repository's `EXSET_I3.md`, especially §§3–4 and 7. Also checked the actual K2 leak proof, IF Theorem 2.2, NC §§4 and 8.5, and the switching script. This is an internal mathematical review.

**Overall: MAJOR, confined principally to the new scope/door-closing claims.** The repaired word-universe cap, including selectors and non-reduced certificate pair classes, survives. The W-uniformity repair is adequate. The prime/rough-input theorem survives and is compatible with lane E. However, “covers all three” incorrectly includes arbitrary prime-only methods; Theorem 4.3 is false literally without certificate refinements; and “D1 = D2” imports a conditional exact-moment result as unconditional. No fatal obstruction to the core §2–3 results was found.

| Item | Verdict |
|---|---|
| D1–D14 repair audit | SOUND-WITH-REPAIRS; open details and regressions listed below |
| Theorem 2.1 / Lemma 2.4 W-uniformity (D4) | SOUND |
| Unit-square base for selectors and non-reduced certificate pair classes | SOUND |
| §1.3 comparison with lane E | MAJOR scope repair; underlying comparison is valid |
| Theorem 3.1 and consistency with lane E | SOUND; minor definition/presentation repairs |
| Proposition 4.1 inequality | SOUND; subsequent detector inference needs refinements |
| Proposition 4.2 bounded mass | SOUND-WITH-REPAIRS |
| Theorem 4.3 as written | MAJOR; explicit counterexample to literal statement |
| Residual D1 = D2 / quantitative depth assertion | MAJOR |
| D7 assessment | MAJOR as a purported exclusion; acceptable as “no successful input found” |

## A. Round-1 repair ledger

| Defect | Current repair / remaining issue |
|---|---|
| D1 | **Substantively repaired.** Proposition 1.2 distinguishes parameter-freezing from set equality and gives coincidences. Still change the §1.3 heading “yes-but-irrelevant as sets”: set containment is expressly undecided in the body. Also `C_II(1,tv−1,v)` should have third parameter `t`, as its immediately following parameter tuple says. |
| D2 | **Closed.** The filtered 392 parameter instances / 318 distinct classes and finite coverage scope are accurately described. |
| D3 | **Partly open.** The even-endpoint implication and atom prefixes are repaired. But U nondegeneracy is not always merely a finite-prefix issue in an endpoint grouping: a fixed factor `tv−1=1` never becomes >1. See R2-7. |
| D4 | **Closed.** The every-W hypothesis and polylogarithmic W dependence are now present and justified; detailed check below. |
| D5 | **Closed.** Selectors are separate from the square-free certificate universe and are added through the unit-base argument. |
| D6 | **Closed.** The large-divisor factor is now `x^(−1/8)` with ε=1/16. |
| D7 | **Closed in substance.** The long-block boundary is now `16ℓ^(v/3)`, giving the required Shiu interval length, and q=1 is assigned to the short range. In the short range write `m≪ℓ^(2v)` rather than `m≤ℓ^(2v)`, or enlarge the fixed W; the harmless constants do not affect the proof. |
| D8 | **Repaired in Corollary 2.5.** Whole-avoider/word-universe scope and universe exhaustion are explicit. **Regresses in the new material:** arbitrary words/raw classes in Theorem 4.3, and the exhaustive door list in §7, exceed the proved scope. |
| D9 | **Repaired locally, regresses in Theorem 4.3.** Corollary 2.5 leaves P unchecked and explicitly limits its mixed-family transfers to M1/M2. Section 4 again asserts mixed-family L1/C without the promised separate transfer. This is readily repairable, but the two statements currently disagree. |
| D10 | **Closed.** Unrestricted exponent sharpness versus bounded-B order sharpness is now distinguished. |
| D11 | **Essentially repaired.** Positive intervals, onset costs, and ES₅ at p≡3 mod4 are supplied. `a₀` in Lemma 3.6 remains undefined: specify, for example, a₀=1/8 for sufficiently large K. |
| D12 | **Closed.** The quantitative predecessor and shared construction are acknowledged; the claimed increment is now prime/rough log-log removal, not an unprecedented construction. |
| D13 | **Closed.** The misleading boundary-word example is gone and polynomial auxiliary primes are distinguished from non-CRT evaluation. |
| D14 | **Partly open.** The title and numerical U-identity description are corrected. Line 120 still calls the identity script “symbolic”; it is an exact-arithmetic checker, while the displayed algebra is the symbolic proof. More importantly, new §4 assertions misuse theorem scope and a conditional citation. |

Thus D3 and small remnants of D1/D11/D14 remain; D8/D9 recur in §4. It is inaccurate to record all D1–D14 as unqualifiedly closed.

## B. Lane E, selectors, pair classes, and the square base

### R2-1 — The distinction is real, but “covers all three” overclaims prime-only scope (MAJOR)

Lane E Corollary 7.1 quantifies over its specified native endpoint refinements, on n≡1 mod4, with majorization of their **whole** avoider set. Its base is 2-adically square and zero modulo small odd primes. It does not establish a theorem for an augmented family containing, for example, `0 mod 3`.

This is not just a naming distinction. Take F={`0 mod 3`} and `ν=1−1[3|n]`. This is a globally nonnegative whole-avoider majorant, identically zero on lane E's base once W≥3. It satisfies the selector-containing hypotheses of Corollary 2.5 (the word part can be empty), but not the family hypothesis of lane E Corollary 7.1. The unit-square base avoids this selector. This demonstrates a genuine extension of architecture; it does not say that every selector is obstructive in every particular family (e.g. `0 mod 2` is irrelevant on n≡1 mod4).

The pair examples also genuinely work:

* `21 mod 36` is P(12,3), with `t=(n+15)/36`. Every positive member has endpoint 12 divisible by 4 and both adjacent factors >1. No onset exception is needed in this example.
* `57 mod 72` is its refinement. Both classes are `3 mod 9`, so every member has 3-adic valuation exactly one. Neither contains **any** positive perfect square.
* The second class meets lane E's base: it is `1 mod 8` and `0 mod 3`; additional pinned odd primes other than 3 can be imposed by CRT. It is not a native reduced endpoint class.
* Both belong to the certificate-word universe of Corollary 2.5. Non-reducedness poses no problem for the unit-square construction: a complete progression containing no positive perfect square cannot contain a square residue modulo its modulus. Otherwise a positive integer representative of a modular square root would supply a positive square in the progression. Lemma 2.2, not reducedness, supplies the needed base exclusion.

**The invalid part is “Corollary 2.5 … covers all three,” when the third category is prime-only methods.** Corollary 2.5 still requires ν≥0 globally and ν≥1 on the whole periodic avoider. It can cap such certificates even when they are used to bound primes. It does **not** cap arbitrary functions majorizing only exceptional primes or nonnegative only at primes. Its own next paragraph expressly leaves the prime-law/unit-group rerun unchecked.

**Repair:** say that the corollary covers selector-augmented whole-avoider architectures (including their use for prime bounds) and non-reduced certificate pair classes. Keep genuinely prime-only majorants outside its proved scope until P is proved. “A unit base is available” is not that proof.

### R2-2 — Log-log removal is consistent, but its purported cause must stay architectural (SOUND-WITH-REPAIRS)

Theorem 3.1 really has the stronger saving `exp(−c(log N)^(2/3))` at primes and y-rough inputs, rather than lane E's all-integer `exp(−c(log N)^(2/3)/(log log N)^(1/3))`. Its selector `S_y` excludes the very fibres used by lane E's comparison. Its majorant covers avoiders of **atoms plus selectors**, not all avoiders of the native atom family. There is therefore no contradiction with lane E Theorem 4.1 or Corollary 7.1.

However, lane E proves intrinsic log-log loss only for the **native whole-avoider architecture**, not all possible all-integer whole-avoider methods, and certainly not a lower bound for genuine U failures. In particular its theorem does not exclude log-log removal over all n using non-reduced pair classes or another forcing universe.

**Repair:** replace “it is the price of inputs with many small prime factors” by “the native whole-avoider obstruction is witnessed on small-prime-divisible fibres, which the rough-input construction excludes.” Retain the native-family qualifier every time intrinsic loss is claimed. Remark 3.8's weaker all-n speculation is now superseded by the known lane E theorem and should be labelled as such or removed.

## C. W-uniformity: checked and adequate

Theorem 2.1 now assumes (iii) for every W≥W₁ with `C_κ(W)≤A_κ(log W)^d`, while permitting the first-moment constants to depend on the subsequently fixed cutoff. This fixes the original quantifier problem.

Lemma 2.4 supplies the required dependence:

1. For pairs, the Euler product for `τ(q)^3 Γ(q)/q` has large-prime parameter 8. The finitely modified small-prime factors contribute at most a power of log W.
2. For long endpoint blocks, the first Cauchy–Schwarz factor uses `τ(q)^2 Γ(q)^2`, with large-prime parameter 4. Its small-prime cost is again polylogarithmic in W. Shiu is applied to `τ^4`, not to a W-dependent function.
3. For short blocks, `Γ(q)≤8·3^ω(q)` is independent of W, so the pointwise divisor estimates have uniform constants.
4. K2 Lemma 4.1 contributes another Euler factor `Σ Γ(q)/q≪(log W)^O(1) log ℓ`, not an exponential-in-W loss. With κ=1/4, Minkowski over v gives `E p_ℓ²≪(log W)^O(1) ℓ^(−7/4)(log ℓ)^O(1)`.
5. The leak is consequently `≪W^(−1/4)(log W)^O(1)→0`. Fix W first, then use the first-moment constant at that W and enlarge λ₀.

**Verdict: SOUND.** No remaining load-bearing W-uniformity gap. For completely precise theorem bookkeeping, allow λ₀ to depend on y₀ and the chosen admissible cutoff as well; the printed list of parameter dependencies omits these harmless thresholds.

## D. Divisor switching

### R2-3 — Proposition 4.1 is correct; raw cheap classes are not automatically certificate classes (SOUND-WITH-REPAIRS)

For positive n all adjacent factors are positive. The product argument is valid. When u,v≥2, `(u−1)(v−1)≤n+1` and `u+v≤(u−1)(v−1)+3≤n+4`; the u=1 or v=1 cases are also valid by symmetry. Thus the displayed inequality is proved.

But transferring a **certificate** to the cheapest grouping can require refinement by the free coordinate modulo 4, or modulo 8 for U predicates. For n=5 the U-word `(t,u,v)=(1,3,4)` has cheapest raw grouping `E(1,3)=1 mod 2`. That class contains the square 1 and is not this word's certificate class. Retaining `4|v` gives `5 mod 8` instead.

**Repair:** state the certified modulus bound as `≤4(2N+4)^(2/3)`, or the safe `≤8(2N+4)^(2/3)` for all refinements, hence `<N/2` for sufficiently large N. IF Theorem 2.2 applies only if the **expansion of ν itself**, not just its generating family, has small denominators. Products can still have lcm>N, as §4.2 correctly notices. Also correct the parenthesis about modulus 1: τ(n+1), τ(2n+1) count broader level-1/2 word families, not just the pairs with `tu−1=1`.

### R2-4 — Proposition 4.2 needs an averaging convention and an accurate numerical comparison (SOUND-WITH-REPAIRS)

For ordered words and the limit of averages over 1≤n≤X as X→∞ with T fixed,

`w_pair(T)=Σ_{m≤T}τ(m)/m`,

`w_end(T)=Σ_{A≤T}τ(A+1)/A`.

Both are `(1/2)log²T+O(log T)` by divisor hyperbola/partial summation, so the quadratic inventory and the bounded-factor conclusion are correct. Define `w_max=max_g w_g` if that notation is retained.

In fact, under this averaging convention,

`w_min(T)=w_pair(T)+2w_end(T)`.

Two grouping cutoffs bound all three coordinates, hence their overlap contains only finitely many words/n and has zero limiting density. The cheapest/single-endpoint ratio therefore tends to **3**, not 1.25–1.51. The saved script counts unordered u≤v and compares against **either endpoint** on a finite n-range; its own output says so. That is a legitimate different diagnostic, not verification of the displayed ordered/Haar ratio.

**Repair:** define the limit and ordered convention, cite the elementary asymptotic, and label the numerical ratio “unordered words, either endpoint, finite interval.” If certificate-only counts are intended, assert the inherited upper bound rather than these unrestricted leading constants.

### R2-5 — Theorem 4.3 is false literally, but has a simple scoped replacement (MAJOR)

It currently allows “each word” and “any one of its three classes.” Arbitrary words are not certificate words, and even a certificate word's raw class need not preserve its certificate.

There is an immediate counterexample: `(t,u,v)=(4,1,1)` is a certificate word of n=2. Choose its raw pair class P(1,1), which is all integers. The resulting finite family's avoider is empty, and ν=0 is a valid majorant. To avoid any convention about the level of zero, use `ν=ε(1+1[n≡0 mod q])` with a fixed prime q above W and log q≥λ₀, then let ε→0. No positive lower bound on Eν at that fixed level, hence no claimed logarithmic cap, holds. This counterexample persists even if “word” is changed to “certificate word” without adding refinement.

**Repair:** require a finite family of **certificate-preserving congruence refinements** of selected groupings, and a globally nonnegative majorant of its whole avoider. Then the word-only cap is exactly Corollary 2.5, regardless of the selection rule. For eventual U words, retain the proper onset convention and discard structurally degenerate groupings.

For mixtures, invoke Theorem 2.1 on the union with verified combined moments, not K2/KARY3 as if their stated universes already contained all word classes. The word first moment `O(log²y(log log y)²)` is `O(log³y)`, so together with KARY3's K2 first moment a pure 3/4 mean cap is available. State the transfers actually established: M1/M2 already appear in §2; either supply the short family-free L1/C transfer or omit those two for mixtures. All evaluation-specific hypotheses remain necessary.

The subsequent “depth bought: O(1) factor” also does not follow for arbitrary selected finite families merely from an upper bound on the full-universe inventory. Switching can change individual log-modulus costs dramatically. The supported conclusion is: **the full inventory remains quadratic and the specified whole-avoider evaluations remain capped**, not a universal constant-factor comparison of optimal depths.

## E. The claimed closure of doors D1 and D7

### R2-6 — D1 = D2 drops an explicit conditional hypothesis (MAJOR)

The cited `EXCEPTIONAL_NONCRT.md` Corollary 8.7 is explicitly **CONDITIONAL on H_node(k)**, an unproved lower bound on empirical hit-count probabilities at interpolation nodes. It also needs a suitable mean/degree range and concerns symmetric hit-count polynomials, not arbitrary hit-pattern majorants. Proposition 8.6 alone supplies no uniform saving cap without lower bounds on those node probabilities. These hypotheses are neither stated nor proved for this word family.

NC Proposition 4.2 and TU's CRT-main-term statements bound **CRT-evaluated** moments, not arbitrary exact interval moments. Indeed NC §4 explicitly retains the alternative of *lower-order true moments deviating favourably from CRT*. Thus §4.2(4)'s unconditional claim that bounded-order exact data are useless, and its quantitative necessary order `(log N)^θ/log log N`, are unsupported.

Also:

* Summing only r-tuples with lcm>N gives the high-lcm part of `Σ binom(H(n),r)`, not automatically the full factorial moment. Weighted/non-symmetric expansions require their corresponding correlations.
* Classical r=2 shifted-divisor asymptotics do not automatically cover arbitrary growing shifts, divisor restrictions, or the uniformity/error scale of this detector. Cite a precise applicable theorem or call this an analogy. Likewise, fixed-shift r=3 difficulty is not a theorem excluding usable aggregate estimates.
* D1 as defined includes interval-only majorants and signed/position-sensitive counts. Nothing proves all such certificates reduce to symmetric high-order hit-count polynomials.

**Repair:** replace the identity of doors by: “For this Bonferroni implementation, counting its high-lcm terms is a correlation problem. Existing CRT moment caps do not settle favourable exact-interval evaluations. A high-degree necessity follows only under an appropriate proved node hypothesis; no such hypothesis is established here.” Remove the unconditional depth threshold from §0, §4.2 and §7. The final list of necessary escape routes must also retain interval-only and unchecked prime-only architectures.

### R2-8 — D7 offers no new barrier; several purported reductions are unjustified (MAJOR as written)

A Vaughan/Heath-Brown decomposition does not by itself make every Type-I estimate a prime-law CRT evaluation or every Type-II estimate a CRT-admissible large sieve. Period Q≫N is not a sufficient hypothesis for the cited LS caps. To import one of those caps, identify the actual certificate and check its comparison/admissibility hypotheses. A signed bilinear argument might instead use precisely the interval information absent from the comparison law.

Nor does `ν(mk)` not being determined by ν(m),ν(k) prove “no extra multiplicative structure.” Even a single progression has nontrivial multiplicative character structure on units. Harman-style lower bounds for the complement could in principle yield upper bounds for exceptional primes if sufficiently accurate; no general impossibility follows from the direction of the sieve inequality.

Finally, NC Propositions 4.1–4.2 bound specified CRT moment certificates, not the actual normalized variance of every possible ES/U representation count. They do not justify the asserted variance lower bound or exclude a reformulation with a small L² error.

**Repair:** retain only the research outcome “no applicable prime-specific estimate or L²-small reformulation was found.” Remove the universal Type-II-to-LS and structural/variance assertions, or prove them for an explicitly defined count and evaluation. Keep the prime-law extension in its current unchecked status. The “Assessment” label does not turn these categorical reductions into valid deductions.

## F. Remaining definition and label repairs

### R2-7 — Fixed degeneracy is not a finite prefix (minor but real D3 remainder)

In E(t,v), `tv−1` is fixed. If it equals 1, no later member supplies a U-word in that grouping. For example E(1,2) with n≡6 mod8 has free u=n+2 and satisfies the endpoint/slot congruences, but `tv−1=1` forever. An alternative U-word, if available, is a separate argument, not a finite-prefix repair of this one.

**Repair:** discard fixed adjacent factors ≤1 when constructing eventual-U endpoint classes. Only then can the inequality involving the free coordinate be handled by deleting finitely many initial members. The certificate-word cap itself is unaffected, and the actual §3 atoms are nondegenerate above the paid onset.

Other small repairs: define a₀; change the §1.3 set-containment heading and C_II parameter typo; separate symbolic algebra from numerical checking; mark Remark 3.8 superseded. Update the summary and §6 repair ledger only after the substantive §4 scope changes. “No barrier broken” and the restricted sharpness language are now appropriate.

## G. Independent bounded check

Created `/tmp/z50_ncrt_review2_check.py`, importing only Python's standard library and no campaign code. Executed with `ulimit -v 524288` (512 MiB virtual memory) and a 60-second timeout via `uv run python`. It streams divisor trials and allocates no Cartesian-product arrays. Output is `/tmp/z50_ncrt_review2_check.log`.

Results:

* Exhaustive square-residue checks modulo 36 and 72 find no square in `21 mod36` or `57 mod72`; the first 1,000 positive members of each have the explicit U-word `( (n+15)/36,12,3 )`.
* Exhaustive ordered-word enumeration for every n=701,…,750 checks **1,858 words**, including **1,177 certificates**, with zero failures of Proposition 4.1. The maximum cubed ratio is exactly `128000/508369`.
* Independently verifies the raw-class/refinement counterexample at n=5: cheapest `1 mod2` contains square 1; certificate refinement is `5 mod8`.
* At T=10 the exact ordered-word limiting masses are pair `2521/420`, each endpoint `3641/504`, cheapest `6442/315`; cheapest/single-endpoint is `51536/18205≈2.831`, confirming why the script's 1.25–1.51 statistic must be described differently.

These finite checks support only their stated scope; they do not certify the asymptotic analytic inputs.

## Final decision

**Preserve §§2–3 after the small remaining definition repairs.** In particular, selector-containing whole-avoider families and non-reduced certificate pair classes really are covered by the repaired unit-square cap, and D4 is fixed. Preserve Proposition 4.1 and the quadratic mass upper bound. Re-state Theorem 4.3 with certificate refinements and actual transfer hypotheses. Retract the unconditional D1=D2/depth claim and the supposed exhaustive prime-method reduction. The new material currently overstates what is proved; it does not expose a fatal flaw in the prime U/ES₅ exceptional bound.

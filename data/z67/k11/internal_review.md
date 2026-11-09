# K11 hostile internal review

Reviewed `cefd3d413..598648844` (all four commits), restricted to `Z67_K11.md`, `scripts/z67_k11_*.py`, and `data/z67/k11/*`. Context checked: UCOVER Lemma 1 and Theorem T, LOGIC2 Theorem D and §5.6, and the actual ET Proposition 1.9 / §10 PDF text.

**Verdict: revise before accepting the memo as written.** Lemmas R and N are sound. The event congruences are sound with the I-3 root-selection qualification below. The principal finite computations reproduce. The serious defects are unproved enumeration/completeness assertions and conclusions stronger than the finite evidence or the failed union bound supports. **ES remains OPEN; nothing here settles K ∩ U.**

**Model/provider errors:** none encountered. An independent certificate check initially failed because three advertised non-residues are actually quadratic residues modulo 11; this was an arithmetic/input-classification finding, not a provider failure.

## Numbered findings

1. **MAJOR — Finite-level survival is advertised as survival of every 13-smooth class.**
   `Z67_K11.md:23–24` says the 1,316,612 residues “survive all 13-smooth classes” and adds “no finite covering.” The enumerator proves survival only against classes whose moduli **divide the particular level** Q = 3,116,623,910,400. A 13-smooth modulus can have arbitrarily higher exponents. Neither nonemptiness of X_13 nor absence of a finite 13-smooth covering follows. The careful qualification in §5 does not repair the abstract. Replace this with “survive all classes with modulus dividing Q; no covering at this level was found,” and apply the same qualification wherever “no covering” is summarized. The numerical count itself is correct.

2. **MAJOR — The finite-events/effective-enumeration assertion after Lemma M is not proved for all rows.**
   `Z67_K11.md:117–120` supplies only an unfinished I-2 argument (“a quotient argument”), then infers exact enumeration for every family, including mixed I-3 and II-3. Congruence equivalences alone do not give a terminating parameter search. If “events” means distinct cylinders at a fixed S-level, finiteness is tautological (at most φ(N) cylinders), but that does **not** supply an algorithm certifying that no further cylinder is realizable. If it means parameter tuples, effective bounds must be proved.

   I-2 is repairable: write a = A x, c = B y, f = F z with the S-parts A, B, F fixed, set Fz + 1 = 4xyD and a + c = wz. Then
   `w(4xyD − 1) = F(Ax + By)`.
   If Ax ≤ By, this gives `3wxD ≤ 2FB`; the remaining variable is
   `y = (FAx + w)/(4wxD − FB)`, with positive denominator. This is a genuine finite search. The memo does not give corresponding arguments for every other row/support split. **Demand:** separate the proved event equations from the unproved effective-enumeration assertion; relabel the latter until all bounds are supplied. I am not claiming the desired finiteness theorem is false.

3. **MAJOR — Tested rational slices do not classify all possible rational slices.**
   The abstract (`Z67_K11.md:18–21`) and §3 (`:145–149`) conclude that the “only” rational-slice candidates are profiles equal to 1 away from finitely many primes. Tests of finitely many q and two T sets cannot prove this. Even a proved cover for a fixed (q,T) need not cover the larger slice obtained by freeing additional primes in T. The displayed EVIDENCE heading is insufficient when the statement beneath it is categorical. State only that every **tested nonempty K-slice** with q ≠ 1 was covered; any universal classification is a separate conjecture. The verified explicit coverings remain useful.

4. **MAJOR — §4 proves failure of particular estimates, not an exhaustive obstruction to measure certificates.**
   `Z67_K11.md:185–216,244–245,275` overstates what follows from the calculations.
   * The II-2 prime subseries really diverges with P. This defeats the unconditioned sum-of-all-class-masses bound, not every uniform argument proving X_P ≠ ∅. Positive lower bounds depending on P may tend to zero and still suffice via Lemma R. Conditioning, removing overlaps, or bounding only events meeting the survivor set are not excluded.
   * The purported two-option classification of “every route” is not established. Haar-nullness does not restrict useful slices to the tested rational ones, nor does it force every proof to use a global ΣII point-count estimate. A sub-square-root estimate is sufficient for the stated counting route, not proved necessary for all routes.
   * The quoted 2-adic values are **sums of K-relative cylinder measures with family labels retained**, not measures of the union or of its intersection with existing survivors. I reproduced them, and also deduplicated them:

     | v₂(m) | family-tagged sum | distinct (m,r) sum |
     |---|---:|---:|
     | 9 | 0.422057998 | 0.346135972 |
     | 10 | 0.257558400 | 0.212046223 |
     | 11 | 0.153159534 | 0.126679073 |
     | 12 | 0.092950660 | 0.080102430 |

     Even the deduplicated sums still overcount overlaps between cylinders of different moduli. A large upper bound is not a lower bound on the damage done by the tail. Also, the v₂ = 9 layer is already included in the final §5 level.
   * The square-root arithmetic is **correct as an upper-bound diagnosis**: N = a_S d_S and n = a_S² d_S give `sqrt(n)/N = 1/sqrt(d_S)`, hence no decay as a_S grows with d_S fixed. This does **not** prove that there actually are ≍N events. Likewise the divisor estimate gives an upper bound involving `Σ a^(−1/2) d^(−3/4)`, not the asserted asymptotic equivalence for the actual tail.

   Keep the divergence labelled PROVED, and explicitly scope it to the raw series. Relabel the feasibility thresholds (2-levels 25–30, 60+ digit factorizations, N around 10^30–10^50), “route-kill,” and universal impossibility wording as an assessment of the specific estimates tried, not a mathematical obstruction to other certificates.

5. **MINOR — Three of the “24 non-residue” q values are not in K; the four-prime tbox does not validate this precondition.**
   In `Z67_K11.md:134`, `7/2 ≡ 9`, `12 ≡ 1`, and `14 ≡ 3 (mod 11)`, all quadratic residues. Thus only **21**, not 24, listed values define nonempty K-slices for T = {2,3,5,7}. `z67_k11_tbox.py` filters the free 11-component correctly when 11 ∈ T, but never checks the rigid q-component when 11 ∉ T. It reports an ambient box of 2520 residues even for these three empty K-slices. All 24 ambient slices really are covered, but three are irrelevant to K. Validate q as a T-unit and, when 11 ∉ T, validate its non-residue condition or explicitly report an empty K-slice. Similarly, the rigid probe q₁ = −1/2 has residue 5 mod 11 and is an outside-K control, not another K example.

6. **MINOR — I-3 needs an explicit distinction between a chosen root/class and existence of a suitable class.**
   `Z67_K11.md:101,104,108–109`: `f′ | 4c²d + 1` guarantees that root 1 is **available** modulo f′; it does not make every chosen root equal to 1 there. Example: S = {11}, c = 1, d = 11, f = 3. The I-3 class `41 mod 132` has root 2 modulo 3. All displayed table conditions hold, and its S-cylinder is γ ≡ 8 mod 11, but it does not catch e_{11,8}, whose 3-component is 1. The class using root 1 is `85 mod 132`, and that one does catch it. The proof already gestures at the correct existential interpretation. State explicitly that the table constructs classes with root 1 modulo f′ and arbitrary compatible roots modulo f_S; for a previously fixed class, check its actual root. This is a precision fix, not a failure of the union-of-family-events reduction.

7. **MINOR — The rational-profile probe does not test every class below MMAX as advertised.**
   `scripts/z67_k11_ratprobe.py:32–39` discards classes with v₁₁(m) > K or v₁₃(m) > J even when m ≤ MMAX. For example, the genuine II-2 class `−4 mod 11^5` (a = d = 1, c = 40263, modulus 161051 < 400000) is omitted at K = 4. The docstring and `Z67_K11.md:158–160` omit this restriction. Describe the brute portion as modulus- **and valuation-truncated**, or remove that extra cutoff for evaluating rational profiles. The 26 survivors reproduce for the implemented search, but they are upper-bound evidence, not a completeness certificate for all classes of modulus ≤ 400000. I have not shown that this omission changes the reported 26 pairs.

8. **MINOR — Rigid-probe “class counts” count parameter/family occurrences, not distinct classes.**
   `scripts/z67_k11_rigidprobe.py:84–86`, `rigidprobe_2e4.txt`, and the corresponding §3 bullets report 5, 3, 18, 4024 “classes.” Deduplicating by (modulus,residue) gives **4, 3, 13, 2382** respectively. In the first list, I-2 and I-3 both produce `9913 mod 15708`; the other lists also repeat parameterizations. Rename the counts “catching parameter/family occurrences,” or deduplicate. The script also prints only the first 12 occurrences, so the file is not a list of every catching class when the count exceeds 12. This does not invalidate any covering witness.

9. **MINOR — Open problem O3 is already a topological tautology.**
   `Z67_K11.md:284–285`: profiles equal to 1 outside a finite prime set are dense in Ẑ^×. A basic open neighborhood restricts only finitely many prime components; match those and put 1 elsewhere. Consequently their closure is the entire space, so U ∩ K̄ is contained in it without §3 or any ES input. This remains true relative to K̄. A nontrivial question would ask whether `U ∩ K̄ ∩ {finite-support profiles}` is dense **in U ∩ K̄**, or whether such profiles exist there at all.

10. **MINOR — The committed evidence is less complete than the CERTIFIED/replay presentation suggests.**
    `data/z67/k11/tree13_deep.txt` is empty. The deep table is reproducible (I reproduced every row), but the named data artifact supplies no evidence. Only q = 2 has a committed covering certificate; the other listed q values have neither committed certificates nor a replay loop in §9. `z67_k11_tbox.py` writes a certificate only with `--cert`, not automatically whenever survivors = 0. Preserve the deep output and covering certificates or an explicit batch replay/independent verifier. The same applies to the layer-mass numbers: document their normalization and duplicate-counting convention. These are reproducibility/wording defects, not failed numerical results.

## Proof checks that passed

* **Lemma R:** P ≥ 11 includes every constrained prime (2,3,5,7,11). Each B_P point extends to K̄ by arbitrary unit components outside P. Every family modulus is P-smooth for some P, so the closed decreasing Y_P have intersection K̄ ∩ U. Product compactness proves all three assertions. There is no missing K-box condition at the small primes. In §1, 1 mod 840 really does imply a local square at 2,3,5,7 (1 mod 8 at 2; Hensel at the odd primes). Theorem D applies to K as a finite union of primitive classes mod 9240, with the prime-tail/standard-numeral qualification from LOGIC2.
* **Lemma N:** For a prime f ≡ 3 mod 4, a = c = 1 and d = (f+1)/4 give an actual primitive ET II-2 class −1 mod f. ET §10's construction applies. Distinct primes give independent Haar events, of probability 1/(f−1). The divergent reciprocal-prime sum in the progression 3 mod 4 and Borel–Cantelli II prove μ(U) = 0. Omitting finitely many primes, or conditioning on K's small components, causes no problem.
* **Lemma M algebra:** For I-1, multiplication of `4na′²d′ + 1` by the unit `4d′C² mod f` produces `n + 4d′C² mod f`, since `4a′d′C ≡ 1`. For I-4 and II-1, the off-S residue condition is exactly e ≡ −1 mod 4a′b′. For II-2, `c(4a²d+1) − af = a+c` and gcd(c,f) = 1 prove the equivalence. I-2's two congruences give precisely f ≡ −1 mod 4(ac)′ and f′ | a+c. I-3's existential root reduction and II-3's two CRT conditions are correct, including mixed supports. Coprimality of the two modulus factors is part of the ET family hypotheses and must remain understood.
* **The q = 2 hand certificate:** gcd(152,55) = 1; 6481 mod 152 = 97 = −55 mod 152; 6481 mod 55 = 46; 46² mod 55 = 26 = −4·2²·19 mod 55. Also 8360 = 40·209, 6481 ≡ 1 mod 40 and ≡ 2 mod 209 = 11·19. Therefore every K-profile equal to 2 at primes ≥ 11 lies in this genuine I-3 class.
* **tbox logic for valid inputs:** The rigid test is exactly `rv ≡ u mod m_outside`; the small-prime compatibility and free-11 non-residue filters are correct. Requiring m_T | LEVEL makes each deletion a whole cylinder of the slice. The enumerated box residues are all unit residues compatible with K at that level. Consequently zero survivors really proves a finite covering of the full slice, not merely of its finite approximation. Larger omitted cylinders can only reduce survivors. All seven ET families are implemented correctly for this purpose. The omitted f = 1 cases of I-2/I-3 are −1 mod 4 and disjoint from K.
* **Fixed-P convergence:** The assertion that the raw measure series converges for fixed P is sound. For a fixed modulus m, the parameter counts are bounded by divisor-function factors, and I-3 has at most 2^ω(f) unit roots. Thus the number of classes is O_ε(m^ε) for any ε > 0. On the P-box their individual masses are O_P(1/m). For ε < 1, the sum of m^(−1+ε) over P-smooth m is a finite Euler product. This does not give the stronger uniform obstruction claimed in §4.
* **π° II-2 falsifier:** Put q = 4ad, A = qa, f = qc−1. Since gcd(q,f) = 1,
  `q(a+c) ≡ A+1` and `q(a+2c) ≡ A+2 (mod f)`.
  Hence the necessary product divisibility used by the script is valid. A+1 and A+2 are coprime, so the Cartesian product of their divisor lists generates **all** divisors of their product. The filter δ ≡ −1 mod q gives every positive candidate c = (δ+1)/q. The nested loops cover precisely a·d ≤ X, and the final exact-S-part divisibility tests are necessary and sufficient. N = 1 cannot catch: f | a+c would contradict f = 4acd−1 > a+c. Thus skipping it is sound. The scan is complete for the stated a·d bound, with no independent c or modulus cap. The square and (2,1) controls are also valid.

## Replays and numerical audit

Every numerical Python run used `uv run`, `ulimit -v 4000000`, and a timeout at most 900 seconds. NumPy runs used one OpenBLAS thread. No unconstrained Cartesian-product geometry/image computation was involved; the largest saved survivor array was about 11 MB. Original memo/scripts/data were not edited.

* Replayed the requested short tree `13,3,2,5,7,11,13,3,2` and the full §9 tree, and separately the LOGIC2 cross-check chain `13,3,17,2,5`. The latter gives exactly 2,6,5,13,18,57.

  | exponents (2,3,5,7,11,13) | reproduced open / B-residues |
  |---|---:|
  | 3,1,1,1,1,0 | 2 / 5 |
  | 3,1,1,1,1,1 | 6 / 60 |
  | 4,2,2,2,2,2 | 7136 / 1801800 |
  | 5,3,2,2,2,2 | 11685 / 10810800 |
  | 7,4,2,2,2,2 | 120231 / 129729600 |
  | 9,5,2,2,2,2 | 1316612 / 1556755200 |

  Final fraction: 0.000845741. Final modulus: 3116623910400. The stated final-digit losses round to 2.3%, 1.5%, 3.2%, 4.2%. All 32 residues 1 mod 16 modulo 512 occur. Mod 11 the final counts are 824033 at 2 and 492579 at 6; mod 13 they are 204278 at 2, 511154 at 3, 435266 at 4, 165914 at 7. Residue 1 mod 3,5,7 is forced by K, not an empirical preference.
* Replayed **all 24** listed four-prime q values at MMAX = 100000, level 2116800: each gives 0/2520 in the ambient box. Generated certificates and independently verified every family parameter, congruence, rigid condition, and box coverage, without calling the class enumerator. Each needs one class. Only 21 are nonempty K-slices (finding 5).
* Replayed T = {2,3,5,7,11,13}, level 103062960, MMAX = 100000: q = 4,9,2,3,−1 each gives 0/51480; q = 1 gives 161/51480. Independent certificate verification passed for all five covered slices. For example q = 4 has a five-class certificate: the usual three II-2 classes mod 11 cover residues 7,8,10; II-2 `(a,d,f)=(43,5,5159)` covers residue 2; I-1 `(a,d,f)=(46,517,3239)` covers residue 6. Here 5159 = 7·11·67 and 95128 = 8·11·23·47; the rigid residues are 4 at the outside primes.
* Replayed q = 1 at MMAX = 300000 and level 3091888800: 276/1544400. Entire stdout matches `slice_q1_T13.txt`.
* Recompiled the existing UCOVER helper, then replayed `z67_k11_ratprobe.py 400000 4 3 12`: 1048 brute cylinders, 11609 total, 69×182 pairs, 26 survivors. Entire stdout matches the data; all surviving pairs reduce to (2,2). Apply finding 7's completeness qualification.
* Replayed `z67_k11_rigidprobe.py 20000 2 1 1/2 1 6 1 -1/2 1`: entire stdout matches the data. Independently counted distinct (m,r) pairs as in finding 8.
* Replayed `z67_k11_pi0_ii2.py 100000`: **29 candidates, 0 π° catches, 0 square-control catches, one positive-control catch `(4,9,1,143,143)`**. Entire stdout matches `pi0_ii2_1e5.txt`.
* Independently recomputed the §4 layer sums using `classes_dividing({2:12,3:4,5:2,7:2,11:2,13:2}, tag=True)` and K-relative weight `φ(gcd(m,840))·(2 if 11|m else 1)/φ(m)`. This explains the printed approximate values exactly, but also their duplicate-counting convention (finding 4).

The cited Salez/Tao literature-search assertions and the universal negative “no published statement settles…” were not independently established by this bounded source review; they should not be read as a literature-exhaustiveness certificate. The mathematical and computational conclusions above do not depend on that claim.

## Second pass

Reviewed the entire `cb37dc179..8a40d474b` diff (one commit), including the actual scripts and certificates, not just §9's fix claims. **Verdict: the main mathematical repair survives; remaining proof-presentation, validation, and replay defects need correction. No new major mathematical counterexample found.** Memo not edited. **Model/provider errors: none encountered** (`openai/gpt-6-astra`).

1. **INFO — The new I-3/II-3 finiteness argument passes, including the delicate second case.** With fixed C,D,F, G = C²DF, elimination gives
   `s(4xyt−1) = 4Gx²y+F`, hence `s+F = 4xy(ts−Gx)`.
   Thus u = ts−Gx is an integer and is positive, and substitution gives exactly
   `x(4tyu−G) = u+tF`. The denominator is positive, and x ≥ 1 gives (*).
   For H := 4yu > F, `t(H−F) ≤ G+u`; since t ≥ 1, `u(4y−1) ≤ G+F`, bounding both y,u before t. For H ≤ F, y,u are bounded and
   `x−F/H = (u+FG/H)/(Ht−G) > 0` is exact. The stated η is the distance to the **next strictly larger** integer, so η > 0 even if F/H is integral. Consequently `Ht−G ≤ (u+FG/H)/η` is a valid effective upper bound, not merely an asymptotic assertion. Then x,z,s are determined; filter positivity, integrality, exact S-parts, coprimality and the finitely many roots modulo F. Replacing (c,d,f) by (a,d,e) proves II-3 too. No hidden unbounded parameter remains.

   The II-2 citation also transfers: dividing by c when a ≤ c gives `4adw ≤ 2N+w`, and `4ad−1 ≥ 3ad` gives the bound; the denominator determining c is positive. Swap a,c for the other ordering. No prime-power assumption on N is used. I-4/II-1's `4a′b′D−1 ≥ 3a′b′D` works for arbitrary N₁,N₂, including shared S-primes, and the opposite ordering is symmetric. I-2's analogous bound and positive denominator also pass. These searches may include extraneous tuples; exact family/S-part filters remove them without compromising completeness.

2. **MINOR — I-1 omits a symmetry step; the proposition's notation convention is false literally (§2).** The displayed I-1 argument treats only C ≤ w. Actual events with C > w exist: S = {11}, a = 1, d = 11, f = 15 gives n = 11, a′ = d′ = 1, C = 4, w = 1, and class 29 mod 44. The repair is immediate but should be stated: the equation is symmetric in C,w, so the same argument bounds d′Cw ≤ n/2 in either ordering. Do not discard the swapped solutions: they can give different residues. Integrality of w follows from `C(4na′²d′+1)−na′f = C+na′` and gcd(C,f) = 1; this too transfers to general n. Also “upper-case letters denote fixed S-parts, lower-case letters the S-free parts” is not a valid global convention: I-1's C and I-4/I-2's D are variable quotients, and auxiliary s,t,u,w need not be S-free. Restrict the convention to explicitly defined part variables. The finiteness theorem is salvageable without changing any bound.

3. **MINOR — Old finding 5 is only partly fixed: T-unit validation stops at 199.** `scripts/z67_k11_tbox.py:44–46` checks only primes below 200, contrary to §9's unrestricted “rejects non-units.” Reproduced with `100 211 3 1 1 1` and `100 1/211 3 1 1 1`: both are accepted and print `0/1` survivors, although neither defines the advertised unit profile at 211. Strip all T-prime factors from |numerator| and denominator and require residual 1 (reject zero). The residue warning for q = 12 does work. All 26 committed certificate inputs really are T-units, so this does not invalidate those coverings.

4. **MEDIUM — The new batch replay fails open.** `scripts/z67_k11_slices.sh:4,9,13` uses `set -e` but no `pipefail`; a failed or timed-out Python/uv command is hidden by successful downstream `sed`. With a temporary mock uv that always exits 42, the **entire batch exits 0**. Also positive survivors do not make tbox fail, and `--cert` leaves an existing certificate untouched in that case, allowing stale certificates to survive an unsuccessful rerun. Propagate pipeline errors and explicitly require successful zero-survivor runs with fresh certificates. This is a reproducibility defect, not evidence that the committed certificates are wrong.

5. **MINOR — Old findings 8/10 retain misleading prose despite correct artifacts.** §3 still says the rigid-probe file “lists the catching classes”; its docstring says “Lists every catching class found.” It prints only the first 12 **occurrences**, not all 13/2382 distinct classes in the last two cases. Counts and output headers are now correct. Likewise §3's “the script writes [the covering] out” remains conditional on `--cert`, not automatic. Say so. The empty tree artifact really was removed; the replacement tree, 26 certificates, replay output and layer-mass normalization are present.

6. **MINOR — Residual necessity language still exceeds the scoped conclusion.** §4(ii) says the route “needs” θ < 1/2 immediately before calling it sufficient and not proved necessary; §7 and its FRONTIER text repeat “needs,” and FRONTIER retains “any certificate lives on a null slice.” Use “would be sufficient for this estimate” and “cannot establish positive ambient Haar mass,” respectively. O2's “needs a König argument” likewise describes a proposed route, not a proved necessity. These leftovers do not undo the substantially improved scoping, but §9 overstates the completeness of that cleanup.

**Fix audit / verification.** Old findings 1, 3, 6, 7 and 9 are substantively fixed; 2 is mathematically repaired subject to item 2 above; 4 is substantially fixed with item 6's leftovers; 5, 8 and 10 have the residual issues above. Independently checked all **26 certificates / 39 class entries**, including family equations, exact rigid congruences, unit inputs and full finite-box coverage, without calling the enumerator. Replayed the full deep tree and the four rigid profiles: stdout matches the committed files byte-for-byte. Shell syntax and `git diff --check` pass. Runs used uv, 2–4 GB virtual-memory limits, timeouts, and one OpenBLAS thread; certificate coverage was streamed, not built as a class-by-residue array. No full batch recomputation or unchanged rational-profile/π° scan was needed for these changes. K̄ ∩ U remains undecided; the finite evidence and Proposition M′ do not supply its missing tail certificate.

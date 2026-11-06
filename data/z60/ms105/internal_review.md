# Hostile internal review — Z60 MS105

**Verdict: revise before integration.** The stated **univariate Theorem 3(b), Claim 0, Lemmas 1–2, Proposition 4, and the complete §2.1 kernel census survive review**. The main problems are stronger claims made around those results, an incorrect auxiliary counting engine, and inaccurate FRONTIER wording. Nothing establishes ES or (MS⁺₁₀₅).

Reviewed working-tree `Z60_MS105.md`, SHA-256 `ffc409ad8e82e90a4e98c4846909eeae55761ba1cbb92c1810823d731b2f109a`. Ignored `FILLRESULT` and did not require the live R₈ run to be complete. All review computations were sequential, memory-limited to 4 GB, and individually time-limited to at most 120 seconds. No production census was rerun in full.

## MAJOR

**M1 — §4 Remark (iii), §7 “non-algebraic” conclusion: non-squareness is not preserved by composition.**
`f(t)=4t+1` is non-square, but `h(t)=t(t+1)` gives `f(h(t))=(2t+1)²`. Thus `Z_f` does contain an infinite polynomially parametrised subfamily. The parenthetical “f∘h is again non-square” and the unqualified deduction that every thin zero family is non-algebraic are false. **Fix:** require explicitly that `f∘h` is non-square (and nonconstant/eventually positive). Say only that no polynomial taking non-square values eventually can consist entirely of zeros. Do not assert closure of non-squareness under substitution.

**M2 — §4 Remark (i), §7 structure bullet and proposed FRONTIER: unsupported extensions of Theorem 3.**
The several-variable assertion is neither formulated with a positivity domain/density convention nor proved by the displayed finite-extension argument: `Q(t₁,…,t_k)/Q(f)` is not finite when `k>1`. Arbitrary multivariate polynomials also have positive-density negative-value regions, e.g. `t₁²−t₂²` on `[1,T]²,` where there are no positive solutions. The FRONTIER statement additionally drops “nonconstant with positive leading coefficient”; the nonsquare constant `f=409` directly contradicts it. **Fix:** retain the precise univariate hypotheses in every exported theorem and withdraw the multivariate claim pending a separately stated and proved extension. Restriction to a nonconstant positive-step arithmetic progression is fine: a nonconstant affine substitution preserves being a square/non-square in `Q[t]`.

**M3 — `scripts/z60_ms105_prim.c:15`, §5.1, `prim_2e7.txt`: the supposedly exact R enumeration omits solutions.**
The outer condition `4*u-2 <= N` is wrong. Taking `B=C=1` gives `n=3u-1`, so the necessary outer range is `3*u-1 <= N`. Already at `N=17`, `(6,1,1)` is omitted and the internal R(17) count is 1 rather than 2. I changed only this condition in a temporary copy and reran `N=20000000`:

| group | stored mean R | corrected mean R |
|---|---:|---:|
| prime | 41.000 | **41.118** |
| composite | 39.826 | **39.954** |

Counts 635169/1649523, zeros 14/23, the six inheritance-only integers, and mean imprimitive count 0.6679 are unchanged; the rounded 1.7% share remains valid. **Fix:** correct the loop, regenerate the artifact, and replace §5.1’s means by 41.1 and 40.0 (or the three-decimal values). This is a systematic omission, not rounding.

**M4 — §5.1 opening, §7 assessment/bottom line: “ascent is exactly inheritance” overclassifies all possible constructions.**
Lemma 2 classifies the particular simultaneous scaling `(u,B,C)→(gu,gB,C/g)`, not every way of obtaining a product witness from a factor witness. Concrete counterexample inside the coprime-to-105 domain: `(1,6,1)` solves R(17); multiplying by 37 gives the primitive witness `(1,210,1)` for R(629), via `210=37·6−(37−1)/3`. More generally, a witness with `u=C=1` transports this way whenever the multiplier is 1 mod 3. This is not an imprimitive lift and needs no multiplier dividing C. It does not solve the research problem, but it disproves the unrestricted classification. **Fix:** consistently say “the simultaneous-scaling lifts are exactly the imprimitive solutions”; restrict the no-help bound on the small factor and the C-divisibility requirement to those lifts. Replace “composite-only proof routes collapse” by a statement about the specific routes examined.

**M5 — §6 second bullet, §5.2 sieve barrier, §7 bottom line: necessary conditions are promoted to impossibility theorems.**
`depth(n) ≤ d_min(n)` correctly implies that a uniform polylogarithmic witness bound would imply a polylogarithmic least-nonresidue bound. It does **not** imply that every proof must use GRH-type input or allow witnesses beyond every unconditional nonresidue bound; an unconditional improvement is not logically excluded, and positivity need not come with a polylogarithmic bound. One finite pseudosquare with first hit 431 versus depth 379 does not establish a scale-separation theorem. Likewise “finiteness would need” moduli `n^{2/3}` and “beyond any sieve range” are not proved. The `n^{2/3}` bound in Z58_WITNESS concerns the least of three different moduli, not the displayed prime-d sieve alone. **Fix:** retain the conditional implication about polylogarithmic bounds; label the rest as limitations of currently available methods, not requirements on every proof. Remove the universal sieve/GRH/scale conclusions.

**M6 — §7 proposed FRONTIER numerical sentence: the exported certificate is false as written.**
“No zero … near squares … the 52 pseudosquares” includes known zeros: `409=21²−32`, and pseudosquares 2641 and 18001. Moreover `|c|≤200` is a larger offset domain than the 50 offsets actually run. **Fix:** say “no zero **above 29210401** in the tested domains,” with `c∈±{8,16,…,200}`, odd `m≤10⁹`, and the stated coprimality/non-square filters. Keep the explicit finite exceptions when discussing all inputs. The same qualification is needed for §2’s “no rigid obstruction anywhere” if meant literally rather than as an eventual-positivity assessment.

## MINOR

**m1 — §2.4 and §6: two incorrect pseudosquare numbers.**
For `L≥87481`, stored/replayed hit counts range over **8–44**, not 12–44: 117049 has 8 hits and 936664079266714697089 has 10. The last value 4235025223080597503519329 is **OEIS A002189(73)**, not `L₅₁`; 51 is its index after deduplicating the table. Original A002189(51) is 1773855791877850321. **Fix:** use 8–44 and call the final value A002189(73), or define a distinct-value indexing convention explicitly rather than mixing it with the first-k-primes definition.

**m2 — §2 evidence paragraph: the 15–30% reduction is not a per-input or all-family conclusion.**
The small-kernel/window/near-square engines stop at the first hit and do not measure hit-count reductions against controls. Pseudosquare reductions vary greatly: 117049 has 8 hits against a control mean of 31 (74% lower), and some pseudosquares exceed their control mean. Moreover additive controls `L±840·10⁶` are not size-matched for the small L values; e.g. controls for 17 are mostly of size 10⁸. **Fix:** scope the percentage to group means of the pseudosquare/locally-square experiments, disclose the small-L control-size problem, and either restrict the size-matched analysis to large L or regenerate genuinely size-matched controls. For `L≥87481` the pooled means are 23.1136 versus 33.1534 (30.3% lower); locally-square deficits are about 11–17%.

**m3 — §5.3 after Proposition 4: “exactly” reverses a necessary implication.**
Opposite symbols do not suffice for a hit. At `d=7`, `a=29,b=17` have symbols +1 and −1, but `ab=493≡3 (7)` is not a hit: `r=4` does not divide `(d+1)/4=2`. **Fix:** replace “exactly at moduli where” by “only at moduli where”; retain the additional tied-divisibility condition.

**m4 — §0 F2: Lemma 2 does not hold verbatim for R₈ on its stated all-positive-integer domain.**
Under the inverse map, `C=C′/g` must remain even. `C′` even and `g|C′` do not suffice for even g. For example R₈(12)=0, but the proposed g=2 term includes the primitive R₈(6) solution `(1,1,2)`, whose inverse `(2,2,1)` has odd C. **Fix:** require `2g|C′`, or explicitly restrict this assertion to odd n, when every g is odd. Also qualify the F2 polynomial claim by Remark (iv)’s exceptions: R₈ is not density-zero along `f=2t²`.

**m5 — §1 “a single zero … not (MS)”: too categorical.**
A zero above the MS⁺₁₀₅ threshold need not refute (MS), but one which is a prime in the MS residue domain above its threshold would refute both. **Fix:** say “refutes (MS⁺₁₀₅), but need not refute (MS).”

**m6 — engine range guards, outside the production ranges.**
`sm2w.c` forms `(u128)s*m*m` before its overflow check, although accepted individual limits `s<2³¹,m<2⁶³` allow a 157-bit product. A wrapped product can pass `n>>126`; the same general pre-multiplication issue exists for unconstrained sm2 arguments. `dec128.c` silently wraps oversized decimal input while parsing; nsq accepts arbitrary signed c without checking that the resulting n fits u64. **Fix:** check multiplication/addition/decimal accumulation before performing them and reject out-of-contract inputs. This does **not** invalidate this census: I checked the actual kernel endpoints and window/sample magnitudes; their arithmetic fits the declared widths.

## NIT

**n1 — §3 attribution and §5.3 novelty.** Claim 0 is the same reciprocity calculation as Z59_MSPF Lemma 1.3 (also Z57_BFII Lemma 2.1); the explicitly named `χ_n(d)` assertion is Z59_MSPF **Lemma 1.5**, not 1.3. Lemma 1 is a useful corollary, with the same kernel-sign contradiction already used in Z58_WILDCARD Lemma 4.3. Proposition 4 is another immediate corollary of the same hit-class sign fact. **Fix:** correct the lemma number and cite that source at Proposition 4; describe these as corollaries/repackaging, not new obstructions. Lemma 2’s existing attribution to Z59_MSPLUS Lemma 5.1 is adequate. Searches found the `s·t²` theorem in Z59_MSPLUS Lemma 4.1, but no earlier equivalent of the full univariate Theorem 3.

**n2 — §8 reproduction / runner exit reporting.** The literal commands `scripts/z60_ms105_dec128.c 10000000` and `scripts/z60_ms105_prim.c 20000000` do not execute C source. `sm2_big.sh` needs the output-directory argument omitted in §2.1. The window runner turns a failed engine into `echo FAIL` and can then append `EXIT 0`; the big runner’s advertised timeout is not implemented. **Fix:** provide explicit compile-and-run commands, the third shell argument, and propagate failure/timeout status. All retained completed census files nevertheless pass the independent coverage checks below.

**n3 — §0 F4 / hit-count comment.** “Every UNK of every run” must say “every R-run”: the intentionally different R₈ control has other UNK values. In `dec128.c`, the exact interpretation is “number of ordered solutions whose d≤LIM,” not a lower bound for “R/2-ish.” **Fix:** use those precise scopes.

## Proof audit: what passed

- **Claim 0:** `gcd(t,d)=1`; the 2-part is +1 when present, and the two reciprocity signs for the odd part cancel. This includes t=1.
- **Lemma 1:** `gcd(d,n)=gcd(d,u)=1`, hence `(m/d)²=1`; `(n/d)=(s/d)=−1`. Absorption of s in uC forces the contrary sign +1. Swapping u and B is legitimate. For `g=gcd(s,uC)`, Claim 0 gives `(g/d)=1`, proving the sharpened statement even without squarefreeness. No counterexample found.
- **Lemma 2:** dividing by `g=gcd(u,B)` gives exactly `(u/g,B/g,gC)`, with `g|n`, and the stated inverse is exact. Terms with `s|g` vanish by Lemma 1. Plain R version is correct; see m4 for R₈.
- **Proposition 4:** correct as a necessary-condition/anti-multiplicativity statement for the same d, including composite d. It gives no sufficiency result.
- **Other §5 proved pieces:** `C≤(a+2)/4` is valid, so the small-factor exclusion is valid for the specified scaling lift. In a fixed admissible kernel class and at a prime d with `(s/d)=−1`, the distinct divisors r of `(d+1)/4` give exactly `2τ((d+1)/4)` distinct m-classes; such primes have relative density 1/2 among d≡3 (4). The §5.4 progression union, its positive-C cutoff, and its exclusion of squares are correct. These facts do not establish the broader no-go conclusions flagged above.
- **Theorem 3, step 1:** `f(t)+u` is irreducible over `Q(u)`; α is transcendental over Q and `u=−f(α)`, so `K=Q(α)` really is rational with constant field Q. The square criterion is over **Q(t)**, not the algebraic closure. Thus `f=cg²` with nonsquare rational c is correctly in case (b); repeated factors of f cause no problem, since `f+u` is separable generically.
- **Step 2:** use a finite étale open subset and full-fibre specialization of the entire Galois closure. This preserves the root permutation action, stabilizer, and the two normal-subgroup non-inclusions, not merely an abstract isomorphism of Galois groups. It works even though M has a nontrivial constant field. Serre Proposition 3.3.1 requires K-irreducibility, not geometric irreducibility. Cohen’s `O(√N log N)` exceptional count is smaller than the number of primes q≡3 (4), so a suitable positive prime exists.
- **Step 3:** the 2-Sylow of `C₂×C_{q−1}` is elementary abelian for q≡3 (4). Nontrivial complex conjugation in its quotient is detected by a quadratic character. The only imaginary quadratic subfields of `Q(ζ_{4q})` are Q(i) and Q(√−q). Both were excluded, so F is real.
- **Step 4:** restriction from `Gal(N/K_q)` has image `Gal(Q(ζ_{4q})/F)`. A lift of complex conjugation fixes α_q; every conjugate fixes some root, while its cyclotomic restriction stays complex conjugation. Away from the listed finite bad primes this gives a root mod ℓ and ℓ≡−1 (4q). Chebotarev gives positive prime density and divergent reciprocal sum.
- **Steps 5–6:** C and B are positive integers once `f(t)+q≥ℓ`, and the displayed identity is exact. For each fixed z, eventual positivity removes only finitely many t; CRT gives the stated density product. Taking T→∞ before z→∞ proves density zero.
- **Case (a):** correct, and weaker than the actual T1 fact: all positive square arguments, even as well as odd, have R=0. **Remark (iv):** the analogous univariate argument works after adjoining the four listed imaginary square roots and excluding f and 2f squares. The 2-Sylow of `Gal(Q(ζ_{8q})/Q)` is `C₂³`; no missing imaginary quadratic field was found.

Source verification: I read Serre’s actual §3.3 and Theorem 3.4.4 in the [Harvard-course notes PDF](https://www.ms.uky.edu/~sohum/ma561/notes/workspace/books/serre_galois_theory.pdf). The cited HIT/Cohen statements match their use. I also checked the original [OEIS b-file](https://oeis.org/A002189/b002189.txt): the stored list contains exactly its 52 distinct values.

## Numerical audit: reconciled results

| data | summary rows | input occurrences | UNK occurrences / distinct n | largest first d |
|---|---:|---:|---:|---:|
| `sm2/*.txt` | 106 | 6086436506 | 2 / 2 | 3048771 |
| `sm2big/jobs/*.out` | 10955 | 61785619898 | 14 / 14 | 6637967 |
| `win/*.txt` | 848 | 3876571898 | 0 / 0 | 2512619 |
| `nsq/*.txt` | 50 | 11361904661 | 27 / 15 | 15110783 |

- Kernel total **67872056404**; total of these four rows **83110532963**, so the approximate `8.3·10¹⁰` workload is right (input occurrences, not a claim of pairwise distinct n across experiments).
- Independently regenerated the **11061** admissible squarefree kernels and checked every S-line endpoint against `isqrt((2⁶⁴−1)//s)`, every odd/coprime-m count by inclusion–exclusion, and exact kernel coverage with no duplicates. All 16 large-job exits and four small-lane exits are zero. Thus §2.1’s complete-domain **CERTIFIED statement is justified**: n≡1 (4) forces odd m and s≡1 (4), coprimality factors through s and m, and no admissible nontrivial kernel below 13 was omitted.
- Checked all 848 window/kernel pairs against the eight prescribed intervals. Independently computed all 50 near-square input counts using residue classes mod 210 and exact small-m square/positivity corrections. No missing interval or offset.
- Kernel UNK union is exactly the stated 16. Near-square distinct UNK list is **409, 577, 1969, 2641, 2929, 5161, 5569, 9601, 12001, 23881, 23929, 25441, 83449, 1134241, 12538801**. Every R-run UNK, including the two pseudosquares, belongs to the 38-row reference list. All these particular UNK have LIM above the complete d bound; this is not treating arbitrary large-LIM misses as zeros.
- Reference zeros agree with the filtered z58 gzipped census; factorizations/kernels check, with **14 primes, 24 composites**, **27 below 10⁶**, maximum **29210401**, and only **752257=6217·11²** non-squarefree. Their depths span **5–37**. Also replayed all 38 through sm2 at LIM=10⁸: all are UNK, with a complete scan bound at each n.
- Reverified every stored L-line witness and every S-line maximum witness using Python integers. Independently replayed the four extremal first hits: `(s,m)=(949,121061833)`, `(92989,10060349)`, window `(37,10013243339)`, near-square `(c,m)=(48,760301293)`. All four first-hit records match.
- Pseudosquares: **52+1040=1092** inputs; exactly **2641 and 18001** are UNK. All others hit. Depths for the selected `L≥87481` subset are **29–379**; control-mean extrema **30 and 38.05**, control-minimum extrema **9 and 25**. Last pseudosquare first hit **431**, depth **379**, hit count **31**. See m1 for the incorrect quoted hit minimum/index.
- Locally square: **500+500=1000** inputs, no UNK, maximum n **421756856582670009118236823802063329**. Means (LS/control) by y=47,59,71,79,83 are **28.66/33.89, 29.03/33.47, 27.44/32.18, 27.62/33.40, 28.91/32.33**. Every LS input is a nonzero square at every prime ≤y and in the required mod-840 classes.
- Both Python generators reproduce their input files byte for byte. Rerunning dec128 on **all 2092** pseudo/locsq inputs reproduces every first-hit/count output line exactly; the only file difference is the stored shell `exit 0` footer. All recorded depths were separately recomputed.
- Primitive census: corrected-engine full rerun at 2·10⁷ confirms all six rescue values **8569, 20689, 115489, 174841, 4264249, 10865569**; only the mean-R claims change (M3).
- R₈ spot checks independently reproduce the four cited s=29 late witnesses: m **140827093, 174741683, 383394787, 472803077** give first d **128300223, 145290191, 102600159, 100345783**. These are witnesses, not certified zeros. Live partial-run UNK totals/maxima were not frozen or graded.

## Engine and small-brute-force checks

The d-form is genuinely complete: in any solution, `u≤(n+1)/3` and `d=(n+u)/B≤(4n+1)/3`; also `u<d`, hence `u=(-n mod d)`. Conversely every scanned hit gives the unique positive ordered solution at that d. For R₈ the additional predicate is exactly `d≡7 (8), r|(d+1)/8`. The production limits, modular products, square tests, and witness-verification arithmetic are safe; no production off-by-one or overflow failure was found in sm2/sm2w/nsq/dec128. The reduced verification in sm2w/nsq/dec128 (divisibility plus `4uC−1=d`) is algebraically sufficient.

Reran the existing 6000 lemma check: **78200 (solution,s) pairs, zero violations**. A separate exhaustive positive-triple enumeration through n=10000 found **95948 solutions**, tested **147103 (solution,s) pairs**, **18210 Claim-0 instances**, and **11147 ordered same-d hit pairs**, with no counterexample to the proved lemmas. It checked the decomposition map and the sharpened kernel sign, compared complete d-form solution sets for every n≤1000, and made **1640** small-input comparisons against the compiled sm2, sm2w, nsq, dec128 and R₈ engines. All passed. The separate prim.c counterexample and corrected full rerun are recorded in M3.

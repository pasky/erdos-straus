# IDEAA hostile cross-review

**Verdict: ACCEPT-WITH-FIXES. ES is OPEN.** Accept the numerical results and scoped null outcome, not a blanket closure of the 21 directions.
Reviewed `side-agent/z69-ideaa` at `5f4c3cc68628262e6e6b196a43587f8f2d2f2aa6`, including scripts/data and cited repository entries via `git grep`/`git show`.
**No provider/auth/quota error occurred.** All computation used `ulimit -v 6000000`, timeouts ≤1800 s, and one compute process at a time (NumPy BLAS restricted to one thread).

## A. Per-claim audit

| Claim | Classification | Independent result / correction |
|---|---|---|
| Lemma T(i)–(ii), Artin symbol equals norm residue | CORRECT | Re-derived below. Total norm −1 supplies the trivial B=1 hit; total norm +1 supplies no odd-inert-parity conclusion. |
| Lemma T(iii), conductor hypothesis | CORRECT | Finite relative ramification disappears when the conductor is not a prime power; principal reciprocity gives the signed-norm congruence. |
| Ramified counterexample m=8 | CORRECT | Independently checked: 9−2·93²=−17289, 17289=3²·17·113=8·2161+1; 2161 prime, ≡1 (24); no divisor is 7 (8). |
| “CM reciprocity can force the class only trivially” as a general no-go | GAP | The lemma identifies a character with a residue; it does not prohibit forcing a proper ideal divisor with that character. Restrict the conclusion to the total-norm/sign argument actually attempted. |
| Type I/II identities | CORRECT | Clearing the common denominator gives respectively 1+pe=4abd and p+e=4abd. Both also checked exactly on all six extreme-prime witnesses using arbitrary-precision integers. |
| T2 subrange census | CORRECT in checked range | Independent ordinary prime sieve + prime-by-prime direct congruence search: 719781 primes ≡1 (24) through 10⁸; all 137 available joint/marginal survival cells agree with the archived decade sums. Max joint K=2388 at 66306529; marginal maxima I=9499, II=7348. |
| T2 extreme minima | CORRECT | Exhausted all smaller products: K(1775179561)=5777, K(2431459801)=4460, K(278893729)=3657, K(7183201)=1133; II(6106475761)=35967; I(3280856329)=22628. Primality checked by trial division. |
| Entire 10¹⁰ census / 56876600 primes | SUPPORTED, not independently duplicated | Engine inspection found no counting error; full-range exhaustion remains one engine. Do not upgrade that scope based on this review. |
| T2 fits / largest 14 logged representatives | CORRECT as EVIDENCE | Replayed `kfit.py`; regenerated JSON is byte-identical, including j≈2.28 and the Mordell/QNR profiles. Fits do not establish a tail theorem, search lower bound, or unprovability. |
| T2b dependence | CORRECT | From full-range integer counts, ratios at Q=5,21,68,108,421,1031,3152 are 0.888874,2.19410,8.71944,11.1047,52.8108,148.547,660.174. θ endpoints over the stated positive-dependence range round to 1.215–1.420. Positive joint counts refute guaranteed same-cap rescue; covariance alone does not refute eventual coverage. |
| T1 dictionary experiment | CORRECT as EVIDENCE | Replayed both UMIN runs; JSON byte-identical. Interior R²: .578,.391,.373,.281,.145; odd-square W⁻₄=0. One finite dictionary is rejected, not all signed-count identities. |
| Gaussian lemma / slice criterion | CORRECT | Factorisation and all unit cases re-derived below. Independent actual-divisor/cofactor tests, rather than residue-set propagation, reproduce the entire T3 sample. |
| T3 counts / kill | CORRECT, narrowly scoped | Exactly 1015/20000 vs 4176/119826, ratio 1.45621875. The precommitted point-estimate kill fires; not a statistically established ≤1.5 population ratio. Paired-prime delta-method 95% interval: [1.364,1.549], or [1.409,1.503] with finite-population correction for 26969 eligible primes. |
| ALG-SLICE e=p−2 / QR-FLOOR | CORRECT | Odd prime factors of ab on the minus slice divide p−1; p≡1 (8) makes p a square modulo 4ab. This contradicts `JOINT_BUDGET.md` Remark 4.4. Likewise QR at all odd primes ≤y lifts to 4ab whenever its odd prime factors are ≤y (p≡1 (8) handles 2), contradicting that remark. |
| ALG-SLICE e=p+2 | EVIDENCE ONLY | Independently extended emptiness to all 19552 primes p≡1 (8), p≤10⁶. Still no proof of sterility; “dead” must not turn this into one. |

### Proof reconstruction
For a prime ideal of K⁺ over ℓ∤m, let r be the order of ℓ in (ℤ/m)×/{±1}. Its norm is ℓʳ≡±1, and its relative Frobenius is exactly that power; multiplication proves T(i) for all integral ideals prime to m. Thus Art=−1 implies N𝔞≡−1, proving T(ii), but not nonexistence of a useful proper ideal divisor.
For conductor f not a prime power, at each finite prime the cyclotomic inertia subgroup fixes a nontrivial prime-to-that-prime cyclotomic part; complex conjugation does not. Hence inertia intersects {±1} trivially. Principal reciprocity then gives Art((γ))=∏σ sgn σ(γ); combine with N((γ))=|N(γ)| to obtain signed N(γ)≡1 (m). For m=10 the displayed unit has norm −1; for m=8 the checked example demonstrates why finite local symbols cannot be dropped.
For the Gaussian equation, (2α−π)(2β−π)=π². Since π≡1 (2), units ±i fail integrality; ±1 with exponents 0,2 give the two signed pairs and their swaps, while exponent 1 gives the diagonal or the excluded zero pair. Norm expansion gives e=1±2a. Finally (ey−M)(ez−M)=M² proves the stated slice criterion, with gcd(M,e)=1 ensuring the cofactor congruence.
For Type I fixed coordinates at a prime p, set m=a and f=4acd−p. Positivity gives c<p, hence gcd(c,f)=gcd(c,p)=1; the equations give f∣4a²d+1 and f≡−p (4ad). Conversely c=(p+f)/(4ad), b=(p(4a²d+1)/f+1)/(4ad), e=(4a²d+1)/f reconstruct the positive point. Square d is sterile, but algebraic factorisation does not require square d.

## B. All 21 dismissals audited

“Prior” below means the named passage was inspected, not that a prior conjecture or experiment proves impossibility.

| # / idea | Judgment on dismissal and checked prior |
|---|---|
| 1 CPLX | JUSTIFIED as no new reduction. `Z58_LOGIC` Thm 3.1 is explicitly relative to Buss witnessing; `OMEGA13` Thm 5.1 concerns W, not K. `FOREST_H4` §5 and `Z58_WITNESS` §2.1 contain the tail methodology. No complexity no-go follows. |
| 2 IDENT-OE | JUSTIFIED only for this dictionary. `STRONG_APPROX_ES` Thm 9.1 concerns finite n-local Eisenstein combinations, not every fixed-level or shifted identity; §9.1 really has the 150-column experiment. The different signed count is not thereby exhausted. |
| 3 INV | JUSTIFIED at equal tested caps. `POINTWISE_MORDELL17` Lemma 1.1 contains U/U⁻¹; `Z60_LOPEZ` Prop E concerns the related U branches. New depth-resolved counts are useful, not a general complementarity obstruction. |
| 4 TRACE | JUSTIFIED withdrawal. Independently reproduced local inversion at 7: modulo 2884 the new residue is 2865=−19; trace unchanged, ab=721 hits, original p does not hit there. |
| 5 TORUS | JUSTIFIED as certificate-only. Cyclic norm-one group and supersingular order d+1 give the stated equivalences; CRT gives the exponent when d,d′ are distinct primes. `y3_lucas_dickson_trace` Prop G is genuinely related; Z1958 is only the much weaker prime-level anti-certificate, not this torus calculation. |
| 6 SIGN | PREMATURE beyond total norms. T is sound; the universal reading is not proved. `Z60_RAYCLASS` §3 explicitly exempts extra information on a particular ideal-divisor set. See next steps. |
| 7 GAUSS-SPLIT | JUSTIFIED as “not a universal rule”; NOT killed as an enriched selector. `Z58_WITNESS` tests different two-square selectors. The matched-control follow-up already suggested in the memo remains legitimate. |
| 8 LYNESS | CORRECTLY LEFT OPEN in its own paragraph; inconsistent with the blanket summary. The invariant and four-neighbour identities check. `z52b_translate` #49 and `y2_zamolodchikov_forcing` concern the twisted period-5 version, not a no-go for this autonomous elliptic pencil. |
| 9 E₂-FORM | JUSTIFIED restatement: the two-fraction factorisation above gives both directions and the k identity. No additional forcing lemma was proposed. |
| 10 TYPE-I-FIXED | PARTLY WRONG closure. Square-d sterility agrees with `SYNTHESIS_SPARKS8` Lemma 4.1, but “algebraic factorisations need d square” is false as a general statement. Explicit successful nonsquare-d example below. |
| 11 ALG-SLICE | JUSTIFIED minus-slice theorem; PREMATURE plus-slice closure. `JOINT_BUDGET` Remark 4.4 proves the former, not the latter; the expanded census is still finite evidence. |
| 12 SUBSET-COVER | GAP / PREMATURE. “General position” is undefined; Olson/Erdős–Heilbronn do not give the stated logarithmic deterministic guarantee as written. A whole-group coverage threshold is not necessary for hitting one target. `z31_zero_sum` distinguishes logarithmic random, square-root spread-set, and linear worst-case scales. |
| 13 SIEVE-FL | JUSTIFIED obstruction to the naive free-variable argument, not a sieve no-go. C≡−(4p)⁻¹ (d), together with C≤(d+1)/4, leaves at most one C for fixed d. That does not exclude a new argument summing over d. |
| 14 MONOID-DESCENT | JUSTIFIED identities, unsupported “board killed” attribution. Multiplying a −1-factor pair by a +1 integer preserves it; division by a +1 prime removes it from one factor. `git grep` finds no tracked astra-4 source beyond this memo. Actual prior: `z52b_translate` #265 / `ES_CONNECTIONS_TODO` Z2847, not a universal descent no-go. |
| 15 RSR | JUSTIFIED “open, empty.” `Z59_CONV2` Prop 4.1 only excludes equation-scaling monomial transports; the memo correctly identifies a genuinely new link as the missing ingredient. |
| 16 UNDEC | JUSTIFIED speculative status; no theorem or concrete reduction supplied, hence no established route to dismiss. Variable counts alone are not an impossibility proof. |
| 17 INVERSE-SIEVE | JUSTIFIED for the unadapted standard theorem, not all inverse methods. Sparse H_d is the obstacle. `Z58_LADDER` does not itself prove an inverse-sieve no-go; `bsL_sieve_saturation` is a better scoped reference and distinguishes larger orbit families. |
| 18 TIE-LADDER | JUSTIFIED exact prior. `Z59_CONV2` Lemma 1(v), Prop 2.1 and Prop 4.2 give C=g²d′, modulus 4C/g, c=g. Linnik with a free C does not restore that tie. |
| 19 4-TERM-MERGE | PREMATURE as a no-go. Equivalence is elementary (split a unit fraction into two equal halves), but “polylog count” is unsupported and lacks a defined cutoff/statistic. Prior proposals exist in `z52b_analogues` #312 and `z52b_upgrades` #208; neither closes structured merging. |
| 20 MIRROR-SIZE | JUSTIFIED as the stated Assessment, not an impossibility result. Same inversion as #3 with different positivity/size restrictions; no extra mechanism is supplied. |
| 21 QR-FLOOR | JUSTIFIED prior substance. `JOINT_BUDGET` Remark 4.4 yields the bound; `Z58_LADDER` Lemma 1.1(c) gives the analogous least-nonresidue floor. It does not explain or bound the measured residual tail. |

## Possibly-premature dismissals: concrete next steps

1. **#10:** With d=4m²k²−2k, 4dm²+1=(4m²k−1)². At m=1,k=6, d=132 is nonsquare; p=1033≡1 (24) has (a,b,c,d,e)=(1,45,2,132,23). This is only an ordinary ET congruence family, not a new mechanism, but refutes blanket algebraic sterility. Separate square-d from nonsquare-d factorizations and test any claimed general obstruction against this fixture.
2. **#6:** State the exact total-norm-only no-go. A stronger proposal must supply a new lemma forcing an Artin−1 proper ideal divisor without assuming its norm/factorisation; screen that lemma first at 409 and the R₈ zeros. T alone does not forbid it.
3. **#11:** Replace “dead” for e=p+2 by “empirically empty, unproved.” The exact remaining obligation is: M⁴ has no divisor ≡−M² (mod 2M+1), M=(p+1)/2. Prove this or find a counterexample; the checked range is now 10⁶.
4. **#12:** Specify the target-specific subset-product theorem and its deterministic hypotheses before using a primorial budget to kill it. A single target can be hit by one factor; ω≳log₂(4u) is not necessary. Quantify only the actual construction's forced length/spread.
5. **#7/#8:** If revisited, match Gaussian/control slices on divisor availability, φ(e), and local factors; for Lyness, choose K(p) independently of a known word, then test integral neighbours on F1–F4. Existing experiments do not settle either modified question; neither is a HOT LEAD now.
6. **#13/#19:** A restart needs respectively a specified tied-incidence sieve weight, or a four-term construction with a forced merge/divisibility invariant. Uniqueness of C or equivalence to ES is not a proof that such constructions cannot exist. Delete the unsupported polylog count.

## Falsifier-table audit

| Screen | Result |
|---|---|
| F1 odd squares | Correct restricted-family obstruction; not failure of ES at squares. T1 replay checks W⁻₄=0. Write O₄=−E₄ explicitly: the unrestricted all-level O is not constrained that way. The Gaussian square slice and global inversion respect T1. |
| F2 numerator 8 / 12 R₈ zeros | Correct distinction: t≡0 (8) is R₈, not full 8/p. Independently exhausted full three-term representations at 131 and 241: none. Lemma T's power-of-two caveat is correct; the other even C are not all ramified. Gaussian screening was explicitly not done, so no “pass” is earned. |
| F3 285 composites | Correct as a constraint on the (★) count, O₄=−E₄. It does not force full α-family failure; no primality-free universal positivity claim survives the table. |
| F4 14 (★), 38 𝔊* zeros | Correct family distinction. Directly verified the 409 Type II rescue (1,117,2,1,59). Only the 14 (★) zeros require O₄=−E₄; the other 24 𝔊* zeros need not. No successful general mechanism is asserted. Screen zero lists themselves were not recertified here. |

## Required fixes, priority order

1. Correct #10's overbroad factorisation claim and #12's unsupported subset-product threshold; retain only proved restricted statements.
2. Narrow SIGN's reading and the opening “every arithmetic re-encoding collapses”/global dead language. Preserve #8, #11-plus and structured variants as unproved, not ruled out. “No mechanism found” remains justified.
3. Repair prior-art scope: STRONG_APPROX Thm 9.1 is not an all-identities theorem; supply the missing astra-4 artifact or cite Z2847; distinguish “already proposed” from “proved impossible.” Remove #19's polylog assertion.
4. Keep the one-engine 10¹⁰ limitation, T3 point-estimate qualification, and explicit O₄/E₄ notation. No new computation is required to retain the null verdict.

Reproduction: archive the lane's `scripts/z69_ideaa_*` and `data/z69/ideaa/` into `/tmp/xrev_IDEAA`; compile `scripts/z69_xrev_ideaa_census.cpp` with `g++ -O2 -std=c++17`, run with argument `100000000` into `/tmp/xrev_IDEAA/census.txt`, then `uv run python scripts/z69_xrev_ideaa_checks.py /tmp/xrev_IDEAA` (apply the limits above). Original T1 and kfit reruns were performed in the temporary archive, not the worktree.

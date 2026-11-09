# Z68 U7O hostile cross-model review

**Verdict: ACCEPT-WITH-FIXES.** The mathematical narrowing is defensible, conditional where stated; the mandatory-screen presentation and eventual/universal quantifiers need repair. **ES and the pointwise U₇ conjecture remain OPEN.**
Reviewed `side-agent/z68-u7o` at `031466e67`, including `Z68_U7O.md`, its engines/data, Z60 Lemma 7 and Z58 Prop C1. No lane files changed.

## Per-claim audit

| Claim | Classification | Finding |
|---|---|---|
| R1–R3; word/shift/T equivalences | CORRECT | CRT/divisibility and parity check out. For prime p>3, a common endpoint factor must be p, impossible since p ab y=a+b+1≤3ab. A word's x need not equal the least residue when y=1; this does not invalidate existence. |
| Theorem A / A′ | CORRECT | All sieve hypotheses hold for each **fixed** K; κ_K→∞ is legitimate. See source audit below. No uniform-in-growing-K conclusion follows. A′ follows by taking A>1 and the PNT in a fixed reduced class. |
| A: novelty / ES comparison | CORRECT, LOW NOVELTY | Standard fixed-dimensional sieve with K chosen after A, not a new ES exceptional-set improvement. Its log-power saving is weaker than Vaughan's exp(−c(log N)^{2/3}) saving. However U₇ is a narrower predicate: an ES exceptional-set bound alone does **not** logically imply A. Exact U₇ priority is not established here. |
| Theorem B | CORRECT | If max(deg X,deg Z)≥d, degree of XYZ forces the other two degrees to vanish. Otherwise the irreducible top form is the product of the three top forms, so at most one degree is positive. No positivity argument is needed. |
| Corollary B′ / prior art | CORRECT | Valid specializations make the two constant letters positive integers. Each ambient predicate is eventually periodic; the class 1 contains arbitrarily large odd squares and hence cannot be allowed. Take a common multiple exceeding the thresholds. This is the advertised word-form reuse of Z58 Prop C1 / NORMFORM_CUBIC, not a new obstruction to arbitrary algebraic rules. |
| Lemma N | CORRECT | The adaptive x=2t construction gives d=p+2t≡−1 mod 8t. For shifts 2,4,8, avoiding divisor class 7 excludes both prime class 7 and the simultaneous occurrence of classes 3 and 5. The mod-7/15 guards are necessary and present. |
| N counts 41,866 / 15,468 | VERIFIED | Independent prime-factor-class marking census and original engine both give these counts among 1,439,970 primes ≡1 mod 8 up to 10⁸. This proves neither infinitely many chain survivors nor a pointwise obstruction. |
| Lemma C; m(p), S(C) | CORRECT | Fixed endpoint searches reconstruct both orientations; fixed middle letter uses (cx−1)(cz−1)=cp+1. All positive divisors, not just prime divisors, must be tested. The engine does so. |
| Cascade record / survivor counts | VERIFIED WITH LIMITED RANGE | Full original-engine rerun through 10⁸ is byte-identical. Independent reconstruction verifies all 39 REC/DEEP primes in the four cascade outputs, the 60 deep primes ≤10⁸, and 128 seeded random primes ≤4·10⁹. The full 4·10⁹ census was **not** independently rerun; its stated maximum is supported by code audit, records and sampling, not a fresh exhaustive certificate. |
| Composite-residual engine repair | CORRECT IN DECLARED DOMAIN | Residuals are now primality-tested and recursively factored, including repeated factors. Twelve small-prime Miller–Rabin bases suffice for its uint64 inputs. Regression at p=1,000,829,135,329 gives m=4, not 6. No old reported census input reaches the affected residual range. |
| Prop K admissibility | CORRECT, CONDITIONAL | Every form is positive linear with constant term 1. For every prime ℓ, t≡0 mod ℓ avoids all zeros: admissibility really holds. Remove duplicate forms, notably q₁=Q₁, before invoking Dickson. |
| Prop K divisor exclusion | CORRECT, CONDITIONAL | q_k,Q_k>k+1 imply **every** divisor is e or eq with e∣k+1, including composite e and eq. Reduction mod 8k handles x=k,y=k; z=k needs the separate k=1,2,3 checks, all valid. Thus m(p)>C: all three letters exceed C, not merely failure of words with all letters small. |
| Lemma S / Cor K′ | CORRECT / CONDITIONAL | The size inequalities hold for positive n; for large p every Λ-divisor is ≤C₀+1 or ≥p/(C₀+1). A large letter forces another small letter. Bounded multiples have the same dichotomy. No general nonlinear-divisor exclusion follows without additional work. |
| Lemma P / negative Pell | CORRECT | Jacobi cancellation requires gcd(f,s)=1; the revised statement supplies it. Coprimality is automatic for f∣t,t±1, not t±c generally. p=41,t=32,s=5,f=15 is a genuine witness and defeats the unguarded claim. The size bound is g≤p+2, and the t²+2 argument excludes g=s² only, not all Pell rules. |
| Gaussian / norm-chain controls | HONESTLY LIMITED | Independently verified all seven R-G failures by exhausting their divisor-letter sets. This refutes the stated all-primes rule, not every eventual or modified Gaussian rule. R-G2's 60/60 and unmatched controls do not establish enrichment or a mechanism. |
| F1–F4 / labels / “narrowed” | CORRECT-WITH-FIX | F1 is structural; all actual finite-screen outcomes below agree. But F2 is misplaced and F3 omits the full supplied screen. The conditional narrowing is justified; unconditional “dead” language and unqualified finite-range passes need scoping. |

## Decisive sieve-source check

Richert, *Lectures on Sieve Methods*, §11, (11.9), Theorem 11.3/(11.10), states exactly the Brun O-bound under (Ω₁), (Ω₂(κ)), (R), for z≤X^A. Its chapter Notes explicitly identify this with Halberstam–Richert **Theorem 2.2**.
Source read directly: https://www.math.utoledo.edu/~codenth/Spring_13/3200/NT-books/Lectures_on_Sieve_Methods-Richert.pdf
Also checked the authors' precursor, *A new look at Brun's sieve*, Theorem 3, p.100: https://www.numdam.org/item/MSMF_1971__25__97_0.pdf
The 1974 book page itself was not accessible; the same-author restatement and explicit cross-reference were accessible. This is not a guessed theorem-number citation.
Here ω(ℓ)≤K+1<ℓ/2, so A₁=2; CRT gives |R_d|≤ω(d), exactly condition (R), **not** an unproved averaged level-of-distribution assertion. Fixed-modulus PNT gives the stated weighted prime sum with bounded K-dependent error and dimension 1+Σ1/φ(lcm(8,x)). Mertens then gives W(z)≍_K(log z)^{−κ_K}; κ_K≥1+H_K/8. Thus z=N^{1/2} is allowed by this O-bound; no missing remainder term invalidates A.
The same reasoning with odd x (or 8∣x) still has divergent dimension: A really is U⁽⁸⁾-blind.
Vaughan's rate is confirmed in Elsholtz–Tao, arXiv:1107.1010, introduction p.3 (`sources/lit2026/audit-elsholtz-tao-1107.1010.txt`); Vaughan's original article was not obtained. The comparison is of rates/methods, not an inclusion of exceptional sets in the wrong direction.

## Independent numerical evidence

Reproducer: `scripts/z68_xrev_u7o_check.py`; independent 100-MB census: `scripts/z68_xrev_u7o_norm.c`. All runs use `ulimit -v 6000000`, command timeouts ≤900 s, and at most two compute processes.
- At p=3,613,009: exhaustive searches for each letter 1,…,25 fail; (272,26,511) is a word. Hence m=26 independently, not just an upper bound.
- At p=128,677,046,401: m=17 with word (65,285,158,116,17). All 22 Dickson examples satisfy their simultaneous-primality conditions and their claimed depth inequalities.
- Residual regression: (500112,4,500303) represents 1,000,829,135,329; (4x−1)(4z−1)=2,000,447·2,001,211=4p+1. Both factors exceed the old 2·10⁶ trial-division table, explaining the original omission.
- All 18 least-f records checked directly against the defining least-residue test. The sievecheck 10⁸/1024 run is byte-identical, including the 728 survivors.
- F1: all 500 odd squares ≤10⁶ have no witness, by exhaustive f≤2n+1 search (in addition to the Jacobi proof).
- **F2 proper:** all 12 supplied R₈-zero primes have direct U₇ witnesses. R₈ is the C-even B-subline, **not** the two-branch U⁽⁸⁾ predicate.
- **F3 proper:** of all 285 supplied non-square composite (★)-zeros, 277 have U₇ witnesses; exactly {105,1465,3865,4545,10305,12145,39361,67425} do not. Zero checks exhaust f≤2n+1.
- **F4 proper:** all 14 (★)-zero primes and all 38 𝔊*-zero primes have direct U₇ witnesses. These finite checks do not follow from Theorem A.

## Required fixes, priority order

1. Restore the mandatory F2/F3 rows in **both** falsifier tables: put the 12 R₈ controls under F2, distinguish U⁽⁸⁾ as an additional screen, and state the 277/285 versus 8/285 U₇ split under F3. Moving R₈ to F4 and listing only Z₇ is not a faithful presentation of the required screens.
2. Respect the target's **“all sufficiently large primes”** quantifier. The 45 finite U⁽⁸⁾ failures and seven finite R-G failures refute all-primes claims, not eventual ones. “Must use extra targets” is justified for a proof covering those particular primes, not for an unspecified eventual theorem. Label K2/K4 as deliberately stronger finite-range selection tests, not impossibility theorems for eventual rules.
3. In §6A.6, replace R-Λ's unqualified “pass for large C₀” by “passes the tested finite range for sufficiently large C₀”; keep “dead” for R-casc/R-Λ explicitly **conditional on Dickson**. Likewise the assertion that depth-26 closure is a finite-range artefact is conditional, not an unconditional theorem.
4. Add the accessible Richert restatement/cross-reference to A's citation and retain the precise novelty disclaimer: standard sieve specialization, weaker ES saving, no established new pointwise mechanism. Keep 4·10⁹ results labelled EVIDENCE rather than independently certified by this review.

## Concrete directions still unexcluded

- Test R-G2 outside its selected 60 deep primes, using exhaustive coordinate representations and same-p controls matched for candidate-set size; the observed 60/60 is not a universal statement.
- Derive a word from a divisor of a genuinely nonlinear expression in Gaussian coordinates, e.g. a²+ab+b² or a²+2b², then prove the required residue/integrality condition. B excludes global polynomial *letters*, not this operation; K′ excludes only its specified linear-shift divisor menus.
- For Pell data test f∣t±c with c≥2, explicitly separating gcd(f,s)>1; or other functions of t,s instead of g=c s². The p=41,f=15 example demonstrates why the excluded branches cannot be promoted to a blanket Pell no-go.
- Let the cascade bound grow with p and seek a quantitative upper bound on m(p). Neither fixed-K Theorem A nor fixed-C Dickson counterfamilies decide any proposed unbounded C(p).

No provider/auth/quota error occurred. Source-access limitation: the 1974 book page and Vaughan original were not obtained; the accessible sources used are identified above.

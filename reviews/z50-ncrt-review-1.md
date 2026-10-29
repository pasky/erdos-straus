# z50 ncrt — Astra hostile review 1

Reviewed `EXSET_BEYOND_CRT.md` in full at `aa91e387e50a1086e29dbbf6509a65f624dae640` (409 lines), against the specified K2, EK, ETw, theta, inter-frequency, large-sieve and three-quarter-note dependencies. This is an internal mathematical review, not external refereeing.

**Overall verdict: MAJOR.** The quadratic-supply construction and its prime exceptional-set bound survive my checks, subject to small explicit repairs. The advertised *problem-wide* 2/3 CRT ceiling does not follow. The abstract cap also omits the uniformity needed to choose its small-prime cutoff. Neither issue should be hidden behind “PROVED given K2/EK.” I found no fatal obstruction to the narrower word-class theorem after the repairs below.

| Requested item | Verdict |
|---|---|
| (1) Identities, groupings, containment evidence | SOUND-WITH-REPAIRS |
| (2) Abstract supply-exponent cap | MAJOR |
| (3) Word square obstruction and moment estimates | SOUND-WITH-REPAIRS |
| (4) Corollary 2.5 and problem-wide reading | MAJOR |
| (5) U-atom exceptional-set theorem | SOUND-WITH-REPAIRS mathematically; novelty correction required |
| (6) Scope, labels and other claims | MAJOR |

## 1. Certificate identities and class containment

All five displayed rational identities and all five displayed ET equations are correct. For Type II the equation is `4abcd=a+b+cn`; for Type I it is `4abcd=n(a+b)+c`. The asserted R-class divisibilities in rows 1–2 and the Case-A containment in row 3 check. These are algebraic ET parameters; no assertion of primitive normalization is needed for these identities.

The distinction between *holding different parameters fixed* is legitimate. It is not a theorem that individual classes from the new grouping cannot already be K2 classes.

**D1 — False exclusivity language, §1.3, Proposition 1.2(b), lines 127–132.** “Every refinement” and especially “only through moduli … that grow with d” are too strong if read as assertions about the resulting sets. Explicit counterexamples:

* Endpoint `(t,v)=(2,3)`, `4|u`: `17 mod 20` is exactly Case A with `(d,m)=(5,7)`.
* Endpoint `(t,v)=(3,1)`, `4|u`: `7 mod 8` is exactly the fixed `(a,D)=(1,2)` class. Thus even the assertion specifically about membership in `(a,D)` classes only through growing moduli is false.
* Pair `(u,v)=(2,3)`, `t≡3 mod4`: the certificate class `13 mod24` is exactly `(a,D)=(3,2)`.

**Repair:** say that the *parameter-freezing rule* is different and that the displayed witness-to-K2 map has varying moduli. Delete “only.” Explicitly permit coincidences, containment and alternative certificates. Give a genuinely noncoincident example if literal failure of inclusion as a set of classes is desired. The present parameter argument alone does not establish that stronger assertion.

**D2 — Census scope/counting, lines 142–147.** The published run reproduces 392 tested parameter instances, 299 single-class containments and 93 residual instances, with no sampled uncovered member. But these are **318 distinct residue classes**, not 392 distinct classes. Moreover the script skips cases already certified by fixed slots (`A≡0 mod4`, `4|t`, `4|v`); it is not literally every endpoint subclass with modulus at most 400.

**Repair:** describe the filtered parameter census accurately. The “undecided / EVIDENCE” status is otherwise honest: coverage of integers below `10^5` cannot prove coverage of the entire progression. Also distinguish “covered by a finite union” from “equal to a finite union”; the implemented test addresses coverage, not equality or a polynomial modulus bound.

**D3 — Definitions, lines 104–113.** For general positive n, the proof of `U⇒ES₅` omits the even-endpoint branch. If `v≡−n mod8` is even, `tv−1` is odd, so `8|u`; this repairs the implication. Exclude the degenerate endpoint modulus `tv−1=0` explicitly. U's inequalities `tu−1,tv−1>1` are not, in general, congruence conditions: a U-refined progression may need finitely many initial members removed. For example `(t,u,v)=(1,2,4)` represents 2 and passes the endpoint congruence, but is not a U-word. Such a progression can still be used as a certificate-word class, or as an eventual U-class with its exceptional prefix paid separately.

**Repair:** define certificate-word classes first, keep selectors separate, and state the finite-prefix convention for eventual U-classes. The atom construction later already pays a safe prefix.

## 2. Theorem 2.1

The exponent calculation is correct. With

`s₁=λ^(1/(β+1))(log λ)^(−γ/(β+1))`,

the singleton cost is `O(s₁^β(log λ)^γ)` and the block costs sum to `O(λ/s₁)+O(log²λ)`. The identity `s₁^(β+1)(log λ)^γ=λ` produces the stated saving exponent. The assumption `β≥1` absorbs the additive logarithmic errors. One must take `λ₀` so that `s₁>2log W`; the linear top block and the zero-cost coordinates above `e^λ` remain as in K2.

I checked the relevant EK/ETw mechanisms: the coupling, random-cost comparison, locality count, chain-rule inflation, singleton step and linear step do **not** silently need cubic supply or an R-class identity. The arithmetic enters through the base and moments. Thus replacing the cubic first moment is a legitimate strategy.

Condition (i), for actual complete congruence classes, **is sufficient for R1**. If b is a square modulo G, choose a positive representative x of a square root; the positive perfect square `x²` lies in the class. Excluding positive squares therefore excludes unit-square residues, not merely squares in some tested interval. Selectors require the separate unit-square argument, since `0 mod p` contains `p²`.

**D4 — Missing cutoff-uniformity hypothesis, lines 189–208 (MAJOR).** The inference “(iii) ⇒ K2 Lemma 4.3 ⇒ leak ≤1/2” is incomplete as stated. For a fixed W the cofactor estimate gives

`E p_ℓ² ≤ C(W) ℓ^(−7/4)(log ℓ)^c`,

but choosing W sufficiently large requires control of **how C(W) changes when W is enlarged**. K2 Lemma 4.3 expressly proves `C(W)≪(log W)^C`; this is a substantive part of that lemma. It is not an arithmetic-free consequence of an unspecified cofactor constant at one cutoff. Here Γ itself changes with W, so one cannot simply retain the old `(iii)` constants after moving more primes into the square base. A crude comparison of the two Γ weights can cost a product of constant factors over the newly small primes, rather than a power of log W.

**Repair:** formulate the hypotheses for every sufficiently large W with, for example, `C_κ(W)≤A_κ(log W)^d`, with fixed exponents, and allow the first-moment constant to depend on the subsequently fixed W. Alternatively explicitly assume the existence of a fixed cutoff for which the resulting leak sum is at most 1/2. Then prove that hypothesis for the word universe. Its proof is available here: the long-block Euler factors and pair-part factors cost only powers of log W, Shiu's constant is W-independent, and the short-block estimate can use `Γ(q)≤8·3^ω(q)` uniformly in W. This supplies the needed repair without changing the exponent.

This is a proof/interface gap, not a counterexample to the abstract conclusion. The current statement does not specify the uniformity needed by its proof.

**D5 — Selector inconsistency, lines 112–113, 149–151 and Lemma 2.2.** `𝔘_W` was defined to include selectors, but is then said to satisfy (i), which forbids every positive square. It does not: selectors contain squares.

**Repair:** apply Theorem 2.1 to the certificate-word universe without selectors, and add selectors as the theorem already permits. Their first moment is `O(log log y)` and their cofactor contribution is 1, so this changes no conclusion.

## 3. Lemmas 2.2–2.4

The square exclusion for certificate-word classes is sound. For complete self-containment one can avoid the opaque Lean line reference: any positive Type-II tuple has `M=4bcd−1`, `D=b²d`, `D|(bcd)²`, and `n≡−4D mod M`; K2 Lemma 2.1 excludes squares. Type-I rows 3 and 5 give Case A using `nt+1=(tu−1)(tv−1)`, exactly as stated. This works for even as well as odd squares.

The first-moment counting idea is correct: endpoint multiplicity is `O(τ(A+1))`, pair multiplicity is `O(τ(A))`, and refinements change the modulus by at most a factor 8. The elementary divisor-in-AP estimate is valid: retain `(d,s)=1` while counting `m≡1 mod s`, then each divisor condition occupies at most one class modulo ds. The accumulated `O(√x)` term is absorbed when `s≤√x`. The Rankin/Cauchy–Schwarz tail has the right powers: a block costs `O(e^(−u/2)u^(3/2)(log y)^2)` and the block density costs one further log y. Taking `u₀=12log log y` suffices.

**D6 — Wrong large-divisor exponent, Lemma 2.3, line 245.** From `s>√x` one gets

`Σ h(s)/s ≤ x^(−1/8) Σ h(s)s^(−3/4)`,

not the displayed `x^(−1/4)` bound by that argument.

**Repair:** replace `x^(−1/4)` by `x^(−1/8)` and choose, say, `ε=1/16`. The large-divisor contribution is then `O_W(x^(15/16))`, enough for the claimed `O_W(x log x)` bound. Both Euler products still converge. This is not a loss in the final exponent.

For Lemma 2.4, the pair estimate `μ(q)≪(v+1)τ(q)` and the endpoint estimate `μ(q)≪Σ_{i=0}^3 τ(qℓ^v/2^i+1)` are valid overcounts. Cauchy–Schwarz gives Euler parameter 4 in the first long-block factor and Shiu parameter 16 for `τ⁴` in the second. The resulting logarithmic and v-polynomial losses fit (iii). The short-block pointwise divisor bounds also fit (iii), uniformly in W as explained under D4.

**D7 — Shiu range constant, Lemma 2.4, lines 257–261.** For the `i=3` term the m-interval length is `Y=Kℓ^v/8`, not `Kℓ^v`. At the declared lower boundary `K=4ℓ^(v/3)`, one has `Y=(1/2)ℓ^(4v/3)`, so `ℓ^v<Y^(3/4)` is false. Asymptotic comparability does not preserve this strict cutoff inequality.

**Repair:** start the long range at `K≥16ℓ^(v/3)` (or any suitably larger fixed constant), and include the intervening blocks in the short range. The latter still has `m≪ℓ^(4v/3)` and costs `ℓ^(κv)`. Check the upper endpoint and lower interval-length condition in Shiu explicitly; here the interval length is comparable with its location, so that part has ample slack. Treat q=1 separately in the dyadic decomposition if using blocks `(K,2K]` starting at K=1.

After D4–D7, the claimed word moment estimates are justified. I found no hidden cubic moment in them.

## 4. Corollary 2.5: the central overclaim

**D8 — A cap for one universe is promoted to a cap for a problem (MAJOR), lines 149–155, 175–179, 264–282.** The theorem, once repaired, caps majorants of the **whole periodic avoider set of a finite word-class family**. It does not cap all methods proving bounds for failure of U or ES₅. Such a method can legitimately use any progression separately proved to force the target, including a progression covered by different words in different residue subcases, or a non-word R-class if a separate target-forcing argument is available. Its mean/supply must then be estimated for that enlarged universe.

The table shows that the particular R-class witness need not be a word of n. It does **not** prove that the progression's members have no other certificate words, nor that no cubic-supply non-word family can force U/ES₅. Conversely I am not claiming that all R-classes force either target: that implication is unproved here. There is simply no universe-exhaustion theorem in the note. A useful caution from the existing failed I3 witness-map fixture is `n=6336`: despite that map failing, it has the certificate word `(2,12,276)`, independently enumerated in my check.

**Repair:** rename the result “2/3 ceiling for the specified word-class architecture.” Explicitly exclude other forced classes, coverings/coarsenings and majorants required to dominate only the actual exceptional set. Replace “every CRT method for U/ES₅” by the exact architecture hypotheses. Retain as an open question whether a larger useful forced-class universe has cubic supply. A theorem exhausting all usable classes would be a separate, substantial result, not a consequence of the first-moment bound.

The M1 projection/coarsening reduction is family-free **with its whole-avoider majorization and prime-size hypotheses retained**. The M2 reduction through IF Theorem 2.2 is also family-free. The large-sieve duality is family-free, but the level/fibre conditions must remain: polynomial-period rows and a suitably bounded conditioning modulus, or the precise later generalized-row theorem. These valid black-box transfers do not enlarge the target family.

**D9 — “Every method in the barred union” and “extends verbatim,” lines 278–282.** Only M1, M2, L1 and C are actually transferred in the displayed corollary. P is expressly left unchecked immediately above; M4 has special prime-slice hypotheses, and the other listed architectures have their own conditions. A scalar mean cap alone is not a proof of every transfer.

**Repair:** list only the transferred cases, and give separate proofs/references with retained hypotheses before adding others. For K2-plus-word mixtures, establish the applicable combined moment bounds and state which black-box consequences follow; do not simultaneously call the unit-group rerun unchecked and the entire union transferred.

**D10 — Constant-sharpness overstated, lines 302–303.** Bounded-B for the author's atoms does not impose bounded-B on a competing word-class method. For the unrestricted word universe, Corollary 2.5 still allows a `(log log N)^(2/3)` gain.

**Repair:** claim exponent sharpness for the stated unrestricted architecture, and order sharpness up to constants only within fixed bounded-B families and the specified evaluations.

## 5. Theorem 3.1 and its construction

I found no load-bearing failure in the prime U bound. In particular:

* `4w|kℓ+1` forces `(w,k)=1`, `ℓ≡3 mod4`, and the event is precisely `n≡−4w mod kℓ`. Beyond the stated prefix, the reconstructed word has endpoint `4w`, `u≥2`, and both adjacent factors exceed 1. The actual atom cutoff forces its word level `(kℓ+1)/(4w)` to tend to infinity, so the second nondegeneracy inequality is safe.
* Same-ℓ distinctness uses `4w<ℓ` and `4w>K` correctly. Conditional independence is a CRT identity, not an assumption about the empirical distribution in `[1,N]`.
* Lemma 3.3(b)'s error terms are absorbable: `log H/H + (log z)/√H ≪ Λ/K²` when `H=K^10`, `z≥H²`. Its main term correctly involves `1/d`, not `1/φ(d)`. The proof should state the elementary harmonic-progression estimate for arbitrary modulus and lower endpoint, since its application to `d≤K²` and `(H/e,z/e]` is more general than the literal wording of part (a).
* BT and BV have large slack: the actual moduli are at most `4x^(1/6)`. The main block mass is `≍x g(J)`. Expanding `r(w)²` gives `ΛΣ1/[k,k']≪t^4`; multiplying by `x/log x` gives `xt³`. BV with R=10 therefore gives the stated `O(xt^(−7/2))` error, uniformly in c and J. No Shiu input is hidden here.
* The void argument works. Choose explicitly, for example, `a₀=1/8` for large K from `g(K(K))=(1/4)log K+O(1)`. The exponential moment is at most `e^4`; `a_v=aa₀κ/3` is valid eventually since `log K∼κt`. The proposed `B₀=8a_v/a₀+1` suffices.
* The even Bonferroni depth is `O(t²)`, with atom inventory `exp(O(t))` and selector ledger `exp(O(t²))`. Thus the total absolute coefficient ledger is `exp(O(t³))`. Balancing `t=α(log N)^(1/3)` gives the claimed 2/3 bound, with `KX=exp(O(t))` negligible. This is independent of the disputed cap theorem.

**D11 — Short-interval/passing-to-all-primes omissions, lines 297–300 and 384–389.** The interval proof only writes the majorant count, whereas U-failures below the atom-validity threshold need an additional `O(KX)` (and small primes an `O(y)`) contribution. These are harmless uniformly in the shift for intervals in the positive integers, but must be included. The implication from the `p≡1 mod4` U result to ES₅ at all primes also needs the other residue class addressed.

**Repair:** add the prefix terms to the interval bound before absorbing them, state the positive-integer interval convention, and note that for `p≡3 mod4`, `(t,u,v)=(p+2,1,1)` is a certificate because `tu−1=tv−1=p+1` is divisible by 4. Handle p=2 separately. Define `a₀` rather than importing it without a definition.

**D12 — Novelty audit missed prior quantitative work, lines 305–308.** The assertion that the strongest earlier U-or-ES₅ statement was qualitative is false. `I3_DEEP_ASTRA.md:146` explicitly proves a `N exp(−c√log N)` exceptional bound for the interior star subfamily with `t=4C`. Every such hit is an ES₅ certificate by the present definition, so its failure bound is also a quantitative ES₅ bound. More importantly, `I3_DEEP_ASTRA.md`, Lemma 8.7 and §8.8 (around lines 537–641), already contain the one-divisor multiplier atoms, same-prime distinctness, `t Σ1/k` fibre supply, incidence mean square, exponential Z-moment and `t³` Bonferroni ledger used here. Their unrestricted I3 result is not itself an ES₅ theorem, but this is a very close prior construction.

**Repair:** cite both predecessors. Describe the new theorem as the certificate/U congruence-restricted adaptation of the previous one-divisor I3 construction, improving the earlier quantitative ES₅ star bound to exponent 2/3. I did not locate an earlier explicitly stated prime U bound of this strength in the searched repository. “The symbols are internal, so no literature comparison applies” should become “no external priority claim; equivalent arithmetic formulations have not been literature-audited.”

## 6. Other claims and labels

**D13 — Incorrect door examples, §1.4.** At lines 160–161, words with `u=1` or `t=1` are not intrinsically single points as class families. For example fixing `u=1,v=4` gives the infinite progression `n=4t−5`, not one point. At lines 168–170, `q≤tN+1` is still polynomial in N when t is fixed or polynomially bounded. This does not exemplify primes beyond `N^{O(1)}`. The K2 cap permits arbitrary family moduli and arbitrary total family level; high total level alone does not evade it.

**Repair:** retain the true statement about a *fixed class of modulus>N*, delete the unsupported word-boundary example, and distinguish a genuinely super-polynomial auxiliary-prime range from a different, genuinely multiplicative/non-CRT evaluation of a polynomial-prime family.

**D14 — Labels and numerical certification.** The generic theorem and global reading must not retain their current unqualified PROVED interpretation before D4/D8/D9 are repaired. “The single binding constraint” in §1.1 is a description of the exhibited construction, not a universal necessity for all possible evaluations. The title claims “breaking” a barrier, while §3 currently attains a restricted architecture's barrier rather than breaking it. The containment, prime-Haar toy comparison and square checks remain finite evidence only, as mostly acknowledged.

The identity script is a random/exhaustive exact-arithmetic checker, not a symbolic identity checker. Its 25,230 “U-atom checks” verify the word equation and rational identity, **not the full U predicate**: its broad loop includes `(k,ℓ,w,u)=(1,3,1,2)`, yielding `(t,u,v)=(1,2,4)` with `tu−1=1`. This does not refute the actual asymptotic atom theorem, whose cutoffs exclude t=1.

**Repair:** describe those 25,230 checks as algebraic atom-identity checks, or additionally filter to the theorem's admissible atoms and assert every U condition. Separate symbolic proof from numerical evidence. Retitle/reframe the result as an audit, word-architecture cap and matching theorem. Finish or clearly leave pending the summary/review/§4 deliverables rather than implying a completed beyond-CRT attack.

## Reproduction and independent check

All runs used `ulimit -v 8000000`, explicit timeouts, and `uv run --with sympy --with numpy python`. I inspected the scripts before running them; the toy fibre modulus for K=21 is only 69615, and the actual prime array had length 1000001. No unbounded Cartesian-product allocation was used.

* `scripts/z50_ncrt_identities.py`: reproduced slot counts `[50036,49985,25036,49527,24804]`, zero identity failures; 25,230 algebraic atom checks, zero failures.
* `scripts/z50_ncrt_k2contain.py 400 400 100000`: reproduced 392/299/93 and zero uncovered tested members in the reported residual rows.
* `scripts/z50_ncrt_uatoms.py 1000000 3000 21 30`: 5,045 toy atoms; 36,028 eligible primes; actual avoider fraction `0.11588`, prime-Haar prediction `0.11245`; zero hits among 375 eligible odd squares. These deliberately relaxed toy parameters do not test the asymptotic supply theorem.
* Independent `/tmp/z50_ncrt_review_independent.py`, importing no campaign code: exhaustively checked all positive words with `1≤t,u,v≤24`, obtaining slot counts `[3456,3450,1699,3450,1699]`, exact rational identities/ET equations and no square certificate; checked the explicit K2 coincidences in D1; enumerated the certificate `(2,12,276)` at 6336; verified the exact toy CRT void `765/1463` for primes 7,11,19 against enumeration of a complete period, and square avoidance through root 499; counted 318 distinct classes among the 392 containment instances.

Logs are `/tmp/z50-review-{identities,contain,uatoms,independent}.log`. Only this review is added to the repository.

## Final decision

**MAJOR revision required, not rejection of the quadratic-supply construction.** Preserve the prime U/ES₅ exceptional-set theorem after its small proof/presentation repairs. Fix the cutoff-uniformity hypothesis and the two elementary moment-proof slips. Narrow the 2/3 ceiling to the explicitly defined word-class architecture and its actually transferred evaluations. Correct the false exclusivity wording and the prior-work claim. No result here establishes that beating 2/3 for U/ES₅ necessarily requires a non-CRT input.

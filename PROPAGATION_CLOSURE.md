# PROPAGATION_CLOSURE (board #4 addendum, 2026-10-19)

**Assessment / verdict: PARTIAL, promise 1/5 (documentation), no active ES route.** Board #4 supplies neither (P) exception propagation contradicting Vaughan nor (G) a non-counting positivity mechanism. This closes its *supplied constructions*, not these proof shapes in general. The retained identities remain inside familiar certificate families. ES is open. Sources: `BREADTH_Z45.md` §§6–7, `AMPLIFY_EXCEPTION.md` Thms 2.3–2.4, `DELTA_TRANSPORT.md`, `Q3_PIVOT.md`; boards `~/.pi/boards/20261019-es-{propagation,sidestep}/memo.md`, especially propagation rounds 02-fable and 03-astra/fable. Earlier norm-coordinate attempts are indexed under z35 and s7 in `BRAINSTORM/README.md`.

## 1. Audited descent lemmas (board #4 addendum, 2026-10-19)

**PROVED, patched Mordell profile, independently audited here.** An exceptional prime p lies in the six unit-square classes modulo 840; hence p≡1 (8), (p/3)=(p/5)=(p/7)=1. Reciprocity gives complete splitting in ℚ(i,√2,√3,√5,√7). It is represented by the principal forms of discriminants **−4,−8,8,−3,12,−7,−20**, respectively

    x²+y², x²+2y², x²−2y², x²+xy+y²,
    x²−3y², x²+xy+2y², x²+5y².

*Audit proof, relative to the classical Minkowski ideal-class bound:* every quadratic ideal class has an integral ideal of norm ≤(2/π)√|Δ| in the imaginary case, ≤√Δ/2 in the real case. For Δ=−4,−8,8,−3,12,−7 these bounds are <2, so the ordinary class groups are trivial. A split prime ideal therefore has a generator of norm ±p. Imaginary norms are positive; in Δ=8 the unit 1+√2 changes the sign; in Δ=12 norm −p is impossible modulo 3 since p≡1 (3). For Δ=−20 the bound is <3, so every nonprincipal class is represented by the ramified ideal above 2, whose square is (2). If a split p were nonprincipal, multiplying its ideal by that ideal would give x²+5y²=2p. This is impossible: x,y must both be odd, giving 6 modulo 8 rather than 2. Thus its ideal is principal too. ∎ The original lqnr≥17/11/13 extension is **withdrawn**; real-form coordinates need not be ≤√p and are not used in the census below.

**PROVED (Astra's diagonal lemma).** If p=a²+b² is an odd prime, a>b≥1, and ℓ is an odd prime dividing a+b or a−b, then **(p/ℓ)=(2/ℓ)**. Indeed gcd(a,b)=1, so ℓ∤b and p≡2b² (ℓ). Axis primes ℓ|ab instead give (p/ℓ)=1. The hypotheses exclude ℓ=2 and nonprimitive composite representations. Diagonal nonresiduosity supplies visibility, not a divisor-class hit.

**PROVED, precisely scoped square screen.** A step valid at an admissible odd square, with soluble source coordinates, cannot output an **ET-normalized** Type I/II certificate there (ET Prop. 1.6; `AMPLIFY_EXCEPTION` Thm 2.3). This includes polynomial ET steps **only when validity, positivity, integrality and normalization persist at that square**. Polynomial dependence or writing `(abd,nacd,nbcd)` alone is not a substitute for checking those hypotheses. **Normalization loophole:** mixed/scaled outputs remain legal. For example 169=12²+5² has soluble block {5,7,12,17}, and scaling a solution at 13 gives (52,234,6084) at 169. Consequently no blanket impossibility of polynomial norm-coordinate recombination is proved.

## 2. Rechecked finite evidence (board #4 addendum, 2026-10-19)

**CERTIFIED.** Set Q(p)={a,b,a+b,a−b}∩[2,∞), a>b, p=a²+b²; 1 is *excluded*, not called soluble. Among **273 Mordell-hard primes p<10⁵**, all source blocks are known soluble: **265** by q∉𝓜 or a prime factor ≢1 (4), and the other **8** by additionally scaling solutions at 13 or 17. Their p are 14281,15121,27241,42841,42961,49081,54721,95881; the only remaining coordinates are **169,289**, not 121. The six board fixtures 97,193,313,3361,5209,233689 also pass (a separate fixture list, not all members of this census). Thus on every tested input the proposed implication Q(p)⊆S ⇒ p∈S is simply ES(p), by Thm 2.4. This is not a prohibition on proving that implication.

**CERTIFIED numerator-uniform refutations.** Complete searches find no triple for **12/1657**, with 1657=36²+19², although its sources 17,19,36,55 have triples (2,5,170), (2,8,152), (4,13,156), (5,56,3080). Likewise **10/181**, 181=10²+9², fails while sources 9,10,19 have (1,10,90), (2,3,6), (2,39,1482). These refute a threshold-free numerator-uniform block law, not a 4-specific one.

**EVIDENCE, null pairing.** Fable reported 0.108 versus 0.105 after pairing the same representation coordinate b with another prime, removing an apparent size-control excess (0.108 versus 0.052). Independently, for 246 Mordell-hard p∈[10⁴,10⁵), the least b in p=a²+Db², D=1,2,3, gives **80/738=0.108401** hits of `∃d|b²: 4b−1 | pb+d`. Testing each same b at *all* 245 other primes gives **19263/180810=0.106537**. These exact counts reproduce the null interpretation with a deterministic control, not the unavailable original random pairing. They do not exclude other recombination mechanisms.

**CERTIFIED / PROVED bookkeeping.** `DELTA_TRANSPORT.md` §7 independently verifies 542 folds: old coverage 99/143, enlarged 131/143, odd-K external-2 coverage 93/143; without the no-zero filter, the union word family covers 137/143. Every target is the existing a=1 ET-II certificate `(1,tv−1,t,u/4,v)`. `Q3_PIVOT.md` §7 certifies the four-vertex island at 1321,6121,12241,14281; its §3 already refutes the *whole-seed-union* Q3 conjecture at 7909441 and 8604961. Neither dictionary is propagation.

## 3. Mixed-square Lemma D (board #4 addendum, 2026-10-19)

**PROVED.** Let p be an odd prime and let a positive solution of 4/p² have p-adic valuations (0,1,≥2), up to permutation. If K is its unique p-coprime denominator and m=4K−p², then m>0, m≡3 (4), p∤m, and **(p/m)=−1** (Jacobi; m may be composite).

*Proof.* gcd(K,m)=1. For every odd prime r|K, p²≡−m (r), so quadratic reciprocity for m≡3 (4) gives (r/m)=(−m/r)=1. If 2|K, then m≡7 (8) and (2/m)=1 too. Thus every divisor of K² has Jacobi symbol +1 modulo m, including K. Write the other denominators y,z with vₚ(z)=1. Factoring the residual equation gives

    (my−p²K)(mz−p²K)=p⁴K².

The second factor has p-valuation exactly one, so it is p·f with f|K². Reducing modulo m yields f≡−pK (m). Taking Jacobi symbols gives 1=(−1/m)(p/m)(K/m)=−(p/m). ∎ **CERTIFIED:** complete unordered-triple enumeration at 5≤p<100 reproduces **1096 mixed solutions**, zero violations (529 for p<60). This necessary sign condition neither supplies a divisor hit nor descends a mixed solution to p.

## 4. Open residue and screening (board #4 addendum, 2026-10-19)

**OPEN, unconstructed:** astra-1 is positive recombination from Gaussian-coordinate source fibres; astra-2 is integral series/parallel/Y–Δ reduction from four resistance-n parallel edges to a three-path theta network. The latter's 1,305,624-choice negative one-expansion catalogue at 1321 is **board-reported EVIDENCE**, not an infinite-component obstruction or a rerun here. Both are retired from the active slate, not refuted.

**OPEN crux (rule Λ).** Is there a rule uniform over an infinite family of **distinct prime pairs** (q,p), mapping every witness in W(q) into W(p), whose validity is not equivalent to a witness-determined residue condition or tied-divisor event? No construction or general impossibility theorem is supplied. **Assessment / Astra's dissent:** AMPLIFY and NONCONG exclude specified mediation classes; B1 has bounded-procedure hypotheses and conditional conclusions. Rewriting an eventual output as a divisor certificate does **not** prove that every proof must search/count divisors, or that B2 is necessary.

**Assessment, all FRONTIER §4 screens (of the proposed routes, not the negative proofs):** 1 PASS scoped (ET normalization; mixed squares allowed); 2 PASS controls (8/131,8/241 retained); 3 FAIL uniform law (10,12 refutations); 4 FAIL (no class-forcing input); 5 PASS (fixed-input audits, no average-to-point leap); 6 N.A. (no count/error proof); 7 PASS (no two-sided law); 8 FAIL supplied finite recipes (no growing mechanism); 9 FAIL (diagonal lemma only parity); 10 PASS (no pooled large primes); 11 N.A. (no signed reflection); 12 FAIL (no general transport/recombination theorem); 13 PASS (no BM sufficiency); 14 FAIL universal move claims (fold misses and Q3 traps); 15 PASS diagnostic (Mordell census and explicit square); 16 N.A. (no thin-family transfer); 17 FAIL as forcing (large-factor classes uncontrolled).

**Assessment, new-theory sketch / next test.** A positive recombination calculus would act on complete source fibres, allowing mixed/scaled square outputs. Its first required theorem is an actual nontrivial norm-compatible step, not another equivalent existence assertion. Toy: construct such a step for 169=12²+5² without importing its known target; the displayed scaled solution only checks admissibility, not the missing construction. No such calculus is supplied here.

**CERTIFIED replay.** `ulimit -v 1000000; timeout 300 uv run python scripts/z48_closure_verify.py`. Independent of all seat scripts; bounded factor cache, streamed divisors, no denominator cutoff in trap fibres. Data: `data/z48_closure/{summary,coordinates,folds,mixed,pairing,traps}.json`. No new ES claim follows.

# z59 hostile cross-model review — MSPF

Reviewed `side-agent/z59-mspf` at `a1b7de0881dfddd2d5ddf4dc15c1d8ca97139e99` (`Z59_MSPF.md`).
**Verdict: ACCEPT-WITH-FIXES.** The witness lemmas and decisive computations hold. This is a mostly prior structural audit, not a new positivity mechanism. The F3 inference is invalid, the mandatory F4 screen is incomplete, and the no-go wording needs scope restrictions. ES remains OPEN.

## Per-claim audit

| Claim | Classification | Independent derivation / limitation |
|---|---|---|
| Lemma 1.1, four bijections | CORRECT | Set d=4kC−1; dB=n+k and 1≤k≤(d+1)/4<d recover k uniquely as −n mod d. Conversely B=(n+k)/d and C=(d+1)/(4k) are positive integers. Also (4kC−1)(4BC−1)=4Cn+1; a divisor x≡−1 (4C) forces its complementary divisor into the same class. Exclude zero residues. Finiteness follows from 1.2 and C≤(n+2)/4. |
| Lemma 1.2, size bounds | CORRECT | k+B≤2kB gives n≥2kB. Hence min(k,B)≤√(n/2). Since 4k−1≤d=(n+k)/B≤n+k, 3k≤n+1; swap to bound B. |
| Lemma 1.3, (−k/d)=−1 | CORRECT | Write k=2ᵃv, v odd. gcd(k,d)=1; d≡−1 (v). Reciprocity gives (v/d)=(d/v)(−1)^((v−1)/2)=1. If a>0 then d≡7 (8), so (2/d)=1. Finally (−1/d)=−1. No primality assumption on d. |
| Corollary 1.4, squares | CORRECT | A hit at n=m² would have gcd(m,d)=1 and (−k/d)=(m²/d)=1, contradicting 1.3. Works for even as well as odd m. |
| Lemma 1.5, χ_n(d)=−1 and d≥q₁(n) | CORRECT | n≡−k (d) forces gcd(n,d)=1 and (n/d)=−1. For odd n≡1 (4), reciprocity transfers this to (d/n). Multiplicativity forces a prime factor q of d with χ_n(q)=−1, hence d≥q≥q₁. CRT makes χ_n nonprincipal exactly when an exponent in n is odd; factoring any unit with character −1 proves q₁ exists. In 𝔐 the signs at 2,3,5,7 are all +1, giving q₁≥11. Necessary, never sufficient. |
| Character/conductor remark | CORRECT-WITH-FIX | Define the squarefree part explicitly as f=∏_{v_p(n) odd}p, not rad(n); f≡1 (4) is the primitive conductor. The character mod n can additionally vanish at primes dividing n/f. S(n)⊂{χ_n=−1} makes its claimed coset-intersection formulation exactly S(n)≠∅, not progress toward existence. |
| Lemma 1.6, opposite cofactor signs | CORRECT | dB≡k (n) gives −χ_n(B)=χ_n(k). The unit hypothesis ensures these are nonzero signs; at prime n, 1.2 guarantees it. |
| Lemma 1.7, R(n) even | CORRECT | Swap k and B. A fixed point has n=4k²C−2k even, impossible for odd n. Therefore every orbit has size two. It supplies no nonemptiness or odd-count argument. |
| Lemma 1.8, no bounded hit menu | CORRECT | If d≤D then d divides L=lcm(1,…,D); a unit square mod L has Jacobi +1 mod d and cannot hit. The displayed CRT chooses m coprime to L in each prescribed 840-root class. The progression m²+840Lt contains at least X/(840L)−1−840L terms ≤X, versus at most √X squares. For D=(1/2−ε)log X use log L=(1+o(1))D≤(1/2−ε/2)log X for large X. Thus infinitely many nonsquares in each class have no hit ≤D; existence of larger hits is not proved. |
| §1.8 consequence, §2, §9 F1 | CORRECT-WITH-FIX | This excludes bounded witness moduli, fixed-modulus witness selectors and finite class-wide positive identities. It does not classify every possible proof using congruences plus a global nonsquare hypothesis. Replace “only through non-principality” by “one available equivalent encoding is non-principality,” as §0 already allows other arithmetic information. |
| §2 least-nonresidue estimates | CORRECT-WITH-FIX | Supply the composite-modulus citation and reduction below. Replace “nothing is known … below” by “no smaller uniform power exponent is supplied/claimed”; it is not a statement about special n or almost-all results. |
| §§3.1–3.2, identity/near-square attempts | CORRECT, scoped | Both displayed families have the stated witness; n is comparable to a² or (st)², and divisor summation bounds their total parameter count by O(√X log X). This proves thinness of those families only, not of arbitrary near-square constructions. The two explicit d=11,55 class lists are correct. |
| §§3.3–3.6, remaining algebraic attempts | CORRECT as Assessment | For d=qt, q must be coprime to 4k and t≡−q⁻¹ (4k); this is a restatement, not a forcing theorem. Prime-only failures are finite-range evidence. The swap argument excludes that parity mechanism only. The small-C character tests and matrix reformulation check out; “no action found” is not a theorem about all actions. |
| §3.7, analytic model | HONESTLY HEURISTIC | The exact representation sum is valid. The support indicator (χ²−χ)/2 handles nonunits correctly. The complete double sum is pχ_p(−1)=p: a=0 contributes p, each a≠0 row contributes zero. Weighted cancellation and unspecified local densities are not established; the 1/16 discussion is a model calculation, not a conditional positivity theorem. |
| §0 F3, infinite zeros and necessary 𝔐 dependence | GAP / WRONG INFERENCE | “Outside 𝔐 … continue indefinitely” has no proof here. Finite outside-𝔐 zeros do not refute an eventual theorem with a higher threshold, so “a proof that does not use membership in 𝔐 is wrong” does not follow. `Z58_LADDER.md` §0 F3 and §2 explicitly preserve broader eventual statements. Quoting a lane brief does not certify infinitude. |
| Final “not a hot lead” verdict | CORRECT | No witness-producing mechanism or pointwise positivity theorem is supplied. The eventual target remains inconclusive, not dead; individual tested routes are narrowed only within their specified scope. |

## Mandatory falsifiers

| Screen | Checked outcome and correction |
|---|---|
| F1 odd squares | Structural proof is valid, and all 224 squares among the 348 small zeros agree numerically. Avoid elevating the character description into a necessary architecture for every proof. |
| F2 numerator-8 / C-even | Recomputed all twelve listed primes: all supplied (R,R₈) pairs agree and R₈=0 throughout. Exactly four lie in 𝔐: 10301993881, 10529331121, 10532106649, 10868474401. These refute only statements whose threshold includes them; the memo correctly retains this qualification. |
| F3 285 composite zeros | Independent all-n enumeration reproduces the exact 285-entry list; 15 lie in 𝔐, 270 outside. The three additional in-𝔐 zeros 8725201, 12538801, 17401609 also give R=0 on rerun. gcd(d,n)=1 explains dead moduli, not the absence of every witness. Add these screen counts and remove the unsupported infinitude/necessary-domain inference. The 10¹¹ census remains attributed prior evidence, not a computation repeated here. |
| F4 14 (★)-zeros and 38 𝔊*-zeros | The memo substitutes nine in-𝔐 (★)-zeros and never addresses 𝔊*. Rerunning all 38 screen primes gives exactly the 14 (★)-zeros, nine in 𝔐; the other 24 have R>0. Of the 20 𝔊*-zeros in 𝔐, eleven have R>0. Example: 564661441 has R=2, both C odd, d_min=2741075, k=9. These are subfamily failures, not full-family zeros. Add the distinction explicitly; the lemmas hold at all these inputs but force no existence. |

## Numerical reproduction

All execution used `ulimit -v 4000000` and explicit timeouts ≤600 seconds (below the requested 1800-second cap).
The submitted C engines were inspected before use: their sqrt(n/2) search is exhaustive by symmetry, the prime sieve covers both oriented moduli, and the fixed divisor buffers are ample at these ranges. They are not arbitrary-size certified tools.

* Original `hits 10000000 1`: 20513 rows, byte-for-byte equal to `primes_M_1e7.txt`; nine zeros.
* **Independent engine** `scripts/z59_xrev_mspf_independent.c`: enumerates k≤B and all C with 4kBC−k−B≤10⁷, not divisors of n+k. Visits 38114976 unordered triples; both orientations reproduce every field of all 20513 prime rows byte-for-byte, including q₁, R_prime and k_min. Approximate allocation: 105 MB; no Cartesian-product arrays.
* Independent small-zero totals: 348=224 squares+124 nonsquares. Original `hits 200000 2` also reproduces `zeros_all_2e5.txt` byte-for-byte.
* Among 20504 positive prime rows: C-even absent at 186 (last 9965881), C-odd absent at 118 (9744001), prime d absent at 136 (9831889). The per-million counts in the memo all agree.
* d_min=q₁ at 4636/20504 (22.610%); d_min≤10q₁ at 17498/20504 (85.339%); k_min≤10 at 20119/20504 (98.122%). Maxima: q₁=53, d_min=64255, k_min=410 at p=4160641. Mean R over (5·10⁶,10⁷] is 30.1481.
* Rerun lemma checks: 7069 Jacobi pairs, 1998 cofactor-sign pairs, both polynomial families: zero failures. Brute-force pair versus modulus counts for n≡1 (4), n<3000: zero mismatches. `zeros_profile.txt` reproduces byte-for-byte, including the bounded-multiplicity qualification.
* `scripts/z59_xrev_mspf_report.py` checks the independent rows, all 285 composites, all twelve (R,R₈) pairs and the 14/38-prime distinction. Large single-n checks rerun the submitted trial-factor engine, rather than claiming a second independent large-n algorithm.

Reproduction, after archiving the reviewed memo/scripts/data to `/tmp/xrev_MSPF`:
```sh
ulimit -v 4000000
timeout 30 gcc -O2 -Wall -Wextra -o /tmp/xrev_MSPF/independent scripts/z59_xrev_mspf_independent.c
timeout 300 /tmp/xrev_MSPF/independent /tmp/xrev_MSPF
timeout 30 gcc -O2 -o /tmp/xrev_MSPF/single /tmp/xrev_MSPF/scripts/z59_mspf_single.c -lm
timeout 600 bash -c '/tmp/xrev_MSPF/single $(awk "!/^#/ {print \$1}" /tmp/xrev_MSPF/data/z58/screens/r8_zeros_1e10.txt) > /tmp/xrev_MSPF/recomputed_r8.txt'
timeout 300 bash -c '/tmp/xrev_MSPF/single $(awk "!/^#/ {print \$1}" /tmp/xrev_MSPF/data/z58/screens/gstar_zeros.txt) > /tmp/xrev_MSPF/recomputed_gstar.txt'
timeout 120 uv run python scripts/z59_xrev_mspf_report.py /tmp/xrev_MSPF
```

## Provenance and source check

* **Prior:** `Z56_FAMTRY.md` Lemmas 1.1–1.4 already give the divisor/pair/C forms, square obstruction and prime-character sign; `Z57_SYNTH.md` Lemma A.1 gives the all-n bijection, bound and Jacobi obstruction verbatim in substance. Lemmas 1.1–1.4 are rederivations, not new structural results.
* **Prior:** `Z58_WITNESS.md` Lemma 1.1 gives a nonresidue prime factor and d_min≥n_p at prime inputs; MSPF extends the d-form statement to nonsquare composite n≡1 (4). The unit-cofactor sign is also a specialization of `LOWER_TAIL_ASTRA.md` Lemma 2.2; it is not a newly discovered sign mechanism.
* **Prior:** `FRONTIER.md` §2.1 states R(p) even; `BRAINSTORM/z45_interlacing_stable.md` §1 proves the no-diagonal/all-odd-n version. `Z56_FAMTRY.md` Prop. 2.2 and `Z58_WITNESS.md` §0 F1 already exclude finite coverings/fixed-modulus selectors. Lemma 1.8's explicit all-six-classes CRT/logarithmic-size presentation is an incremental strengthening of that obstruction, not a new no-go principle.
* **Prior:** C-even=R₈ and the twelve large zeros are `Z57_SYNTH.md` §2.1; prime-only failures and the divisor-in-moving-class wall are already `Z56_FAMTRY.md` §§4.2–4.6. MSPF's contribution is a consolidated attempt record, elementary extensions and refreshed 𝔐-restricted census, not a novel pointwise approach.
* **Source opened:** Lau–Wu, *On the least quadratic non-residue*, [Theorem 1, pp. 1–2](https://www.math.hku.hk/imrwww/IMRPreprintSeries/2007/IMR2007-4.pdf): the least integer with χ≠0,1 is ≪_ε q^{1/(4√e)+ε} for cubefree q. View χ_n as a nonprincipal character modulo rad(n), preserving its zero set; this modulus is squarefree and ≤n. Its least −1 integer is prime by multiplicativity. This supplies the claimed q₁ bound, without wrongly replacing q₁ by the least nonresidue of the primitive conductor. The introduction also records the GRH log²q bound. These bounds do not supply the missing class hit.

## Required fixes, in priority order

1. **P1 — F3:** remove “continue indefinitely” or supply an infinitude theorem; remove the inference that every eventual proof must use 𝔐. Attribute the finite 10¹¹ claim to `Z58_LADDER.md`, not merely the brief.
2. **P1 — screens:** explicitly handle all 285 composites and the 14/38 prime screens, separating full-family and subfamily zeros and in-domain counts. Nine prime zeros alone do not meet this review brief.
3. **P2 — scope:** state the bounded-menu/congruence-selector theorem precisely; remove the universal “only through” character-language requirement. Distinguish a non-square residue from Jacobi value −1 (e.g. 11 mod 121 is not a square but has Jacobi symbol zero). Keep route failures local to the constructions actually tried.
4. **P2 — provenance:** add the prior-result mapping above before recording these as z59 theorems; do not sell necessary conditions or fresh census subsets as a new positivity mechanism.
5. **P3 — citations/notation:** define the conductor's squarefree part unambiguously, cite the composite-modulus least-nonresidue theorem with the rad(n) reduction, and qualify the “nothing known below” phrase as a uniform-exponent comparison.

After these repairs: **accept as a correct, useful but mainly prior audit; target unresolved and not a HOT LEAD.**

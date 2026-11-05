# z58 cross-model hostile review — FFIELD

Reviewed `side-agent/z58-ffield` at `54cc8f900175a4096dc42b151c84d667b48b4c93`, including `Z58_FFIELD.md`, its scripts/data, and the decisive z51 dependency.
**Verdict: ACCEPT-WITH-FIXES.** No counterexample or gap found in the core PROVED results. **“Narrowed” follows in the explicitly restricted sense of excluding fixed-degree, large-q universal positivity.** This is not an integer reduction or a general obstruction to function-field methods. ES remains OPEN.
All shell commands used `ulimit -v 4000000` and tool timeouts ≤1800 seconds; computations were sequential. No subagent verdict was used.

## Per-claim audit

| Claim | Classification | Independent derivation / qualification |
|---|---|---|
| Definition 1.0 / dictionary | CORRECT-WITH-FIX | A defensible **chosen analogy**, not an exact reduction: monicity models positivity; even degree matches `(−1/P)=1`; odd `deg t` forces the desired reciprocity sign. Integer `d=4uC−1` is always 3 mod 4, whereas polynomial `deg d` need not be odd. C-parity is not preserved. See fixes 1–2. |
| Lemma 1.1 | CORRECT | Since `s=deg t≥1`, the product strictly dominates both subtracted terms, so `n=s+a+b`. Even n forces opposite cofactor-degree parities and excludes the trivial word. Odd n admits `(f+2,1,1)`. |
| Lemma 1.2(i), d-form | CORRECT | `d=tu−1` is monic, `deg u<deg d≤n`, and `f+u=dv`; thus the actual remainder of `−f` is u. Conversely the stated remainder/divisibility conditions give monic `t=(d+1)/r`, `v=(f+r)/d` and the original identity. |
| Lemma 1.2(ii–iii), T1 | CORRECT | `gcd(r,d)=1`; reciprocity gives `(−r/d)=(−1)^(D+Da+a)`, with `D=deg d`, `a=deg r`. Opposite parities make this −1. If f=g², then `−r≡g² mod d`, coprime to d, giving Jacobi symbol +1 even when d has repeated factors. Contradiction. |
| Lemma 1.3, unit line | CORRECT | `f+1=u(t−1)` has an odd-degree divisor iff it has an odd-degree irreducible factor; since n is even, such a divisor has degree <n. The repaired norm implication, not equivalence, is correct. The integer comparison assumes integer input ≡1 mod 4. |
| Shape mass / Tables 2.1–2.2 | CORRECT in audited ranges | Each shape has exactly q^n triples; summing `n−s+1` over positive odd s gives `n(n+2)/4` at even n. No saturation in replays. Counts and zero indices agree; see below. |
| z51 finite-flat word maps | CORRECT | Weighted leading map is multiplication; its zero fibre is only the origin. A homogeneous parameter basis gives finite flat rank `n!/(s!a!b!)`, surviving lower-weight perturbation. The multiplication differential is injective at pairwise-coprime factors by reduction modulo each factor, in every characteristic. |
| §2.3 / §3.2, large-q theorem | CORRECT | In the simultaneous scaled family, the product boundary is étale over squarefree generic f. Its splitting residue field is the generic S_n root field, including after adjoining the roots of f itself; constants are F_q. The boundary n-cycle fixes no ordered partition with two nonempty blocks. Chebotarev therefore counts a positive-proportion **irreducible** no-nontrivial-word event. Every even-degree star shape is nontrivial. The stronger z51 event suffices; no new independence assumption is needed. |
| Corollary 3.2 | CORRECT | For every fixed even n there are zeros for **all sufficiently large** allowed q. Given any bound B, choose an even n≥B; any true threshold must exceed n for sufficiently large q. Thus `N₀(q)→∞`, conditional only on existence of thresholds, not merely unboundedness. |
| Lang–Weil discussion | CORRECT, scoped | Fixed-f fibres of these finite maps have dimension zero, not a positive-dimensional geometrically irreducible fibre to which positivity follows from Lang–Weil. The memo now expressly leaves auxiliary varieties and hybrid growing-n arguments open. Chebotarev itself uses Lang–Weil on higher-dimensional twists; there is no contradiction. |
| Lc-free Weil remark | CORRECT-WITH-FIX in interpretation | For monic nonsquare f, the Weil bound gives some c with χ(f(c))=−1 when q>(n+1)². Take divisor A=T−c and scalar shift r=−f(c); for q≡3 mod4, r is a square scalar. The reconstructed t=(A+1)/r has reciprocal leading coefficient, so this is an enlarged normalization, not an all-monic star word. See fix 3. |
| Prop. 3.1, local blindness | CORRECT | Of Q² pairs `(x,y)`, Q−1 have xy=1. Other pairs determine one z. For f₀≠0 exactly one exceptional pair supplies Q choices, yielding Q²+1; at f₀=0 none does, yielding Q²−Q+1. The integer change of variable by 4 works at odd primes. Blindness is only at primes not dividing the input. |
| §3.1 singular-series mean / composite explanation | EVIDENCE / Assessment only | The Euler product identity is correct, and observed means match. Neither the limiting conditional mean nor an explanation of individual zeros follows from the local count. The phrase “mostly explained” is stronger than the evidence; fix 3. |
| Prop. 3.3, avoiders | CORRECT | Unit squares modulo ℓ^e have index 2: residue units are cyclic of even order and principal units have odd order. CRT gives index `2^ω`. Their images modulo every d dividing M remain squares, contradicting T1 colour for a witness. Summing RH errors gives relative error `O((deg M+1)q^(deg M−n/2))`, uniformly small in the stated range. M=1 follows separately from the prime-polynomial theorem. |
| Stronger subgroup version | CORRECT | Expand the subgroup indicator as `2^(−ω)Σχ`, over quadratic characters. Each nonprincipal prime sum is `O((deg M+1)q^(n/2)/n)`, including prime-power/imprimitive corrections. The resulting error has no Φ(M) factor. The displayed little-o condition suffices; it is not a sharp barrier. |
| Logarithmic menus / least nonresidue | CORRECT, scoped | `deg M_m=Σ_{d≤m}d·π_q(d)⌊m/d⌋ ≍_q q^m`, while `ω(M_m)≍_q q^m/m`. This gives the claimed logarithmic sufficient ranges. RH for the nontrivial quadratic character modulo P also forces a nonresidue prime by degree `2log_q n+O(1)`; this is colour information, not a star witness. |
| Lemma 3.4, composition | CORRECT | Substitution by a nonconstant monic φ is injective, preserves the identity and monicity, and multiplies t-degree by odd k. The sparsity comment correctly excludes k=1 and constant/linear outer f. Decomposable does not mean reducible. |
| Lemma 4.1 / census restriction | CORRECT | If P(c)=−1, `d=T−c`, u=1 gives the explicit word. At q=3 an irreducible of degree≥2 cannot take value 0, so a zero must equal 1 at all c, equivalently modulo T³−T. This is necessary, not sufficient. |
| Even-degree decider / translation quotient | CORRECT | Opposite cofactor parities permit orientation a<b, hence `a≤(n−2)/2` and `a<deg d<n−a`. Factoring P+u and checking every divisor in this window is complete. Translation preserves the conditions; the code retains singleton orbits instead of dividing blindly by three. |
| §4.2 composite structure | CORRECT evidence | All archived composite zeros at degrees 12,14,16 were independently factored and redecided. Small-factor domination and the rough squarefree two-factor tail are real; neither implies an infinite family. |
| §§4.3–4.5 / least-u heuristics | CORRECT as finite evidence | Replayed targeted families agree. They are thin congruence families, not a complete census to norm 3³⁰. Small a* and integer least-u maxima do not prove polylogarithmic bounds or eventual positivity. |

## Decisive source checks

Read z51 §§3.2–3.5 rather than accepting the citation alone. The boundary argument supplies the needed arithmetic/geometric-group equality for the joint root/word cover, not just for separate covers.
Read Andrade–Bary-Soroker–Rudnick, [arXiv:1407.2076](https://arxiv.org/pdf/1407.2076), Appendix A, especially Theorem A.4 and the twisting proof. The permitted Frobenius-coset condition matters and is satisfied here.
Do not justify uniformity merely by extension degree: arbitrary fixed-degree covers can have growing complexity. Here z51 explicitly uses bounded equations/fibre powers at fixed n, which supplies the needed uniform bound. The [2016 correction](https://ndownloader.figshare.com/files/56732546) only repairs equations (1.17), (7.36), not Chebotarev.
Read Rosen, *Number Theory in Function Fields*, Theorem 4.8 and its proof, pp.40–43: the logarithmic-derivative argument has ≤deg M−1 reciprocal roots, of absolute value 1 or √q, giving precisely the required modulus-dependent RH error. Source PDF located through [this copy](https://ebooks.karbust.me/Mathematics/Michael%20Rosen%20-%20Number%20Theory%20in%20Function%20Fields%20(2002)%20%5B978-1-4757-6046-0%5D.pdf).

## Recomputations

`gcc -O2 -Wall -Wextra` builds the archived C engine. Full `.sum` and `.zeros` files match byte-for-byte on replays at `(q,n)=(3,12),(3,14),(3,16),(11,4)`.
At `(3,16)` the full-family zero counts are **0 prime / 15 composite / 6561 square**; sub-line prime zeros are **15** for s≡1, **0** for s≡3, **29070** for s=1; mass=72. Run: 215.80 seconds, 295008 KiB maximum RSS.
At `(3,14)` the full family has no prime zeros but the s≡1 and s≡3 sub-lines have **9 and 3**. At `(11,4)` there are **363/3630** prime zeros, **1441** composite zeros, mass=6.
The committed review script independently enumerates **d and divisors r of d+1**, then f=dv−r, not the C word odometer. Every nonsquare zero index/type agrees at `(3,6),(3,8),(7,4)`; prime/composite/square totals are respectively **3/27/27**, **3/48/81**, **49/252/49**. Exact masses agree.
The full filtered n=12 GP replay gives **19683 candidates / 5460 irreducibles / 1824 representatives / 1 zero representative**, histogram `[690,976,148,9]`, exactly the archived output.
The n=18 replay uses `part=0,nparts=64`: **224202 candidates / 41854 irreducibles / 13925 representatives / 0 zeros**, histogram `[6914,6456,541,14]`.
A separate unquotiented n=18 slice, `k≡17 mod512`, has **5257 irreducibles**. All returned t,u,v are monic polynomials with odd t-degree and satisfy the exact identity; histogram `[2579,2505,168,5]`.
This checks a degree-18 slice and the algorithm, **not** an independent full degree-18 certification. The full archived log is internally consistent: 14348907 candidates, 2689596 irreducibles, 896556 representatives, zero zeros; 36 singleton translation orbits explain why representatives are not exactly irreducibles/3.
All **67/51/15** archived composite zeros at n=12/14/16 are redecided as zeros. Factor types include squarefree 2·10, 3·9 at n=12 and 2·12 at n=14; all 15 at n=16 have at least two distinct linear factors.
Factoring the integer screen reproduces **285 total, 214 with smallest factor 3, 274 with smallest factor≤13**; the 11 rough examples have 2 distinct prime factors (10 cases) or 3 (1 case).
Target replays: M₂,n=18 gives **729 candidates / 219 irreducibles / 0 zeros / max a*=3**; M₂ times four cubics,n=30 gives **729 / 139 / 0 / 3**. No capped undecided cases.
Local solution counts independently match at Q=3,7,11. Large q=7,n=10 and q=11,n=6 censuses and the integer least-u scan were not rerun; they are not needed for the verdict.

Reproduction (extract the reviewed files into `/tmp/xrev_FFIELD` first):
```sh
ulimit -v 4000000; timeout 1800 uv run --with cypari2 python scripts/z58_xrev_ffield_check.py /tmp/xrev_FFIELD
ulimit -v 4000000; timeout 1800 gcc -O2 -Wall -Wextra -o /tmp/xrev_FFIELD/z58ff /tmp/xrev_FFIELD/scripts/z58_ffield_enum.c
ulimit -v 4000000; timeout 1800 /tmp/xrev_FFIELD/z58ff 3 16 star /tmp/xrev_FFIELD/replay_q3_n16
```

## Mandatory falsifiers

| Screen | Hostile assessment |
|---|---|
| F1 odd squares | **PASS in the model.** The proof genuinely reproduces the Jacobi obstruction, including composite witness moduli; all square counts replay correctly. Do not turn this proof into a necessity theorem about all possible proofs. |
| F2 twelve numerator-8 zeros | **PROXY ONLY, honestly admitted.** The integer screen contains 12 entries. There is no C-parity transport; s mod4 proxies reproduce finite sub-line failures, but s≥3 does not extend the last observed prime-zero degree. No eventual sub-line failure follows. |
| F3 285 composite zeros | **PASS qualitatively, not a transfer theorem.** Both small-factor enrichment and rough tails check out. Positivity for every nonsquare is false in this monic model. The lc-free theorem concerns a different witness set, not a contradiction to these zeros. |
| F4 14 star / 38 𝔊* prime zeros | **PARTIAL.** The integer files contain 14 and 38 entries. FF prime zeros genuinely obstruct uniform positivity and resemble star failures. No 𝔊* analogue, nor mapping/testing of these 38 inputs, is supplied. Calling this a full F4 reproduction needs qualification. |

## Required fixes, priority order

1. **Scope/faithfulness:** replace “behaves like the integer problem in every respect tested” and unqualified “F4 reproduced” with the precise assessment: T1-compatible star model, qualitative F3/star-F4 agreement, F2 proxy only, **𝔊* portion of F4 unmodelled**. “Exact analogue” means the chosen word/divisor identities, not a reduction preserving all integer arithmetic. No HOT LEAD or “survives all four” conclusion is justified.
2. **Proof necessity:** final F1 says an FF argument “must use non-squareness at the Jacobi symbol.” Only this proof does. Replace with “the T1 proof here uses…”; other algebraic, spectral or global proofs are not excluded. Likewise the odd-degree colour restriction is sufficient and deliberately chosen, not uniquely forced by the integer statement.
3. **Causality/domain:** change §4.2 “composite zeros are mostly explained” to “small-factor enrichment is consistent with the local-density deficit.” In the lc-free remark say that the enlarged-set theorem cannot be transferred to the monic model without new input, rather than suggesting it is itself falsified by monic zeros.

**Final decision:** retain the core PROVED/CERTIFIED results and the verdict **narrowed**, after these scope repairs. Fixed-q eventual positivity, a faithful numerator-8/𝔊* dictionary, and any route from this model back to integer (MS) remain open; no general method-impossibility theorem is established.

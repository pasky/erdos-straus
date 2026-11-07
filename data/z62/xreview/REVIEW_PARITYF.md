# z62 PARITYF — cross-model hostile review

**Verdict: ACCEPT-WITH-FIXES, for the scoped elementary results only; do not bank the current blanket PROVED/no-go claims.**
Reviewed `side-agent/z62-parityf` at `b080ebc3d7023a7f82a1e698b68803319a7694a6`, including all 188 memo lines and relevant scripts/data; compared `side-agent/z62-parity:Z62_PARITY.md` and prior repository sources.
The defensible outcome is **narrowed / no HOT LEAD**, not exclusion of ES-based parity constructions. ES remains open.

## Per-claim audit

| Claim | Classification | Independent finding / necessary repair |
|---|---|---|
| Lemma 1.1; Lemma 1.2a | CORRECT | Divisibility types, distinctness for p ≡ 1 (4), and exclusion of p from gabc follow from the stated inequalities. |
| Proposition 1.2 master bijection | CORRECT-WITH-FIX | The squarefree reconstruction is sound, but the forward proof assumes without proof that denominator p-adic exponents are ≤ 1. Supply the short argument below. |
| Corollaries 1.3–1.4; Proposition 1.5; Remark 1.6 | CORRECT | Substitution gives the two shapes, positive k and divisibility conditions; `(ty−px)(tz−px)=p²x²` gives the three divisor classes. Retain the i-label in the Type-I swap. |
| “Equivalently” paragraph after 1.5, Type II | WRONG as a parameter correspondence | Subtracting a p-free denominator does not force the remaining two to be p-divisible: p=13, m=5, k=7 gives `7/65=1/10+1/130`, a Type-I solution, while no factorization Gab=5 has 7|a+b. Require both residual denominators divisible by p; the unrestricted residual test is only necessary here. |
| Theorems 2.1–2.2 | CORRECT-WITH-FIX | Fixed points, oddness, slices, and c=1 targets are correct. In 2.1(iii), the parenthetical `a|2p,c|2p` does not derive the five exceptional pairs (it excludes (2p,3p)); instead solve r|1+s, s|1+r after a=pr,c=ps. |
| Theorem 2.3 and S′ chain | CORRECT | K,J and inverses satisfy the divisibilities; their conjugated involution is exactly the swap. The coprimality condition on T is essential and correctly retained. |
| Proposition 2.4(i)–(iv) | CORRECT | Reciprocity works, including the even part of G and composite odd n in (iii)/(iv); see derivation below. No hidden primality is needed for the square obstruction. |
| §2.4 Consequence; Proposition 3.5 | WRONG in one algebraic assertion; otherwise heuristic | Type-I **G does not divide 4Ga²+1**: their gcd is 1, whereas G is a nonresidue and hence G>1. It is D=4Gac−p that divides this integer. Delete the claimed QNR-divisor conclusion for G. The polynomial/congruence no-go is not established by reciprocity. |
| Theorem 2.5 | CORRECT | Finite support ≤p+2, the unique possible smaller neighbour, roots, child divisors and ES-edge test all follow. This is the previously studied word forest, not a new structure. |
| Remark after 2.5 | WRONG as a general obstruction | An unrooted forest need not have only sibling-permuting automorphisms (even a two-vertex tree has a root-reversing automorphism). Neither that assertion nor the fixed-vertex theorem prohibits a useful arithmetic involution/index. |
| Lemma 3.1 | CORRECT premise; WRONG unrestricted conclusion | A **swap-closed** set of ordered solutions has even size. An arbitrary subset, quotient, or asymmetric decoration need not: 409 has 15 unordered solutions. Thus “ES solutions can only be fixed points, never the set” does not follow. |
| Lemma 3.2; Theorem 3.3 | CORRECT, scoped | Odd S_p with empty 4|g target cannot have a target-only fixed set. This kills that support at the F4 primes, not every map from S_p to other ES certificates, nor thresholded claims avoiding them. |
| Theorem 3.4 fixed-point formulas and ES map | CORRECT | The two formulas re-derive exactly; U_I's prime-only qualification is necessary. All 4|g elements give genuine ES identities. |
| Theorem 3.4 “for odd squares ... U_I does [contain a 4|g element]” | GAP | The n=9 example proves **some**, not every, odd square. At n=q², q odd prime, this existence is equivalent to Type-I existence at q; see below. Do not label universal square existence PROVED. |
| §4.1, §4.3–4.5 | CORRECT in checked ranges | c=1 counts, 409/577 solution counts and c-values, Jacobi checks, and K-set orbit counts reproduce. |
| §4.2 U_II cardinalities | WRONG | The enumerator truncates a at n+2 but admits its swapped partner b up to 2n+2. Corrected counts below. Fixed counts and the non-uniform-parity conclusion survive. |
| §4.6 prime decoration table | CORRECT for its 18 tested features | Independent enumeration reproduces every prime total. No feature is uniformly odd, including on the ten p ≡ 1 (24) controls in the archived table. |
| §4.6 square controls / universal no-go | WRONG scope | The code silently drops composite solutions without its prime-style master representation. At 9 it counts 2 of 6 unordered solutions; at 25, 1 of 10. “No one-variable-split Zagier set exists in these coordinates” exceeds the finite dictionary tested. |

## Proof checks and missing hypotheses

**Master exponent repair.** If only one denominator is divisible by p, valuations force exponent 1. If two are, unequal exponents force the larger to be 1. If both exponents are ≥2, the p-free denominator x obeys `4/p ≤ 1/x+2/p²`, hence `x ≤ p²/(4p−2) < (p+1)/4`; but `x>p/4` and x integral imply `x≥(p+1)/4`. Contradiction. The mutual divisibilities of the p-free parts then yield common squarefree g and unique a,b,c exactly as claimed.

**Jacobi, Type II.** Put d=4Gac−1. The identity `d(4Gbc−1)=4Gnc²+1` gives `(−Gn/d)=1`, with gcd(2cG n,d)=1. Here `(−1/d)=−1`, `(G/d)=1`: odd factors of G cancel by reciprocity and, if G is even, d≡7 (8). Thus `(n/d)=−1`. For p≡1 (4), reciprocity gives `(d/p)=−1`; for square n this is impossible.
**Jacobi, Type I.** From `4Gab−1=pk`, `kc=a+b`, obtain `kD=4Ga²+1`, D=4Gac−p>0. Then `(G/D)=−1` because D≡3 (4), and reciprocity with D≡−p modulo 4Ga gives `(G/D)=(G/p)`, including the 2-part. Also `(Gab/p)=1`, hence `(ab/p)=−1`. The same calculation with c=1 and any odd n≡1 (4) proves (iv). G itself is not the divisor D.

**Square-existence gap.** In `c(4Gab−1)=q²(a+b)`, q²∤c by `4Gab−1>a+b`. If q∤c, q²|4Gab−1 and the same reciprocity argument gives `(G/q²)=−1`, impossible. Hence c=qc′, and division by q gives `c′(4Gab−1)=q(a+b)`, precisely a Type-I witness at q. Conversely multiply a Type-I c′ at q by q. Thus the claimed all-square existence is not a consequence of the example or Jacobi proof.

**Fixed points.** In U_II, a=b gives δ=ga²−n|2a and c=2a/δ, with a²|n+δ; a=1 contributes two. In U_I, a|c, c=ac′, and `c′(ga²−1)=2n`. For prime p the four divisors 1,2,p,2p give `2+s(p+1)+s(2p+1)`. These derivations also prove finiteness of the fixed loci; full-set finiteness follows from the bounds documented in the checker.

## Numerical re-verification

Command: `ulimit -v 4000000; timeout 1800 uv run --with sympy python scripts/z62_xrev_parityf_check.py --screens` — **PASS**. Scalar/divisor-list enumerations only; no dense products. Independent ES enumeration uses divisors of (nx)², not the lane's y-loop; independent universal enumeration restores both orders with proved bounds.

* Full U_I/U_II fixed formulas and parity checked for every odd n≤101. U_I fixed counts at 9,15,25 are 7,11,6.
* For p=5,13,17,29,37,41,53,61,73,89,97, corrected **|U_II| = 28,42,57,80,60,88,105,81,81,151,110**; fixed counts remain 2,2,3,2,2,2,3,3,3,3,4. All eleven U_I counts match the memo.
* Missing at p=5: `(g,a,b,c)=(1,8,1,3),(1,11,1,2)`. Generally exactly τ(p+1)−2 rows are omitted: `(1,p+δ,1,1+(p+1)/δ)`, δ|p+1, δ>2. This number is even for odd p, and all have g=1; hence neither the quoted prime parities nor the ES/Jacobi conclusions change.
* c=1 claims reproduce for all 59 primes p≡1 (4)≤700 and all odd squares≤700. All 15 listed forest examples reproduce, including every reported root set and absence of ES-edges at 409,577,5569.
* All prime ES solutions through 600 pass master recovery and the Jacobi tests (the −1 assertions restricted to p≡1 (4)); 409 and 577 have 90 and 108 ordered solutions, with marked Type-II c respectively {2,3,4,15}, {2,5,10,21}.
* K-set unordered counts: 7,11,15,18 at 5,13,17,29; exactly two swap-fixed points each.
* Decoration odd-prime totals, in script column order, are **28,30,29,28,16,12,19,20,0,28,0,30,29,18,22,8,28,24**, each out of 51: exact agreement.

## Is the “uniformly odd split” real?

**Version mismatch:** this pinned memo's §4.6 explicitly says *none* of its ES decorations is uniformly odd; there is no positive uniform-odd claim there to validate. Ordered factorizations Q=uv give multiplicity τ(Q), whose parity is [Q square]. For its listed ES features the counterexamples are real, but they exclude only those features.
If the intended candidate instead splits **universal c** into two factors, a small-range apparent oddness is false: U_II(241) has **44** elements with square c, and U_I(769) has **176**. Their square-c swap-fixed rows are respectively `(243,1,1,1),(3,9,9,9)` and `(1539,1,1,1),(19,9,9,9)`, so each decorated total is even. Both primes are ≡1 (24). These are independently checked, not claims attributed to the pinned text.
In any case an odd count on a universal set does not force 4|g: the trivial fixed rows have g=243 or 1539, not ES support. A second involution/index with certificate-supported fixed points is still missing.

## Mandatory falsifiers

| Screen | Verified behaviour and required qualification |
|---|---|
| F1 odd squares | Type II and Type-I c=1 vanish by the valid Jacobi proofs; S/S′ oddness alone has no ES implication. General U_I can contain imprimitive square witnesses (9), but universal square existence is not proved. A successful Type-II argument must distinguish its domain from squares, not necessarily use primality rather than merely nonsquareness. |
| F2 12 numerator-8 zeros | Replayed the exact z57 engine at all 12 supplied primes: every R and R8 matches, with R>0, R8=0. Thus C-even support is insufficient on a domain containing them; the memo's C-odd/other-shape escape is correct. |
| F3 285 composite zeros | Replayed the z58 census through 9·10⁶: exactly the supplied 285 nonsquare composite zeros below 8·10⁶. Universal parity makes no contrary existence prediction; prime-only claims need not extend here. |
| F4 14 ★ / 38 𝔊* zeros | All 14 ★ zeros reproduced by that census. Replayed z56 𝔊* decisions (independent small-p enumeration below 1000): all 38 zeros agree, **24 have R>0**. The memo omits the 𝔊* half entirely: add it, and never identify 𝔊*-emptiness with S_p target-emptiness. |

The screen replays use existing certified engines, not a claimed independent rescan of every prime through 10¹⁰. Independent S_p enumeration already supplies the decisive 409/577/5569 contradictions.

## Prior art inside the repository

Ran the requested `git grep -il 'windmill\|zagier\|involution' -- '*.md'` and inspected the directly relevant matches.
* **S_n is exactly the old X(n)** of `INVOLUTION_ES.md` §§0–2: same equation, swap, fixed-point formula and periodic point (n+2,1,1), with square-obstruction analysis already present. The 4|g target differs from that memo's 4|gu−1 target; do not conflate those slices.
* **Γ_p is exactly the old word forest**: `FOREST_H4.md` §1 and `FOREST_CONNECTIVITY.md` §1 already give vertices≤p+2, parent (−p mod v), divisibility criterion and forest property; they study stronger five-slot ES information and much larger censuses.
* `EXACT_FORMULA.md` setup/§2.1 already has both algebraic Type-I/II shapes and the unrestricted Type-II square obstruction, with the same factorization/Jacobi proof (even squares included). Its composite Type-I discussion explicitly treats imprimitive square witnesses. `DEDEKIND_ES.md` §3 and `INVOLUTION_ES2.md` §5 supply related Jacobi constraints; these are not a newly discovered square-killing mechanism.
* The parity template, support-at-zeros obstruction and weighted-certificate formulation are prior in `WINDMILL.md`, `INVOLUTION_ES.md`, and **Z62_PARITY Lemmas P0/P1**. PARITY carefully allows known fixed points, decorations and thresholds; PARITYF's broad no-go should not undo that scoping.
* `WINDMILL.md` §3.1 already tests square indicators of ES coordinates and derived quantities, including g,a,b,c and multiplicity weights, on 732 primes; §4.6 is a smaller related replication, not a new decoration programme. PARITY tests other finite river/Jacobi dictionaries without excluding arbitrary weights.
* The explicit squarefree master packaging, the particular S′ jump chain, and the U_I/U_II fixed-count formulas may be useful additions in this presentation; I found no exact prior formula for the latter in the inspected sources. This is not an exhaustive novelty or literature priority claim.

## Required fixes, priority order

1. Restrict Lemma 3.1 and every downstream “cannot” to swap-closed ordered sets; remove the forest-automorphism no-go and the global split-decoration exclusion.
2. Replace “U_I has witnesses at odd squares” by the explicit examples/conditional statement; repair the Type-I QNR-divisor assertion (G versus D) and the Type-II residual-fraction equivalence.
3. Fix U_II enumeration and regenerate `universal_counts.txt`; retain the valid fixed formulas and non-uniform-parity conclusion with corrected cardinalities. Label composite decoration rows as a filtered subset or redesign that control.
4. Supply the missing p-adic exponent proof, repair the exceptional-pair derivation, and add all 38 𝔊* controls with the 24/38 distinction.
5. Attribute the old X(n), forest, Jacobi/square obstruction and weighted-count programme. Keep the verdict **no new forcing mechanism; scoped candidates narrowed**, not “parity on ES coordinates is impossible.”

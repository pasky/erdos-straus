# O215 hostile review

Reviewed `d0c91bcf..6c32664d720d12b942ffce81a38cb521da420108`, restricted to `SEVEN_SIBLING.md`, committed `BRAINSTORM/y7_*.md`, `scripts/y7_*.py`, and `reviews/agent-reports/AGENT_REPORT_O215.md`. Merged main/Y5 material is not reviewed. Earlier results are consulted only to check O215's citations.

**Verdict: changes required.** The finite covering results, explicit identities, square-search counts, and integral-isometry counterexample survive. The identification of II-e with the T1-bearing shot family is false; the field statement for M = 6 is false; several conclusions go substantially beyond the evidence. There is also an actual prime-sieve bug in the split-norm experiment. No original deliverable was edited.

All computational checks below used `ulimit -v 4000000` and an explicit `timeout` (30–180 seconds), with Python run through `uv`. No dense Cartesian-product arrays were allocated.

## Findings

### D1 — MAJOR: II-e is not the square-shot family and is not sterile at odd squares

Locations: `BRAINSTORM/y7_full_t1.md:4–5,23–25`; `SEVEN_SIBLING.md:35–42`; O215 report SHARP 2.

The cited O212 obstruction concerns `g | n + M Q²`, with `g ≡ −1 (mod M)`. O215 silently replaces `Q²` with `a²d`, allowing arbitrary positive d. This destroys the obstruction, even for odd g.

Explicit counterexample: M = 7, n = 25, `(a,b,c,d,e) = (1,2,1,2,3)`. Then

- `7abd = 28 = 25 + 3`, and `a+b = ce = 3`;
- `g = 7acd − 1 = 13` is odd and divides `25 + 7a²d = 39`;
- `7/25 = 1/4 + 1/50 + 1/100`.

This is precisely an II-e identity at an odd square prime to 7. The cited O212 theorem remains correct: `(−7/13) = −1`, but `(−14/13) = +1`. The nonsquare factor d matters. Restrict to the actual square-shot subfamily (for example square d, with the original admissibility hypotheses), and stop identifying all II-e families with it. The useful conclusion “7 lacks full Type-I/II T1” survives, but the proposed explanation of which family retains T1 does not.

### D2 — MAJOR: Q(sqrt(−6)) is not Q(sqrt(−3))

Locations: `SEVEN_SIBLING.md:28`; `BRAINSTORM/y7_free_inert.md:1,6,9–12,18–28,38`; O215 report goal (a).

For M = 6, the non-free units are p ≡ 1 (mod 6), the splitting classes of Q(sqrt(−3)), not Q(sqrt(−6)). Concrete counterexamples:

- p = 5 is free, but `(−24/5) = +1`, so it splits in Q(sqrt(−6));
- p = 13 is non-free, but `(−24/13) = −1`, so it is inert in Q(sqrt(−6)).

The script itself reports characters −12 and −3, not the discriminant −24 of Q(sqrt(−6)). Its “some odd quadratic character” experiment does not establish the stated “the field Q(sqrt(−M))” proposition. The correct character-kernel classification can retain {4,6,7}; the literal specified-field classification cannot retain 6. The norm `x²+xy+y²` in the memo already points to the correct field.

Moreover `y7_free_inert.py:38–44` tests only eight representatives, discards zero character values, and contains `... or True`. This is not a rigorous conductor/periodicity test and cannot justify the word “exhaustive” for characters. Replace it with exact character/conductor checks or give the short elementary classification: at most three free units forces φ(M) ≤ 6; for M ≥ 3 the candidates are 3,4,5,6,7,8,9,10,12,14,18, which can be checked exactly.

### D3 — MINOR theorem defect: the unrestricted prime conclusion includes p = 2

Locations: `SEVEN_SIBLING.md:53`; O215 report SHARP 1.

2 is not 1 modulo 105, but 7/2 > 3, whereas three positive unit fractions sum to at most 3. State **every odd prime** (or p ≥ 3). The memo's Theorem Y7.1 already has the safe coprimality hypothesis.

No hidden problem occurs at 11,13,17,19; explicit witnesses are below. The primes 3,5,7 also work, respectively `(1,1,3)`, `(1,5,5)`, `(3,3,3)`. Part (c) should explicitly inherit “n odd”: n = 8 satisfies its written mod-7/mod-5 conditions, but the claimed e = 13 family requires n ≡ 43 modulo 70, not 8 modulo 70.

### D4 — MAJOR overclaim: finite covering counts do not prove the asserted asymptotic or constrain every possible proof

Locations: `SEVEN_SIBLING.md:72–79,95`; `BRAINSTORM/y7_mordell_levels.md` Barrier screen; O215 report sparks.

The seven per-prime counts reproduce, but they do not establish a uniform O(1) bound as ℓ grows. Even such an upper bound alone would not establish “decays like a power of log”: that needs quantitative lower/upper information and justification of the relevant product model. The script counts classes covered for **every** base lift, not the full covered mass; partial lifts and families at levels involving several new primes are not controlled by this statistic. Label the extrapolation heuristic, or supply the missing theorem.

Likewise the assertion that a 7/p proof must use “size/positivity and nothing else” does not follow from an obstruction to these five fixed congruence families. A proof can use arithmetic, analytic, or moving-parameter information not represented by this menu. A prime cannot literally have p−1 divisible by every small prime simultaneously without a quantified cutoff; the valid statement is that each fixed finite menu leaves an arithmetic progression containing infinitely many primes.

The class-one obstruction forces residue 1 at the menu's common modulus. At level 840 it does not, just by itself, force all four residues 1,211,421,631. Those extra survivors are a verified feature of this menu, not automatically an independently “PROVED-forced set.” The fixed-level core is not a description of all unsolved primes or of the unrestricted identity problem.

### D5 — MINOR code defects and scope problem in the split-norm experiment

Locations: `scripts/y7_split_norm.py:25,42–45`; `SEVEN_SIBLING.md:16,99–100`.

`spf[1] == 1`, so `0 < n <= X and spf[n] == n` admits n = 1. It also passes `p % 21 == 1` and is counted as a double failure. All three X = 10⁶ runs contain **6,531 observations and 1,818 failures**, rather than 6,530 and 1,817. Require n ≥ 2.

For q = 5, the p ≡ 4 stratum has rate zero and contributes no tested cells, but `len(byp)` still subtracts it as a fitted parameter. There are six nondegenerate cells in three tested strata, so the nominal degrees of freedom are **3, not 2**. For general inputs, discarding small cells while estimating the mean using all cells also needs a defensible testing convention. q = 4 has zero degrees of freedom, so its zero statistic supplies no evidence for independence.

More fundamentally, the script examines finite residue classes modulo q = 4,5,9, quotiented by conjugation; it does not measure the archimedean Hecke angle, all ray characters, or all Hecke inputs. “No detected association in these tested residue partitions” is supported. “No Hecke-angle input” or a general absence of an algebraic-field mechanism is not.

### D6 — MINOR: property P contradicts its own definition at M = 3

Locations: `SEVEN_SIBLING.md:66–69`; `BRAINSTORM/y7_mordell_levels.md` Reading; O215 report goal (b).

The empty set is neither the full unit-square set nor a class-one fibre modulo a divisor of 840: both contain residue 1. Thus P(3) is false as defined, although the document says it holds. Add an explicit empty-core alternative or remove 3. Also make the exceptional level choice for 11 part of a single consistent definition, and state the tested numerator range when saying 6 is the “only” failure-free numerator outside P. The finite observations for 4,5,7,8,11,12 themselves reproduce.

### D7 — MAJOR interpretation problem: one-solution examples do not rule out an existence mechanism

Locations: `BRAINSTORM/y7_near_misses.md` Idea, Luck estimate, Assessment; `SEVEN_SIBLING.md:83–86`; O215 report goal (c).

The arithmetic is essentially right: 18 zeros and 34 ones give 18/52 = 0.3461538, and the proposed independent exchangeable model gives `(34/52)^3 = 0.2795289`. Rounding first to 0.65 gives 0.274625, explaining the displayed 0.27. This is not a material arithmetic error.

The inference is the problem. The three exact examples rule out a universal lower bound f₇ ≥ 2, **not** a structural theorem guaranteeing f₇ ≥ 1, nor a mechanism valid beyond a finite threshold. “If there were a mechanism, f should stay away from zero” already holds when f ≥ 1. “Not a hidden existence input” and “yes, lottery-lucky” are unsupported verdicts; the defensible conclusion is consistency with a deliberately crude model.

Pooling different numerators and different prime ranges, and treating observations at overlapping primes as independent, is not a calibrated probability model. The caveat in the memo is good but does not rescue the categorical conclusion. Keep finite upper limits beside the counts and the minimum-f₄ claim: the deep file's “min f = 6 on p ≥ 11” reads as an unbounded theorem, whereas the evidence is a finite census.

### D8 — MINOR: full-T1 labels are inconsistent, but the intended equivalence is repairable

Locations: `BRAINSTORM/y7_full_t1.md:19–29`; `SEVEN_SIBLING.md:33–37`; O215 report SHARP 2 and caveats.

The script is sound for the documented domain. Type II is complete because
`e ≤ a+b ≤ ab+1 ≤ abd+1 = (n+e)/M + 1`, hence `(M−1)e ≤ n+M`.
`hit` enumerates all a,b with ab dividing N, leaving positive integer d. The Type-I search is bounded by e ≤ 200; a zero count alone proves no unrestricted negative statement. All seven rows reproduce.

There is a simple missing proof for the claimed Type-I zero rows at **all** M = 4h, not just 8,12: a Type-I or Type-II tuple for M = 4h gives one for numerator 4 by replacing d with hd. The known numerator-4 square obstruction therefore excludes both types. Conversely `POINTWISE_MN` Prop 2.1 supplies square-consistent Type-II atoms whenever 4 does not divide M (in its stated domain M ≥ 4); CRT gives odd square n prime to M in such a class, and positivity gives a valid tuple. Thus full sterility of the union of Types I/II really can be proved equivalent to 4 | M, with domain and references made explicit. M = 3 is separately trivial.

Do not simultaneously call this an evidence-only statement and assert the infinite classification without that bridge. “Strictly weaker/easier model” should remain a comparison of this particular barrier, not a proved logical or complexity comparison between conjectures. D1 still invalidates the claimed identification of the surviving shot subfamily.

### D9 — MINOR: order-3 conclusions exceed the actual test

Locations: `BRAINSTORM/y7_order3.md:21–28,36–38`; `scripts/y7_order3.py:22,30–31`; `SEVEN_SIBLING.md:89–91`.

The exact counts 1771/19564 and 1817/6530 reproduce. The factor test is correct on these populations: the relevant N are prime to 3, and for M = 7 also odd. A divisor prime ≡ 2 modulo 3 supplies a = 1,b = q; without such a prime all divisors are 1 modulo 3. The parity distinction with M = 4 is real.

However p ≡ 1 modulo 21 is a **necessary ambient congruence**, not the actual double-failure set (only 27.8% fail there), and it is not a sub-core of n ≡ 1 modulo 105. The cited double-failure p = 43 already disproves that containment.

`cube(a,p)` records only whether the cubic character equals 1; it merges its two nontrivial values. Eight Boolean cells are not a test of the full three-valued cubic characters (up to 27 cells for a chosen identification). Say “no detected association with these cubic-residuosity indicators,” not “no cubic residue pattern.” Independence of the two shifted-prime factorization events and the asserted 1/log p law are heuristics, not consequences of the displayed counts or of the ordinary Landau counting theorem. Also N_I ≈ ep/M, not p/M, although this constant does not change the proposed logarithmic exponent.

### D10 — MINOR delivery/wording defects

- The report claims seven committed memos. There are only six. `BRAINSTORM/y7_split_norm.md` exists in the working tree but is **untracked** at the reviewed HEAD; a clean checkout cannot read the memo cited throughout. It was inspected only as working-tree context, not treated as a committed change. Commit the intended memo separately; this review leaves it untouched.
- `SEVEN_SIBLING.md:54–56` conflates levels: at 14,42,70,210 the uncovered unit residue set is {1}; at 840 it is {1,211,421,631}. The cited script's main routine tests primes only, not all integers, and deliberately skips primes dividing the level. Distinguish these populations and preserve a reproducible all-integer command.
- `SEVEN_SIBLING.md:11` writes `n ∤ 14`, but the local argument needs 7 ∤ n (and its stated prime/odd hypotheses). The present condition even admits n = 49. “Hasse invariant” should be distinguished from the project's isotropy/Clifford sign ε; in particular the inherited ε∞ = −1 is an anisotropy sign, not the usual Hasse invariant of a positive-definite diagonal form.
- `SEVEN_SIBLING.md:14` says marking dependence occurs for **every M ≠ 4**, whereas the examples establish only M = 5,7,8,11. In fact, for prime n ≠ 3, S₃ is all words: if none of t,u,v,tu−1,tv−1 is divisible by 3, then u = v = −t modulo 3 and n = tuv−u−v = 0 modulo 3, a contradiction. Thus S₃ is a constant lattice-class function.
- “Prop 2.1” references in the deep file should point to Prop Y7.2 in the lattice memo.
- `y7_lowcounts.py` hardcodes `/tmp/y7_cnt_M.txt`; the claimed near-miss lists are not reproducible from a clean checkout without a documented generation command and the actual upper bound per numerator. Its interval summaries do not themselves print the claimed zero/one lists. Temporary files on this host agree with the listed sibling counts, but are not durable evidence artifacts.

## Positive verification: every Thm 3.1 identity

All quantities here are positive integers for the stated positive odd n; repeated denominators are allowed.

| Class | Denominators | Sum before substituting d |
|---|---|---|
| n ≡ 6 (7), 7d = n+1 | d,2dn,2dn | (n+1)/(dn) = 7/n |
| n ≡ 5 (7), 7d = n+2 | d,dn,dn | (n+2)/(dn) = 7/n |
| n ≡ 3 (7), 7d = 2n+1 | dn,d,d | (2n+1)/(dn) = 7/n |
| n ≡ 2 (7), 14d = 3n+1 | 2dn,d,2d | (3n+1)/(2dn) = 7/n |
| n ≡ 4 (7), 14d = n+3 | 2d,dn,2dn | (n+3)/(2dn) = 7/n |

For the last two rows the numerator defining d is divisible by 7 and is even, hence divisible by 14. All d are positive. Examples: p = 11 gives (2,11,22); p = 13 gives (2,52,52); p = 17 gives (85,5,5); p = 19 gives (3,57,57).

For n odd, n ≡ 2 modulo 3: n+1 is a positive multiple of 6. With b = (n+1)/6,
`1/n + 1/b + 1/(bn) = [b+n+1]/(bn) = 7/n`.
The smallest positive n is 5, b = 1; no small-n positivity exception occurs.

The level-70 families, restricted to odd n ≡ 1 modulo 7:

- n ≡ 4 modulo 5 means n ≡ 29 modulo 35. With d = (n+6)/35, the sum `1/(5d)+1/(dn)+1/(5dn)` is `(n+6)/(5dn) = 7/n`.
- n ≡ 3 modulo 5 gives n ≡ 43 modulo 70. Put c = (n+27)/70 ≥ 1, b = 13c−5 = (13n+1)/70 ≥ 8. Then `7·5·b·2 = 13n+1`, `5+b = 13c`, and the denominators are `10bn,10c,2bc`.
- n ≡ 2 modulo 5 gives n ≡ 57 modulo 70. Put c = (n+13)/70 ≥ 1, b = 27c−5 = (27n+1)/70 ≥ 22. Then `7·5·b·2 = 27n+1`, `5+b = 27c`, with the same denominator formula.

For either I-c family their reciprocal sum is
`[c+bn+5n]/(10bcn) = [1+en]/(10bn) = 7/n`.
At 43 this yields (3440,10,16); at 127 the e = 27 family yields (62230,20,196). The separate exhaustive `y7_sols.sols` search verifies unique solutions at 43,127,211, including (438880,32,520) for 211.

## Positive verification: all five general family types

Assume fixed parameters are positive integers, M ≥ 3, n ≥ 1, and the printed divisibility conditions hold. Add the necessary `gcd(e,Mab)=1` when writing an inverse in I-d (the script correctly enforces it).

- II-d: `d=(n+e)/(Mab)` is a positive integer and `c=(a+b)/e` is a positive integer.
- II-c: `c=(n+e+Ma²d)/(Made)` is a positive integer; `b=ce−a=(n+e)/(Mad)>0`.
- II-e: `g=Macd−1>0`, `e=(n+Ma²d)/g>0` is integral; `b=ce−a=(cn+a)/g>0`.
- I-d: `d=(ne+1)/(Mab)>0` is integral, and `c=(a+b)/e>0` is integral.
- I-c: with `t=Ma²d+1` and e dividing t, `c=(n+t/e)/(Mad)>0` is integral; `b=ce−a=(ne+1)/(Mad)>0`.

Thus the positivity claim is correct for every positive n in each class, not merely asymptotically. The Type-II reciprocal sum is `(cn+a+b)/(abcdn)=(n+e)/(abdn)=M/n`; the Type-I sum is `(c+n(a+b))/(abcdn)=(1+ne)/(abdn)=M/n`.

## Positive verification: covering and search implementations

No coverage-inflating defect was found in `y7_mordell_cover.py` or `y7_cover_verify.py`:

- `add` explicitly rejects moduli not dividing L. Every generated q or g is already a divisor of L.
- All five residue signs and the modular inverse in I-d agree with the identities.
- II-e determines positive c from acd; not explicitly storing c in `cover` loses no necessary condition.
- The certificate generator reconstructs the same families. Integer divisions are justified by membership in the generated residue class; its public `cert` helper itself assumes that precondition.
- The prime harness checks positivity and exact rational equality but accepts the first valid certificate. It is not, by itself, a validation of every generated family. This review additionally tested **every** generated family at its least positive class representative, the next representative, and a representative 100 periods later, for M = 3,4,5,6,7,8,11,12 at the documented small levels. All passed. The algebra above covers the unbounded tail.
- The union of the certificate generator's classes equals the covering code's class set at those levels.

Reproduced all table counts, including the larger levels:

| M | L | Uncovered | Unit squares among uncovered / all unit squares |
|---|---|---|---|
| 4 | 840,2520,9240,27720 | 6,18,34,96 | 6/6,18/18,30/30,90/90 |
| 7 | 14,42,70,210 | 1,1,1,1 | unique uncovered residue 1 |
| 7 | 840,2520,9240,27720 | 4,10,10,17 | 1/6,3/18,1/30,3/90 |
| 5 | 840,2520 | 2,2 | — |
| 6 | 840 | 11 | — |
| 8 | 840,2520 | 23,48 | 6/6,18/18 |
| 11 | 9240 | 28 | — |
| 12 | 840 | 44 | — |
| 3 | 840 | 0 | — |

For the expensive larger-level runs I substituted an exactly equivalent sqrt-time divisor enumerator **in memory**, leaving the covering logic unchanged. This avoids the production function's linear scan up to numbers of order L²/M and its roughly 30-minute runtime. The original divisor implementation is inefficient, not mathematically wrong.

All positive integers n ≤ 300000 coprime to L were checked with exact Fraction certificates for L = 14,42,70,210. Certified/uncovered counts: 107142/21429, 78571/7143, 98571/4286, 67142/1429; every uncovered n is 1 modulo its level. The unmodified prime harness at M = 7,L = 840,X = 10⁶ reports 76871 certified and 1623 uncertified, with residues **1,211,421,631**. The stated per-new-prime lists also reproduce exactly.

`y7_full_t1.py M 99 200` reproduces every table row for M = 4,5,6,7,8,11,12. Its first Type-II hit for 7 is n = 25, which is exactly the D1 counterexample.

## Positive verification: qfisom example, without trusting qfisom

For the n = 5 words w = (1,2,7), w' = (2,1,6), let their displayed Gram matrices be G,H. Then

```
U = [[1,0,0],
     [1,0,1],
     [0,1,0]],    det U = −1,    Uᵀ G U = H.
```

Directly,
`Q_w(x,y,z)=(y−x−z)²+(z−x)²+5x²`,
`Q_w'(x,y,z)=(z−y)²+(y−x)²+5x²`.
The substitution `(x,y,z) -> (x,x+z,y)` gives the claimed integral isometry. Their five slots are respectively `{1,2,7,1,6}` and `{2,1,6,1,11}`, so the first belongs to S₇ and the second does not. This is a rigorous counterexample to single-word S₇ membership being an invariant of the unmarked integral lattice.

The full command `uv run --with cypari2 python scripts/y7_class_test.py 150 4 7 8 11 5` also reproduces all class/mixed counts: 238/0,235/59,238/22,235/33,236/56. Examples for M = 5,8,11 are found as claimed. This does **not** prohibit counting markings, testing whether a class has some admissible marking, or using different lattices; the memo mostly acknowledges this scope correctly.

## Bottom line

Keep the finite covering theorem after the small-prime/oddness repairs, the exact identities and positivity proof, the lack of full T1 for 7, and the integral-isometry obstruction for single-word slice membership. Repair the false shot-family identification and M = 6 field, fix the split-norm population/test bookkeeping, commit the missing memo, and demote the probabilistic/asymptotic/proof-method exclusions to explicitly bounded evidence or conjectural assessment.

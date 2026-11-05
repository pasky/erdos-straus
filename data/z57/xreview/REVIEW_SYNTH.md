# Z57 SYNTH — cross-model hostile review

**Verdict: ACCEPT-WITH-FIXES. ES remains OPEN.**
Reviewed `side-agent/z57-synth` at `83c6f1dae2d8fa533cdc885b522d3ecba3a92e85`, not its uncommitted work.
The intended positive-modulus MS is correctly derived, suffices with the stated finite bridge, and is not refuted by the checked data.
There are no genuinely new positivity mechanisms here; the useful additions are numerical diagnostics and synthesis.

## Per-claim audit

| Claim | Classification | Independent check / restriction |
|---|---|---|
| MS and its equivalent divisor forms (§1.1) | CORRECT-WITH-FIX | Specify **positive** d (fix 1). The bijection and complementary-factor argument otherwise hold; no prime hypothesis is needed for the bijection. |
| MS + Mordell + Salez ⇒ ES | CORRECT relative to cited verification | Checked the certificate identity, prime-to-composite scaling, CRT survivors, and Salez's actual §§4.1–4.3, not merely its abstract. No uncovered interval. |
| Internal threshold 10¹⁰ suffices | CORRECT relative to prior censuses | Full R has only the 14 recorded zeros through 10¹⁰; the cited union census covers them. This does not assert R>0 below that threshold. |
| Proposition 1.1, ladder | CORRECT | Inclusion gives L4⇒L3⇒L2 and both parity arrows. L5⇒L3 requires M_G*>0 and ε>0. Theorem V with η/2 slack gives L6⇒R≥ηL²/2 only after p_V(η). |
| Lemma 1.2; threshold lower bounds | CORRECT | R is a nonnegative integer and X+M=R. Positive genus witnesses (1,158) at 564661441 and (1,62) at 8813281 checked; these support the stated ≥ endpoint convention. |
| “Minimal” / sufficient, not necessary | CORRECT as scoped Assessment | Full-family positivity is weaker than subfamily positivity. No strict separation of eventual statements, or converse ES⇒MS, is established. “Not necessary” must retain this proof-route meaning. |
| Lemma 2.1, numerator 8 | CORRECT | Substitute C=2C′; the common denominator gives numerator p+u+B=8uBC′. Doubling all three denominators gives 4/p. |
| Lemma E1 and Burgess interpretation | CORRECT in its stated scope | Completing the square gives μ²/(1+a)−δ(r)=(1+a)(1/r−2μ/(1+a))²/4. Equality requires the displayed r≥1. This is the worst-conductor expression, not a bound on true cancellation (fix 3). |
| Lemma E2 | CORRECT | Twice the rectangle μ/3 plus triangle 2μ²/3 gives 2μ/3+4μ²/3; x+y<1 is inactive in the claimed range. Quadrature rerun agrees. |
| Proposition E3 | CORRECT | Taking logarithms gives the strict sufficient inequality exactly. Integrality of R converts strict positivity to R≥1; it is not a necessary budget. |
| Assessment E4 | CORRECT as hypothetical model arithmetic | Kept-area/envelope calculation and both fitted-domain outputs reproduce. The universal crossover reading additionally assumes monotone fitted tails; it is not a lower bound on an actual proof threshold. |
| Lemma S1 | CORRECT | Individual López divisors lift exactly in class j=0. Multiplication of an odd number gives −1+4dΣj modulo 16d; coprimality ensures their product divides p+4d. A constant nonzero j never sums to 0 with odd multiplicity. |
| Lemma A.1 | CORRECT with positive moduli | Exact count bijection; reciprocity gives (k′/d)=1, and an even k forces d≡7 (8), hence (2/d)=1. Thus every hit is a Jacobi nonresidue and squares cannot hit. Mostly already FAMTRY Lemmas 1.1–1.4 (fix 2). |
| Proposition A.2 | CORRECT | p>max(D,g) makes the class a unit; p≡1 (8) excludes 2 as the least nonresidue; reciprocity transfers the odd nonresidue to (p/n_p). Contraposition of SMCR gives a hit. |
| Proposition A.3 | CORRECT relative to HCF T3.1 | A hit has c=4C≤d+1≤D+1 and d dividing cp+1. T3.1 with S={11}, R=2, Y=max(D,11), and p>D+1 excludes every such certificate while (p/11)=−1. Infinitely many p allow p>g. |
| A.3 complement / Remark A.4 | CORRECT in scope | 329617 is a full-family zero with least nonresidue 5; its first positive multiple ≡3 (4) is 3·329617. Finite-D obstruction gives no size-controlled obstruction. Bach is only a conditional input, not used for MS⇒ES. |
| “Narrowed; B2 did not move” | CORRECT | Concrete parity counterexamples and calibration sharpen diagnostics; neither supplies prescribed-prime positivity. No eventual target is disproved. |

## Core derivation and certified range

For d≥3, d≡3 (4), write r=(−n mod d), 1≤r<d, with r|(d+1)/4.
Then u=r, C=(d+1)/(4r), B=(n+r)/d are positive integers and 4uBC−u−B=n.
Conversely, a positive triple gives d=4uC−1 and 1≤u≤(d+1)/4<d, so the least residue recovers u uniquely.
Moreover d≤n+r≤n+(d+1)/4, hence **d≤(4n+1)/3**: the unbounded-looking count is finite.
The factorization (4uC−1)(4BC−1)=4Cn+1 gives the other divisor form, with both factors ≡−1 (4C).
The three denominators uBC, pBC, puC have reciprocal sum (p+u+B)/(puBC)=4/p.
For p=2 use (1,2,2); for p≡3 (4), put a=(p+1)/4 and use (a,2pa,2pa).
UPPER2 Prop 3.1 covers the remaining primes outside the six Mordell classes; its elementary words/CRT were checked.
Salez covers the smaller primes; MS covers precisely the remaining primes above 10¹⁷. The endpoint 10¹⁷ is not prime.
For any integer n≥2 choose a prime divisor p and multiply the three denominators for p by n/p.
Thus the implication is sound **relative to Salez's computational result**, not a fresh certification through 10¹⁷.
An unspecified eventual threshold still does not bridge the gap; Proposition 1.1 correctly retains p_V(η).

Primary source visited: https://arxiv.org/html/1406.6307v1 (§4.1 lists exactly the six residues; §4.3 reports
16,512,783,482,880 tested residual integers, including 51,732,427 squares, for N=10¹⁷).
The abstract was also checked at https://arxiv.org/abs/1406.6307. The 10¹⁸ report is not needed.

## Numerical audit

All shell runs used `ulimit -v 6000000`, a CPU ulimit, and explicit `timeout`; temporary outputs are in `/tmp/xrev_SYNTH/`.
Sources/data were extracted with `git archive` from the pinned commit. The reproducible supplemental audit is
`scripts/z57_xrev_synth_audit.py /tmp/xrev_SYNTH` (run via `uv run --with sympy python`).

- Recompiled/reran `z57_synth_tri.c 100000000 8`: **stdout and stderr byte-identical** to both committed files.
- Repeated with a saturation-abort guard: no prime p≡1 (4) reaches either uint16 cap, so R_odd=R−R8 is safe here.
- Recounted 14 R-zeros, 1270 R8-zeros, 423 R_odd-zeros; last values 8813281, 99671381, 99111841. All decade counts agree.
- Ran the independent SymPy divisor enumerator `z57_synth_check8.py` on **all twelve** high-range zeros: every R8=0 and every quoted R agrees (56,52,30,42,12,28,66,58,30,66,18,52 in increasing p order). All twelve pass primality checks.
- Exactly four of those twelve are in Mordell's classes: 10301993881, 10529331121, 10532106649, 10868474401; each has R>0. They refute the 10¹⁰ **R8** target, not MS at either threshold.
- Audited the high-range C engine's three disjoint cases P≤Q≤C, P≤C<Q, C<P≤Q and its early-exit witnesses. Did **not** repeat the full billion-integer interval: “exactly twelve” and 21,668,737 primes retain single-engine provenance.
- Recomputed genus masses for all seven uniform-bound violations and the closest Mordell prime using freshly compiled `z56_famdesign_mgen.c`; all eight agree to stored precision. No violation is Mordell-class.
- Recounted all 334 stored low-R cases: 249 Mordell cases, minimum normalized margin **0.00637190** at 72690361, mean M_gen/L² **0.11682271**. The other 326 genus sums were not re-enumerated.
- `z57_synth_pincer.py`, `z57_synth_zerofit8.py`, `z57_synth_zerofitm.py`: all outputs reproduce byte-for-byte. The margin-family enumeration itself was not rerun; its floating-point membership remains EVIDENCE-grade.
- `z57_synth_hitjacobi.py 200000`: **548725 classes, zero violations**, identical output. Supplemental direct triple/modulus enumerations agree for every n=1,…,1000, including even n, and verify the 4/n and 8/n identities exactly.
- Independently recomputed least prime nonresidues of the 14 and 38 stored zero sets: the quoted sets agree; all are <2log²p. The inherited full 10¹⁰ censuses were not rerun.
- Independently recounted the endpoint witnesses: R(8813281)=0; R(564661441)=2, its C=76141 pair (18,103) lies outside G*. Genus-positive pairs cited in §1.3 satisfy the exact local conditions.

## Novelty versus Z53–Z56

Read all four SUMMARY files and checked the pertinent underlying memos. The revised “prior in shape” disclaimer is right.
I: Z55_CROSSF §4 already fits enormous zero-tail crossovers (10¹²⁴); Z56_FAMDESIGN §4.4 compares family tails.
The new contribution is the specific Burgess-margin/envelope-versus-family-tail calibration, **not** explicit effectivity or a new method.
II: Z56_FAMATTACK §§3.2–3.3 already studies partitions, covariance, and joint emptiness; Z56_PRIMET1 has disjoint-ticket diagnostics.
The C-parity/numerator-8 split and its new scan are not in the checked Z53–Z56 memos; complementarity as a mechanism is old.
III: Z55_HCF T3.1/§3 already excludes fixed coverings even at least nonresidue 11; Z53_NONCRTLOGIC/FORESTCLASS precede it.
In particular **Z56_FAMTRY Lemmas 1.1–1.4 already contain the hit-modulus count, Jacobi obstruction, and MS residue criterion**.
A.3 is a clean corollary/repackaging of HCF, not a new growing-modulus theorem; no size-controlled variant is formulated here.

## Required fixes, in priority order

1. **MS domain (formal):** write `d≥3`, `d≡3 (mod 4)`, `r=(−p mod d)∈{1,…,d−1}` throughout, including FRONTIER export. “An integer d” alone admits negative moduli: if interpreted literally, d=−1 has least positive residue 1 dividing (d+1)/4=0, but reconstructs C=0. The intended positive-divisor convention repairs the statement completely; the upper bound (4p+1)/3 may also be included.
2. **Novelty attribution:** cite FAMTRY Lemmas 1.1–1.4 explicitly for A.1 and replace “new … growing-modulus (★)-specific statements” with “reformulations/corollaries of FAMTRY and HCF.” Do not advertise any of the three as a genuinely “not yet tried” mechanism. Keep novelty confined to the checked diagnostics.
3. **E1 export scope:** carry “for the worst allowed conductor in this single Burgess bound expression” into the summary/FRONTIER bullet. A conductor upper bound does not prevent stronger savings at smaller actual conductors, nor exclude another argument. The body already has the essential qualification.
4. **Range wording:** replace §0's “counterexamples above the certified range” by “C-even counterexamples above the internal 10¹⁰ full-(★) census range.” They are below Salez's 10¹⁷ ES range and do not refute MS.

After these fixes the narrowed verdict is justified. Retain all model/conditional labels and the finite-D and sampled-domain restrictions.
